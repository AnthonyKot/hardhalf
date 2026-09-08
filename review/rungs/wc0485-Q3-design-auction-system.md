# wc0485-Q3-design-auction-system — review note (2026-09-08)

**Wrong in the original text (3 of 3 tempting items had bad arithmetic; 1 of them a wrong verdict).**
- "5e4 getHighestBidder calls, each scanning up to 5e4 entries = 2.5e9": the 5e4 cap is on *total* calls. Worst split is 25,000 adds + 25,000 queries = 6.25e8. Verdict (TLE) holds: 13.0 s in Python, 3.2 s in Java on that exact input; record shows 3 such submissions TLE at 497–498/509.
- "bisect.insort ... 5e4 * 5e4 = 2.5e9 element moves. TLE": false. 50,000 inserts at index 0 took 0.20 s (memmove). Dropped.
- "heap.remove ... 2.5e9 ops": same cap error (6.25e8). Verdict holds: 24.6 s measured.
- Essence: "a sorted structure inverts this" conflates a sorted array with an ordered set.

**Verified how.** Scratch dir `<scratchpad>/wc0485-Q3-design-auction-system/`: `gen.py` makes 43 tests (official sample; 40 random call sequences checked against a brute-force dict scan; 25k-add/25k-query stress; 50k mixed ops with expected from a lazy heap cross-checked against brute force on a 3,000-call prefix). Text-format runners for py/java/cpp/js/go (`run_py.py`, `Main.java`, `main.cpp`, `run_js_tail.js`, `main_go.txt`), `check.sh` compares outputs. Pitfall inputs run in `tempt.py` and `tie.in`.

**Solutions tested.** 43/43: python kimi-k2.5-cloud (shipped), deepseek-flash/pro, glm-t0.0, qwen-t1.0; java codex-mini-direct (shipped), kimi, deepseek-flash; cpp kimi (shipped); js kimi (shipped); go kimi (shipped), qwen, minimax. Failed as on record: codex-agent-gpt-5.5-high java 24/43 (tie-break reversed; `tie.in` returns 3, expected 5); minimax python 0/43 (class named `Solution`).

**Not settled.** LeetCode's Runtime Error for glm-5-cloud (py) and deepseek-v4-pro-cloud-t0.0-javascript: both pass 43/43 here. claude-sonnet-4-6's SortedList solution not run (no `sortedcontainers` locally). No hidden testcases exist for this design problem (`testcases` is empty), so LeetCode's 509 cases were not replayed.
