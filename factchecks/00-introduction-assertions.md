# Assertions Report: 00-introduction.md
**Date:** 2026-05-14
**Source file:** chapters/00-introduction.md
**Assertions flagged:** 4
**Breakdown:** STAT: 0 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 3 | SPECIALIST: 1 | CURRENT: 0

---

## ⚠️ Critical — Requires Immediate Expert Review
None found.

---

## Full Findings

### SPECIALIST — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "She reaches Chapter 3, Section 3.5, where Griffiths derives σ_A σ_B ≥ (1/2) |⟨[Â, B̂]⟩| from the Cauchy-Schwarz inequality."
**Claim checked:** The Robertson uncertainty bound σ_A σ_B ≥ (1/2)|⟨[A,B]⟩| is the standard generalized form, with the Cauchy–Schwarz proof being the canonical derivation. Griffiths §3.5 (3rd ed.) location reference.
**Site visited:** https://plato.stanford.edu/entries/qt-uncertainty/
**Finding:** Standard generalized uncertainty relation; the Cauchy–Schwarz proof is in every standard undergraduate text. Specific Griffiths section/edition pointer is an in-text citation that the human reviewer can verify against their copy.
**Expert review needed:** No (formula); Yes (section number — verify against the specific Griffiths edition the book is recommending)
**Suggested reference:** Robertson, H. P. "The Uncertainty Principle." Phys. Rev. 34, 163 (1929). https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163
**Notes:** The Griffiths section number (3.5) is the standard location in the 2nd and 3rd editions for the generalized uncertainty derivation. Worth a quick edition-check before publication.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Fermi's golden rule (historically attributed to Dirac 1927)."
**Claim checked:** The transition-rate formula known as "Fermi's golden rule" was first derived by P. A. M. Dirac in 1927.
**Site visited:** Not separately searched — well-established in physics history. Dirac's 1927 paper "The Quantum Theory of the Emission and Absorption of Radiation" (Proc. R. Soc. Lond. A 114, 243–265) contains the derivation that became known as Fermi's golden rule.
**Finding:** Standard physics-history attribution. Fermi coined the "golden rule" terminology in lectures published in his 1950 book *Nuclear Physics* (notes by Orear, Rosenfeld, Schluter), referring back to Dirac's earlier derivation.
**Expert review needed:** No
**Suggested reference:** Dirac, P. A. M. "The Quantum Theory of the Emission and Absorption of Radiation." Proc. R. Soc. Lond. A 114, 243–265 (1927). https://doi.org/10.1098/rspa.1927.0039
**Notes:** Worth flagging the historiographic point in Unit 9 directly: it's "Dirac's rule named by Fermi" — exactly as the book says.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Robertson 1929 corrected it."
**Claim checked:** Robertson 1929 produced the generalized standard-deviation uncertainty inequality.
**Site visited:** https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163
**Finding:** Phys. Rev. 34, 163 (1929) is correct.
**Expert review needed:** No
**Suggested reference:** Robertson, H. P. "The Uncertainty Principle." Phys. Rev. 34, 163 (1929). https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163
**Notes:** As in 00-frontmatter, "corrected" is the book's polemical shorthand — Kennard 1927 had σ_x σ_p ≥ ℏ/2 already; Robertson generalized to arbitrary observables.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Heisenberg's 1927 microscope argument — the *epistemic* version of uncertainty."
**Claim checked:** The 1927 Heisenberg paper used the gamma-ray-microscope thought experiment to argue uncertainty as measurement disturbance.
**Site visited:** https://plato.stanford.edu/entries/qt-uncertainty/
**Finding:** Confirmed — Heisenberg's 1927 paper includes the gamma-ray microscope thought experiment alongside an algebraic argument. The disturbance/epistemic reading is standard historical characterization.
**Expert review needed:** No
**Suggested reference:** Heisenberg, W. "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik." Z. Phys. 43, 172–198 (1927). https://doi.org/10.1007/BF01397280
**Notes:** Stanford Encyclopedia of Philosophy entry "The Uncertainty Principle" is the cleanest secondary source for this characterization.

---

## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
| "ten units rather than chapters because each unit maps to a unit of a standard semester quantum-mechanics course" | (pedagogical/organizational claim) | BASIC | Not a verifiable fact — author's editorial choice |

---

## AI-Pass Flags
- The introduction repeats most of the substantive content of the Preface (00-frontmatter.md) — Heisenberg/Robertson, balloon analogy, audit framing. Not an error, but worth noting that any factual correction in one should be propagated to the other.
- The chapter map (lines 53–68) names Unit 5 as "Quantum Formalism" with "the rigorous Robertson uncertainty derivation; the balloon-analogy correction" — and Unit 6 as "Hydrogen Atom" with "spin and Stern-Gerlach, Pauli exclusion." This split is unusual (Stern-Gerlach is typically a Unit-7 angular-momentum topic) but matches the actual content of those units in the book — consistent internal cross-referencing.
