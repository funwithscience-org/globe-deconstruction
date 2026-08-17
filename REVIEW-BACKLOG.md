# Globe Deconstruction review — working backlog

Repo-root working file, **not** published (only `docs/` is served by Pages).
Tick items as pages land; keep the banked research notes with the item so
nothing has to be re-derived.

Catalogue source of truth is `docs/index.html`. When an item closes, update
**both** this file and the landing page's status chip.

**State as of 2026-08-17: 22 tracked items — 10 answered, 2 partial, 10 open.**

Ranking weights: how load-bearing the claim is to his thesis × how decisive an
answer we can actually make × public-facing (site) vs buried (book) × work
already banked.

---

## The queue

### ~~1. Equator Flight Data Challenge~~ — `Q3 (p.46)` + `Section p.117` — **DONE 2026-08-17**

- [x] Page built — `docs/equator-flight/`
- [x] Landing page updated (both entries)

Published as *The Equator Flight Data Challenge, Answered*. What it ended up
arguing, in case it needs defending later:

- Conceded four things up front: the experiment is sound; the globe's
  prediction really is exactly zero; **the equator is the best possible route**
  because it is the one latitude where the two models differ maximally (they
  converge above ~60°); and the p.119 pendulous-vane analysis is correct.
- The table's 119° = 8,250 mi ÷ 24,901 mi × 360° — the globe's circumference.
  On the flat map the same leg is **75.9°** at **5.15°/hr**, 76 inputs not 119.
  Also: the named airports are 172°/188° apart (~11,900/13,000 mi), so the
  endpoints and the distance are not the same flight.
- Noted the tension with pp.118–120, which argue map distances are unreliable,
  four pages before the headline figure is derived from trusting them.
- The instruments section is the load-bearing one: bank angle is 2.2 arcmin,
  turn needle would not move, **and the compass reads 090° in both models**
  because the flat map's north reference rotates with you. The discriminator is
  the gyro against inertial space — Earth rate 15.04 sin φ plus transport
  (V/R) tan φ, both exactly zero at the equator, against 5.15°/hr flat.
- Closed the loop: his own correct p.119 mechanism (vanes erect to *local*
  vertical, which rotates at V/R) is what answers his island-of-pilots
  objection on p.122.
