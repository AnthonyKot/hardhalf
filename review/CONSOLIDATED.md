# Cold-reader review — 2026-09-08

Three independent runs of `review/PROMPT.md` against the first pilot (commit 1): Gemini 3.7 Flash
and Gemini 3.1 Pro via agy, GPT-5.6 via codex. Raw outputs: `gemini-flash.md`, `gemini-pro.md`,
`codex.md`. Persona: engineer six weeks from a senior loop, twenty minutes tonight.

## Consensus (3 of 3)

- All three skip the 100%-accepted rungs and reject "Pick the lowest rung you have not cleared";
  "Nobody stumbled. Can you?" reads as absurd. **Applied:** ladder rebuilt from set-1 problems on
  which at least one submission failed (rates 0.97 → 0.41); rule removed; rubric shortened.
- None would press Start before reading the statement; the `<details>` fold is friction.
  **Applied:** statement open by default; "Open on LeetCode" is a button beside Start.
- The reveal's reward is the negative space only. Flash and codex want the idea first (the data
  already carried `essence_html`, unrendered). **Applied:** "The idea that works" precedes
  "Wrong but tempting". Gemini Pro would show the pitfalls *before* the attempt as an anti-hint;
  not applied, it removes the one stake the page has, but it is the first thing to test with a
  real reader.
- "Stumbled: claude" is misleading when one language variant failed. **Applied:** the line now
  carries fractions ("claude 1/3"), and the submissions-per-language definition sits in the rubric
  above the ladder, not the footer.
- The bar duplicates the percentage (codex). **Applied:** cut.

## Content errors in the lifted manual text (codex; both confirmed)

- Rung "Longest Almost-Palindromic Substring": heading says O(n^3), body computes O(n^4), then
  "2500^4 / something..." and a wrong 2500^3. Corrected in the lifted passage.
- Rung "Maximum Bitwise AND After Increment Operations": "[7, 8], k = 1 ... one increment cannot
  help" is false (7+1 = 8, AND = 8). Corrected with a visible note.
- Consequence: the "Wrong But Tempting" sections are Claude-generated and were never checked.
  The page now labels them as such. The vendored manuals are untouched; corrections live only in
  `CORRECTIONS` in `build_data.py`.

## Not applied

- Cut the model chips (Gemini Pro). Codex found "claude 0/2" the one thing that created curiosity;
  kept, smaller in the hierarchy.
- Inline canonical solution code (Flash). The manual link is the deeper cut; a reader test decides.

## Prompt defect

The prompt's example challenge line ("Stumbled: claude, deepseek") did not match any card; codex
noticed. Harmless here, but examples in review prompts must be copied from the artifact.

## Would they come back tomorrow?

All three said no, before the changes. Reasons: the reward was thin (fixed), the ladder wasted the
session on Mediums (fixed), and the page competes with LeetCode's own tracking (not fixable in a
static page). The reader test in CONTEXT.md stands.
