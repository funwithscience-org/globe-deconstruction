#!/usr/bin/env python3
"""Inject (or refresh) the shared left-hand nav into every docs/**/index.html.

Idempotent: an existing block between the markers is replaced, so editing
scripts/nav_block.html and re-running is the way to change the nav everywhere.
"""
import glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = open(os.path.join(ROOT,'scripts','nav_block.html'),encoding='utf-8').read().strip()
START, END = '<!--SITENAV-->', '<!--/SITENAV-->'
payload = START + '\n' + BLOCK + '\n' + END

changed = []
for f in sorted(glob.glob(os.path.join(ROOT,'docs','**','index.html'), recursive=True)):
    s = open(f,encoding='utf-8').read()
    if START in s:
        new = re.sub(re.escape(START)+r'.*?'+re.escape(END), lambda m: payload, s, flags=re.S)
    else:
        m = re.search(r'<body[^>]*>', s)
        if not m:
            print('NO BODY TAG:', f); continue
        new = s[:m.end()] + '\n' + payload + s[m.end():]
    if new != s:
        open(f,'w',encoding='utf-8').write(new)
        changed.append(os.path.relpath(f, ROOT))
print('updated %d file(s)' % len(changed))
for c in changed: print('  ', c)
