# CAJAL Figure Intelligence — Chapter 8: Identical Particles

**Source:** `chapters/08-identical-particles.md`
**Mode:** `/scan silent`
**Domain note:** Content-rich chapter with strong author-placed figure choices — the author already identified the high-leverage visualizable moments (exchange correlation in 2D position-pair space, helium singlet/triplet splitting, Madelung filling, Fermi-Dirac vs Bose-Einstein distributions). CAJAL's job here is mostly validation and discipline, with one likely drop (Slater determinant as figure = typeset math anti-pattern).

---

## Density Recommendation

**4 figures, Mechanistic density.** The chapter's argument hinges on three visual claims that prose alone cannot deliver: the exchange correlation alters joint probability density without any interaction (Fig 8.2), the symmetry of the spatial wave function shifts measured energies by ~0.8 eV in helium (Fig 8.3), and the sign in the denominator of the occupation distribution produces two different universes at low temperature (Fig 8.5). Add Madelung filling (Fig 8.4) as the organizing visual for the periodic table discussion. Drop Fig 8.1 (Slater determinant rendered as a figure) — it's typeset math reproduced in figure form, which is the CAJAL anti-pattern.

Final count: **4 figures** — 4 validated author-placed + 1 dropped + 0 CAJAL-added.

---

## Zone Map

- **MC (Mechanism Complexity):** Exchange correlation is genuinely complex mechanism — symmetry of the spatial wave function determines how often two electrons sit near each other, which determines the Coulomb energy. The mechanism is *causally chained* and a single figure (Fig 8.2) breaks it open.
- **VG (Verification Gap):** The 0.8 eV singlet-triplet splitting in helium is a measurable consequence. Without an energy-level diagram showing parahelium above orthohelium by 2K, the calculation lands as algebra without an empirical anchor.
- **PQ (Proportional/Quantitative):** Three quantitative payoffs — the J ± K splitting (0.8 eV in helium), the FD/BE/MB distribution functions at varying T/μ, and the Madelung filling order (1s → 2s → 2p → 3s → ...). Each warrants its own figure.

---

## Figure-by-Figure

### Figure 8.1 — N=3 Slater determinant *(author-placed; DROP)*

**Decision:** Drop. The Slater determinant is rendered in full typesetting at line 57 of the source. A figure that re-renders the determinant adds no information; it is typeset math reproduced as a graphic. CAJAL anti-pattern: figures that exist to redisplay equations the prose has already typeset.

**Alternative considered and rejected:** A "matrix anatomy" diagram showing the two key properties (swap two columns → minus sign; two identical rows → zero) could be pedagogically valuable. But the chapter already states these properties cleanly in prose at lines 64–66 ("Swap two particle labels...that is what determinants do"; "if two of the spin-orbitals are identical...the determinant is zero"). The properties are short enough to read; a figure would not improve them.

**Recommendation:** Strike Fig 8.1 reference. If a visual is desired here, replace with a 2-row, 2-column matrix illustration of the N=2 case showing column-swap producing the minus sign — but only if the author wants a visual anchor for students who do not know determinant algebra. Otherwise the inline math at line 70 is sufficient.

---

### Figure 8.2 — Joint probability density: distinguishable, fermion, boson *(author-placed; VALIDATE)*

**Decision:** Keep. This is the chapter's single highest-leverage figure. The exchange correlation is the chapter's central conceptual move — the claim that wave-function symmetry alone (no interaction term in the Hamiltonian) changes how close two particles sit to each other. A side-by-side comparison of |ψ(x₁, x₂)|² for three cases makes the claim visible in a way no equation can.

**SCOPE:**

- **Specification:** 3-panel 2D heatmap, side by side.
- **Content:**
  - Panel A: Distinguishable particles — |ψ₁(x₁)ψ₂(x₂)|², a uniform-looking product distribution.
  - Panel B: Fermions (antisymmetric spatial) — |ψ_A(x₁, x₂)|² with a clear *exchange hole* (vanishing density along the diagonal x₁ = x₂).
  - Panel C: Bosons (symmetric spatial) — |ψ_S(x₁, x₂)|² with *enhanced density* along the diagonal.
