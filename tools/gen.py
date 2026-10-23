"""Generate SumerFast data.js from content.py: cuneiform via OGSL, readings, Cyrillic, audio map. Reports unknown signs."""
import json, re, sys
import content as C
from cun import cuneiform, reading, sign_of, SIGNS, INDEX, norm

UNKNOWN = {}
AUDIO = {'m': {}, 'f': {}}           # key -> text for the TTS voice
NARR = 'm'

def cun(tr):
    c, bad = cuneiform(tr)
    for b in bad: UNKNOWN.setdefault(b, tr)
    return c
CYR = [('ng', 'нг'), ('ş', 'ш'), ('h', 'х'), ('a', 'а'), ('b', 'б'), ('d', 'д'), ('e', 'э'), ('g', 'г'), ('i', 'и'), ('k', 'к'), ('l', 'л'), ('m', 'м'), ('n', 'н'),
       ('p', 'п'), ('r', 'р'), ('s', 'с'), ('t', 'т'), ('u', 'у'), ('z', 'з'), ('w', 'в'), ('y', 'й')]
def cyr(tr):
    t = reading(tr).lower()
    for a, b in CYR: t = t.replace(a, b)
    return re.sub(r'[a-z]', '', t)
def item(tr, voice=NARR, **kw):
    """standard item: th = cuneiform, lat = transliteration, cyr = Russian reading; audio keyed by both"""
    th = cun(tr)
    audio(th, tr, voice); audio(tr, tr, voice)
    d = {'th': th, 'lat': tr, 'cyr': cyr(tr), 'say': tr, 'np': 1}
    d.update(kw)
    return d
def audio(key, tr, voice=NARR):
    if key: AUDIO[voice][key] = reading(tr)

def same_sign(value, ref):
    a, b = INDEX.get(norm(value)), INDEX.get(norm(ref))
    return a is not None and a == b

out = {}
# ---------- phrases ----------
PH = []
for c_, tr, ru, en, tru, ten, src in C.PH:
    PH.append(item(tr, c=c_, ru=ru, en=en, tip=[f'{tru} · {src}', f'{ten} · {src}'], hero=c_ in C.HERO_FROM))
for icon, tr, ru, en, tru, ten in C.BILL:
    PH.append(item(tr, c='letter', bill=icon, ru=ru, en=en, tip=[tru, ten]))
out['CATS'] = [list(x) for x in C.CATS]
out['PH'] = PH
out['PARTICLE'] = {'m': {'th': '', 'lat': '', 'cyr': ''}, 'f': {'th': '', 'lat': '', 'cyr': ''}}

# ---------- sounds / conventions / homophones ----------
out['SOUNDS'] = [dict(item(ex), sym=sym, ru={'t': rt, 'd': rd_, 'w': rw}, en={'t': et, 'd': ed, 'w': ew}) for sym, ex, rt, rd_, rw, et, ed, ew in C.SOUNDS]
out['CONV'] = [dict(item(ex) if not ex.isupper() and '[' not in ex else {'th': cun(ex.strip('[]')), 'lat': ex, 'say': ex.strip('[]').lower(), 'np': 1}, mark=m, ru={'n': rt, 'd': rd_}, en={'n': et, 'd': ed}) for m, ex, rt, rd_, et, ed in C.CONV]
for x in out['CONV']: audio(x['th'], x['say']); audio(x['say'], x['say'])
ftr, fru, fen = C.FAMOUS
out['FAMOUS'] = dict(item(ftr), ru=fru, en=fen)
out['HOMO'] = [dict(item(tr), ru=ru, en=en) for tr, ru, en in C.HOMO]

# ---------- signs ----------
GRID = []
for v, cls, ru, en, also in C.GRID:
    name = INDEX.get(norm(v))
    th = cun(v)
    reads = [a for a in also.split() if a != v and same_sign(a, v)]
    dropped = [a for a in also.split() if a != v and not same_sign(a, v)]
    if dropped: print('  drop readings', v, dropped)
    GRID.append(dict(item(v), cls=cls, name=name, ru=ru or v, en=en or v, reads=reads, word=bool(ru)))
    for r in reads: audio(r, r)
