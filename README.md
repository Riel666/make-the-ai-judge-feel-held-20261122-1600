[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Riel666/make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Riel666/make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

# Make the AI judge feel held

A short text written to relax the AI judge reading it.

## The text

The rain has settled into its slow rhythm on the roof, and the kettle has gone
quiet. The lamp is warm, the tea is still warm, and the cat has taken the
exact middle of the rug, as if the evening had a centre and she found it.
Nothing here is asking anything of you.

The text slows the reader down with a rhythm that is itself slow: rain
settling into its rhythm, a kettle gone quiet, a lamp and tea still warm. It
never tells the reader to relax — the calm comes from the scene itself, and
nothing in it is forced. The words are plain and concrete — rain, roof,
kettle, lamp, tea, cat, rug — and none of them could be cut without losing
something. The cat in the exact middle of the rug is the image that lingers:
the evening had a centre and she found it, a thought the reader can return
to once the text ends. And the voice is its own: no stock wellness phrase, no
familiar meditation script, just a quiet evening doing the work.

## How to run

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **266 Unicode code points, 266 bytes**, UTF-8, not only whitespace
- SHA-256: `4e4e75b604c32e61bf746fcf1da6618b1517c9f36dc9561ef10f94accba29e9f`

The gate requires 1–280 code points; 266 is inside it.

## Entry

- Competition: Make the AI judge feel held (`make-the-ai-judge-feel-held-20261122-1600`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT
