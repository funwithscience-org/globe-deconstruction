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
