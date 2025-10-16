#!/usr/bin/env python3
import os, json, time, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "labs" / "01_sdk_boot" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

backend = os.getenv("BACKEND","openai")
offline = os.getenv("OFFLINE","1") == "1"

# Simulated streaming chunks
chunks = [
    {"type":"start","backend": backend, "ts": time.time()},
    {"type":"delta","text":"Olá, "},
    {"type":"delta","text":"mundo!"},
    {"type":"end","ok": True, "schema":{"title":"demo","fields":["message","tokens"]}}
]

# Simulated structured output
result = {
    "message": f"Hello from {backend} (offline={offline})",
    "tokens": 12,
    "file_ingest": {"name":"demo.txt","bytes": 42}
}

with open(OUT / "output.jsonl","w", encoding="utf-8") as f:
    for c in chunks:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
    f.write(json.dumps({"type":"result","data":result}, ensure_ascii=False) + "\n")

print(str(OUT / "output.jsonl"))