- **Organization:** Three panels, identical axes (x₁ horizontal, x₂ vertical, both in units of L). Common colorscale so the panels are quantitatively comparable. Diagonal x₁ = x₂ drawn as a dashed line in each panel.
- **Presentation:** Single sequential colormap (Okabe-Ito sky blue → dark blue) for density magnitude. All panels share the same colorbar.
- **Exclusions:** Do not use diverging colormaps (red-blue) for density — density is a non-negative quantity, sequential is correct. Do not annotate "exchange force" anywhere (the chapter explicitly notes "there is no exchange force; there is only the Coulomb force and the antisymmetry constraint"). Caption should make explicit: same Hamiltonian (no interaction), three different wave-function symmetries, three different distributions.

**Discipline check:** 3 panels × 1 main element each + diagonal reference = 4 visible elements per panel, well under 6–8 ceiling ✓. The exchange hole on the diagonal is the visual signature that lands the entire chapter's argument — the figure must show it cleanly without colormap distortion.

---

### Figure 8.3 — Helium energy level diagram: parahelium vs orthohelium *(author-placed; VALIDATE)*

**Decision:** Keep. The 1s2s configuration splits into parahelium (J + K) and orthohelium (J − K) by ~0.8 eV — measured, predicted, agreement. The figure is the chapter's empirical anchor.

**SCOPE:**

- **Specification:** Energy-level diagram, vertical energy axis, configuration label on x-axis or as column headers.
- **Content:** Three columns — (1) unperturbed 1s2s level at E₀ (single line), (2) +J shift (single line displaced up), (3) ±K splitting (two lines: parahelium at E₀+J+K labeled S=0, orthohelium at E₀+J−K labeled S=1). Right side shows experimental values from NIST: orthohelium at −59.2 eV, parahelium at −58.4 eV, splitting 0.8 eV labeled as "2K."
- **Organization:** Left-to-right progression mirrors the perturbation calculation. Energy gap annotations between levels.
- **Presentation:** Okabe-Ito bluish-green for parahelium (singlet), vermillion for orthohelium (triplet). Reference line at unperturbed E₀ in gray.
- **Exclusions:** Do not include other helium configurations (1s², 1s2p, etc.) — focus on the 1s2s splitting that the calculation addresses. Do not draw transition arrows (this is about energies, not spectroscopy). Do not depict the spin orientations as little arrows on the energy levels (chapter has spent considerable effort arguing spin should not be drawn as classical rotation).

**Discipline check:** 3 columns × 2 levels max + experimental annotations = ~6 visible elements ✓. The "orthohelium is lower" punchline must be unmistakable — that's the experimentally surprising result that exchange physics explains.

---

### Figure 8.4 — Madelung diagonal-filling diagram *(author-placed; VALIDATE with constraint)*

**Decision:** Keep, with discipline. The Madelung rule has a standard textbook diagonal-filling visualization — orbitals arranged in a grid (n rows, ℓ columns), with arrows tracing the (n+ℓ) filling order. Useful and well-established. Discipline constraint: keep to orbitals actually populated in the first ~5 rows of the periodic table; do not extend into territory where Madelung exceptions dominate.

**SCOPE:**