out['GRID'] = GRID
out['CLS_COLOR'] = {'v': 'bg-accent', 'c': 'bg-zinc-500', 'l': 'bg-sky-400'}
SYL = []
for c_ in C.SYL_ROWS:
    cells = []
    for vw in 'aeiu':
        val = c_ + vw
        cells.append(item(val) if sign_of(val) else None)
    SYL.append({'c': c_ or '∅', 'cells': cells})
out['SYL'] = SYL
POLY = []
for sign, reads in [('ka', [('ka', 'рот', 'mouth'), ('inim', 'слово', 'word'), ('dug₄', 'говорить', 'speak'), ('zu₂', 'зуб', 'tooth'), ('gu₃', 'голос', 'voice'), ('kiri₃', 'нос', 'nose')]),
                    ('du', [('du', 'идти', 'go'), ('ĝen', 'идти', 'go'), ('gub', 'стоять', 'stand'), ('de₆', 'нести', 'carry'), ('tum₂', 'приносить', 'bring')]),
                    ('an', [('an', 'небо', 'sky'), ('diĝir', 'бог', 'god'), ('d', 'определитель «бог»', 'god determinative')]),
                    ('u₄', [('u₄', 'день', 'day'), ('babbar', 'белый', 'white'), ('utu', 'солнце', 'sun'), ('zalag', 'сиять', 'shine')]),
                    ('ni', [('ni', 'слог ni', 'syllable ni'), ('i₃', 'масло', 'oil'), ('ni₂', 'сам', 'self'), ('zal', 'проходить', 'pass')])]:
    ok = [(r, ru, en) for r, ru, en in reads if same_sign(r, sign)]
    bad = [r for r, *_ in reads if not same_sign(r, sign)]
    if bad: print('  poly drop', sign, bad)
    for r, *_ in ok: audio(r, r)
    POLY.append({'th': cun(sign), 'name': INDEX.get(norm(sign)), 'reads': [{'lat': r, 'ru': ru, 'en': en} for r, ru, en in ok]})
out['POLY'] = POLY

# ---------- numbers ----------
NN = C.NUM_NAMES
def num_sign(n):  # cuneiform for 1..59 within one sexagesimal place
    t, o = divmod(n, 10)
    s = ''
    if t: s += SIGNS[INDEX[f'{t}(u)']]['utf8']
    if o: s += SIGNS[INDEX[f'{o}(diš)']]['utf8']
    return s
def num_name_parts(n):
    t, o = divmod(n, 10); p = []
    if t: p.append(NN[t * 10])
    if o: p.append(NN[o])
    return p
for w in set(NN.values()): audio(w, w)
out['NUM'] = [dict(item(NN[k]), th=(num_sign(k) if k < 60 else SIGNS[INDEX['1(geš₂)']]['utf8']), ru=str(k), en=str(k)) for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60]]
for x in out['NUM']: audio(x['th'], x['lat'])
out['NUM_SIGN'] = {str(n): num_sign(n) for n in range(1, 60)}
out['NUM_PARTS'] = {str(n): num_name_parts(n) for n in range(1, 60)}
out['GESH'] = NN[60]

# ---------- body ----------
BODY = []
for tr, ru, en in C.BODY:
    my = f'{tr}-ĝu₁₀'
    d = item(tr, ru=ru, en=en); d['my'] = item(my); BODY.append(d)
out['BODY'] = BODY

# ---------- verbs ----------
VERB = []
for root, inf, past, may, let, en, enp in C.VERB:
    forms, tr = {}, {}
    for k, pre, *_ in C.MODALS:
        f = pre + root
        forms[k] = item(f)
    tr = {'none': [f'Он {past}', f'He {enp}'], 'not': [f'Он не {past}', f'He did not {en}'], 'may': [may.capitalize(), f'May he {en}'], 'let': [let.capitalize(), f'Let me {en}']}
    VERB.append(dict(item(root), ru=inf, en=en, forms=forms, tr=tr))
out['VERB'] = VERB
out['MODALS'] = [{'k': k, 'pre': pre, 'ru': ru, 'en': en, 'note': [nr, ne]} for k, pre, ru, en, nr, ne in C.MODALS]

