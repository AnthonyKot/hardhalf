# wc0484-Q4 Maximum Bitwise AND After Increment Operations — review note (2026-09-08)

## Original text

- Tempting 2: "Binary search exploring mid=3 marks False and contracts hi=2; it returns 1 instead of 5" on [5], k=0, m=1. glm-5-cloud-t0.0 returns 5. lo=0, hi=2^31 (or 2^31−1), mid=(lo+hi+1)//2 probes exactly ans|(1<<b), b=30..0: bit-greedy equivalence on 2000 random inputs (`probes.py`). "Happened to pass" is wrong; these files are correct. hi=max(nums)+k fails (deepseek-flash py, glm/kimi js: 661–667/1032): [2], 0, 1 → 0, expected 2.
- Tempting 3: "[7, 8], k = 1, m = 2" isn't a top-m counterexample (both selected; optimum=8). Reference/random-search counterexamples: [5,3,3], k=0, m=2 (top-two→1, answer=3); [12,5,5], k=2, m=2 (top-two→4, answer=6).
- Tempting 1: C(50000,2)=1249975000 correct; "10x over TLE" unfounded. Recorded replacements: claude-haiku java cost formula target|(x&~target) (637/1032; [1,5], k=2, m=2 → 1, expected 2); kimi cpp lowest-missing-bit-first loop (TLE 992/1032; 2^b−2 iterations for x=1, mask=2^b−1; local harness: 14.6s vs others' ≤1s); qwen py LIMIT=30 (1030/1032; [10^9], 73741824, 1 → 1073741823, expected 2^30).
- "17 accepted": recorded 19/25.

## Verification

`experiments.py`: exhaustive brute force (all m-subsets/increment distributions, k≤6) vs sonnet/deepseek-pro/kimi Python: 3000 tiny inputs, 0 mismatches. `harness.py`: 3 LeetCode testcases + 50 random/edge inputs (five n=50000; counterexamples above); deepseek-pro py expectations.

53/53: python3 claude-sonnet-4-6, deepseek-v4-pro-cloud-t0.0/t1.0, kimi, glm; java deepseek-flash, deepseek-pro, qwen, codex-agent, glm; javascript deepseek-pro; golang qwen, minimax, kimi; cpp kimi (correct, slow). Reproduced failures: deepseek-flash py 27/53, glm js 27/53, kimi js 27/53, haiku java 28/53, qwen py 47/53. Commented shipped code: 53/53, python3/java/javascript/golang. No accepted C++ exists; none shipped.
