"""Keycap legends for the EME layout (made up for SumerFast): SVG files with the signs as outlines, sizes in mm.

  keycaps/eme-keycaps.svg   the whole layout on an ANSI board (cap outlines in the "guides" group)
  keycaps/keys/<code>.svg   one legend per 1u keycap top (12.7 mm)

Each cap: plain layer in the centre, Shift top right, AltGr bottom right, AltGr+Shift bottom left, Latin key top left —
the same as the keyboard on the site. Usage: python3 tools/keycaps.py (needs fontTools)."""
import json, os, re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'keycaps')
CUN = TTFont('/usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf')
LAT = TTFont('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')
EME = json.loads(re.search(r'const KB_EME = (\{.*\});', open(os.path.join(HERE, 'data.js'), encoding='utf8').read()).group(1))
CODE = {'`': 'Backquote', '-': 'Minus', '=': 'Equal', '[': 'BracketLeft', ']': 'BracketRight', '\\': 'Backslash',
        ';': 'Semicolon', "'": 'Quote', ',': 'Comma', '.': 'Period', '/': 'Slash'}
CAP, PITCH = 12.7, 19.05   # printable cap top and key spacing, mm

def glyph(font, text, cx, cy, em, box):
    """text as one outline, centred on (cx, cy): em mm high, shrunk to fit a box x box square"""
    gs, cmap, upm = font.getGlyphSet(), font.getBestCmap(), font['head'].unitsPerEm
    parts, x = [], 0
    for ch in text:
        name = cmap[ord(ch)]
        parts.append((name, x)); x += gs[name].width
    bounds = [None]
    def grow(r):
        bounds[0] = r if bounds[0] is None else (min(bounds[0][0], r[0]), min(bounds[0][1], r[1]), max(bounds[0][2], r[2]), max(bounds[0][3], r[3]))
    paths = []
    for name, dx in parts:
        p = BoundsPen(gs); gs[name].draw(p)
        if p.bounds: grow((p.bounds[0] + dx, p.bounds[1], p.bounds[2] + dx, p.bounds[3]))
        s = SVGPathPen(gs); gs[name].draw(s)
        paths.append(f'<path transform="translate({dx} 0)" d="{s.getCommands()}"/>')
    x0, y0, x1, y1 = bounds[0]
    k = min(em / upm, box / (x1 - x0), box / (y1 - y0))
    tx, ty = cx - (x0 + x1) / 2 * k, cy + (y0 + y1) / 2 * k
    return f'<g transform="translate({tx:.3f} {ty:.3f}) scale({k:.6f} {-k:.6f})">{"".join(paths)}</g>'

def legend(lat, layers):
    """legend group for one cap, origin at the top-left corner of the cap top"""
    g = [glyph(LAT, lat.upper(), 1.9, 1.9, 1.9, 1.6)]
    spots = [(6.35, 7.0, 7.0, 6.4), (10.5, 2.3, 3.6, 3.2), (10.5, 10.5, 3.6, 3.2), (2.3, 10.5, 3.6, 3.2)]
    for (cx, cy, em, box), sign in zip(spots, layers):
        if sign: g.append(glyph(CUN, sign, cx, cy, em, box))
    return ''.join(g)

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">'
            f'<title>{title}</title><desc>EME — a cuneiform keyboard layout made up for SumerFast (sumer.dateonymous.com), not a standard.</desc>{body}</svg>\n')

# ANSI rows as on the Machenike K500: (offset in units, keys); \ sits at the end of the QWERTY row, 1.5u
ROWS = [(0, '`1234567890-='), (1.5, 'qwertyuiop[]\\'), (1.75, "asdfghjkl;'"), (2.25, 'zxcvbnm,./')]
layer = {}
for lat, *ls in EME['rows']:
    for i, ch in enumerate(lat): layer[ch] = [l[i] for l in ls]

os.makedirs(os.path.join(OUT, 'keys'), exist_ok=True)
for ch, ls in layer.items():
    name = CODE.get(ch) or ('Digit' + ch if ch.isdigit() else 'Key' + ch.upper())
    open(os.path.join(OUT, 'keys', name + '.svg'), 'w').write(
        svg(CAP, CAP, f'<g fill="#000">{legend(ch, ls)}</g>', f'EME keycap {name}'))

pad, guides, legends = 4, [], []
for r, (off, keys) in enumerate(ROWS):
    for i, ch in enumerate(keys):
        wide = 1.5 if ch == '\\' else 1
        x, y = pad + (off + i) * PITCH, pad + r * PITCH
        guides.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{PITCH * wide - 1:.2f}" height="{PITCH - 1:.2f}" rx="1.6"/>')
        cx = x + (PITCH * wide - 1) / 2 - CAP / 2
        legends.append(f'<g transform="translate({cx:.2f} {y + (PITCH - 1 - CAP) / 2:.2f})">{legend(ch, layer[ch])}</g>')
W, H = pad * 2 + 15 * PITCH, pad * 2 + 4 * PITCH
open(os.path.join(OUT, 'eme-keycaps.svg'), 'w').write(svg(f'{W:.1f}', f'{H:.1f}',
    f'<g id="guides" fill="none" stroke="#999" stroke-width=".25">{"".join(guides)}</g><g id="legends" fill="#000">{"".join(legends)}</g>',
    'EME keycaps'))
print('written', len(layer), 'keys to', os.path.normpath(OUT))