- **Specification:** 2D grid diagram, rows = n (1 through 6 or 7), columns = ℓ (s, p, d, f), diagonal sweep arrows.
- **Content:** Each cell is an orbital labeled "ns", "np", etc. Diagonal arrows (top-right to bottom-left in standard convention) trace the filling order: 1s → 2s → 2p, 3s → 3p, 4s → 3d, 4p → 5s, 4d → 5p → 6s → 4f → 5d → 6p → 7s, ...
- **Organization:** Grid layout, n increasing down, ℓ increasing right. Arrows overlaid in distinct color so they don't compete with cell labels.
- **Presentation:** Cell labels in black on white. Arrows in Okabe-Ito orange (#E69F00). Cells beyond practical filling (e.g., 8s, 6f if extending too far) faded or omitted.
- **Exclusions:** Do not label the exceptions in the figure itself (chromium, copper, etc.) — those go in the caption or accompanying text. Do not draw transition-metal subshells with electrons-as-dots (different figure type, would crowd this one).

**Discipline check:** ~16–20 cells + ~10 arrows = ~30 elements. This is at the edge of the component ceiling, but the grid structure provides visual chunking — cells are not all independent components, they form a regular array. Discipline holds as long as the grid stays uncluttered.

---

### Figure 8.5 — Fermi-Dirac vs Bose-Einstein vs Maxwell-Boltzmann *(author-placed; VALIDATE)*

**Decision:** Keep. The chapter's headline summary — "one sign difference in the denominator. Two different universes at low temperature" — must be a figure. Three distribution functions plotted on shared axes makes the convergence at high T and the divergence at low T visible at a glance.

**SCOPE:**

- **Specification:** Line plot, three curves, shared axes.
- **Content:** x-axis = (E − μ)/k_BT, range maybe −4 to +4. y-axis = ⟨n⟩, range 0 to 3 (boson curve goes above 1, fermion clamped at 1, classical asymptotes both). Three curves: FD (1/(e^x + 1)), BE (1/(e^x − 1)), MB (e^(−x)).
- **Organization:** Vertical line at x = 0 (E = μ) as reference. Asymptote callouts: "FD: max occupation 1 (Pauli)", "BE: diverges as E → μ (condensation)", "MB: classical limit, both quantum cases converge to this at high T."
- **Presentation:** Okabe-Ito — vermillion for FD, bluish-green for BE, gray for MB. The chapter's phrase "one sign difference" should appear in the caption, not the figure body.
- **Exclusions:** Do not plot specific temperatures (the dimensionless x-axis makes the plot universal). Do not annotate "Fermi energy" or "BEC critical temperature" — those are chapter 9/10 material if at all.

**Discipline check:** 3 curves + 1 reference line + 3 callouts = 7 elements ✓. The BE divergence as x → 0 is the dramatic feature; the figure must let that divergence be visible without crowding it out.

---

## What CAJAL Declines to Architect

- **Singlet/triplet spin-spatial pairing diagram.** The chapter's table at lines 38–46 carries the spin/statistics dichotomy in tabular form. The detailed singlet/triplet enumeration at line 105 is mathematical and reads cleanly. A figure here would compete with the helium energy level diagram (Fig 8.3) which already shows the pairing's *consequence*.
- **Carbon ground-state Hund's-rule derivation as figure.** The chapter walks through the carbon ²P₀ derivation in prose at lines 160–162. The first-row term symbols at line 162 are a list, not a figure. A flowchart of Hund's rules would be borderline; the prose is sufficient.
- **Chandrasekhar limit / white dwarf figure.** Tempting (degeneracy pressure as visualizable phenomenon at astrophysical scale), but it would over-extend a chapter that is fundamentally about atomic-scale identical particles. Save for an astrophysics excursion if one is planned.
- **Anyons / fractional statistics diagram.** Mentioned in the chapter as a structural sidebar at line 49. The topology of 2D particle exchange is genuinely figure-worthy but the chapter does not dwell on it; a figure here would crowd a brief reference.

---

## Video Candidate Pass

Reviewing all four kept figures against the four criteria:

- **Fig 8.2 (exchange correlation panels):** Sub-observation criterion met — the exchange hole forms because of antisymmetry, not because of any temporal process. Static comparison is the right form. Not a video candidate.
- **Fig 8.3 (helium levels):** Static energy diagram. Not a candidate.
- **Fig 8.4 (Madelung):** Could be animated to trace the filling sequence orbital by orbital. Mild candidate — pedagogically helpful but the static diagonal-arrow version carries the same information.
- **Fig 8.5 (FD/BE/MB):** **Mild video candidate.** Animating the temperature parameter — sweeping from high T (all three converge to MB) down to low T (FD plateaus, BE diverges) — would dramatize the "one sign difference, two different universes" point. Worth considering if a video budget exists.

**Recommendation: no required videos.** Fig 8.5 temperature sweep is a worthwhile bonus if production capacity allows, but the static figures carry the chapter's arguments effectively.

---

## Summary

4 figures: 4 validated author-placed + 1 dropped (Slater determinant = typeset math). No CAJAL-added figures — the author identified the high-leverage moments correctly. The dropped Slater determinant should either be removed entirely or replaced with a tiny matrix-anatomy schematic for N=2 if the author wants a visual anchor; the inline math at line 70 is otherwise sufficient. One borderline video candidate (Fig 8.5 temperature sweep) for capacity-permitting bonus content.
