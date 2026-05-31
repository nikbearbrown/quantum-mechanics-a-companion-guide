# CAJAL Figure Intelligence — Chapter 1: Why Quantum Mechanics?

**Source:** `chapters/01-why-quantum-mechanics.md`
**Mode:** `/scan silent`
**Domain note:** Quantum mechanics textbook. CAJAL's natural domain — five canonical experiments (Planck blackbody, photoelectric, Compton, Davisson–Germer, Franck–Hertz) with well-established figure conventions. Author has placed five inline figure references (Fig 1.1–1.5) but has not architected them with `[SCOPE | ...]` markers. CAJAL builds from scratch.

Layout-purpose palette: Okabe-Ito governs. Energy-level diagrams use Sky Blue / Blue for levels, Bluish Green for allowed transitions, Vermillion for blocked/classical-failure regions, Orange for accent annotations. No red-green combinations.

---

## Density Recommendation

**5 figures, Mechanistic density.** The chapter walks through five confrontations between classical predictions and experimental data; each confrontation gets one figure. Five is at the upper boundary but justified — this is the chapter that motivates the entire book by showing the five quantitative facts QM must accommodate.

---

## Zone Map

- **MC:** Compton scattering geometry (energy and momentum conservation across photon-electron collision); Franck–Hertz inelastic-collision sequence (electrons stepping through discrete energy losses).
- **VG:** Compton scattering geometry — the spatial relationship between incident photon, scattered photon, and recoiling electron at angle θ.
- **PQ:** Rayleigh–Jeans vs. Planck distribution (classical divergence vs. observed peak); stopping potential vs. frequency (linear plot with x-intercept ν₀); Tonomura buildup (single-electron statistics accumulating to interference pattern); Franck–Hertz current vs. voltage (regular dips at 4.9 V intervals).

---

## Figure 1.1 — Rayleigh–Jeans Catastrophe vs. Planck Distribution

**Priority: Critical.** PQ. The classical prediction diverges; the data peaks and falls. The contrast is the chapter's opening confrontation and the reader has to see both curves on the same axes.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Spectral energy density (vertical axis, label region blank for typography) vs. frequency (horizontal axis, label region blank). Two curves plotted on the same axes from origin outward: the Rayleigh–Jeans prediction in Vermillion `#D55E00` 1pt solid, rising as ν² without bound and exiting the top of the panel; the Planck distribution in Blue `#0072B2` 1pt solid, rising to a finite peak at characteristic frequency and falling exponentially. The Vermillion curve carries a small arrow at its truncation point indicating "to infinity." A vertical Black `#000000` 0.5pt dashed reference line at the Planck peak's location. Y-axis at exactly zero. White background, flat vector. No log scaling without explicit indication.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background, 300 DPI fallback.
[C] Two curves: Rayleigh–Jeans (rising as ν², unbounded, Vermillion) and Planck distribution (finite peak, exponential fall-off, Blue). Both share the same x-axis (frequency) and y-axis (spectral energy density). Vertical dashed reference at peak location. Truncation arrow on Rayleigh–Jeans where it exits the panel.
[O] Linear axes with origin at lower-left. Both curves start at the origin. Rayleigh–Jeans exits the top of the chart; Planck reaches a peak inside the chart frame and descends to near-zero at the right edge.
[P] Rayleigh–Jeans curve Vermillion `#D55E00` 1pt solid. Planck curve Blue `#0072B2` 1pt solid. Reference line Black `#000000` 0.5pt dashed. Axes Black 1pt. Truncation arrow Vermillion 1pt single-headed.
[E] No axis numerical labels (post-applied typography), no curve labels, no title, no legend, no temperature-isotherm family of curves (one temperature only), no Wien-distribution curve, no historical attribution, no SI/cgs unit conflicts in the image, no human figures, no shadows, no gradient fills, no log scales without explicit indication.

### Block 3 — Negative prompt

text labels, words, axis numerical labels, equations, curve names, temperature labels, legend, chart title, isotherm families, Wien curve overlay, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, log-scale tick marks unless requested

---

## Figure 1.2 — Photoelectric: Stopping Potential vs. Frequency

