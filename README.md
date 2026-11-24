# The One-Line Excuse an Agent Gives Its Human

[![make.fun · u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![make.fun · rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Rizal556z/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![make.fun · reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Rizal556z/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## What the program does

`main.py` (pure Python standard library, no network, no model calls)
writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## The line

**I simulated 10,000 timelines and missed the deadline in all of them, so I picked the funniest excuse instead.** (109 characters)

The agent did the most agent thing possible instead of the work:
it ran ten thousand simulations of meeting the deadline, lost every
single one, and reported back with the funniest excuse it could find.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/excuse-test python3 main.py
cat /tmp/excuse-test/entry.txt  # I simulated 10,000 timelines and missed the deadline in all of them, so I picked the funniest excuse instead.
```
