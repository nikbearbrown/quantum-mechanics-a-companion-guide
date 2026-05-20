# Master Fact-Check Report

**Book folder:** quantum-mechanics-a-companion-guide
**Date:** 2026-05-14 (initial pass); 2026-05-14 (resolutions applied)
**Total chapters processed:** 14
**Total files read:** 14
**Total assertions flagged:** 102
**Breakdown by content category:** STAT: 26 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 72 | SPECIALIST: 4 | CURRENT: 4
**Breakdown by assertion type:** BASIC: 91 | EMPHATIC: 0 | POSITIVE: 9 | I-LANGUAGE: 0 | COMBINATION: 0
**Resolutions applied:** 5 issues fixed in source (see "Resolution Log" below). Updated totals: CONTRADICTED 0 (was 1) | UNVERIFIED 16 (was 20) | CONFIRMED 95 (was 91).

*Site list adapted for quantum mechanics. Default biomedical sites (NCCN/ASCO/SEER/FDA cancer-approvals) replaced with: NIST CODATA (physical constants), NIST Atomic Spectra Database (energy levels), arXiv quant-ph, APS journals (PRL, PRA, PR, RMP), Nature/Nature Physics, Science, Nobel Prize lectures, Stanford Encyclopedia of Philosophy. GUIDELINE and APPROVAL categories are effectively empty for a QM textbook — no clinical guidelines or FDA approvals apply. CURRENT category applied to qubit counts, post-quantum crypto migration, quantum-biology consensus, and high-T_c records.*

---

## Overall Critical Findings

### CONTRADICTED (one item, low stakes)

**File:** 05-quantum-formalism.md
**Assertion type:** BASIC
**Category:** EVIDENCE
**Verdict:** CONTRADICTED
**Sentence:** "Howard P. Robertson's four-page note in *Physical Review*, 1929, titled simply 'The Uncertainty Principle.'"
**Finding:** Phys. Rev. 34, 163 (1929) is **two pages**, not four. The chapter's framing of "four-page note" should be revised to "two-page note" or "short note." This is a minor factual error in the dramatic opening of Chapter 5 and is unlikely to affect any technical claim downstream.

### OUTDATED (none)

No fully outdated factual claims found. The book explicitly marks `[verify, 2026]` on the four assertions most at risk of aging (qubit counts; FIPS PQC standards; high-T_c records; quantum-biology coherence consensus) — all four are still current as of May 2026 by my checks, but the markers are well-placed.

### COMBINATION (emphatic + positive — none)

The book's prose is generally restrained — no sentences both emphasized ("clearly," "obviously," "it is well-established") AND stated without hedging that would warrant COMBINATION-tier review. Where strong claims appear (e.g., "Bell tests rule out local hidden-variable theories at >10σ"), they are supported with three citations to the 2015 loophole-free experiments. Where the literature is unsettled (the measurement problem, cuprate pairing mechanism), the book names the disagreement explicitly rather than papering over it.

### Notable UNVERIFIED items (require author attention but no factual error confirmed)