# ---------- questions & cases ----------
out['QWORDS'] = [item(tr, ru=ru, en=en) for tr, ru, en in C.QWORDS]
QP = []
for suf, ru, en, ex, xru, xen in C.CASES:
    d = item(suf.strip('-'), ru=ru, en=en); d['lat'] = suf
    x = item(ex); d.update(xth=x['th'], xlat=ex, xru=xru, xen=xen)
    QP.append(d)
out['QPARTS'] = QP

# ---------- measures & ration builder ----------
out['CLS'] = [item(u, ru=ru, en=en) for u, ru, en in C.MEASURES]
out['ORDER'] = [item(tr, ru=ru, en=en, cls=u) for tr, ru, en, u in C.ORDER]
ORDER_PH = {}
for tr, ru, en, u in C.ORDER:
    for n in range(1, 6):
        lat = f'{n} {u} {tr}'
        th = num_sign(n) + ' ' + cun(u) + ' ' + cun(tr)
        speak = f'{NN[n]} {u} {tr}'
        AUDIO[NARR][th] = reading(speak)
        ORDER_PH[f'{tr}|{n}'] = {'th': th, 'lat': lat, 'cyr': cyr(speak)}
out['ORDER_PH'] = ORDER_PH
out['ORDER_N'] = [[n] for n in range(1, 6)]

# ---------- economy ----------
out['FOOD'] = [{'g': g, 'ru': ru, 'en': en, 'items': [item(tr, ru=r, en=e) for tr, r, e in items]} for g, ru, en, items in C.ECON]

# ---------- sentences ----------
out['SENT_TYPES'] = [{'k': k, 'ru': ru, 'en': en, 'note': [nr, ne]} for k, ru, en, nr, ne in C.SENT_TYPES]
out['ROLE_RU'] = {k: list(v) for k, v in C.ROLE.items()}
def slot(r, tr, j=0):
    d = {'r': r, 'th': cun(tr), 'lat': tr, 'cyr': cyr(tr)}
    if j: d['j'] = 1
    return d
SB = []
for ru, en, doer, erg, plerg, obj, root, impf, tr in C.SENT_BASES:
    pl_suf = {'sar': '-re-eš'}.get(root, '-uš')  # attested: mu-un-du₃-uš, mu-un-sar-re-eš
    slots = {
        'st': [slot('S', erg), slot('O', obj), slot('T', 'mu-un-'), slot('V', root, 1)],
        'neg': [slot('S', erg), slot('O', obj), slot('NEG', 'nu-'), slot('T', 'mu-un-', 1), slot('V', root, 1)],
        'may': [slot('S', erg), slot('O', obj), slot('M', 'ḫe₂-en-'), slot('V', root, 1)],
        'impf': [slot('S', erg), slot('O', obj), slot('T', 'i₃-'), slot('V', impf, 1)],
        'pl': [slot('S', plerg), slot('O', obj), slot('T', 'mu-un-'), slot('V', root, 1), slot('P', pl_suf, 1)],
        'wh': [slot('QW', 'a-ba-a'), slot('O', obj), slot('T', 'mu-un-'), slot('V', root, 1)],
    }
    texts = {}
    for k, ss in slots.items():
        lat = ''.join(('' if s.get('j') else ' ') + s['lat'] for s in ss).strip().replace('--', '-').replace('- ', '-')
        lat = re.sub(r'-(?=\s|$)', '', lat).replace(' -', '-')
        th = ' '.join(s['th'] for s in ss)
        AUDIO[NARR][th] = reading(lat)
        texts[k] = {'th': th, 'lat': lat, 'cyr': cyr(lat)}
    SB.append({'ru': ru, 'en': en, 'v': [cun(root)], 'slots': slots, 'texts': texts, 'tr': {k: list(v) for k, v in tr.items()}})
out['SENT_BASES'] = SB
out['SENT_RULES'] = [[ic, list(t), list(b)] for ic, t, b in C.SENT_RULES]

