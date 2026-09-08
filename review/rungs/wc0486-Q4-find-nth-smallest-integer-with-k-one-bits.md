# wc0486-Q4 Find Nth Smallest Integer With K One Bits — rung review (2026-09-08)

## Original text
- Tempting 2: "C(50, 25) ~ 1.26 * 10^14 combinations -- a 14-trillion element array ... 800 TB". C(50,25) = 126,410,606,437,752 = 126 trillion; × 8 bytes = 1.01 PB.
- Tempting 2: "Only works for tiny k (k <= 6 or so)". C(50,6) = 15,890,700, C(50,7) = 99,884,400; no defensible threshold. Dropped.
- Tempting 1/3: "10^15 * 1ns = 10^6 seconds" — arithmetic fine, rate invented; replaced with a measured one.
- Essence: "O(50 * k) time" — true only when binomials are recomputed per step; restated.
- Nothing in the original covered the walk itself, where a solver who has the idea still fails.

## Verified
- Reference walk vs brute force: every x < 2^18 bucketed by popcount, 262,143 (n, k) cases, 0 mismatches (`scratchpad/wc0486/checks.py`).
- Six large cases from the reference walk (e.g. n = C(50,25), k = 25 → 2^50 − 2^25; n = 50, k = 1 → 2^49) fed to every shipped language.
- `>=` walk on samples: 10 and 8. int32 Pascal table simulated in Python: C(34,17) wraps to −1,961,361,076; (2,333,606,220, 17) → 1,118,254,868,758,793 vs 17,179,738,112.
- Gosper loop timed in Python: 2×10^6 steps in 0.32 s → 6.3×10^6/s; 2^40 steps ≈ 2.0 days. Both TLE submissions (Qwen3-Coder, python3) are this loop.
- Scan size for (2^40, 20): answer 9,952,741,884,412 → 2.8 h at 10^9/s.

## Solutions tested (2/2 testcases + 6 large cases, 8/8 each)
python3 qwen3.5-cloud (shipped), deepseek-v4-pro-cloud-t0.0, deepseek-v4-flash-cloud-t0.0; java codex-low-gpt-5.4-mini-java; cpp kimi-k2.5-cloud-t0.0-cpp; javascript kimi-k2.5-cloud-t0.0-javascript; golang kimi-k2.5-cloud-t0.0-golang. Comments added, logic untouched, shipped text re-run.

## Unsettled
Nothing.
