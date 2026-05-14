# Research Notes: Unit 10 — Quantum Mechanics in the Modern World

**Source:** TIKTOC.md Unit 10 entry (lines 288–294), Part X diagnostic (lines 168–188)
**Notes file:** 10-quantum-mechanics-in-the-modern-world_notes.md
**Corresponding chapter:** chapters/10-quantum-mechanics-in-the-modern-world.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 10: Quantum Mechanics in the Modern World
> - Entanglement, Bell's theorem, EPR **[BOOK: Ch. 7 — strong; use directly]**
> - Lasers and stimulated emission **[BOOK: Ch. 14 — use directly]**
> - Semiconductors and band theory — ❌ (Ch. 4 provides motivation only)
> - Quantum computing: motivation and qubits **[BOOK: Ch. 16 — for motivation only]**
> - Superconductivity: overview **[BOOK: Ch. 17 — historical narrative is good]**
> - Tunneling applications: STM, flash, biology **[BOOK: Ch. 9 — excellent]**

TIKTOC Part X Verdict: "Mixed. Entanglement and lasers are genuinely good chapters. Quantum computing is well-motivated but has no technical content. The applications catalog for tunneling is excellent for motivating the topic. MRI and superconductivity are at a science-literacy level, not a physics level." This is the unit where the pop-sci book pulls its weight most directly. The companion's strategy: lean on the pop-sci narrative for motivation (Ch. 7 entanglement, Ch. 9 tunneling apps, Ch. 14 lasers, Ch. 17 superconductivity history), and add the math (Bell inequality, Einstein A/B coefficients, Bloch theorem sketch, qubit algebra, BCS gap equation in cartoon form, STM tunneling current).

Target ~3,500 words (longest unit in the book — broadest scope). Critical aging-risk warning: quantum computing, Bell-test loophole-free experiments, and high-T_c superconductivity all moved meaningfully in 2022–2025. The chapter should label its currentness explicitly and provide "as of 2026" framing for any quantitative claim. See §G for aging risks.

---

## A. Conceptual foundations

### 1. Entanglement, EPR, and Bell's theorem

The 1935 Einstein–Podolsky–Rosen paper (*Physical Review* 47, 777–780, "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?") posed a thought experiment: prepare two particles in a momentum-correlated state, separate them by an arbitrary distance, then measure the position of one. By quantum mechanics, the position measurement on particle A immediately determines what the position-measurement outcome on particle B would have to be (because the positions are correlated). EPR argued that, since particle B was spacelike-separated from A at the time of measurement, the position of B must have been a *real property* of B before the measurement on A — and similarly the momentum (which is correlated the same way) must also have been a real property. But QM forbids assigning simultaneous values to position and momentum. Therefore, EPR concluded, QM is incomplete.

David Bohm's 1951 reformulation (in his textbook *Quantum Theory*, Prentice-Hall) replaced position-momentum with two spin-1/2 particles in a singlet state. Cleaner: the singlet state |ψ⟩ = (1/√2)(|↑⟩_A|↓⟩_B − |↓⟩_A|↑⟩_B) has total spin zero, so any spin measurement on A perfectly predicts the opposite outcome on B. The setup is binary, the math is two-by-two matrices, and the philosophical content is identical.

John Bell's 1964 paper (*Physics Physique Fizika* 1, 195–200, "On the Einstein Podolsky Rosen Paradox") turned the EPR argument into a quantitative test. *Any* local hidden-variable theory — any theory in which particle B has predetermined values for spin along every axis, with no faster-than-light coordination between A and B — must satisfy certain inequalities. The most experimentally useful is the CHSH inequality (Clauser, Horne, Shimony, Holt 1969 *Physical Review Letters* 23, 880):

|⟨A₁B₁⟩ + ⟨A₁B₂⟩ + ⟨A₂B₁⟩ − ⟨A₂B₂⟩| ≤ 2

where A_i and B_j are ±1-valued measurements of spin along chosen axes. Local hidden variables: ≤ 2. Quantum mechanics for the singlet state, with axes optimally chosen: 2√2 ≈ 2.828. The two predictions are not only different — they are different by 41%, which means a finite experiment can distinguish them with confidence.

Alain Aspect, Philippe Grangier, and Gérard Roger at Institut d'Optique in Orsay performed the first widely-accepted experimental violation in 1981–1982. Aspect, Grangier, Roger 1982 (*Physical Review Letters* 49, 91 and *PRL* 49, 1804) used pairs of polarization-entangled photons from a calcium cascade source; the second paper added time-varying analyzers to close the "communication loophole" (whereby in principle the detectors could in some sense have signaled each other before the measurement was complete). Result: S = 2.697 ± 0.015, violating the Bell inequality by tens of standard deviations.

The loopholes — detection efficiency (most photons missed; if the detected subsample is non-representative, the inequality can be violated even by local hidden variables); locality (the choice of measurement basis must be made fast enough that no light-speed signal can coordinate between the detectors); freedom-of-choice (the basis choices must be genuinely independent of any "hidden" causal predecessor) — were closed simultaneously for the first time in 2015 by three independent experiments:

- Hensen et al. (Delft) 2015 *Nature* 526, 682–686, "Loophole-free Bell inequality violation using electron spins separated by 1.3 km." Used NV centers in diamond.
- Giustina et al. 2015 *Physical Review Letters* 115, 250401, "Significant-loophole-free test of Bell's theorem with entangled photons" (Vienna).
- Shalm et al. 2015 *Physical Review Letters* 115, 250402, "Strong loophole-free test of local realism" (NIST Boulder).

