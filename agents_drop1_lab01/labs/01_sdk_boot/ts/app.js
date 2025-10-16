// Minimal JS app (no external deps), offline-friendly
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const OUT = path.join(ROOT, '01_sdk_boot', 'outputs');
fs.mkdirSync(OUT, { recursive: true });

const backend = process.env.BACKEND || 'openai';
const offline = (process.env.OFFLINE || '1') === '1';

const chunks = [
  { type: 'start', backend, ts: Date.now()/1000 },
  { type: 'delta', text: 'Olá, ' },
  { type: 'delta', text: 'mundo!' },
  { type: 'end', ok: true, schema: { title: 'demo', fields: ['message','tokens'] } }
];

const result = {
  message: `Hello from ${backend} (offline=${offline}) [js]`,
  tokens: 11,
  file_ingest: { name: 'demo.txt', bytes: 42 }
};

const outPath = path.join(OUT, 'output-js.jsonl');
const lines = [...chunks, { type: 'result', data: result }].map(o => JSON.stringify(o)).join('\n');
fs.writeFileSync(outPath, lines, 'utf-8');
console.log(outPath);
