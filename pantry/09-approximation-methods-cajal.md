# CAJAL Figure Intelligence — Chapter 9: Approximation Methods

**Source:** `chapters/09-approximation-methods.md`
**Mode:** `/scan silent`
**Domain note:** Five-tools survey chapter — perturbation theory (non-degenerate and degenerate), variational principle, WKB, Fermi's golden rule. The author has placed four figures, one per major tool except WKB. The chapter's organizing claim ("five methods, five jobs") is best served by figures that show each method *in action* on a canonical example, not by abstract method-comparison diagrams. CAJAL adds one figure for WKB to balance the tool coverage.

---

## Density Recommendation

**5 figures, Mechanistic density.** Each of the five methods deserves one visualizable anchor. The author placed four; WKB is conspicuously unfigured despite getting its own section. CAJAL adds a WKB wave-function visualization (oscillation in classically allowed regions, exponential decay in forbidden regions, matching at turning points) to round out the coverage.

Final count: **5 figures** — 4 validated author-placed + 1 CAJAL-added (WKB wave function).

---

## Zone Map

- **MC (Mechanism Complexity):** Each method has a non-trivial mechanism the prose unpacks. Level repulsion (mixing under perturbation), variational minimization (parameter sweep finding the minimum), Stark splitting (degeneracy-breaking through diagonalization), sinc²-to-delta (long-time limit of the transition amplitude), WKB matching (semi-classical wave function across turning points). Each warrants its own figure.
- **VG (Verification Gap):** The variational helium calculation gives −77.5 eV vs experiment's −79.0 eV. Showing the ⟨H⟩(Z*) curve with the minimum marked anchors "the calculation works" empirically.
- **PQ (Proportional/Quantitative):** Hydrogen Stark splitting (±3eEa₀), variational helium (−2.848 Hartree), sinc² peak height (∝ t²), sinc² peak width (∝ 1/t). All quantitatively visualizable.

---

## Figure-by-Figure

### Figure 9.1 — Level repulsion under perturbation *(author-placed; VALIDATE)*

**Decision:** Keep. The second-order energy correction's sign structure — ground state always pushed down, near-degenerate levels pushed apart — is the chapter's first big structural insight, and an avoided-crossing diagram is the canonical visualization.

**SCOPE:**

