# CAJAL Figure Intelligence — Chapter 6: The Hydrogen Atom

**Source:** `chapters/06-the-hydrogen-atom.md`
**Mode:** `/scan silent`
**Domain note:** Canonical CAJAL territory. Hydrogen is the most-figured topic in introductory quantum mechanics — emission spectrum, effective potential, radial wave function, radial probability density, orbital isosurfaces, Stern–Gerlach. The author has placed six inline figure references, all well-motivated. The job here is to validate each against discipline, flag the one redundancy with Chapter 1 (Stern–Gerlach), and consider whether the chapter is missing the energy-level diagram that the SO(4) degeneracy argument almost requires.

---

## Density Recommendation

**6 figures, Mechanistic density.** Hydrogen is the chapter where the math has been working toward observable structure all along; figures earn their keep here because the orbital cloud, the radial probability shape, and the spectral lines are *what the prediction looks like*. The chapter's main pedagogical move — dismantling the orbit picture — is itself a visual argument (most-probable radius ≠ average radius), so trimming below 5 figures would gut the argument. CAJAL adds one figure the author missed (energy-level diagram showing the SO(4) degeneracy) and reduces redundancy by recommending that Fig 6.3 be folded into Fig 6.4 as a two-panel.

Final count: **6 figures** — 5 validated/restructured author-placed + 1 CAJAL-added energy-level diagram.

---

## Zone Map

- **MC (Mechanism Complexity):** Separation of variables → radial equation → ansatz substitution → Bohr radius and 13.6 eV falling out. The radial mechanism is genuinely complex; effective-potential and wave-function plots break it open.
- **VG (Verification Gap):** The chapter's central claim — "there is no orbit, there is a probability cloud" — needs the radial probability density with both the most-probable-radius marker AND the average-radius marker. Without that figure, the verification is purely algebraic and students will keep the orbit picture anyway.
- **PQ (Proportional/Quantitative):** Hydrogen emission spectrum (real wavelengths: 656, 486, 434 nm), energy levels (13.6 eV / n²), shell capacities (2, 8, 18 = 2n²). The chapter is rich with verifiable numbers.

---

## Figure-by-Figure

### Figure 6.1 — Hydrogen emission spectrum (visible range) *(author-placed; VALIDATE)*

**Decision:** Keep as-is. The Balmer-series visible lines (Hα 656 nm red, Hβ 486 nm cyan, Hγ 434 nm violet, Hδ 410 nm) are the empirical anchor for the entire chapter — Bohr's formula has to land these wavelengths or it is wrong. The figure proves the framework predicts what we see.

**SCOPE:**

- **Specification:** Spectrum strip diagram, horizontal, ~400–700 nm wavelength axis.
- **Content:** Four sharp vertical lines at 656, 486, 434, 410 nm. Each labeled with its Balmer-series identifier (Hα, Hβ, Hγ, Hδ) and transition (n = 3 → 2, etc.).
- **Organization:** Wavelength axis below, color-mapped continuous spectrum as background reference, sharp lines superimposed.
- **Presentation:** Background can use perceptually accurate visible-spectrum color gradient. Lines as solid vertical bars in matched colors (red, cyan, violet, deep violet). Axis labels in 10pt or larger.
- **Exclusions:** No Lyman or Paschen series (ultraviolet / infrared) — keep the figure to "what you actually see in a discharge tube." No transition diagram in this figure (that comes later if needed).

**Discipline check:** 4 components ✓. Wavelength axis is a continuous quantity, so a continuous color gradient is appropriate. Color encoding is data-driven (the wavelengths *are* those colors), not decorative.

---

### Figure 6.2 — Effective potential for the hydrogen radial problem *(author-placed; VALIDATE)*

**Decision:** Keep. The effective potential V_eff(r) = −e²/(4πε₀r) + ℏ²ℓ(ℓ+1)/(2m_e r²) deserves its own figure because the *centrifugal barrier* is exactly the kind of term that emerges from the math and would otherwise be invisible. Students should see that ℓ > 0 states have an inner wall that ℓ = 0 states do not.

**SCOPE:**

