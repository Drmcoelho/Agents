#!/usr/bin/env python3
import json, os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "labs" / "02_mcp" / "assets" / "pdfs"

def summarize_text(text, max_words):
    words = text.split()
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words])

class H(BaseHTTPRequestHandler):
    def _json(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path == "/health":
            return self._json(200, {"ok": True})
        return self._json(404, {"error":"not found"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length","0"))
        body = self.rfile.read(length).decode("utf-8") if length>0 else "{}"
        try:
            data = json.loads(body or "{}")
        except:
            data = {}
        if self.path == "/tools/list_pdfs":
            files = sorted([p.name for p in ASSETS.iterdir() if p.is_file()])
            return self._json(200, {"files": files})
        if self.path == "/tools/summarize_pdf":
            path = data.get("path")
            max_words = int(data.get("max_words", 40))
            if not path:
                return self._json(400, {"error":"path required"})
            fp = ROOT / path
            if not fp.exists() or not fp.is_file():
                return self._json(404, {"error":"file not found"})
            text = fp.read_text(encoding="utf-8", errors="ignore")
            return self._json(200, {"summary": summarize_text(text, max_words)})
        if self.path == "/shutdown":
            self._json(200, {"ok": True})
            # shutdown server gracefully
            def stopper(httpd):
                httpd.shutdown()
            import threading
            threading.Thread(target=stopper, args=(self.server,), daemon=True).start()
            return
        return self._json(404, {"error":"not found"})

def main():
    port = int(os.getenv("MCP_PORT","8765"))
    httpd = HTTPServer(("127.0.0.1", port), H)
    print(f"[mcp-stub] serving on http://127.0.0.1:{port}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