# ---------- names ----------
out['ANS_CATS'] = [list(x) for x in C.NAME_CATS]
out['ANS'] = [item(tr, v, c=c_, v=v, ru=ru, en=en, tip=[tr_, te]) for c_, v, tr, ru, en, tr_, te in C.NAMES]

# ---------- tablet scenes ----------
SC = []
for k, icon, ru, en, src, steps in C.SCENES:
    st = []
    for line, v, lru, len_, opts in steps:
        hint = next(((wr, we) for _, _, ok, wr, we in opts if not ok), (lru, len_))  # the hint explains, it doesn't give the answer away
        them = dict(item(line, v), v=v, ru=hint[0], en=hint[1])
        you = [{'th': '', 'lat': '', 'ru': a, 'en': b, **({'ok': 1} if ok else {'why': [wr, we]})} for a, b, ok, wr, we in opts]
        st.append({'them': them, 'you': you})
    SC.append({'k': k, 'icon': icon, 'ru': ru, 'en': en, 'src': src, 'steps': st})
out['SCENES'] = SC

# ---------- world ----------
out['ADDR'] = [dict(item(tr), ru=ru, en=en, call=call) for tr, ru, en, call in C.ROLES]
for r in C.ROLES: audio(r[3], r[3]); audio(cun(r[3]), r[3])
eg, eru, een, pairs = C.EMESAL
out['EMESAL'] = dict(item(eg), ru=eru, en=een, pairs=[{'eg': item(a), 'es': item(b), 'ru': ru, 'en': en} for a, b, ru, en in pairs])
out['SCHOOL'] = [[ic, ru, en, item(ex)] for ic, ru, en, ex in C.SCHOOL]
out['MYTHS'] = [list(x) for x in C.MYTHS]
out['WISDOM'] = [item(tr, ru=ru, en=en, tip=[src, src]) for tr, ru, en, src in C.WISDOM]

# ---------- determinatives & numerals ----------
SG = []
for det, look, ru, en, ex, xru, xen in C.DETS:
    x = item(ex)
    SG.append({'k': 'sign', 's': look, 'th': cun(det), 'lat': '{' + det + '}', 'cyr': '', 'ru': ru, 'en': en, 'say': ex, 'ex': x, 'xru': xru, 'xen': xen, 'np': 1})
for name, val in C.NUMERALS:
    w = NN[val] if val in NN else ''
    th = SIGNS[INDEX[name.lower()]]['utf8']; audio(w, w)
    SG.append({'k': 'tag', 's': 'yellow', 'th': th, 'lat': name.lower(), 'cyr': cyr(w), 'ru': f'{val} — {w}', 'en': f'{val} — {w}', 'say': w, 'np': 1})
out['SIGNS'] = SG
DET_OPT_RU = {'d': ('бог', 'god'), 'ki': ('место', 'place'), 'ĝiš': ('дерево', 'wood'), 'na₄': ('камень', 'stone'), 'id₂': ('река', 'river'), 'mušen': ('птица', 'bird'), 'ku₆': ('рыба', 'fish'), 'tug₂': ('ткань', 'cloth')}
out['DET_OPTS'] = [{'k': k, 'th': cun(k), 'lat': '{' + k + '}', 'ru': DET_OPT_RU[k][0], 'en': DET_OPT_RU[k][1]} for k in C.DET_OPTS]
out['DET_DRILL'] = [dict(item(w), k=re.search(r'\{([^}]+)\}', w).group(1)) for w in C.DET_DRILL]

# ---------- top verbs from ePSD2 ----------
lex = json.load(open('lex.json'))
verbs = sorted([e for e in lex if e['pos'] in ('V/t', 'V/i')], key=lambda e: -e['n'])
TOPV, rank = [], 0
for e in verbs:
    key = (e['cf'], e['gw'])
    if key not in C.TOPV_RU: continue
    forms = [f for f, n in e['forms'] if 'ₓ' not in f and '(' not in f and not re.search(r'[A-Z]', f)][:3]
    if not forms: continue
    rank += 1
    ru, en = C.TOPV_RU[key]
    top = forms[0]
    d = item(top, ru=ru, en=en)
    d.update(rank=rank, lat=e['cf'], cyr=cyr(top), forms=forms, gw=e['gw'], n=e['n'], xth='', xlat='', xru='', xen='')
    for f in forms: audio(f, f); audio(cun(f), f)
    TOPV.append(d)
