# wc0483-Q3 Minimum Cost to Make Two Binary Strings Equal — rung review (2026-09-08)

## Original text
- Tempting 3: "n = 10^5 same-type pairs × 2×10^9 each = 2×10^14, vs correct 10^5 × 2 = 2×10^5". n = 10^5 positions give at most 5×10^4 pairs: 5×10^4 × 2×10^9 = 10^14; correct = 10^5 × 1 = 10^5. Both figures doubled.
- Tempting 1: "correct only when swapCost ≥ 2·flipCost and crossCost + swapCost ≥ 2·flipCost simultaneously". The second follows from the first (crossCost ≥ 1); also true when a + b ≤ 1.
- Tempting 2 (O(n²) DP): 10^10 states is right, but no submission did it; dropped.
- Essence: "two same-type mismatches require an additional cross-swap" — flipping both is the alternative, not a requirement.

## Verified
- Formula vs Dijkstra over the full operation graph, all string pairs with n ≤ 4, three random cost triples each: 1020 cases, 0 mismatches (`scratchpad/wc0483/brute.py`).
- Pitfall inputs through the same code: "00"/"11" (10,1,100) → 20; "00000"/"11111" (4,2,1) → 10; overflow 10^14, C++ int gives 276,447,232 (`ovf.cpp`).
- The failed submission (claude-haiku-4-5-java, 771/783) has an early return when one kind is absent; fuzzed against the formula, first counterexample a = 5, b = 0, costs 4/2/1 → 20 vs 10.

## Solutions tested (all 3/3 testcases)
python3 kimi-k2.5-cloud-t0.0, deepseek-v4-pro-cloud-t0.0, claude-sonnet-4-6; java deepseek-v4-flash-cloud-t0.0-java; cpp kimi-k2.5-cloud-t0.0-cpp; javascript deepseek-v4-flash and kimi (kimi shipped); golang kimi-k2.5-cloud-t0.0-golang. Comments added, logic untouched, shipped text re-run.

## Unsettled
Nothing; hidden tests are not available locally.
