# Research Notes: Unit 09 — Approximation Methods

**Source:** TIKTOC.md Unit 9 entry (lines 281–287), Part IX diagnostic (lines 152–164)
**Notes file:** 09-approximation-methods_notes.md
**Corresponding chapter:** chapters/09-approximation-methods.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 9: Approximation Methods
> - Time-independent perturbation theory — ❌
> - Variational principle — ❌
> - WKB approximation — ❌
> - Time-dependent perturbation theory — ❌
> - Fermi's Golden Rule — ❌

TIKTOC Part IX Verdict: "Entirely absent. This is arguably the most practically important section of any QM course and the book contributes nothing." The pop-sci book gives the companion nothing in this unit — no narrative to borrow, no diagrams, no historical hook. Unit 9 is fully original companion territory. The compensating virtue: approximation methods are where QM stops being an abstract eigenvalue problem and starts producing numbers that match experiments. The companion's job is to make the methods feel like instruments — when to reach for each, what each one tells you, where each one fails.

This is the most math-dense unit in the book. Target ~2,800 words; budget the deep-dive on time-dependent perturbation theory leading to Fermi's golden rule (the formula that powers everything from atomic line widths to nuclear decay rates to scattering cross sections).

---

## A. Conceptual foundations

### 1. Time-independent perturbation theory (non-degenerate)

The setup: an exactly-solvable Hamiltonian Ĥ₀ with known eigenstates |n⁽⁰⁾⟩ and energies E_n⁽⁰⁾, plus a small correction Ĥ′ such that the full Hamiltonian is Ĥ = Ĥ₀ + λĤ′. The parameter λ is a bookkeeping device — it labels the order of the expansion, and at the end you set λ = 1.

Expand the perturbed states and energies in powers of λ:

|n⟩ = |n⁽⁰⁾⟩ + λ|n⁽¹⁾⟩ + λ²|n⁽²⁾⟩ + ...
E_n = E_n⁽⁰⁾ + λE_n⁽¹⁾ + λ²E_n⁽²⁾ + ...

Substitute into Ĥ|n⟩ = E_n|n⟩ and match powers of λ. The results that earn their place in the chapter:

**First-order energy correction:**
E_n⁽¹⁾ = ⟨n⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩

The simplest formula in perturbation theory and the one students will use most often. Sandwich the perturbation between the unperturbed state and read off the energy shift. The reason this works: the first-order correction depends only on the diagonal matrix element of Ĥ′ in the unperturbed basis.

**First-order state correction:**
|n⁽¹⁾⟩ = Σ_{m≠n} (⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩ / (E_n⁽⁰⁾ − E_m⁽⁰⁾)) |m⁽⁰⁾⟩

The state mixes in contributions from every other unperturbed state, weighted by the off-diagonal matrix element of Ĥ′ and divided by the unperturbed energy gap. The smaller the gap, the bigger the mixing — and the more suspicious you should be that perturbation theory is converging.

**Second-order energy correction:**
E_n⁽²⁾ = Σ_{m≠n} |⟨m⁽⁰⁾|Ĥ′|n⁽⁰⁾⟩|² / (E_n⁽⁰⁾ − E_m⁽⁰⁾)

The ground state's second-order correction is always negative (numerator is non-negative, denominator is positive when n is the ground state). This is the *level-repulsion* effect: turning on a perturbation pushes the ground state down and excited states up, the more strongly the closer the unperturbed levels are. Important in solid-state physics (band repulsion at avoided crossings), nuclear physics (level repulsion in random-matrix models), and quantum chemistry.

**Common misconception:** "Perturbation theory always converges if Ĥ′ is small." It does not. Even for the harmonic oscillator with a quartic perturbation x⁴, the perturbation series is asymptotic, not convergent — the series gives excellent results when truncated at the optimal order, then *diverges* if you keep going. Dyson argued in 1952 (*Physical Review* 85, 631–632, "Divergence of Perturbation Theory in Quantum Electrodynamics") that QED perturbation theory must be asymptotic because the vacuum is unstable against pair creation when the coupling is flipped from +e to −e — the series cannot be analytic at α = 0. Bender and Wu (1969, *Physical Review* 184, 1231–1260) showed numerically that the x⁴ oscillator series has zero radius of convergence. The companion should say this plainly: perturbation theory is an asymptotic expansion that is useful precisely because the first few terms are accurate, not because the full series is.