out['TOPV'] = TOPV

# ---------- trace sets & alphabet pool ----------
out['TR_SYL'] = [{'g': g['th'], 'say': g['say'], 'lat': g['lat'], 'ru': g['ru'], 'en': g['en']} for g in GRID if g['cls'] in ('v', 'c')]
out['TR_LOG'] = [{'g': g['th'], 'say': g['say'], 'lat': g['lat'], 'ru': g['ru'], 'en': g['en']} for g in GRID if g['cls'] == 'l']
out['TR_NUM'] = [{'g': x['th'], 'say': x['say'], 'lat': x['lat'], 'ru': x['ru'], 'en': x['en']} for x in out['NUM']]

audio('lugal-e e₂ ḫe₂-en-du₃', 'lugal-e e₂ ḫe₂-en-du₃')

# ---------- tongue-twister block: no Sumerian tongue twisters survive, so the TU-TA-TI school drill stands in ----------
out['TWISTERS'] = [
    dict(item('tu ta ti tu-ta-ti'), ru='Строка 1 школьного упражнения TU-TA-TI', en='Line 1 of the TU-TA-TI school drill',
         tip=['Три слога по отдельности, потом они же слитно, как одно «слово». Ученик проговаривал строку вслух и писал её снова и снова.',
              'Three syllables one by one, then together as one “word”. Pupils said the line aloud and wrote it again and again.']),
    dict(item('nu na ni nu-na-ni'), ru='Строка 2: та же схема с согласной n', en='Line 2: the same pattern with n',
         tip=['Дальше упражнение шло так же по другим согласным. Так тренировали и письмо, и произношение слогов.',
              'The drill went on the same way through other consonants, training both writing and pronunciation.']),
]

# ---------- transliteration inside Russian tips and notes: tappable on the page ----------
TOKEN = r'[-{]*[a-zšĝḫŋ][a-zšĝḫŋ₀-₉ₓ{}-]*'
def ru_strings(v):
    if isinstance(v, str):
        if re.search('[а-яё]', v, re.I): yield v
    elif isinstance(v, dict): yield from (x for w in v.values() for x in ru_strings(w))
    elif isinstance(v, (list, tuple)): yield from (x for w in v for x in ru_strings(w))
ui = re.findall(r"'((?:[^'\\\n]|\\.)*)'", open('t.js', encoding='utf8').read())
for txt in list(ru_strings(out)) + [q for q in ui if re.search('[а-яё]', q, re.I)]:
    for tok in re.findall(TOKEN, re.sub(r'<[^>]*>', ' ', txt)):
        parts = [p.strip('{}') for p in re.split(r'(\{[^}]+\}|-)', tok) if p and p != '-']
        if tok != "x" and tok not in AUDIO[NARR] and parts and reading(tok) and all(sign_of(p) for p in parts): audio(tok, tok)

# ---------- write ----------
js = ['// GENERATED by gen.py from content.py — edit the content, not this file.']
js.append(open('t.js', encoding='utf8').read())
for k, v in out.items():
    js.append(f'const {k} = {json.dumps(v, ensure_ascii=False)};')
# transliteration -> cuneiform for the keyboard block (only words whose every sign is known)
KB_CUN = {}
for k in AUDIO[NARR]:
    if re.search(r'[\U00012000-\U0001254F]', k): continue
    c, bad = cuneiform(k)
    if c and not bad: KB_CUN[k] = c
js.append(f'const KB_CUN = {json.dumps(KB_CUN, ensure_ascii=False)};')