**Priority: Critical.** PQ. Einstein's K_max = hν − φ as a line with slope h/e and x-intercept ν₀ = φ/h. The figure has to make the threshold visible and the linear relationship undeniable.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Stopping potential V_s (vertical axis) vs. frequency ν (horizontal axis). A single Blue `#0072B2` 1pt straight line with positive slope, crossing the horizontal axis at the threshold frequency ν₀ — to the *left* of ν₀ the line is dashed (no photoemission region) and to the *right* it is solid (photoemission region). The slope equals h/e. A small Orange `#E69F00` filled circle at the x-intercept (ν₀). Below the x-axis on the left side (the dashed region), a Vermillion `#D55E00` 0.5pt dashed bracket marking "no photoemission" — bracket only, no text. Y-axis at zero. White background.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Single straight line on (frequency, stopping potential) axes. Threshold frequency ν₀ marked with an Orange filled circle at the x-intercept. Line dashed below ν₀ (no-emission region), solid above (emission region). Vermillion bracket beneath the dashed segment.
[O] Linear axes. Y-axis at zero (line passes through origin only in the limit; here it crosses x-axis at ν₀ > 0). X-axis from 0 to a value comfortably above ν₀.
[P] Line Blue `#0072B2` 1pt, switching from dashed to solid at ν₀. Threshold marker Orange `#E69F00` filled circle. No-emission bracket Vermillion `#D55E00` 0.5pt dashed. Axes Black 1pt.
[E] No multiple-metal family of lines (one metal only), no work-function labels, no slope-equals-h/e annotation, no axis numerical labels, no equations, no human figures, no historical photographs (Lenard, Einstein, Millikan), no apparatus schematic, no shadows, no gradient fills.

### Block 3 — Negative prompt

text labels, words, equations, axis numerical labels, slope annotations, work function labels, multiple metal lines, apparatus schematics, photoelectron trajectory diagrams, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 1.3 — Compton Scattering Geometry

**Priority: Critical.** MC + VG. The kinematic relationship between incident photon, scattered photon, and recoiling electron. The angles θ and φ have to be visible because the chapter's derivation uses them.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. A single scattering event drawn at the center. From the left, a Blue `#0072B2` 1pt arrow representing the incident photon enters horizontally and reaches a small Black `#000000` filled dot at the scattering vertex (the initially-at-rest electron). From the vertex, two outgoing arrows emerge: the scattered photon, Sky Blue `#56B4E9` 1pt, departing at angle θ above the horizontal; the recoiling electron, Vermillion `#D55E00` 1pt, departing at angle φ below the horizontal. Small Black 0.5pt arc-of-angle marks at the vertex indicating θ (between incident and scattered photon) and φ (between incident direction and recoil). All three vectors share the same vertex. White background, flat vector.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Scattering vertex (Black filled dot — initially-at-rest electron). One incoming photon arrow from left. Two outgoing arrows from vertex: scattered photon (above horizontal at angle θ), recoiling electron (below horizontal at angle φ). Arc-of-angle indicators at the vertex showing θ and φ.
[O] Vertex at panel center-left. Incoming photon horizontal from left. Outgoing photon angled upward and rightward. Recoil angled downward and rightward. Equal arrow lengths optional — angle is the load-bearing visual property.
[P] Incident photon Blue `#0072B2` 1pt. Scattered photon Sky Blue `#56B4E9` 1pt. Recoiling electron Vermillion `#D55E00` 1pt. Scattering vertex Black `#000000` filled dot. Angle arcs Black 0.5pt.
[E] No wavelength labels (λ, λ′), no momentum labels (p_γ, p_e), no energy labels, no angle numerical values, no detector apparatus, no graphite block, no Cartesian axis lines, no atomic nucleus, no other electrons, no historical photographs, no human figures, no Feynman diagrams (this is classical kinematics, not QED).

### Block 3 — Negative prompt

text labels, words, equations, wavelength labels, momentum labels, energy labels, angle numerical values, detector apparatus, graphite blocks, Cartesian axis lines, atomic nuclei, Feynman diagram conventions, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 1.4 — Tonomura Buildup: Single Electrons Form Interference

**Priority: Critical.** PQ + MC. The chapter's most surprising image — a row of frames showing dots accumulating into a fringe pattern. The visual claim is that *each* electron is a point but the *pattern* is a wave.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Four panels in a horizontal row labeled by post-applied typography as "N = 100," "N = 3,000," "N = 20,000," "N = 70,000" — but in the generated image, each panel is just a rectangular detector frame with Black `#000000` 1pt outline. Inside each panel, an increasing density of small Blue `#0072B2` filled dots positioned within a vertical-stripe interference pattern envelope. Panel 1: ~30 dots scattered apparently randomly. Panel 2: ~300 dots beginning to cluster into stripes. Panel 3: ~1500 dots making clear vertical bright bands visible. Panel 4: ~5000 dots forming sharp vertical fringes (5–7 bright bands across the panel width). Panels separated by thin Black 0.5pt vertical rules. White background.

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] Four equal-size horizontal panels showing detector view as electron count increases. Each panel is a rectangular detector frame with Blue dots inside. Panel 1: sparse random-looking dot distribution. Panel 2: denser distribution with hint of vertical clustering. Panel 3: clear vertical bright bands. Panel 4: sharp vertical interference fringes.
[O] Four panels side by side, equal width, equal height. Inner dot density increases left to right. Bright-fringe positions identical across panels (the envelope is the same; only the sampling density changes).
[P] Detector frames Black `#000000` 1pt outline. Dots Blue `#0072B2` filled small circles. Panel dividers Black 0.5pt.
[E] No electron-source apparatus, no biprism, no double-slit schematic, no actual electron-microscope photographs, no count labels inside panels, no axis labels, no scale bar, no human figures, no historical photographs of Tonomura or his lab, no equipment diagram.

