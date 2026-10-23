// Prints {voice: {audioKey: readingForTTS}} for every string the page can speak (precomputed by gen.py).
// Usage: node tools/texts.js > texts.json
const src = require('fs').readFileSync(__dirname + '/../index.html', 'utf8');
const m = src.match(/const AUDIO = (\{.*\});/);
console.log(m[1]);
