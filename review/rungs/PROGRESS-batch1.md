# Batch 1 checkpoint — 2026-09-08 (quota stop at 82%)

## Status
1. wc0483-Q3-minimum-cost-to-make-two-binary-strings-equal — DONE, committed (5 languages).
2. wc0486-Q4-find-nth-smallest-integer-with-k-one-bits — DONE, committed (5 languages).
3. wc0487-Q4-longest-alternating-subarray-after-removing-at-most-one-element — DONE, committed (5 languages); note trimmed to 256 words in this checkpoint.
4. wc0482-Q4-number-of-balanced-integers-in-a-range — PARTIAL. JSON holds python3 + javascript (verified, no step comments yet) and two `changes`. Missing: idea_html, pitfalls_html, java/cpp/golang verification, review note.

## Rung 4 — verified facts not yet in the rung file
- Harness: scratchpad/wc0482/ref.py builds cases.txt (416 cases: 3 samples, 406 random ranges ≤ 1e6 with brute-force expected, 7 large ranges from a padded DP). Padded DP (alternating sum over the zero-padded 16-digit string, no started/parity flag) vs brute force: 409/409. So original tempting 3 (leading zeros break parity) is false.
- Reference values: balanced count in [1, 1e6] = 55,251; in [1, 1e15] = 32,811,494,188,974 (1e15 itself is not balanced).
- Passed 416/416: python3 deepseek-v4-pro-cloud-t0.0 (34 lines, pick), qwen3.5-cloud-t1.0, kimi-k2.5-cloud-t0.0; javascript deepseek-v4-pro-cloud-t0.0-javascript (pick), deepseek-v4-flash-cloud-t0.0-javascript.
- Not yet run: java deepseek-v4-flash-cloud-t0.0-java (45 lines, 95 ms, 5-D memo array), cpp kimi-k2.5-cloud-t0.0-cpp (50 lines, memo only on non-tight), golang minimax-m2.7-cloud-t0.0-golang (70 lines, map memo) or qwen3.5-cloud-t1.0-golang (105 lines, 38 ms). Drivers for (long, long) -> long still to write; cases.txt format is `low high expected` per line.
- Failure record: 5 of 34. Two Python TLEs are the brute-force loop (tempting 1 confirmed). Three Java TLEs: claude-haiku-4-5-java and eff-low-claude-haiku-4-5-java use HashMap<String, Long> memo with string keys; java-t08 Qwen3-Coder fills a dp array but never reads it (no memo lookup), so it is exponential. Timings not measured.
- Tempting 1 arithmetic error: 1.6e16 / 1e9 = 1.6e7 s (16 million), text says 18 million.
- Tempting 2 (sharing one lru_cache across f(high) and f(low-1) with tight in the key) NOT verified; needs a shared-cache implementation run over cases.txt.
- State count for the idea: pos 16 x diff (-72..72 = 145) x tight 2 x started 2 x parity 2 ≈ 18,560 states x 10 digits ≈ 2e5 operations per bound.
- Sample 1 walk for the idea: f(100) counts 3-digit strings d1 d2 d3 ≤ 100 with d1 - d2 + d3 = 0: d1 = 0 gives d3 = d2, 10 strings (000, 011, ..., 099); d1 = 1 forces 100, sum 1, none. f(100) = 10 (includes 0), f(0) = 1, answer 9.
