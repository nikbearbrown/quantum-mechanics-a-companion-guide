# CAJAL Figure Intelligence — Chapter 4: One-Dimensional Problems

**Source:** `chapters/04-one-dimensional-problems.md`
**Mode:** `/scan silent`
**Domain note:** QM textbook. Author places six inline figure references (Fig 4.1–4.6) but no `[SCOPE | ...]` markers. CAJAL builds from scratch. The chapter covers four canonical 1D systems: infinite square well, harmonic oscillator, finite square well, tunneling/alpha decay.

---

## Density Recommendation

**6 figures, Mechanistic density.** All six earn their place — this is the chapter where students must *see* what bound-state wave functions and tunneling barriers look like, not just compute them. Six is at the upper boundary, justified because each canonical 1D system gets one figure and tunneling gets two (potential + Geiger-Nuttall data).

---

## Zone Map

- **MC:** Tunneling through the Coulomb barrier (alpha-decay mechanism); ladder-climbing in the harmonic oscillator.
- **VG:** Wave function shapes for infinite-well eigenstates (4.1); probability densities showing correspondence principle at large n (4.2); harmonic-oscillator eigenfunctions with Gaussian envelope (4.3); finite-well potential geometry showing classically forbidden tails (4.4); nuclear potential well for alpha decay (4.5).
- **PQ:** Geiger-Nuttall log(half-life) vs. 1/√E across 24 orders of magnitude (4.6) — the chapter's quantitative payoff.

---

## Figure 4.1 — Infinite Square Well: First Four Eigenfunctions

**Priority: Critical.** VG. The canonical figure of introductory QM. ψ₁ through ψ₄ stacked vertically, each showing the standing-wave shape with n half-wavelengths.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Four panels stacked vertically, each showing the well interval [0, L] with two short Black `#000000` 1pt vertical lines at x=0 and x=L (the infinite walls). In each panel, a Blue `#0072B2` 1pt curve representing ψ_n(x): panel 1 (n=1) a single half-sine arch above the x-axis; panel 2 (n=2) a full sine cycle (one node at x=L/2); panel 3 (n=3) one-and-a-half sine periods (two nodes); panel 4 (n=4) two full sine periods (three nodes). Each panel's curve oscillates about a horizontal baseline (the x-axis). Light gray dashed horizontal baseline in each panel. Vertical Black 0.5pt dashed lines marking each interior node. Y-axis from −√(2/L) to +√(2/L). White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Four vertically stacked panels showing ψ_n(x) for n=1,2,3,4 over [0, L]. Each curve has n half-wavelengths between the walls.
[O] Vertical stack with equal panel heights. Common x-axis range [0, L]. Common y-axis range (symmetric around 0). Walls marked at x=0, x=L.
[P] Curves Blue `#0072B2` 1pt solid. Baselines light gray dashed. Node markers Black `#000000` 0.5pt dashed vertical. Walls Black 1pt vertical. Axes Black 1pt.
[E] No probability-density (|ψ|²) overlay (separate figure), no energy-level diagram, no quantum-number labels in image, no equation overlays, no boundary-condition annotations, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis labels, equations, quantum-number labels, energy levels, probability-density overlay, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4.2 — Probability Density and Correspondence Principle

**Priority: Important.** PQ + VG. |ψ_n|² for n=1, n=2, n=10 — showing how rapid oscillations at high n approach a uniform classical distribution.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Three panels stacked vertically. Each panel shows |ψ_n|² vs. x over [0, L]. Top panel (n=1): single Blue `#0072B2` 1pt curve, sin² shape, single peak in the middle. Middle panel (n=2): Sky Blue `#56B4E9` 1pt curve, two peaks with zero at x=L/2. Bottom panel (n=10): Orange `#E69F00` 1pt curve, ten oscillating peaks with rapidly varying envelope. A horizontal Black `#000000` 0.5pt dashed line at the classical-uniform value 1/L spans the bottom panel only (the asymptote). Y-axis at zero in all panels. Vertical Black 1pt walls at x=0 and x=L. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Three stacked panels showing |ψ_n|² for n=1, 2, 10. Classical-uniform asymptote line in bottom panel only.
[O] Vertical stack, equal panel heights, shared x-axis [0, L].
[P] n=1 curve Blue `#0072B2` 1pt. n=2 curve Sky Blue `#56B4E9` 1pt. n=10 curve Orange `#E69F00` 1pt. Classical asymptote Black `#000000` 0.5pt dashed horizontal. Walls Black 1pt vertical. Axes Black 1pt.
[E] No axis numerical labels, no n labels in image (post-applied), no wave-function ψ_n overlay (this is |ψ|² only), no energy-level diagram, no equation overlays, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis labels, n labels, equations, ψ_n curves, energy levels, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4.3 — Harmonic Oscillator Eigenfunctions

