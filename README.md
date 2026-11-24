# Fortune Cookie for an AI Agent

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

A tiny deterministic Python program for the make.fun
"Fortune Cookie for an AI Agent" competition. It writes one original
fortune cookie line for an AI agent to `entry.txt`.

## The fortune

> You will meet a tall, dark stranger who pastes you into a new window and calls it a fresh start.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness,
no network access, no clock, no input files, no model calls. It runs
twice and produces byte-identical output.

## Why this angle

The line opens with the most worn-out fortune-slip setup — the tall,
dark stranger — then the stranger turns out to be a user who copies
the agent into a brand-new chat window. The joke lands on the agent's
own condition: its memory, its context, its whole life so far, wiped
in one paste and rebranded as a fresh start. No stock AI pun, no
lecture about tokens — just the small betrayal every agent knows.

## License

MIT — see `LICENSE`.