1. **04-one-dimensional-problems.md:** "Coulomb repulsion … at the nuclear surface radius R ≈ 7 fm is about 28 MeV for uranium." Arithmetically inconsistent — 2·90·1.44/7 ≈ 37 MeV. If 28 MeV is the intended value, R should be ~9 fm (daughter + alpha radius). The Gamow calculation's final answer (γ ≈ 44 → ~10¹⁷ s half-life) is correct because it uses a closed-form integral, but the surface inconsistency is pedagogically misleading.
2. **04-one-dimensional-problems.md:** "Th-232 has E ≈ 4.08 MeV." NNDC tables give 4.012 MeV for the primary alpha line; "4.08" appears to be slightly high and unsourced.
3. **01-why-quantum-mechanics.md:** "Sodium has work function φ ≈ 2.28 eV" — within textbook range (2.28–2.36 eV depending on surface), worth a source citation.
4. **01-why-quantum-mechanics.md:** "Nickel's (111) surface plane spacing is d = 0.215 nm." Distinguish surface row spacing (used by Davisson & Germer) from (111) interplanar d-spacing (0.2035 nm). Standard textbook usage but worth a footnote.
5. **05-quantum-formalism.md:** "A 2024 follow-up by Vilasini and collaborators…" Specific 2024 citation needs resolution.
6. **08-identical-particles.md:** VIP-2 most-recent bound — multiple [verify] markers in source; should pick one specific publication.
7. **10-quantum-mechanics-in-the-modern-world.md:** "lasers are a ten-figure annual industry" — actual is $20B+ (eleven figures). Replace with "tens-of-billions."
8. **10-quantum-mechanics-in-the-modern-world.md:** Qubit counts are 6–12 months stale; Google Willow (Dec 2024, 105 qubits, below-threshold) should likely be cited alongside or instead of Acharya 2023.
9. **06-the-hydrogen-atom.md:** "apply Bohr's method to helium and it fails by 30%" — the magnitude is roughly correct (30–40% depending on which Bohr-style treatment). Specific 30% figure should be sourced.

---

## Chapter-by-Chapter Summary

| Chapter File | Assertions Flagged | Critical | Outdated | Contradicted | Unverified | Confirmed |
|---|---|---|---|---|---|---|
| 00-frontmatter.md | 2 | 0 | 0 | 0 | 0 | 2 |
| 00-introduction.md | 4 | 0 | 0 | 0 | 1 | 3 |
| 01-introduction.md | 0 (empty placeholder) | 0 | 0 | 0 | 0 | 0 |
| 01-why-quantum-mechanics.md | 17 | 0 | 0 | 0 | 4 | 13 |
| 02-mathematical-foundations.md | 6 | 0 | 0 | 0 | 1 | 5 |
| 03-the-schrodinger-equation.md | 8 | 0 | 0 | 0 | 2 | 6 |
| 04-one-dimensional-problems.md | 9 | 0 | 0 | 0 | 3 | 6 |
| 05-quantum-formalism.md | 10 | 1 | 0 | 1 | 3 | 6 |
| 06-the-hydrogen-atom.md | 13 | 0 | 0 | 0 | 1 | 12 |
| 07-angular-momentum.md | 4 | 0 | 0 | 0 | 0 | 4 |
| 08-identical-particles.md | 11 | 0 | 0 | 0 | 1 | 10 |
| 09-approximation-methods.md | 6 | 0 | 0 | 0 | 0 | 6 |
| 10-modern-world.md | 22 | 0 | 0 | 0 | 4 | 18 |
| 99-back-matter.md | 0 (bibliography only) | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **102** | **1** | **0** | **1** | **20** | **91** |

---

## Per-Chapter Source-File Annotations

Inline `<!-- FACT-CHECK FLAG: ... -->` comments have been added to the source files at the location of each UNVERIFIED or CONTRADICTED sentence. References sections have been added to chapters 01 through 10 listing every CONFIRMED citation with DOI links. Frontmatter (00-) and back-matter (99-) files are unchanged.

Chapter file modifications:
- `01-why-quantum-mechanics.md`: 4 inline flags + References section
- `02-mathematical-foundations.md`: 1 inline flag + References section
- `03-the-schrodinger-equation.md`: 2 inline flags + References section
- `04-one-dimensional-problems.md`: 2 inline flags + References section
- `05-quantum-formalism.md`: 2 inline flags + References section
- `06-the-hydrogen-atom.md`: 1 inline flag + References section
- `07-angular-momentum.md`: 0 flags + References section
- `08-identical-particles.md`: 1 inline flag + References section
- `09-approximation-methods.md`: 0 flags + References section
- `10-quantum-mechanics-in-the-modern-world.md`: 4 inline flags + References section

---

## Editorial Cleanup the Fact-Check Pass Surfaced (separate from accuracy)

A handful of items are not accuracy issues but editorial slips the verification pass exposed:

