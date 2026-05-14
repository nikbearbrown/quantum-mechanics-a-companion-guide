# Research Notes: Unit 4 — One-Dimensional Problems

**Source:** TIKTOC.md Part IV diagnostic + Recommended Course TOC Unit 4 (line 251–255)
**Notes file:** 04-one-dimensional-problems_notes.md
**Corresponding chapter:** chapters/04-one-dimensional-problems.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

Recommended Course TOC, Unit 4 (lines 252–255):

> - Particle in a box — ❌
> - Harmonic oscillator — ❌
> - Finite well and bound states — ❌
> - Tunneling and the WKB approximation — **[BOOK: Ch. 9 for motivation and applications]**

Part IV diagnostic (TIKTOC.md lines 67–80): every topic absent from the pop-sci book *except* quantum tunneling (Ch. 9, marked ✅ — "best coverage in the book; qualitative mechanism solid; WKB not discussed but applications section is excellent"). Transmission coefficient defined qualitatively, formula not given. The Part IV verdict: "Quantum tunneling is the one bright spot — applications (STM, flash memory, fusion, Josephson junctions, radioactive decay) are listed with enough detail to motivate the topic. Everything else is absent."

**Companion's job for Unit 4:** supply the math the pop-sci book skips (boxes, oscillators, wells, transmission formulas), let the pop-sci book do what it does well (motivate tunneling applications), and route every section to the parallel Griffiths section so the student can read both books with one eye on each.

---

## A. Conceptual foundations

### A1. The infinite square well (particle in a box)

The simplest bound system in quantum mechanics: a particle confined to 0 ≤ x ≤ L by infinite walls. Outside the box, ψ(x) = 0 (the particle cannot be there). Inside, the time-independent Schrödinger equation reduces to the free-particle form, and the boundary conditions ψ(0) = ψ(L) = 0 quantize the allowed energies.

The stationary-state solutions are ψ_n(x) = √(2/L) sin(nπx/L) with energies E_n = n²π²ℏ²/(2mL²), for n = 1, 2, 3, .... Griffiths Ch. 2.2 (4th ed.) walks the derivation step by step: separation of variables, the general solution A sin(kx) + B cos(kx), boundary condition at x=0 forcing B=0, boundary condition at x=L quantizing k = nπ/L, normalization fixing A = √(2/L).

Two structural lessons the box teaches before the student has met anything harder. First: confinement quantizes. The wall is a boundary condition; the boundary condition selects a discrete set of wavelengths; the discrete wavelengths produce a discrete energy spectrum. The "quantum" in quantum mechanics is, very often, a standing-wave constraint dressed up in operator language. Second: the ground state has nonzero energy. E₁ = π²ℏ²/(2mL²) — the particle is never at rest. This zero-point energy is not a quirk of the box. It is the uncertainty principle made arithmetic: confining a particle to a finite region forces its momentum spread to be at least of order ℏ/L, which forces its kinetic energy to be at least of order ℏ²/(mL²).

**Misconception to correct:** "n=0 is the ground state, with E=0." No. Setting n=0 gives ψ ≡ 0 everywhere, which is not a valid quantum state — it cannot be normalized, and a particle that has zero probability of being anywhere is not a particle. The ground state is n=1, with strictly positive E₁. The student who memorizes "energy levels go as n²" without understanding why n starts at 1 will eventually try to compute thermodynamic quantities by summing from n=0 and get the wrong answer.

**Worked example (for chapter):** probability of finding the particle in the central third of the box (L/3 ≤ x ≤ 2L/3) in the n=1 state versus the n=2 state. Direct integral of |ψ_n|². For n=1, the wave function is largest in the middle, so the central third carries more than 1/3 probability (≈ 0.609). For n=2, the wave function has a node at the center, so the central third carries less than 1/3 probability (≈ 0.196). This is the kind of thing the student should be able to do by hand by the end of the unit. Griffiths Problem 2.4 gives a closely related calculation; Solution Manual (4th ed.) carries the worked steps.

**Sources:** Griffiths *Introduction to Quantum Mechanics* (4th ed.) §2.2 — canonical undergraduate derivation. Liboff §4.4 — alternate exposition.

