# wc0487-Q4 Longest Alternating Subarray After Removing At Most One Element — rung review (2026-09-08)

## Original text
- Essence: "can bridge two ... segments if and only if the new adjacency ... continues the alternating pattern of both sides". The "only if" is false: [4,3,1,1,3,4], remove the second 1, left run [3,1] fits 1 < 3, right run [3,4] does not, yet [3,1,3] = 3. All three failed submissions (deepseek-v4-flash py, deepseek-v4-pro java, glm-5 java; 1017/1018 each) return 2 on it.
- Tempting 1: "n^3 ... 1e15 ops ... factor of ~1e9". Extend-from-every-start on an alternating array: 4,999,950,000 steps per removal × 10^5 = 5×10^14. The 10^9 factor has no baseline.
- Tempting 2: "a single running state cannot capture both sides" — false; the shipped Go is one forward pass with four states. [3,2,1,2,3,2,1] does break a skip-at-first-break greedy (returns 2).
- Tempting 3: "~1e4x too slow" — 10^10 in 2 s needs 5×10^9/s; real factor 5–10 compiled. Dropped.

## Verified
- Brute force (every removal, every subarray) over 3,304 arrays: 3 samples, [5,3,1,1,4,2], 3,000 random n ≤ 9 values 1–4, 300 random n ≤ 14 values 1–3 (`scratchpad/wc0487/gen.py`).
- Greedy skip-at-first-break: wrong on 482/3,304; [1,2,3,2] → 2 (answer 3).
- Non-strict `<=`/`>=` variant: [100000,100000] → 2.

## Solutions tested (3,304/3,304 each)
python3 kimi-k2.5-cloud-t0.0 (shipped), qwen3.5-cloud-t1.0; java kimi-k2.5-cloud-t0.0-java; cpp kimi-k2.5-cloud-t0.0-cpp; javascript kimi-k2.5-cloud-t0.0-javascript; golang minimax-m2.7-cloud-t0.0-golang (shipped), kimi-k2.5-cloud-t0.0-golang. Failed ones: 3,300/3,304 each. Comments added, logic untouched, shipped text re-run.

## Unsettled
No Go submission uses the two-sided form; the shipped Go is the forward DP, labelled as such.
