"""SumerFast content. Sumerian is given in transliteration; cuneiform, Cyrillic reading and audio keys are generated.
Sources: ETCSL (etcsl.orinst.ox.ac.uk) for literary lines and translations, ePSD2 / ORACC for vocabulary, OGSL for signs."""

# ---------- phrases from tablets: (cat, translit, ru, en, tip_ru, tip_en, source) ----------
CATS = [('royal', 'crown'), ('letter', 'mail'), ('proverb', 'quote'), ('lit', 'book-open'), ('scribe', 'pen-line'), ('gods', 'sparkles'), ('daily', 'wheat')]
PH = [
    # royal inscriptions (standard formulae, ETCSRI)
    ('royal', 'lugal kiš{ki}', 'царь Киша', 'king of Kish', 'Самый древний царский титул: тот, кто владел Кишем, считался владыкой всего Шумера.', 'The oldest royal title: whoever held Kish was seen as lord of all Sumer.', 'ETCSRI'),
    ('royal', 'lugal ki-en-gi ki-uri', 'царь Шумера и Аккада', 'king of Sumer and Akkad', 'ki-en-gi — так шумеры называли свою страну. ki-uri — Аккад, север.', 'ki-en-gi is what the Sumerians called their land; ki-uri is Akkad, the north.', 'ETCSRI'),
    ('royal', 'lugal an-ub-da limmu₂-ba', 'царь четырёх сторон света', 'king of the four quarters', 'Титул правителей, претендовавших на весь мир: an-ub-da — «стороны неба», limmu₂ — четыре.', 'Title of rulers claiming the whole world: an-ub-da “corners”, limmu₂ “four”.', 'ETCSRI'),
    ('royal', 'ur-{d}namma lugal uri₅{ki}-ma', 'Ур-Намму, царь Ура', 'Ur-Namma, king of Ur', '-ma здесь — родительный падеж (-ak): «царь (чего?) Ура».', '-ma here is the genitive (-ak): “king of Ur”.', 'ETCSRI'),
    ('royal', 'e₂-a-ni mu-na-du₃', 'он построил ему его храм', 'he built his temple for him', 'Концовка тысяч строительных надписей на кирпичах: e₂ — дом/храм, -a-ni — «его», mu-na-du₃ — «построил ему».', 'The ending of thousands of building inscriptions on bricks: e₂ house/temple, -a-ni “his”, mu-na-du₃ “built for him”.', 'ETCSRI'),
    ('royal', 'gu₃-de₂-a ensi₂ lagaš{ki}', 'Гудеа, правитель Лагаша', 'Gudea, ruler of Lagash', 'ensi₂ — правитель города, ниже «лугаля».', 'ensi₂ is a city ruler, below a lugal.', 'ETCSRI'),
    # letters (ETCSL 3.1.01)
    ('letter', 'lugal-ĝu₁₀-ra u₃-na-a-dug₄', 'Моему господину скажи:', 'Say to my lord:', 'Письма начинались с обращения к гонцу, который читал письмо вслух адресату.', 'Letters began by addressing the messenger, who read it aloud to the recipient.', 'ETCSL 3.1.01'),
    ('letter', 'arad₂-zu na-ab-be₂-a', 'так говорит твой слуга', 'thus says your servant', 'Вторая часть формулы: кто пишет. Дальше — суть письма.', 'Second half of the formula: who is writing. The message follows.', 'ETCSL 3.1.01'),
    # proverbs (ETCSL 6.1.x)
    ('proverb', 'kaš naĝ-naĝ-e a ba-naĝ-naĝ', 'Кто пьёт пиво, пьёт воду.', 'He who drinks beer drinks water.', 'Повтор основы naĝ-naĝ — признак повторяющегося действия.', 'Repeating the root naĝ-naĝ marks a repeated action.', 'ETCSL 6.1.01'),
    ('proverb', 'kaš gud-dam ka kun₄-bi-im', 'Пиво — это бык, а рот — его лестница.', 'Beer is a bull. The mouth is its stairway.', '-am₃ / -im — «есть, является»: связка в конце фразы.', '-am₃ / -im means “is” — the copula comes last.', 'ETCSL 6.1.01'),
    ('proverb', 'ninda {ĝiš}ma₂-am₃ a {ĝiš}gi-muš-am₃', 'Хлеб — лодка, вода — шест.', 'Bread is the boat, water is the punt-pole.', '{ĝiš} — определитель «дерево»: не читается, подсказывает, что ma₂ (лодка) деревянная.', '{ĝiš} is the “wood” determinative: silent, it hints that ma₂ (boat) is wooden.', 'ETCSL 6.1.01'),
    ('proverb', 'nam-tar ud ḫuš kalam-ma ri-a', 'Судьба — свирепая буря, что носится по стране.', 'Fate is a raging storm blowing over the Land.', 'nam-tar — «судьба», буквально «то, что отрезано (решено)».', 'nam-tar “fate”, literally “what is cut (decided)”.', 'ETCSL 6.1.02'),
    ('proverb', 'ka ĝal₂ taka₄-a nim ba-an-ku₄-ku₄', 'В открытый рот залетают мухи.', 'Flies enter an open mouth.', 'Шумерский вариант нашего «молчание — золото».', 'The Sumerian take on “silence is golden”.', 'ETCSL 6.1.03'),
    ('proverb', 'inim dug₃ gu₅-li lu₂ šar₂-ra-ka', 'Доброе слово — друг многим людям.', 'A good word is a friend to numerous men.', 'inim — «слово», dug₃ — «сладкий, добрый».', 'inim “word”, dug₃ “sweet, good”.', 'ETCSL 6.1.03'),
    ('proverb', 'ud ma-ra-an-ĝal₂ zid₂ ma₅-a', 'Пока есть свет — мели муку.', 'While you still have light, grind the flour.', 'Шумерское «куй железо, пока горячо».', 'The Sumerian “make hay while the sun shines”.', 'ETCSL 6.1.03'),
    ('proverb', 'e₂-še₃ ga-ĝen-na saĝ a-ab-kal', '«Пойду-ка я домой» — вот что ему дороже всего.', '“I’m going home” is what he prefers.', 'ga- — «давай я…»: ga-ĝen «пойду-ка».', 'ga- means “let me…”: ga-ĝen “let me go”.', 'ETCSL 6.1.03'),
    ('proverb', 'niĝ₂ maḫ gu₇-gu₇-e u₃ nu-um-ši-ku-ku', 'Кто ест слишком много, не может уснуть.', 'He who eats too much cannot sleep.', 'nu- — отрицание в начале глагола.', 'nu- is the negation at the start of the verb.', 'ETCSL 6.1.01'),
    # literature
    ('lit', 'an gal-ta ki gal-še₃ ĝeštug₂-ga-ni na-an-gub', 'С великих небес к великой земле она обратила свой разум.', 'From the great heaven she set her mind on the great below.', 'Первая строка «Нисхождения Инанны в подземный мир». -ta — «из», -še₃ — «к».', 'First line of “Inana’s Descent to the Netherworld”. -ta “from”, -še₃ “to”.', 'ETCSL 1.4.1'),
    ('lit', '{d}inana an mu-un-šub ki mu-un-šub kur-ra ba-e-a-ed₃', 'Инанна оставила небо, оставила землю и сошла в подземный мир.', 'Inana abandoned heaven, abandoned earth, and descended to the underworld.', 'kur — и «гора», и «чужая страна», и «подземный мир».', 'kur means mountain, foreign land and the netherworld.', 'ETCSL 1.4.1'),
    ('lit', 'lu₂-kiĝ₂-gi₄-a ag-ga dumu en-me-barag-ge₄-si-ke₄', 'Послы Агги, сына Энмебарагеси…', 'Envoys of Aga, the son of En-me-barage-si…', 'Начало поэмы «Гильгамеш и Агга». lu₂-kiĝ₂-gi₄-a — «человек, посланный с делом», то есть гонец.', 'Opening of “Gilgameš and Aga”. lu₂-kiĝ₂-gi₄-a is “the man sent on an errand” — an envoy.', 'ETCSL 1.8.1.1'),
    ('lit', 'kiš{ki}-ta {d}gilgameš₂ unug{ki}-še₃ mu-un-ši-re₇-eš', '…пришли из Киша к Гильгамешу в Урук.', '…came from Kiš to Gilgameš in Unug.', 'Урук по-шумерски — Unug. {ki} — определитель «место».', 'Uruk in Sumerian is Unug. {ki} is the “place” determinative.', 'ETCSL 1.8.1.1'),
    # scribes
    ('scribe', 'dub-sar eme-gir₁₅ nu-mu-un-zu-a a-na-am₃ nam-dub-sar-ra-ni', 'Что это за писец, если он не знает шумерского?', 'What kind of a scribe is a scribe who does not know Sumerian?', 'eme-gir₁₅ — «родной язык», так шумеры называли свой язык.', 'eme-gir₁₅ “native tongue” — the Sumerians’ name for their language.', 'ETCSL 6.1.02'),
    ('scribe', 'dub-sar an-ta-me-en lu₂ ki-ta nu-me-en', 'Ты — писец высокий, ты не человек низкий.', 'You are an outstanding scribe; you are no lowly man.', '-me-en — «ты есть», nu-me-en — «ты не есть».', '-me-en “you are”, nu-me-en “you are not”.', 'ETCSL 6.1.02'),
    ('scribe', 'izi nu-ub-da-an-ten-a-aš li-gi₄-in-zu sar-ra-ab', 'Пока огонь не погас, пиши свою табличку!', 'Before the fire has gone out, write your exercise tablet!', 'sar — «писать». -ab в конце — повелительное наклонение.', 'sar “to write”. -ab at the end marks the imperative.', 'ETCSL 6.1.03'),
    ('scribe', 'dub-sar šu nu-a nar ĝili₃ nu-a', 'Писец без руки — что певец без голоса.', 'A scribe without a hand. A singer without a throat.', 'šu — «рука», nu-a — «нет».', 'šu “hand”, nu-a “without”.', 'ETCSL 6.1.02'),
    # gods / temples
    ('gods', '{d}inana-ke₄ šag₄ gig-ga-ĝu₁₀ i₃ ḫe₂-eb-de₂', 'Пусть Инанна прольёт масло на моё больное сердце.', 'May Inana pour oil on my heart that aches.', 'ḫe₂- — «пусть»: пожелание и молитва.', 'ḫe₂- means “may”: wishes and prayers.', 'ETCSL 6.1.03'),
    ('gods', 'diĝir sizkur-ra me-te-bi-im', 'Жертвы — слава богов.', 'Offerings are the glory of the gods.', 'diĝir — «бог», знак-звезда 𒀭.', 'diĝir “god”, the star sign 𒀭.', 'ETCSL 6.1.02'),
    ('gods', 'sizkur₂-re nam-til₃ i₃-u₃-tud', 'Жертвы порождают жизнь.', 'Offerings create life.', 'nam-til₃ — «жизнь»: nam- превращает слово в отвлечённое понятие.', 'nam-til₃ “life”: nam- makes an abstract noun.', 'ETCSL 6.1.03'),
    # daily life
    ('daily', 'dam-gara₃ iri-ta ba-ra-e₃ ganba ba-ra-an-du₈', 'Купец ушёл из города — и рынок опустел.', 'The merchant left the city and the market broke up.', 'iri — «город», -ta — «из».', 'iri “city”, -ta “from”.', 'ETCSL 6.1.01'),
    ('daily', 'gud-de₃ al-ur₁₁-ru ur-re sur₃ an-tag', 'Пока бык пашет, собака портит борозды.', 'While the ox is ploughing, the dog is spoiling the deep furrows.', '-e (gud-de₃, ur-re) — эргатив: показывает того, кто действует.', '-e (gud-de₃, ur-re) is the ergative: it marks the doer.', 'ETCSL 6.1.02'),
    ('daily', 'šu nu-luḫ-ḫa ka-e tum₃-da niĝ₂-gig-ga-am₃', 'Тянуть немытые руки ко рту — мерзость.', 'Putting unwashed hands to one’s mouth is disgusting.', 'Санитарная грамотность 4000 лет назад.', 'Hygiene advice from 4,000 years ago.', 'ETCSL 6.1.03'),
    ('daily', 'engar igi-ĝal₂-la e₂-a ḫu-mu-e-da-an-til₃', 'Пусть с тобой в доме живёт мудрый земледелец.', 'May a clever farmer live at home with you.', 'igi-ĝal₂ — «мудрый», буквально «имеющий глаз».', 'igi-ĝal₂ “wise”, literally “having an eye”.', 'ETCSL 6.1.03'),
]
HERO_FROM = ('royal', 'proverb', 'scribe', 'lit')

