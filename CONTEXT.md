# Hard Half — CONTEXT

## Working idea

A practice layer over an existing reference layer. The reference layer is the LLM coding
benchmark's published manuals (anthonykot.github.io/lc-benchmark-manuals): 37 recent LeetCode
weekly-contest problems, Q3 and Q4 only, each with a manual generated from every accepted
model solution. The practice layer is one page: a ladder of ten of those problems, ordered by
model acceptance rate, with a stopwatch, a self-recorded verdict, and, only after the attempt,
the models' mistakes and the manual.

The opponent is the published record of which models got Accepted. That is the stake the three
earlier AlgoPath attempts lacked (user diagnosis, 2026-09-08: "what was missing is either more
interesting/complex tasks or some gamification"). Here the hard content and the game are the
same feature.

## Evidence

- **User-reported (2026-09-08):** three published AlgoPath versions (v1 static handbook, v2
  Vite study app, v3 curriculum DAG) were not good enough to share; the missing thing was
  harder problems or gamification.
- **Observed:** the benchmark holds LeetCode ground truth for model submissions
  (`submissions/<model>/<problem>.json`, fields `accepted`, `status_msg`, `lang`) and manuals with
  a "Wrong But Tempting" section per problem.
- **Hypothesis:** a reader who sees "12 of 29 model submissions accepted" attempts the problem and
  returns for the next rung. Opening the page is not success; a second recorded attempt is.

## What this is not

- Not a curriculum, not spaced repetition, not an account system. Progress is browser-local.
- Not a new manual generator. Manuals are linked, not rewritten; the only lifted text is each
  manual's "Wrong But Tempting" section, shown after the attempt.
- Not a claim about model rankings. Counts are submissions (model × language), shown as such.

## Pipeline

    scripts/build_data.py   # reads the benchmark checkout (BENCH env var) → data/problems.json
    scripts/build.py        # data/problems.json + scripts/template.html → docs/index.html
    ./verify.sh             # data integrity, links, page sanity

The ladder is the LADDER list in `build_data.py`, then sorted by acceptance rate. Set 1 (WC482–489)
only, because set 2 has at most nine submissions per problem and the scoreboard would look thin.

## Reader test (the gate)

Put the page in front of one person preparing for interviews. Success = a second attempt recorded
on a later day. Record what they said about the challenge line, the reveal, and the manual link.
Do not add features before that result exists.