Aspect, Clauser, and Zeilinger shared the 2022 Nobel Prize in Physics for this body of work [https://www.nobelprize.org/prizes/physics/2022/].

The reading: local hidden-variable theories of the form EPR envisioned are ruled out, at confidence levels equivalent to >10 standard deviations. What remains is some combination of (i) quantum mechanics is correct, (ii) signals do propagate faster than light *but not in a way that allows useful communication* (a tightrope that few practicing physicists are willing to walk), (iii) some assumption of the Bell setup is wrong (most often: counterfactual definiteness, or "the world is super-deterministic"). The companion should make this explicit and not pretend the question is fully settled philosophically — it is settled experimentally for local realism in its standard form.

**Common misconception:** "Entanglement allows faster-than-light communication." It does not. The marginal statistics of measurements on particle B are unchanged by measurements on A — only the *correlations* are non-classical. To learn about the correlation, you need to compare your data with the partner's, and that comparison travels at light speed. The no-signaling theorem is a theorem in QM, not an assumption: P(b|a, x, y) = P(b|y) regardless of what x is. The companion should state this with the precision the pop-sci book often muddles.

**Worked example (the Bell inequality math):** For the singlet state and measurement axes a₁ = 0, a₂ = π/4 on Alice's side, b₁ = π/8, b₂ = 3π/8 on Bob's side, compute ⟨A_i B_j⟩ = −cos(2(a_i − b_j)) and verify CHSH = 2√2. This is the calculation the pop-sci book skips and the companion supplies. Five-line calculation; the content of Bell's theorem in a half page.

**Sources:**
- Einstein, A., Podolsky, B., and Rosen, N. (1935). "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Physical Review* 47, 777–780.
- Bell, J. S. (1964). "On the Einstein Podolsky Rosen Paradox." *Physics Physique Fizika* 1, 195–200.
- Clauser, J. F., Horne, M. A., Shimony, A., and Holt, R. A. (1969). "Proposed Experiment to Test Local Hidden-Variable Theories." *Physical Review Letters* 23, 880–884.
- Aspect, A., Grangier, P., and Roger, G. (1982). "Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A New Violation of Bell's Inequalities." *Physical Review Letters* 49, 91–94.
- Hensen, B. et al. (2015). "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." *Nature* 526, 682–686.
- Giustina, M. et al. (2015). *Physical Review Letters* 115, 250401.
- Shalm, L. K. et al. (2015). *Physical Review Letters* 115, 250402.
- Nobel Prize in Physics 2022 [https://www.nobelprize.org/prizes/physics/2022/].

### 2. Lasers and stimulated emission

Einstein 1917 (*Physikalische Zeitschrift* 18, 121–128, "Zur Quantentheorie der Strahlung," "On the Quantum Theory of Radiation") introduced the three radiative processes between two atomic levels: absorption (rate B₁₂ ρ(ν)), spontaneous emission (rate A₂₁), and stimulated emission (rate B₂₁ ρ(ν)). The third was new — Einstein deduced its necessity from thermodynamic consistency with Planck's blackbody distribution. The Einstein relations link the three:

A₂₁/B₂₁ = 8πhν³/c³
B₂₁ = B₁₂ (for non-degenerate levels)

The first relation says spontaneous emission is dominant at high frequencies, stimulated emission at low frequencies — which is why lasing is easier in the infrared than the X-ray. The second relation says that the matrix element governing emission and absorption is the same, modulo statistical degeneracy. Both relations fall out of Fermi's golden rule (Unit 9) applied to the atom-field interaction in the dipole approximation.

Lasing requires *population inversion* — more atoms in the upper level than the lower. In thermal equilibrium this is impossible (Boltzmann puts most population in the lower level). Inversion is achieved by *pumping* — driving atoms into a third or fourth level from which they decay to the upper laser level faster than the laser-emission decay rate. Three-level (ruby) and four-level (HeNe, Nd:YAG) schemes are the two canonical configurations.

Theodore Maiman built the first laser in May 1960 at Hughes Research Labs in Malibu, California, using a ruby rod pumped by a flashlamp. The output was 694.3 nm red light in pulses. *Nature* 187, 493–494 (August 1960), "Stimulated Optical Radiation in Ruby." Maiman's paper was famously rejected first by *Physical Review Letters*, which judged it too incremental [historical context: Bromberg 1991, *The Laser in America 1950–1970*]. Within months, Schawlow and Townes had worked out the He-Ne laser, and within a year the technology was off and running.

**Common misconception:** "Lasers are coherent because the photons are 'in the same state.'" More precise: lasers are coherent because the *electromagnetic field mode* is in a coherent state |α⟩ (a Glauber coherent state, eigenstate of the annihilation operator, displaced vacuum), with photon-number distribution sharply peaked and definite phase. The classical wave picture works because coherent states are the closest a quantum field can get to a classical field. Photons in the same mode of the EM field are bosons; their joint state is well-described as a coherent state of that mode, not a tensor product of N single-photon states.

**Worked example:** Compute the threshold population inversion for a four-level laser given spontaneous emission rate A, cavity loss rate κ, mode volume V. From rate-equation analysis: N_threshold = κ V / (c σ A) where σ is the stimulated-emission cross section. For a typical Nd:YAG laser, σ ≈ 3 × 10⁻¹⁹ cm² and the numbers work out cleanly. Griffiths Ch. 9.3 has the textbook treatment; for a fuller derivation see Siegman, *Lasers* (University Science Books 1986). [verify pagination.]

**Sources:**
- Einstein, A. (1917). "Zur Quantentheorie der Strahlung." *Physikalische Zeitschrift* 18, 121–128. English translation in van der Waerden, B. L. (1967), *Sources of Quantum Mechanics*, Dover.
- Maiman, T. H. (1960). "Stimulated Optical Radiation in Ruby." *Nature* 187, 493–494.
- Griffiths Ch. 9.3 (lasers via Fermi's golden rule).

### 3. Semiconductors and band theory

Felix Bloch's 1928 thesis at Leipzig (*Zeitschrift für Physik* 52, 555–600, "Über die Quantenmechanik der Elektronen in Kristallgittern") established that for a periodic potential V(r) = V(r + R) — where R is any lattice translation vector — the electronic eigenstates take the form

ψ_{n,k}(r) = e^(ik·r) u_{n,k}(r)

where u_{n,k}(r) has the same periodicity as the lattice. The energy E_n(k) as a function of crystal momentum k forms a *band* labeled by n, and there are forbidden gaps between bands where no allowed energies exist. Conductors have a partially-filled band (the Fermi level sits in the middle of a band); insulators have a fully-filled valence band and an empty conduction band separated by a wide gap; semiconductors have a smaller gap (~1 eV scale) so thermal excitation populates the conduction band at room temperature.

Doping shifts the equilibrium populations. *n-type* doping (phosphorus in silicon: one extra valence electron per dopant atom) supplies electrons to the conduction band; *p-type* doping (boron in silicon: one fewer valence electron) supplies holes to the valence band. The *pn junction* — a single crystal with adjacent p- and n-doped regions — develops a depletion zone with a built-in electric field, and is the heart of every diode, LED, photovoltaic cell, and bipolar transistor. The MOSFET (metal-oxide-semiconductor field-effect transistor), which dominates modern integrated circuits, uses a gated channel to switch current; the gate voltage controls the carrier density in a quantum-mechanically confined inversion layer.

The companion should not attempt a full solid-state derivation — Bloch theorem in one dimension via the Kronig–Penney model is doable in one chapter, but full three-dimensional band structure requires a solid-state course. Recommended scope: state Bloch's theorem, sketch the Kronig–Penney 1D model (Kronig and Penney 1931, *Proceedings of the Royal Society A* 130, 499–513, "Quantum Mechanics of Electrons in Crystal Lattices") to show how bands and gaps emerge from a periodic potential, then describe doping and the pn junction qualitatively. Forward-reference: a solid-state physics course.

**Common misconception:** "Holes are real particles." Holes are quasi-particles — the absence of an electron in a nearly-full band, which behaves as if a positive-charge particle were moving through an empty band, with an effective mass set by the band curvature near the band edge. The mathematics works because the band structure has approximate particle-hole symmetry near the band extrema. The companion should label "hole" as a quasi-particle the first time it appears.

**Worked example:** Kronig–Penney model. For a 1D periodic array of delta-function barriers V(x) = V₀ a Σ_n δ(x − na), apply Bloch's theorem and the boundary conditions at each barrier. The result is a transcendental equation cos(ka) = cos(qa) + (mV₀a/ℏ²q) sin(qa) where q = √(2mE)/ℏ. The left side is bounded between ±1; the right side has stretches where |RHS| > 1 and no real k exists. Those are the forbidden gaps. The walk-through is in Griffiths Ch. 5.3 (third edition). One of the cleanest "from solving the Schrödinger equation, here are bands" calculations.

**Sources:**
- Bloch, F. (1928). "Über die Quantenmechanik der Elektronen in Kristallgittern." *Zeitschrift für Physik* 52, 555–600.
- Kronig, R. de L. and Penney, W. G. (1931). "Quantum Mechanics of Electrons in Crystal Lattices." *Proceedings of the Royal Society A* 130, 499–513.
- Ashcroft, N. W. and Mermin, N. D. (1976). *Solid State Physics.* Holt, Rinehart, Winston. [Standard reference for band theory at the senior/graduate level.]

### 4. Quantum computing

A *qubit* is a two-level quantum system. The basis states are conventionally |0⟩ and |1⟩, and the general state is

|ψ⟩ = α|0⟩ + β|1⟩,  |α|² + |β|² = 1.

A computation is a unitary operation on N-qubit Hilbert space (dimension 2^N), implemented as a circuit of one- and two-qubit gates. Measurement at the end collapses the state to a classical bit string with the Born-rule probability distribution. The two ingredients that distinguish quantum from classical computation are *superposition* (a single qubit can hold all of |0⟩, |1⟩, and any linear combination simultaneously) and *entanglement* (an N-qubit state can have 2^N independent complex amplitudes, exponentially more than the 2N real numbers needed to specify N independent classical bits).

Two algorithmic results anchor the field:

**Shor's algorithm** (Shor 1994, *Proceedings of FOCS '94*, 124–134, "Algorithms for quantum computation: discrete logarithms and factoring") factors an n-bit integer in O(n³) operations on a quantum computer, where the best classical algorithm (general number-field sieve) requires sub-exponential time exp(O(n^(1/3) (log n)^(2/3))). If a sufficiently large fault-tolerant quantum computer existed, RSA encryption (which depends on factoring being hard) would be broken.

**Grover's algorithm** (Grover 1996, *Proceedings of STOC '96*, 212–219, "A fast quantum mechanical algorithm for database search") finds a marked item in an N-item unsorted database in O(√N) queries, vs. O(N) classically. Quadratic, not exponential — the speedup is real but much smaller than Shor's. Applies to brute-force search problems.

As of 2026, the field is in the "noisy intermediate-scale quantum" (NISQ) era — Preskill's 2018 coinage (*Quantum* 2, 79). Current hardware: IBM's Condor processor (2023, 1121 superconducting qubits); Google's Sycamore family (53–70 qubits in published configurations); Quantinuum's H2 (56 trapped-ion qubits with all-to-all connectivity); IonQ Forte (32 trapped-ion qubits); Atom Computing (>1000 neutral-atom qubits). Logical-qubit demonstrations: Google reported in 2023 (*Nature* 614, 676–681, Acharya et al., "Suppressing quantum errors by scaling a surface code logical qubit") that increasing surface-code distance from 3 to 5 reduced the logical error rate — the first below-threshold demonstration of quantum error correction at scale.

The honest framing: as of mid-2026, no quantum computer has demonstrated useful speedup on a practically important problem. The 2019 "quantum supremacy" claim (Arute et al. 2019 *Nature* 574, 505–510, Google Sycamore) and the 2020 photonic claim (Zhong et al. 2020 *Science* 370, 1460–1463, Jiuzhang) are sampling tasks with no classical utility, included here for transparency rather than as capability claims. The largest integer factored by Shor's algorithm with full fault-tolerance assurance is still very small; non-Shor factoring claims (using variational methods like QAOA) factor larger numbers but do not exploit the Shor speedup [verify largest claim as of 2026].

**Common misconception:** "Quantum computers will break all encryption by 2030." Shor's algorithm threatens RSA and ECC *if and only if* a fault-tolerant quantum computer of millions of logical qubits is built. Current physical-qubit counts (~10³) and error rates (~10⁻³ per gate) put us many generations of progress short. NIST's post-quantum cryptography standardization (CRYSTALS-Kyber, CRYSTALS-Dilithium, FALCON, SPHINCS+, finalized 2022, standardized as FIPS 203/204/205 in 2024 [https://csrc.nist.gov/projects/post-quantum-cryptography]) is the practical response — the migration is happening *now*, in anticipation of an eventual large quantum computer, not in response to a current threat.

**Worked example:** Single-qubit gates and the Bloch sphere. A general qubit state can be written |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩, parameterized by two angles θ ∈ [0, π], φ ∈ [0, 2π]. The mapping is to a point on the unit sphere (Bloch sphere). Show that the three Pauli matrices generate rotations: X (NOT), Y, Z. The Hadamard gate H = (X + Z)/√2 maps |0⟩ → (|0⟩ + |1⟩)/√2, the canonical superposition. Two-qubit gates: the CNOT (controlled-NOT) flips the target qubit conditional on the control. CNOT plus single-qubit gates is universal (DiVincenzo 1995 *Physical Review A* 51, 1015) — every multi-qubit unitary can be decomposed into this gate set.

**Sources:**
- Shor, P. W. (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer." *SIAM Journal on Computing* 26(5), 1484–1509. [Final version; conference paper 1994.]
- Grover, L. K. (1996). "A fast quantum mechanical algorithm for database search." *Proceedings of STOC '96*, 212–219.
- Nielsen, M. A. and Chuang, I. L. (2010). *Quantum Computation and Quantum Information*, 10th Anniversary Edition. Cambridge University Press. [The canonical textbook.]
- Acharya, R. et al. (Google Quantum AI) (2023). "Suppressing quantum errors by scaling a surface code logical qubit." *Nature* 614, 676–681.
- NIST PQC Project [https://csrc.nist.gov/projects/post-quantum-cryptography].

### 5. Superconductivity

Heike Kamerlingh Onnes at Leiden discovered in 1911 that mercury's electrical resistance dropped abruptly to zero below 4.2 K. Onnes 1911 (Communications from the Physical Laboratory at the University of Leiden, No. 122b). Nobel 1913 for the liquefaction of helium that made the measurement possible. The phenomenon — resistance exactly zero, persistent currents lasting indefinitely — was the experimental fact; the theoretical explanation took 46 years.

The BCS theory (Bardeen, Cooper, Schrieffer 1957 *Physical Review* 108, 1175–1204, "Theory of Superconductivity") supplied the mechanism. Electrons near the Fermi surface experience an attractive interaction mediated by phonons (lattice vibrations); for arbitrarily weak attraction, the Fermi sea is unstable against formation of bound "Cooper pairs" (Cooper 1956 *Physical Review* 104, 1189–1190). The paired electrons, being composite bosons, can condense — and the condensate is rigid against perturbations smaller than the *superconducting gap* Δ, the energy required to break a Cooper pair. The current carriers (Cooper pairs) scatter only if scattering can supply Δ, which is forbidden by energy conservation at low temperature. Hence zero resistance.

The BCS gap equation at zero temperature is

1 = N(0)V ∫_0^(ℏω_D) dε / √(ε² + Δ²)

where N(0) is the density of states at the Fermi level, V is the attractive interaction strength, ω_D is the Debye frequency. The solution Δ ≈ 2ℏω_D exp(−1/N(0)V) is non-analytic in V — perturbation theory in V cannot find it. This is the "essential singularity" that made BCS hard to discover and explains why pre-BCS attempts failed.

Bednorz and Müller's 1986 discovery of high-T_c superconductivity in copper-oxide perovskites (Bednorz and Müller 1986, *Zeitschrift für Physik B* 64, 189–193, "Possible high T_c superconductivity in the Ba-La-Cu-O system") — Nobel 1987, the fastest in Nobel history — broke the picture. La₂₋ₓBaₓCuO₄ at T_c ≈ 35 K, then YBa₂Cu₃O₇ at T_c ≈ 93 K (Wu et al. 1987 *PRL* 58, 908), then higher cuprates up to ~135 K under ambient pressure (HgBa₂Ca₂Cu₃O₈₊δ). Hydrogen sulfide H₃S at ~200 K and 150 GPa pressure (Drozdov et al. 2015 *Nature* 525, 73–76) and lanthanum hydride LaH₁₀ at ~250 K and 170 GPa (Somayazulu et al. 2019 *Physical Review Letters* 122, 027001; Drozdov et al. 2019 *Nature* 569, 528–531) extended the record but require extreme pressure. Room-temperature ambient-pressure superconductivity has not been demonstrated as of 2026 [verify — Dias retractions complicate the recent literature; the 2023 LK-99 claim was not reproduced and is widely considered debunked].

The high-T_c mechanism remains contested. Phonon-mediated pairing of standard BCS form is too weak to account for T_c ~ 100 K in the cuprates; spin-fluctuation-mediated pairing and other strong-correlation mechanisms are leading candidates but consensus is unsettled. The companion should label this honestly. [verify state of the art 2026.]

**Common misconception:** "Superconductors are perfect conductors." Not quite — a perfect conductor maintains its flux state under changing external field; a superconductor expels magnetic flux entirely (the Meissner–Ochsenfeld effect, 1933, *Naturwissenschaften* 21, 787–788). The Meissner effect distinguishes superconductors from hypothetical perfect conductors and falls out of BCS theory (the supercurrent screens the field within a London penetration depth).

**Worked example:** Estimate T_c using the BCS relation 2Δ/k_B T_c = 3.53 (universal in weak-coupling BCS). For aluminum, Δ ≈ 0.17 meV → T_c ≈ 1.1 K. Compare to measured T_c = 1.18 K. The BCS prediction is within 7%. This is the strongest evidence that BCS captures the conventional-superconductor mechanism correctly.

**Sources:**
- Onnes, H. K. (1911). Communications from the Physical Laboratory at the University of Leiden, No. 122b.
- Bardeen, J., Cooper, L. N., and Schrieffer, J. R. (1957). "Theory of Superconductivity." *Physical Review* 108, 1175–1204.
- Bednorz, J. G. and Müller, K. A. (1986). "Possible high T_c superconductivity in the Ba-La-Cu-O system." *Zeitschrift für Physik B* 64, 189–193.
- Drozdov, A. P. et al. (2015). "Conventional superconductivity at 203 K at high pressures in the sulfur hydride system." *Nature* 525, 73–76.

### 6. Tunneling applications

Quantum tunneling — the WKB-transmission formula from Unit 9 — produces a long catalog of technologies and natural phenomena. The pop-sci book Ch. 9 has the best list in the book per TIKTOC. The companion adds the math.

**Scanning tunneling microscopy (STM).** Gerd Binnig and Heinrich Rohrer at IBM Zurich 1981–1982 (Binnig and Rohrer 1982 *Helvetica Physica Acta* 55, 726; Binnig et al. 1982 *Physical Review Letters* 49, 57–61); Nobel 1986. A metal tip is brought ångström-close to a conducting surface; electrons tunnel through the vacuum gap. The tunneling current depends exponentially on the gap distance d: I ∝ exp(−2κd) where κ ≈ √(2mφ)/ℏ ≈ 1 Å⁻¹ for typical work functions φ ≈ 4 eV. A 1 Å change in d changes the current by a factor of e² ≈ 7.4. This is the reason STM resolves individual atoms: the current is dominated by the single closest atom on the tip.

**Flash memory.** The floating-gate transistor (Dawon Kahng and Simon Sze 1967 at Bell Labs, *Bell System Technical Journal* 46, 1288). Writes a bit by tunneling electrons through a thin oxide layer onto a floating gate; reads by sensing whether the floating gate's charge has shifted the transistor's threshold voltage. Erase: tunnel them back off. The reason flash retains data for years without power is that the tunneling rate at low voltage is exponentially small — the same WKB exponential that makes alpha decay slow.

**Alpha decay.** Gamow 1928 (covered in Unit 9 §A.4). The 24-orders-of-magnitude span of alpha-decay half-lives is one of the cleanest empirical signatures of tunneling.

**Josephson junctions and SQUIDs.** Cooper-pair tunneling across an insulating barrier between two superconductors. Josephson 1962 *Physics Letters* 1, 251–253. The DC Josephson effect (supercurrent through the barrier at zero voltage) and AC Josephson effect (oscillating current at frequency 2eV/ℏ under DC bias) provide the basis for SQUIDs (superconducting quantum interference devices), the most sensitive magnetometers known, and for the volt as defined by the SI since 1990.

**Tunneling in biology.** Per-Olov Löwdin (1963, *Reviews of Modern Physics* 35, 724) proposed proton tunneling in DNA base pairs as a possible source of spontaneous mutation. Tautomeric forms of the bases (with a proton shifted between two heteroatoms) mispair with their normally-complementary base; if the tautomer occurs during replication, a point mutation is fixed. The mechanism remains contested as a *quantitatively significant* source of mutation; thermally-driven tautomerization can do the same job. The companion should flag this as suggestive but not settled. Other biological tunneling claims (enzyme catalysis, olfaction, photosynthetic energy transfer) range from well-established (electron tunneling in respiration is uncontroversial — Marcus theory) to actively contested (quantum coherence in photosynthesis — the Engel et al. 2007 *Nature* 446, 782–786 claim has been substantially walked back in subsequent literature). [verify state of the field 2024–2026.]

**Worked example:** STM tunneling current. For a 5 Å gap with φ = 4 eV, compute the order-of-magnitude tunneling current at 1 V bias. With κ ≈ 1 Å⁻¹, exp(−2κd) = exp(−10) ≈ 4.5 × 10⁻⁵. Pre-factor depends on tip and sample density of states; for a typical metal-metal junction the current is in the nanoamp range. STM operates at picoamps to nanoamps; the math checks.

**Sources:**
- Binnig, G., Rohrer, H., Gerber, C., and Weibel, E. (1982). "Surface Studies by Scanning Tunneling Microscopy." *Physical Review Letters* 49, 57–61.
- Kahng, D. and Sze, S. M. (1967). "A floating-gate and its application to memory devices." *Bell System Technical Journal* 46(6), 1288–1295.
- Josephson, B. D. (1962). "Possible new effects in superconductive tunneling." *Physics Letters* 1(7), 251–253.
- Löwdin, P.-O. (1963). "Proton Tunneling in DNA and Its Biological Implications." *Reviews of Modern Physics* 35(3), 724–732.

---

## B. Domain examples and cases

### Case 1 — The 2022 Nobel and the closing of the loopholes

The 2022 Nobel Prize in Physics went to Aspect, Clauser, and Zeilinger for "experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science." The Nobel committee's citation is unusual in naming "quantum information science" as a field — the prize is awarded for the *closure* of a fifty-year argument, not the opening. The companion can use this as the framing case: from EPR's 1935 thought experiment to a 2022 Nobel, a single thread of theory and experiment took nine decades to fully close. There is no more honest pedagogical narrative about "what does it mean for quantum mechanics to be right" than this one. [https://www.nobelprize.org/prizes/physics/2022/press-release/]

### Case 2 — The 1960 ruby laser and the path from theory to artifact

Einstein's 1917 paper gave the theoretical basis (B coefficient, stimulated emission). Schawlow and Townes 1958 (*Physical Review* 112, 1940) proposed the "optical maser." Maiman 1960 built the first working device. The 43-year gap from prediction to artifact is shorter than most pedagogically-clean cases (Bell's theorem took 31 years from theorem to first violation; Higgs took 48 years from prediction to detection); the laser is a fast-feedback case where each theoretical step had an immediate experimental program attached. By 1962 there were He-Ne, semiconductor, and CO₂ lasers; by 2026 lasers are a 10-figure annual industry. The companion can name this trajectory.

### Case 3 — The 1986 high-T_c discovery and a still-open theory

Bednorz and Müller's discovery is the most dramatic case in modern condensed-matter physics of an experimental result outrunning theoretical explanation. Forty years later [verify — Bednorz/Müller 1986 to "as of 2026" is 40 years], the mechanism of pairing in the cuprates is still contested. The companion can use this as a deliberate counter-example to the implicit narrative that physics always closes loops cleanly. Some loops remain open for a long time, and saying so is more honest than pretending otherwise.

### Failure case — "Quantum supremacy means quantum computers are now useful"

The 2019 Google Sycamore claim (*Nature* 574, 505) demonstrated that a 53-qubit superconducting processor could sample from a specific random circuit's output distribution in 200 seconds, while the best classical simulation at the time was estimated to require ~10,000 years. The estimate was revised within months as classical algorithms improved (IBM 2019; subsequent tensor-network and Monte Carlo methods brought the classical runtime down by many orders of magnitude). More importantly, the *sampling task itself has no use* — it's a benchmark, not a problem someone needed solved. The companion should name this failure mode by name: a quantum computer demonstration that does a hard-to-simulate-classically thing is not the same as a quantum computer demonstration that solves a problem someone cared about. The latter has not happened as of 2026 [verify].

---

## C. Connections and dependencies

**Prerequisites:** All previous units. In particular: Unit 5 (formalism — measurement postulate and tensor products for entanglement); Unit 7 (angular momentum for spin-1/2 algebra in Bell tests); Unit 8 (identical particles for Cooper pairs); Unit 9 (Fermi's golden rule for lasers, time-dependent perturbation theory for qubit gates, WKB for tunneling applications).

**Unlocks:** Solid-state physics (Bloch theorem); quantum information and quantum computing (Nielsen-Chuang level); quantum field theory (entanglement entropy, AdS/CFT pedagogy starts from finite-dimensional entangled states).

**Adjacent unit connections:**
- Unit 5 → Unit 10: the measurement postulate and the no-signaling theorem are the technical machinery that makes Bell's theorem work and forbid faster-than-light communication.
- Unit 9 → Unit 10: Fermi's golden rule applied to atom-field coupling gives the Einstein A and B coefficients; WKB gives the STM and alpha-decay rates; time-dependent perturbation theory gives qubit gate dynamics.
- Unit 10 → outside the book: solid-state physics (Ashcroft & Mermin); quantum information (Nielsen-Chuang); quantum optics (Loudon); high-energy physics (Peskin & Schroeder).

---

## D. Current state of the field

**Settled:**
- Local hidden-variable theories of the EPR form are ruled out at >10σ by loophole-free Bell tests.
- Laser physics is engineering, not research, for most wavelengths. Active research in extreme regimes (attosecond, X-ray free-electron lasers, hard-X-ray amplification) continues, but the conventional laser is settled physics.
- BCS theory accounts for conventional (low-T_c, phonon-mediated) superconductivity to high precision.
- STM, flash memory, and Josephson junctions are settled technologies.

**Active research:**
- *Quantum computing.* Both hardware (superconducting, trapped-ion, neutral-atom, photonic, topological) and software (algorithms, error correction, benchmarking). Moving fast. The Google 2023 surface-code result was a key milestone; the question of whether scaling will continue gracefully is the open empirical question of the next decade. As of 2026 [verify], no demonstrated useful quantum advantage on a classically-hard problem of practical interest.
- *High-T_c and unconventional superconductivity.* Cuprate mechanism contested; iron-based superconductors (Hosono 2008 *Journal of the American Chemical Society* 130, 3296) opened a second family of high-T_c materials with their own mechanism questions. Nickelate superconductors (2019, Hwang group at Stanford) are a third family. Hydride superconductors at high pressure approach room temperature but require extreme conditions [verify status post-Dias retractions].
- *Quantum biology.* Photosynthetic energy transfer, avian magnetoreception (radical-pair mechanism, Hore and Mouritsen 2016 *Annual Review of Biophysics* 45, 299), enzyme tunneling. Field-wide reckoning post-2007 with whether long-lived coherence really plays a role in biological function. [verify recent reviews, e.g., Cao et al. 2020 *Science Advances*.]
- *Quantum simulation.* Ultracold-atom simulators of Hubbard models and gauge theories; trapped-ion simulators of spin chains; programmable simulators (QuEra, ColdQuanta). One of the few near-term claims of practical quantum advantage that may hold up.
- *Post-quantum cryptography.* NIST finalized FIPS 203/204/205 in August 2024 (CRYSTALS-Kyber, CRYSTALS-Dilithium, SPHINCS+); migration of internet infrastructure is in progress and will be a major focus through the late 2020s [https://csrc.nist.gov/projects/post-quantum-cryptography].

**Key references:**
- Nielsen, M. A. and Chuang, I. L. (2010). *Quantum Computation and Quantum Information.* Cambridge University Press.
- Ashcroft, N. W. and Mermin, N. D. (1976). *Solid State Physics.* Holt, Rinehart, Winston.
- Tinkham, M. (2004). *Introduction to Superconductivity*, 2nd ed. Dover. [Standard reference, includes BCS and high-T_c.]
- Loudon, R. (2000). *The Quantum Theory of Light*, 3rd ed. Oxford. [Standard for stimulated emission, coherent states, laser theory at intermediate level.]

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **"Entanglement allows FTL communication."** The most stubborn misconception in the unit. The companion should spend a paragraph on the no-signaling theorem with the marginal probability written out: P(b|a, x, y) = P(b|y), independent of Alice's choice x. Once they see the marginals don't change, the conceptual block usually clears.

2. **"Quantum computers are exponentially faster than classical computers at everything."** No. Quantum computers are exponentially faster than the best known classical algorithms for *specific* problems (factoring, Shor's; discrete log, Shor's; certain quantum simulation problems). Most problems do not admit quantum speedup; many admit only quadratic speedup (Grover); a few admit exponential speedup. The companion should name this carefully. The complexity class BQP is *not* known to contain NP.

3. **"Superconductivity is just zero resistance."** Three things: zero resistance, Meissner-effect flux expulsion, and a quantum-mechanical wave function with macroscopic phase coherence. The third is where the Josephson effect comes from and is more fundamental than the first two. Worth a paragraph.

4. **"The laser is coherent because all the photons are identical."** Misleads. Coherent light is in a coherent state of the EM field; identical photons (Bose statistics) is a prerequisite but not the explanation. Coherent states are quasi-classical states of the field. The chapter can spend half a page on this and the student's quantum-optics future will be easier.

**Analogies that work:**
- Bell-inequality violation as "the correlations are stronger than any classical box could produce" — anchors the operational meaning without metaphysics.
- Cooper pair as "a many-body composite that resists being torn apart at low temperature" — gets the energy-gap intuition without committing to a microscopic picture.
- STM as "a quantum amplifier of distance" — the exponential sensitivity is the entire reason it works.

**Analogies that mislead:**
- "Quantum bits hold both 0 and 1 at once." Pop-sci shorthand that confuses superposition with classical probabilistic uncertainty. Superposition is a *complex* linear combination, with phases that interfere — and the interference is what gives quantum algorithms their power. Replace with: "A qubit's state is a complex linear combination α|0⟩ + β|1⟩, and the phases of α and β matter — that's what 'quantum' adds to 'probabilistic.'"
- "Superconductors levitate because of magnetic force." Levitation in a Type-II superconductor with flux pinning is more nuanced than that — flux lines are pinned at defect sites, locking the position. Type-I shows pure diamagnetic Meissner levitation. Both are real, neither is just "magnetic repulsion."

**Exercises (Bloom's level):**
- **Knowledge:** State Bell's theorem; write the Einstein A/B relations; write a single-qubit state on the Bloch sphere; state the BCS gap relation 2Δ/kT_c = 3.53. (L1)
- **Application:** Compute the CHSH value for the singlet state with given measurement axes; compute the threshold population inversion for a four-level laser; compute the STM current ratio for a 1 Å gap change. (L3)
- **Analysis:** Given a published "quantum advantage" claim, identify the task, the classical-runtime estimate, and whether the task has utility. (L4)
- **Evaluation:** Read the abstract of a recent high-T_c paper; evaluate the claimed T_c and mechanism. (L5)
- **Synthesis:** Derive the Einstein A/B coefficients from Fermi's golden rule and the photon density of states; relate to laser threshold conditions. (L6)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 12 (Afterword) covers Bell's theorem and EPR at exactly the right level for this unit; Ch. 9 covers laser physics via Fermi's golden rule; Ch. 5.3 (in 3rd edition) covers the Kronig-Penney model. (`822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt` in pantry; verify section numbers against current edition — Ch. 12 is the afterword in some editions and an integrated chapter in others.)
- **Liboff, *Introductory Quantum Mechanics*** — has a chapter on solids and Bloch theory with more detail than Griffiths; useful for the band-structure portion. (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`)
- **Pop-sci references** — Ch. 7 (entanglement) is the single best chapter in the pop-sci book per TIKTOC; use directly. Ch. 9 (tunneling applications) is the best applications catalog; use directly. Ch. 14 (lasers) is thorough; use directly. Ch. 16 (quantum computing) is motivation-only; companion adds math. Ch. 17 (superconductivity) is good historical narrative; companion adds BCS gap equation and high-T_c context.
- **`_lib_QM-Into-the-Light-Beginners.md`** — pop-sci reference notes; useful for the entanglement and quantum-computing narrative voice.
- **`_lib_Nielsen-Reinventing-Discovery.md`** — Michael Nielsen on open science and quantum computing; may supply framing on the quantum-computing arc and the relationship between hardware and algorithm progress.
- **`_lib_Davies-Demon-in-the-Machine.md`** — Davies on information physics, possibly relevant to the quantum-computing section's conceptual framing (information as a physical resource).
- **`_lib_The-Blind-Spot.md`** — possibly relevant to the entanglement / measurement-foundations material; check whether the authors engage Bell's theorem.
- **`_lib_Penrose-Emperors-New-Mind.md`** — Penrose on quantum mechanics and computation; useful as a contrary-view reference if the chapter wants to engage critics of the quantum-computing program.

---

## G. Gaps and flags

**Aging-risk flags (Unit 10 specifically — this unit ages faster than any other in the book):**

- **AGING:** Quantum computing hardware counts and milestone claims move every 6–18 months. As of 2026, the largest superconducting processor is in the ~1,000-qubit range, and the first sub-threshold logical qubit was demonstrated by Google in 2023. Any sentence with a specific qubit count or specific company will need re-verification in 2027 and again every year after. Recommend: write numbers with "as of 2026 [verify]" inline, and ensure the chapter survives revision by leaning on the *structure* of progress (NISQ → fault-tolerance → quantum advantage) rather than specific milestones.

- **AGING:** Post-quantum cryptography migration. NIST FIPS 203/204/205 standardized in August 2024 [https://csrc.nist.gov/projects/post-quantum-cryptography — verify current standards]. Adoption rates in industry will change rapidly through the late 2020s.

- **AGING:** High-T_c superconductivity. The Dias retractions (2022–2024) have left the room-temperature-superconductivity record in a contested state. The LK-99 episode (2023) further muddied the public discourse. As of 2026, the highest-T_c claim that has survived independent reproduction is [verify — likely still in the high-200 K range under high-pressure hydrides]. The companion should describe the field's state honestly and label uncertainty.

- **AGING:** Quantum biology — photosynthetic coherence claims have walked back substantially since the 2007 Engel paper. Recent reviews (2020–2024) generally describe coherence as short-lived and not the dominant mechanism in energy transfer. Avian magnetoreception (radical-pair) is more durable but still active. [verify status of major claims 2024–2026.]

- **AGING:** Loophole-free Bell tests have continued past the 2015 trio. Notably, NIST and other groups have extended the tests with cosmologically-distant random bits as the basis-choice source ("BIG Bell Test" 2018; Handsteiner et al. 2017 *Physical Review Letters* 118, 060401, using starlight). [verify any 2024–2026 advances.]

**Other flags:**

- **FLAG:** Bell's theorem is at the edge of foundational physics and philosophy. The companion should not relitigate the interpretation question (many-worlds vs. Copenhagen vs. QBism vs. Bohmian) — that's a different book. Stick to "local hidden variables are ruled out at >10σ; what remains is constrained, but not unique."

- **FLAG:** The "supercurrent persists indefinitely" claim — measurements of supercurrent decay rates (Quinn and Ittner 1962 *Journal of Applied Physics*) put lower bounds of >10⁵ years for typical superconducting rings. Sometimes pop-sci sources claim "exactly zero" decay; the experimental claim is "below detection limit." Calibrate the language.

- **FLAG:** Griffiths Ch. 12 (Afterword on Bell's theorem) is in the older editions; in the 3rd edition (2018) the Bell material is integrated into the formalism chapters. [verify section number for chosen edition.]

- **FLAG:** "Quantum advantage" vs. "quantum supremacy" — Google's 2019 term "quantum supremacy" was politically retreated from in subsequent literature; "quantum advantage" is now standard. The companion should use "quantum advantage" throughout.

- **GAP:** Bose-Einstein condensation as a topic — covered in Unit 8 §B.1 (Cornell/Wieman/Ketterle 1995). Could be revisited in Unit 10 as a "quantum mechanics in the modern world" application. Recommend: brief forward-reference rather than full redevelopment.

- **GAP:** Decoherence as a topic. Crucial for quantum computing (the reason error correction matters) and for the measurement problem. The companion could spend a paragraph on this; recommend a brief treatment in the quantum computing section where it earns its place by explaining why qubits are hard.

- **GAP:** Quantum cryptography (BB84, E91 protocols). Currently absent from the unit per the TIKTOC outline. Could be added as a one-paragraph note in the quantum computing section. BB84: Bennett and Brassard 1984, *Proceedings of IEEE International Conference on Computers, Systems and Signal Processing*, 175–179. E91: Ekert 1991 *Physical Review Letters* 67, 661.

- **FLAG:** Length budget. Six topics at the depth proposed (entanglement, lasers, semiconductors, quantum computing, superconductivity, tunneling applications) will press hard against 3,500 words. Recommend: pick two for full deep-dive (suggest entanglement + Bell, and quantum computing + qubits), treat the other four at "mechanism + worked example + sources" depth. Or scope back — drop one topic to a forward-reference.