# ---------- letter formula block (uses PH bill items) ----------
BILL = [
    ('mail-open', 'lugal-ĝu₁₀-ra', 'Моему господину', 'To my lord', '-ra — дательный падеж: «кому?». ĝu₁₀ — «мой».', '-ra is the dative: “to whom?”. ĝu₁₀ “my”.'),
    ('megaphone', 'u₃-na-a-dug₄', 'скажи (ему)', 'say (to him)', 'Повеление гонцу: u₃- … dug₄ «скажи».', 'An order to the messenger: u₃- … dug₄ “say”.'),
    ('user', 'arad₂-zu', 'твой слуга', 'your servant', '-zu — «твой».', '-zu “your”.'),
    ('message-square', 'na-ab-be₂-a', 'говорит так', 'says thus', 'Конец формулы. Дальше — само сообщение.', 'End of the formula; the message follows.'),
    ('hand-heart', 'ḫa-na-ab-šum₂-mu', 'пусть он ему даст', 'let him give it to him', 'Так заканчиваются письма-распоряжения эпохи III династии Ура: ḫa- (= ḫe₂-) «пусть», šum₂ «давать».', 'How Ur III letter-orders end: ḫa- (= ḫe₂-) “let”, šum₂ “give”.'),
]

# ---------- 01 sounds: (sym, example translit, ru title, ru desc, ru word, en title, en desc, en word) ----------
SOUNDS = [
    ('a e i u', 'an', 'Четыре гласные', 'В письме различаются a, e, i, u. Произносите их чисто, как в русском «а, э, и, у», без «йотов».', 'небо', 'Four vowels', 'The script distinguishes a, e, i, u. Say them pure, as in Spanish — no glides.', 'sky'),
    ('š', 'šu', 'š — «ш»', 'Как русское «ш». В транслитерации — s с птичкой.', 'рука', 'š — “sh”', 'Like English “sh”. Written as s with a háček.', 'hand'),
    ('ḫ', 'ḫe₂-ĝal₂', 'ḫ — русское «х»', 'Глухой звук в глубине горла — как «х» в слове «хлеб». Не английское h.', 'изобилие', 'ḫ — “ch” in Bach', 'A rasp at the back of the throat, like Scottish “loch”. Not English h.', 'abundance'),
    ('ĝ', 'ĝiš', 'ĝ — носовое «нг»', 'Один звук, как ng в английском sing. Пишется ĝ или ŋ.', 'дерево', 'ĝ — “ng”', 'One sound, like ng in “sing”. Written ĝ or ŋ.', 'tree, wood'),
    ('z', 'zu', 'z — «дз» или «ц»', 'Точно неизвестно. Многие учёные читают как «дз»; мы озвучиваем простым «з».', 'знать', 'z — “dz” or “ts”', 'Unknown for sure. Many scholars read it as “dz”; our voice uses a plain z.', 'to know'),
    ('b / p', 'dub', 'b, d, g — не совсем звонкие', 'Вероятно, b d g были ближе к русским «п т к», а p t k — к ним же, но с выдохом. Шумеры не различали «д» и «т» так, как мы.', 'табличка', 'b, d, g — not quite voiced', 'Probably b d g were plain p t k, and p t k were aspirated. The contrast wasn’t our voiced/voiceless one.', 'tablet'),
    ('-k', 'kalam-ma', 'Исчезающий согласный', 'Конечный согласный часто не произносился и всплывал только перед гласной: kalam «страна» → kalam-ma «страны».', 'страны', 'Vanishing consonant', 'A final consonant was often silent and resurfaced before a vowel: kalam “land” → kalam-ma “of the land”.', 'of the land'),
    ('ˈ', 'lugal', 'Ударение', 'Его не записывали. Чаще всего реконструируют ударение на последнем слоге: лу-ГАЛЬ.', 'царь', 'Stress', 'It was never written. It’s usually reconstructed on the last syllable: lu-GAL.', 'king'),
]