**Worked example:** First-order Stark effect on the hydrogen ground state — zero. The 1s state has no electric dipole moment because it is spherically symmetric, so ⟨1s|eẑ E|1s⟩ = 0. The Stark effect on hydrogen 1s appears at *second* order, scaling as E². Compute it (Griffiths Ch. 6 has the calculation) and compare to experiment. For the n = 2 manifold of hydrogen, the linear Stark effect *does* appear, because the 2s and 2p_z levels are degenerate and the perturbation mixes them — this is degenerate perturbation theory (see below).

**Sources:**
- Griffiths, D. J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Ch. 6, "Time-Independent Perturbation Theory."
- Sakurai and Napolitano (2017), Ch. 5.1–5.2 — more rigorous treatment with explicit projection operators.
- Bender, C. M. and Wu, T. T. (1969). "Anharmonic Oscillator." *Physical Review* 184, 1231–1260.

### 2. Degenerate perturbation theory

When two or more unperturbed states |a⁽⁰⁾⟩ and |b⁽⁰⁾⟩ share the same energy E⁽⁰⁾, the first-order state-correction denominator E_n⁽⁰⁾ − E_m⁽⁰⁾ → 0 and the non-degenerate formula blows up. The fix: choose the *right* basis within the degenerate subspace before applying the perturbation. Specifically, diagonalize Ĥ′ restricted to the degenerate subspace; the eigenvalues are the first-order energy corrections, and the eigenvectors are the "good" unperturbed states for the perturbation problem.

For an n-fold degeneracy, this is an n×n matrix-diagonalization problem in a subspace. For a 2-fold degeneracy (which is most of what students will see):

W = ( ⟨a⁽⁰⁾|Ĥ′|a⁽⁰⁾⟩  ⟨a⁽⁰⁾|Ĥ′|b⁽⁰⁾⟩ )
    ( ⟨b⁽⁰⁾|Ĥ′|a⁽⁰⁾⟩  ⟨b⁽⁰⁾|Ĥ′|b⁽⁰⁾⟩ )

Eigenvalues of W are the first-order corrections; eigenvectors are the right linear combinations to use as zeroth-order states.

**Common misconception:** "Degenerate perturbation theory is just non-degenerate perturbation theory with extra steps." The conceptual content is different: degenerate perturbation theory is choosing a basis, not adding higher-order corrections. The perturbation tells you which basis was appropriate all along; the unperturbed degeneracy did not pick out a preferred basis, so any orthonormal pair was as good as any other — until Ĥ′ broke the tie.

**Worked example:** Linear Stark effect on hydrogen n = 2. The four degenerate states are |2s⟩, |2p_x⟩, |2p_y⟩, |2p_z⟩. The perturbation Ĥ′ = eEẑ. Show that the only non-zero matrix elements are ⟨2s|eEẑ|2p_z⟩ and ⟨2p_z|eEẑ|2s⟩, equal to −3eEa₀ (where a₀ is the Bohr radius). The 4×4 matrix block-diagonalizes — the 2p_x and 2p_y states are unaffected (no z-component); the 2s and 2p_z mix into ±(1/√2)(|2s⟩ ∓ |2p_z⟩) with energies ∓3eEa₀. The hydrogen n = 2 manifold splits linearly with field strength. Griffiths Ch. 6.4 has the full calculation.

