"""Fetch an ETCSL composite text + translation; print paragraphs with transliteration, glossed words and English."""
import re, html, sys, json, subprocess, os
UA = "Mozilla/5.0 (X11; Linux x86_64) Chrome/120 Safari/537.36"
def get(t):
    f = f'{t}.html'
    if not os.path.exists(f):
        subprocess.run(['curl', '-s', '-A', UA, '--max-time', '90', '-o', f, f'https://etcsl.orinst.ox.ac.uk/cgi-bin/etcsl.cgi?text={t}&display=Crit&charenc=gcirc'], check=True)
    return open(f, encoding='utf8', errors='replace').read()
def clean(x):
    x = re.sub(r'<sub>(\d+)</sub>', lambda m: ''.join('₀₁₂₃₄₅₆₇₈₉'[int(c)] for c in m.group(1)), x)
    x = re.sub(r'<sup>([^<]+)</sup>', r'{\1}', x)
    return html.unescape(re.sub(r'<[^>]+>', '', x)).strip()
def parse(code):
    c = get('c.' + code); t = get('t.' + code)
    lines = []
    for m in re.finditer(r"lineid=(t[\w.]+?\.p\d+)'>([^<]+)</a>.*?</td><td>(.*?)</td></tr>", c, re.S):
        pid, num, body = m.groups()
        words = [(clean(f), clean(g)) for g, f in re.findall(r"doTooltip\(event, '(.*?)'\)\" onMouseout=\"hideTip\(\)\">(.*?)</span>", body)]
        raw = clean(re.sub(r'<span class="note">.*?</span>', '', body))
        lines.append({'p': pid, 'n': num.strip('.'), 'tr': raw, 'w': words})
    trans = {}
    for m in re.finditer(r"<a name='(t[\w.]+?\.p\d+)'></a>(.*?)(?=<a name='t[\w.]+?\.p\d+'></a>|</body>)", t, re.S):
        trans[m.group(1)] = clean(m.group(2))
    return lines, trans
if __name__ == '__main__':
    code = sys.argv[1]
    lines, trans = parse(code)
    by = {}
    for l in lines: by.setdefault(l['p'], []).append(l)
    out = [{'p': p, 'lines': [{'n': l['n'], 'tr': l['tr'], 'w': l['w']} for l in ls], 'en': trans.get(p, '')} for p, ls in by.items()]
    json.dump(out, open(f'{code}.json', 'w'), ensure_ascii=False, indent=0)
    print(code, len(lines), 'lines,', len(out), 'paragraphs,', sum(1 for o in out if o['en']), 'translated')