# ---------- 02 transliteration conventions: (mark, example, ru title, ru desc, en title, en desc) ----------
CONV = [
    ('abc', 'lugal', 'Строчные — шумерское чтение', 'Обычные буквы — это шумерское слово так, как его читают учёные.', 'Lowercase — Sumerian reading', 'Lowercase letters are the Sumerian word as scholars read it.'),
    ('ABC', 'LUGAL', 'Заглавные — имя знака', 'Так пишут знак, когда его чтение неизвестно или речь о самом знаке.', 'Capitals — sign name', 'Used when the reading is unknown or when talking about the sign itself.'),
    ('x₂', 'du₃', 'Индекс — разные знаки', 'Одинаково звучащие слова писались разными знаками. Цифра внизу различает их: du «идти», du₃ «строить».', 'Index — different signs', 'Words that sound the same used different signs. The subscript tells them apart: du “go”, du₃ “build”.'),
    ('{d}', '{d}inana', 'Определитель — не читается', 'Знак-пояснение перед или после слова: {d} — бог, {ki} — место, {ĝiš} — дерево. Его пишут, но не произносят.', 'Determinative — silent', 'A classifier sign before or after a word: {d} god, {ki} place, {ĝiš} wood. Written, never spoken.'),
    ('a-b', 'e₂-gal', 'Дефис — знаки одного слова', 'Каждый слог — отдельный знак клинописи. e₂-gal — «большой дом», то есть дворец.', 'Hyphen — signs of one word', 'Each syllable is a separate cuneiform sign. e₂-gal “big house” — a palace.'),
    ('[ ]', '[lugal]', 'Скобки — табличка разбита', 'Восстановленное по смыслу. x — знак, который невозможно прочитать.', 'Brackets — broken tablet', 'Restored text. x is a sign that can’t be read.'),
]
FAMOUS = ('an gal-ta ki gal-še₃ ĝeštug₂-ga-ni na-an-gub', '«С великих небес к великой земле она обратила свой разум» — первая строка «Нисхождения Инанны».', '“From the great heaven she set her mind on the great below” — first line of “Inana’s Descent”.')
# homophones: (translit, ru, en)
HOMO = [('du', 'идти', 'to go'), ('du₃', 'строить', 'to build'), ('du₁₀', 'хороший, сладкий', 'good, sweet'), ('du₁₁', 'говорить', 'to speak'),
        ('gu₂', 'шея', 'neck'), ('gu₃', 'голос', 'voice'), ('gu₄', 'бык', 'ox'), ('gu₇', 'есть (пищу)', 'to eat')]

# ---------- 03 signs. syllabary rows (consonant -> values a e i u), logograms ----------
SYL_ROWS = ['', 'b', 'd', 'g', 'ḫ', 'k', 'l', 'm', 'n', 'r', 's', 'š', 't', 'z']
# grid tiles: (value, class v/c/l, ru meaning as a word or '', en, other readings)
GRID = [
    ('a', 'v', 'вода', 'water', 'a'), ('e', 'v', '', '', ''), ('i', 'v', '', '', ''), ('u', 'v', 'десять', 'ten', 'u'),
    ('ba', 'c', '', '', ''), ('bi', 'c', 'пиво', 'beer', 'kaš'), ('bu', 'c', '', '', ''),
    ('da', 'c', 'сторона', 'side', 'da'), ('di', 'c', 'суд; здоровье', 'case; health', 'di silim'), ('du', 'c', 'идти; стоять', 'go; stand', 'ĝen gub'),
    ('ga', 'c', 'молоко', 'milk', 'ga'), ('gi', 'c', 'тростник', 'reed', 'gi'), ('gu', 'c', 'нить', 'thread', 'gu'),
    ('ḫa', 'c', 'рыба', 'fish', 'ku₆'), ('ḫi', 'c', 'хороший', 'good', 'dug₃'), ('ḫu', 'c', 'птица', 'bird', 'mušen'),
    ('ka', 'c', 'рот; слово', 'mouth; word', 'inim dug₄ zu₂ gu₃'), ('ki', 'c', 'земля, место', 'earth, place', 'ki'), ('ku', 'c', 'сидеть', 'sit', 'tuš dur₂'),
    ('la', 'c', '', '', ''), ('li', 'c', '', '', ''), ('lu', 'c', 'овца', 'sheep', 'udu'),
    ('ma', 'c', '', '', ''), ('mi', 'c', 'ночь', 'night', 'ge₆'), ('mu', 'c', 'имя; год', 'name; year', 'mu'),
    ('na', 'c', '', '', ''), ('ni', 'c', 'масло; сам', 'oil; self', 'i₃ ni₂'), ('nu', 'c', 'не', 'not', 'nu'),
    ('ra', 'c', 'бить', 'strike', 'ra'), ('ri', 'c', '', '', ''), ('ru', 'c', 'падать', 'fall', 'šub'),
    ('sa', 'c', 'жила', 'sinew', 'sa'), ('si', 'c', 'рог', 'horn', 'si'), ('su', 'c', 'кожа, тело', 'skin, body', 'su'),
    ('ša', 'c', '', '', ''), ('ši', 'c', 'глаз', 'eye', 'igi'), ('šu', 'c', 'рука', 'hand', 'šu'),
    ('ta', 'c', '', '', ''), ('ti', 'c', 'жизнь; стрела', 'life; arrow', 'til₃'), ('tu', 'c', '', '', ''),
    ('za', 'c', 'камень', 'stone', 'na₄'), ('zi', 'c', 'жизнь, дыхание', 'life, breath', 'zi'), ('zu', 'c', 'знать', 'know', 'zu'),
    ('lugal', 'l', 'царь', 'king', 'lugal'), ('e₂', 'l', 'дом, храм', 'house, temple', 'e₂'), ('an', 'l', 'небо; бог', 'sky; god', 'diĝir'),
    ('kur', 'l', 'гора; чужая страна', 'mountain; foreign land', 'kur'), ('iri', 'l', 'город', 'city', 'uru'), ('dumu', 'l', 'ребёнок, сын', 'child, son', 'dumu'),
    ('lu₂', 'l', 'человек', 'man, person', 'lu₂'), ('munus', 'l', 'женщина', 'woman', 'munus'), ('ninda', 'l', 'хлеб', 'bread', 'ninda'),
    ('gud', 'l', 'бык', 'ox', 'gud'), ('še', 'l', 'ячмень', 'barley', 'še'), ('dub', 'l', 'табличка', 'tablet', 'dub'),
    ('eme', 'l', 'язык', 'tongue, language', 'eme'), ('saĝ', 'l', 'голова', 'head', 'saĝ'), ('dug₃', 'l', 'сладкий, хороший', 'sweet, good', 'dug₃'),
]

