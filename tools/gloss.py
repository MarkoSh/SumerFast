"""Stream ePSD2 gloss-sux.json -> compact lexicon (cf, gw, pos, icount, top forms)."""
import ijson, json, zipfile, sys
out = []
with zipfile.ZipFile('epsd2.zip') as z, z.open('epsd2/gloss-sux.json') as f:
    for e in ijson.items(f, 'entries.item'):
        forms = sorted(((fm.get('n') or fm.get('form'), int(fm.get('icount', 0) or 0)) for fm in e.get('forms', []) if fm.get('n') or fm.get('form')), key=lambda x: -x[1])[:6]
        senses = [s.get('mng') for s in e.get('senses', []) if s.get('mng')][:4]
        out.append({'cf': e.get('cf'), 'gw': e.get('gw'), 'pos': e.get('pos'), 'n': int(e.get('icount', 0) or 0), 'forms': forms, 'senses': senses})
json.dump(out, open('lex.json', 'w'), ensure_ascii=False)
print(len(out), 'entries')
