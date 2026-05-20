# Assertions Report: 02-mathematical-foundations.md
**Date:** 2026-05-14
**Source file:** chapters/02-mathematical-foundations.md
**Assertions flagged:** 6
**Breakdown:** STAT: 0 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 4 | SPECIALIST: 2 | CURRENT: 0

---

## ⚠️ Critical — Requires Immediate Expert Review
None found.

---

## Full Findings

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Stueckelberg showed in 1960 that you can reformulate quantum mechanics with real numbers if you double the dimension of every space — one extra real dimension to replace each complex one."
**Claim checked:** Stueckelberg's 1960 paper on real-amplitude reformulation of QM via doubled-dimension Hilbert space.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Stueckelberg, E. C. G. "Quantum theory in real Hilbert space." Helv. Phys. Acta 33, 727 (1960). The construction "doubles" the dimension by encoding each complex amplitude in a real symplectic pair.
**Expert review needed:** No
**Suggested reference:** Stueckelberg, E. C. G. "Quantum theory in real Hilbert space." Helv. Phys. Acta 33, 727–752 (1960).
**Notes:** None.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "And Renou and collaborators published an experiment in 2021 that directly tested a whole class of real-amplitude reformulations using Bell inequalities — and ruled them out [Renou et al., *Nature* 600, 625–629 (2021), *verify pagination*]."
**Claim checked:** Renou et al. 2021 Nature paper on falsifying real-amplitude QM; pagination 600, 625–629.
**Site visited:** https://www.nature.com/articles/s41586-021-04160-4
**Finding:** Confirmed. Renou, M.-O. et al. "Quantum theory based on real numbers can be experimentally falsified." Nature 600, 625–629 (2021). Pagination matches the book's tentative citation exactly.
**Expert review needed:** No — the in-text "*verify pagination*" marker can be removed.
**Suggested reference:** Renou, M.-O. et al. "Quantum theory based on real numbers can be experimentally falsified." Nature 600, 625–629 (2021). https://doi.org/10.1038/s41586-021-04160-4
**Notes:** Strictly the Renou et al. paper is theoretical (proposing a Bell-test that distinguishes real from complex QM in a network scenario). A separate experimental test — Li, M.-C. et al. "Testing real quantum theory in an optical quantum network." Phys. Rev. Lett. 128, 040402 (2022) — implemented it and ruled out real-amplitude reformulations. The book conflates the proposal with the experimental falsification slightly; minor editorial tightening recommended.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "P. A. M. Dirac introduced the bra-ket notation in 1939 [Dirac, *Math. Proc. Cambridge Phil. Soc.* 35, 416–418]."
**Claim checked:** Dirac introduced bra-ket notation in a 1939 paper in MPCPS 35, pp. 416–418.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Dirac, P. A. M. "A new notation for quantum mechanics." Math. Proc. Cambridge Phil. Soc. 35, 416–418 (1939). https://doi.org/10.1017/S0305004100021162
**Expert review needed:** No
**Suggested reference:** Dirac, P. A. M. "A new notation for quantum mechanics." Math. Proc. Cambridge Phil. Soc. 35, 416–418 (1939). https://doi.org/10.1017/S0305004100021162
**Notes:** Pagination is correct.

### SPECIALIST — CONFIRMED
**Assertion type:** POSITIVE
**Sentence:** "In infinite dimensions, *Hermitian* and *self-adjoint* are not the same thing — a Hermitian operator might have eigenstates but lack a complete eigenbasis, or fail to admit a unique unambiguous extension to its full domain."
**Claim checked:** Distinction between symmetric (Hermitian on a dense domain) and self-adjoint operators in infinite-dimensional Hilbert space.
**Site visited:** General mathematical-physics reference.
**Finding:** Confirmed. This is the canonical distinction in functional analysis; Reed & Simon Vol. II treats it carefully (Stone's theorem, deficiency indices, von Neumann's extension theory).
**Expert review needed:** No
**Suggested reference:** Reed, M. & Simon, B. *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness*. Academic Press, 1975.
**Notes:** The book mentions Reed & Simon Vol. 2 by name in-text. Good citation discipline.

### SPECIALIST — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "(Bender and Boettcher, 1998)" [referring to PT-symmetric non-Hermitian theories]
**Claim checked:** Bender & Boettcher 1998 paper introducing PT-symmetric non-Hermitian Hamiltonians.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Bender, C. M. & Boettcher, S. "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry." Phys. Rev. Lett. 80, 5243 (1998).
**Expert review needed:** No
**Suggested reference:** Bender, C. M. & Boettcher, S. "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry." Phys. Rev. Lett. 80, 5243 (1998). https://doi.org/10.1103/PhysRevLett.80.5243
**Notes:** None.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "(Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995)"
**Claim checked:** Adler's quaternionic QM monograph.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Adler, S. L. *Quaternionic Quantum Mechanics and Quantum Fields*. Oxford UP, 1995.
**Expert review needed:** No
**Suggested reference:** Adler, S. L. *Quaternionic Quantum Mechanics and Quantum Fields*. Oxford University Press, 1995.
**Notes:** None.

---

## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
| "Ballentine *Quantum Mechanics: A Modern Development* Ch. 1 handles it carefully." | reference pointer | BASIC | Pointer to a specific chapter of a real textbook; verify against the actual edition the book recommends. Ballentine 2nd ed. (2014) Ch. 1 does treat the rigged Hilbert space construction. |

---

## AI-Pass Flags
- The chapter's strongest factual claim — that complex amplitudes are *measured* not conventionally chosen — rests on Renou et al. 2021 (theoretical Bell-test design) plus subsequent experimental implementations (Li et al. 2022, Chen et al. 2022). The book cites only Renou et al. and credits them with the experimental ruling-out. Strictly that paper is the theoretical proposal; the actual experimental falsifications came in 2022. Tightening this to "Renou et al. 2021 designed the test; Li et al. and Chen et al. 2022 implemented it and ruled out real-amplitude QM" would be more accurate.
- The "(1/√2)" symmetric assignment in the double-slit calculation (line 47–49) implicitly assumes equal amplitudes from each slit. Fine for the toy calculation, but worth noting that real double-slit experiments have asymmetric amplitudes when one slit is partially blocked.