# ---------- 05 words ----------
# number names are reconstructed from Old Babylonian lexical lists (Edzard 2003)
NUM_NAMES = {1: 'aš', 2: 'min', 3: 'eš₅', 4: 'limmu₂', 5: 'ia₂', 6: 'aš₃', 7: 'imin', 8: 'ussu', 9: 'ilimmu', 10: 'u', 20: 'niš', 30: 'ušu₃', 40: 'nimin', 50: 'ninnu', 60: 'ĝeš₂'}
NUM_RU = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 20: '20', 30: '30', 40: '40', 50: '50', 60: '60'}
# (translit, ru, en, no "my" form)
BODY = [('saĝ', 'голова', 'head'), ('igi', 'глаз; лицо', 'eye; face'), ('ĝeštug₂', 'ухо; разум', 'ear; mind'), ('kiri₃', 'нос', 'nose'), ('ka', 'рот', 'mouth'),
        ('zu₂', 'зуб', 'tooth'), ('eme', 'язык', 'tongue'), ('gu₂', 'шея', 'neck'), ('šu', 'рука, кисть', 'hand'), ('a₂', 'рука; сила', 'arm; strength'),
        ('ĝiri₃', 'нога, ступня', 'foot'), ('šag₄', 'сердце, нутро', 'heart, belly'), ('gaba', 'грудь', 'chest'), ('su', 'тело, кожа', 'body, skin'), ('ur₂', 'колено', 'lap; root')]
# transitive verbs: (root, ru infinitive, ru "he did", ru "may he", ru "let me", en base, en past)
VERB = [('du₃', 'строить', 'построил', 'пусть построит', 'давай я построю', 'build', 'built'), ('sar', 'писать', 'написал', 'пусть напишет', 'давай я напишу', 'write', 'wrote'),
        ('gu₇', 'есть', 'съел', 'пусть съест', 'давай я съем', 'eat', 'ate'), ('naĝ', 'пить', 'выпил', 'пусть выпьет', 'давай я выпью', 'drink', 'drank'),
        ('ak', 'делать', 'сделал', 'пусть сделает', 'давай я сделаю', 'do', 'did'), ('zu', 'знать', 'узнал', 'пусть узнает', 'давай я узнаю', 'know', 'learned'),
        ('šum₂', 'давать', 'дал', 'пусть даст', 'давай я дам', 'give', 'gave'), ('dab₅', 'хватать', 'схватил', 'пусть схватит', 'давай я схвачу', 'seize', 'seized'),
        ('ĝar', 'ставить, класть', 'поставил', 'пусть поставит', 'давай я поставлю', 'place', 'placed'), ('tuku', 'иметь, брать', 'взял', 'пусть возьмёт', 'давай я возьму', 'have, take', 'took')]
# verbal prefixes for the builder: (key, prefix, ru label, en label, ru pattern key, en pattern)
MODALS = [('none', 'mu-un-', 'Он сделал', 'He did', 'mu-un- — «он (сделал)»: обычное прошедшее.', 'mu-un- — “he (did)”: plain past.'),
          ('not', 'nu-mu-un-', 'Он не сделал', 'He didn’t', 'nu- впереди всей цепочки — отрицание.', 'nu- in front of the whole chain negates it.'),
          ('may', 'ḫe₂-en-', 'Пусть он', 'May he', 'ḫe₂- — «пусть»: так пишут пожелания и проклятия.', 'ḫe₂- — “may”: used for wishes and curses.'),
          ('let', 'ga-', 'Давай я', 'Let me', 'ga- — «давай-ка я…»: ga-gu₇ «дай-ка я поем».', 'ga- — “let me…”: ga-gu₇ “let me eat”.')]
# question words: (translit, ru, en)
QWORDS = [('a-ba', 'кто', 'who'), ('a-na', 'что', 'what'), ('me-a', 'где', 'where'), ('me-še₃', 'куда', 'where to'), ('a-na-aš', 'почему', 'why'), ('a-gin₇', 'как', 'how')]
# cases: (suffix, ru name, en name, example translit, example ru, example en)
CASES = [('-e', 'эргатив — кто действует', 'ergative — the doer', 'lugal-e', 'царь (сделал)', 'the king (did)'),
         ('-ak', 'родительный — чей', 'genitive — of', 'e₂ lugal-la', 'дом царя', 'the king’s house'),
         ('-ra', 'дательный — кому', 'dative — to whom', 'lugal-ra', 'царю', 'to the king'),
         ('-ta', 'исходный — откуда', 'ablative — from', 'iri-ta', 'из города', 'from the city'),
         ('-še₃', 'направительный — куда', 'terminative — to', 'e₂-še₃', 'к дому', 'to the house'),
         ('-a', 'местный — где', 'locative — in', 'e₂-a', 'в доме', 'in the house'),
         ('-da', 'совместный — с кем', 'comitative — with', 'lugal-da', 'с царём', 'with the king'),
         ('-gin₇', 'сравнительный — как', 'equative — like', 'ur-gin₇', 'как собака', 'like a dog')]
# measures: (unit, ru, en)
MEASURES = [('sila₃', 'сила ≈ 1 л — мера зерна, пива, масла', 'sila ≈ 1 l — grain, beer, oil'), ('gur', 'гур = 300 сила — мера зерна', 'gur = 300 sila — grain'),
            ('ma-na', 'мина ≈ 500 г — мера веса', 'mina ≈ 500 g — weight'), ('gin₂', 'шекель ≈ 8 г — серебро', 'shekel ≈ 8 g — silver'),
            ('gun₂', 'талант = 60 мин ≈ 30 кг', 'talent = 60 minas ≈ 30 kg'), ('iku', 'ику ≈ 0,36 га — мера поля', 'iku ≈ 0.36 ha — field'),
            ('sar', 'сар ≈ 36 м² — участок, кирпичи', 'sar ≈ 36 m² — plot, bricks'), ('danna', 'данна ≈ 10 км — «двойной час» пути', 'danna ≈ 10 km — a “double hour” walk')]
# order builder: (item, ru, en, unit)
ORDER = [('kaš', 'пиво', 'beer', 'sila₃'), ('ninda', 'хлеб', 'bread', 'sila₃'), ('i₃', 'масло', 'oil', 'sila₃'), ('zu₂-lum', 'финики', 'dates', 'sila₃'),
         ('še', 'ячмень', 'barley', 'gur'), ('ku₃-babbar', 'серебро', 'silver', 'gin₂'), ('siki', 'шерсть', 'wool', 'ma-na'), ('urudu', 'медь', 'copper', 'ma-na'), ('a-šag₄', 'поле', 'field', 'iku')]
# economy words (FOOD tab): group key, ru, en, items (translit, ru, en)
ECON = [
    ('food', 'Еда и напитки', 'Food & drink', [('ninda', 'хлеб', 'bread'), ('kaš', 'пиво', 'beer'), ('ga', 'молоко', 'milk'), ('i₃', 'масло', 'oil, fat'), ('lal₃', 'сироп, мёд', 'syrup, honey'), ('zu₂-lum', 'финики', 'dates'), ('ku₆', 'рыба', 'fish'), ('uzu', 'мясо', 'meat')]),
    ('animals', 'Животные', 'Animals', [('udu', 'овца', 'sheep'), ('gu₄', 'бык', 'ox'), ('anše', 'осёл', 'donkey'), ('ur', 'собака', 'dog'), ('maš₂', 'козёл', 'goat'), ('šaḫ₂', 'свинья', 'pig'), ('mušen', 'птица', 'bird')]),
    ('land', 'Земля и вода', 'Land & water', [('še', 'ячмень', 'barley'), ('ĝiš', 'дерево', 'tree, wood'), ('gi', 'тростник', 'reed'), ('a-šag₄', 'поле', 'field'), ('id₂', 'река', 'river'), ('a', 'вода', 'water'), ('kalam', 'страна (Шумер)', 'the Land (Sumer)')]),
    ('goods', 'Материалы', 'Materials', [('ku₃-babbar', 'серебро', 'silver'), ('ku₃-sig₁₇', 'золото', 'gold'), ('urudu', 'медь', 'copper'), ('na₄', 'камень', 'stone'), ('za-gin₃', 'лазурит', 'lapis lazuli'), ('siki', 'шерсть', 'wool'), ('tug₂', 'ткань, одежда', 'cloth, garment')]),
]

