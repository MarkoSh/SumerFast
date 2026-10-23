"""Build SumerFast/index.html from ThaiFast/index.html: same design and engine, Sumerian content (RU/EN UI, no He/She).
Content: tools/content.py -> tools/gen.py -> tools/data.js. Usage: python3 tools/gen.py && python3 tools/build.py"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
SRC = os.path.join(HERE, '../../ThaiFast/index.html')
DST = os.path.join(HERE, '../index.html')
s = open(SRC, encoding='utf8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, f'expected {n}, found {c}: {a[:90]!r}'
    s = s.replace(a, b)
def func(name, new):
    global s
    i = s.index(f'function {name}(')
    j = s.index('\n}\n', i) + 3
    s = s[:i] + new.strip('\n') + '\n' + s[j:]
def between(a, b, new):
    global s
    i = s.index(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]

# ---------- head ----------
rep('<title>ThaiFast — тайский с нуля</title>', '<title>SumerFast — шумерский язык и клинопись</title>')
rep('content="Тайский язык с нуля: звуки, тоны, алфавит, цифры, нужные фразы и быстрые тренажёры."', 'content="Шумерский язык с нуля: клинопись, транслитерация, грамматика и строки с настоящих табличек. Sumerian from scratch: cuneiform, grammar and real tablets."')
s = re.sub(r'<link href="https://fonts.googleapis.com/css2\?[^"]+" rel="stylesheet">',
           '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Cuneiform&display=swap" rel="stylesheet">', s, count=1)
rep("fontFamily: { sans: ['Inter', 'Noto Sans Thai', 'system-ui', 'sans-serif'], thai: ['Noto Sans Thai', 'sans-serif'], loop: ['Noto Sans Thai Looped', 'Noto Sans Thai', 'sans-serif'] },",
    "fontFamily: { sans: ['Inter', 'Noto Sans Cuneiform', 'system-ui', 'sans-serif'], thai: ['Inter', 'Noto Sans Cuneiform', 'system-ui', 'sans-serif'], loop: ['Noto Sans Cuneiform', 'Inter', 'sans-serif'] },")

# ---------- nav: keep RU/EN, drop He/She ----------
i = s.index('      <div class="flex rounded-lg border border-white/10 p-0.5 text-xs font-semibold" role="group" aria-label="Gender">')
j = s.index('</div>', i) + len('</div>\n')
s = s[:i] + s[j:]
s = s.replace('ThaiFast', 'SumerFast')

# keyboard block: ATF conventions instead of a national layout; cuneiform shown for words the course knows
between('// Kedmanee, the standard Thai layout.', 'const KB_CODE =', r"""// No cuneiform layout exists. ATF: transliteration in Latin letters, as in ORACC and ETCSL.
// EME: a cuneiform layout made up for this project (built by gen.py from OGSL, see KB_EME).
const KB_EX = ['lugal', 'ĝiš', 'šu', 'dub-sar', 'e₂', 'diĝir'];
const KB_ACC = { 'á': 'a2', 'é': 'e2', 'í': 'i2', 'ú': 'u2', 'à': 'a3', 'è': 'e3', 'ì': 'i3', 'ù': 'u3' };
const atfConv = s => s.replace(/sz/g, 'š').replace(/S[zZ]/g, 'Š').replace(/s,/g, 'ṣ').replace(/S,/g, 'Ṣ').replace(/t,/g, 'ṭ').replace(/T,/g, 'Ṭ')
  .replace(/j/g, 'ĝ').replace(/J/g, 'Ĝ').replace(/h/g, 'ḫ').replace(/H/g, 'Ḫ')
  .replace(/([a-zA-ZšĝḫṣṭŠĜḪṢṬ₀-₉])([0-9])/g, (m, a, d) => a + '₀₁₂₃₄₅₆₇₈₉'[d]).replace(/([₀-₉])([0-9])/g, (m, a, d) => a + '₀₁₂₃₄₅₆₇₈₉'[d]);
const atfKeys = s => s.replace(/[áéíúàèìù]/g, c => KB_ACC[c]).replace(/š/g, 'sz').replace(/Š/g, 'SZ').replace(/ṣ/g, 's,').replace(/Ṣ/g, 'S,').replace(/ṭ/g, 't,').replace(/Ṭ/g, 'T,')
  .replace(/[ĝŋ]/g, 'j').replace(/[ĜŊ]/g, 'J').replace(/ḫ/g, 'h').replace(/Ḫ/g, 'H').replace(/[₀-₉]/g, c => '₀₁₂₃₄₅₆₇₈₉'.indexOf(c));