### A2. The quantum harmonic oscillator

The harmonic oscillator is the most reused mechanism in physics. Any smooth potential V(x) near a stable minimum looks quadratic — V(x) ≈ V(x₀) + ½V″(x₀)(x−x₀)² — so molecular vibrations, lattice phonons, photons in a cavity, and small oscillations of fields all reduce to harmonic oscillators in their first nontrivial approximation. Learn this one system well and you have learned half of modern physics.

Two ways to solve it, and the chapter should show both. The **analytic method** (Griffiths §2.3.2) substitutes ψ(x) = h(x) exp(−mωx²/2ℏ) into the Schrödinger equation, derives a recursion relation for the coefficients of h(x), and shows that the series must terminate to keep ψ normalizable. The terminating polynomials are the Hermite polynomials H_n(ξ), and termination at degree n fixes the energy E_n = (n + ½)ℏω.

The **algebraic method** (Griffiths §2.3.1) introduces the ladder operators a₊ = (−ip̂ + mωx̂)/√(2ℏmω) and a₋ = (ip̂ + mωx̂)/√(2ℏmω), which obey [a₋, a₊] = 1. The Hamiltonian becomes H = ℏω(a₊a₋ + ½). One then shows a₊ raises any energy eigenstate by ℏω and a₋ lowers it by ℏω; demanding a₋ψ_0 = 0 (you cannot go below the ground state) fixes ψ_0 as a Gaussian and gives the ground-state energy E_0 = ℏω/2. All higher states follow by applying a₊ repeatedly. Dirac introduced this method in *The Principles of Quantum Mechanics* (1930) — the factorization of the Hamiltonian is the move.

The two methods agree on E_n = (n + ½)ℏω, and they agree that the ground state has nonzero zero-point energy ℏω/2 — the oscillator never sits still, for the same uncertainty-principle reason the box has nonzero E₁.

**Misconception to correct:** "ladder operators are just a mathematical trick to avoid solving the differential equation." This sells the algebra short. The operators a₊ and a₋ have direct physical meaning — they create and destroy quanta of vibration. In the quantization of the electromagnetic field, the analogous operators create and destroy photons. The harmonic-oscillator algebra is not a shortcut; it is the prototype for second quantization. A student who learns it as a trick will be surprised when, in a later course, the same letters appear in a paper on quantum optics or QFT. (Lahiri & Pal *A First Book of QFT* opens its photon chapter exactly here.)

**Worked example (for chapter):** compute ⟨x²⟩ and ⟨p²⟩ in the n-th eigenstate using ladder operators (Griffiths Example 2.5). Result: ⟨x²⟩⟨p²⟩ = (n + ½)²ℏ² — saturates the Robertson uncertainty bound only for n=0. This worked example does double duty: it teaches the algebraic technique and sets up the rigorous uncertainty principle in Unit 5.

**Sources:** Griffiths §2.3 (both methods presented in parallel — the pedagogical model the companion should follow). Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930) — historical source for the algebraic method.

### A3. Bound states, scattering states, and the finite square well

The finite square well — V(x) = −V₀ for |x| ≤ a and V(x) = 0 otherwise — looks like a small modification of the infinite well but teaches two ideas the infinite well cannot. First: the distinction between **bound states** (E < 0, particle localized, discrete spectrum) and **scattering states** (E > 0, particle free at infinity, continuous spectrum). Second: the wave function leaks into the classically forbidden region. Outside the well, where E < V, the Schrödinger equation gives exponentially decaying solutions ψ(x) ∝ exp(−κ|x|) with κ = √(2m|E|)/ℏ. The particle has nonzero probability of being found where it "shouldn't" be.

Bound-state energies are determined by a transcendental equation — matching ψ and ψ′ at x = ±a yields conditions like z tan(z) = √(z₀² − z²) for even-parity states (where z = ka and z₀² = 2mV₀a²/ℏ²). The number of bound states is finite and depends on the dimensionless depth z₀. A shallow well always has at least one bound state in 1D — this is a special feature of one dimension and does *not* generalize to 3D, where a sufficiently shallow well has none. Worth flagging.