# ---------- 06 grammar: sentence builder ----------
# roles: S doer (with ergative -e), O object, NEG, M modal prefix, T verbal prefix chain, V root, P suffix
SENT_TYPES = [
    ('st', 'Он сделал', 'He did', 'Порядок SOV: кто → что → глагол. Делающий получает эргатив -e, глагол собирает приставки: mu-un- — «он (сделал)».', 'SOV order: doer → object → verb. The doer takes the ergative -e; the verb stacks prefixes: mu-un- “he (did)”.'),
    ('neg', 'Отрицание', 'Negative', 'nu- ставится в самое начало глагольной цепочки.', 'nu- goes at the very front of the verb chain.'),
    ('may', 'Пусть…', 'May…', 'ḫe₂- вместо mu- — пожелание: «пусть построит». Так заканчиваются царские надписи и проклятия.', 'ḫe₂- instead of mu- makes a wish: “may he build”. Royal inscriptions and curses end like this.'),
    ('impf', 'Делает / сделает', 'Does / will do', 'Незавершённое действие (marû): i₃- + основа + -e в конце. Одна форма для «строит» и «будет строить».', 'Unfinished action (marû): i₃- + root + final -e. One form for “builds” and “will build”.'),
    ('pl', 'Они сделали', 'They did', 'Множественное число людей — -e-ne, и глагол получает -eš в конце: mu-un-du₃-uš.', 'Human plural is -e-ne, and the verb ends in -eš: mu-un-du₃-uš.'),
    ('wh', 'Кто сделал?', 'Who did?', 'Вопросительное слово встаёт на место того, о ком спрашивают: a-ba «кто» + эргатив -e → a-ba-a.', 'The question word takes the place of what is asked: a-ba “who” + ergative -e → a-ba-a.'),
]
ROLE = {'S': ('кто + -e', 'doer + -e'), 'O': ('что', 'what'), 'NEG': ('не', 'not'), 'M': ('пусть', 'may'), 'T': ('приставки', 'prefixes'), 'V': ('основа', 'root'), 'P': ('окончание', 'suffix'), 'QW': ('вопрос', 'question')}
# base: doer, doer-erg, doer-plural-erg, object, root, imperfective root, translations per type
SENT_BASES = [
    ('царь · дом', 'king · house', 'lugal', 'lugal-e', 'lugal-e-ne', 'e₂', 'du₃', 'du₃-e', {
        'st': ('Царь построил дом', 'The king built the house'), 'neg': ('Царь не построил дом', 'The king did not build the house'), 'may': ('Пусть царь построит дом', 'May the king build the house'),
        'impf': ('Царь строит дом', 'The king builds the house'), 'pl': ('Цари построили дом', 'The kings built the house'), 'wh': ('Кто построил дом?', 'Who built the house?')}),
    ('писец · табличка', 'scribe · tablet', 'dub-sar', 'dub-sar-e', 'dub-sar-e-ne', 'dub', 'sar', 'sar-re', {
        'st': ('Писец написал табличку', 'The scribe wrote the tablet'), 'neg': ('Писец не написал табличку', 'The scribe did not write the tablet'), 'may': ('Пусть писец напишет табличку', 'May the scribe write the tablet'),
        'impf': ('Писец пишет табличку', 'The scribe writes the tablet'), 'pl': ('Писцы написали табличку', 'The scribes wrote the tablet'), 'wh': ('Кто написал табличку?', 'Who wrote the tablet?')}),
    ('ребёнок · хлеб', 'child · bread', 'dumu', 'dumu-e', 'dumu-e-ne', 'ninda', 'gu₇', 'gu₇-e', {
        'st': ('Ребёнок съел хлеб', 'The child ate the bread'), 'neg': ('Ребёнок не съел хлеб', 'The child did not eat the bread'), 'may': ('Пусть ребёнок съест хлеб', 'May the child eat the bread'),
        'impf': ('Ребёнок ест хлеб', 'The child eats the bread'), 'pl': ('Дети съели хлеб', 'The children ate the bread'), 'wh': ('Кто съел хлеб?', 'Who ate the bread?')}),
]
SENT_RULES = [
    ('arrow-right', ('Глагол — в конце', 'The verb comes last'), ('Порядок SOV: lugal-e e₂ mu-un-du₃ — «царь дом построил».', 'SOV order: lugal-e e₂ mu-un-du₃ — “king house built”.')),
    ('target', ('Эргатив: -e у того, кто действует', 'Ergative: -e marks the doer'), ('Если есть объект, делающий получает -e (lugal-e). Без объекта — без -e: lugal ba-uš₂ «царь умер».', 'With an object the doer takes -e (lugal-e). Without one there is no -e: lugal ba-uš₂ “the king died”.')),
    ('link', ('Склеивание: слово + окончания', 'Agglutination: word + endings'), ('Окончания нанизываются: e₂-lugal-la-ka «в доме царя» = дом + царь + чей + где.', 'Endings stack up: e₂ lugal-la-ka “in the king’s house” = house + king + of + in.')),
    ('layers', ('Глагол — цепочка приставок', 'The verb is a prefix chain'), ('Перед основой стоят: отрицание/модальность, направление, кому, кто. mu-na-du₃ — «он построил ему».', 'Before the root: negation/mood, direction, to whom, who. mu-na-du₃ “he built for him”.')),
    ('users', ('Род: люди и вещи', 'Gender: people vs things'), ('Не мужской и женский, а «одушевлённый» и «неодушевлённый». -a-ni «его (человека)», -bi «его (вещи)».', 'Not male/female but human vs non-human. -a-ni “his (person)”, -bi “its (thing)”.')),
    ('circle-slash', ('Связка «есть» — в конце', 'The copula comes last'), ('-am₃ «есть»: kaš gud-dam «пиво — (это) бык». nu-me-en «ты не есть».', '-am₃ “is”: kaš gud-dam “beer is a bull”. nu-me-en “you are not”.')),
]

