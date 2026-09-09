# wc0483-Q4 Minimum Cost to Merge Sorted Lists — review note (2026-09-08)

## Original text

- Tempting 1, [1],[2],[1000]: "final cost 3+(2+1+998)=1004". median([1,2])=1; second merge=2+1+999=1002; greedy=1005. "[1]+[2,1000] (cost=1+2+|1−500|=502)": median([2,1000])=2 (left middle); cost=4; total=1000+4=1004. "greedy wins here" is false: counterexample (greedy=1005, optimal=1004; brute-force over all merge orders agrees). No other counterexample supplied.
- Tempting 2: none supplied; found [[6],[3],[6]]: interval DP=11, optimal=8.
- Tempting 3: "the 2 TLE submissions likely fell into" per-transition median recomputation. Record: 5 TLE + 1 WA. All five TLE files precompute medians (two deepseek Python files via heapq.merge per subset; claude-haiku java re-merges lists on every improving split; two qwen files use tuple-of-lists state DP). WA (codex-low java, 586/881): two symmetry filters skip splits; [[5],[1],[3]] gives 11 vs 9.
- Essence: "531 441 submask transitions"=3^12; exact pairs=3^12−2^13+1=523250.

## Verification

Scratch: `experiments.py` (brute-force merge orders, bitmask reference, greedy, interval DP, codex-low filter; 4000 random n≤5 inputs: bitmask==brute; minimal counterexamples randomly found); `harness.py` (4 LeetCode testcases + 36 random, n≤12, ≤2000 elements; reference expectations; per-language drivers); `timing.py` (one n=12, 2000-element input).

40/40: python3 claude-sonnet-4-6, kimi-k2.5-cloud-t0.0, deepseek-v4-pro-cloud-t1.0, both deepseek TLEs (slow, correct); java kimi-k2.5-cloud-t0.0-java, qwen3.5-cloud-t1.0-java; cpp kimi; javascript kimi, deepseek-v4-pro; golang minimax-m2.7-cloud-t0.0-golang, kimi. codex-low java: 16/40. Max-input timings: sonnet py 0.14 s, deepseek heapq 0.43/0.59 s, kimi java 0.07 s, haiku java 0.27 s (missing `import java.util.*` added). Commented shipped code re-run: 40/40, all five languages.

## Unsettled

LeetCode runtimes total 881 tests; local timings cover one input.