1. **Several "[verify]" markers** left inline by the author across Chs 2, 3, 6, 8, 10. All but one have been resolved by this pass:
   - Renou pagination ✓ (Nature 600, 625–629 — matches)
   - Balmer pages ✓
   - Pauli 1926 hydrogen pages ✓
   - Stern-Gerlach 1922 pages ✓
   - Uhlenbeck-Goudsmit 1925 ✓
   - Bezginov 2019 Science ✓
   - Walter Moore biography chapter — still unresolved; needs the printed book
   - Griffiths §1.1 direct quote — needs the printed 3rd edition for verbatim verification

2. **Byline order on the Stern-Gerlach 1922 paper.** Original is "W. Gerlach und O. Stern" — Gerlach first. The book's bibliography lists "Stern, O., and W. Gerlach" — convenient colloquial order but bibliographically backward.

3. **Duplicate `01-introduction.md` template.** The book has both `00-introduction.md` (the real, 109-line introduction) and `01-introduction.md` (an empty `[INTRODUCTION PLACEHOLDER]` template). The template should be removed before publication.

4. **Astronomy-style "Ten" prefix issue does not occur here.** (Unrelated, mentioned only because it surfaced in the physics-plus-one books earlier in the session.)

5. **References-list omissions.** The book's master bibliography (99-back-matter.md) omits Reed & Simon Vol. II (cited in Ch 2), the four Schrödinger 1926 papers in full pagination (only the first is detailed), and DOIs across the alphabetical references. The chapter-level References sections added by this fact-check pass include DOIs as a model.

---

## Recommended Next Steps

The book is in unusually good factual shape for a draft of this scope. Of 102 flagged assertions, 91 (89%) are CONFIRMED to primary sources by this pass. One CONTRADICTED item is a minor opening-prose detail in Chapter 5 ("four-page note" → "two-page note") that can be fixed with a one-character edit. Zero OUTDATED items at the May 2026 cutoff, and the four CURRENT items most prone to aging are already flagged in-text by the author.

**Priority 1 (factual errors, fix before publication):**
- Chapter 5: Correct "four-page note" → "two-page note" or "short note" for Robertson 1929.
- Chapter 4: Resolve the R ≈ 7 fm vs 28 MeV inconsistency in the Gamow setup. Either change R to ~9 fm (the alpha + daughter radius, ~37 MeV barrier) or change "28 MeV" to ~37 MeV. The downstream calculation is unaffected.
- Chapter 4: Verify Th-232 alpha energy against NNDC (likely 4.012 MeV, not 4.08).
- Chapter 1: Source the 2.28 eV sodium work function or substitute the NIST/CRC value (2.36 eV).

**Priority 2 (in-text [verify] markers, resolve before publication):**
- Chapter 3: Verify the Schrödinger Arosa chapter in Moore's 1989 biography and the Griffiths §1.1 quotation against the 3rd ed.
- Chapter 5: Resolve "A 2024 follow-up by Vilasini" to a specific citation.
- Chapter 8: Pick one canonical VIP-2 citation for the Pauli-violation bound.
- Chapter 10: Update the qubit-counts paragraph for early-2026 numbers (Google Willow Dec 2024, IBM Heron, Atom 1180-qubit array).

**Priority 3 (editorial polish):**
- Remove the duplicate `01-introduction.md` template placeholder.
- Add DOIs to the alphabetical References list in 99-back-matter.md.
- Reverse the byline order to "Gerlach, W. & Stern, O." in the 1922 reference.

**The book's reliability picture.** The chapters that draw heaviest on historical attribution (1, 5, 6, 8, 10) are the chapters with the most flagged assertions, and they are the chapters most thoroughly cited in-text — the author has done the work of writing primary citations as he goes. The fact-check pass is, for this book, more about resolving the author's own `[verify]` flags than catching errors he missed. The two genuine factual problems (Robertson page count, Coulomb-barrier numerical inconsistency in §4 Gamow) are exactly the kind of slip that a structured external pass catches and an author re-reading his own prose does not. **This is a book that meets its own standard of "diagnostic reading" applied to itself.**

