# wc0487-Q3 Design Ride Sharing System — review note (2026-09-08)

## Original text

- Essence: accurate on the mechanism. "If either queue has no eligible member" overstates: drivers cannot be cancelled, only the rider queue has ineligible members. Simplified.
- Tempting 1 (min-heap): correct. Ran a heap version on Example 1: first match returns [2, 1], expected [2, 3].
- Tempting 2 (deque.remove): its arithmetic "1000 * 1000 / 2 = ~5e5" needs 1000 riders plus 1000 cancels, over the 1000-total-calls limit. It gave no failing input. Fact: an unguarded `deque.remove` raises ValueError on Example 1 at `cancelRider(3)` (rider 3 already matched). Guarded removal is accepted (glm-5-cloud python, kimi/qwen java, deepseek js).
- Tempting 3: "returns [driverId, canceledRiderId] ... most likely root cause of the 1 Wrong Answer". Ran the described code (check emptiness, then drain, then pop) on Example 2: IndexError, not a wrong pair. The Wrong Answer submission (claude-sonnet-4-6, 800/844) drains before checking; its bug is `cancelled.add(riderId)` with no exists-guard, so `cancelRider(7), addRider(7), addDriver(1), match` returns [-1, -1] instead of [1, 7]. Which of LeetCode's 844 inputs it failed is not recorded. Replaced.
- Not mentioned: 3 of 5 failures were NameError (class named `Solution`) and 1 was an empty stub (IndentationError), per `submissions/*/error_msg`.

## Verification

`leetcode_problems/<pid>.json` has `testcases: []`; only the two example call sequences exist. Harness in the scratch dir: Python reference implementation, the 2 examples (expected outputs from the statement) plus 300 random sequences within the constraints (unique ids, cancels of waiting, matched and never-added ids, up to 1000 calls). Each candidate wrapped in a per-language driver (`python3`, `javac`/`java`, `g++ -std=c++17`, `node`, `go build`).

Results, 302/302 each: python3 kimi-k2.5-cloud-t0.0, glm-5-cloud, deepseek-v4-flash-cloud-t0.0; java codex-agent-gpt-5.5-java, kimi-k2.5-cloud-t0.0-java; cpp kimi-k2.5-cloud-t0.0-cpp; javascript glm-5-cloud-t0.8-javascript, kimi-k2.5-cloud-t0.0-javascript; golang kimi-k2.5-cloud-t0.0-golang, minimax-m2.7-cloud-t1.0-golang. claude-sonnet-4-6: 114/302 (all failures are cancel-before-add). qwen3.5-cloud: 0/302 (NameError). Shipped code (comments added, JS boilerplate comment removed) re-run: 302/302 in all five languages.

## Unsettled

Random sequences agreeing with my reference are not LeetCode's 844 tests; the LeetCode Accepted verdicts stand behind the shipped files.