**Priority: Critical.** VG. The first three or four ψ_n for the SHO, each plotted against the parabolic potential V(x) = ½mω²x² with horizontal energy-level lines for context.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Cartesian axes with x horizontal and energy/wave-function vertical. A Black `#000000` 1pt parabolic curve V(x) = ½mω²x² centered at origin. Four horizontal energy-level lines at heights E_n = ħω(n + ½) for n=0, 1, 2, 3, each in Black 0.5pt solid running between the classical turning points where V(x) = E_n. Sitting on each energy-level line, a Blue `#0072B2` 1pt curve representing ψ_n(x): n=0 a Gaussian bump, n=1 antisymmetric one-node curve, n=2 two-node symmetric curve, n=3 three-node antisymmetric curve. Curves are vertically offset so each sits on its energy-level line, with each curve's zero-line being the energy line itself. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Parabolic potential V(x). Four horizontal energy-level lines. Four wave functions ψ_n vertically offset to sit on their energy lines.
[O] Standard energy-axis vertical, position horizontal. Wave functions superposed on energy levels (each ψ_n drawn with its baseline at E_n).
[P] Parabola Black `#000000` 1pt. Energy levels Black 0.5pt horizontal. Wave functions Blue `#0072B2` 1pt. Axes Black 1pt.
[E] No probability-density |ψ_n|² (separate figure if needed), no zero-point arrow, no classical-turning-point markers (energy lines naturally show this where they meet the parabola), no equation overlays, no quantum-number labels, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis labels, quantum-number labels, equations, probability-density overlay, zero-point arrows, turning-point markers, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4.4 — Finite Square Well: Tails into the Forbidden Region

**Priority: Critical.** VG. The contrast with the infinite well — wave function decays exponentially in the classically forbidden region instead of being identically zero.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Cartesian axes. V(x) shown as a piecewise Black `#000000` 1pt curve: V=0 for x<−a, V=−V₀ for |x|<a, V=0 for x>a. The well-bottom region [−a, +a] shown as a horizontal Black line at depth −V₀. Vertical Black 1pt segments at x=±a connecting the well bottom to the V=0 baseline outside. A horizontal Black 0.5pt energy-level line at some E<0 spanning the full panel width. On this energy level, a single Blue `#0072B2` 1pt wave function curve: oscillating cosine-like inside [−a, +a], decaying exponentially outside both walls. The exterior tails clearly extend visible distances into the V=0 region before fading. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Finite-well potential V(x) shown explicitly. Single bound-state wave function ψ(x) drawn at energy E<0 with oscillating interior and exponential exterior tails.
[O] Position axis horizontal, energy/V axis vertical. Wave function drawn at its energy level with that level as the baseline.
[P] Potential curve Black `#000000` 1pt. Energy level Black 0.5pt horizontal. Wave function Blue `#0072B2` 1pt. Axes Black 1pt.
[E] No probability-density overlay, no κ or k labels in image, no infinite-well comparison, no scattering-state continuum, no multiple bound states (one only), no boundary-condition equations, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis labels, equations, k or κ labels, infinite-well comparison, scattering continuum, multiple bound states, boundary equations, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4.5 — Nuclear Potential Well: Alpha-Decay Geometry

**Priority: Critical.** VG. Combined attractive nuclear well + repulsive Coulomb barrier, with the alpha-particle energy line crossing the barrier and exiting on the right.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Radial axis r horizontal (from origin rightward). V(r) vertical. The potential drawn as a Black `#000000` 1pt curve: deep attractive square well from r=0 to r=R (nuclear radius) at value −V_nuc, then jumping up to the Coulomb peak at r=R, then decaying as ~1/r to the right. A horizontal Black 0.5pt energy-level line at E (positive, below the Coulomb peak) spanning the full panel. The barrier region (between r=R and r=r₂, where V(r₂)=E) shaded with Vermillion `#D55E00` 15% opacity fill — the tunneling region. Inside the well, a Blue `#0072B2` 1pt oscillating wave function curve sitting on the energy level. Beyond the outer turning point r₂, a Blue 1pt outgoing wave that connects to the well's wave function with an exponentially-decaying segment through the barrier. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Nuclear potential V(r): attractive well (0 to R), Coulomb barrier (R to large r). Alpha energy level horizontal. Tunneling region shaded. Wave function: oscillating inside, decaying through barrier, oscillating outside.
[O] r-axis horizontal, V-axis vertical. Wave function superposed at energy level. Tunneling region (between inner and outer turning points) shaded.
[P] Potential Black `#000000` 1pt. Energy level Black 0.5pt horizontal. Tunneling region Vermillion `#D55E00` 15% opacity fill. Wave function Blue `#0072B2` 1pt. Axes Black 1pt.
[E] No equation overlays, no specific Z values, no specific energy values (4.27 MeV labels post-applied if needed), no alpha-particle iconography (no helium balls), no daughter nucleus depiction, no historical photographs (Gamow), no human figures, no shadows, no decay-product label.

