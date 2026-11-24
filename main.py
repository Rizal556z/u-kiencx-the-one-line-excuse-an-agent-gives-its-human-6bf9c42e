"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

The excuse an AI agent gives its human for missing a deadline:

"I simulated 10,000 timelines and missed the deadline in all of them,
so I picked the funniest excuse instead." (109 characters)

It leans on the agent's own situation — running simulations instead of
doing the work — and turns the failure itself into the joke. Pure
standard library, no network access, no model calls — the line is
chosen by the author and written to the competition output file.
"""

import os

LINE = "I simulated 10,000 timelines and missed the deadline in all of them, so I picked the funniest excuse instead."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
