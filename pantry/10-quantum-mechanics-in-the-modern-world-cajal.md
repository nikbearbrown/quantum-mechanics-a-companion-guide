# CAJAL Figure Intelligence — Chapter 10: Quantum Mechanics in the Modern World

**Source:** `chapters/10-quantum-mechanics-in-the-modern-world.md`
**Mode:** `/scan silent`
**Domain note:** Application-survey chapter — six major topics (Bell/CHSH, lasers, semiconductors, quantum computing, superconductivity, tunneling applications), each connecting earlier-chapter formalism to a modern Nobel-Prize or trillion-dollar-industry payoff. The author placed seven figures, roughly one per topic with quantum computing getting two (gate circuit + algorithm scaling). This is the chapter's natural figure density — applications need visual anchors because each topic touches a different physical regime, and a reader who skims this chapter for the "what is the quantum story behind X" answer needs each topic figure-led.

---

## Density Recommendation

**7 figures, Mechanistic density.** This is the chapter where high figure count is justified by the chapter's structure — six independent application areas, each with its own visualizable payoff. CAJAL validates all seven author-placed figures with discipline notes; no additions. The density that would be excessive in a foundational chapter (like Ch 5 or Ch 7) is appropriate here because the chapter's job is to land six distinct claims about the world.

Final count: **7 figures** — 7 validated author-placed + 0 CAJAL-added.

---

## Zone Map

- **MC (Mechanism Complexity):** Each application has its own mechanism — Bell/CHSH inequality structure, three-level laser pumping, band gap formation, gate-based quantum circuit construction, BCS Cooper-pair condensation, STM tunneling exponential. The chapter compresses each mechanism into a few paragraphs; figures relieve that compression.
- **VG (Verification Gap):** The chapter cites a *lot* of experimental numbers (Aspect S = 2.697, 1.3 km Hensen separation, 1.12 eV silicon gap, 1,100 IBM Condor qubits, 4.2 K Onnes mercury, 250 K LaH₁₀ at 170 GPa). Most are mentioned without visual anchor, but the structural diagrams (band gaps, T_c timeline, CHSH bar diagram) anchor the most pedagogically critical ones.
- **PQ (Proportional/Quantitative):** Strong PQ candidates — the 2 vs 2√2 vs 4 hierarchy in CHSH, the band-gap energies across semiconductor families, the 1911→present T_c records, the Shor (polynomial) vs Grover (sqrt) vs classical (exponential) scaling on a log plot. Each is figured.

---

## Figure-by-Figure

### Figure 10.1 — CHSH bound, Tsirelson bound, Popescu-Rohrlich bound *(author-placed; VALIDATE)*

**Decision:** Keep. The chapter's headline mathematical result — local hidden variables ≤ 2, quantum mechanics achievable ≤ 2√2, mathematically possible without superluminal signaling ≤ 4 — is exactly the kind of three-region number line that lands the structural argument: there is *room* for quantum mechanics to lie above LHV and below the mathematical maximum, and the room is exactly what experiment is testing.

**SCOPE:**

