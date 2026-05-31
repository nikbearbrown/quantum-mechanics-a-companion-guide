# CAJAL Figure Intelligence — Chapter 2: Mathematical Foundations

**Source:** `chapters/02-mathematical-foundations.md`
**Mode:** `/scan silent`
**Domain note:** QM textbook. Author places five inline figure references (Fig 2.1–2.5) but has not architected with `[SCOPE | ...]` markers. CAJAL builds from scratch. Layout-purpose palette: Okabe-Ito governs.

---

## Density Recommendation

**4 figures, Mechanistic density.** Keep four: double-slit single-electron buildup (2.1), complex plane with z = re^iθ (2.2), interference intensity 2cos²(kd sinθ/2) (2.3), Stern–Gerlach sequential measurements (2.4). Drop Fig 2.5 (integration-by-parts steps) — that is *typeset math*, not a figure. A figure of derivation steps is text rendered as an image, which CAJAL declines.

**Cut from current draft:** Fig 2.5 (integration-by-parts steps for momentum Hermiticity proof). The derivation is already on the page as LaTeX-typeset equations. A figure of the same equations adds nothing.

---

## Zone Map

- **MC:** Sequential Stern–Gerlach apparatus — successive σ_z, σ_x, σ_z measurements showing how a second basis "destroys" the first measurement's outcome.
- **VG:** Complex plane (z = a + bi as a point, r and θ as polar coordinates). Double-slit experimental setup with single-electron buildup. Stern–Gerlach beam paths.
- **PQ:** Interference intensity pattern |ψ|² = 2cos²(kd sinθ/2) — periodic bright/dark bands across angle.

---

## Figure 2.1 — Double-Slit Single-Electron Buildup

**Priority: Critical.** VG + PQ. The chapter's opening experiment that motivates the whole formalism. Combines apparatus schematic with the sequential-buildup outcome.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Left side: schematic of double-slit apparatus — a single electron source on the far left (small Black `#000000` filled dot with rightward Sky Blue `#56B4E9` 1pt arrow), a vertical barrier with two horizontal gaps (the two slits) at the center-left, a detector screen as a vertical Black `#000000` 0.5pt line on the right. From each slit, Sky Blue 0.5pt fan-out arcs reach the detector screen. Right side: three small inset panels stacked vertically showing detector hits accumulating — first inset ~10 Blue `#0072B2` dots scattered, second inset ~100 dots showing emerging vertical clustering, third inset ~1000 dots forming sharp vertical fringes. Thin Black 0.5pt vertical rule separates apparatus side from buildup side. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Left: electron source + two-slit barrier + detector screen + fan-out from each slit. Right: three stacked buildup panels (sparse, clustering, fringes).
[O] Side-by-side layout with vertical divider. Apparatus runs left-to-right within left half. Buildup panels stack vertically within right half, oldest at top.
[P] Source dot Black `#000000` filled. Incident-beam arrow Sky Blue `#56B4E9` 1pt. Slit barrier Black 1pt. Slit fan-out arcs Sky Blue 0.5pt. Detector dots Blue `#0072B2` filled. Detector screen Black 0.5pt vertical line. Vertical divider Black 0.5pt.
[E] No wavelength labels, no slit-separation labels (d), no angle labels (θ), no source-type designation (electron gun specifics), no quantum-mechanical wave-function overlay, no historical photographs, no Feynman path overlays, no biprism (Tonomura specifics belong to Ch. 1 figure), no human figures, no shadows, no gradient fills.

### Block 3 — Negative prompt

text labels, words, wavelength labels, slit-separation labels, angle labels, source-type designations, wavefunction overlays, historical photographs, Feynman paths, biprism schematics, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2.2 — The Complex Plane

**Priority: Critical.** VG. Foundational structural diagram — every reader of QM needs the (Re, Im) plane with a labeled point z, its modulus r, and its angle θ.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Cartesian plane with horizontal axis (Real) and vertical axis (Imaginary), axes Black `#000000` 1pt with arrowheads at positive ends. A single point z marked as a Blue `#0072B2` filled small circle in the upper-right quadrant. A Blue 1pt solid line from the origin to z. A Black 0.5pt dashed vertical line dropping from z to the real axis (showing the real part a), and a Black 0.5pt dashed horizontal line from z to the imaginary axis (showing the imaginary part b). A Black 0.5pt arc near the origin indicating the angle θ between the positive real axis and the line to z. Below z (its complex conjugate z*) marked as a Vermillion `#D55E00` filled small circle in the lower-right quadrant (mirror image across the real axis). A faint Vermillion 0.5pt dashed line from origin to z*. White background.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] (Real, Imaginary) Cartesian plane. Point z in upper-right with modulus line and angle arc. Real and imaginary projections shown as dashed lines. Conjugate point z* mirrored in lower-right.
[O] Standard math orientation: positive real to the right, positive imaginary up. Origin at panel center.
[P] Axes Black `#000000` 1pt with arrowheads. z marker Blue `#0072B2` filled circle. Modulus line Blue 1pt. Projections Black 0.5pt dashed. Angle arc Black 0.5pt. Conjugate z* Vermillion `#D55E00` filled circle. Conjugate modulus line Vermillion 0.5pt dashed.
[E] No numerical labels, no equation overlays, no e^iθ formula in image, no unit circle (unless specifically requested for a multiplication figure — separate figure), no Argand-diagram historical typography, no multiple points, no rotation animation cues, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, numerical labels, equations, formula overlays, unit circle, multiple labeled points, historical typography, rotation cues, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2.3 — Interference Intensity Pattern