# ---------- 07 names: (cat, voice, translit, ru, en, tip_ru, tip_en) ----------
NAMES = [
    ('gods', 'm', '{d}en-lil₂', 'Энлиль', 'Enlil', 'Верховный бог, «владыка ветра». Его храм — в Ниппуре.', 'The chief god, “lord wind”. His temple was at Nippur.'),
    ('gods', 'f', '{d}inana', 'Инанна', 'Inana', 'Богиня любви и войны, звезда Венера.', 'Goddess of love and war, the planet Venus.'),
    ('gods', 'm', '{d}en-ki', 'Энки', 'Enki', 'Бог мудрости и пресных вод, «владыка земли».', 'God of wisdom and fresh water, “lord earth”.'),
    ('gods', 'm', 'an', 'Ан', 'An', 'Небо и бог неба. Тот же знак 𒀭 — «бог».', 'Heaven and its god. The same sign 𒀭 means “god”.'),
    ('gods', 'm', '{d}utu', 'Уту', 'Utu', 'Солнце и бог справедливости.', 'The sun and god of justice.'),
    ('gods', 'm', '{d}nanna', 'Нанна', 'Nanna', 'Луна, бог-покровитель Ура.', 'The moon, patron god of Ur.'),
    ('gods', 'f', '{d}nin-ḫur-saĝ', 'Нинхурсаг', 'Ninhursag', '«Владычица горы», богиня-мать.', '“Lady of the mountain”, the mother goddess.'),
    ('cities', 'm', 'unug{ki}', 'Урук', 'Uruk', 'Город Гильгамеша, где появилась письменность.', 'Gilgamesh’s city, where writing appeared.'),
    ('cities', 'f', 'uri₅{ki}', 'Ур', 'Ur', 'Столица III династии Ура, родина зиккурата Нанны.', 'Capital of the Third Dynasty of Ur, home of Nanna’s ziggurat.'),
    ('cities', 'm', 'nibru{ki}', 'Ниппур', 'Nippur', 'Священный город Энлиля и главная школа писцов.', 'Enlil’s holy city and the main scribal school.'),
    ('cities', 'f', 'lagaš{ki}', 'Лагаш', 'Lagash', 'Город Гудеа и тысяч хозяйственных табличек.', 'Gudea’s city and thousands of administrative tablets.'),
    ('cities', 'm', 'kiš{ki}', 'Киш', 'Kish', 'Самое раннее «царство» в Шумерском царском списке.', 'The earliest “kingship” in the Sumerian King List.'),
    ('cities', 'f', 'eridu{ki}', 'Эриду', 'Eridu', 'Древнейший город, город Энки.', 'The oldest city, the city of Enki.'),
    ('kings', 'm', '{d}gilgameš₂', 'Гильгамеш', 'Gilgamesh', 'Царь Урука, герой поэм. {d} — его почитали как бога.', 'King of Uruk, hero of the poems. {d} — he was worshipped as a god.'),
    ('kings', 'm', 'ur-{d}namma', 'Ур-Намму', 'Ur-Namma', 'Основатель III династии Ура, автор древнейшего свода законов.', 'Founder of the Third Dynasty of Ur, author of the oldest law code.'),
    ('kings', 'm', 'šul-gi', 'Шульги', 'Šulgi', 'Сын Ур-Намму, правил почти 50 лет, хвалился, что знает пять языков.', 'Ur-Namma’s son, ruled almost 50 years and boasted of knowing five languages.'),
    ('kings', 'm', 'gu₃-de₂-a', 'Гудеа', 'Gudea', 'Правитель Лагаша, известный статуями из диорита.', 'Ruler of Lagash, famous for his diorite statues.'),
    ('places', 'f', 'ki-en-gi', 'Шумер', 'Sumer', 'Так шумеры называли свою страну.', 'The Sumerians’ own name for their land.'),
    ('places', 'm', 'eme-gir₁₅', 'шумерский язык', 'Sumerian (language)', '«Родной язык» — самоназвание шумерского.', '“Native tongue” — Sumerian’s own name.'),
    ('places', 'm', '{id₂}idigna', 'Тигр', 'Tigris', '{id₂} — определитель «река».', '{id₂} is the “river” determinative.'),
    ('places', 'f', '{id₂}buranun', 'Евфрат', 'Euphrates', 'Река, на которой стояли Ур, Урук и Киш.', 'The river of Ur, Uruk and Kish.'),
    ('places', 'm', 'e₂-dub-ba-a', 'школа', 'school', '«Дом табличек» — школа писцов.', '“Tablet house” — the scribal school.'),
]
NAME_CATS = [('gods', 'sparkles'), ('cities', 'castle'), ('kings', 'crown'), ('places', 'map')]

# ---------- 08 read a tablet: (key, icon, ru, en, source, steps[(line, voice, ru, en, [(answer_ru, answer_en, ok, why_ru, why_en)])]) ----------
SCENES = [
    ('brick', 'brick-wall', 'Кирпич Ур-Намму', 'Ur-Namma’s brick', 'ETCSRI, Ur-Namma', [
        ('{d}nanna', 'm', 'Нанне', 'For Nanna', [('Нанне (богу Луны)', 'For Nanna (the moon god)', 1, '', ''), ('Царю Ура', 'For the king of Ur', 0, '{d} — определитель бога: это имя божества.', '{d} marks a god: this is a divine name.')]),
        ('lugal-a-ni', 'm', 'его господину', 'his lord', [('его господину', 'his lord', 1, '', ''), ('моему царю', 'my king', 0, '-a-ni — «его», а не «мой» (-ĝu₁₀).', '-a-ni is “his”, not “my” (-ĝu₁₀).')]),
        ('ur-{d}namma', 'm', 'Ур-Намму', 'Ur-Namma', [('Ур-Намму (имя царя)', 'Ur-Namma (the king’s name)', 1, '', ''), ('город Ур', 'the city of Ur', 0, 'Город был бы с {ki} в конце. Здесь имя человека.', 'A city would end in {ki}. This is a personal name.')]),
        ('lugal uri₅{ki}-ma-ke₄', 'm', 'царь Ура', 'king of Ur', [('царь Ура', 'king of Ur', 1, '', ''), ('дом Ура', 'house of Ur', 0, 'lugal — «царь». Дом был бы e₂.', 'lugal is “king”. House would be e₂.')]),
        ('e₂-a-ni', 'm', 'его храм', 'his temple', [('его дом (храм)', 'his house (temple)', 1, '', ''), ('его сына', 'his son', 0, 'Сын — dumu. e₂ — дом или храм.', 'Son is dumu. e₂ is house or temple.')]),
        ('mu-na-du₃', 'm', 'построил ему', 'built for him', [('построил ему', 'built for him', 1, '', ''), ('разрушил', 'destroyed', 0, 'du₃ — «строить». -na- — «ему».', 'du₃ is “build”. -na- is “for him”.')]),
    ]),
    ('letter', 'mail', 'Письмо царю Шульги', 'Letter to King Šulgi', 'ETCSL 3.1.01', [
        ('lugal-ĝu₁₀-ra', 'm', 'Моему господину', 'To my lord', [('Моему господину', 'To my lord', 1, '', ''), ('Царь Киша', 'King of Kish', 0, '-ĝu₁₀ «мой», -ra «кому».', '-ĝu₁₀ “my”, -ra “to”.')]),
        ('u₃-na-a-dug₄', 'm', 'скажи', 'say', [('скажи (ему)', 'say (to him)', 1, '', ''), ('напиши', 'write', 0, 'dug₄ — «говорить». Письмо читал вслух гонец.', 'dug₄ is “speak”. A messenger read the letter aloud.')]),
        ('{m}arad₂-ĝu₁₀ arad₂-zu', 'm', 'Арадгу, твой слуга', 'Aradĝu, your servant', [('Арадгу, твой слуга', 'Aradĝu, your servant', 1, '', ''), ('мой слуга Арадгу', 'my servant Aradĝu', 0, '-zu — «твой»: автор пишет о себе царю.', '-zu is “your”: the writer refers to himself.')]),
        ('na-ab-be₂-a', 'm', 'говорит так', 'says thus', [('говорит так:', 'says this:', 1, '', ''), ('пусть даст', 'let him give', 0, 'Это конец формулы приветствия, дальше — суть письма.', 'This closes the greeting formula; the message follows.')]),
    ]),
    ('scribe', 'pen-line', 'Пословица о писце', 'A proverb about scribes', 'ETCSL 6.1.02', [
        ('dub-sar', 'm', 'писец', 'a scribe', [('писец', 'scribe', 1, '', ''), ('табличка', 'tablet', 0, 'dub — табличка, dub-sar — «пишущий таблички».', 'dub is a tablet; dub-sar is “tablet writer”.')]),
        ('eme-gir₁₅', 'm', 'шумерский язык', 'Sumerian', [('шумерский язык', 'Sumerian', 1, '', ''), ('язык врага', 'the enemy’s tongue', 0, 'eme-gir₁₅ — «родной язык», шумерский.', 'eme-gir₁₅ is “native tongue” — Sumerian.')]),
        ('nu-mu-un-zu-a', 'm', 'который не знает', 'who does not know', [('который не знает', 'who does not know', 1, '', ''), ('который знает', 'who knows', 0, 'nu- в начале — отрицание.', 'nu- at the start negates.')]),
        ('a-na-am₃ nam-dub-sar-ra-ni', 'm', 'что за писец он?', 'what kind of scribe is he?', [('что за писец он?', 'what kind of scribe is he?', 1, '', ''), ('где его школа?', 'where is his school?', 0, 'a-na — «что». nam-dub-sar — «писцовость, ремесло писца».', 'a-na is “what”. nam-dub-sar is “scribeship”.')]),
    ]),
    ('inana', 'moon-star', 'Нисхождение Инанны', 'Inana’s Descent', 'ETCSL 1.4.1', [
        ('an gal-ta', 'f', 'с великих небес', 'from the great heaven', [('с великих небес', 'from the great heaven', 1, '', ''), ('к великому небу', 'to the great heaven', 0, '-ta — «из, от». «К» было бы -še₃.', '-ta is “from”. “To” would be -še₃.')]),
        ('ki gal-še₃', 'f', 'к великой земле', 'to the great earth', [('к великой земле', 'to the great below', 1, '', ''), ('из большого дома', 'from the big house', 0, 'ki — земля, -še₃ — «к».', 'ki is earth, -še₃ is “to”.')]),
        ('ĝeštug₂-ga-ni', 'f', 'свой разум', 'her mind', [('свой разум (ухо)', 'her mind (ear)', 1, '', ''), ('свою корону', 'her crown', 0, 'ĝeštug₂ — «ухо», а значит и «разум»: шумеры думали ушами.', 'ĝeštug₂ is “ear” and so “mind”: Sumerians thought with their ears.')]),
        ('na-an-gub', 'f', 'обратила', 'set', [('направила, обратила', 'set, directed', 1, '', ''), ('забыла', 'forgot', 0, 'gub — «ставить, стоять»: «поставила разум» = решила.', 'gub is “stand, set”: “set her mind” = decided.')]),
    ]),
    ('gilgamesh', 'swords', 'Гильгамеш и Агга', 'Gilgameš and Aga', 'ETCSL 1.8.1.1', [
        ('lu₂-kiĝ₂-gi₄-a', 'm', 'послы', 'envoys', [('послы, гонцы', 'envoys', 1, '', ''), ('воины', 'warriors', 0, 'lu₂ «человек» + kiĝ₂ gi₄ «отправить с делом» = посланник.', 'lu₂ “man” + kiĝ₂ gi₄ “send on an errand” = envoy.')]),
        ('ag-ga dumu en-me-barag-ge₄-si-ke₄', 'm', 'Агги, сына Энмебарагеси', 'of Aga, son of En-me-barage-si', [('Агги, сына Энмебарагеси', 'of Aga, son of En-me-barage-si', 1, '', ''), ('царя Урука', 'of the king of Uruk', 0, 'dumu — «сын». Агга — царь Киша, противник Гильгамеша.', 'dumu is “son”. Aga is Kish’s king, Gilgameš’s rival.')]),
        ('kiš{ki}-ta', 'm', 'из Киша', 'from Kiš', [('из Киша', 'from Kiš', 1, '', ''), ('в Киш', 'to Kiš', 0, '-ta — «из». «В» было бы -še₃.', '-ta is “from”.')]),
        ('{d}gilgameš₂ unug{ki}-še₃', 'm', 'к Гильгамешу в Урук', 'to Gilgameš in Unug', [('к Гильгамешу в Урук', 'to Gilgameš in Unug', 1, '', ''), ('от Гильгамеша из Урука', 'from Gilgameš in Unug', 0, '-še₃ — «к, в направлении».', '-še₃ is “to, towards”.')]),
        ('mu-un-ši-re₇-eš', 'm', 'пришли', 'came', [('пришли', 'came', 1, '', ''), ('ушли домой', 'went home', 0, '-ši- — «к нему», -eš — «они».', '-ši- “towards him”, -eš “they”.')]),
    ]),
]