- **Specification:** Line plot, V_eff vs r, two curves overlaid.
- **Content:** ℓ = 0 curve (pure Coulomb, attractive everywhere, diverging to −∞ as r → 0). ℓ = 1 curve (Coulomb plus centrifugal — has a minimum at finite r, rises to +∞ as r → 0). Mark E₁ as a dashed horizontal at −13.6 eV.
- **Organization:** r on x-axis (in units of a₀, range 0 to ~5 a₀), V_eff on y-axis (in eV, range maybe −30 to +10). Energy levels superimposed as dashed horizontals.
- **Presentation:** Okabe-Ito sequential — ℓ = 0 in blue (#0072B2), ℓ = 1 in vermillion (#D55E00). Legend top-right. Centrifugal barrier annotated with a short arrow.
- **Exclusions:** Do not plot ℓ = 2 or higher — adds clutter without pedagogical gain at this stage. Do not plot wave functions on this figure — separate from Fig 6.3/6.4. Do not draw the curves crossing into a regime where they overlap visually (use dashing if they get close).

**Discipline check:** 2 curves + 1 reference line + axis labels = ~5 components ✓. Y-axis can go negative (potential energy) — the zero-axis rule applies to bar charts, not line plots, so this is fine. The centrifugal barrier is the punchline; annotate it explicitly.

---

### Figure 6.3 + 6.4 — Radial wave function AND radial probability density *(author-placed; RESTRUCTURE as 2-panel)*

**Decision:** Merge. The author placed these as two separate figures (Fig 6.3 R₁₀(r), Fig 6.4 P(r) = r²|R|²). Showing them separately invites students to confuse them — they are mathematically related but pedagogically distinct objects. A 2-panel figure with explicit axis annotation of the r² Jacobian factor makes the relationship visible and the orbit-dismantling argument land.

**SCOPE for combined Fig 6.3:**

- **Specification:** 2-panel line plot, side-by-side, shared x-axis.
- **Content:**
  - Panel A: R₁₀(r) = (2/a₀^{3/2})e^{−r/a₀} vs r/a₀. Monotonically decreasing.
  - Panel B: P(r) = (4/a₀³)r²e^{−2r/a₀} vs r/a₀. Peaked at r = a₀, falling on both sides.
  - Panel B annotations: vertical line at r = a₀ labeled "most probable: a₀." Vertical line at r = 3a₀/2 labeled "average: 3a₀/2." Shaded tail showing the asymmetry that pulls ⟨r⟩ > r_mp.
- **Organization:** x-axis range 0 to 5 a₀, shared. Panel A on left, Panel B on right.
- **Presentation:** Okabe-Ito — single accent color (sky blue #56B4E9) for both curves to emphasize they are the same physical state seen two ways. Vertical markers in vermillion (#D55E00) for visibility. Shaded tail in light gray.
- **Exclusions:** No 2s or 3s curves on these panels — single-state figure. No probability cloud rendering (that is Fig 6.5). The original caption of Fig 6.4 — "The orbit picture requires both markers to be at the same place. They are not." — should be the panel B caption verbatim; that sentence is doing the chapter's heaviest pedagogical work.

**Discipline check:** 2 panels × ~3 components = 6 components ✓. The r² Jacobian point — that the most-probable and average radii differ *because* the probability is a density-times-volume product — is the chapter's whole orbit-dismantling argument. The 2-panel restructure exists so students cannot leave thinking "R(r) and P(r) are the same thing."

---

### Figure 6.5 — Orbital isosurfaces (1s, 2s, 2p_z, etc.) *(author-placed; VALIDATE with constraint)*

**Decision:** Keep, but cap the orbital count at four. The author's caption suggests "1s, 2s, 2p_z, ..." which trails off. CAJAL discipline: pick four (1s spherical, 2s spherical with node, 2p_z dumbbell, 3d_{z²} dumbbell-with-torus) and stop. Showing all five 3d orbitals adds visual complexity without pedagogical gain at the textbook level.

**SCOPE:**

- **Specification:** 2×2 grid of 3D isosurface renderings, 90% probability surface.
- **Content:** Four panels — 1s, 2s, 2p_z, 3d_{z²}. Each labeled with quantum numbers (n, ℓ, m) and spectroscopic name.
- **Organization:** Top row simple (1s, 2s); bottom row directional (2p_z, 3d_{z²}). All panels same scale (use a common bounding box) so size comparison is meaningful — 2s and 2p are larger than 1s; 3d is larger still.
- **Presentation:** Single neutral color (light bluish-gray) for positive lobe, second color (light orange) for negative lobe where the wave function changes sign. Soft lighting, semi-transparent surfaces. No background gradient.
- **Exclusions:** No "electron dots" sprayed on the surface (a common textbook decoration that misleads — orbitals are not dot clouds frozen in time). No 4f orbitals. No 3d_{xy}, 3d_{xz}, 3d_{yz}, 3d_{x²−y²} crowded in — one 3d representative is enough at this stage.

**Discipline check:** 4 panels ✓. Sign-change rendering with two colors is real information (the radial node of 2s, the angular nodes of 2p and 3d). The "orbital ≠ orbit" point that the prose makes immediately after this figure depends on the figure showing *static probability surfaces*, not motion arrows.

---

### Figure 6.6 — Stern–Gerlach apparatus diagram *(author-placed; FLAG OVERLAP, then VALIDATE)*

**Decision:** Keep, but redesign to avoid duplicating Chapter 1's Stern–Gerlach treatment. Chapter 1's `01-why-quantum-mechanics-cajal.md` does not architect a Stern–Gerlach figure in detail (it focuses on the historical photoelectric, Compton, Tonomura, Franck–Hertz experiments instead). So there is no formal overlap. But Stern–Gerlach also appears in Chapter 2's `02-mathematical-foundations-cajal.md` (Fig 2.4). **Cross-reference: confirm with the chapter 2 figure to avoid two near-identical apparatus drawings**.

**SCOPE:**

- **Specification:** Schematic apparatus side-view, single panel.
- **Content:** Source on left (silver-atom oven), collimating slit, inhomogeneous magnet (poles labeled N/S with wedge-shaped gap to show field-gradient direction), detector screen on right showing two discrete spots. Beam path traced.
- **Organization:** Left-to-right flow matching the experiment's temporal order. Inset or callout showing the two spots magnified.
- **Presentation:** Single accent color (Okabe-Ito orange #E69F00) for the magnetic-field gradient indicator. Black/gray for apparatus geometry. Two spots in vermillion.
- **Exclusions:** No "expected classical smear" overlay (the contrast with classical prediction is in the text; adding it to the figure crowds it). No spin-up/spin-down vector arrows on the atoms (that visual metaphor is what the chapter spends paragraphs warning against — "spinning ball is geometrically impossible"). No quantization-of-orbital-angular-momentum framing (the chapter correctly notes Stern/Gerlach themselves got this wrong; the figure should show the experiment, not the misinterpretation).
- **Cross-check with Ch 2 Fig 2.4:** If the Ch 2 figure is the apparatus, this Ch 6 figure should be the *spin-specific* framing (silver atom, 5s electron, two spots → S_z = ±ℏ/2). Adjust labels so the two figures are clearly answering different questions: Ch 2 = "what does superposition look like?", Ch 6 = "what is spin?"

**Discipline check:** Standard schematic, ~6 components ✓. The "no spinning-ball vectors on atoms" exclusion is doctrinal — the chapter spends an entire paragraph killing the spinning-ball picture with a velocity calculation, and a figure that depicts spin as rotation would undo that work.

---

### Figure 6.7 — Hydrogen energy-level diagram with SO(4) degeneracy *(CAJAL adds; high priority)*

**Why this figure exists:** The chapter's structural punchline — "states with the same n but different ℓ have exactly the same energy; this is the SO(4) accidental degeneracy" — is a *visual* claim that the prose only states verbally. An energy-level diagram with horizontal lines at E_n = −13.6/n² eV, labeled with their (n, ℓ) content, makes the degeneracy unmistakable: 2s and 2p sit on the same line. The table at lines 158–165 in the source has placeholder cells, so the visual is doing the load-bearing work.

**SCOPE:**

- **Specification:** Energy-level diagram, vertical energy axis, horizontal lines for each level. Subshells grouped by n.
- **Content:** Four energy levels at E = −13.6, −3.4, −1.51, −0.85 eV (n = 1, 2, 3, 4). Each level subdivided horizontally into ℓ-sublevels (n=1: 1s; n=2: 2s, 2p; n=3: 3s, 3p, 3d; n=4: 4s, 4p, 4d, 4f). All sublevels of a given n drawn at exactly the same vertical height to show the degeneracy.
- **Organization:** Energy on y-axis (eV, log-scale optional to compress higher n). E = 0 ionization threshold at top, dashed. Bound states below.
- **Presentation:** Each sublevel as a short horizontal bar. Subshells of the same n in matched color (blue for n=1, vermillion for n=2, bluish-green for n=3, orange for n=4 — Okabe-Ito). Spectroscopic labels (s, p, d, f) below each bar. Degeneracy count (1, 4, 9, 16) annotated.
- **Exclusions:** No Lamb shift (the chapter mentions it as a fact-check confirmation but does not derive it). No fine structure (introduces relativistic complication outside the chapter's scope). No spin splitting (2n² doubling can be a textual annotation: "× 2 with spin"). No transition arrows between levels (Fig 6.1 already showed the consequences).

**Discipline check:** 4 levels × 4 sublevels max = ~10 visible elements, but grouped by color so visual chunking keeps it readable ✓. The degeneracy claim is what the figure exists to make visible — students should be able to look at the n=2 line and see two bars at the same height labeled 2s and 2p.

---

## What CAJAL Declines to Architect

- **Quantum number table as a figure.** The author placed a table at lines 158–165 with placeholder rows. Keep this as a *table* once filled in — quantum numbers × spectroscopic labels × counts × running totals is exactly the tabular form. A figure would not improve on it.
- **SO(4) symmetry group diagram.** Tempting (a 4D rotation group hidden inside a 3D problem), but representing SO(4) visually requires either abstract group-theory diagrams (too advanced for this chapter) or the classical Laplace–Runge–Lenz vector picture (which would need its own elliptical-orbit context). Skip; the prose carries the argument and the energy-level diagram (Fig 6.7) shows the *consequence* of the symmetry.
- **Pauli exclusion / periodic table figure.** The text walks through 2, 8, 18 shell capacities cleanly. A periodic-table-coloring figure here would over-extend a chapter that is fundamentally about one-electron hydrogen. Save for Chapter 8 (identical particles) where it belongs.
- **Electron-spinning-ball-velocity calculation as a figure.** Pure algebra; no visual gain.

---

## Video Candidate Pass

Reviewing all six figures against the four criteria:

- **Fig 6.1 (emission spectrum):** Static. Not a candidate.
- **Fig 6.2 (effective potential):** Could be sweepable — animate ℓ from 0 to 3 and watch the centrifugal barrier grow. Mild candidate, but the static two-curve figure already makes the point.
- **Fig 6.3/6.4 (radial wave function + probability density):** Static.
- **Fig 6.5 (orbital isosurfaces):** **Strong video candidate.** Rotating the 3D isosurfaces would make the angular structure (nodes of 2p, lobes of 3d) genuinely clearer than static 2D projections can. This is the canonical "rotating orbital" video that almost every QM course produces — and it earns its place because 3D shape *is* the content. Sub-observation criterion: human-eye 2D projection loses the angular structure; rotation recovers it.
- **Fig 6.6 (Stern–Gerlach):** Possible candidate — animate the beam exiting the magnet and the spots accumulating. But the sequential-measurement Stern–Gerlach video belongs more naturally in Chapter 5's measurement-process discussion (Exercise A3), not here.
- **Fig 6.7 (energy levels):** Static.

**Recommendation: one video — rotating orbital isosurfaces (Fig 6.5).** 15-second clip per orbital, ideally an interactive selector. This is high-leverage because the orbital shapes are *the* visualizable content of hydrogen's solution, and they are genuinely poorly served by static 2D images.

---

## Summary

6 figures: 5 author-placed (one restructured as 2-panel) + 1 CAJAL-added (energy-level diagram with degeneracy). One video candidate (rotating orbital isosurfaces). Key cross-reference: confirm with Chapter 2 Fig 2.4 that the Stern–Gerlach treatments do not duplicate — frame Ch 6's as spin-specific (5s electron, S_z = ±ℏ/2). Key restructure: merge author's Fig 6.3 (radial wave function) and Fig 6.4 (radial probability density) into a single 2-panel so the r² Jacobian's role in the most-probable-vs-average distinction is visible.