// typed signs -> transliteration: signs of a word joined by hyphens
const emeTr = v => v.split(/\s+/).filter(Boolean).map(w => [...w].map(c => KB_EME.read[c] || '?').join('-')).join(' ');
// numbers are sexagesimal: each space-separated group of numeral signs is one place (0–59)
const emeNum = v => {
  const g = v.split(/\s+/).filter(Boolean).map(w => [...w].reduce((s, c) => s + (KB_EME.num[c] ?? NaN), 0));
  if (!g.length || g.some(x => !(x <= 59))) return '';
  const n = g.reduce((a, x) => a * 60 + x, 0);
  return g.length < 2 ? `= ${n}` : g.map((x, i) => x + (g.length - 1 - i ? ` × ${60 ** (g.length - 1 - i)}` : '')).join(' + ') + ` = ${n}`;
};
const kbCun = c => c ? `<p class="mt-5 font-thai text-5xl text-white">${esc(c)}</p>` : '';
const KB_SETS = [{
  name: ['ATF · латиница', 'ATF · Latin'], ph: 'kbPh', note: 'kbNote', ex: KB_EX,
  rows: [
    ['`1234567890-=\\', '`1234567890-=\\', '~!@#$%^&*()_+|'],
    ['qwertyuiop[]', 'qwertyuiop[]', 'QWERTYUIOP{}'],
    ["asdfghjkl;'", "asdfghjkl;'", 'ASDFGHJKL:"'],
    ['zxcvbnm,./', 'zxcvbnm,./', 'ZXCVBNM<>?'],
  ],
  hint: { s: 'š', j: 'ĝ', h: 'ḫ', ',': 'ṣ ṭ', 0: '₀', 1: '₁', 2: '₂', 3: '₃', 4: '₄', 5: '₅', 6: '₆', 7: '₇', 8: '₈', 9: '₉' },
  conv: atfConv, keys: ch => [...atfKeys(ch)], read: null,
  say: v => AUDIO[gender][v] ? v : '',
  out: v => kbCun(KB_CUN[v]),
}, {
  name: ['EME · клинопись', 'EME · cuneiform'], ph: 'kbPhEme', note: 'kbNoteEme', ex: KB_EME.ex,
  rows: KB_EME.rows, hint: {},
  conv: s => s, keys: ch => [ch], read: ch => KB_EME.read[ch] || '',
  say: v => AUDIO[gender][emeTr(v)] ? emeTr(v) : '',
  out: v => { const n = emeNum(v); return !v ? '' : n ? `<p class="mt-4 font-mono text-lg text-accent">${esc(n)}</p>` : `<p class="mt-4 font-mono text-lg text-accent">${esc(emeTr(v))}</p>` },
}];
""")

# tappable words in tips: transliteration that has audio (in English text only words with a Sumerian marker)
assert s.count('const SAY_RUN = ') == 1
s = re.sub(r'^const SAY_RUN = .*$', lambda m: "const SAY_RUN = /(?<![A-Za-z0-9])[-{]*[a-zšĝḫŋ][a-zšĝḫŋ₀-₉ₓ{}-]*(?![A-Za-z0-9])/g, SAY_HAS = /[a-zšĝḫŋ]/, SAY_OTHER = /\\s/, SAY_OK = m => AUDIO[gender][m] && (lang === 'ru' || /[-šĝḫŋ₀-₉{}]/.test(m));", s, flags=re.M)
rep('// Thai words inside notes and tips become tappable: only text that mixes Thai with Latin/Cyrillic,', '// Sumerian words inside notes and tips become tappable (only those with audio),')

# ---------- static html ----------
rep('<dt class="text-2xl font-bold text-white">44</dt>', '<dt class="text-2xl font-bold text-white">58</dt>')
rep('<p class="mt-2 font-thai text-3xl text-white">ไม้ใหม่ไม่ไหม้ไหม</p>', '<p id="famTh" class="mt-2 font-thai text-3xl text-white leading-relaxed"></p>')
rep('<p class="mt-1 font-mono text-accent">mái mài mâi mâi mǎi</p>', '<p id="famLat" class="mt-1 font-mono text-accent"></p>')
rep('<p class="mt-1 text-sm text-zinc-400" data-i18n="twisterTr"></p>', '<p id="famTr" class="mt-1 text-sm text-zinc-400"></p>')
rep('<button data-say="ไม้ใหม่ไม่ไหม้ไหม"', '<button id="famPlay" data-say=""')
rep('''    </div>
  </section>

  <!-- 03 ALPHABET -->''', '''      <div class="reveal mt-12">
        <h3 class="text-xl font-bold text-white" data-i18n="homoTitle"></h3>
        <p class="mt-2 text-sm text-zinc-400 max-w-2xl" data-i18n="homoSub"></p>
        <div id="homoGrid" class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3"></div>
      </div>
    </div>
  </section>

  <!-- 03 ALPHABET -->''')
rep('<input id="numIn" type="number" min="0" max="99999" value="250"', '<input id="numIn" type="number" min="1" max="3599" value="75"')
rep('          <button data-tab="speak" class="tab px-4 py-2.5 rounded-xl flex items-center gap-2 transition"><i data-lucide="mic" class="w-4 h-4"></i><span data-i18n="tabSpeak"></span></button>\n', '')
rep('<p class="font-thai text-5xl md:text-7xl font-bold text-white">โชคดี<span class="text-accent" data-particle></span></p>', '<p class="font-thai text-5xl md:text-7xl font-bold text-white">𒈗𒂠 𒂍 𒃶𒂗𒆕</p>')
rep('<p class="mt-4 font-mono text-accent">chôhk-dii</p>', '<button data-say="lugal-e e₂ ḫe₂-en-du₃" class="mt-4 inline-flex items-center gap-2 font-mono text-accent hover:text-white transition"><i data-lucide="volume-2" class="w-4 h-4"></i>lugal-e e₂ ḫe₂-en-du₃</button>')

# ---------- data ----------
between('/* ================= UI TEXT ================= */', '/* ================= STATE ================= */',
        open(HERE + 'data.js', encoding='utf8').read() + '''
// engine glue for the shared sentence builder
const SENT_JOIN = ' ', SENT_END = {}, SENT_PH = {};
const sentSlots = (k, b) => SENT_BASES[b].slots[k];
const sentText = (k, b) => SENT_BASES[b].texts[k].th;

''')

# ---------- state & speech ----------
rep("let gender = store.get('tf-gender', 'm');", "const gender = 'm'; // narrator voice")
func('ttsFallback', '''
function ttsFallback(text, done) {
  // no browser voice can read Sumerian: missing audio stays silent
  console.warn('no audio for', text); done();
}''')
rep("function speak(text, btn, voice, onEnd) {\n  const id = ++playId, parts = text.split('|');", "function speak(text, btn, voice, onEnd) {\n  if (!text) { onEnd?.(); return }\n  const id = ++playId, parts = text.split('|');")
rep("  $$('[data-particle]').forEach(el => el.textContent = pt().th);\n", "")

func('renderTones', r'''
function renderTones() {
  $('#tonesGrid').innerHTML = CONV.map(x => `
    <button data-say="${x.say}" class="flex flex-col text-left rounded-2xl border border-white/10 bg-ink-950 p-4 hover:border-accent/50 transition">
      <span class="font-mono text-2xl font-bold text-accent">${x.mark}</span>
      <span class="mt-3 font-semibold text-white">${x[lang].n}</span>
      <p class="mt-1 text-xs text-zinc-500 leading-relaxed">${x[lang].d}</p>
      <div class="mt-auto pt-3 border-t border-white/5"><span class="font-thai text-xl text-white">${x.th}</span> <span class="font-mono text-sm text-zinc-400">${x.lat}</span></div>
    </button>`).join('');
  $('#famTh').textContent = FAMOUS.th; $('#famLat').textContent = FAMOUS.lat; $('#famTr').textContent = FAMOUS[lang];
  $('#famPlay').dataset.say = FAMOUS.say;
  $('#homoGrid').innerHTML = HOMO.map(x => `<button data-say="${x.say}" class="text-left rounded-2xl border border-white/10 bg-ink-950 p-4 hover:border-accent/50 transition">
    <span class="font-thai text-3xl text-white">${x.th}</span>
    <span class="block mt-2 font-mono text-lg text-accent">${x.lat.replace(/([₀-₉]+)/, '<b class="text-white">$1</b>')}</span>
    <span class="block text-sm text-zinc-400">${x[lang]}</span></button>`).join('');
}''')

func('renderAlphabet', r'''
function renderAlphabet() {
  $('#classTabs').innerHTML = [['all', 'clsAll'], ['v', 'clsV'], ['c', 'clsC'], ['l', 'clsL']].map(([k, key]) =>
    `<button data-cls="${k}" class="${chip(cls === k)}">${k !== 'all' ? `<span class="w-2 h-2 rounded-full ${CLS_COLOR[k]}"></span>` : ''}${t(key)}</button>`).join('');
  $('#consGrid').innerHTML = GRID.map((c, i) => {
    const dim = cls !== 'all' && c.cls !== cls ? 'opacity-20' : '';
    return `<button data-cons="${i}" class="relative aspect-square rounded-xl border ${i === selCons ? 'border-accent bg-accent/10' : 'border-white/10 bg-ink-900 hover:border-white/30'} transition grid place-items-center ${dim}">
      <span class="absolute top-1.5 left-1.5 w-1.5 h-1.5 rounded-full ${CLS_COLOR[c.cls]}"></span>
      <span class="font-loop text-2xl md:text-3xl text-white leading-none">${c.th}</span>
      <span class="absolute bottom-1 inset-x-0 text-center font-mono text-[10px] text-zinc-500">${c.lat}</span>
    </button>`;
  }).join('');
  const c = GRID[selCons];
  $('#consDetail').innerHTML = `<div class="fade-up">
    <div class="flex items-start justify-between"><span class="font-loop text-7xl text-white leading-none">${c.th}</span>${playBtn(c.say, 'w-12 h-12')}</div>
    <p class="mt-5 font-mono text-2xl text-accent">${c.lat}</p>
    ${c.word ? `<p class="text-lg text-white">${c[lang]}</p>` : ''}
    <dl class="mt-5 space-y-3 text-sm border-t border-white/5 pt-5">
      <div class="flex justify-between gap-4"><dt class="text-zinc-500">${t('signName')}</dt><dd class="font-mono text-white">${c.name}</dd></div>
      ${c.reads.length ? `<div class="flex justify-between gap-4"><dt class="text-zinc-500 shrink-0">${t('signReads')}</dt><dd class="flex flex-wrap justify-end gap-1.5">${c.reads.map(r => `<button data-say="${r}" class="rounded-full border border-white/10 px-2 py-0.5 font-mono text-xs text-accent hover:border-accent transition">${r}</button>`).join('')}</dd></div>` : ''}
    </dl>
    <p class="mt-5 flex items-start gap-2 text-xs text-zinc-400"><span class="mt-1 w-2 h-2 shrink-0 rounded-full ${CLS_COLOR[c.cls]}"></span>${t('cls' + c.cls.toUpperCase() + 'd')}</p>
  </div>`;
  $('#vowelGrid').innerHTML = POLY.map(p => `<div class="rounded-xl border border-white/10 bg-ink-900 p-4 col-span-3 sm:col-span-5 lg:col-span-4">
    <div class="flex items-center gap-3"><span class="font-loop text-4xl text-white">${p.th}</span><span class="font-mono text-xs text-zinc-500">${p.name}</span></div>
    <div class="mt-3 flex flex-wrap gap-1.5">${p.reads.map(r => `<button data-say="${r.lat}" class="rounded-lg border border-white/10 bg-ink-950 px-2.5 py-1.5 text-left hover:border-accent/50 transition"><span class="font-mono text-sm text-accent">${r.lat}</span> <span class="text-xs text-zinc-400">${L(r.ru, r.en)}</span></button>`).join('')}</div></div>`).join('');
}''')
rep("  const c = CONS[selCons]; speak(c.ch + ' ' + c.word);", "  speak(GRID[selCons].say);")

func('renderPoster', r'''
function renderPoster() {
  $$('[data-pfont]').forEach(b => b.className = `px-3 py-1.5 rounded-md transition ${b.dataset.pfont === pfont ? 'bg-white text-ink-950' : 'text-zinc-400 hover:text-white'}`);
  const cun = pfont === 'loop';
  const head = (n, key, note = '') => `<div class="mt-8 first:mt-0 flex flex-wrap items-baseline gap-x-3 gap-y-1"><span class="font-mono text-2xl font-bold text-accent">${n}</span><span class="text-sm font-semibold text-white">${t(key)}</span>${note ? `<span class="text-xs text-zinc-500">${t(note)}</span>` : ''}</div>`;
  const cell = (x, sub) => x ? `<button data-say="${x.say}" class="group rounded-xl border border-white/5 bg-ink-950 hover:border-accent/50 hover:-translate-y-0.5 transition pt-1 pb-2 px-1 text-center"><span class="flex h-14 md:h-16 items-center justify-center ${cun ? 'font-loop text-2xl md:text-3xl' : 'font-mono text-lg'} leading-none text-white group-hover:text-accent transition">${cun ? x.th : x.lat}</span><span class="block font-mono text-[11px] leading-tight text-zinc-500 truncate">${sub ?? (cun ? x.lat : '')}</span></button>` : '<div class="rounded-xl border border-dashed border-white/5"></div>';
  $('#poster').innerHTML =
    head(SYL.reduce((n, r) => n + r.cells.filter(Boolean).length, 0), 'pSyl', 'pSylNote') +
    `<div class="mt-3 grid grid-cols-[2.5rem_repeat(4,minmax(0,1fr))] gap-1.5 max-w-xl">
      <div></div>${['a', 'e', 'i', 'u'].map(v => `<div class="text-center font-mono text-sm text-accent">${v}</div>`).join('')}
      ${SYL.map(r => `<div class="grid place-items-center font-mono text-sm text-accent">${r.c}</div>${r.cells.map(x => cell(x)).join('')}`).join('')}
    </div>` +
    head(GRID.filter(g => g.cls === 'l').length, 'pLog', 'pLogNote') +
    `<div class="mt-3 grid grid-cols-3 sm:grid-cols-5 lg:grid-cols-8 gap-1.5">${GRID.filter(g => g.cls === 'l').map(g => cell(g, `${g.lat} · ${g[lang]}`)).join('')}</div>` +
    head(NUM.length, 'pNum', 'pNumNote') +
    `<div class="mt-3 grid grid-cols-5 sm:grid-cols-8 lg:grid-cols-[repeat(15,minmax(0,1fr))] gap-1.5">${NUM.map(x => cell(x, `${x.ru} · ${x.lat}`)).join('')}</div>`;
}''')

func('renderNum', r'''
function renderNum() {
  const inp = $('#numIn');
  const n = Math.max(1, Math.min(3599, parseInt(inp.value, 10) || 1));
  const g = n / 60 | 0, r = n % 60;
  const parts = [...(g ? [GESH, ...(g > 1 ? NUM_PARTS[g] : [])] : []), ...(r ? NUM_PARTS[r] : [])];
  const signs = [g ? NUM_SIGN[g] : '', r ? NUM_SIGN[r] : ''].filter(Boolean).join(' ');
  $('#numOut').innerHTML = `<div class="fade-up">
    <div class="flex items-center gap-4"><span class="font-mono text-4xl font-bold text-white">${n}</span><span class="font-loop text-4xl text-white">${signs}</span><span class="ml-auto">${playBtn(parts.join('|'), 'w-12 h-12')}</span></div>
    <p class="mt-3 font-mono text-sm text-zinc-500">${g ? `${g} × 60 + ${r}` : ''}</p>
    <p class="mt-2 font-mono text-2xl text-accent">${parts.join(' ')}</p></div>`;
  $('#numGrid').innerHTML = NUM.map(x => `<button data-say="${x.say}" class="rounded-2xl border border-white/10 bg-ink-900 p-4 text-left hover:border-accent/40 transition">
    <div class="flex items-baseline justify-between"><span class="font-mono text-xl font-bold text-white">${x.ru}</span><span class="font-loop text-2xl text-white">${x.th}</span></div>
    <p class="mt-2 font-mono text-sm text-accent">${x.lat}</p>${lang === 'ru' ? `<p class="text-xs text-zinc-500">${x.cyr}</p>` : ''}</button>`).join('');
}''')
rep("$('#numRand').onclick = () => { setNum([20, 40, 50, 60, 80, 120, 150, 250, 350, 499, 1200, 3500][Math.random() * 12 | 0]); speak(thaiNum(+$('#numIn').value).parts.join('|'), $('#numOut [data-say]')) };",
    "$('#numRand').onclick = () => { setNum(1 + Math.random() * 3599 | 0); $('#numOut [data-say]').click() };")
rep("const setNum = v => { $('#numIn').value = Math.max(0, Math.min(99999, v)); renderNum(); icons() };", "const setNum = v => { $('#numIn').value = Math.max(1, Math.min(3599, v)); renderNum(); icons() };")

func('renderBody', r'''
function renderBody() {
  $('#bodyGrid').innerHTML = BODY.map(x => wordTile(x,
    `<button data-say="${x.my.say}" class="mt-3 inline-flex items-center gap-1.5 rounded-full border border-white/10 px-2.5 py-1 text-xs text-zinc-400 hover:border-accent hover:text-accent transition"><i data-lucide="user" class="w-3 h-3"></i>${t('hurts')} · <span class="font-mono">${x.my.lat}</span></button>`)).join('');
}''')

func('renderVerbs', r'''
function renderVerbs() {
  $('#modalOpts').innerHTML = MODALS.map(m => `<button data-modal="${m.k}" class="${chip(modal === m.k)}">${L(m.ru, m.en)} · <span class="font-mono">${m.pre}</span></button>`).join('');
  const v = VERB[verbI], m = MODALS.find(x => x.k === modal) || MODALS[0], f = v.forms[m.k];
  $('#sentOut').innerHTML = `<div class="fade-up flex items-start justify-between gap-4">
    <div>
      <p class="font-thai text-4xl text-white">${f.th}</p>
      <p class="mt-2 font-mono text-2xl"><span class="text-accent">${m.pre}</span><span class="text-white">${v.lat}</span></p>
      ${lang === 'ru' ? `<p class="text-zinc-500">${f.cyr}</p>` : ''}
      <p class="mt-3 text-lg font-semibold text-white">${L(...v.tr[m.k])}</p>
      <p class="mt-1 text-sm text-zinc-400">${L(...m.note)}</p>
    </div>${playBtn(f.say, 'w-12 h-12')}</div>`;
  $('#verbGrid').innerHTML = VERB.map((x, i) => `<button data-verb="${i}" class="text-left rounded-2xl border ${i === verbI ? 'border-accent bg-accent/10' : 'border-white/10 bg-ink-900 hover:border-white/30'} p-4 transition">
    <span class="font-thai text-2xl text-white">${x.th}</span>
    <p class="mt-1 font-mono text-sm text-accent">${x.lat}</p>
    ${lang === 'ru' ? `<p class="text-xs text-zinc-500">${x.cyr}</p>` : ''}
    <p class="mt-2 text-sm font-medium text-white">${x[lang]}</p></button>`).join('');
}''')
rep("let cat = 'greet', cls = 'all', selCons = 0, vtab = 'num', modal = 'want',", "let cat = 'royal', cls = 'all', selCons = 0, vtab = 'num', modal = 'none',")
rep("if (b) { verbI = +b.dataset.verb; renderVerbs(); icons(); speak(VERB[verbI].th) }", "if (b) { verbI = +b.dataset.verb; renderVerbs(); icons(); speak(VERB[verbI].forms[modal].say) }")

func('renderQues', r'''
function renderQues() {
  $('#qwGrid').innerHTML = QWORDS.map(x => wordTile(x)).join('');
  $('#qpGrid').innerHTML = QPARTS.map(exTile).join('');
}''')

func('renderCls', r'''
function renderCls() {
  $('#orderItems').innerHTML = ORDER.map((x, i) => `<button data-ord="${i}" class="${chip(i === ordI)}">${x[lang]}</button>`).join('');
  $('#orderNums').innerHTML = ORDER_N.map(([n]) => `<button data-ordn="${n}" class="${chip(n === ordN)} font-mono">× ${n}</button>`).join('');
  const it = ORDER[ordI], o = ORDER_PH[`${it.lat}|${ordN}`], c = CLS.find(x => x.lat === it.cls);
  $('#orderOut').innerHTML = `<div class="fade-up flex items-start justify-between gap-4"><div>
    <p class="font-thai text-4xl text-white">${o.th}</p>
    <p class="mt-2 font-mono text-2xl text-accent">${o.lat}</p>
    ${lang === 'ru' ? `<p class="text-zinc-500">${o.cyr}</p>` : ''}
    <p class="mt-3 text-lg font-semibold text-white">${ordN} ${c.lat} · ${it[lang]}</p>
    <p class="mt-1 text-sm text-zinc-400">${c[lang]}</p>
  </div>${playBtn(o.th, 'w-12 h-12')}</div>`;
  $('#clsGrid').innerHTML = CLS.map(x => wordTile(x)).join('');
}''')

func('renderEtq', r'''
function renderEtq() {
  $('#addrGrid').innerHTML = ADDR.map(x => `<div class="rounded-2xl border border-white/10 bg-ink-900 p-5 hover:border-accent/40 transition">
    <div class="flex items-start justify-between gap-2"><span class="font-thai text-3xl text-white">${x.th}</span>${playBtn(x.say, 'w-9 h-9')}</div>
    <p class="font-mono text-sm text-accent">${x.lat}</p>${lang === 'ru' ? `<p class="text-xs text-zinc-500">${x.cyr}</p>` : ''}
    <p class="mt-2 text-sm text-zinc-300 leading-relaxed">${x[lang]}</p>
    <button data-say="${x.call}" class="mt-3 inline-flex items-center gap-1.5 rounded-full border border-white/10 px-2.5 py-1 text-left font-mono text-xs text-zinc-400 hover:border-accent hover:text-accent transition"><i data-lucide="scroll-text" class="w-3 h-3 shrink-0"></i>${x.call}</button>
  </div>`).join('');
  const e = EMESAL;
  $('#politeYes').innerHTML = `<h3 class="font-semibold text-white flex items-center gap-2"><i data-lucide="sparkles" class="w-4 h-4 text-accent"></i>${t('politeTitle')}</h3>
    <div class="mt-4 flex items-center gap-4"><span class="font-thai text-5xl text-white">${e.th}</span>${playBtn(e.say, 'w-12 h-12')}</div>
    <p class="mt-2 font-mono text-accent">${e.lat}</p>
    <p class="mt-3 text-sm text-zinc-300 leading-relaxed">${e[lang]}</p>
    <div class="mt-4 space-y-2 text-sm">${e.pairs.map(p => `<div class="flex flex-wrap items-center gap-2"><button data-say="${p.eg.say}" class="font-mono text-zinc-300 hover:text-white">${p.eg.lat}</button><i data-lucide="arrow-right" class="w-3.5 h-3.5 text-zinc-500"></i><button data-say="${p.es.say}" class="font-mono text-accent hover:text-white">${p.es.lat}</button><span class="text-zinc-500">— ${L(p.ru, p.en)}</span></div>`).join('')}</div>`;
  $('#waiList').innerHTML = `<h3 class="font-semibold text-white flex items-center gap-2"><i data-lucide="school" class="w-4 h-4 text-accent"></i>${t('waiTitle')}</h3>
    <ul class="mt-4 space-y-3">${SCHOOL.map(([ic, ru, en, ex]) => `<li class="flex items-start gap-3"><span class="grid place-items-center w-8 h-8 shrink-0 rounded-lg bg-white/5 text-accent"><i data-lucide="${ic}" class="w-4 h-4"></i></span><span class="pt-1 text-sm text-zinc-300 leading-relaxed">${L(ru, en)} <button data-say="${ex.say}" class="ml-1 inline-flex items-center gap-1 font-mono text-accent hover:text-white transition"><i data-lucide="volume-2" class="w-3.5 h-3.5"></i>${ex.lat}</button></span></li>`).join('')}</ul>`;
  $('#dontList').innerHTML = `<h3 class="font-semibold text-rose-200 flex items-center gap-2"><i data-lucide="shield-alert" class="w-4 h-4"></i>${t('dontTitle')}</h3>
    <ul class="mt-4 grid md:grid-cols-2 gap-3">${MYTHS.map(([ic, ru, en]) => `<li class="flex items-start gap-3"><span class="grid place-items-center w-8 h-8 shrink-0 rounded-lg bg-white/5 text-rose-300"><i data-lucide="${ic}" class="w-4 h-4"></i></span><span class="pt-1 text-sm text-zinc-300 leading-relaxed">${L(ru, en)}</span></li>`).join('')}</ul>`;
  $('#smileGrid').innerHTML = WISDOM.map(phraseCard).join('');
}''')

func('renderSigns', r'''
function renderSigns() {
  $('#signTabs').innerHTML = [['sign', 'tags'], ['tag', 'hash']].map(([k, ic]) => `<button data-sgk="${k}" class="${chip(k === sgKind)}"><i data-lucide="${ic}" class="w-3.5 h-3.5"></i>${t('sg_' + k)}</button>`).join('');
  $('#signGrid').innerHTML = SIGNS.filter(x => x.k === sgKind).map(x => `
    <button data-say="${x.say}" class="fade-up group text-left rounded-2xl border border-white/10 bg-ink-900 p-4 hover:border-accent/40 transition">
      <div class="rounded-xl border-2 ${SIGN_STYLE[x.s]} px-3 py-4 flex items-center justify-center gap-3 group-hover:scale-[1.03] transition"><span class="font-loop text-4xl">${x.th}</span>${x.k === 'sign' ? `<span class="font-mono text-lg">${x.lat}</span>` : ''}</div>
      <p class="mt-3 text-sm font-medium text-white">${x[lang]}</p>
      ${x.ex ? `<p class="mt-1 text-sm"><span class="font-thai text-white">${x.ex.th}</span> <span class="font-mono text-accent">${x.ex.lat}</span> <span class="text-zinc-500">— ${L(x.xru, x.xen)}</span></p>` : `<p class="mt-1 font-mono text-xs text-zinc-500">${x.lat}</p>`}
    </button>`).join('');
}''')

func('renderTopVerbs', r'''
function renderTopVerbs() {
  const qv = $('#tvSearch').value.trim().toLowerCase();
  const max = TOPV[0].n;
  const rows = TOPV.filter(v => !qv || [v.lat, v.gw, v.ru, v.en, ...v.forms].some(f => (f || '').toLowerCase().includes(qv)));
  const shown = qv || tvAll ? rows : rows.slice(0, 20);
  $('#tvCount').textContent = TOPV.length;
  $('#tvBody').innerHTML = shown.map(v => `<tr class="hover:bg-white/[.02] transition">
    <td class="px-4 py-3 font-mono text-zinc-500">${v.rank}</td>
    <td class="px-4 py-3"><button data-say="${v.say}" class="text-left group/v"><span class="font-thai text-2xl text-white group-hover/v:text-accent transition">${v.th}</span><span class="block font-mono text-xs text-accent">${v.lat} [${v.gw}]</span>${lang === 'ru' ? `<span class="block text-xs text-zinc-500">${v.cyr}</span>` : ''}</button></td>
    <td class="px-4 py-3 text-zinc-200">${v[lang]}</td>
    <td class="px-4 py-3"><div class="flex flex-wrap gap-1.5">${v.forms.map(f => `<button data-say="${f}" class="inline-flex items-center gap-1 rounded-lg border border-white/10 bg-ink-950 px-2 py-1 font-mono text-xs text-zinc-300 hover:border-accent hover:text-accent transition"><i data-lucide="volume-2" class="w-3 h-3"></i>${f}</button>`).join('')}</div></td>
    <td class="px-4 py-3"><div class="h-1.5 rounded-full bg-white/5 overflow-hidden"><div class="h-full bg-accent/70" style="width:${Math.max(4, v.n / max * 100)}%"></div></div><span class="mt-1 block font-mono text-[11px] text-zinc-500">${v.n.toLocaleString(lang)}</span></td>
  </tr>`).join('');
  const more = $('#tvMore');
  more.classList.toggle('hidden', !!qv);
  more.querySelector('span').textContent = tvAll ? t('tvLess') : `${t('tvMore')} ${TOPV.length}`;
  more.querySelector('i')?.setAttribute('data-lucide', tvAll ? 'chevrons-up' : 'chevrons-down');
}''')

# grammar: show the glued transliteration of the whole sentence
rep("<p class=\"mt-2 font-mono text-accent\">${slots.map(s => s.lat).join(' ')}</p>", "<p class=\"mt-2 font-mono text-accent\">${SENT_BASES[stBase].texts[stType].lat}</p>")
rep("${lang === 'ru' ? `<p class=\"text-zinc-500\">${slots.map(s => s.cyr).join(' ')}</p>` : ''}", "${lang === 'ru' ? `<p class=\"text-zinc-500\">${SENT_BASES[stBase].texts[stType].cyr}</p>` : ''}")

# dialogs = reading a tablet: options are translations (no audio), them = tablet line
rep("const dlgYouSay = o => o.th + pt().th;", "const dlgYouSay = o => ''; // translations are not voiced")
rep('<span class="block text-sm text-zinc-400">${o[lang]}</span></button>` }).join(\'\');', '<span class="block text-base text-white">${o[lang]}</span></button>` }).join(\'\');')

rep("let ansCat = 'food';", "let ansCat = 'gods';")

# hero, pools, trainers
rep("const HERO = PH.filter(x => ['greet', 'polite', 'bye'].includes(x.c));", "const HERO = PH.filter(x => x.hero);")
rep("  alpha: CONS.filter(c => !c.old).map(c => ({ th: c.ch, lat: c.name, ru: `${c.word} — ${c.ru}`, en: `${c.word} — ${c.en}`, say: c.ch + ' ' + c.word, np: 1 })),",
    "  alpha: GRID.filter(g => g.word).map(g => ({ th: g.th, lat: g.lat, ru: g.ru, en: g.en, say: g.say, np: 1 })),")
func('tNext', r'''
function tNext(play) {
  tn.cur = tn.next ?? (Math.random() * DET_DRILL.length | 0);
  tn.next = Math.random() * DET_DRILL.length | 0;
  preload(DET_DRILL[tn.cur].say); preload(DET_DRILL[tn.next].say);
  tn.lock = false;
  const x = DET_DRILL[tn.cur];
  $('#tReveal').innerHTML = `<span class="font-thai text-4xl text-white">${x.th}</span>`;
  tRender();
  if (play) speak(x.say, $('#tPlay'));
}''')
func('tRender', r'''
function tRender() {
  $('#tOpts').innerHTML = DET_OPTS.map((o, i) => `<button data-t="${i}" class="tone-btn rounded-xl border border-white/10 bg-ink-900 p-3 hover:border-white/30 transition"><span class="font-loop text-2xl text-white">${o.th}</span><p class="mt-1 font-mono text-xs text-accent">${o.lat}</p><p class="text-sm font-semibold text-white">${o[lang]}</p></button>`).join('');
  $('#tScore').textContent = tn.score; $('#tTotal').textContent = tn.total;
}''')
between("$('#tPlay').onclick", "\n/* trace */", r'''$('#tPlay').onclick = e => speak(DET_DRILL[tn.cur].say, e.currentTarget);
$('#tHint').onclick = () => { $('#tReveal').innerHTML += `<span class="block mt-2 font-mono text-base text-accent">${DET_DRILL[tn.cur].lat.replace(/\{[^}]+\}/, '{…}')}</span>` };
$('#tOpts').addEventListener('click', e => {
  const b = e.target.closest('[data-t]');
  if (!b || tn.lock) return;
  tn.lock = true; tn.total++;
  const x = DET_DRILL[tn.cur], ri = DET_OPTS.findIndex(o => o.k === x.k), ok = +b.dataset.t === ri;
  if (ok) tn.score++;
  $$('[data-t]').forEach(el => {
    if (+el.dataset.t === ri) el.className += ' !border-emerald-400 !bg-emerald-400/10 pop';
    else if (el === b) el.className += ' !border-rose-400 !bg-rose-400/10 shake';
  });
  $('#tReveal').innerHTML = `<span class="fade-up inline-block"><span class="font-thai text-4xl text-white">${x.th}</span><span class="block mt-2 font-mono text-lg text-accent">${x.lat}</span></span>`;
  $('#tScore').textContent = tn.score; $('#tTotal').textContent = tn.total;
  setTimeout(() => tNext(true), 1800);
});
''')
rep('<p id="tReveal" class="mt-5 h-8 font-mono text-xl text-accent"></p>', '<div id="tReveal" class="mt-5 min-h-[88px] text-center"></div>')
rep("if (name === 'tones') speak(TONES[tn.cur].th, $('#tPlay'));", "if (name === 'tones') speak(DET_DRILL[tn.cur].say, $('#tPlay'));")
rep('<div id="tOpts" class="mt-6 grid grid-cols-2 sm:grid-cols-5 gap-3"></div>', '<div id="tOpts" class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3"></div>')

# trace: cuneiform sets, one script style
between('const TR_SETS = {', 'const TR_W = 340;', '''const TR_SETS = {
  syl: () => TR_SYL,
  log: () => TR_LOG,
  num: () => TR_NUM
};
''')
rep("const tr = { set: 'cons', size: 'm',", "const tr = { set: 'syl', size: 'm',")
rep("const TR_STYLES = { loop: ['Noto Sans Thai Looped', 500], school: ['Mali', 500], hand: ['Sriracha', 400], cursive: ['Charm', 700] };", "const TR_STYLES = { cun: ['Noto Sans Cuneiform', 400] };")
rep("tr.style = 'loop'; tr.slant = 0;", "tr.style = 'cun'; tr.slant = 0;")
rep('class="leading-none">กขค</span>', 'class="leading-none">𒀭𒂗𒆠</span>')
rep("xs: 'text-[7px]' }[k]}\">ก</span>", "xs: 'text-[7px]' }[k]}\">𒀭</span>")
rep("document.fonts.load(trFontCss(100), 'กอ๑')", "document.fonts.load(trFontCss(100), '𒀭')")
rep("""document.fonts?.load('500 100px "Noto Sans Thai Looped"', 'กอ๑')""", """document.fonts?.load("400 100px 'Noto Sans Cuneiform'", '𒀭')""")

rep("const normTh = s => s.replace(/[\\s.,!?ๆ]/g, '').replace(/ครับ|ค่ะ|คะ|นะ/g, '');", "const normTh = s => s.toLowerCase().replace(/[^a-z]/g, '');")
rep("console.assert(simil('สวัสดีครับ', 'สวัสดี') === 1 && simil('ขอบคุณ', 'สวัสดี') < .5, 'simil');", "")

rep("const SITE = 'thai';", "const SITE = 'sumer';")

# trace: cuneiform is impressed, not drawn — each stroke becomes a wedge (head where you press, tail towards release)
func('trInk', r"""
function trInk(ctx, color, width) {
  const b = trSz().brush, grow = Math.max(0, width - b);       // grow > 0: dilated copy used for scoring tolerance
  const W = b * 2.4, H = b * 2.2, TW = Math.max(1.2, b * .4);  // head width, head length, tail width
  ctx.strokeStyle = ctx.fillStyle = color; ctx.lineCap = ctx.lineJoin = 'round';
  for (const st of tr.strokes) {
    const [sx, sy] = st[0], [ex, ey] = st[st.length - 1];
    let dx = ex - sx, dy = ey - sy, len = Math.hypot(dx, dy);
    if (len < H * .6) { dx = -1; dy = 0; len = 0 } else { dx /= len; dy /= len }  // a tap = Winkelhaken pointing left (𒌋)
    const px = -dy, py = dx;
    ctx.beginPath();
    ctx.moveTo(sx + px * W / 2, sy + py * W / 2); ctx.lineTo(sx - px * W / 2, sy - py * W / 2); ctx.lineTo(sx + dx * H, sy + dy * H); ctx.closePath();
    ctx.fill();
    if (grow) { ctx.lineWidth = grow; ctx.stroke() }
    if (len > H) {
      ctx.lineWidth = TW + grow;
      ctx.beginPath(); ctx.moveTo(sx + dx * H * .7, sy + dy * H * .7); ctx.lineTo(ex, ey); ctx.stroke();
    }
  }
}""")

for bad in ['CONS', 'thaiNum', 'thaiDigits', 'VOWELS32', 'TONEMARKS', 'VSAY', 'PRONOUN', 'INI[', 'FIN[', 'TONES[', 'orderPhrase(', 'ปวด', 'ไ', 'ก', 'ครับ']:
    if bad in s:
        print('LEFTOVER', bad, [s[m.start() - 40:m.start() + 40] for m in re.finditer(re.escape(bad), s)][:2])
open(DST, 'w', encoding='utf8').write(s)
print('written', DST, len(s))