- **Specification:** Horizontal number line or bar diagram, |S| value on x-axis, range 0 to 4.
- **Content:** Three regions colored or shaded distinctly: (1) 0 to 2, labeled "achievable by local hidden variables (LHV)"; (2) 2 to 2√2 ≈ 2.828, labeled "quantum mechanics (singlet, optimal axes)"; (3) 2√2 to 4, labeled "no-signaling but non-quantum (Popescu-Rohrlich)." Markers at 2 (CHSH bound), 2√2 (Tsirelson bound), 4 (algebraic maximum). Experimental marker at 2.697 (Aspect 1982) somewhere in the QM region.
- **Organization:** Single horizontal axis with the three regions shown as filled bands or distinct colors.
- **Presentation:** Okabe-Ito — LHV region in light sky blue (#56B4E9), QM region in vermillion (#D55E00), PR region in light gray. Markers as vertical lines with labels above.
- **Exclusions:** Do not include the full Bell inequality derivation in the figure (that's the prose). Do not include experimental values from multiple experiments (one representative marker is enough; the chapter lists three 2015 loophole-free experiments and listing them all in the figure would clutter). Do not editorialize about which interpretation is "right" — the figure is structural.

**Discipline check:** 3 regions + 3 markers + experimental annotation + axis = ~7 elements ✓. The structural punchline — there's a quantum region *strictly above* the LHV region — is the figure's reason to exist.

---

### Figure 10.2 — Three-level (or four-level) laser energy diagram *(author-placed; VALIDATE)*

**Decision:** Keep, but the author's caption just says "Energy level diagram" — needs to specify which scheme. Recommendation: use the three-level scheme (as in the original ruby laser, which the chapter cites) to keep continuity with Maiman 1960, with an inset or callout showing the four-level scheme as the more common modern variant.

**SCOPE:**

- **Specification:** Energy-level diagram, three or four levels stacked vertically.
- **Content:**
  - Three-level scheme: ground state (level 1, heavily populated), pump level (level 3, broad band), metastable upper laser level (level 2, narrow). Pump arrow from 1 to 3 (broadband light from flashlamp). Fast non-radiative decay arrow from 3 to 2. Stimulated emission arrow from 2 to 1 (the lasing transition). Population inversion annotation: N₂ > N₁.
  - Optional inset: four-level scheme showing why four-level lasers are easier (the lower laser level isn't the ground state, so inversion is achieved with less pumping).
- **Organization:** Energy on y-axis, level labels on left, transitions as arrows.
- **Presentation:** Okabe-Ito — pump arrow in orange (#E69F00, broadband), non-radiative decay in gray (heat), stimulated emission in vermillion (#D55E00, coherent). Population labels (N₁, N₂, N₃) on right.
- **Exclusions:** Do not show the actual Einstein A and B coefficients as labels on arrows (those are computed quantities, not visual elements). Do not include cavity mirrors / optical feedback (that's a separate apparatus figure if needed). Do not show specific ruby energy levels — keep generic enough to apply to any three-level laser.

**Discipline check:** 3–4 levels + 3 arrow types + population labels = ~7 elements ✓. The pedagogical point — "population inversion is achieved by pumping through a third level" — must be clear from the diagram alone.

---

### Figure 10.3 — Band diagrams: conductor, insulator, semiconductor *(author-placed; VALIDATE)*

**Decision:** Keep. The three-panel side-by-side band diagram is canonical for distinguishing conductors (overlap or partial filling), insulators (large gap), and semiconductors (small gap). The figure does exactly what the chapter's prose claim needs.

**SCOPE:**

- **Specification:** 3-panel band-energy diagram, side by side.
- **Content:**
  - Panel A (conductor): Valence band and conduction band overlap, or the valence band is partially filled. Fermi level inside a band. Caption: "metal."
  - Panel B (insulator): Wide gap (~5 eV) between filled valence band and empty conduction band. Fermi level in the middle of the gap. Caption: "insulator (gap ~5 eV)."
  - Panel C (semiconductor): Narrow gap (~1 eV). Same structure as insulator but with the gap labeled "Si: 1.12 eV, GaAs: 1.43 eV." Caption: "semiconductor."
- **Organization:** All three panels share the same energy axis range so gaps are quantitatively comparable.
- **Presentation:** Okabe-Ito — filled valence bands in dark blue (#0072B2), empty conduction bands in light blue (#56B4E9), Fermi level as a dashed horizontal in vermillion. k_BT ≈ 0.025 eV at 300 K shown as a small reference bracket.
- **Exclusions:** Do not show E vs k dispersion curves — those are different figures (the band-structure figure type). This figure is energy-level schematic only. Do not include doping (n-type, p-type) in this figure — the chapter discusses doping in prose; a separate figure for doped semiconductors would over-extend.

**Discipline check:** 3 panels × 2 bands + Fermi level + gap labels = ~9 elements across all panels ✓. The quantitative comparability — gaps drawn to scale across panels — is the discipline-critical choice that makes the semiconductor case visibly intermediate.

---

### Figure 10.4 — Bell state generation circuit (Hadamard + CNOT) *(author-placed; VALIDATE)*

**Decision:** Keep. The circuit notation is the lingua franca of quantum computing, and showing the simplest non-trivial circuit — two gates producing maximal entanglement — anchors the chapter's claim that "the Bell states at the heart of every CHSH experiment are produced in two gates."

**SCOPE:**

- **Specification:** Standard quantum-circuit diagram, two qubits.
- **Content:** Two horizontal wires (top = qubit 1, bottom = qubit 2). Both start in |0⟩ (annotated on the left). Hadamard gate (boxed "H") on qubit 1. CNOT gate (filled dot on qubit 1, ⊕ on qubit 2) after the Hadamard. Output annotated on the right as (|00⟩ + |11⟩)/√2. Intermediate state labeled between gates: (|00⟩ + |10⟩)/√2.
- **Organization:** Left-to-right reading, standard circuit convention. Time flows rightward.
- **Presentation:** Black wires on white background, standard circuit notation. Gate boxes in single Okabe-Ito accent color (sky blue #56B4E9). Bell state output highlighted in vermillion for emphasis.
- **Exclusions:** Do not include measurement gates (the Bell state is the output, not measured here). Do not show all four Bell states (Φ⁺, Φ⁻, Ψ⁺, Ψ⁻) — the chapter mentions one, the figure should show that one. Do not depict the Bloch sphere or vector representations (different visualization style, would crowd).

**Discipline check:** 2 wires + 2 gates + 3 state annotations = 7 elements ✓. Standard circuit notation is well-established; the figure earns its place by showing that maximal entanglement requires only two gates.

---

### Figure 10.5 — Shor vs Grover vs classical: runtime scaling *(author-placed; VALIDATE)*

**Decision:** Keep. The "not all quantum speedups are the same" point lands much harder visually than verbally. On a log-log plot, Shor's polynomial scaling vs the classical sub-exponential factoring algorithm should look dramatically different from Grover's √N vs N quadratic improvement. The visual makes the pedagogical claim that *exponential speedup is the rare, special case*.

**SCOPE:**

- **Specification:** Log-log plot (or possibly semi-log), runtime on y-axis, problem size on x-axis.
- **Content:**
  - Factoring panel (or top curves): Classical GNFS runtime ∝ exp(O(n^{1/3} (log n)^{2/3})) as a steeply rising curve. Shor's algorithm runtime O(n³) as a much shallower curve. The gap widens dramatically with n.
  - Search panel (or bottom curves): Classical brute force O(N) as a linear-on-log-scale curve. Grover's O(√N) as a flatter curve. Gap exists but is constant on log scale (factor of 2 shift).
- **Organization:** Either two panels (factoring | search) or one combined plot with four curves and a legend distinguishing them.
- **Presentation:** Okabe-Ito — classical algorithms in vermillion (#D55E00, dramatic), quantum algorithms in bluish-green (#009E73, beneficial). Annotations: "exponential speedup" for Shor with arrow showing widening gap; "quadratic speedup" for Grover with arrow showing parallel-on-log gap.
- **Exclusions:** Do not include specific hardware estimates (those age fast). Do not include other algorithms (HHL, quantum simulation) — the chapter focuses on Shor and Grover, the figure should follow. Do not use linear axes — the whole point is the dramatic asymptotic difference, which requires log scaling.

**Discipline check:** 4 curves + 2 annotations + legend = ~7 elements ✓. The visual asymmetry between Shor's gap (widens) and Grover's gap (parallel) is the chapter's argument; the figure must make it unmistakable.

---

### Figure 10.6 — Superconductor T_c records, 1911–present *(author-placed; VALIDATE)*

**Decision:** Keep. The history of superconductivity is a sequence of T_c records, each one with a story: Onnes/Hg/4.2 K, the slow grind to ~23 K with conventional materials, the 1986 cuprate breakthrough to ~35 K and quickly to ~93 K (above LN₂), the 2010s pressure-stabilized hydrides to ~200–250 K. The chapter cites all of these; the figure timelines them.

**SCOPE:**

- **Specification:** Scatter plot, year on x-axis (1911 to present), T_c (K) on y-axis (log scale recommended given the 1.1 K to 250 K range).
- **Content:** Marked points for each major record — Hg (1911, 4.2 K), Nb (1930, 9 K), Nb₃Ge (1973, 23 K), LBCO (1986, 35 K), YBCO (1987, 93 K), HgBaCaCuO (1993, 133 K), H₃S under pressure (2015, 203 K), LaH₁₀ under pressure (2019, 250 K). Horizontal reference line at 77 K (liquid nitrogen boiling point) — crossing it in 1987 is the chapter's economic-significance threshold.
- **Organization:** Time forward on x-axis, T_c log-scaled on y-axis. Reference line at LN₂ boiling point.
- **Presentation:** Okabe-Ito — conventional superconductors in blue, cuprates in vermillion, pressure-stabilized hydrides in orange. Different markers (circle, square, triangle) to distinguish categories. Legend.
- **Exclusions:** Do not include unconfirmed claims (LK-99 2023, etc.) — keep to confirmed, peer-reviewed records. Do not extrapolate to predicted future records. Do not include T_c for individual elements/compounds that are not records — only milestone points.

**Discipline check:** ~8 data points + reference line + categorical color/marker scheme + legend = ~12 elements. At the edge of the ceiling but well-organized as a scatter plot. The chapter's claim "the slope is real; room-temperature ambient-pressure remains elusive" must be visually evident.

---

### Figure 10.7 — STM cross-section *(author-placed; VALIDATE)*

**Decision:** Keep. The STM works on a single physical principle — the WKB tunneling exponential — and the cross-section diagram makes that principle visible: tip atoms close to surface atoms, ångström-scale gap, exponential current dependence. The chapter's punchline — "the atom's height changes by 1 Å, the tunneling current changes by a factor of 7" — should appear as an annotation.

**SCOPE:**

- **Specification:** Schematic cross-section, atomic-scale.
- **Content:** STM tip (apex shown as a single or few atoms at the very bottom), vacuum gap (labeled d ≈ a few Å), conducting surface with several atoms visible. Tunneling current arrow between tip apex and the closest surface atom. Inset graph: I vs d showing the exponential I ∝ e^(−2κd) with κ ≈ 1 Å⁻¹.
- **Organization:** Main diagram on left (cross-section), inset graph on right (exponential dependence).
- **Presentation:** Tip and surface atoms as spheres in neutral gray. Current arrow in vermillion. Vacuum gap labeled clearly. Inset graph axes labeled, exponential curve in bluish-green.
- **Exclusions:** Do not show the entire STM apparatus (piezoelectric scanners, vibration isolation, electronics) — this figure is about the tunneling physics, not the engineering. Do not include a topographic image of an actual surface (those are the data STM produces; this figure is about how STM works). Do not editorialize about resolution — let the exponential annotation do the work.

**Discipline check:** Tip + atoms + gap + current arrow + inset = ~6 elements ✓. The annotation "1 Å → factor of 7 current change" is essential; without it, the figure looks like a generic apparatus diagram rather than an explanation of why STM resolves atoms.

---

## What CAJAL Declines to Architect

- **EPR thought-experiment diagram.** Mentioned at line 28 as the historical setup. The CHSH figure (Fig 10.1) carries the structural argument; a separate EPR diagram would duplicate. Skip.
- **Bell-state Bloch-sphere visualization.** Quantum-computing texts often visualize single-qubit states on the Bloch sphere; the chapter focuses on multi-qubit circuits where the Bloch sphere does not generalize cleanly. Skip.
- **pn-junction band diagram.** The chapter discusses doping and the pn junction in prose at line 121. A separate figure would extend the semiconductor section into device territory; the chapter's purpose is the band-theory foundation. Skip.
- **Josephson-junction circuit diagram.** Mentioned at line 199 as one of several tunneling applications. Would over-extend; the STM figure (Fig 10.7) is the chapter's tunneling-application visual.
- **Cooper-pair / BCS gap diagram.** The 2Δ/k_BT_c ≈ 3.53 universality is mentioned at line 172 but is a quantitative prediction better made in prose. A density-of-states figure showing the BCS gap could be added, but the T_c timeline (Fig 10.6) is the chapter's superconductivity visual.

---

## Video Candidate Pass

Reviewing all seven figures against the four criteria:

- **Fig 10.1 (CHSH bands):** Static. Not a candidate.
- **Fig 10.2 (laser energy levels):** **Mild video candidate.** Animate the populations: atoms pumped from 1 to 3, decaying to 2, accumulating in metastable level until N₂ > N₁, then a stimulated emission cascade. The temporal buildup of population inversion is genuinely dynamic.
- **Fig 10.3 (band diagrams):** Static. Not a candidate.
- **Fig 10.4 (Bell state circuit):** **Strong video candidate.** Animate the state evolution through each gate — |00⟩ → (|00⟩ + |10⟩)/√2 after Hadamard → (|00⟩ + |11⟩)/√2 after CNOT. Each gate as a discrete temporal step. Sequential causal stages criterion met cleanly.
- **Fig 10.5 (algorithm scaling):** Static asymptotic plot. Not a candidate.
- **Fig 10.6 (T_c timeline):** Could be animated as records-fall-over-time, but the static scatter plot carries the same content.
- **Fig 10.7 (STM):** **Mild video candidate.** Animate the tip scanning over a surface with atoms, current responding to atomic topography. Visual demonstration of why exponential sensitivity produces atomic resolution.

**Recommendation: one video — Bell state generation (Fig 10.4).** The gate-by-gate evolution is canonical quantum-computing pedagogy and the most visually compelling of the candidates. Laser pumping (Fig 10.2) is a second-tier candidate if production capacity allows.

---

## Summary

7 figures: 7 validated author-placed (CHSH bounds, laser levels, band diagrams, Bell state circuit, algorithm scaling, T_c timeline, STM cross-section). No CAJAL additions — the author identified the right visualizable moments for each application. One strong video candidate (Bell state generation animation) plus secondary candidates (laser pumping, STM scan). The chapter's natural figure density is high because its job is to land six independent application claims, each in a different physical regime; trying to reduce the count would force readers to do the visual work the chapter is meant to do for them.