**Misconception to correct:** "the particle cannot exist outside the classically forbidden region." It can. The wave function is exponentially suppressed there, not zero. This is the *mechanism* of tunneling. The pop-sci book (Ch. 9) describes tunneling without ever showing this. The companion should show the exponential tail explicitly with a small calculation: at distance d into the barrier, |ψ|² is suppressed by a factor exp(−2κd). Pick numbers (electron, V₀ − E = 1 eV, d = 1 nm) and the suppression is ~e^(−10) ≈ 5×10^(−5). Small, but not zero. STMs read out signals at exactly these suppression levels.

**Sources:** Griffiths §2.6 (finite square well, bound states) and §2.7 (scattering, delta-function potential). Liboff Ch. 7 for an alternate route through the same material.

### A4. Tunneling and the WKB approximation

The pop-sci book's Ch. 9 is, per TIKTOC, the best chapter in the book — qualitative tunneling mechanism is solid, application catalog (STM, flash memory, fusion, Josephson junctions, alpha decay) is excellent for motivation. What it does not do is the math. The companion supplies it.

For a rectangular barrier of height V₀ and width L, with particle energy E < V₀, the transmission coefficient is
T = [1 + (V₀²/(4E(V₀−E))) sinh²(κL)]^(−1) where κ = √(2m(V₀−E))/ℏ.
In the thick-barrier limit κL ≫ 1, this collapses to T ≈ 16(E/V₀)(1 − E/V₀) exp(−2κL). The exponential is what controls everything: T is exponentially sensitive to barrier width and to √(V₀ − E). Halve the barrier width and T grows by a factor of e^(κL) — orders of magnitude. This is why STMs see atomic resolution from a tip held nanometers above a surface: a small change in distance produces a large change in tunneling current.

For barriers that are not rectangular, the **WKB approximation** (Wentzel-Kramers-Brillouin, 1926) generalizes: T ≈ exp(−2γ) where γ = ∫√(2m(V(x) − E))/ℏ dx, integrated across the classically forbidden region. WKB is semiclassical — it works when V(x) varies slowly compared to the local de Broglie wavelength — and it is the workhorse for any tunneling calculation involving a non-rectangular barrier. Griffiths Ch. 9 develops WKB and applies it. (Note: Griffiths' WKB chapter is the natural place to read this, but the pop-sci book's Ch. 9 application list is the natural place to motivate it. The two read in tandem.)

**Misconception to correct:** "tunneling is rare." It is exponentially suppressed for thick barriers, but for thin barriers, atomic-scale events, or particles with energies just below the barrier, it is the dominant transport mechanism. Alpha decay rates span tens of orders of magnitude — from microseconds (Po-212) to 10^17 years (Th-232) — entirely from small changes in barrier-integral γ. Gamow showed this in 1928. The lesson: exponentials are merciless. A small input change is a big output change.

