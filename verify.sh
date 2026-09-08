#!/usr/bin/env bash
# Hard Half — standing verification: data integrity, page sanity, manual links.
set -u; cd "$(dirname "$0")"; fail=0
python3 - <<'PY' || fail=1
import json, os, re, sys
d = json.load(open('data/problems.json'))
ids = [p['id'] for p in d]
assert len(ids) == len(set(ids)), 'duplicate ids'
assert [p['rank'] for p in d] == list(range(1, len(d) + 1)), 'ranks not sequential'
rates = [p['rate'] for p in d]
assert rates == sorted(rates, reverse=True), 'ladder not ordered by acceptance rate'
for p in d:
    assert p['attempts'] >= p['accepted'] > 0, p['id']
    assert sum(m['attempts'] for m in p['models']) == p['attempts'], p['id']
    assert p['statement_html'] and os.path.exists('docs/' + p['manual_url']), p['id']
    if not p['tempting_html']: print('  advisory: no Wrong-But-Tempting section for', p['id'])
page = open('docs/index.html', encoding='utf-8').read()
assert '/*DATA*/' not in page and page.count('"id": "wc') == len(d), 'page data not embedded'
assert '/mnt/c/' not in page and 'C:\\' not in page, 'local path leaked'
print('  data ok: %d problems, rates %.2f → %.2f' % (len(d), rates[0], rates[-1]))
PY
echo "== vendored manuals self-contained (no external src/href) =="
python3 - <<'PY' || exit 1
import glob, re
for f in glob.glob('docs/manuals/*.html'):
    h = open(f, encoding='utf-8', errors='ignore').read()
    ext = [u for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', h) if 'leetcode.com' not in u]
    print('  %-70s %d external refs' % (f.split('/')[-1][:70], len(ext)))
PY
[ $fail = 0 ] && echo PASS || { echo FAIL; exit 1; }