- **Specification:** Line plot, energy vs perturbation strength λ. Two energy levels.
- **Content:** Two unperturbed levels (dashed lines) that would cross at some λ_c if they didn't interact. The actual eigenvalues (solid curves) bend away from each other near λ_c, never crossing. Annotation: "level repulsion" with arrows showing the upper level pushed up and the lower level pushed down. Gap between solid curves at λ_c labeled as 2|⟨a|H'|b⟩| (twice the off-diagonal matrix element).
- **Organization:** λ on x-axis, E on y-axis. Both curves and the dashed crossing-without-interaction reference shown.
- **Presentation:** Okabe-Ito — solid curves in vermillion (#D55E00, upper) and blue (#0072B2, lower). Dashed reference lines in gray. Annotation arrows in orange (#E69F00).
- **Exclusions:** Do not extend to more than 2 levels (multi-level avoided crossings get visually messy). Do not annotate with specific physical systems — this is the structural phenomenon, not a particular example. Do not draw eigenstate composition arrows (the figure is about energies, not states).

**Discipline check:** 2 solid curves + 2 dashed reference lines + gap annotation + 2 push arrows = ~7 elements ✓.

---

### Figure 9.2 — Hydrogen n=2 linear Stark effect *(author-placed; VALIDATE)*

**Decision:** Keep. The n=2 splitting is the cleanest worked example of degenerate perturbation theory in the chapter, and the figure should show the four-fold degeneracy breaking into three levels (two outer, one doubly-degenerate inner).

**SCOPE:**

- **Specification:** Energy-level diagram, two columns — "ℰ = 0" (single fourfold-degenerate level) and "ℰ ≠ 0" (three levels: +3eℰa₀, 0 with degeneracy 2, −3eℰa₀).
- **Content:** Left column: single line labeled "n=2 (4-fold degenerate)." Right column: three lines with their energies and state labels — top line at +3eℰa₀ labeled (|2s⟩ − |2p_z⟩)/√2; middle line at 0 with degeneracy 2, labeled |2p_x⟩, |2p_y⟩; bottom line at −3eℰa₀ labeled (|2s⟩ + |2p_z⟩)/√2. Connecting lines from left to right show which states evolved into which.
- **Organization:** Energy on y-axis, ℰ-state on x-axis (categorical: 0 vs ≠ 0). Connecting lines diagonal.
- **Presentation:** Okabe-Ito — left-side level in neutral gray; right-side levels in vermillion (top), blue (middle), bluish-green (bottom). Connecting lines in matched colors.
- **Exclusions:** Do not show second-order corrections (those are not linear in ℰ; this figure is the linear Stark effect). Do not include other principal quantum numbers (n=1 is unshifted, n=3 is more complex; stay focused).

**Discipline check:** 4 levels + connecting lines + state labels = ~7 elements ✓. The state-mixing labels at top and bottom are essential — they make the "good zeroth-order states are linear combinations" point visible.

---

### Figure 9.3 — Variational helium ⟨H⟩(Z*) vs Z* *(author-placed; VALIDATE)*

**Decision:** Keep. The variational principle in action — sweep over the trial parameter, find the minimum, read off the energy estimate. The figure makes the abstract minimization concrete.

**SCOPE:**

- **Specification:** Line plot, ⟨H⟩(Z*) on y-axis (in Hartrees or eV), Z* on x-axis (range maybe 1.0 to 2.5).
- **Content:** Parabolic-shaped curve representing ⟨H⟩(Z*) = (Z*)² − 4Z* + (5/8)Z*. Minimum marked at Z* = 27/16 ≈ 1.69 with horizontal/vertical reference lines. Annotation: "E_var = −2.848 Hartree ≈ −77.5 eV." Reference line at the experimental value −79.0 eV showing the 1.5 eV gap. Annotation at Z* = 2 (bare nuclear charge) showing where naive unscreened calculation would land (higher energy than the minimum).
- **Organization:** x-axis Z* from 1.0 to 2.5. y-axis energy in eV from about −80 to −60.
- **Presentation:** Curve in Okabe-Ito blue (#0072B2). Minimum marker as a vermillion dot. Experimental reference line in dashed bluish-green. Annotations as text callouts.
- **Exclusions:** Do not include the kinetic-only and Coulomb-only pieces separately (chapter walks through them in prose; figure should show the combined ⟨H⟩). Do not include multi-parameter variational calculations (the chapter's whole point is that one parameter gets you to within 2%).

**Discipline check:** 1 curve + 1 minimum + 2 reference lines + ~3 annotations = ~7 elements ✓. The two "wins" the figure must convey: (1) there is a minimum, and (2) the minimum is close to but above the experimental value (variational bound).

---

### Figure 9.4 — Sinc² convergence to delta function *(author-placed; VALIDATE)*

**Decision:** Keep. Fermi's golden rule rests on the long-time limit of sin²(Ωt/2)/Ω². Showing three values of t (small, medium, large) overlaid makes the convergence visible — and visible convergence to a delta function is what justifies treating the formula as a transition rate rather than an oscillatory amplitude.

**SCOPE:**

- **Specification:** Line plot, sin²(Ωt/2)/Ω² on y-axis, Ω on x-axis (with Ω = 0 centered).
- **Content:** Three curves overlaid, for three increasing values of t (e.g., t₁, t₂ = 2t₁, t₃ = 4t₁). Each curve peaked at Ω = 0 with peak height proportional to t² and width proportional to 1/t. Area under each curve approximately constant (proportional to t · const, integrating to π t/2 in the limit). Annotations: "peak height ∝ t²," "peak width ∝ 1/t," "area ∝ t → delta function as t → ∞."
- **Organization:** Ω from about −5/t₁ to +5/t₁ on x-axis, dimensionless. y-axis shows the absolute value (sin²/Ω² is non-negative).
- **Presentation:** Okabe-Ito sequential — sky blue (#56B4E9) for small t, bluish-green for medium, vermillion for large t. Legend distinguishing the three values.
- **Exclusions:** Do not show t = ∞ as a literal delta function spike (that's the limit, not a plottable curve). Do not show the sub-peaks far from Ω = 0 in extreme detail — they decay as 1/Ω² and are not the figure's point.

**Discipline check:** 3 curves + 3 annotations = 6 elements ✓. The visual story — narrow-and-tall vs broad-and-short — is what makes the long-time limit intuitive.

---

### Figure 9.5 — WKB wave function across a turning point *(CAJAL adds)*

**Why this figure exists:** The chapter's WKB section makes the semi-classical claim that wave functions oscillate in classically allowed regions, decay exponentially in forbidden regions, and match across turning points via Airy functions. Without a figure showing this structure, students treat WKB as a transmission-probability formula rather than as a *wave-function approximation* with a specific shape. The Maslov index (+1/2 in the Bohr-Sommerfeld formula) only makes sense once you see why two matchings are needed.

**SCOPE:**

- **Specification:** 2-panel figure, top panel = potential V(x) with bound-state energy E marked, bottom panel = WKB wave function ψ(x) plotted on shared x-axis.
- **Content:**
  - Top: Smooth potential well V(x) (could be a parabola or asymmetric shape). Horizontal dashed line at energy E. Classical turning points x_a and x_b marked where V(x_a) = V(x_b) = E.
  - Bottom: ψ(x) curve. For x < x_a (classically forbidden), exponential decay. For x_a < x < x_b (classically allowed), oscillation with local wavelength λ(x) = h/p(x) = h/√(2m(E−V(x))) — wavelength compresses where V is low (high p), stretches where V is closer to E (low p). For x > x_b (classically forbidden), exponential decay. Matching annotations at x_a and x_b indicating "Airy function patch" with small connecting curves.
- **Organization:** Shared x-axis. Energy and wave-function panels stacked.
- **Presentation:** Top panel — potential in dark gray, energy line in dashed orange. Bottom panel — oscillating region in blue, exponentially decaying tails in lighter blue, matching regions highlighted with vermillion brackets.
- **Exclusions:** Do not plot the exact Airy function shape at the matchings (the figure should show that matching *happens*, not the explicit Ai/Bi functions — those would over-extend the figure's scope). Do not draw the WKB amplitude factor 1/√p(x) as a separate curve overlay (mention in caption that amplitude varies inversely with sqrt(local momentum)).

**Discipline check:** 2 panels × ~4 elements each = 8 elements ✓. The two punchlines the figure must land: (1) wavelength varies with local momentum, (2) two turning points means two Airy patches, hence the Maslov +1/2.

---

## What CAJAL Declines to Architect

- **Method-selection flowchart.** The chapter's table at lines 217–219 (placeholder) is the right form for "five methods, five jobs." A flowchart would be more visually elaborate without adding information beyond what a table does cleanly.
- **Perturbation series convergence diagrams.** The asymptotic-series-with-zero-radius discussion at line 62 and line 224–233 is conceptually important but not visualizable in a way that improves on the prose. A toy plot showing "first few terms accurate, then diverging" could work but adds little.
- **Alpha-decay tunneling figure.** Already done in Chapter 4 (Fig 4.5 alpha-decay potential, Fig 4.6 Geiger-Nuttall plot). Cross-reference to Ch 4; do not duplicate.
- **Hartree-Fock / DFT lineage diagram.** Mentioned in passing at line 74 and line 209 as descendants of variational principle. A genealogy diagram would over-extend a chapter that is focused on the five core methods, not on their computational descendants.

---

## Video Candidate Pass

Reviewing all five figures against the four criteria:

- **Fig 9.1 (level repulsion):** **Mild video candidate.** Sweep λ from 0 to large value and watch the two solid curves bend away from the crossing. Transition mechanism criterion met. The animation makes "as the perturbation grows, the levels avoid each other" visceral.
- **Fig 9.2 (Stark splitting):** Static categorical diagram. Could animate the splitting as ℰ increases from 0, but the static comparison is already clear.
- **Fig 9.3 (variational curve):** Static. Animating Z* sliding to find the minimum is mildly helpful but the marked-minimum static plot carries the same content.
- **Fig 9.4 (sinc² convergence):** **Strong video candidate.** Continuously increase t and watch the sinc² peak narrow and grow taller while area stays constant — this is the visual definition of weak convergence to a delta function. The sub-observation criterion is met (the limit is what is being approached, and the approach itself is the content).
- **Fig 9.5 (WKB wave function):** Static. Could animate as energy E sweeps upward through the potential well (turning points move outward, wavelengths shift), but probably not high enough leverage to justify.

**Recommendation: one video — sinc² convergence (Fig 9.4).** This is the only figure where the temporal limit *is* the pedagogical point. Animated convergence to a delta function is canonical Fermi's-golden-rule pedagogy and worth the production cost.

---

## Summary

5 figures: 4 validated author-placed (level repulsion, Stark splitting, variational helium, sinc² convergence) + 1 CAJAL-added (WKB wave function across turning points). One video candidate (sinc² convergence to delta). The WKB addition exists because the chapter's section gets prose but no visual; without a figure, WKB reads as a tunneling formula rather than as a semi-classical wave-function method.