- **Added 2026-08-17 (operator's point):** a turn is not forced by the
  aerodynamics of flow. Lift is perpendicular to the wings; nothing in the
  airflow curves the path. So vertically the aircraft sits in an equilibrium
  with a restoring force (level flight *is* curved flight, free), while
  horizontally there is no equilibrium at all — a bank has to be commanded and
  held. The flat model therefore needs the kind of curve that cannot happen by
  itself. That is listed as a §1 concession (it is *why* the flight recorder is
  the right instrument — the signal is a commanded action, not a residual) and
  developed in §5 as the **hands-off test**: trim level over the equator and
  stop steering. Globe keeps you on the line, because it is the one latitude
  where *both* (V/R)tan φ and the Coriolis sin φ term vanish — at the equator
  the Coriolis term points straight up (Eötvös, 0.37% of g), not sideways.
  Flat map: 25 mi off in 1 h, 100 in 2, 391 in 4 (√(r²+d²)−r, r = 6,225 mi).
  This is the strongest form of the experiment — no instruments, no pilot in
  the loop, answer arrives as a position anyone on board can see.
- **Added 2026-08-17 (operator, second round):** the per-latitude turn-rate
  table was the wrong comparison north of the equator, because nobody flies a
  parallel — the great circle is 15–31% shorter (London–Tokyo 5,946 vs 7,004 mi,
  vertex 70.9°N). And the natural objection — *"you can just fly due west and
  never turn"* — is the same constant-heading-vs-constant-direction trap as §4,
  and is why the chapter persuades. Both now in §3.
  The fix that generalises everything: **a full circuit of the parallel at
  latitude φ is 360°·sin φ of turning on a globe and 360° on any flat surface**,
  so the gap is 360°(1−sin φ) — the enclosed curvature, Gauss–Bonnet. Scale-free,
  covers every latitude, maximal (a whole revolution) at the equator, zero at the
  pole. This supersedes the AE-dependent rate table as the primary argument.
  Also: hands-off at 45°N the track curves 21.3°/hr on Coriolis alone (100 mi in
  the first hour), so the hands-off test is equator-only — a third independent
  reason the route is right.
- **Added 2026-08-17 (third round) — §3 rewritten to TEACH, not assert.**
  Operator: *"you could actually drive straight west without turning"* — and
  that it was news to them. That reaction is the most useful signal we have had
  about this chapter: the distinction defeats most globe defenders, so the usual
  reply ("the equator is a great circle") answers a question nobody asked. Now
  conceded on the page as a point in Miller's favour.
  Three-step teaching sequence replaces the assertion: (1) turn the numbers up —
  10 m from the pole, walk due west, 10 m circle, lap every 45 s, **8°/second**,
  compass on 270 throughout; (2) drive it — straight line falls south of due west
  by 6.7 in/mile, **20.1 ft per 6-mile township**, 724 ft in 36 mi at 40°N
  (derived from κ = tan φ / R); (3) **the PLSS has corrected for it since 1785** —
  GLO/BLM *Standard Field Tables* Table 13 "Offsets from the tangent to the
  parallel" + Table 14 for the secant method. Verified the tables exist and are
  named; could NOT reliably extract the scanned figures, so the page labels the
  offsets as derived and points readers at Table 13. **If this is ever quoted at
  Miller, pin the published values first.**
  Then: 3.4 arcmin of bank at 45°N, and nobody commands the turn — you command a
  heading. Closes on the 360 sin φ circuit result as the definition-free version.

### 2. Unknown Luminaries expansion — `Section p.153` + `Q5` + `Q6` + `Q7` + rest of `Claim #3`

- [ ] Q5 — stars vs planets show no apparent-speed difference (p.48)
- [ ] Q6 — Jupiter's moon shadows don't align to one light source (p.49)
- [ ] Q7 — full Moon evenly lit, no highlight point (p.50)
- [ ] Claim #3 remainder (moon lighting, moon-tilt illusion, Jupiter's moons)
- [ ] `p.153` upgraded from Partial to Answered

Highest leverage on the board: one page closes **five** catalogue entries,
including the outstanding two-thirds of a *public site* claim.

Notes:

- **Q5** is the weakest of his set — angular rate of the sky is set by Earth's
  rotation; distance does not enter. Short section.
- **Q6** is projection geometry plus ephemeris. Checkable, satisfying.
- **Q7 is the one to be careful with** — see Risk flags below.

### 3. Q8 — the Sun shrinks and fades rather than sets (p.51)

- [ ] Page built

Direct observational claim, camera-testable, and it plugs into the angular-size
machinery already built for Polaris in `docs/celestial-globes/`. If the Sun
receded it would shrink continuously and by a large factor all afternoon;
measured angular diameter is flat to well under a percent. "Shrink and fade" is
extinction and haze, plus the perceptual effect.

### 4. Section p.241 — All Construction Records Missing

- [ ] Page built

Blue-collar documentary evidence, which is where this project is strongest.
Candidate sources: long-span bridge tower separations (Verrazzano ~1⅝ in,
Humber, Akashi Kaikyō), canal and levelling surveys, the Channel Tunnel
gyrotheodolite work **already cited on the earth-rotation page**, long pipelines,
VLBI baselines, LIGO's 4 km arms following a chord rather than the geoid.

Caveat: it is a prove-a-negative challenge, so the page should be about what
*is* in the records rather than about the absence of anything.

### 5. Q12 — straight-line sunlight through the atmosphere / shadow angles (p.55)

- [ ] Page built

Cheapest win left. The plane-stratified Snell apparatus written for
`docs/celestial-globes/` §3 answers this almost verbatim: bench-measured n,
the exact `n·sin z = const` invariant, refraction ≈ 1 arcmin at 45° elevation,
and refraction measured terrestrially against tape-and-level targets with no
astronomy in it. Mostly an assembly job.

### 6. Q2 — has gravity been shown to override hydrostatics? (p.45)

- [ ] Page built

The "water finds its level" core. Real answer available — level *is* the
equipotential surface; the geoid; satellite gravimetry (GRACE); torsion
balances and gravimeters detecting local mass anomalies. Needs care not to read
as hand-waving; the strongest version is probably a working gravimeter survey
that finds a buried ore body, because that is a prediction with money on it.

### 7. Q4 — mirrored reflections over large still water as observer height rises (p.47)

- [ ] Page built

Narrower and optically fiddly. Overlaps the territory of
`docs/bottom-up-observations/`; check for reuse before starting.

### 8. Section p.203 — Extraordinary Evidence or Fallacy

- [ ] Page built

Different genre — epistemology, not arithmetic. Do it late, and concede the most.
**If he is arguing that the two models are held to asymmetric standards of
proof, that critique lands on this review too, and the page should say so
before it says anything else.**

### 9. Section p.415 — Antarctica's Magnetic North

- [ ] Page built

Well-documented, narrow, low stakes either way. Last.

---

## Risk flags

- **Q7 (full-Moon uniform brightness) is the one where his observation is
  genuinely real and counterintuitive.** A smooth Lambertian sphere *would*
  show limb darkening and the Moon flatly does not. The answer is the
  opposition surge and coherent backscatter off regolith, and it needs real
  photometry to do honestly rather than a wave at "the surface is rough." Highest
  chance of us getting something wrong — and also the best concession available
  in the whole remaining set.
- **p.203** — he may be partly right. See above.
- **Q4** — atmospheric and specular-reflection subtleties; easy to overclaim.

## Structure note

The 12 outstanding entries collapse into roughly **7 pages**, because item 2
merges five catalogue entries. (Item 1 merged two and is done.)

---

## Already answered (for reference)

| Item | Page |
|---|---|
| Claim #1 — bottom-up disappearance / angular resolution | `bottom-up-observations/`, `rampion/` |
| Claim #2 — rocket thrust in vacuum | `rockets-in-vacuum/` |
| Claim #3 — celestial red flags | **partial** — eclipse half in `luminaries/`, rest as tests in `self-test-protocol/` |
| Q1 — gas thrust needs surrounding air | `rockets-in-vacuum/` |
| Q9 — no Moon silhouette before an eclipse | `luminaries/` |
| Q10 — atmospheric co-rotation at every altitude | `earth-rotation/` |
| Q11 — polar time-lapse, Compton generator in Antarctica | `earth-rotation/`, `coriolis-drifters/` |
| Section p.124 — Celestial Globes Exposed (Polaris, perspective) | `celestial-globes/` |
| Section p.153 — Unknown Luminaries | **partial** — eclipse half only |
| Section p.179 — Perfectly Synchronized Gas Rotating with Earth? | `earth-rotation/` |

## Standing constraints

- Review stays **unlinked from the funwithscience.net main page** while the book
  is prerelease. Deliberate courtesy window.
- `celestial-globes/` is held back from Levi until he responds on the earlier
  material — it is the harshest page and the chapter is the least *him* thing in
  the book.
- Pushes go via the bundle procedure in `PUSH-README-globe-deconstruction.md`
  (working copy in the Cowork session; the sandbox git proxy blocks writes).

---

## Peer-review passes (2026-08-17)

Two adversarial reviews came back from an independent instance, on
`equator-flight/` and `celestial-globes/`. Both were verified item by item
against primary sources before acting; **do not apply a review from that
instance unchecked** — see the misses below.

### equator-flight — applied
Big one: §4 claimed the divergence is in the flight-recorder trace. **False.**
14 CFR Part 121 App. M mandates roll at 0.5° resolution / ±2° accuracy / 1 Hz
against a 0.04° bank; body rates aren't mandated; recorded heading is
post-correction IRS output so reads 090 under both models. Page now says so and
names the cheap alternative (nav-grade FOG in a seat + GPS on any scheduled
equator sector). Also: twitter card, V/R unified on R = 3,963.19 mi, "ten metres
across" → twenty (radius vs diameter), UIO/PNK real coordinates, p.118 quote,
INS "since ~1970", nautical miles. Softened "no equilibrium at all" → no
*aerodynamic* mechanism (our own 21.3°/hr Coriolis contradicted it), and
replaced the Schuler hand-wave with the tilt derivation V(1/R_true − 1/R_assumed)
= 2.9° after an hour = 0.05 g. New §7 answers the p.122 magnetic-south follow-up,
which we'd skipped: southbound tracks converge on a globe, diverge on any
pole-centred flat map — topology, not rate — and those flights carry passengers.

### celestial-globes — applied
Real physics error found: the **Vostok row** scaled refraction by record low
temperature while holding pressure at sea level. Vostok is at 3,488 m (~620 hPa),
so actual refraction there is ~5.1′, *below* standard. Row relabelled as an
explicit sea-level hypothetical and a realistic Siberian-High row added
(1,060 hPa at −60 °C → 7.5′). The 8.9′ "both records at once" wall is unaffected.
Also: setting-Sun flattening 10% → ~19% (6′ of a 32′ disc, Bennett); refraction
at 10° unified on 0.090° with 5.3/5.4/5.7 explained once (10°N "wrong by"
271× → 285×); Kochab 16° → 16.6°; "best telescope" → best optical interferometer;
noted his 18,860 is right to his own 430 ly. Softened: **"69 mi/deg never
changes" varies 1% with oblateness** — now says so and credits the French
Geodesic Missions 1735–44 as this experiment run three centuries early (a gain,
not a loss); the extinction degeneracy now closed properly (coefficient measured
from *other* stars, not fitted to Polaris); Kochab isn't circumpolar from 10°N.
Added: Fermat one-liner (no medium knows how far away the source is — which is
what licenses walking the Sun through the field), the Moon-illusion pre-empt,
σ Octantis + Polaris photographed in one night from Ecuador, and **his own p.131
invitation** quoted as the thing the page is answering.

### What the reviews got WRONG — check these next time
- **SVG `<desc>` "leaking into body text"** — claimed on *both* pages, false on
  both. Verified by rendering. Almost certainly an artifact of fetching the page
  through a markdown converter, which flattens `<desc>`. Not a page bug.
- **"along the parallel" figures are rhumb lines** — no, they were parallel-at-
  mean-latitude; they agree with rhumb within 0.3% only because the city pairs
  sit at similar latitudes. Relabelled anyway, because the prescription was right.
- **tangent/secant procedure "formalised in the 1855 Manual"** — fetched it; that
  manual has correction lines for meridian convergency but no curve methodology.
  Page now claims only what the 1910 tables support.

### Rescan round (2026-08-17, both pages) — applied
`equator-flight`: **§7 offered radial Antarctic flights as evidence and they
cannot discriminate** — an azimuthal-equidistant map preserves distance along
its radii by construction, so due-south legs are where it is *designed* to be
right. (The reviewer said identical; actually Cape Town–Troll is 16° off a
meridian so it differs 2,700 vs 3,800 mi, 1.4× — weak, not null. Page says
exactly that.) Replaced with the legs that do discriminate: **Novolazarevskaya →
Progress, east–west at 70°S, 1,450 vs 11,800 mi (8.2×)**, flown by Basler BT-67
on the DROMLAN network in a working day; and **Pan Am 50**, 28–30 Oct 1977,
747SP N533PA, Cape Town → Auckland over the South Pole, 7,300 vs 17,000 mi
(2.3×) — date/aircraft/route verified. Also the **wind confound**: a 22-kt
crosswind produces the flat map's entire first-hour departure, so the
"needs no instruments" claim was untenable; now conceded with the two
separators (wind is linear in t and moves track-vs-heading; the flat departure
goes as t² and moves the pole-referenced heading itself). Hands-off leg defined
operationally (roll-attitude hold at 0° bank, no heading/LNAV) so it stops
contradicting the spiral-mode concession. Gyro grades corrected (nav-grade is
tens of thousands; rent it or buy tactical and calibrate) **and the clause the
test needs added — a seat gyro does NOT read zero on a globe**; the comparison
is integrated gyro yaw vs GPS-derived heading change, whose predicted difference
is zero only at the equator.

`celestial-globes`: extinction coefficient was stated backwards — mountain sites
are *lower* (0.12–0.15 vs 0.2 mag/airmass at sea level); the 0.6 figure is the
*total* at 10° from a summit, against 0.95 from the coast. Kochab table rescaled
from 16° to 16.6° to match its own lead-in (16.6/16.2 · 12.0/8.5 · 8.3/4.1).
"circumpolar circle" → "Kochab–Polaris circle".

### Optics pages — reviewed and rescanned (2026-08-17)
`bottom-up-observations` and `rampion` both went through review + rescan.

**Real error found in bottom-up:** the §5 refraction table computed the mid-path
*sagitta* (how far the sightline bows below the chord) but labelled it "ray needs
to miss the lens by". A sagging ray still reaches the lens. True hiding criterion
— limiting ray from a 63.5 mm source to a 12.7 mm lens over 125 m grazing the
water — needs **−17.6 °C/m ≈ 0.70 °C over the lowest 4 cm**, seven times what
the page implied. Column relabelled, cutoff row added, "it's the default"
softened. Also Wallace was backwards (the *midpoint* disc showed above the far
marker), pixel scale was the ultrawide figure not the main lens (0.8 px at
1080p), five orders not six.

**Best new material, both from his own numbers:**
- bottom-up §3: p.132 *"you see the flare of light, but not the physical
  dimensions of the source"* — his own concession that a source past the
  resolution limit stays visible. Plus his p.134 worked example: 1 in at the
  limit = 286 ft, so 2.5 in = **716 ft**, against Claim #1's "410+ ft minimum".
- rampion §7: he concedes the dark band at support 6 is ⅓ its height at turbine
  1 and calls it perspective. Perspective gives **8.0/11.0 = 0.73**. On his own
  figure something that grows with distance removed the rest. Only differential
  measurement in the chapter, and it runs against the chapter.

**Errors I introduced while fixing, caught by the rescan** — argues for always
running the rescan: k attributions swapped (Bowditch implies 0.179; **0.13 is
Gauss's**), two page refs wrong (286 ft is p.134 not 133; the art-class quote is
p.95 not 94), "six thousand stars visible at once" is the whole-sky total, and
"a few millionths of an arcminute" fails for Betelgeuse (0.00075).

### Not done — operator's call
- **Length.** equator-flight ~8,100 words, celestial-globes ~9,200, for chapters
  of 6 and 28 pages. Both reviews flag it.
- **equator-flight:** "why the equator" is argued four times (§1, §3, §5, §6);
  the suggested instrument-panel table would let a lot of prose be *deleted*.
- **celestial-globes §4.5:** run §2 with the Earth-radius lamp from the start and
  demote the 45°N fit to a footnote. Structurally cleaner but a big rewrite of
  the page's spine.
