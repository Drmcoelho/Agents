#!/usr/bin/env python3
import os, sys, subprocess, time, json
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "labs" / "02_mcp" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

PORT = int(os.getenv("MCP_PORT","8765"))
BASE = f"http://127.0.0.1:{PORT}"

def http_get(path):
    with urlopen(BASE+path) as r:
        return json.loads(r.read().decode("utf-8"))

def http_post(path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = Request(BASE+path, data=data, headers={"Content-Type":"application/json"})
    with urlopen(req) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    # start server
    server = subprocess.Popen([sys.executable, str(ROOT / "labs" / "02_mcp" / "server.py")])
    # wait for server
    ok=False
    for _ in range(30):
        try:
            health = http_get("/health")
            if health.get("ok"): ok=True; break
        except URLError:
            time.sleep(0.1)
    if not ok:
        server.terminate()
        raise SystemExit("server did not start")

    # call tools
    log = []
    log.append({"type":"health", "data": health})
    files = http_post("/tools/list_pdfs", {})
    log.append({"type":"list_pdfs", "data": files})
    # summarize first file
    first = files["files"][0]
    summ = http_post("/tools/summarize_pdf", {"path": f"labs/02_mcp/assets/pdfs/{first}", "max_words": 10})
    log.append({"type":"summarize_pdf", "data": summ})

    # write outputs
    out = OUT / "session.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for item in log:
            f.write(json.dumps(item, ensure_ascii=False)+"\n")

    # shutdown
    try:
        http_post("/shutdown", {})
    except Exception:
        pass
    server.wait(timeout=2)
    print(str(out))

if __name__ == "__main__":
    main()
