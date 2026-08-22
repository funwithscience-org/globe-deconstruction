#!/usr/bin/env python3
"""Emit the page-density map + stat tiles from data/page-density.json.

Three states, not a word gradient: a page is prose, a plate (a picture with
no sentence on it), or both. Counting words alone reported the book's last
third as near-empty; it is not empty, it is pictorial, and the map has to
show that or it misrepresents the book.
"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, 'data', 'page-density.json')))
m = d['meta']

def prose_shade(w):
    if w < 45:  return 1
    if w < 90:  return 2
    if w < 150: return 3
    return 4

TILES = [(f"{m['pdf_pages']}", 'Pages in the draft'),
         ('24', 'Testable claims in it'),
         ('10', 'Answered in full'),
         (f"{m['pct_first240']}%", 'Of its words, in the first 240 pages'),
         (f"{m['plates']}", 'Pages carrying a picture and no sentence')]

h = ['<div class="tiles">']
for v, l in TILES:
    h.append(f'  <div class="tile"><span class="tv">{v}</span><span class="tl">{l}</span></div>')
h.append('</div>')

h.append('<div class="mapkey">')
for cls, lab in [('k1','sparse prose'),('k2','&nbsp;'),('k3','&nbsp;'),('k4','dense prose'),
                 ('plate','a picture, no sentence'),('claim','hosts a claim')]:
    h.append(f'<span class="sw {cls}"></span><span class="kl">{lab}</span>')
h.append('</div>')

h.append('<div class="pmap">')
for s in d['sections']:
    plate = f' &middot; <b>{s["plates"]} of them a picture with no sentence</b>' if s['plates'] else ''
    h.append('  <div class="psec">')
    h.append(f'    <p class="pname">{s["name"]}</p>')
    h.append(f'    <p class="pmeta">pp.&nbsp;{s["a"]}&ndash;{s["b"]} &middot; {s["pages"]} pages &middot; {s["words"]:,} words, mean {s["mean"]} a page{plate}</p>')
    h.append('    <div class="cells">')
    for c in s['cells']:
        k = c['k']
        cls = 'plate' if k == 'plate' else ('blank' if k == 'blank' else f'k{prose_shade(c["w"])}')
        if c['c']: cls += ' claim'
        what = {'plate':'picture, no sentence','blank':'blank','mixed':'text and picture','prose':'text'}[k]
        t = f'p.{c["p"]} — {c["w"]} word' + ('' if c['w'] == 1 else 's') + f' — {what}'
        if c['c']: t += f' — {c["c"]}'
        h.append(f'<i class="{cls}" title="{t}"></i>')
    h.append('</div>\n  </div>')
h.append('</div>')
print('\n'.join(h))
