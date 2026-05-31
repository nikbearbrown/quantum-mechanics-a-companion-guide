# CAJAL Figure Intelligence — Chapter 7: Angular Momentum

**Source:** `chapters/07-angular-momentum.md`
**Mode:** `/scan silent`
**Domain note:** Algebra-heavy chapter — the chapter's pedagogical promise is "pure algebra, no spatial integration, no differential equations." That makes most visualizations a tradeoff between honoring the algebraic spirit and giving students something to anchor to. Three author-placed figures (ladder, spherical harmonics, singlet measurement) are well-chosen. The 720° rotation and the WCOE neutron-interferometer experiment are CAJAL-add candidates because they are the chapter's most concrete claims about the world and the prose alone leaves them abstract.

---

## Density Recommendation

**5 figures, Mixed density.** The chapter is fundamentally algebraic, but it makes three claims that *must* be made visible to land: the bounded ladder structure (Fig 7.1), the angular shapes of the spherical harmonics (Fig 7.2), and the singlet's perfect anti-correlation (Fig 7.3). CAJAL adds two more — the 720° rotation result (Fig 7.4) because it is the chapter's most physical claim and the prose makes the reader work uphill to picture it, and the WCOE 1975 neutron-interferometer experiment (Fig 7.5) because the chapter cites a specific measurement and citing an experiment without showing it leaves the verification implicit.

Final count: **5 figures** — 3 author-placed + 2 CAJAL-added.

---

## Zone Map

- **MC (Mechanism Complexity):** The ladder-operator derivation is the entire chapter — but the derivation is the math, not a figure. The bounded ladder *output* of that derivation (m running from −ℓ to +ℓ in unit steps with the (ℓ+1) gap on top) is what should be figured.
- **VG (Verification Gap):** The 720° rotation claim is verified experimentally but described only in prose. Without a figure showing what acquires the minus sign and what stays unchanged, students keep the half-angle factor as a typesetting artifact rather than as a measured fact.
- **PQ (Proportional/Quantitative):** Spin probabilities (1/2 each for ±ℏ/2), singlet correlations (perfect anti-correlation along any axis), interference phase shift (π for 360° rotation of one neutron beam). The phase shift is the most quantitatively dramatic — π radians is the maximum possible shift.

---

## Figure-by-Figure

### Figure 7.1 — Ladder diagram for angular momentum spectrum *(author-placed; VALIDATE)*

**Decision:** Keep. The ladder is the chapter's single most important visual — it concretizes the derivation's output: a discrete spectrum of m-values running from −ℓ to +ℓ in unit steps, with raising/lowering operators climbing or descending one rung at a time.

**SCOPE:**

