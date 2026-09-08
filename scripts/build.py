#!/usr/bin/env python3
"""Render docs/index.html from data/problems.json (embedded, so the page works from file:// and Pages)."""
import json, html, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(root, 'data', 'problems.json'), encoding='utf-8'))
tpl = open(os.path.join(root, 'scripts', 'template.html'), encoding='utf-8').read()
page = tpl.replace('/*DATA*/', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
page = page.replace('{{N}}', str(len(data)))
open(os.path.join(root, 'docs', 'index.html'), 'w', encoding='utf-8').write(page)
print('wrote docs/index.html with %d problems' % len(data))
