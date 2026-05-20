# Assertions Report: 04-one-dimensional-problems.md
**Date:** 2026-05-14
**Source file:** chapters/04-one-dimensional-problems.md
**Assertions flagged:** 9
**Breakdown:** STAT: 4 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 0

---

## ⚠️ Critical — Requires Immediate Expert Review
None found.

---

## Full Findings

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "the scanning tunneling microscope (Binnig and Rohrer, 1982, Nobel Prize 1986) works"
**Claim checked:** Binnig & Rohrer invented the STM, first published in 1982, awarded the 1986 Nobel Prize.
**Site visited:** https://www.nobelprize.org/prizes/physics/1986/summary/
**Finding:** Confirmed. Binnig, G. & Rohrer, H. "Scanning Tunneling Microscopy." Helv. Phys. Acta 55, 726 (1982); first PRL: Binnig, Rohrer, Gerber, Weibel, "Tunneling through a controllable vacuum gap," Appl. Phys. Lett. 40, 178 (1982). Nobel 1986 shared with E. Ruska (electron microscope).
**Expert review needed:** No
**Suggested reference:** Binnig, G. & Rohrer, H. "Scanning Tunneling Microscopy—from Birth to Adolescence." Rev. Mod. Phys. 59, 615 (1987). https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.59.615
**Notes:** Strictly the STM project began in 1981 at IBM Zürich; first publications appeared in 1982. The book's "1982" is the publication-year shorthand and is fine.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "George Gamow published in 1928."
**Claim checked:** Gamow's 1928 alpha-decay calculation.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Gamow, G. "Zur Quantentheorie des Atomkernes." Z. Phys. 51, 204–212 (1928). Independently: Gurney, R. W. & Condon, E. U. "Wave Mechanics and Radioactive Disintegration." Nature 122, 439 (1928).
**Expert review needed:** No
**Suggested reference:** Gamow, G. "Zur Quantentheorie des Atomkernes." Z. Phys. 51, 204–212 (1928). Gurney, R. W. & Condon, E. U. Nature 122, 439 (1928).
**Notes:** Gurney & Condon independently derived the same result in 1928 and did not get equal billing in the textbook record. Worth a one-line footnote: "Gamow, and independently Gurney & Condon, 1928."

### STAT — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "The measured half-life of U-238 is 4.5 × 10⁹ years."
**Claim checked:** Half-life of U-238.
**Site visited:** NIST / IAEA nuclear data.
**Finding:** Confirmed. T_{1/2}(U-238) = 4.468 × 10⁹ years (IAEA Nuclear Data Section, Atomic Mass Evaluation). The book's "4.5 × 10⁹" is correct rounding.
**Expert review needed:** No
**Suggested reference:** Audi, G. et al. "The NUBASE evaluation of nuclear and decay properties." Nucl. Phys. A 729, 3 (2003); IAEA Nuclear Data Section, https://www-nds.iaea.org/
**Notes:** None.

### STAT — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "For U-238, plugging in E = 4.27 MeV and Z = 92"
**Claim checked:** U-238 alpha energy ≈ 4.27 MeV.
**Site visited:** Nuclear-data tables.
**Finding:** Confirmed. E_α(U-238) = 4.270 MeV (primary alpha line). Z = 92 is correct.
**Expert review needed:** No
**Suggested reference:** NNDC, Brookhaven National Laboratory. Nuclear Wallet Cards. https://www.nndc.bnl.gov/
**Notes:** None.

