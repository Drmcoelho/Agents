import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "labs" / "01_sdk_boot" / "outputs"

def test_python_output_exists():
    p = OUT / "output.jsonl"
    assert p.exists(), "output.jsonl não foi gerado pelo app.py"

def test_js_output_exists():
    p = OUT / "output-js.jsonl"
    assert p.exists(), "output-js.jsonl não foi gerado pelo app.js"

def test_schema_and_result():
    p = OUT / "output.jsonl"
    data = [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines()]
    assert any(x.get("type")=="end" for x in data), "faltou chunk end"
    res = [x for x in data if x.get("type")=="result"]
    assert res, "faltou result"
    r = res[0]["data"]
    assert {"message","tokens","file_ingest"} <= set(r.keys()), "schema de result inesperado"
