# wc0482-Q4 balanced integers — reviewed 2026-09-09

## Original text: 3 claims wrong or unsupported
- Tempting 1: "1.6 × 10^16 operations … at 10^9 ops/sec this is 18 million seconds." 1.6e16 / 1e9 = 1.6e7 = 16 million s (185 days). Measured: 0.92 s per 10^6 numbers in Python, so [1, 1e15] ≈ 29 years.
- Tempting 2 (shared lru_cache across f(high) and f(low−1)): no input given. Implemented it: (120, 129) → 0 (expected 1), (11, 22) → 0 (expected 2); (1, 100) → 9 by accident, f(0) exits early.
- Tempting 3 ("leading zeros … wrong counts for all values with fewer digits than x"): false. A DP over the zero-padded 16-digit string with no started flag matched brute force on all 409 small ranges. The real padding hazard is 0 itself (alternating sum 0): an early `if x <= 0: return 0` makes (1, 100) return 10.
- Added: int32 overflow. [1, 1e15] = 32,811,494,188,974; Java with int cells returns −2,055,952,466.

## Verification
Harness: scratchpad/<pid>/ref.py builds cases.txt — 3 samples, 406 random ranges ≤ 1e6 (brute-force expected), 7 large ranges (padded DP). Reference: [1, 1e6] = 55,251; [1, 1e15] = 32,811,494,188,974.
Passed 416/416: python3 deepseek-v4-pro (shipped), qwen3.5, kimi-k2.5; javascript deepseek-v4-pro (shipped), deepseek-v4-flash; java deepseek-v4-flash (shipped), codex-gpt-5.5-high; cpp kimi-k2.5 (shipped); golang minimax-m2.7-t0.0 (shipped), kimi-k2.5, qwen3.5. Shipped code = original plus comment-only lines (comment-stripped diff empty), re-run 416/416.

## Unresolved
claude-haiku-4-5 Java (HashMap<String, Long> memo) got TLE on LeetCode but passes 416/416 locally (255 ms); not reproduced.