**Sources:** Griffiths §2.7 (delta barrier, transmission), Ch. 9 (WKB). For applications: Binnig & Rohrer, "Scanning Tunneling Microscopy — from Birth to Adolescence," Nobel Lecture, 1986 ([https://www.nobelprize.org/uploads/2018/06/binnig-lecture.pdf](https://www.nobelprize.org/uploads/2018/06/binnig-lecture.pdf)). Original STM paper: G. Binnig, H. Rohrer, Ch. Gerber, E. Weibel, "Surface Studies by Scanning Tunneling Microscopy," *Physical Review Letters* 49, 57 (1982).

---

## B. Domain examples and cases

### B1. Gamow's 1928 alpha-decay calculation (success)

George Gamow submitted "Zur Quantentheorie des Atomkernes" to *Zeitschrift für Physik* on 29 July 1928 (independently, Gurney and Condon submitted a parallel explanation in *Nature* the next day). The puzzle: alpha particles emitted by uranium have energies ~4 MeV, far less than the Coulomb barrier they would classically need to escape (~25 MeV). Classically forbidden. Quantum-mechanically, the WKB integral across the Coulomb barrier gives a transmission probability whose logarithm scales as Z/√E. Combining this with a "knock rate" of the alpha against the barrier wall reproduces the Geiger-Nuttall empirical law that had related alpha energy to half-life across 24 orders of magnitude. This is the first major quantitative match between a quantum-mechanical tunneling calculation and an experimental observable. Cite as the historical anchor of the unit. ([Physics Today: "The Early History of Quantum Tunneling"](https://physicstoday.aip.org/features/the-early-history-of-quantum-tunneling))

### B2. Scanning tunneling microscope (modern application)

Binnig and Rohrer at IBM Zürich saw atomic-resolution images on the night of 16 March 1981. Their 1982 *Physical Review Letters* paper formally announced the result; the 1986 Nobel Prize followed. The STM exploits the exponential sensitivity of T to barrier width: a metal tip held ~0.5 nm above a conducting surface, biased at ~1 V, draws a tunneling current of order nA. A 0.1 nm change in tip-sample distance changes the current by roughly a factor of 10. Feedback loop holds current constant, tip height becomes a topographic map. This is the worked-example version of why exponentials matter. The pop-sci book lists STM as an application; the companion shows the student that "atomic resolution" follows from "exponential dependence on distance."

### B3. Vibrational spectroscopy as harmonic oscillator (worked example)

A diatomic molecule near its equilibrium bond length is a harmonic oscillator with effective spring constant k = V″(r₀) and reduced mass μ. Energy levels E_n = (n + ½)ℏω, with ω = √(k/μ). For HCl, the measured fundamental IR absorption is at ~2886 cm⁻¹, corresponding to ℏω ≈ 0.358 eV. The companion should run the calculation: from the IR line, derive k; from k and the masses, predict the next overtone (at 2ω, with anharmonic correction); compare to the observed first overtone at ~5668 cm⁻¹. The 50 cm⁻¹ discrepancy is the anharmonic correction — the bond is not actually a perfect spring — and this teaches both the power and the limit of the harmonic approximation. [Numbers above are textbook-standard but should be confirmed against a primary spectroscopic source: NIST Chemistry WebBook is the canonical reference for HCl IR — verify exact line position before citing.]

### B4. Failure case: 1D models do not predict scattering lifetimes in 3D

A clean failure mode worth flagging in the chapter. The finite square well in 1D always has at least one bound state. The same well in 3D, expressed as a spherical square well of radius a and depth V₀, has a bound state only if V₀a² exceeds a critical value (Griffiths §4.1.3). A student who has only seen 1D problems may conclude "any attractive potential binds." It is true in 1D, false in 3D. The companion should name this explicitly, both as preparation for Unit 6 (hydrogen atom in 3D) and as a Feynman move — naming where the simpler model stops mapping. Source: Griffiths §4.1.3.

---

## C. Connections and dependencies

**Prerequisites:** Unit 2 (mathematical foundations — Hilbert space, operators, eigenvalues) and Unit 3 (Schrödinger equation, normalization, stationary states). Without those, the student cannot read ψ_n(x) = √(2/L) sin(nπx/L) as a wave function in a Hilbert space — only as a sine wave.

**Unlocks:** Unit 5 (the worked examples here become the worked examples on which uncertainty, commutators, and measurement get tested rigorously). Unit 6 (hydrogen atom is the 3D analog — central potential separates into radial and angular parts, the radial part is a 1D problem dressed in spherical coordinates). Unit 9 (perturbation theory and variational methods use the harmonic oscillator and the infinite well as the unperturbed systems on which everything is built). Unit 10 applications (STM, flash memory, Josephson junctions, semiconductor heterostructures) all use Unit 4 mechanisms.

**Adjacent:** Solid-state physics (Kronig-Penney model = periodic square wells; Bloch's theorem extends the box). Statistical mechanics (Planck's law is a sum over harmonic-oscillator modes). Quantum field theory (every mode of every field is a harmonic oscillator; ladder operators become creation/annihilation operators for particles).

---

## D. Current state of the field

**Settled:** The exact solutions for box, oscillator, finite well, and step/barrier are textbook material a century old. No physicist disputes them; they are taught the same way (modulo notation) at every university. WKB is a standard tool; transmission formulas have been confirmed experimentally to many decimal places (STM tunneling currents, alpha-decay rates).

**Contested:** Almost nothing within Unit 4 itself. The interpretation of the wave function (Born rule vs. ensemble vs. epistemic) is a Unit 5 question, not a Unit 4 question. The student does Unit 4 calculations the same way regardless of interpretation.

**Recent developments (last 3 years, for instructor flavor — not chapter required):** Experimental tunneling-time measurements ("how long does the particle spend in the barrier?") have produced new results using attosecond ionization techniques. The interpretation of "tunneling time" is still under debate — multiple definitions (Wigner time, Larmor time, Büttiker-Landauer time) give different answers. Sainadh et al., *Nature* 568, 75 (2019), reported attoclock measurements consistent with zero tunneling time in hydrogen, contradicting earlier helium results. Active area; the companion should mention this only as "the textbook calculation gives transmission probability, not transit time, and the latter is still researched." [verify exact citation of Sainadh et al. before including in chapter]

**References:**
- Griffiths, D. J. *Introduction to Quantum Mechanics*, 4th ed. (Cambridge University Press, 2018). Chapters 2 (one-dimensional problems) and 9 (WKB). Primary reference for the chapter.
- Griffiths *Solution Manual*, 4th ed. — pull worked examples 2.4, 2.5, 2.10, 2.27, 9.7.
- Dirac, P. A. M. *The Principles of Quantum Mechanics*, 1st ed. (Oxford, 1930). Historical source for ladder-operator method.
- Gamow, G. "Zur Quantentheorie des Atomkernes," *Zeitschrift für Physik* 51, 204 (1928). Submitted 29 July 1928. Historical source for alpha-decay tunneling. [verify page numbers against original]
- Gurney, R. W., and Condon, E. U. "Quantum Mechanics and Radioactive Disintegration," *Nature* 122, 439 (1928). Independent contemporaneous derivation.
- Binnig, G., and Rohrer, H. "Scanning Tunneling Microscopy — from Birth to Adolescence," Nobel Lecture, 8 December 1986. [https://www.nobelprize.org/uploads/2018/06/binnig-lecture.pdf](https://www.nobelprize.org/uploads/2018/06/binnig-lecture.pdf)
- Binnig, G., Rohrer, H., Gerber, Ch., and Weibel, E. "Surface Studies by Scanning Tunneling Microscopy," *Physical Review Letters* 49, 57 (1982). DOI: 10.1103/PhysRevLett.49.57.

---

## E. Teaching considerations

**Where students stick:**
1. Why ψ must vanish at the walls of the infinite well. The honest answer: continuity of ψ across the boundary plus ψ = 0 outside (because V = ∞ there). The cheap answer is "boundary condition." The honest answer is the one that teaches.
2. Why E_n = n²π²ℏ²/(2mL²) rather than nπℏ/L or some other dimensionally adjacent combination. Dimensional analysis check on the page builds confidence.
3. The two solution methods for the harmonic oscillator. Students often pick one and ignore the other. The companion should force both, in parallel, and show explicitly that they agree.
4. The boundary-matching algebra for the finite square well. The transcendental equation looks like nothing they have seen. The companion should solve it graphically (plot LHS and RHS, intersections give energies) before solving it numerically.
5. The leap from "rectangular barrier" to "general WKB." Students learn the rectangular formula and assume it covers everything. The integral form ∫√(2m(V−E))/ℏ dx needs explicit demonstration on a non-rectangular barrier (Coulomb, linear ramp).

**Analogies that work:**
- Particle in a box ↔ standing waves on a guitar string (Griffiths uses this; sound). The discrete frequencies are the quantization. Note where the analogy ends: the string has no probability interpretation, just amplitude.
- Tunneling ↔ a ball that, for no classical reason, occasionally appears on the other side of a wall (Feynman's gloss). Works for motivation; fails for mechanism. The mechanism is wave-function leakage, not a particle "deciding" to penetrate.

**Analogies that mislead:**
- "The particle is a little ball bouncing around in the box." Wrong; the particle is the wave function. The probability density is the bouncing-around object, and it has nodes (places of zero probability) that no classical ball has.
- "Ladder operators are like raising and lowering volume on a stereo." Misses that they change the number of quanta in a state, not just an amplitude. Better to say "they add or remove one unit of vibration."

**Exercises with Bloom's levels:**
1. *Remember.* State the energy levels of (a) infinite well, (b) harmonic oscillator. [Warm-up.]
2. *Understand.* Sketch ψ_n and |ψ_n|² for n = 1, 2, 3 in the infinite well. Identify nodes.
3. *Apply.* Compute the probability of finding the n=2 particle in the left third of the box. [Worked-example level.]
4. *Apply.* Use ladder operators to compute ⟨x²⟩ and ⟨p²⟩ for the n-th oscillator state. [Connects to Unit 5.]
5. *Analyze.* For a finite square well of depth V₀ and width 2a, derive the transcendental equation determining the energies of even-parity bound states. Solve graphically for one specific (V₀, a) pair.
6. *Apply / synthesize.* Compute the WKB transmission for a particle of energy E through a rectangular barrier of height V₀ and width L. Then redo it for a triangular barrier (V(x) linear from V₀ at x=0 to 0 at x=L). Compare.
7. *Analyze / evaluate.* Estimate the half-life of an alpha emitter using the Gamow factor. Compare with measured half-life for one isotope (Po-212 or U-238). Discuss why agreement is at the order-of-magnitude level. [Synthesis exercise tying tunneling math to historical case B1.]
8. *Evaluate.* Read the pop-sci book's Ch. 9 description of tunneling. Identify two statements that are correct, two that are imprecise, and one that would be wrong without the mathematics from this chapter. [The "companion-guide" exercise.]

---

## F. Library files relevant to this unit

- `_lib_QM-Into-the-Light-Beginners.md` — the pop-sci audit target; Ch. 9 is the relevant chapter. The companion explicitly fills the math gap diagnosed in TIKTOC Part IV.
- `_lib_Significant-Figures-Stewart.md` — possibly contains historical material on Gamow / alpha decay; check for biographical sketches.
- `_lib_Penrose-Emperors-New-Mind.md` — Penrose discusses harmonic-oscillator and oscillator-mode arguments; check for any tunneling-rate discussion (Penrose has views on biological tunneling that should be flagged as speculative, not standard).
- Not relevant to this unit: `_lib_The-Blind-Spot.md`, `_lib_Davies-Demon-in-the-Machine.md`, `_lib_Nielsen-Reinventing-Discovery.md` (those connect more to Units 5, 6, 10).

---

## G. Gaps and flags

1. **Numbers for the HCl worked example** (B3) need confirmation against NIST Chemistry WebBook or a primary spectroscopy text before the chapter cites them. `[verify]` flag in draft.
2. **Tunneling-time experimental results** (Sainadh et al. 2019) — citation should be confirmed against the published *Nature* article; the field has moved since and the chapter should not overclaim. `[verify]`
3. **Gamow paper page numbers** — *Zeitschrift für Physik* 51, 204 (1928) is the conventional citation but the volume and page should be confirmed against a primary archive (e.g., SAO/NASA ADS) before final draft.
4. **Biological tunneling claims** (proton tunneling in DNA, enzyme kinetics) are contested and the literature is mixed. The pop-sci book lists biology among tunneling applications. The companion should mention it but flag it as "speculated, with active research, not as settled as STM or alpha decay." Cite specifically: Klinman & Kohen reviews on hydrogen tunneling in enzymes are a starting point; check current consensus before chapter draft.
5. **WKB for non-Coulomb barriers** — the integral form is standard but worked examples in standard textbooks tend to use rectangular or Coulomb barriers. The companion's "triangular barrier" exercise (E7) needs the integral worked once on the page so the student has a model.
6. **The pop-sci book's specific framings in Ch. 9** — the companion should quote one or two passages directly (with citation) to show what the math adds. This requires going back into the source text; the audit notes in TIKTOC do not preserve quotations.

---

*Notes assembled 2026-05-13 for Nik's review. Primary text: Griffiths 4th ed., Ch. 2 and Ch. 9. Companion's structural job: math + corrections + tandem-reading map with the pop-sci Ch. 9.*
