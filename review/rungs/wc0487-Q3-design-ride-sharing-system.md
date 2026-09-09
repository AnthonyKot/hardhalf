# wc0487-Q3 Design Ride Sharing System — review note (2026-09-08)

## Original text

- Essence: accurate mechanism. "If either queue has no eligible member" overstates: drivers cannot be cancelled; only riders become ineligible. Simplified.
- Tempting 1 (min-heap): correct; Example 1’s first match returns [2, 1], expected [2, 3].
- Tempting 2 (deque.remove): "1000 * 1000 / 2 = ~5e5" requires 1000 riders+1000 cancels, exceeding 1000-total-calls. No counterexample supplied. Unguarded `deque.remove`: ValueError on Example 1's `cancelRider(3)` (already matched). Guarded removal accepted (glm-5-cloud python, kimi/qwen java, deepseek js).
- Tempting 3: "returns [driverId, canceledRiderId] ... most likely root cause of the 1 Wrong Answer". Executed emptiness-check/drain/pop: Example 2 gives IndexError, not a wrong pair. WA (claude-sonnet-4-6, 800/844) drains before checking; unguarded `cancelled.add(riderId)` makes `cancelRider(7), addRider(7), addDriver(1), match` return [-1, -1], expected [1, 7]. Which of LeetCode’s 844 inputs failed is unrecorded. Replaced.
- Unmentioned failures: 3/5 NameError (class `Solution`), 1 empty-stub IndentationError (`submissions/*/error_msg`).

## Verification

`leetcode_problems/<pid>.json`: `testcases: []`; only 2 examples. Scratch harness: Python reference, 2 examples (statement expectations), 300 random constrained sequences (unique ids; waiting/matched/never-added cancellations; ≤1000 calls). Per-language drivers: `python3`, `javac`/`java`, `g++ -std=c++17`, `node`, `go build`.

302/302 each: python3 kimi-k2.5-cloud-t0.0, glm-5-cloud, deepseek-v4-flash-cloud-t0.0; java codex-agent-gpt-5.5-java, kimi-k2.5-cloud-t0.0-java; cpp kimi-k2.5-cloud-t0.0-cpp; javascript glm-5-cloud-t0.8-javascript, kimi-k2.5-cloud-t0.0-javascript; golang kimi-k2.5-cloud-t0.0-golang, minimax-m2.7-cloud-t1.0-golang. claude-sonnet-4-6: 114/302 (all failures: cancel-before-add); qwen3.5-cloud: 0/302 (NameError). Shipped code (comments added; JS boilerplate comment removed): re-run 302/302, all five languages.

## Unsettled

Random agreement with the reference does not establish passing LeetCode's 844 tests; shipped files have LeetCode Accepted verdicts.