# ---------- 09 world of Sumer ----------
ROLES = [
    ('lugal', 'Царь — «большой человек» (lu₂ + gal).', 'King — “big man” (lu₂ + gal).', 'lugal kiš{ki}'),
    ('ensi₂', 'Правитель города, наместник бога.', 'City ruler, the god’s steward.', 'gu₃-de₂-a ensi₂ lagaš{ki}'),
    ('dub-sar', 'Писец — самая уважаемая профессия грамотеев.', 'Scribe — the most respected literate profession.', 'dub-sar an-ta-me-en'),
    ('dam-gara₃', 'Купец, торговавший с далёкими странами.', 'Merchant trading with distant lands.', 'dam-gara₃ iri-ta ba-ra-e₃'),
    ('engar', 'Земледелец — основа хозяйства храмов.', 'Farmer — the backbone of temple estates.', 'engar igi-ĝal₂-la'),
]
EMESAL = ('gašan', 'Эмесал — «тонкий язык» (eme-sal): так в текстах говорят богини, женщины и жрецы-плакальщики gala. Слова в нём другие.', 'Emesal, “fine tongue” (eme-sal), is how goddesses, women and gala lamentation priests speak in texts. Its words differ.', [('nin', 'gašan', 'госпожа', 'lady'), ('diĝir', 'dimmer', 'бог', 'god'), ('ĝiš', 'mu', 'дерево', 'tree')])
SCHOOL = [
    ('school', 'e₂-dub-ba-a — «дом табличек»: школа, где мальчики годами переписывали знаки, словари и пословицы.', 'e₂-dub-ba-a, “tablet house”: the school where boys copied signs, word lists and proverbs for years.', 'e₂-dub-ba-a'),
    ('users', 'Учитель — um-mi-a, «мастер». Старший ученик помогал младшим.', 'The teacher was um-mi-a, “master”. Senior pupils helped juniors.', 'um-mi-a'),
    ('pen-line', 'Писали тростниковой палочкой по сырой глине — отсюда клиновидные штрихи.', 'They wrote with a reed stylus in wet clay — hence the wedge-shaped strokes.', 'dub'),
    ('languages', 'К 1800 году до н. э. шумерский уже не был разговорным. Его учили, как в Европе латынь, — по двуязычным словарям.', 'By 1800 BCE Sumerian was no longer spoken. It was learned like Latin in Europe — from bilingual word lists.', 'eme-gir₁₅'),
]
MYTHS = [
    ('ban', 'Шумерский не родственник ни турецкому, ни венгерскому, ни грузинскому. Это изолят: у него нет известных родственников.', 'Sumerian is not related to Turkish, Hungarian or Georgian. It’s an isolate with no known relatives.'),
    ('ban', 'Точное произношение неизвестно. Его восстанавливают по аккадским записям и заимствованиям.', 'The exact pronunciation is unknown; it is reconstructed from Akkadian spellings and loanwords.'),
    ('ban', 'Клинопись — не язык, а письмо. Им же писали аккадский, хеттский, урартский и другие языки.', 'Cuneiform is a script, not a language. It was also used for Akkadian, Hittite, Urartian and more.'),
    ('ban', '«Нибиру» и «пришельцы-аннунаки» — выдумки XX века. В табличках этого нет.', '“Nibiru” and “alien Anunnaki” are 20th-century inventions — not in the tablets.'),
    ('ban', 'Шумерский — не «первый язык человечества». Просто один из первых, который записали.', 'Sumerian isn’t “humanity’s first language” — just one of the first to be written down.'),
]
WISDOM = [
    ('ukur₃ nu-kal', 'Бедняк не в почёте.', 'The poor man is not appreciated.', 'ETCSL 6.1.02'),
    ('ḫu-ru-um ka tuku', 'Дурак болтлив.', 'The fool is garrulous.', 'ETCSL 6.1.03'),
    ('nam-sag₉-ga kaš-am₃ nam-ḫul kaskal-am₃', 'Хорошее — это пиво, плохое — это дорога.', 'The good thing is the beer. The bad thing is the journey.', 'ETCSL 6.1.02'),
    ('su nam-lu₂-ulu₃-ka a gig i₃-ĝal₂', 'В человеческой плоти — горькие слёзы.', 'There are bitter tears in human flesh.', 'ETCSL 6.1.03'),
    ('nam-tar tug₂-ga-am₃ edin-na mu-un-na-an-la₂', 'Судьба — ткань, растянутая в степи.', 'Fate is a cloth stretched out in the desert for a man.', 'ETCSL 6.1.02'),
    ('ka₅-a {ĝiš}si-ĝar-bi ĝiš-ur₃-am₃', 'Засов у лисы — целое бревно.', 'The fox’s door-bolt is a wooden beam.', 'ETCSL 6.1.02'),
    ('sipad-tur kuš₂-a-ni ama-ni nu-mu-un-da-an-zu', 'Уставший пастушок не узнаёт родной матери.', 'A shepherd-boy when weary cannot recognise his own mother.', 'ETCSL 6.1.03'),
    ('ninda in-na-til-la-am₃', 'Его хлеб кончился.', 'His bread is finished.', 'ETCSL 6.1.01'),
]

