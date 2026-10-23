"""Generate audio/<m|f>/<fnv1a(key)>.mp3: each key is spoken as its reconstructed reading by a Turkish neural voice
(Turkish spelling reads Sumerian transliteration almost letter by letter: pure a e i u, ş = š, h ≈ ḫ, stress near the end).
Needs: pip install edge-tts.  Usage: node tools/texts.js > /tmp/t.json && python tools/gen_audio.py /tmp/t.json"""
import asyncio, json, os, sys
import edge_tts

VOICES = {'m': 'tr-TR-AhmetNeural', 'f': 'tr-TR-EmelNeural'}
RATE = '-20%'  # slow: learners and a reconstructed language
ROOT = os.path.join(os.path.dirname(__file__), '..', 'audio')

def fnv(s):
    h = 0x811c9dc5
    for b in s.encode('utf8'):
        h = ((h ^ b) * 0x01000193) & 0xffffffff
    return f'{h:08x}'

async def main(path):
    data = json.load(open(path, encoding='utf8'))
    sem, jobs = asyncio.Semaphore(8), []
    for g, items in data.items():
        os.makedirs(os.path.join(ROOT, g), exist_ok=True)
        for key, text in items.items():
            out = os.path.join(ROOT, g, fnv(key) + '.mp3')
            if text and not os.path.exists(out): jobs.append((g, text, out))
    print(len(jobs), 'files to generate')
    async def one(g, t, out):
        async with sem:
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(t, VOICES[g], rate=RATE).save(out); return
                except Exception as e:
                    if attempt == 2: print('FAIL', g, t, e)
                    await asyncio.sleep(2)
    await asyncio.gather(*(one(*j) for j in jobs))

asyncio.run(main(sys.argv[1]))