# EME: a cuneiform keyboard layout made up for this project (no standard one exists).
# Consonant on the key, vowel by modifier: plain a, Shift u, AltGr i, AltGr+Shift e.
EME_LAT = ['`1234567890-=\\', 'qwertyuiop[]', "asdfghjkl;'", 'zxcvbnm,./']
EME_VOW = ['a', 'u', 'i', 'e']
EME_CONS = {'b': 'b', 'd': 'd', 'g': 'g', 'j': 'ĝ', 'h': 'ḫ', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'r': 'r', 's': 's', 'c': 'š', 't': 't', 'z': 'z'}
EME_VC = {'[': 'n', ']': 'm', ';': 'r', "'": 'š', ',': 'b', '.': 'l', '/': 'k', '\\': 'd'}    # vowel + consonant
EME_WORDS = {'`': ['ĝiš', 'lu₂'], 'q': ['lugal', 'dumu', 'ama', 'nin'], 'w': ['e₂', 'uru', 'kur'],
             'y': ['dub', 'eme', 'nam', 'inana'], 'f': ['ninda', 'gud'], 'v': ['sila₃', 'gur', 'ma₂', 'sar'],
             'o': ['du₃', 'šum₂', 'gu₇', 'naĝ'], 'a': ['a'], 'u': ['u'], 'i': ['i'], 'e': ['e']}
SUBD = '₀₁₂₃₄₅₆₇₈₉'
def eme_value(v):
    """the lowest-numbered reading of v that is one sign: v, v₂, v₃ …"""
    for n in range(1, 30):
        r = v if n == 1 else v + ''.join(SUBD[int(d)] for d in str(n))
        u = sign_of(r)
        if u and len(u) == 1: return r, u
    return None, ''
EME_READ, EME_MISS, EME_AT = {}, [], {}
def eme_vals(ch):
    if ch in EME_CONS: return [EME_CONS[ch] + v for v in EME_VOW]
    if ch in EME_VC: return [v + EME_VC[ch] for v in EME_VOW]
    return (EME_WORDS.get(ch, []) + ['', '', '', ''])[:4]
# a sign has many readings: the key label and the reading under a typed sign come from the first placement,
# so plain syllables go first (b before p, m before ĝ: they share signs), then vowel+consonant, then words
ORDER = 'aiuebdgklmnrsczhpj' + ''.join(EME_VC) + ''.join(EME_WORDS)
KEYS = {ch: ['', '', '', ''] for lat in EME_LAT for ch in lat}
for ch in sorted(KEYS, key=lambda c: ORDER.index(c) if c in ORDER else 99):
    if ch.isdigit():
        n = int(ch) or 10
        KEYS[ch] = [num_sign(n), num_sign(n * 10) if 2 <= n <= 5 else '', '', '']
        for v, r in zip(KEYS[ch][:2], [n, n * 10]):
            if v: EME_READ.setdefault(v, str(r))
        continue
    for m, v in enumerate(eme_vals(ch)):
        if not v: continue
        r, u = eme_value(v)
        if not u: EME_MISS.append(v); continue
        if EME_AT.setdefault(u, ch) != ch: continue      # the sign already sits on another key
        EME_READ.setdefault(u, r); KEYS[ch][m] = u
eme_rows = [[lat] + [[KEYS[ch][m] for ch in lat] for m in range(4)] for lat in EME_LAT]
EME_EX = [KB_CUN[w] for w in ['lugal', 'e₂', 'ki-en-gi', 'dub-sar', 'dumu', 'nin', 'šu', 'a-ba-a'] if w in KB_CUN and all(c in EME_READ for c in KB_CUN[w])]
if EME_MISS: print('EME: no single sign for', EME_MISS)
EME_NUM = {num_sign(n): n for n in list(range(1, 11)) + [20, 30, 40, 50]}   # numeral sign -> value within one place
js.append(f'const KB_EME = {json.dumps({"rows": eme_rows, "read": EME_READ, "ex": EME_EX, "num": EME_NUM}, ensure_ascii=False)};')
js.append('// audio keys -> reconstructed reading (for tools/texts.js)')
js.append(f'const AUDIO = {json.dumps(AUDIO, ensure_ascii=False)};')
open('data.js', 'w', encoding='utf8').write('\n'.join(js) + '\n')
print('data.js written:', sum(len(v) for v in AUDIO.values()), 'audio keys,', len(PH), 'phrases,', len(GRID), 'grid signs,', len(TOPV), 'top verbs')
print('UNKNOWN signs:', json.dumps(UNKNOWN, ensure_ascii=False, indent=0))
