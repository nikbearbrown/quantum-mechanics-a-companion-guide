# CAJAL Figure Intelligence — Chapter 5: Quantum Formalism

**Source:** `chapters/05-quantum-formalism.md`
**Mode:** `/scan silent`
**Domain note:** Conceptual/argumentative chapter — postulates as theory architecture, Robertson derivation as theorem, six interpretations of the measurement problem as live disagreement. Heavier on prose and equations than on visualizable phenomena. Author placed one inline figure (Fig 5.1 — proof flowchart). The chapter's true visual leverage points are the Heisenberg/Robertson/Ozawa three-way contrast and the Schlosshauer–Kofler–Zeilinger 2013 survey result.

---

## Density Recommendation

**3 figures, Mixed density.** The chapter is mostly text-and-math, but contains two high-leverage visual moments (the three-uncertainty-types contrast and the empirical survey result) plus one borderline proof-structure diagram. Anything more would over-figure a chapter whose argument is the prose; anything less would let the contrast that the chapter most wants to land (Heisenberg ≠ Robertson ≠ Ozawa) slip past.

---

## Zone Map

- **MC (Mechanism Complexity):** Robertson proof has 5 distinct steps (shifted operators → Cauchy-Schwarz → imaginary part → commutator falls out → state-independent for [x,p]). A flowchart can hold the structure that the prose unfolds linearly.
- **VG (Verification Gap):** The chapter explicitly argues *three different uncertainties* keep getting conflated — Heisenberg 1927 measurement disturbance vs. Robertson 1929 state preparation vs. Ozawa 2003 corrected measurement-disturbance. The verification gap is that students leave with one inequality in their head when the chapter just told them there are three. A side-by-side panel forces the distinction visible.
- **PQ (Proportional/Quantitative):** Schlosshauer–Kofler–Zeilinger 2013 — Copenhagen 42%, QBism/information 24%, Many-Worlds 18%, smaller minorities. Real percentages, real disagreement, headline that "there is no consensus" lands harder as bars than as a paragraph.

---

## Figure-by-Figure

### Figure 5.1 — Robertson proof structure flowchart *(author-placed; VALIDATE with caveats)*

**Decision:** Keep, but discipline it. A proof flowchart is a known CAJAL failure mode when it reproduces typeset math as boxed equations. This one survives only if it diagrams the *logical structure* of the steps, not the algebra.

**SCOPE:**

