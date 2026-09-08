#!/usr/bin/env python3
"""Extract the pilot's data from the LLM coding benchmark (local path) into data/problems.json.
Sources: leetcode_problems/*.json (statement), submissions/*/*.json (LeetCode ground truth per model),
docs/set*/*.html (the published manuals: essence + 'Wrong But Tempting')."""
import glob, html, json, os, re, sys, collections
BENCH = os.environ.get('BENCH', '/mnt/c/Users/CoderA/benchmark')
MANUALS_URL = 'manuals/'  # vendored copies under docs/manuals/, self-contained HTML
import shutil
os.makedirs('docs/manuals', exist_ok=True)
LADDER = [  # chosen by model acceptance rate, easiest first (set 1, richest submission data)
    'wc0482-Q3-smallest-all-ones-multiple',
    'wc0484-Q3-count-caesar-cipher-pairs',
    'wc0486-Q3-pythagorean-distance-nodes-in-a-tree',
    'wc0483-Q3-minimum-cost-to-make-two-binary-strings-equal',
    'wc0482-Q4-number-of-balanced-integers-in-a-range',
    'wc0483-Q4-minimum-cost-to-merge-sorted-lists',
    'wc0487-Q4-longest-alternating-subarray-after-removing-at-most-one-element',
    'wc0484-Q4-maximum-bitwise-and-after-increment-operations',
    'wc0489-Q3-longest-almost-palindromic-substring',
    'wc0485-Q4-lexicographically-smallest-string-after-deleting-duplicate-characters',
]
FAMILIES = ['claude', 'codex', 'deepseek', 'glm', 'qwen', 'minimax', 'kimi', 'gemini', 'gpt', 'llama', 'mistral']
def family(slug):
    s = slug.lower()
    hits = [(s.find(f), f) for f in FAMILIES if f in s]
    return min(hits)[1] if hits else s.split('-')[0]
def section(page, heading):
    m = re.search(r'<h2[^>]*>\s*%s\s*</h2>(.*?)(?=<h2|\Z)' % re.escape(heading), page, re.S)
    if not m: return ''
    body = m.group(1)
    body = re.sub(r'<(script|style).*?</\1>', '', body, flags=re.S)
    body = re.sub(r'\s+on\w+="[^"]*"', '', body)
    return body.strip()
manuals = {os.path.basename(f)[:-5]: f for f in glob.glob(BENCH + '/docs/set*/wc*.html')}
out = []
for rank, pid in enumerate(LADDER, 1):
    prob = json.load(open(BENCH + '/leetcode_problems/' + pid + '.json', encoding='utf-8'))
    subs = collections.defaultdict(lambda: {'attempts': 0, 'accepted': 0, 'langs': collections.defaultdict(lambda: [0, 0])})
    for f in glob.glob(BENCH + '/submissions/*/' + pid + '.json'):
        try: j = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        fam = family(j.get('candidate_slug') or f.split('/')[-2]); lang = j.get('lang', '?')
        ok = str(j.get('accepted', '')).lower() == 'true' or j.get('status_msg') == 'Accepted'
        subs[fam]['attempts'] += 1; subs[fam]['accepted'] += int(ok)
        subs[fam]['langs'][lang][0] += int(ok); subs[fam]['langs'][lang][1] += 1
    page = open(manuals[pid], encoding='utf-8', errors='ignore').read()
    shutil.copyfile(manuals[pid], 'docs/manuals/' + pid + '.html')
    fams = [{'family': k, 'attempts': v['attempts'], 'accepted': v['accepted'],
             'langs': {l: {'accepted': a, 'attempts': n} for l, (a, n) in sorted(v['langs'].items())}}
            for k, v in sorted(subs.items(), key=lambda kv: (-kv[1]['accepted'] / max(kv[1]['attempts'], 1), kv[0]))]
    tot_a = sum(f['accepted'] for f in fams); tot_n = sum(f['attempts'] for f in fams)
    out.append({
        'rank': rank, 'id': pid, 'title': prob['title'], 'difficulty': prob['difficulty'],
        'contest': prob.get('contest'), 'position': prob.get('position'),
        'leetcode_url': prob.get('problem_url'), 'function': prob.get('function_name'),
        'tags': [t.get('name', t) if isinstance(t, dict) else t for t in prob.get('topicTags', [])],
        'statement_html': prob['content'],
        'essence_html': section(page, 'Problem Essence'),
        'tempting_html': section(page, 'Wrong But Tempting'),
        'manual_url': MANUALS_URL + pid + '.html',
        'models': fams, 'accepted': tot_a, 'attempts': tot_n,
        'rate': round(tot_a / tot_n, 3) if tot_n else None,
    })
out.sort(key=lambda p: (-(p['rate'] or 0), p['id']))
for i, p in enumerate(out, 1): p['rank'] = i
json.dump(out, open('data/problems.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for p in out: print(f"{p['rank']:2d} {p['accepted']:3d}/{p['attempts']:3d} {p['rate']:.2f} {p['difficulty']:6s} {p['title']}  fams={len(p['models'])} essence={len(p['essence_html'])} tempting={len(p['tempting_html'])}")