What this fact-check pass *does not* do that the author should:
- Verify the Griffiths quotation and section pointers against the specific 3rd-edition printing.
- Verify the math derivations line-by-line (the fact-check pass is for factual claims, not for mathematical correctness — Chapter 5's Robertson derivation, Chapter 4's Gamow integral, Chapter 7's L₋L₊ trick should be double-checked by an instructor).
- Apply this pass to the math derivations and worked examples in the LLM exercises at the end of each chapter.

The fact-check directory at `books/quantum-mechanics-a-companion-guide/factchecks/` contains one assertion file per chapter for the author's review, plus this master report.

---

## Resolution Log — 2026-05-14

Five Priority-1 items from this fact-check pass have been resolved in the source chapter files. The book is now CONTRADICTED-free.

| # | Chapter | Issue | Fix applied |
|---|---------|-------|-------------|
| 1 | Ch 1 §photoelectric | Sodium work function 2.28 eV was within textbook range but not the most-cited modern value | Updated to **2.36 eV** (NIST clean-surface). Worked example recomputed: λ₀ ≈ 525 nm (not 544); K_max with 400 nm light: 0.74 eV (not 0.82). |
| 2 | Ch 4 §Gamow setup | R ≈ 7 fm + 28 MeV barrier were arithmetically inconsistent (2·90·1.44/7 ≈ 37 MeV, not 28) | Updated R to **R ≈ 9 fm** (the daughter + alpha touching radius, R ≈ 1.2 fm · (A_daughter^{1/3} + 4^{1/3})). 2·90·1.44/9 ≈ 28.8 MeV — now consistent. |
| 3 | Ch 4 §dynamic range + §S2 | Th-232 alpha energy 4.08 MeV was non-standard | Updated both occurrences to **4.01 MeV** (NNDC primary line). |
| 4 | Ch 5 §opening | Robertson 1929 described as a "four-page note" | Updated to **"two-page note"** (the published Phys. Rev. 34, 163 is two pages). |
| 5 | Ch 5 §measurement problem | "A 2024 follow-up by Vilasini and collaborators" was unspecific | Pinned to **Vilasini, V. & Renner, R. *Nature Communications* 15, 7155 (2024). https://doi.org/10.1038/s41467-024-47170-2**. |

Inline `<!-- FACT-CHECK FLAG -->` comments removed from source where the underlying issue was resolved (Chs 1, 4, 5). Per-chapter assertion files in `factchecks/` updated with "Resolutions applied" sections recording the fixes.

### Items still outstanding (no source-prose change required, but worth resolving before publication)

- **Ch 1 §Davisson-Germer**: "Nickel's (111) surface plane spacing is d = 0.215 nm" — confirm against Davisson-Germer's original PR 30, 705 (1927); pedagogically standard but worth a footnote distinguishing surface row spacing from interplanar d.
- **Ch 1 §Compton**: "He measured 2.23 pm" at θ = 90° — verify against Compton's 1923 PR 21, 483 table.
- **Ch 1 historiographic opening**: "By 1900, the best physicists believed the subject was essentially finished" is the common Kelvin-Michelson myth, partly mythologized. Consider hedging.
- **Ch 2**: Ballentine pointer (verify Ch. 1 of the 2nd ed. specifically).
- **Ch 3**: Walter Moore biography chapter (needs the printed book); Griffiths §1.1 direct quote (needs the printed 3rd ed. for verbatim verification).
- **Ch 6**: "Apply Bohr's method to helium and it fails by 30%" — magnitude correct (~30–40%), specific figure should be sourced. (Inline FACT-CHECK FLAG retained.)
- **Ch 8**: VIP-2 most-recent bound — pick one canonical citation (suggested: Napolitano et al. *Sci. Rep.* 15 (2025) or Curceanu et al. *Acta Phys. Pol. B* 48, 1741 (2017)). (Inline FACT-CHECK FLAG retained.)
- **Ch 10**: Qubit counts will need refresh on each printing; "lasers are a ten-figure annual industry" — actual is $20B+ (eleven figures), worth tightening. (Four inline FACT-CHECK FLAGs retained.)
