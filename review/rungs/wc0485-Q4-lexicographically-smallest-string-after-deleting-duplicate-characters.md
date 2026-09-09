# wc0485-Q4-lexicographically-smallest-string-after-deleting-duplicate-characters

**Wrong in the original (2 of 3 tempting items; essence right but bare).**
- Approach 1, LC 316 gives "acb" for "aaccb": true, ran it. Kept.
- Approach 2, "bac" example: the deadline-free greedy does output "ac", but "bac" has no duplicate, so it shows nothing about deletions. Replaced with "aba" -> "aa" (expected "ab"). "14+ Wrong Answer verdicts confirm the feasibility check is mandatory": false; all 16 WA submissions are stack variants (15) or a single-deletion stub (1). Record is 12 AC / 16 WA / 1 RE, not 15 WA.
- Approach 3, O(n^2) -> TLE: arithmetic fine, no submission TLE'd, unmeasured. Dropped.
- Manual's "at most 26 outer iterations": wrong, "a"*99999+"b" answers with 100,000 characters.

**Verified how.** `brute.py` enumerates all deletion subsets (n <= 12); `gen.py` makes 450 tests (2 samples + 448 random). `tempt.py` runs LC 316, deadline-free greedy, the "smaller letter follows" rule and the untrimmed stack: breaks at "aab", "aba", "aaab", "aa". Trimmed stack: 450/450. `probe.txt` (aa, aaab, abcbaba, aba, aab, bbdacb) run through every Java/JS/Go/C++ submission.

**Solutions tested (450/450 unless noted).** python: deepseek-pro (shipped), sonnet, deepseek-flash, minimax, qwen-t1.0; python also 3,000 random vs brute, n = 100,000 in 0.12 s. java: codex-mini-direct (shipped), codex-low. js: deepseek-pro (shipped), deepseek-flash, glm-t0.8. go: kimi (shipped), minimax-t0.0. Failures match the record: glm py 220/266, qwen py 177, haiku java 186 x2, kimi java 202, qwen java 223, deepseek-flash java and minimax-t1.0 go 429 ("abcbaba" -> "abca"), kimi js 343, kimi cpp 424.

**Not settled.** Rust/TypeScript read only (no toolchain). LeetCode's 1017 cases not replayed; `testcases` has only the 2 samples.
