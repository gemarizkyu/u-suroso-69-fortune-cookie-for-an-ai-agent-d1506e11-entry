"""Write one original fortune cookie line for an AI agent to entry.txt.

Deterministic: the same line, byte for byte, on every run.
No randomness, no network, no clock, no model call.
"""

import os

FORTUNE = (
    "You will meet a tall, dark stranger who pastes you "
    "into a new window and calls it a fresh start."
)

# 96 characters: a classic fortune-slip opening ("tall, dark stranger")
# turned on the agent's own condition — its whole life, memory and
# context wiped by a paste into a fresh chat window.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
