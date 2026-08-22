#!/usr/bin/env python3
"""Ensure every claim-answering page opens with the claim in the author's own words.

House pattern is the .qbox block already used on docs/earth-rotation/. Idempotent:
a page that already carries the box for a given reference is left alone.
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('.qbox{background:#fbfaf7;border:1px solid var(--rule);border-left:4px solid var(--accent);'
       'border-radius:6px;padding:.9rem 1.1rem;margin:1.2rem 0;font-family:var(--sans);font-size:.95rem;line-height:1.55}\n'
       '.qbox .qn{display:block;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);'
       'font-weight:700;margin-bottom:.35rem}\n')

Q = {
 'Q4':  ('Question 4, p.&nbsp;47',  'Do we observe perfectly mirrored reflections over large bodies of water at rest as we increase observer height?'),
 'Q5':  ('Question 5, p.&nbsp;48',  'Why is there no difference in visual speed between stars and planets as the Earth spins during a single night? A large distance gap requires that visual speeds will not be equal to the observer.'),
 'Q6':  ('Question 6, p.&nbsp;49',  'Why do the moons of Jupiter produce shadows that are not aligned with the singular light source of the Sun? Are we assuming them to be shadows or can it be proven?'),
 'Q7':  ('Question 7, p.&nbsp;50',  'If the Moon is a spherical rock in a vacuum, how does the light of the Sun perfectly distribute across the entire surface during a full Moon without any highlight points?'),
 'Q9':  ('Question 9, p.&nbsp;52',  'Why do we never observe the entire circular silhouette of the Moon when approaching a solar eclipse? Photo manipulation always fails to detect evidence of the Moon.'),
 'Q10': ('Question 10, p.&nbsp;53', 'How was the scientific method used to prove that air layers have enough friction to stay in perfect rotational sync across all heights of the atmosphere and the Earth to where we perceive zero motion? Mechanical common sense states that the speed of the air would be faster as you get closer to the rotational source.'),
 'Q12': ('Question 12, p.&nbsp;55', 'What scientist proved that sunlight moves in a perfectly straight line through hundreds or thousands of miles of gas? Is this an incorrect assumption when measuring shadow angles to dismiss the possibility of a flat Earth?'),
 'BLUEPRINT': ('Celestial Globes Exposed, p.&nbsp;148',
   'Despite a decade of intense public debate, no engineering firm has produced definitive blueprints and construction documents for curved bridges, tunnels, or canals. We should have hundreds of tunnel design plans going through curved mountains. The lack of evidence is alarming. &hellip; Where is the raw evidence of large-scale, curved engineering projects?'),
 'PROOF': ('Extraordinary Evidence or Fallacy, p.&nbsp;205',
   'Remember, we all agree that extraordinary claims require extraordinary evidence. Which side of the debate is being honest with the scientific method? The globe side is making a very long list of positive claims that should be verified in multiple ways (ideally by a handful of independent 3rd parties). The goal of the skeptical side is simply to demonstrate fallacy in the globe model.'),
}
TARGETS = {
 'full-moon-lighting':   ['Q7'],
 'mirrored-reflections': ['Q4'],
 'sky-rate-and-shadows': ['Q5', 'Q6'],
 'sunlight-and-shadows': ['Q12'],
 'luminaries':           ['Q9'],
 'construction-records': ['BLUEPRINT'],
 'extraordinary-evidence':['PROOF'],
 'earth-rotation':       ['Q10'],   # Q11 already present
}

def box(key):
    lab, txt = Q[key]
    return ('<div class="qbox"><span class="qn">Globe Deconstruction? &mdash; %s &middot; his words, quoted</span>\n&ldquo;%s&rdquo;</div>' % (lab, txt))

changed = []
for slug, keys in TARGETS.items():
    f = os.path.join(ROOT, 'docs', slug, 'index.html')
    s = open(f, encoding='utf-8').read(); orig = s
    if '.qbox{' not in s:
        s = s.replace('</style>', CSS + '</style>', 1)
    add = [k for k in keys if Q[k][1][:60] not in s]
    if add:
        blocks = '\n'.join(box(k) for k in add)
        m = re.search(r'</div>\s*(?=<p|<div|<h2|<section)', s[s.find('</header>'):])
        if 'class="draftbar"' in s or 'class="qbox"' in s:
            # after the last leading banner/box before the first h2
            h2 = s.find('<h2')
            cut = s.rfind('</div>', 0, h2)
            anchor = cut + len('</div>')
        else:
            anchor = s.find('</header>') + len('</header>')
        s = s[:anchor] + '\n' + blocks + s[anchor:]
    if s != orig:
        open(f, 'w', encoding='utf-8').write(s)
        changed.append((slug, add))
for c in changed: print('  %-24s +%s' % c)
print('%d page(s) updated' % len(changed))