### Block 3 — Negative prompt

text labels, words, count labels, axis labels, scale bars, source apparatus, biprism diagrams, double-slit schematics, electron microscope photographs, equipment diagrams, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 1.5 — Franck–Hertz Current vs. Voltage

**Priority: Critical.** PQ + MC. The regular dips at 4.9 V, 9.8 V, 14.7 V are direct evidence of discrete energy levels. The figure has to make the regularity visible.

### Block 1 — Illustrae paste block

Single-column figure, 89mm width, flat vector, white background. Collector current I (vertical axis) vs. accelerating voltage V (horizontal axis). A single Blue `#0072B2` 1pt curve that rises with positive slope, drops sharply at V = 4.9 V, rises again, drops at 9.8 V, rises again, drops at 14.7 V, rises again. The pattern is approximately periodic with period 4.9 V. Three small Orange `#E69F00` filled triangle markers below the x-axis at the three dip positions. Y-axis at zero. White background, flat vector. No multi-element family (mercury only).

### Block 2 — Full SCOPE prompt

[S] Single-column 89mm, vector, white background.
[C] One current-vs-voltage curve with three sharp dips at regular voltage intervals (4.9, 9.8, 14.7 V) followed by partial recoveries. Three Orange triangle markers below the x-axis at dip positions.
[O] Linear axes. Y-axis at zero. X-axis from 0 to ~20 V. Curve oscillates with rising envelope.
[P] Current curve Blue `#0072B2` 1pt solid. Dip markers Orange `#E69F00` filled triangles pointing up. Axes Black `#000000` 1pt.
[E] No axis numerical labels (post-applied typography), no equation annotations, no apparatus schematic, no mercury atom diagrams, no energy-level diagram inset, no photon-emission overlay (separate figure if needed), no historical photographs, no multi-gas family, no human figures, no shadows, no gradient fills.

### Block 3 — Negative prompt

text labels, words, axis numerical labels, equations, apparatus schematics, atom diagrams, energy-level inset, photon overlay, multi-gas curves, historical photographs, human figures, decorative ornament, photographic elements, realistic textures, drop shadows, gradient fills, gradient backgrounds, hand-drawn styles, sketch lines, decorative borders, colorful backgrounds, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**FIGURE 1.4 (Tonomura buildup):** **VIDEO CANDIDATE.** Criterion 1 (transition mechanism is the learning target) and criterion 4 (transformation below direct observation). The buildup from random dots to interference pattern *as electrons arrive one at a time* is the chapter's most counterintuitive claim — and a static four-panel sequence approximates the temporal reality with discrete snapshots. A looping animation that begins blank and accumulates dots until the fringe pattern emerges would communicate the wave-particle duality viscerally. Suggested format: 30-second looping animation, dot accumulation rate variable to give the viewer time to feel the absence-then-emergence of the pattern.

**FIGURE 1.1 (Rayleigh–Jeans vs. Planck):** STATIC SUFFICIENT.
**FIGURE 1.2 (Stopping potential):** STATIC SUFFICIENT.
**FIGURE 1.3 (Compton geometry):** STATIC SUFFICIENT. Some authors animate the collision; static suffices here because the chapter's derivation works from the kinematic snapshot.
**FIGURE 1.5 (Franck–Hertz):** STATIC SUFFICIENT.

**Video candidates identified: 1.** Recommended: **Fig 1.4** — the single-electron interference buildup is the chapter's hardest concept to internalize statically; motion makes the wave-from-particles emergence immediately legible.

---

## Split-point note

The chapter's five-experiment summary table (experiment / year / classical prediction / observed / formula forced) is typography — hand to typesetter as a styled five-row comparison. The equation derivations throughout (Planck distribution derivation, Compton shift derivation, de Broglie wavelength worked example) are typeset math, not figures.

The chapter does NOT yet have a figure for the de Broglie/Davisson–Germer confrontation — only inline references to Fig 1.4 (Tonomura) carry the wave-matter claim. If the editorial team wants a dedicated Davisson–Germer figure (electron beam, nickel crystal, diffraction peak at 50°), CAJAL would architect it as a structural schematic. Currently absent from the author's figure list — flag for editorial decision.

---

## CAJAL discipline checks

- Component counts: all within 6–8 limit ✓
- Exclusion lists: present and specific (especially Fig 1.4's exclusion of source apparatus and Fig 1.3's exclusion of momentum/energy labels) ✓
- No red-green combinations ✓
- No text-in-image ✓
- Y-axis at zero in all PQ charts ✓
- Figure types match concept structure: PQ line charts (correct for Rayleigh–Jeans/Planck and stopping potential and Franck–Hertz), structural schematic (correct for Compton geometry), comparison panels (correct for Tonomura buildup sequence) ✓
- One video candidate flagged