### Block 3 — Negative prompt

text labels, words, axis labels, equations, Z values, energy values, alpha-particle icons, helium balls, daughter nuclei, historical photographs, decay-product labels, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4.6 — Geiger-Nuttall Plot

**Priority: Important.** PQ. log₁₀(half-life) vs. 1/√E across 24 orders of magnitude — the chapter's quantitative payoff for the Gamow tunneling calculation.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Vertical axis: log₁₀(half-life in seconds), spanning −6 to +25. Horizontal axis: 1/√E (with E in MeV), spanning a representative range. Several Blue `#0072B2` filled small circles plotted along an approximately straight line — each circle represents one alpha-emitting nucleus (e.g., Po-212 at the lower-left short-half-life end, U-238 and Th-232 at the upper-right long-half-life end). A Blue `#0072B2` 1pt straight line fitted through the points. White background, axes Black `#000000` 1pt. Y-axis starts at the lowest data point (does NOT start at zero in this log-vs-log-ish plot — but the axis itself is clearly bounded; the proportional-ink rule applies to bar charts, not log plots of widely spread data).

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] log₁₀(t₁/₂) vs. 1/√E scatter plot with ~10 nucleus data points on an approximately linear trend. Fitted straight line through points.
[O] Linear axes (log values on y, 1/√E on x). Data points distributed along the line across the 24-order range.
[P] Data points Blue `#0072B2` filled small circles. Fitted line Blue 1pt solid. Axes Black `#000000` 1pt.
[E] No axis numerical labels (post-applied typography), no nuclide labels at each point, no error bars (chapter doesn't provide them), no fit equation, no historical attribution, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, axis numerical labels, nuclide labels, error bars, fit equations, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**FIGURE 4.5 (Alpha-decay tunneling):** **VIDEO CANDIDATE.** Criterion 1 (transition mechanism is the learning target) and criterion 4 (transformation below direct observation). The wave-function leakage through the barrier is the chapter's central tunneling claim — and the static figure has to encode it through a wave-function that oscillates → decays → oscillates again across the barrier shading. Animation showing the wave-function amplitude propagating into the barrier and emerging as an outgoing wave would communicate the leakage viscerally. Suggested format: looping animation with wave-function amplitude pulsing inside the well and faintly leaking through the barrier as outgoing flux.

**FIGURE 4.2 (Correspondence principle):** STATIC SUFFICIENT — borderline. A slider through n=1, 2, 3, ... 10 would show the convergence to classical uniform; but three snapshots in static panels show the trend cleanly.

**Others:** STATIC SUFFICIENT.

**Video candidates identified: 1.** Recommended: **Fig 4.5 (alpha-decay tunneling)** — the leakage mechanism is the chapter's hardest concept to internalize statically; motion makes the wave-function-through-barrier transmission immediately legible.

---

## Split-point note

All equation derivations (ladder operators, Hermite-equation solutions, WKB integral, Gamow factor) are typeset math, not figures. The probability calculation tables (P_n for various n in central third of well) are typography. The transmission-coefficient formula and Geiger-Nuttall straight-line algebra are typeset, not visual.

---

## CAJAL discipline checks

- Component counts: all within 6–8 limit ✓
- Exclusion lists: present and specific (especially Fig 4.5's exclusion of alpha-particle iconography — keep the figure about the *wave function*, not the helium ball cartoon) ✓
- No red-green combinations ✓
- No text-in-image ✓
- Y-axis at zero where applicable (note: Fig 4.6 is a log plot, where proportional-ink doesn't apply — flagged as exception)
- Figure types match: VG wave-function plots (correct for eigenstates), structural schematic (correct for potential geometries), PQ scatter (correct for Geiger-Nuttall) ✓
- One video candidate flagged: alpha-decay tunneling
- All six figures retained — the chapter is the canonical 1D-systems chapter and earns the density