**Priority: Important.** PQ. The result of the four-line algebra: |ψ|² = 2cos²(kd sinθ/2). Periodic bright bands across angle θ.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Intensity (vertical axis, label region blank) vs. angle θ (horizontal axis, label region blank). A single Blue `#0072B2` 1pt curve oscillating as cos²(·) — five to seven maxima visible across the panel width, each maximum at value 2, each minimum at 0. Y-axis at zero. Above the maxima, small Orange `#E69F00` filled triangles pointing down marking the bright-band positions. Between maxima, small Black `#000000` 0.5pt vertical tick marks at the zero positions (dark bands). White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] cos²-shape intensity curve oscillating from 0 to 2 across the angle axis. Five-to-seven maxima visible. Orange downward triangles marking bright-band positions. Black tick marks at zero positions.
[O] Linear axes. Y-axis at zero, runs to ~2.2. X-axis centered on θ=0 with symmetric ±θ range.
[P] Curve Blue `#0072B2` 1pt solid. Bright-band markers Orange `#E69F00` filled triangles. Dark-band ticks Black `#000000` 0.5pt. Axes Black 1pt.
[E] No equation overlay, no axis numerical labels, no Bragg-condition annotations, no envelope from single-slit diffraction (this is pure double-slit, idealized), no wavelength or slit-spacing labels, no source-detector schematic (separate figure), no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, equations, axis numerical labels, Bragg annotations, single-slit envelope, wavelength labels, slit-spacing labels, source/detector schematics, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2.4 — Stern–Gerlach Sequential Measurements

**Priority: Critical.** MC. Three magnets in sequence: σ_z splits, then σ_x splits each beam, then σ_z applied to one σ_x output reveals that the original σ_z information is gone. The non-commutativity of σ_z and σ_x made spatial.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width (or double-column 174mm preferred if available), flat vector, white background. Horizontal apparatus layout left-to-right: oven source (small Black `#000000` filled rectangle) emitting an unpolarized beam (Sky Blue `#56B4E9` 1pt arrow rightward); first magnet (Blue `#0072B2` outlined box labeled implicitly σ_z) splitting the beam into two paths — upper (Sky Blue 1pt, |↑⟩) and lower (Sky Blue 1pt, |↓⟩); a beam block (Vermillion `#D55E00` filled rectangle) absorbs the lower path; the upper path enters a second magnet (Blue outlined box, σ_x) which splits it into two new paths — upper (Sky Blue 1pt) and lower (Sky Blue 1pt); the upper path enters a third magnet (Blue outlined box, σ_z) which splits *again* into both |↑⟩ and |↓⟩ outputs (Sky Blue 1pt and Sky Blue 1pt) — the punchline that σ_z measurement after σ_x has lost the original definite spin-up. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Double-column 174mm preferred (else single-column 89mm), vector, white background.
[C] Linear left-to-right sequence: oven → σ_z magnet (splits) → block on |↓⟩ → σ_x magnet (splits the surviving |↑⟩) → block or pass-through on one σ_x output → σ_z magnet (splits again, both outputs).
[O] Strict horizontal flow. Beams split vertically (upper/lower) at each magnet. Blocks marked as filled Vermillion rectangles on the suppressed paths.
[P] Oven Black `#000000` filled rectangle. Magnet boxes Blue `#0072B2` 1pt outline, no fill. Beam paths Sky Blue `#56B4E9` 1pt. Beam blocks Vermillion `#D55E00` filled.
[E] No spin labels (|↑⟩, |↓⟩, etc., post-applied), no magnet pole-piece geometry (just outlined boxes), no atom trajectories curving (use straight beams for clarity), no detection counter readouts, no spinor mathematics in the image, no historical Stern–Gerlach photographs, no silver atom labels, no temperature labels, no human figures, no shadows.

### Block 3 — Negative prompt

text labels, words, spin labels, pole-piece geometry, curved trajectories, detector readouts, spinor math, historical photographs, atom-species labels, temperature labels, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**FIGURE 2.1 (Double-slit buildup):** STATIC SUFFICIENT. The Tonomura video case was already flagged in Ch 1 Fig 1.4 — having two video versions across consecutive chapters is editorial overkill. Static three-panel inset here.

**FIGURE 2.4 (Stern–Gerlach):** STATIC SUFFICIENT — borderline. Sequential measurement could be animated with beams firing through magnets in time. But the static diagram is the canonical representation in every QM textbook; students need to *read* the sequence, not watch it.

**Others:** STATIC SUFFICIENT.

**Video candidates identified: 0.** (The buildup case is covered in Ch 1; not duplicated here.)

---

## Split-point note

The chapter's tables (Dirac notation summary, Pauli matrices reference) are typography. The momentum-Hermiticity integration-by-parts derivation (draft Fig 2.5) is typeset math, not a figure — drop. All equation derivations throughout (Planck-style expansions, interference algebra, Pauli eigenvector calculations) are typeset LaTeX, not CAJAL territory.

---

## CAJAL discipline checks

- Component counts: all within 6–8 limit ✓
- Exclusion lists: present and specific (especially Fig 2.4's exclusion of pole-piece geometry and curved trajectories — common Stern–Gerlach figure clutter) ✓
- No red-green combinations ✓
- No text-in-image ✓
- Figure types match: structural schematic (correct for apparatus diagrams), conceptual map / Argand (correct for complex plane), PQ line chart (correct for cos² intensity) ✓
- One drop recommended: Fig 2.5 (integration-by-parts) is typeset math, not a figure
