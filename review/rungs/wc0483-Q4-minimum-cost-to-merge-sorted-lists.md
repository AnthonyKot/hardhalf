# wc0483-Q4 Minimum Cost to Merge Sorted Lists — review note (2026-09-08)

## Original text

- Tempting 1, its own example [1],[2],[1000]: "final cost 3+(2+1+998)=1004". median([1,2]) = 1, so the second merge costs 2+1+999 = 1002 and greedy totals 1005. "[1]+[2,1000] (cost=1+2+|1−500|=502)": median([2,1000]) is the left middle, 2; cost 4; that order totals 1000+4 = 1004. So "greedy wins here" is false: the example is itself a counterexample (greedy 1005, optimal 1004; brute force over all merge orders agrees). No other failing input was given.
- Tempting 2: no failing input. Found [[6],[3],[6]]: interval DP 11, optimal 8.
- Tempting 3: "the 2 TLE submissions likely fell into" per-transition median recomputation. Record: 5 TLE + 1 WA. All five TLE files precompute medians (two deepseek Python files via heapq.merge per subset; claude-haiku java re-merges lists on every improving split; two qwen files use a tuple-of-lists state DP). The WA (codex-low java, 586/881) stacks two symmetry filters and skips splits; fails on [[5],[1],[3]] (11 vs 9).
- Essence: "531 441 submask transitions" is 3^12; exact pair count 3^12 − 2^13 + 1 = 523 250.

## Verification

Scratch dir: `experiments.py` (brute force over merge orders, bitmask reference, greedy, interval DP, the codex-low filter; 4000 random n ≤ 5 inputs, bitmask == brute on all; minimal counterexamples by random search), `harness.py` (4 LeetCode testcases + 36 random, n up to 12 and 2000 elements, expected from the reference; per-language drivers), `timing.py` (one n = 12, 2000-element input).

40/40: python3 claude-sonnet-4-6, kimi-k2.5-cloud-t0.0, deepseek-v4-pro-cloud-t1.0, and both deepseek TLE files (slow, not wrong); java kimi-k2.5-cloud-t0.0-java, qwen3.5-cloud-t1.0-java; cpp kimi; javascript kimi, deepseek-v4-pro; golang minimax-m2.7-cloud-t0.0-golang, kimi. codex-low java: 16/40. Timing on the max input: sonnet py 0.14 s, deepseek heapq versions 0.43/0.59 s, kimi java 0.07 s, haiku java (with the missing `import java.util.*` added) 0.27 s. Shipped code with comments re-run: 40/40 in all five languages.

## Unsettled

LeetCode's runtime figures are totals over 881 tests; local timings are one input.
