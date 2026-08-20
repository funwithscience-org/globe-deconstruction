#!/usr/bin/env python3
"""Frame-to-frame skyline-edge stability in `no crop.MOV` — the turbulence discriminator.

Turbulence strong enough to blur an edge makes it dance by an amount comparable to the
blur; a static defocus leaves it still. This measures sub-pixel edge position across
consecutive frames inside and outside the fade-window blur excursion.

Method: for windows t = 300 (sharp control), 415, 430, 445, 460 s, extract 10 consecutive
frames (ffmpeg -ss T -frames:v 10). For columns x = 650..1200 step 25: locate the sky->tree
crossing (first row < 120 grey scanning down from y=300), then the sub-pixel edge row as
the |gradient| centroid within +/-6 px of the gradient peak in a +/-40-row window. A column
is EXCLUDED if its 10-frame position range exceeds 2 px (centroid flipping between two
competing edges in the window - bimodal, not motion; 1-2 columns per window). Report the
per-column standard deviation across frames.

Result (2026-08-20, run on the 15.3 Mbps original; independently re-run same day,
identical to the digit):
  t=300s: n=21 cols, median 0.08 px, p90 0.13, max 0.21
  t=415s: n=22,      median 0.10,    p90 0.33, max 0.65
  t=430s: n=22,      median 0.16,    p90 0.38, max 0.80
  t=445s: n=21,      median 0.13,    p90 0.37, max 0.45
  t=460s: n=22,      median 0.16,    p90 0.42, max 0.75

Reading: in the very frames where the treeline's 10-90 edge width is 20-22 px, the edge's
frame-to-frame motion is ~0.1-0.16 px median, <0.45 px at p90 - about 2% of the blur it
would need to explain - and per-frame blur width is steady. Not turbulence. The small
uptick vs the calm control (0.08 -> 0.16 median) shows the method resolves real sub-pixel
differences (i.e., H.264 block reuse is not faking stillness).
Distinct from NUMBERS.txt pointing stability (<=2 px): that is treetop-row drift at 30 s
samples (camera aim), a different quantity.
"""
import subprocess, sys, glob, os
import numpy as np
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else 'originals/no crop.MOV'
WINDOWS = (300, 415, 430, 445, 460)

def treetop_row(a, x):
    col = a[300:700, x]
    idx = np.where(col < 120)[0]
    return int(idx[0]) + 300 if len(idx) else None

def edge_row_subpix(a, x, y0, y1):
    v = a[y0:y1, x].astype(float)
    g = np.abs(np.gradient(v))
    if g.max() < 3: return None
    p = int(np.argmax(g)); s = slice(max(p-6, 0), min(p+7, len(g)))
    idx = np.arange(len(g))[s]; gg = g[s]
    return y0 + float((idx*gg).sum() / gg.sum())

os.makedirs('/tmp/_jitter', exist_ok=True)
for t in WINDOWS:
    subprocess.run(['ffmpeg','-loglevel','error','-ss',str(t),'-i',SRC,
                    '-frames:v','10', f'/tmp/_jitter/j{t}_%02d.png'], check=True)
    ims = [np.asarray(Image.open(f).convert('L')).astype(float)
           for f in sorted(glob.glob(f'/tmp/_jitter/j{t}_*.png'))]
    sig, excl = [], 0
    for x in range(650, 1201, 25):
        r0 = treetop_row(ims[0], x)
        if r0 is None: continue
        rows = [edge_row_subpix(a, x, r0-40, r0+40) for a in ims]
        rows = [r for r in rows if r is not None]
        if len(rows) < 8: continue
        if max(rows) - min(rows) > 2.0:
            excl += 1; continue
        sig.append(np.std(rows))
    s = np.array(sig)
    print(f"t={t:>4}s  n={len(s):>2}  excluded={excl}  "
          f"median {np.median(s):.2f}  p90 {np.percentile(s,90):.2f}  max {s.max():.2f} px")
