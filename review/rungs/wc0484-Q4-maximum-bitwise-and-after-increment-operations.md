# wc0484-Q4 Maximum Bitwise AND After Increment Operations — review note (2026-09-08)

## Original text

- Tempting 2: "Binary search exploring mid=3 marks False and contracts hi=2; it returns 1 instead of 5" on [5], k=0, m=1. Ran glm-5-cloud-t0.0's code: returns 5. With lo=0, hi=2^31 (or 2^31−1) and mid=(lo+hi+1)//2 the probe sequence is exactly ans|(1<<b), b=30..0 — identical to the bit-greedy on 2000 random inputs (`probes.py`). "Happened to pass" is wrong; they are correct. The variant with hi=max(nums)+k (deepseek-flash py, glm js, kimi js: 661–667/1032) is the one that fails: [2], 0, 1 → 0, expected 2.
- Tempting 3: "[7, 8], k = 1, m = 2" is not a counterexample to top-m selection (both elements are the top 2; 8 is optimal). Re-derived: [5,3,3], k=0, m=2 (top two → 1, answer 3) and [12,5,5], k=2, m=2 (top two → 4, answer 6), by random search against the reference.
- Tempting 1: C(50000,2) = 1 249 975 000, fine; "10x over TLE" unfounded. Replaced by recorded failures: claude-haiku java cost formula target|(x&~target) (637/1032; fails [1,5], k=2, m=2 → 1, expected 2), kimi cpp lowest-missing-bit-first loop (TLE 992/1032; 2^b−2 iterations for x=1, mask 2^b−1; 14.6 s locally on the harness vs ≤ 1 s for others), qwen py LIMIT=30 (1030/1032; [10^9], 73741824, 1 → 1073741823, expected 2^30).
- "17 accepted": record says 19/25.

## Verification

`experiments.py`: exhaustive brute force (all m-subsets, all increment distributions, k ≤ 6) vs sonnet/deepseek-pro/kimi Python on 3000 tiny inputs: 0 mismatches. `harness.py`: 3 LeetCode testcases + 50 random/edge inputs (five at n=50000, the counterexamples above), expected from deepseek-pro py.

53/53: python3 claude-sonnet-4-6, deepseek-v4-pro-cloud-t0.0/t1.0, kimi, glm; java deepseek-flash, deepseek-pro, qwen, codex-agent, glm; javascript deepseek-pro; golang qwen, minimax, kimi; cpp kimi (correct, slow). Failures reproduced: deepseek-flash py 27/53, glm js 27/53, kimi js 27/53, haiku java 28/53, qwen py 47/53. Shipped code with comments: 53/53 in python3, java, javascript, golang. No accepted C++ exists; none shipped.