- **Specification:** Process flowchart, 5 nodes plus one branch annotation. Vertical flow.
- **Content:** Five steps as short verbal labels — (1) "Define shifted operators (zero-mean)" → (2) "Build two Hilbert-space vectors |f⟩, |g⟩" → (3) "Cauchy–Schwarz inequality" → (4) "Discard real part; keep imaginary part" → (5) "Commutator appears." Off-branch annotation at step 4: "Keeping the real part = Schrödinger's 1930 strengthening."
- **Organization:** Top-down. Each box has a short label only (≤8 words). No equations inside boxes.
- **Presentation:** Okabe-Ito sequential — light gray boxes with one accent color (orange #E69F00) on the commutator-appearance node, since that is the punchline. Branch annotation in muted blue.
- **Exclusions:** No equations rendered inside the figure. No arrows that double back. No subscript notation. The whole point is to show that this is *one short logical chain* — students who see a wall of math in the figure will skip it.

**Discipline check:** 5 components ✓. Sequential causal flow ✓. The figure earns its place only if it makes a student who skipped the algebra still able to say "Robertson is Cauchy–Schwarz plus take-the-imaginary-part." If it tries to render the math, drop it.

---

### Figure 5.2 — Three uncertainties, three claims *(CAJAL adds; high priority)*

**Why this figure exists:** The chapter's central pedagogical argument — that Heisenberg 1927, Robertson 1929, and Ozawa 2003 are *different inequalities about different things* — is exactly the kind of distinction a comparison-panels figure exists to lock down. The author placed the comparison table at line 118–120 (with placeholder rows), but a visual comparison is the higher-leverage form for this contrast because each one is a different *picture* (a microscope vs. a state in Hilbert space vs. a state + apparatus).

**SCOPE:**

- **Specification:** Comparison panels, three panels side by side, equal size.
- **Content:**
  - Panel A (Heisenberg 1927): schematic of gamma-ray microscope — photon incoming, electron, scattered photon, with brackets labeling Δx (resolution) and Δp (transferred). Caption: "measurement disturbance."
  - Panel B (Robertson 1929): a Hilbert-space-style icon — a state vector |ψ⟩ with two "width" brackets (σ_A, σ_B) on two non-commuting axes; *no apparatus shown*. Caption: "state preparation."
  - Panel C (Ozawa 2003): system + apparatus + arrow — system state with intrinsic width, apparatus icon with noise label ε, disturbance arrow η back to system. Caption: "measurement-disturbance, corrected."
- **Organization:** Left-to-right chronological. Each panel has the inequality printed below in matched typography — Δx·Δp ≳ ℏ / σ_x·σ_p ≥ ℏ/2 / ε(A)·η(B) + ... ≥ ℏ/2 |⟨[A,B]⟩|.
- **Presentation:** Okabe-Ito — blue (#0072B2) for Panel A, vermillion (#D55E00) for Panel B, bluish-green (#009E73) for Panel C. Consistent stroke weight across panels. No red-green pairing — bluish-green and vermillion are colorblind-safe.
- **Exclusions:** No prose summary inside panels (caption-only). No "which is right" verdict. No popular-physics balloon imagery — the chapter spent a paragraph correcting the balloon and a figure that uses it would undo the work.

**Discipline check:** 3 panels × ~3 components each = ~9 visible components, under the 6–8 ceiling per panel ✓. Comparison-panel pattern with a forced parallel reading. Each panel is the answer to "what is the apparatus doing in this inequality?" — A says "everything," B says "nothing," C says "something specific."

---

### Figure 5.3 — Schlosshauer–Kofler–Zeilinger 2013 survey *(CAJAL adds)*

**Why this figure exists:** The chapter's most contestable empirical claim — "working physicists disagree about what their own most successful theory is describing" — is anchored to a single 2013 survey with 33 respondents. A bar chart turns the claim from a paragraph aside into a verifiable picture. Students who walk away remembering "no consensus" are remembering the headline; students who walk away remembering "Copenhagen 42%, QBism 24%, Many-Worlds 18%" are remembering the *evidence*.

**SCOPE:**

- **Specification:** Horizontal bar chart, 5–6 bars, y-axis = interpretation category, x-axis = percentage of respondents.
- **Content:** Bars for Copenhagen (~42%), Information-based / QBism-adjacent (~24%), Many-Worlds (~18%), and the smaller minorities (Bohmian, Objective collapse, Other / Undecided). Sample-size annotation in the title or subtitle: "n = 33, specialist foundations conference (Schlosshauer, Kofler, Zeilinger 2013)."
- **Organization:** Bars sorted descending by percentage. X-axis starts at zero (mandatory).
- **Presentation:** Single neutral color for all bars (Okabe-Ito sky blue, #56B4E9) so no interpretation looks visually privileged. The sample-size caveat sits as a subtitle, not as small print.
- **Exclusions:** No 3D effects. No pie chart (a pie chart of 33 respondents implies authority the sample does not support). No commentary about which interpretation is "right" — the figure exists to display the disagreement, not adjudicate it. No error bars (the survey did not report them and inventing them would be dishonest).

**Discipline check:** 5–6 bars, well under the component ceiling ✓. Y-axis (categorical) starts at zero on the value dimension ✓. The sample-size disclaimer is structural — without it, this figure overstates the survey's authority.

---

## What CAJAL Declines to Architect

- **"The five postulates" as a diagram.** The chapter states them as a numbered list with clear physical-requirement annotations. A 5-box diagram would add nothing the list does not already do. Skip.
- **"Four settled, one contested" as a hierarchy diagram.** This is a one-sentence structural insight ("Postulates 1, 2, 3, 5 are uncontroversial; Postulate 4 is where interpretations diverge"). A diagram would crowd it; the sentence carries.
- **CSCO Venn diagram.** Tempting, but the CSCO concept is about which operators commute — Venn diagrams represent set membership and would visually misrepresent what is actually a statement about shared eigenbases. Skip.
- **Interpretation comparison as a figure.** The author placed a comparison table at line 184–186 (with placeholder rows). Keep it as a *table*, not a figure — five interpretations × four attributes is exactly what tables do well. A figure here would just be a table with worse typography.
- **Stern–Gerlach sequence (Exercise A3).** Exercises sometimes warrant figures; this one is short and self-contained. Skip unless the exercise expands.

---

## Video Candidate Pass

Reviewing the three figures against the four criteria (transition mechanism, sequential causal stages, cyclical, sub-observation):

- **Fig 5.1 (proof flowchart):** Sequential causal stages — five steps. Borderline candidate. A 20-second build where each step appears with a one-sentence voiceover ("Step 1: shift the operators to zero mean. Why? So the variances become expectation values...") could land the proof structure for students who bounce off the algebra. **Weak candidate** — the static figure already shows the sequence, and the math is the work.
- **Fig 5.2 (three uncertainties):** Comparison, not transition. Not a video candidate.
- **Fig 5.3 (survey bars):** Static data. Not a video candidate.

**Recommendation: no video.** Fig 5.1 is borderline but the marginal benefit over a clear static flowchart does not justify the production cost. If a video is wanted somewhere in this chapter, the better candidate is *not in the figures* — it is the Stern–Gerlach sequential measurement (Exercise A3), where the temporal dynamics of state collapse genuinely benefit from animation. Flag for chapter 7 or a separate measurement-process clip.

---

## Summary

3 figures architected: 1 author-placed (Fig 5.1, validated with discipline caveats), 2 CAJAL-added (Fig 5.2 three-uncertainties comparison, Fig 5.3 Schlosshauer survey). No videos. Chapter's argument is in the prose and the math; figures earn their place by locking down the two visualizable distinctions (preparation vs. disturbance; empirical disagreement among physicists) that the text alone can underdeliver.