- **Specification:** Ladder diagram, vertical, three ladders shown side by side for representative ℓ values.
- **Content:** Three columns — ℓ = 0 (single rung at m = 0), ℓ = 1 (three rungs at m = −1, 0, +1), ℓ = 2 (five rungs at m = −2, −1, 0, +1, +2). Curved arrows on the side showing L₊ (raising) and L₋ (lowering) connecting adjacent rungs. Top rung of each ladder labeled "L₊ |ℓ, ℓ⟩ = 0"; bottom rung labeled "L₋ |ℓ, −ℓ⟩ = 0."
- **Organization:** Columns side-by-side, equal vertical scale so the rungs at common m-values align across columns. m-value labels on the right side; ℓ label at the top of each column.
- **Presentation:** Okabe-Ito blue (#0072B2) for rungs, vermillion (#D55E00) for L₊ arrows, sky blue (#56B4E9) for L₋ arrows. No red-green pairing.
- **Exclusions:** No spin ladders mixed in (separate from orbital algebra at this stage). No spherical harmonic plots (those are Fig 7.2). No half-integer ladders (the half-integer ladders are spin and belong with the Pauli matrix discussion, possibly as a separate small inset).

**Discipline check:** 3 columns × 5 rungs max + 2 arrow types = ~7 visible elements ✓. The ladder structure is exactly what the algebra produces; a figure that adds anything else dilutes the punchline.

---

### Figure 7.2 — Angular shapes of |Y_{ℓm}(θ,φ)|² *(author-placed; VALIDATE with constraint)*

**Decision:** Keep, with two constraints. (1) Show only ℓ = 0 and ℓ = 1 (one s and three p shapes — four panels total). The author's caption trails off ("...for ℓ = 0, 1, ..."); cap there. ℓ = 2 (the d shapes) adds visual complexity without algebraic gain. (2) Cross-reference with Chapter 6 Fig 6.5: those were full 3D orbital isosurfaces (radial × angular); these are *angular only*. Make the distinction explicit in the caption.

**SCOPE:**

- **Specification:** 2×2 grid of polar/spherical-coordinate plots of |Y_{ℓm}|².
- **Content:** Four panels — Y_{0,0} (uniform sphere), Y_{1,0} (dumbbell along z-axis), Y_{1,+1} and Y_{1,−1} (donut shapes around z-axis, indistinguishable in |Y|² since both go as sin²θ). Possibly a fifth row showing the real-basis p_x, p_y, p_z constructed as superpositions, since the chapter discusses this explicitly at line 126–130.
- **Organization:** Each panel is a 3D rendering with z-axis labeled (since m is defined as the L_z eigenvalue, the z-axis is the special direction). Color encodes |Y|² magnitude.
- **Presentation:** Sequential single-color gradient (Okabe-Ito sky blue → dark blue) for magnitude. Background neutral. z-axis drawn explicitly in each panel.
- **Exclusions:** Do NOT show Re(Y_{ℓm}) or Im(Y_{ℓm}) as separate plots — the chapter is plotting probability density |Y|², not the complex amplitude. Do not blur the distinction between complex Y_{1,±1} and real p_x, p_y; if the real combinations are shown, label them clearly as "real basis (chemists)" vs "L_z eigenstate basis (physicists)."

**Discipline check:** 4 panels (or 5–6 with real-basis row) ✓. Cross-reference with Ch 6 Fig 6.5 is a maintenance note for the visual asset library — these two figures should look visually *different* (Ch 6 = full 3D probability cloud with radial extent; Ch 7 = angular shape on unit sphere).

---

### Figure 7.3 — Two-particle singlet measurement schematic *(author-placed; VALIDATE)*

**Decision:** Keep. This is the EPR-Bell setup in embryonic form — two spin-1/2 particles in the singlet state, separated, each measured on chosen axes. Chapter 7 builds the state; Chapter 10 does the Bell calculation; this figure is the visual bridge.

**SCOPE:**

- **Specification:** Schematic, single-panel, left-right symmetric.
- **Content:** Source in the center labeled |0,0⟩. Two particles emerging in opposite directions (left and right) along an axis. Each particle ends at a Stern–Gerlach-style detector with an orientation arrow (the choice of measurement axis). Detector outcomes shown as ±ℏ/2 spots. Inset table or annotation: "When both axes are aligned: outcomes always opposite. When axes are at angle θ: cos²(θ/2) probability of opposite outcomes." (The full Bell calculation is Ch 10's job; this figure should hint that the angle dependence is the interesting structure.)
- **Organization:** Source center, particles flying outward, detectors at the edges. Time/distance is implicit (the source is at t = 0, detection later).
- **Presentation:** Okabe-Ito — particles in matched neutral color (gray), the singlet state labeled with the explicit ket |0,0⟩ = (|↑↓⟩ − |↓↑⟩)/√2 below the source. Detector axes in vermillion and bluish-green for the two sides.
- **Exclusions:** Do not depict "hidden variables traveling with the particles" (the chapter explicitly notes this is the EPR question, not the QM answer). Do not draw Bell-inequality plots here (Ch 10). Do not annotate "spooky action at a distance" or similar editorial framing.

**Discipline check:** ~6 components ✓. The figure earns its place by making the two-particle structure visible — students who only see the algebra often miss that the two measurements are *spatially separated*.

---

### Figure 7.4 — The 720° rotation: spinor under SU(2) *(CAJAL adds; high priority)*

**Why this figure exists:** The chapter's most counterintuitive physical claim — that a 360° rotation sends a spin-1/2 state to its negative, with the original state recovered only after 720° — is verified by experiment (WCOE 1975, Rauch et al. 1975) and is structurally important (it's why SU(2) is the spin group, not SO(3)). The prose at line 167–183 makes the algebraic argument but the geometric picture is left to the reader's imagination. A figure earns its place here because the half-angle factor is otherwise easy to dismiss as a typesetting curiosity.

**SCOPE:**

- **Specification:** Two-panel comparison — vector under SO(3) rotation vs spinor under SU(2) rotation.
- **Content:**
  - Panel A (classical vector): A vector arrow drawn at four positions around a circle — 0°, 90°, 180°, 270° — with the vector at 360° identical to the starting vector. Caption: "SO(3): 360° returns to identity."
  - Panel B (spin-1/2 spinor): Same circular path, but the "spinor" represented by an arrow with a *phase color* (or a small flag/marker attached) that shifts from blue at 0° through purple at 360° (showing the −1 phase) and back to blue at 720°. Caption: "SU(2): 360° gives −|ψ⟩; 720° returns to identity."
- **Organization:** Side-by-side panels, same circular path layout.
- **Presentation:** Panel A in Okabe-Ito blue (#0072B2). Panel B uses a perceptually sequential colormap (Okabe-Ito blue → bluish-green → orange → vermillion) cycled across 0°–720° to make the doubling visible. Phase indicated by color, not by an extra dimension.
- **Exclusions:** No Möbius strip illustration (visually evocative but mathematically suggests something different from what spinors do). No "belt trick" / Dirac scissors animation in a static figure (that's a video idea, not a still). No SU(2) matrix algebra in the figure itself (the math is in the prose).

**Discipline check:** 2 panels × 4 angle positions = 8 visible elements ✓. The color-as-phase encoding is the discipline-critical choice — it makes the doubling visible without requiring 4D geometry.

---

### Figure 7.5 — WCOE 1975 neutron interferometer: 360° rotation produces measurable phase shift *(CAJAL adds)*

**Why this figure exists:** The chapter cites a specific 1975 experiment (Werner, Colella, Overhauser, Eagen) that confirmed the 720° behavior with neutrons. Citing the experiment without showing it leaves the verification abstract. A schematic of the interferometer geometry — beam split, one path rotated by 2π via magnetic field, recombination showing the π phase shift in the interference pattern — converts "this has been measured" from prose claim to visualizable evidence.

**SCOPE:**

- **Specification:** Apparatus schematic, single panel.
- **Content:** Neutron source on left. Crystal beam splitter creating two paths (upper and lower). Magnetic-field coil on one path (labeled "B-field: rotates neutron spin by 2π"). Recombination at second crystal. Detector showing interference fringes — with annotation "fringes shift by π (half period) when one beam rotated by 2π."
- **Organization:** Left-to-right experiment flow. Inset showing the fringe shift, with two superposed sinusoids: solid line (no rotation) and dashed line (with 2π rotation, displaced by π).
- **Presentation:** Apparatus in neutral gray. Magnetic field in Okabe-Ito orange (#E69F00). Fringes in blue (no rotation) and vermillion (with rotation), since these are the data the experiment produced.
- **Exclusions:** No quantum-mechanical formula derivation in the figure (that's in the prose). No follow-up experiments (Rauch et al. confirmed independently; mentioning is enough). No abstract "interferometer concept" overlay — show this specific experiment.

**Discipline check:** ~6 apparatus components + 2 fringe curves = 8 elements ✓. The π-phase-shift signature is the measurement that confirms the −1 sign; the figure must make that shift visible, not just label it.

---

## What CAJAL Declines to Architect

- **Spin algebra derivation as a flowchart.** The chapter's ladder derivation is mostly equations. A flowchart would either reproduce the math (CAJAL anti-pattern) or be so abstract as to add nothing. The text carries it.
- **Pauli matrices as a figure.** They are 2×2 matrices written out at line 144. Typesetting them again as a figure would just be a screenshot of math.
- **Triplet/singlet state diagram.** The four states (three triplet + one singlet) are clearly enumerated at line 205–209. A box diagram would not improve on the equations. Possibly a table showing j, m, symmetry-under-exchange, but a table is fine — not a figure.
- **EPR/Bell inequality figure.** Belongs to Chapter 10. Mentioning it in Fig 7.3's caption is enough.
- **Classical-vs-quantum angular momentum comparison.** The chapter does not lean on this contrast (it dives directly into the algebra). Adding a figure to compare would over-extend.

---

## Video Candidate Pass

Reviewing all five figures against the four criteria:

- **Fig 7.1 (ladder):** Static. Not a candidate.
- **Fig 7.2 (spherical harmonics):** Could be sweepable across ℓ and m, similar to Ch 6's orbital rotation video. Mild candidate, but redundant with the Ch 6 orbital video.
- **Fig 7.3 (singlet measurement):** **Strong video candidate.** Animate the source emitting the entangled pair, the particles flying outward, two detectors clicking with paired outcomes (always opposite when axes aligned, partial correlation when axes at angle). The sequential causal stages criterion is met cleanly. This is also natural prep for Ch 10's Bell discussion.
- **Fig 7.4 (720° rotation):** **Strong video candidate.** This is the textbook case for animation — the half-angle behavior is intrinsically about *temporal evolution under rotation* and the color-as-phase encoding becomes much more compelling when the rotation actually happens in time. Belt-trick / Dirac-scissors physical demonstration video would be the alternative, but a clean spinor-rotation animation is more on-topic.
- **Fig 7.5 (neutron interferometer):** Borderline. Animating the beam through the apparatus is mildly helpful; static schematic is probably sufficient.

**Recommendation: two videos — singlet measurement (Fig 7.3) and spinor 720° rotation (Fig 7.4).** Both are sub-observation phenomena where the temporal dimension is part of the content. The 720° video in particular has high pedagogical leverage because it makes a result that students consistently dismiss as algebraic curiosity into a visual fact.

---

## Summary

5 figures: 3 author-placed (ladder, spherical harmonics, singlet) + 2 CAJAL-added (720° rotation, WCOE neutron interferometer). Two video candidates (singlet animation, spinor rotation). Key cross-reference: Fig 7.2 (angular |Y_{ℓm}|²) must look visually distinct from Ch 6 Fig 6.5 (full 3D orbital isosurfaces) — label the distinction explicitly. The 720° rotation gets a figure because the chapter's most physical claim deserves visual support; without it, the half-angle factor reads as algebra rather than as a measured fact.