**Sources:**
- Griffiths Ch. 6.2 (degenerate perturbation theory), Ch. 6.4 (fine structure of hydrogen — a major application of degenerate perturbation theory).
- Stark, J. (1914). "Observation of the Separation of Spectral Lines by an Electric Field." *Annalen der Physik* 43, 965 [verify reference; Stark's discovery was 1913, published 1914; Nobel 1919].

### 3. The variational principle

For any normalized trial state |ψ_trial⟩, the expectation value of the Hamiltonian provides an upper bound on the true ground-state energy:

⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E_ground.

The proof is two lines: expand |ψ_trial⟩ in the energy eigenbasis, |ψ_trial⟩ = Σ_n c_n|n⟩; the expectation value is Σ_n |c_n|² E_n; since E_n ≥ E_ground for all n and Σ |c_n|² = 1, the result follows. Equality holds only if |ψ_trial⟩ = |ground⟩.

The strategy: parameterize the trial state with a small number of variational parameters, compute ⟨Ĥ⟩ as a function of those parameters, and minimize. The minimum is your best upper bound on the ground-state energy from within the chosen family of trial states. The better the family, the tighter the bound.

This sounds suspiciously easy and it largely is — that's why the method is so useful. Three real virtues:

1. **No expansion parameter required.** Perturbation theory needs a small parameter (Ĥ′ small compared to Ĥ₀). The variational method does not.
2. **The bound is one-sided.** You never overestimate the ground-state energy; you only fail to find it exactly.
3. **The error is *second-order* in the deviation of |ψ_trial⟩ from |ground⟩.** A trial state that is "close" to the ground state gives an energy estimate that is much closer to the true ground state — the variational method is forgiving of imperfect trial states.

**Common misconception:** "The variational method tells you everything about the ground state." It tells you the energy, with bound. It tells you a trial wave function that approximates the true state. But the variational *energy* converges much faster than the variational *wave function*, so observables sensitive to the wave function (like density at a point) are less reliable than the energy estimate. This is why quantum-chemistry papers report energies to 5 decimal places but treat charge densities with more caution.

**Worked example (the textbook helium calculation):** Trial state for two electrons in helium: product of two 1s hydrogenic orbitals, but with effective nuclear charge Z* as a variational parameter rather than Z = 2. Compute ⟨Ĥ⟩(Z*) — three pieces (kinetic, electron-nucleus, electron-electron) — get

E(Z*) = (Z*)² − 2Z·Z* + (5/8)Z*

in atomic units (the kinetic energy is +Z*², the e-n attraction is −2Z·Z*, the e-e repulsion in 1s² is (5/8)Z*). Minimize over Z*: dE/dZ* = 2Z* − 2Z + 5/8 = 0 → Z* = Z − 5/16 = 27/16. Plug back: E_min = −(27/16)² ≈ −2.848 Hartree = −77.5 eV. Compare to experimental ground state −79.0 eV. The variational result is within 2% of experiment, captures most of the "electron screens electron" physics, and was already in Hylleraas's 1928 paper. Griffiths Ch. 7.2.

**Sources:**
- Griffiths Ch. 7 (variational principle and helium).
- Hylleraas, E. A. (1929). "Neue Berechnung der Energie des Heliums im Grundzustande, sowie des tiefsten Terms von Ortho-Helium." *Zeitschrift für Physik* 54, 347–366. [Hylleraas's high-accuracy variational calculation — six-parameter trial function, agreement with experiment to 4 significant figures.]
- Pekeris, C. L. (1958). "Ground State of Two-Electron Atoms." *Physical Review* 112, 1649–1658. [Modern variational benchmark — 1078-parameter trial function.]

### 4. The WKB approximation

The Wentzel–Kramers–Brillouin (WKB) approximation, sometimes called the semi-classical approximation, treats the wave function as a slowly-varying amplitude times a rapidly-oscillating phase whose derivative is the classical momentum. Setting ψ(x) = A(x) exp(iS(x)/ℏ) and expanding in powers of ℏ gives, to leading order:

ψ(x) ≈ (1/√|p(x)|) exp(±(i/ℏ) ∫ p(x′) dx′)

where p(x) = √(2m(E − V(x))) in the classically allowed region (E > V) and p(x) = i|p(x)| in the classically forbidden region (E < V). The approximation is valid when the de Broglie wavelength λ = h/p varies slowly compared to itself — quantitatively, when |dλ/dx| ≪ 1, or equivalently when the potential changes negligibly over one wavelength.

Three classical applications earn their place:

1. **Bound-state quantization (Bohr–Sommerfeld).** For a particle bound between classical turning points a and b at energy E:
   ∮ p(x) dx = 2 ∫_a^b p(x) dx = (n + 1/2) · 2πℏ
   The +1/2 is the Maslov index — it arises from the connection formulas at the turning points (specifically, a phase loss of π/4 at each turning point, total π/2). This is the WKB version of the Bohr quantization condition, with the correction that makes it agree with the exact harmonic-oscillator result E_n = (n + 1/2)ℏω.

2. **Tunneling through a barrier.** For a barrier from a to b with E < V(x) in between, the transmission coefficient is, to leading order in WKB:
   T ≈ exp(−(2/ℏ) ∫_a^b √(2m(V(x) − E)) dx)
   The integral is the *action* across the barrier. The exponential dependence on action means tunneling probabilities span many orders of magnitude with small changes in barrier shape — which is why alpha-decay half-lives span 24 orders of magnitude (from 10⁻⁶ s for thorium isotopes to 10¹⁸ s for thorium-232) for changes in alpha-particle energy of only a factor of two.

3. **Alpha decay (Gamow's 1928 calculation).** Gamow modeled the alpha particle as a wave packet inside a finite-range nuclear potential well, tunneling through the Coulomb barrier outside. The WKB tunneling formula gave the Geiger–Nuttall relation between alpha-particle energy and decay rate — log(T_{1/2}) ∝ Z/√E — quantitatively, from first principles. This was the first nuclear physics calculation done with QM. Gamow, G. (1928). "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik* 51, 204–212. (Gurney and Condon arrived at the same conclusion independently the same year, *Physical Review* 33, 127–140.)

**Common misconception:** "WKB is valid for high-energy states only." More precise: WKB is valid where the potential is *slowly varying compared to the local wavelength*. For low-energy states deep in a potential well, the wavelength is long and the potential varies a lot per wavelength — WKB fails. For high-energy states above a smooth potential, WKB is excellent. For tunneling, WKB is good when the barrier is wide and smooth, less good for sharp narrow barriers (where the connection formulas at the turning points matter relatively more).

**Worked example:** Compute the WKB transmission through a rectangular barrier of height V₀ and width L for E < V₀. The integral is trivial: T ≈ exp(−2L√(2m(V₀−E))/ℏ). Compare to the exact result from solving the Schrödinger equation in three regions: T_exact = 1/(1 + (V₀²/(4E(V₀−E))) sinh²(κL)) where κ = √(2m(V₀−E))/ℏ. For large κL the exact result reduces to ≈ 16(E/V₀)(1 − E/V₀) exp(−2κL); the WKB result is just the exponential, missing the prefactor. The WKB exponential captures the order of magnitude; the prefactor captures the rest.

**Sources:**
- Wentzel, G. (1926). "Eine Verallgemeinerung der Quantenbedingungen für die Zwecke der Wellenmechanik." *Zeitschrift für Physik* 38, 518–529.
- Kramers, H. A. (1926). "Wellenmechanik und halbzahlige Quantisierung." *Zeitschrift für Physik* 39, 828–840.
- Brillouin, L. (1926). "La mécanique ondulatoire de Schrödinger; une méthode générale de résolution par approximations successives." *Comptes Rendus* 183, 24–26.
- Gamow, G. (1928). "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik* 51, 204–212.
- Griffiths Ch. 8 (WKB approximation).

### 5. Time-dependent perturbation theory and Fermi's golden rule

The setup: an unperturbed system with eigenstates |n⟩ and energies E_n, with a perturbation Ĥ′(t) that is turned on at t = 0. The system starts in state |i⟩ at t = 0. What is the probability of finding it in state |f⟩ ≠ |i⟩ at time t?

Expand the time-evolving state in the interaction picture:
|ψ(t)⟩ = Σ_n c_n(t) e^(−iE_n t/ℏ) |n⟩

Substitute into the Schrödinger equation. To first order in Ĥ′:

c_f^(1)(t) = (1/iℏ) ∫_0^t ⟨f|Ĥ′(t′)|i⟩ e^(iω_fi t′) dt′

where ω_fi = (E_f − E_i)/ℏ.

For a sinusoidal perturbation Ĥ′(t) = V̂ cos(ωt), the transition amplitude has resonances at ω = ±ω_fi. Squaring to get the transition probability, integrating over the line shape, and dividing by the elapsed time gives the *transition rate per unit time*:

W_{i→f} = (2π/ℏ) |⟨f|V̂|i⟩|² δ(E_f − E_i ∓ ℏω)

When the final state is part of a continuum with density of states ρ(E_f), the delta function collapses to give Fermi's golden rule:

**W_{i→f} = (2π/ℏ) |⟨f|Ĥ′|i⟩|² ρ(E_f)**

The name is Fermi's; the derivation is Dirac's, who introduced it in his 1927 paper on the emission and absorption of radiation (*Proceedings of the Royal Society A* 114, 243–265, "The Quantum Theory of the Emission and Absorption of Radiation"). Fermi called it "Golden Rule No. 2" in his lecture notes (*Nuclear Physics*, University of Chicago Press, 1950). The misattribution stuck and is now permanent.

The conditions for the rule: (i) time t must be long enough for the delta function to be sharp (long compared to 1/ω_fi) but short enough that the perturbation is still small (the transition probability is still ≪ 1); (ii) the final states must be densely packed (continuum); (iii) first-order perturbation theory must be adequate (Ĥ′ small).

Applications: spontaneous emission rates (Einstein A coefficients fall out of Fermi's golden rule applied to atom-radiation coupling — see Unit 10 §lasers); beta decay (Fermi's original use case); neutron capture cross sections; LED radiative recombination; photoionization; Raman scattering.

**Common misconception:** "Fermi's golden rule is exact." It is first-order perturbation theory applied to transitions into a continuum. It is excellent when its assumptions hold and arbitrarily bad when they don't — bound-state-to-bound-state transitions (no continuum) require a different treatment; strong-field transitions (Ĥ′ not small) require higher orders or non-perturbative methods (Floquet theory, e.g.).

**Worked example:** Atomic transition rate. For a hydrogen 2p → 1s spontaneous emission, the matrix element ⟨1s|er̂|2p⟩ is computable in closed form. Plug into the dipole approximation of Fermi's golden rule with the photon density of states ρ(ω) = ω²V/(π²c³) and one gets the spontaneous emission rate A_{2p→1s} ≈ 6 × 10⁸ s⁻¹ — the natural line width of the Lyman-α line. Compare to experimental measurements (matches to better than 1%). Griffiths Ch. 9.2–9.3.

**Sources:**
- Dirac, P. A. M. (1927). "The Quantum Theory of the Emission and Absorption of Radiation." *Proceedings of the Royal Society A* 114, 243–265.
- Fermi, E. (1950). *Nuclear Physics: A Course Given by Enrico Fermi at the University of Chicago*. University of Chicago Press. [The "Golden Rule No. 2" passage.]
- Griffiths Ch. 9 (time-dependent perturbation theory and Fermi's golden rule).

---

## B. Domain examples and cases

### Case 1 — Hylleraas's helium variational calculation (1929)

Egil Hylleraas in 1929 (*Zeitschrift für Physik* 54, 347) extended the two-electron helium variational calculation by using a trial wave function with explicit electron-electron distance r₁₂ as a coordinate — six variational parameters in his original calculation. The result agreed with experiment to four significant figures and demonstrated that variational methods could rival spectroscopic accuracy. The companion can use this to make the case that approximation methods are not "approximations" in the disparaging sense — they are the methods that delivered the first quantitative confirmation that QM described helium correctly.

### Case 2 — Alpha decay and the Geiger–Nuttall law

Gamow's 1928 WKB calculation of alpha decay rates explained the empirical Geiger–Nuttall relation: log(half-life) ∝ Z/√E_α. The relation spans 24 orders of magnitude in half-life across the alpha-emitting nuclei, with E_α varying only by a factor of two. Without WKB tunneling, the relation looks like numerology. With WKB, it falls out of one integral: the action across the Coulomb barrier scales as Z/√E, and the half-life is exp(action/ℏ), so log(half-life) ∝ Z/√E. This is one of the cleanest cases of an approximation method *explaining* a phenomenon that classical reasoning had no purchase on.

### Case 3 — Fermi's beta-decay theory (1934)

Fermi's 1934 paper *Zeitschrift für Physik* 88, 161 used time-dependent perturbation theory and what would become known as Fermi's golden rule to compute beta-decay rates in terms of a four-fermion contact interaction (the original Fermi constant G_F). The shape of the energy spectrum of emitted electrons and the dependence on nuclear charge fell out. The 1934 paper was rejected by *Nature* as "too speculative" before *Zeitschrift für Physik* published it; the theory survived essentially unchanged into the V−A reformulation of the 1950s and is the prototype of effective-field-theory phenomenology. The companion can use this as the case study for *what an approximation method produces* — not just numbers, but a tractable framework that survives generations of refinement.

### Failure case — Perturbation theory and the harmonic oscillator with a quartic perturbation

For Ĥ = (1/2)p² + (1/2)x² + λx⁴, perturbation theory in λ converges nowhere — the radius of convergence is zero. Bender and Wu (1969, *Physical Review* 184, 1231) computed the coefficients of the energy series to high order; they grow factorially. Yet truncating at the right order (roughly n ≈ 1/λ for small λ) gives an excellent numerical estimate. The companion should use this as the "asymptotic series" case study — perturbation theory works in physics because the first few terms are good, not because the series converges. Borel summation can recover meaningful results from divergent series in many cases (and does, in QED and beyond); but the naive series itself is divergent. Tell the student.

---

## C. Connections and dependencies

**Prerequisites:** Unit 2 (linear algebra and Hilbert space); Unit 3 (Schrödinger equation, eigenvalue problem); Unit 5 (formalism — completeness relation Σ |n⟩⟨n| = Î is the key technical move in deriving perturbation theory); Unit 6 (hydrogen atom, for examples); Unit 8 (identical particles, for the helium variational example, which is a forward-reference from Unit 8 §A.4).

**Unlocks:** Unit 10 (modern applications) — the laser rate equations come from Einstein A and B coefficients which come from Fermi's golden rule; band structure perturbation theory; superconductivity (BCS theory uses variational and perturbative methods); quantum computing (qubit gate calibration uses time-dependent perturbation theory to compute leakage and crosstalk).

**Adjacent unit connections:**
- Unit 6 (hydrogen atom): fine structure (Ch. 6.4 in Griffiths), the Zeeman effect, and the Stark effect are all degenerate perturbation theory applied to the hydrogen atom.
- Unit 7 (angular momentum): selection rules in time-dependent perturbation theory (Δℓ = ±1, Δm_ℓ = 0 or ±1 in dipole transitions) come from angular-momentum algebra applied to the perturbation matrix element.
- Unit 8 (identical particles): the helium ground-state variational calculation belongs in *both* units — it appears once and gets cross-referenced.

---

## D. Current state of the field

**Settled:** All five methods (time-independent perturbation, degenerate, variational, WKB, time-dependent perturbation including Fermi's golden rule) are textbook physics; their domains of validity are well-understood. No contemporary controversy about the methods themselves.

**Active research:**
- *Resurgent analysis and Borel summation.* The divergent nature of perturbation series in QFT has been the subject of sustained mathematical work — resurgence theory (Écalle, 1980s) gives a framework for extracting non-perturbative information (instantons, renormalons) from the divergence pattern of perturbation series. Active research at the intersection of mathematical physics and number theory. [verify: Costin and Dunne reviews around 2020 for state of the art.]
- *Variational quantum eigensolvers* (VQE). On quantum hardware, the variational principle is the centerpiece of one of the most-touted near-term quantum algorithms: prepare a parameterized trial state on a noisy quantum computer, measure ⟨Ĥ⟩, classically optimize the parameters. Peruzzo et al. (2014) *Nature Communications* 5, 4213. Practical utility remains uncertain in the NISQ era; the variational method itself is unchanged from 1929.
- *Tensor-network variational methods.* DMRG (White 1992 *Physical Review Letters* 69, 2863) and its modern descendants (MPS, PEPS) are variational methods with extremely flexible trial states — the variational principle scaled up to thousands of parameters. Workhorses of computational condensed matter.

**Key references:**
- Griffiths Ch. 6 (perturbation theory), 7 (variational), 8 (WKB), 9 (time-dependent perturbation, Fermi's golden rule).
- Sakurai and Napolitano (2017) — more rigorous; Ch. 5 covers the same material at a higher level of formal presentation.
- Bender, C. M. and Orszag, S. A. (1999). *Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic Methods and Perturbation Theory.* Springer. [The reference for asymptotic methods, including WKB.]

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **"When do I use which method?"** This is the most common confusion. Quick guide the chapter should make explicit:
   - Small perturbation, isolated levels → non-degenerate perturbation theory.
   - Small perturbation, degenerate levels → degenerate perturbation theory.
   - No small parameter, want the ground state → variational.
   - Smooth slowly-varying potential, want tunneling or quantization → WKB.
   - Time-dependent driving, transitions between levels → time-dependent perturbation theory.
   - Transitions into a continuum → Fermi's golden rule.

2. **"Why does the perturbation series diverge?"** Many students will be told that "Ĥ′ small" is sufficient for convergence. It isn't, and the chapter should say so. The honest framing: perturbation theory is an asymptotic expansion that gives excellent numerical results when truncated correctly. The point of the series is the first few terms.

3. **"Where does the +1/2 in Bohr–Sommerfeld come from?"** Many treatments present (n + 1/2)·2πℏ as a "WKB rule" without explaining the Maslov index. The companion should sketch the connection formulas at the turning points (Airy functions, the π/4 phase loss per turning point) — at least naming what is going on, if not deriving it in full. This is one of the places the chapter can genuinely teach the *clever part*.

4. **"How do you derive a delta function from an integral?"** Fermi's golden rule derivation involves the identity (sin²(ω t/2))/(ω²) → (π t /2) δ(ω) as t → ∞. This algebraic move is unfamiliar and worth a paragraph — the function on the left is sharply peaked at ω = 0 with peak value t²/4 and width 1/t, so the area scales as t, and in the long-t limit it acts as a delta function multiplied by t. The chapter should not skip this.

**Analogies that work:**
- Variational method as "the height of any hill is an upper bound on the highest mountain" — clean, captures the one-sided-bound structure.
- WKB as "the wave function knows the local momentum and oscillates accordingly, like a string with position-dependent tension" — captures the slowly-varying-amplitude / rapidly-varying-phase decomposition.
- Fermi's golden rule as "the rate of a transition is proportional to the squared coupling times the density of available final states" — keeps the three ingredients (coupling, matrix element, available states) named.

**Analogies that mislead:**
- "Perturbation theory is like a Taylor expansion." Suggests convergence. Replace with: "Perturbation theory is like an asymptotic expansion — the first few terms are accurate, the full series may diverge."
- "WKB is the classical limit." Half-true; WKB is the *leading* term in an expansion in ℏ, and it includes a +1/2 (the Maslov index) that the strict classical limit does not.

**Exercises (Bloom's level):**
- **Knowledge:** State the four key formulas (first-order energy, first-order state, second-order energy, Fermi's golden rule). (L1)
- **Application:** Compute the first-order Stark effect for hydrogen n = 2; the WKB transmission through a triangular barrier; the variational helium energy with one parameter (Z*). (L3)
- **Analysis:** Given a Hamiltonian, decide which approximation method is appropriate and justify the choice in one paragraph. (L4)
- **Evaluation:** Read a paragraph of Dyson's 1952 paper on the divergence of QED perturbation theory; explain in your own words why analyticity at α = 0 fails. (L5)
- **Synthesis:** Derive Fermi's golden rule from time-dependent perturbation theory; identify the long-time and small-Ĥ′ conditions and their tension. (L6)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 6 (time-independent perturbation theory, fine structure of hydrogen, Zeeman, hyperfine), Ch. 7 (variational principle, helium ground state), Ch. 8 (WKB approximation), Ch. 9 (time-dependent perturbation theory, two-level systems, Fermi's golden rule, lasers). Together these four chapters form the spine of Unit 9. (pantry text: `822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt` — 1st ed.; verify section numbers against current edition.)
- **Liboff, *Introductory Quantum Mechanics*** — covers all five methods with somewhat more rigor and a different selection of worked examples; the WKB treatment in particular is denser than Griffiths and useful as a second source. (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`)
- **Pop-sci references** — TIKTOC marks Unit 9 as having no pop-sci coverage. No `[BOOK]` entries in the Recommended Course TOC for this unit. Companion-original throughout.
- **`_lib_Penrose-Emperors-New-Mind.md`** — Penrose has good discussions of WKB and the semiclassical limit; useful for narrative if the chapter wants a popularization-level voice anywhere.
- **`_lib_QM-Into-the-Light-Beginners.md`** — likely contains tunneling narrative usable in the WKB worked example, even though the pop-sci coverage of WKB itself is absent.

---

## G. Gaps and flags

- **FLAG:** The exact form of the Maslov-index correction in Bohr–Sommerfeld (the +1/2) deserves more attention than a one-line mention. The companion should either (a) derive the π/4 phase loss at a soft turning point via the Airy-function connection formula, or (b) state the result and provide a pointer to a more advanced text (Bender & Orszag Ch. 10). Recommend (b) for length reasons; flag in the draft.
- **FLAG:** Fermi's golden rule notation conventions vary. Some texts write it with ρ(E) (density of states per unit energy), some with ρ(ε) (per unit frequency), some absorb factors of 2π differently. Recommend Griffiths's convention; flag the alternatives in a footnote.
- **FLAG:** The chapter risks being too long. Five methods at full depth is more than ~2,800 words affords. Recommend: deep-dive on time-dependent perturbation theory → Fermi's golden rule (because it powers Unit 10 directly), and treat the other four methods at "mechanism + one worked example + sources" depth. The deep-dive earns its place because it's the most heavily reused.
- **FLAG:** The +1/2 Maslov index for Bohr-Sommerfeld gives exact agreement with the harmonic oscillator (E_n = (n + 1/2)ℏω) but only approximate agreement with most other potentials (the hydrogen atom, for instance, gives the exact result up to a centrifugal-barrier correction). Need to be careful not to overclaim. [verify which potentials WKB+1/2 gets exactly right; see Griffiths Ch. 8 problem set.]
- **GAP:** The Dyson 1952 argument for divergence of QED perturbation theory is a beautiful physics argument that students rarely meet — the analytic-continuation argument is short, surprising, and worth one paragraph if length allows. May not fit; flag for possible cut.
- **GAP:** Time-dependent perturbation theory beyond first order — most introductory treatments stop at first order, but second-order is necessary for Raman scattering and other two-photon processes. Probably out of scope for this unit; flag and forward-reference.
- **GAP:** Adiabatic and sudden approximations. Standard topics in many QM courses, omitted here per the TIKTOC outline. The companion may want a one-paragraph note saying they exist and pointing to Griffiths Ch. 10 (adiabatic theorem) for the interested reader.
- **FLAG:** Sign conventions for energy corrections vary between texts. Griffiths uses E_n = E_n⁽⁰⁾ + λE_n⁽¹⁾ + ...; some texts use H' = ε V and expand in ε. Companion should pick one convention and stick with it. [verify final notation matches Griffiths 3rd ed.]
