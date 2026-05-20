# Assertions Report: 09-approximation-methods.md
**Date:** 2026-05-14
**Source file:** chapters/09-approximation-methods.md
**Assertions flagged:** 6
**Breakdown:** STAT: 1 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 0

---

## ⚠️ Critical — Requires Immediate Expert Review
None found.

---

## Full Findings

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "What Egil Hylleraas published in 1929 was something different: a *variational* calculation. ... With six parameters, Hylleraas reproduced the experimental ground-state energy of helium to four significant figures."
**Claim checked:** Hylleraas 1929 helium calculation.
**Site visited:** https://link.springer.com/article/10.1007/BF01375457
**Finding:** Confirmed. Hylleraas, E. A. "Neue Berechnung der Energie des Heliums im Grundzustande, sowie des tiefsten Terms von Ortho-Helium." Z. Phys. 54, 347–366 (1929). Six-parameter variational wave function in r₁, r₂, r₁₂; energy agreement with experiment to four significant figures.
**Expert review needed:** No
**Suggested reference:** Hylleraas, E. A. Z. Phys. 54, 347 (1929). https://doi.org/10.1007/BF01375457
**Notes:** Earlier Hylleraas 1928 (Z. Phys. 48, 469) used a three-parameter trial function and reached three-significant-figure agreement; the six-parameter 1929 paper is the one the book refers to.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Dirac derived it in 1927. Fermi named it 'Golden Rule No. 2' in his lecture notes."
**Claim checked:** Dirac 1927 derivation; Fermi naming.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Dirac, P. A. M. "The Quantum Theory of the Emission and Absorption of Radiation." Proc. R. Soc. Lond. A 114, 243–265 (1927) contains the derivation. Fermi's *Nuclear Physics* (1950, notes compiled from his 1949–1950 University of Chicago lectures by Orear, Rosenfeld, and Schluter) refers to "Golden Rule No. 2."
**Expert review needed:** No
**Suggested reference:** Dirac, P. A. M. Proc. R. Soc. Lond. A 114, 243–265 (1927). https://doi.org/10.1098/rspa.1927.0039 ; Fermi, E. *Nuclear Physics: A Course Given by Enrico Fermi at the University of Chicago*. U. Chicago Press, 1950.
**Notes:** Worth a one-line citation in the chapter to the Dirac paper.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "Freeman Dyson argued in 1952 that QED perturbation theory must be an asymptotic series with zero radius of convergence."
**Claim checked:** Dyson 1952 argument for QED series divergence.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Dyson, F. J. "Divergence of Perturbation Theory in Quantum Electrodynamics." Phys. Rev. 85, 631–632 (1952). The instability-of-α<0-vacuum argument is precisely as the book describes.
**Expert review needed:** No
**Suggested reference:** Dyson, F. J. Phys. Rev. 85, 631 (1952). https://doi.org/10.1103/PhysRev.85.631
**Notes:** None.

### EVIDENCE — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "The anharmonic oscillator with a λx̂⁴ term has a perturbation series with zero radius of convergence (Bender and Wu showed this in 1969)."
**Claim checked:** Bender-Wu 1969 anharmonic oscillator divergence.
**Site visited:** General physics-history record.
**Finding:** Confirmed. Bender, C. M. & Wu, T. T. "Anharmonic Oscillator." Phys. Rev. 184, 1231–1260 (1969). Established that the perturbation series in λ for x̂⁴ anharmonic oscillator has zero radius of convergence.
**Expert review needed:** No
**Suggested reference:** Bender, C. M. & Wu, T. T. Phys. Rev. 184, 1231 (1969). https://doi.org/10.1103/PhysRev.184.1231
**Notes:** None.

### STAT — CONFIRMED
**Assertion type:** BASIC
**Sentence:** "The experimental value is −79.0 eV. The one-parameter variational result is within 2%."
**Claim checked:** He ground-state energy = −79.0 eV; variational result with Z* = 27/16 gives −77.5 eV, ~2% off.
**Site visited:** NIST ASD.
**Finding:** Confirmed. He ionization energy from ground state = 24.587 eV; double ionization (He²⁺ formation from He ground state) = 79.005 eV. The variational result E_var = −(27/16)² Hartree = −2.848 Hartree = −77.49 eV. Difference: 1.5 eV / 79.0 eV ≈ 1.9% — book's "within 2%" is correct.
**Expert review needed:** No
**Suggested reference:** NIST ASD He I; or any quantum chemistry textbook (Levine, McQuarrie, etc.).
**Notes:** None.

### SPECIALIST — CONFIRMED
**Assertion type:** SPECIALIST (level repulsion claim)
**Sentence:** "the second-order correction to the ground-state energy is always non-positive. This is *level repulsion*"
**Claim checked:** Sign of second-order ground-state correction.
**Site visited:** Standard QM result.
**Finding:** Confirmed. For the ground state, every denominator E_0 − E_m < 0 and every numerator |⟨m|H'|0⟩|² ≥ 0, so each term in E_0^{(2)} = Σ |⟨m|H'|0⟩|²/(E_0−E_m) ≤ 0. Sum is ≤ 0.
**Expert review needed:** No
**Suggested reference:** Griffiths, D. J. *Introduction to Quantum Mechanics*, 3rd ed. §7.1 (perturbation theory).
**Notes:** None.

---

## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
| (none) | | | |

---

## AI-Pass Flags
- The chapter's derivation of Fermi's golden rule is the standard textbook derivation; every step is verifiable in any QM text. The historiographic point that Dirac 1927 derived it and Fermi later named it is correct and worth preserving — many introductory texts omit Dirac's role.
- **Resonance approximation** (line 158): the chapter correctly identifies the rotating-wave approximation as the term-keeping move. Pedagogically clear.
- **Hartree-Fock connection** (line 59 of Ch 8 / line 197 of Ch 9): worth a forward-pointing citation to Hartree 1928 / Fock 1930 for completeness. The chapter mentions HF without citation.
- **Polarizability of hydrogen ground state α = 9a₀³/2**: this is the standard analytical result from second-order perturbation theory. Worth a footnote: derived in Griffiths §7.4 and matches the experimental polarizability 4πε₀ × 4.5 a₀³ ≈ 0.667 × 10⁻²⁴ cm³ measured by Coulter et al. — the book quotes the result without citation, which is fine for a companion guide.
- **Linear Stark effect matrix element** ⟨2s|z|2p_z⟩ = −3a₀: standard result, derivable from Griffiths §6.5 or any atomic-physics text.
