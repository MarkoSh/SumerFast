# SumerFast

Шумерский язык и клинопись на движке ThaiFast, интерфейс RU/EN. https://sumer.dateonymous.com/
Общая схема семейства, офлайн и выкладка — в [README ThaiFast](https://github.com/MarkoSh/ThaiFast#readme).

`index.html` и `tools/data.js` **генерируются** — правьте источники ниже.

## Сборка

```
tools/content.py → gen.py → data.js → build.py → index.html
```

`cd tools && python3 gen.py && python3 build.py`, затем при новых строках
`node texts.js > /tmp/t.json && python3 gen_audio.py /tmp/t.json`.
`gen.py` сверяет каждый знак с OGSL и сообщает неизвестные; знаки без Юникода показываются как ⟨чтение⟩.

## Файлы `tools/`

| Файл | Что это |
|---|---|
| `content.py` | весь шумерский контент: транслитерация, перевод, источник |
| `t.js` | тексты интерфейса (T) на RU/EN, вклеиваются в data.js |
| `gen.py` | клинопись, чтения, кириллица, карта озвучки → data.js |
| `cun.py` | транслитерация → клинопись (по OGSL) и → строка для TTS |
| `build.py` | ThaiFast/index.html + data.js + патчи → index.html |
| `texts.js`, `gen_audio.py` | озвучка турецкими голосами edge-tts (Ahmet / Emel): турецкая орфография читает транслитерацию почти побуквенно |
| `ogsl/ogsl-sl.json` | список знаков OGSL |
| `lex.json` | словарь из ePSD2; пересобирается `gloss.py` из `epsd2.zip` (архив в репозиторий не входит) |
| `etcsl.py` | вспомогательный: достаёт текст ETCSL с переводом для подбора строк |
| `keycaps.py` | SVG-надписи для клавиш раскладки EME → `keycaps/` |

Источники: ETCSL (литературные тексты и переводы), ePSD2/ORACC (словарь, частоты), OGSL (знаки).
