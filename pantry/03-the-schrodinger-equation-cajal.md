# CAJAL Figure Intelligence — Chapter 3: The Schrödinger Equation

**Source:** `chapters/03-the-schrodinger-equation.md`
**Mode:** `/scan silent`
**Domain note:** QM textbook. Author places seven inline figure references (Fig 3.1–3.7) but no `[SCOPE | ...]` markers. CAJAL builds from scratch. Layout-purpose palette: Okabe-Ito governs.

---

## Density Recommendation

**5 figures, Mechanistic density.** Drop two: Fig 3.1 (anatomy of TDSE) is *equation annotation*, typography territory, not a CAJAL figure; Fig 3.6 (animation-ready snapshots of superposition |ψ|²) is the same content as Fig 3.5 in different format — collapse. Keep: wave-packet spreading comparison (3.2), ground-state probability density (3.3), continuity-equation region (3.4), phasor beating (3.5), Gaussian width vs. time (3.7).

**Cut from current draft:**
- Fig 3.1 (TDSE anatomy with labeled terms) — typeset math with margin annotations, not a CAJAL figure
- Fig 3.6 (three-snapshot superposition |ψ|² sequence) — collapses into Fig 3.5's phasor-beat representation

---

## Zone Map

- **MC:** Continuity equation — probability density and current with rate-of-change across region boundaries. Wave-packet spreading mechanism (each k-component moves at different speed). Phasor beating mechanism (two stationary states' relative phase rotation produces observable oscillation at the Bohr frequency).
- **VG:** Probability density |ψ₁|² shape for ground state (single peak in center, depleted at edges); 1D region with current flowing across boundaries.
- **PQ:** Gaussian wave-packet width σ(t) vs. time (linear at late times); ground-state probability density (cos² shape over [0, L]).

---

## Figure 3.1 — Wave Packet: Schrödinger Equation vs. Diffusion Equation

**Priority: Important.** VG. The chapter's key claim about the role of the factor of i: Schrödinger evolution preserves the packet's coherent shape (it spreads but remains a packet); the diffusion equation (without the i) smooths irreversibly. Side-by-side comparison.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Two panels side by side. Both panels: probability density |ψ|² (vertical axis) vs. position x (horizontal axis). Left panel ("Schrödinger evolution"): three Blue `#0072B2` 1pt curves showing an initial sharp Gaussian peak at t=0, a moderately wider Gaussian at t=t₁, and a much wider but still Gaussian shape at t=t₂. Right panel ("Diffusion equation"): three Vermillion `#D55E00` 1pt curves at the same three times — same Gaussian at t=0, smoothed and lower-amplitude at t=t₁, nearly flat at t=t₂. Y-axis at zero in both panels. Thin Black `#000000` 0.5pt vertical rule separates the panels. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Two side-by-side panels. Left: Schrödinger evolution as three Gaussian curves spreading over time (Blue). Right: Diffusion evolution as three curves spreading and *decaying in amplitude* over time (Vermillion). Same initial condition in both panels.
[O] Side-by-side. Y-axis at zero in both. X-axis range identical. Time samples identical (t=0, t=t₁, t=t₂).
[P] Schrödinger curves Blue `#0072B2` 1pt. Diffusion curves Vermillion `#D55E00` 1pt. Axes Black 1pt. Panel divider Black 0.5pt.
[E] No axis numerical labels, no time labels at curves, no equation overlays, no panel headers in image (post-applied typography), no real-part-of-ψ curves (this is |ψ|² only), no complex-plane phasor overlay, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, equations, time labels, panel headers, real-part overlays, phasor overlays, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3.2 — Ground-State Probability Density (Infinite Square Well)

**Priority: Important.** PQ + VG. |ψ₁|² = (2/L)sin²(πx/L). Single hump centered in the well; the chapter's worked-example computation shows the left quarter has only 9% probability, not 25%.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Single Blue `#0072B2` 1pt curve plotted as sin²-shape over the interval [0, L]. The curve starts at 0 at x=0, rises smoothly to a maximum at x=L/2, falls smoothly back to 0 at x=L. The region [0, L/4] is shaded with a light Orange `#E69F00` translucent fill at 25% opacity — the "left quarter" with probability 1/4 − 1/(2π) ≈ 0.091. Vertical Black `#000000` 0.5pt dashed reference lines at x=0, x=L/4, x=L/2, x=L. Y-axis at zero. Two short vertical Black 1pt boundaries at x=0 and x=L (the well walls). White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] sin²-shape probability density over [0, L]. Shaded left-quarter region. Reference lines at the quarter, half, and well boundaries. Well-wall markers at x=0 and x=L.
[O] Standard axes, x from 0 to L, y from 0 to ~2/L. Well boundaries vertical at x=0 and x=L.
[P] Curve Blue `#0072B2` 1pt solid. Shaded region Orange `#E69F00` 25% opacity fill. Reference lines Black `#000000` 0.5pt dashed. Well walls Black 1pt vertical. Axes Black 1pt.
[E] No axis numerical labels (L, L/4, L/2 applied as post-typography), no equation overlay, no second eigenstate, no animation cues, no expectation-value marker, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis numerical labels, equations, second eigenstate curve, animation cues, expectation-value markers, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3.3 — Continuity Equation: Probability Current Across Region

**Priority: Critical.** MC. The chapter's local-conservation argument — probability flows across boundaries; the rate of change of total probability in a region equals current in minus current out.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. A horizontal 1D axis. A rectangular region [a, b] shaded with Sky Blue `#56B4E9` 25% opacity fill, with thin Black `#000000` 1pt vertical lines at x=a and x=b marking the boundaries. Inside the region, three small Blue `#0072B2` filled dots representing the probability density ρ(x,t) at three sample points. At x=a, a horizontal Bluish Green `#009E73` 1pt rightward arrow labeled implicitly j(a) showing current entering. At x=b, a horizontal Vermillion `#D55E00` 1pt rightward arrow labeled implicitly j(b) showing current leaving. Above the shaded region, a single Black `#000000` 1pt downward arrow representing dρ/dt where current in differs from current out. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] 1D shaded region [a, b]. Probability-density indicators inside. Inward current arrow at left boundary (j(a), green). Outward current arrow at right boundary (j(b), vermillion). Rate-of-change indicator above region.
[O] Horizontal axis. Region centered on axis. Current arrows at the two vertical boundaries. Rate-of-change arrow above the shaded region.
[P] Shaded region Sky Blue `#56B4E9` 25% opacity. Boundaries Black `#000000` 1pt vertical. Density dots Blue `#0072B2` filled. Inward current Bluish Green `#009E73` 1pt arrow. Outward current Vermillion `#D55E00` 1pt arrow. Rate-of-change indicator Black 1pt arrow.
[E] No equation overlay, no axis numerical labels, no specific function for ρ(x), no multiple regions, no 3D volume rendering, no historical attribution, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, equations, axis numerical labels, ρ(x) function curve, multiple regions, 3D rendering, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3.4 — Phasor Beating: One Stationary State vs. Two

**Priority: Critical.** MC. The chapter's central insight about why spectral lines exist: a single stationary state's phase rotates invisibly; two stationary states beat at the Bohr frequency, producing observable oscillation in |ψ|².

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Two panels side by side. Left panel ("one phasor"): a single Argand diagram with a Blue `#0072B2` filled arrow from origin to a point on the unit circle, with a small curved Black `#000000` 0.5pt arrow indicating counterclockwise rotation. Below the Argand: a flat horizontal Sky Blue `#56B4E9` 1pt line representing |ψ|² unchanged over time. Right panel ("two phasors"): an Argand diagram with two arrows (Blue and Orange `#E69F00`) rotating at different rates, both filled, with a third Reddish Purple `#CC79A7` arrow representing their sum (vector addition). Below the Argand: a sinusoidal Reddish Purple 1pt curve representing |ψ|² oscillating over time at the Bohr frequency. Thin Black `#000000` 0.5pt vertical rule separates panels. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Two panels. Left: single phasor on Argand + flat |ψ|² below. Right: two phasors + sum phasor on Argand + oscillating |ψ|² below.
[O] Side-by-side panels. Argand diagrams on top of each panel; |ψ|²(t) curves on bottom.
[P] Single phasor Blue `#0072B2` filled. Rotation arc Black `#000000` 0.5pt. Two phasors Blue and Orange `#E69F00` filled. Sum phasor Reddish Purple `#CC79A7` filled. Flat |ψ|² Sky Blue `#56B4E9` 1pt. Oscillating |ψ|² Reddish Purple 1pt. Panel divider Black 0.5pt.
[E] No equation overlays, no Bohr-frequency labels in image, no specific energy values, no multiple superpositions, no atomic transitions iconography, no spectral-line overlay, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, equations, frequency labels, energy values, atomic iconography, spectral lines, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3.5 — Gaussian Wave Packet: Width vs. Time

**Priority: Important.** PQ. σ(t) = σ₀√(1 + (ħt/2mσ₀²)²). Late-time linear growth is the chapter's key claim about dispersion.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Position-space width σ(t) (vertical axis) vs. time t (horizontal axis). A single Blue `#0072B2` 1pt curve starting at σ(0)=σ₀ on the y-axis, initially flat (parabolic minimum at t=0), then transitioning smoothly to linear growth. A Vermillion `#D55E00` 1pt dashed asymptote tangent to the late-time linear regime, drawn extending from the late-time portion of the curve back through the y-axis. A small Orange `#E69F00` filled circle marker at t=0 indicating the minimum-width point. Y-axis at zero. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] σ(t) curve: starts at σ₀ on y-axis, flat near t=0, then linear at late times. Dashed late-time asymptote. Marker at minimum.
[O] Linear axes. Y-axis at zero. X-axis from 0 to a late-time value where linear regime is well established.
[P] σ(t) curve Blue `#0072B2` 1pt solid. Asymptote Vermillion `#D55E00` 1pt dashed. Minimum marker Orange `#E69F00` filled circle. Axes Black `#000000` 1pt.
[E] No equation overlay, no axis numerical labels, no τ = 2mσ₀²/ħ characteristic-time annotation, no specific particle (electron, atom, baseball), no comparison curves for different σ₀, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, equations, axis numerical labels, time-scale annotations, particle-type labels, multiple σ₀ curves, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**FIGURE 3.4 (Phasor beating):** **VIDEO CANDIDATE.** Criterion 1 (transition mechanism is the learning target) and criterion 3 (cyclical process where return-to-start is part of the concept). The chapter's key insight is that *rotation produces oscillation* — a single phasor rotates invisibly (|sum|² constant), but two phasors at different rates produce a visibly beating sum. Animation makes this immediate; static phasor diagrams require the reader to mentally rotate. Suggested format: looping animation showing left panel single-phasor rotating with flat |ψ|² below; right panel two-phasor rotation with beating sum.

**FIGURE 3.1 (Schrödinger vs. diffusion):** STATIC SUFFICIENT — borderline. The temporal evolution could be animated as both curves spread over time, but three snapshots in each panel capture the difference cleanly.

**Others:** STATIC SUFFICIENT.

**Video candidates identified: 1.** Recommended: **Fig 3.4 (phasor beating)** — the rotation→oscillation mechanism is exactly the kind of transition that motion communicates and static can only approximate with cycle-arrows.

---

## Split-point note

The chapter's TDSE-anatomy figure (draft Fig 3.1) is typeset equation with margin labels — typography, not CAJAL. Drop. The superposition snapshot figure (draft Fig 3.6) duplicates the phasor-beating concept of Fig 3.5 — collapse into the single phasor figure (CAJAL Fig 3.4 above). All equation derivations (continuity equation, normalization preservation, Bohr-frequency emergence) are typeset math throughout.

---

## CAJAL discipline checks

- Component counts: all within 6–8 limit ✓
- Exclusion lists: present and specific ✓
- No red-green combinations ✓
- No text-in-image ✓
- Figure types match: comparison panels (Schrödinger vs. diffusion), PQ line chart (probability density and width-vs-time), structural schematic (continuity region), conceptual map / Argand (phasor beating) ✓
- Two drops recommended: Fig 3.1 (equation annotation, typography) and Fig 3.6 (duplicate of phasor-beat concept)
- One video candidate flagged: phasor beating
