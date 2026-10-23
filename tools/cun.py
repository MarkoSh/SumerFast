"""Transliteration -> cuneiform (via OGSL value index) and -> a reading string for TTS."""
import json, re
SL = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'ogsl/ogsl-sl.json')))
SIGNS = SL['signs']
# own value -> sign index built from each sign's value list (the bundled 'index' maps some values to related signs)
INDEX, CONFLICTS = {}, {}
for _name, _s in SIGNS.items():
    if not isinstance(_s, dict) or not _s.get('utf8'): continue
    for _v in _s.get('values', []):
        if _v in INDEX and INDEX[_v] != _name: CONFLICTS.setdefault(_v, {INDEX[_v]}).add(_name)
        else: INDEX.setdefault(_v, _name)
SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
def norm(v):
    v = v.replace('ĝ', 'ŋ').replace('Ĝ', 'Ŋ').replace('ḫ', 'h').replace('Ḫ', 'H')
    v = re.sub(r'(\d+)$', lambda m: m.group(1).translate(SUB), v)
    return v
def sign_of(v):
    v = norm(v)
    name = INDEX.get(v) or INDEX.get(v.lower())
    if not name and re.match(r'^[A-ZŠŊḪ₀-₉]+$', v): name = v          # sign names written in caps
    if not name: return None
    s = SIGNS.get(name, {})
    return s.get('utf8')
def cuneiform(tr):
    """returns (cuneiform string, list of unknown parts)"""
    out, bad = [], []
    for word in tr.split():
        w = ''
        for part in re.split(r'(\{[^}]+\}|-|\.)', word):
            if not part or part in '-.': continue
            p = part.strip('{}').strip('[]⸢⸣!?#*')
            m = re.match(r'^(\d+)\((\w+)\)$', p)            # numbers like 2(DIŠ)
            if m: p = m.group(2)
            if p.startswith('m') and part == '{m}': continue  # personal-name marker is not written as a sign here
            u = sign_of(p)
            if u: w += u
            else: bad.append(p); w += f'⟨{p}⟩'  # no Unicode sign: show the reading instead of guessing
        out.append(w)
    return ' '.join(out), bad
def reading(tr):
    """reconstructed reading for a Turkish voice: ş = š, h = ḫ, ng = ĝ; determinatives are not pronounced"""
    t = re.sub(r'\{[^}]+\}', '', tr)
    t = re.sub(r'[₀-₉ₓ]', '', t).replace('.', '-')
    # CV-VC with the same vowel spell one syllable: na-an -> nan, mu-un -> mun, na-a -> na
    t = re.sub(r'([aeiu])-\1', r'\1', t).replace('-', '')
    t = t.replace('ĝ', 'ng').replace('ŋ', 'ng').replace('š', 'ş').replace('ḫ', 'h').replace('ř', 'dr')
    return re.sub(r'\s+', ' ', t).strip()
if __name__ == '__main__':
    for s in ['lugal ki-en-gi ki-uri', '{d}inana an gal-ta ki gal-še₃ ĝeštug₂-ga-ni na-an-gub', 'dub-sar eme-gir₁₅ nu-mu-un-zu-a a-na-am₃ nam-dub-sar-ra-ni', 'e₂-še₃ ga-ĝen-na saĝ a-ab-kal', 'lugal-ĝu₁₀-ra u₃-na-a-dug₄']:
        c, bad = cuneiform(s); print(s, '\n  ', c, bad, '\n  ', reading(s))
