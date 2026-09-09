# wc0489-Q3-longest-almost-palindromic-substring — review note (2026-09-08)

**Wrong or unverifiable in the original.**
- Approach 2: "for `zzabba`, without re-expanding after the skip, the algorithm would not find ... length 5". False: boundary-only expansion returns 5 (core "abba" at right edge). Sample 1: `abca` gives 2, expected 4; shortest failure over a–c: `abbc`.
- Approach 1 arithmetic (3.9e13, 1.56e10) is right; "~10^8 limit" replaced by measurements.
- Approach 3 (deletion-set DP): no submission wrote it; dropped.
- "O(n^2) is the target": right exponent, but 5 of 7 Python TLEs were O(n^2) tables.

**Verified how.** `gen.py`: greedy matched O(n^4) brute force on all binary strings ≤9 and ternary ≤6; 39 tests = 3 samples + 30 random (brute-force expected) + 6 inputs of n=2500. `tempt.py` runs four tempting variants against the brute force and reports the shortest breaking input. Timings: O(n^3) submission 3.72 s at n=1000 (a×1000); O(n^4) 67.7 s at n=1000 (random binary); n×n Python tables 1.0–1.3 s at n=2500 here vs LeetCode's 5427 ms for the rolling variant (0.46 s here). Greedy comparisons at n=2500: 3,126,250 (a×2500), 4,688,749 ((ab)×1250).

**Solutions tested (39/39 unless noted).** Python: qwen-t1.0 (shipped) and 8 others. Java: deepseek-flash (shipped) + 4. C++: kimi (shipped). JS: deepseek-pro (shipped) + 3. Go: minimax t1.0 (shipped), t0.0; kimi 29/39 (`baca` → 3, expected 4) and qwen 2/39 (`abca` → 3) match their WA verdicts.

**Not settled.** The ~12× grader-vs-local Python ratio rests on one data point. `kimi-k2.5-cloud.py` is corrupted in the checkout (terminal escape mid-line) and cannot run.