### STAT — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Po-212 has E ≈ 8.78 MeV; Th-232 has E ≈ 4.08 MeV."
**Claim checked:** Alpha energies for Po-212 and Th-232.
**Site visited:** Nuclear-data tables.
**Finding:** Confirmed. E_α(Po-212) = 8.785 MeV (primary, 100%); E_α(Th-232) = 4.012 MeV (primary, 77%) or 3.948 MeV (secondary, 23%). The 4.08 MeV in the book corresponds to a weighted value or a rounded primary line; 4.012 MeV is the cleanest single number. Close enough for the order-of-magnitude argument the chapter is making.
**Expert review needed:** Yes — verify the exact Th-232 E_α the chapter uses against NNDC tables. 4.012 MeV is more standard than 4.08.
**Suggested reference:** NNDC Nuclear Wallet Cards. https://www.nndc.bnl.gov/
**Notes:** The half-life claims are: Po-212 = 0.299 µs ≈ 0.3 µs (book's value); Th-232 = 1.405 × 10¹⁰ years (book says "1.4 × 10¹⁰" and "~10¹⁰" — both correct).

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "The Geiger-Nuttall law — the empirical observation, known since 1911"
**Claim checked:** Geiger-Nuttall law dated to 1911.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Geiger, H. & Nuttall, J. M. "The ranges of the α particles from various radioactive substances and a relation between range and period of transformation." Phil. Mag. 22, 613 (1911).
**Expert review needed:** No
**Suggested reference:** Geiger, H. & Nuttall, J. M. Phil. Mag. 22, 613 (1911).
**Notes:** None.

### STAT — UNVERIFIED
**Assertion type:** BASIC
**Sentence:** "The Coulomb repulsion between the alpha (+2e) and the residual nucleus ((Z−2)e) at the nuclear surface radius R ≈ 7 fm is about 28 MeV for uranium."
**Claim checked:** Coulomb barrier height for U alpha decay ≈ 28 MeV at R = 7 fm.
**Site visited:** Computed check: V_Coulomb = 2(Z-2)e²/(4πε₀ R) = 2·90·(1.44 MeV·fm)/7 fm = 37 MeV. Using a slightly larger R = 9.3 fm gives ~28 MeV.
**Finding:** The order of magnitude is right; the specific value 28 MeV requires either R ≈ 9 fm (more realistic for U-238 + alpha total radius, since R_alpha + R_daughter ≈ 1.2 fm × (4^{1/3} + 234^{1/3}) ≈ 9.3 fm) or some other convention. The "R ≈ 7 fm" in the book corresponds to the daughter alone; the relevant barrier radius is daughter + alpha. Worth tightening.
**Expert review needed:** Yes — the numbers 7 fm and 28 MeV don't match each other; one should be revised. The standard treatment uses R = 1.2 fm × A^{1/3} for the daughter (≈ 7.5 fm for Th-234) but the barrier radius is daughter + alpha radius.
**Suggested reference:** Krane, K. *Introductory Nuclear Physics*, Wiley, 1988, Ch. 8 (alpha decay).
**Notes:** Pedagogical computation, not a citation-claim. The author should re-derive cleanly for the published edition.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "The scanning tunneling microscope reads signals at exactly these suppression levels and turns them into atomic-resolution images of surfaces."
**Claim checked:** STM resolves single atoms via tunneling current.
**Site visited:** https://www.nobelprize.org/prizes/physics/1986/binnig/lecture/
**Finding:** Confirmed — atomic-resolution STM imaging is what won the 1986 Nobel.
**Expert review needed:** No
**Suggested reference:** Binnig, G. & Rohrer, H. "Scanning Tunneling Microscopy—from Birth to Adolescence." Rev. Mod. Phys. 59, 615 (1987).
**Notes:** None.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "in one dimension, a finite well always has at least one bound state, no matter how shallow."
**Claim checked:** Existence of a bound state in 1D for arbitrarily shallow attractive potential.
**Site visited:** General mathematical-physics result.
**Finding:** Confirmed. This is a standard theorem in 1D scattering theory. Simon, B. "The bound state of weakly coupled Schrödinger operators in one and two dimensions." Ann. Phys. 97, 279 (1976) proves the rigorous version for general short-range potentials in 1D and 2D.
**Expert review needed:** No
**Suggested reference:** Simon, B. "The bound state of weakly coupled Schrödinger operators in one and two dimensions." Ann. Phys. 97, 279 (1976).
**Notes:** The statement is also true in 2D (subtle — requires the integral of V to be negative), but *false* in 3D for short-range potentials. The book correctly flags the 3D failure.

---

## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
| "Coulomb barrier 28 MeV at R = 7 fm for U" | STAT | BASIC | Numbers don't match each other arithmetically; either R or 28 MeV needs revision. |
| "Th-232 alpha energy 4.08 MeV" | STAT | BASIC | Standard value is 4.012 MeV (primary line); 4.08 MeV needs sourcing or correction. |
| "Po-212 half-life ~0.3 µs" | STAT | BASIC | Match (0.299 µs); fine. |

---

## AI-Pass Flags
- **Two arithmetic checks recommended.**
  1. The "28 MeV at R = 7 fm" pair for the Coulomb barrier is internally inconsistent: 2·90·1.44/7 ≈ 37 MeV. If 28 MeV is the intended value, R should be ~9 fm (daughter + alpha radius). The chapter's downstream Gamow calculation does use a closed-form integral that doesn't directly need this number, so the answer (γ ≈ 44 → half-life ~10¹⁷ s) is still correct; the surface inconsistency is a pedagogical lapse.
  2. "The forms are the same — both go as ℏ²/(mL²) — and the factor of roughly 40 between them is geometry, not physics." Factor between π²/2 ≈ 4.93 and 1/8 = 0.125 is 39.5 — "roughly 40" is right.

- **"Confine a particle to a box of width L. Its position uncertainty can be no larger than L."** Tighter bound: σ_x for an infinite-well ground state is L/(2π)·√(π²/3 − 2) ≈ 0.181·L. The book's σ_x ≤ L is a generous upper bound used heuristically; the heuristic estimate of E_min is order-of-magnitude correct but the inequality is loose. This is pedagogically standard and fine, but a reviewer should note that the "factor of 40" is essentially the looseness of σ_x ≤ L.


---

## Resolutions applied 2026-05-14

- **Coulomb barrier R**: chapter prose updated from R ≈ 7 fm → **R ≈ 9 fm** (the daughter + alpha touching radius, R ≈ 1.2 fm · (A_daughter^{1/3} + 4^{1/3})). With R = 9 fm and Z = 92, V_Coulomb = 2·90·1.44/9 ≈ 28.8 MeV — consistent with the stated 28 MeV. Inline FACT-CHECK FLAG removed.
- **Th-232 alpha energy**: both instances updated from 4.08 MeV → **4.01 MeV** (NNDC primary line). Order-of-magnitude conclusion (24 decades of half-life range from a factor-of-two energy difference) unchanged.
