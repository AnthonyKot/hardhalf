# Hard Half — rung review and rewrite brief (2026-09-08)

You own a batch of rungs of the Hard Half page (/home/diablo/hardhalf; read CONTEXT.md and
review/CONSOLIDATED.md first, five minutes). For each rung you produce ONE JSON file and ONE
review note. You never edit shared files (scripts/, docs/, data/problems.json, README, CONTEXT).

## Inputs, per rung (pid = the problem id, e.g. wc0483-Q3-minimum-cost-to-make-two-binary-strings-equal)
- data/problems.json — the rung's entry: statement_html (LeetCode's text, authoritative),
  essence_html and tempting_html (LIFTED FROM A CLAUDE-GENERATED MANUAL, UNVERIFIED — the last review
  found arithmetic and logic errors in two of two sections it read), the model record, manual_url.
- docs/manuals/<pid>.html — the full generated manual (algorithm families, accepted solutions list).
- The benchmark checkout, read-only: /mnt/c/Users/CoderA/benchmark
  - leetcode_problems/<pid>.json — `testcases` (inputs + expected), `function_name`, `codeSnippets`.
  - solutions/<model_slug>/<pid>.<ext> — model-written solutions (py, java, cpp, js, go, …).
  - submissions/<model_slug>/<pid>.json — LeetCode's verdict for that solution: `accepted`,
    `status_msg`, `lang`, `runtime_ms`, `memory_mb`. Only use solutions whose submission says Accepted.
- Toolchains here: python3, node, javac/java, g++, go. No rustc.

## The reader
A working engineer, 4–6 years in, preparing for a senior loop, twenty minutes tonight, solves
Mediums comfortably, fails most contest Q4s. They have just recorded Passed/Failed/Gave up and the
card opens. Everything you write is what they read next. Plain words, no hedging, no praise, every
claim checkable.

## Output 1 — data/rungs/<pid>.json  (write it as soon as each part exists; overwrite as you refine)
{
  "id": "<pid>",
  "idea_html": "<p>…</p>",           // ≤ 220 words. The one idea that makes the problem tractable, then a worked
                                     // pass over the problem's FIRST sample input showing the idea producing the expected
                                     // output, then the time/space complexity of the accepted approach. Simple HTML only:
                                     // p, strong, em, code, ul/ol/li, pre. No headings. No page numbers, no model names.
  "pitfalls_html": "<ul>…</ul>",     // 3–4 items. Each: the tempting approach in one sentence, WHY it fails in one or two,
                                     // and ONE concrete input on which it gives the wrong answer or blows the limit —
                                     // an input you actually ran (or, for TLE, a size you computed). Keep any item from the
                                     // original tempting_html only if you verified it; drop or fix the rest.
  "solutions": {                     // one per language you could VERIFY locally against leetcode_problems testcases.
    "python3": {"code": "...", "model": "<model_slug>", "runtime_ms": "114 ms", "verified": "3/3 samples"},
    "java": {...}, "cpp": {...}, "javascript": {...}, "golang": {...}
  },                                 // Pick, per language, the accepted solution that is most READABLE (clear names, no
                                     // golf, ≤ ~60 lines preferred); add 3–6 short comments marking the idea's steps; do not
                                     // change logic. Skip a language rather than ship an unverified one. Python is required.
  "verified_on": "2026-09-08",
  "changes": ["…"]                   // one line per claim in the ORIGINAL essence/tempting text that was wrong or unverifiable
}

## Output 2 — review/rungs/<pid>.md (≤ 250 words)
What the original sections got wrong (quote the sentence, state the fact), what you verified and how
(commands/inputs), which solutions you tested and the result, and anything you could not settle.

## How to verify
- Numeric and complexity claims: compute them; write the arithmetic in the note.
- "This approach fails on X": implement the tempting approach in a few lines of Python and run X.
- Solutions: run each candidate against every entry in `testcases` using the language's toolchain
  (write a tiny harness in a scratch dir under /tmp/claude-1000/-home-diablo/ca321aaf-51cf-4ac4-a9ff-7e902bbb0802/scratchpad/<pid>/;
  do not write scratch files inside the repo). Record pass counts.
- Design problems (class with several methods): testcases are call sequences; verify what you can and
  say what you could not.

## Commit protocol
After finishing each rung: `git add data/rungs/<pid>.json review/rungs/<pid>.md && git commit -m "<pid>: reviewed rung"`.
Retry on index.lock (sleep 5, up to 5 times). Never push, never `git add -A`, never touch other rungs.

## Final report (≤ 200 words)
Per rung: verdict on the original text (how many claims wrong), languages shipped and verified,
anything unresolved. No prose about your process.