# ---------- 10 determinatives and numerals ----------
# (det, look, ru, en, example translit, example ru, example en)
DETS = [
    ('d', 'blue', 'бог — перед именем', 'god — before the name', '{d}en-lil₂', 'Энлиль', 'Enlil'),
    ('ki', 'green', 'место, город — после', 'place, city — after', 'unug{ki}', 'Урук', 'Uruk'),
    ('ĝiš', 'yellow', 'дерево, деревянное — перед', 'wood, wooden — before', '{ĝiš}ma₂', 'лодка', 'boat'),
    ('id₂', 'green', 'река, канал — перед', 'river, canal — before', '{id₂}buranun', 'Евфрат', 'Euphrates'),
    ('na₄', 'yellow', 'камень — перед', 'stone — before', '{na₄}za-gin₃', 'лазурит', 'lapis lazuli'),
    ('tug₂', 'yellow', 'ткань, одежда — перед', 'cloth, garment — before', '{tug₂}niĝ₂-lam₂', 'праздничная одежда', 'fine garment'),
    ('mušen', 'red', 'птица — после', 'bird — after', 'uz{mušen}', 'утка', 'duck'),
    ('ku₆', 'red', 'рыба — после', 'fish — after', 'suḫur{ku₆}', 'карп', 'carp'),
    ('dug', 'yellow', 'сосуд — перед', 'vessel — before', '{dug}sila₃', 'кувшин-сила', 'sila jar'),
]
# numerals: (sign name, value, ru, en)
NUMERALS = [('1(DIŠ)', 1), ('2(DIŠ)', 2), ('3(DIŠ)', 3), ('4(DIŠ)', 4), ('5(DIŠ)', 5), ('6(DIŠ)', 6), ('7(DIŠ)', 7), ('8(DIŠ)', 8), ('9(DIŠ)', 9),
            ('1(U)', 10), ('2(U)', 20), ('3(U)', 30), ('4(U)', 40), ('5(U)', 50), ('1(GEŠ₂)', 60)]
# determinative drill: word with determinative -> det key
DET_DRILL = ['{d}utu', '{d}en-ki', '{d}nanna', 'nibru{ki}', 'eridu{ki}', 'uri₅{ki}', '{ĝiš}ma₂', '{ĝiš}tukul', '{na₄}kišib', '{na₄}za-gin₃', '{id₂}idigna', '{id₂}buranun', 'uz{mušen}', 'suḫur{ku₆}', '{tug₂}niĝ₂-lam₂']
DET_OPTS = ['d', 'ki', 'ĝiš', 'na₄', 'id₂', 'mušen', 'ku₆', 'tug₂']

# ---------- 12 top verbs (ePSD2): ru translations of the guide words ----------
TOPV_RU = {
    ('hulu', 'bad'): ('быть плохим; портить', 'be bad; spoil'), ('us', 'follow'): ('следовать, примыкать', 'follow, border on'), ('teŋ', 'near'): ('приближаться', 'approach'),
    ('niga', 'fattened'): ('быть откормленным', 'be fattened'), ('šu teŋ', 'accept'): ('принимать (букв. «рукой приблизить»)', 'accept (lit. “bring near by hand”)'),
    ('lal', 'small'): ('быть малым; недоставать', 'be small; be lacking'), ('dab', 'seize'): ('хватать, брать', 'seize, take'), ('du', 'build'): ('строить, делать', 'build, make'),
    ('du', 'go'): ('идти', 'go'), ('sag', 'rare'): ('быть отборным, редким', 'be fine, rare'), ('huŋ', 'hire'): ('нанимать', 'hire'), ('gub', 'stand'): ('стоять; служить', 'stand; serve'),
    ('ŋar', 'place'): ('ставить, класть', 'place, put'), ('gal', 'big'): ('быть большим', 'be big'), ('ŋal', 'be'): ('быть, находиться', 'be (there)'), ('bala', 'turn'): ('вращаться; срок службы', 'turn; term of office'),
    ('zig', 'rise'): ('подниматься; набирать', 'rise; levy'), ('ak', 'do'): ('делать', 'do, make'), ('dug', 'speak'): ('говорить', 'speak, say'), ('uš', 'die'): ('умирать', 'die'),
    ('pad', 'find'): ('находить; называть', 'find; name'), ('ŋen', 'go'): ('идти, приходить', 'go, come'), ('hi', 'mix'): ('смешивать', 'mix'), ('kalag', 'strong'): ('быть сильным', 'be strong'),
    ('zal', 'pass'): ('проходить (о времени)', 'pass (of time)'), ('sug', 'replace'): ('возмещать, возвращать долг', 'repay, replace'), ('e', 'leave'): ('выходить', 'go out, leave'),
    ('mah', 'great'): ('быть великим', 'be great'), ('dirig', 'exceed'): ('превышать', 'exceed'), ('dim', 'create'): ('создавать, изготовлять', 'create, fashion'),
    ('la', 'hang'): ('вешать; взвешивать, платить', 'hang; weigh, pay'), ('me', 'be'): ('быть, являться', 'be'), ('gi', 'turn'): ('возвращаться', 'turn, return'), ('kur', 'enter'): ('входить', 'enter'),
    ('tuku', 'acquire'): ('получать, иметь; жениться', 'acquire, have; marry'), ('šum', 'give'): ('давать', 'give'), ('tur', 'small'): ('быть маленьким, юным', 'be small, young'),
    ('de', 'carry'): ('нести, приносить', 'carry, bring'), ('kug', 'pure'): ('быть чистым, священным', 'be pure, holy'), ('gu', 'eat'): ('есть', 'eat'),
    ('gid', 'long'): ('быть длинным; обмерять поле', 'be long; survey'), ('zid', 'right'): ('быть верным, истинным', 'be right, true'), ('zu', 'know'): ('знать', 'know'),
    ('dug', 'good'): ('быть хорошим, сладким', 'be good, sweet'), ('kud', 'cut'): ('резать, отрезать', 'cut'), ('sa', 'pay for'): ('покупать', 'buy'), ('il', 'raise'): ('поднимать, нести', 'raise, carry'),
    ('de', 'pour'): ('лить', 'pour'), ('kešed', 'bind'): ('связывать', 'bind'), ('tuš', 'sit'): ('сидеть, жить', 'sit, dwell'), ('ba', 'allot'): ('делить, выдавать', 'allot, share'),
}
