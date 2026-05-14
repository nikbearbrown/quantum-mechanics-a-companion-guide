# Unit 10 — Quantum Mechanics in the Modern World

> Bell's theorem is now a Nobel Prize. Lasers are a 10-figure industry. Quantum computing is a hardware race. Foundational quantum mechanics has stopped being only philosophy.

---

## 1. What this chapter is doing

In October 2022 the Nobel Committee for Physics awarded the prize to Alain Aspect, John Clauser, and Anton Zeilinger ["for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"](https://www.nobelprize.org/prizes/physics/2022/press-release/). The award is unusual in two ways. First, it names "quantum information science" as a field — a discipline that did not exist when most of the cited work was done. Second, it is a Nobel Prize for closing a *foundational* argument: from Einstein, Podolsky, and Rosen's 1935 thought experiment to the loophole-free Bell tests of 2015, a single thread of theory and experiment took eight decades to settle whether quantum mechanics could be reproduced by a local hidden-variable theory. The settled answer is no.

This unit takes six modern applications of quantum mechanics — entanglement and Bell's theorem, lasers, semiconductors, quantum computing, superconductivity, and tunneling applications — and connects each to the formalism developed in earlier units. The pop-sci companion ([*Quantum Physics for Beginners*, 2021]) does a strong narrative job on five of these six (its Ch. 7 on entanglement, Ch. 9 on tunneling applications, Ch. 14 on lasers, Ch. 16 on quantum computing, Ch. 17 on superconductivity); the companion's job in Unit 10 is to add the math the pop-sci treatments skip. The signature mathematical move of the unit is the CHSH inequality derivation — five lines of algebra that turn EPR's 1935 philosophical complaint into a quantitative experimental test.

Aging-risk warning. Specific quantum-computing qubit counts, post-quantum cryptography migration milestones, and high-$T_c$ superconductor records will all be out of date within 1–2 years of this draft (2026-05). The chapter is written so that its conceptual claims survive this aging; specific numbers are labeled `[verify, 2026]` so they can be refreshed without rewriting the surrounding logic. See §8 and §9 for details on what depends on what.

## 2. Learning objectives

By the end of this unit, you should be able to:

- **State** Bell's theorem and the CHSH inequality; the Einstein $A$ and $B$ coefficient relations; Bloch's theorem; the BCS gap relation $2\Delta/k_B T_c \approx 3.53$. (Bloom L1)
- **Derive** the CHSH bound $|S| \leq 2$ for any local hidden-variable theory and compute $S = 2\sqrt{2}$ for the singlet state at optimal measurement axes. (L4)
- **Compute** correlation functions $\langle A_i B_j \rangle$ for the spin singlet using the angles $0$, $\pi/8$, $\pi/4$, $3\pi/8$. (L3)
- **Construct** single-qubit and two-qubit gates (Hadamard, Pauli, CNOT) and apply them to a small circuit. (L3)
- **Distinguish** loophole-free Bell tests from earlier tests; the Meissner effect from "perfect conductor" behavior; quantum advantage from quantum supremacy from "useful" quantum computation. (L4)
- **Evaluate** a published claim of quantum advantage by identifying the task, the classical-runtime estimate, and whether the task has utility. (L5)

## 3. The motivating problem

The 2022 Nobel announcement was, in physics terms, a verdict. Local hidden-variable theories of the form Einstein, Podolsky, and Rosen sketched in 1935 are ruled out at confidence levels equivalent to more than ten standard deviations. The verdict relies on a particular kind of theoretical and experimental machinery — an inequality, derived from minimal assumptions, that any local hidden-variable theory must satisfy; an experiment, controlled enough to test the inequality; and an outcome that violates the inequality by tens of standard deviations. The 2022 Nobel honors the line from theorem (Bell 1964) through first measurement (Aspect 1981–1982) to loophole-free measurement (Hensen, Giustina, Shalm 2015).

The mathematical content underneath the Nobel is approximately one page of algebra. It deserves all of §4.1.

## 4. Concept blocks

### 4.1 Entanglement, EPR, Bell's theorem, and the CHSH inequality (deep-dive)

Einstein, Podolsky, and Rosen ([1935, *Physical Review* 47, 777–780](https://doi.org/10.1103/PhysRev.47.777)) proposed a thought experiment with two particles prepared in a correlated state and separated by a large distance. Measure position of particle A; this immediately determines what the position measurement of particle B would have to be, by the prepared correlation. EPR argued: B was spacelike-separated from A at the time of the measurement; therefore the position of B must have been a *real property* of B before the measurement on A; by the same logic the momentum of B must also have been a real property; but QM forbids assigning simultaneous definite values to position and momentum. Therefore, EPR concluded, quantum mechanics is incomplete — a hidden-variable description must underlie the quantum-mechanical one.

David Bohm reformulated the argument in 1951 (in his textbook *Quantum Theory*, Prentice-Hall) using two spin-1/2 particles in a *singlet state*:

$$ |\psi_{\text{singlet}}\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A |\downarrow\rangle_B - |\downarrow\rangle_A |\uparrow\rangle_B \right). $$

(You met this state in Unit 7 and again in Unit 8 as the spin part of parahelium's ground state.) The total spin is zero, so any spin measurement on A — along any axis — perfectly anticorrelates with the matching measurement on B. The setup is binary, the algebra is two-by-two matrices, and the philosophical content matches EPR's original.

John Bell's 1964 paper ([*Physics Physique Fizika* 1, 195–200](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)) turned the EPR argument into a *quantitative test*. Any local hidden-variable theory — any theory in which each particle has predetermined values for every measurement, with no faster-than-light coordination between A's and B's measurements — must satisfy certain inequalities. The most experimentally useful is the *CHSH* inequality, derived by Clauser, Horne, Shimony, and Holt in 1969 ([*Physical Review Letters* 23, 880–884](https://doi.org/10.1103/PhysRevLett.23.880)).

Here is the derivation. Alice has two possible measurement settings, $a_1$ and $a_2$, each producing a binary outcome $A_i \in \{+1, -1\}$. Bob has two possible settings, $b_1$ and $b_2$, with outcomes $B_j \in \{+1, -1\}$. In any local hidden-variable model, the outcomes are determined by some shared hidden variable $\lambda$ (set at the source) and the local setting:

$$ A_i = A_i(a_i, \lambda) \in \{+1, -1\}, \quad B_j = B_j(b_j, \lambda) \in \{+1, -1\}. $$

For each value of $\lambda$, all four products $A_1 B_1$, $A_1 B_2$, $A_2 B_1$, $A_2 B_2$ are well-defined numbers in $\{+1, -1\}$. Form the combination

$$ S(\lambda) = A_1 B_1 + A_1 B_2 + A_2 B_1 - A_2 B_2 = A_1(B_1 + B_2) + A_2(B_1 - B_2). $$

Now observe: since $B_1, B_2 \in \{+1, -1\}$, the pair $(B_1 + B_2)$ and $(B_1 - B_2)$ has one term equal to $\pm 2$ and the other equal to $0$ (either $B_1 = B_2$, in which case $B_1 + B_2 = \pm 2$ and $B_1 - B_2 = 0$, or $B_1 = -B_2$, in which case $B_1 + B_2 = 0$ and $B_1 - B_2 = \pm 2$). Either way, exactly one of $A_1(B_1 + B_2)$ and $A_2(B_1 - B_2)$ is $\pm 2$ and the other is $0$. So

$$ |S(\lambda)| = 2 $$

for every value of $\lambda$. Average over $\lambda$ with whatever probability distribution $P(\lambda)$ the hidden-variable theory uses:

$$ \langle S \rangle_{\text{LHV}} = \int S(\lambda) P(\lambda)\, d\lambda \implies |\langle S \rangle_{\text{LHV}}| \leq 2. $$

In terms of the experimentally measurable correlation functions $E(a_i, b_j) = \langle A_i(\lambda) B_j(\lambda) \rangle$:

$$ \boxed{|S| = |E(a_1, b_1) + E(a_1, b_2) + E(a_2, b_1) - E(a_2, b_2)| \leq 2 \quad \text{(CHSH, any LHV)}.} $$

That is the CHSH inequality. It is a constraint on the four pairwise correlation functions that any local hidden-variable theory must obey, derived from one assumption: that outcomes are predetermined functions of a hidden variable and the local setting.

Now compute the same combination for the *quantum* singlet state. The expectation value of a spin-1/2 measurement along direction $\hat{n}_A$ for particle A and direction $\hat{n}_B$ for particle B, in the singlet state, is (Unit 7)

$$ E_{\text{QM}}(\hat{n}_A, \hat{n}_B) = \langle \psi_{\text{singlet}} | (\hat{\sigma} \cdot \hat{n}_A) \otimes (\hat{\sigma} \cdot \hat{n}_B) | \psi_{\text{singlet}} \rangle = -\hat{n}_A \cdot \hat{n}_B = -\cos(\theta_{AB}), $$

where $\theta_{AB}$ is the angle between the two measurement directions. The minus sign is the signature of the singlet: anti-aligned axes ($\theta_{AB} = 180°$) give correlation $+1$ (perfect anticorrelation), aligned axes ($\theta_{AB} = 0$) give $-1$.

Pick the measurement axes that maximize $|S|$ for the singlet state. We work through the optimal choice in detail in §5; for now, take it as given that the maximum value of $|S|$ achievable by quantum mechanics for the singlet state is

$$ |S|_{\text{QM, max}} = 2\sqrt{2} \approx 2.828. $$

The clean statement is the *Tsirelson bound* ([Tsirelson 1980, *Letters in Mathematical Physics* 4, 93–100](https://doi.org/10.1007/BF00417500)): for any quantum state and any choice of measurement axes, the CHSH expression cannot exceed $2\sqrt{2}$. The singlet at optimal axes saturates this bound. Local hidden-variable theories are bounded by $2$. The gap is $2\sqrt{2} - 2 \approx 0.828$, about 41% — large enough that a finite experiment with reasonable statistics can distinguish the two predictions.

Aspect, Grangier, and Roger in 1981–1982 ([*Physical Review Letters* 49, 91](https://doi.org/10.1103/PhysRevLett.49.91); *PRL* 49, 1804](https://doi.org/10.1103/PhysRevLett.49.1804)) measured the CHSH combination for polarization-entangled photons from a calcium cascade source, with time-varying analyzers in the second paper to close the "locality" loophole. Result: $S = 2.697 \pm 0.015$, violating the Bell bound by tens of standard deviations.

The remaining loopholes — detection efficiency (most photons missed; if the detected subsample is non-representative, an LHV could mimic the violation); locality (measurement bases must be set fast enough that no light-speed signal could coordinate detectors); freedom of choice (basis choices must be independent of any hidden common cause) — were closed simultaneously for the first time in 2015 by three independent experiments:

- Hensen et al. ([*Nature* 526, 682–686](https://doi.org/10.1038/nature15759)), Delft, NV centers in diamond, separated by 1.3 km.
- Giustina et al. ([*Physical Review Letters* 115, 250401](https://doi.org/10.1103/PhysRevLett.115.250401)), Vienna, entangled photons.
- Shalm et al. ([*Physical Review Letters* 115, 250402](https://doi.org/10.1103/PhysRevLett.115.250402)), NIST Boulder, entangled photons.

The reading: local hidden-variable theories of the form EPR envisioned are ruled out at $>10\sigma$. What remains is some combination of (i) quantum mechanics is correct, (ii) signals propagate faster than light *but not in a way that allows controllable communication* (a tightrope few practicing physicists are willing to walk), (iii) some assumption of the Bell setup fails — typically counterfactual definiteness or "superdeterminism."

**Common misconception.** "Entanglement allows faster-than-light communication." It does not. The marginal probability for Bob's outcome is *unchanged* by Alice's measurement choice: $P(b | a, x, y) = P(b | y)$, where $x$ is Alice's setting, $a$ her outcome, $y$ Bob's setting, $b$ Bob's outcome. This is the *no-signaling theorem*, a theorem in quantum mechanics rather than an assumption. To learn about the *correlation* (which is non-classical), Alice and Bob must compare data, and the comparison travels at light speed. No information is transmitted faster than light by the entanglement itself.

### 4.2 Lasers and stimulated emission

Einstein 1917 ([*Physikalische Zeitschrift* 18, 121–128](https://en.wikisource.org/wiki/Translation:On_the_Quantum_Theory_of_Radiation), "On the Quantum Theory of Radiation") introduced three radiative processes between two atomic levels of energies $E_1 < E_2$:

- *Absorption*: rate $B_{12} \rho(\nu) N_1$, where $\rho(\nu)$ is the spectral energy density of the radiation field at frequency $\nu = (E_2 - E_1)/h$ and $N_1$ is the population of the lower level.
- *Spontaneous emission*: rate $A_{21} N_2$, independent of the field, depending only on the upper-level population $N_2$.
- *Stimulated emission*: rate $B_{21} \rho(\nu) N_2$, proportional to the field intensity, with the emitted photon coherent with the stimulating field.

Stimulated emission was the new piece. Einstein deduced its necessity from thermodynamic consistency. In thermal equilibrium, the rates of absorption and emission must balance, and the field must follow the Planck distribution. Setting absorption rate $=$ total emission rate at equilibrium, and using the Boltzmann ratio $N_2/N_1 = e^{-h\nu/k_B T}$, gives

$$ \boxed{\frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3}, \quad B_{21} = B_{12}} $$

for non-degenerate levels. (Both relations follow from matching Einstein's rate equation to Planck's law at thermal equilibrium; Griffiths §9.3 walks the derivation.) The first relation says spontaneous emission *dominates* at high frequency ($\nu^3$ scaling) and stimulated emission at low frequency — which is why lasing is much easier in the infrared than in the X-ray (and almost impossible in the gamma-ray with table-top sources). The second says the matrix element governing emission and absorption is the same. Both relations fall out of Fermi's golden rule (Unit 9 §4.5) applied to the atom-field coupling in the dipole approximation.

Lasing requires *population inversion*: $N_2 > N_1$. In thermal equilibrium this is impossible — Boltzmann puts most population in the lower level. Inversion is achieved by *pumping*: driving atoms into a third or fourth level from which they decay to the upper laser level faster than the laser-emission rate. Three-level (ruby) and four-level (HeNe, Nd:YAG) schemes are the canonical configurations.

Theodore Maiman built the first laser in May 1960 at Hughes Research Labs, using a ruby rod pumped by a flashlamp ([Maiman 1960, *Nature* 187, 493–494](https://doi.org/10.1038/187493a0)). Output: 694.3 nm red light in pulses. *Physical Review Letters* rejected the paper as too incremental; *Nature* published it. Within a year there were HeNe, semiconductor, and CO$_2$ lasers; by 2026, lasers are a ten-figure annual industry, used in fiber-optic communication, surgical and industrial cutting, optical storage, spectroscopy, ranging, and precision metrology.

**Common misconception.** "Lasers are coherent because all the photons are in the same state." More precise: lasers are coherent because the *electromagnetic field mode* is in a Glauber *coherent state* $|\alpha\rangle$ — an eigenstate of the photon annihilation operator $\hat{a}$, with photon-number distribution sharply peaked (Poisson) and a definite quantum phase. The classical wave picture works because coherent states are the closest a quantum field gets to a classical wave. Photons being bosons is a prerequisite — many photons can occupy the same mode — but does not by itself explain coherence.

### 4.3 Semiconductors and band theory

Felix Bloch's 1928 thesis at Leipzig ([*Zeitschrift für Physik* 52, 555–600](https://doi.org/10.1007/BF01339455), "On the Quantum Mechanics of Electrons in Crystal Lattices") established that the eigenstates of a single electron in a perfectly periodic potential $V(\mathbf{r}) = V(\mathbf{r} + \mathbf{R})$ (with $\mathbf{R}$ any lattice translation vector) take the form

$$ \psi_{n, \mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}}\, u_{n, \mathbf{k}}(\mathbf{r}), $$

where $u_{n, \mathbf{k}}(\mathbf{r})$ has the same periodicity as the lattice. This is *Bloch's theorem*. The energy $E_n(\mathbf{k})$ as a function of crystal momentum $\mathbf{k}$ forms a *band* labeled by the band index $n$. There are forbidden energy gaps between bands.

The qualitative consequences are stark. *Conductors* have a partially-filled band — the Fermi level sits in the middle of a band, with empty states immediately above filled ones, so an applied field can accelerate electrons into nearby empty states. *Insulators* have fully-filled valence bands and empty conduction bands separated by a wide gap ($\sim 5$ eV); thermal excitation cannot bridge the gap at room temperature ($k_B T \approx 0.025$ eV), so no current flows. *Semiconductors* sit in between with a smaller gap ($\sim 0.5$–$2$ eV; silicon at $1.12$ eV, gallium arsenide at $1.43$ eV), so thermal excitation populates the conduction band at room temperature in measurable amounts.

The Kronig–Penney model ([Kronig and Penney 1931, *Proceedings of the Royal Society A* 130, 499–513](https://doi.org/10.1098/rspa.1931.0019)) is the cleanest demonstration that bands and gaps emerge from solving the Schrödinger equation in a 1D periodic potential. For a 1D array of delta-function barriers $V(x) = V_0 a \sum_n \delta(x - na)$, applying Bloch's theorem and matching boundary conditions across each barrier gives a transcendental equation

$$ \cos(ka) = \cos(qa) + \frac{m V_0 a}{\hbar^2 q} \sin(qa), $$

where $q = \sqrt{2mE}/\hbar$. The left side is bounded between $\pm 1$; the right side has stretches where $|\text{RHS}| > 1$ and no real $k$ exists. Those stretches are the *forbidden gaps*. Griffiths Ch. 5.3 (third edition) walks the calculation. One of the cleanest "solving the Schrödinger equation produces band structure" derivations in the curriculum.

*Doping* shifts the equilibrium populations. *n*-type doping (phosphorus in silicon — phosphorus has five valence electrons; silicon has four; the extra electron is loosely bound) adds electrons to the conduction band. *p*-type doping (boron in silicon — boron has three valence electrons; one short) adds *holes* to the valence band. The *pn junction* — a single crystal with p-doped and n-doped regions adjacent — develops a depletion region with a built-in electric field, and is the heart of every diode, LED, photovoltaic cell, and bipolar transistor. The MOSFET (metal-oxide-semiconductor field-effect transistor), which dominates modern integrated circuits, switches current via a gate-voltage-controlled inversion layer.

**Common misconception.** "Holes are real particles." Holes are *quasi-particles* — the absence of an electron in a nearly-full band, behaving as if a positive-charge particle were moving through an empty band, with an effective mass set by the band curvature near the band edge. The mathematics works because band structure has approximate particle-hole symmetry near band extrema. Useful as a calculational device; not an entry on the table of fundamental particles.

A full three-dimensional band-structure calculation is beyond an introductory QM course; this is the boundary at which the subject hands off to solid-state physics. The standard reference is Ashcroft and Mermin, *Solid State Physics* (1976).

### 4.4 Quantum computing

A *qubit* is a two-level quantum system. The basis states are conventionally $|0\rangle$ and $|1\rangle$, and a general qubit state is

$$ |\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1. $$

A computation is a unitary operation on $N$-qubit Hilbert space (dimension $2^N$), implemented as a circuit of one- and two-qubit gates. Measurement at the end collapses the state to a classical bit string with the Born-rule probability distribution. Two ingredients distinguish quantum from classical computation: *superposition* (a single qubit can be in any complex linear combination of $|0\rangle$ and $|1\rangle$, with phase relationships that allow interference) and *entanglement* (an $N$-qubit state has $2^N$ complex amplitudes, exponentially more than the $2N$ real numbers needed to specify $N$ independent classical bits).

*One-qubit gates.* The single-qubit gates are $2 \times 2$ unitary matrices. The Pauli matrices are themselves gates:

$$ \hat{X} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\ (\text{bit flip}), \quad \hat{Y} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \hat{Z} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\ (\text{phase flip}). $$

The *Hadamard gate*

$$ \hat{H} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} $$

takes computational-basis states into superpositions: $\hat{H}|0\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, $\hat{H}|1\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$. Hadamard is the standard "load superposition" operation at the start of most quantum algorithms.

*Two-qubit gates.* The CNOT (controlled-NOT) flips the target qubit when the control qubit is $|1\rangle$:

$$ \text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \quad \text{in the basis } \{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}. $$

The CNOT plus arbitrary single-qubit unitaries is a *universal gate set* ([DiVincenzo 1995, *Physical Review A* 51, 1015](https://doi.org/10.1103/PhysRevA.51.1015)) — every multi-qubit unitary can be decomposed into this gate set with polynomially many gates. (The decomposition may itself be exponentially long for arbitrary unitaries on $N$ qubits, but this is a separate question from universality.)

Two algorithmic results anchor the field. *Shor's algorithm* ([Shor 1994, *Proceedings of FOCS '94*](https://doi.org/10.1109/SFCS.1994.365700); final version Shor 1997, *SIAM Journal on Computing* 26, 1484) factors an $n$-bit integer in $O(n^3)$ operations on a quantum computer, vs. the best known classical algorithm (general number field sieve) at $\exp(O(n^{1/3} (\log n)^{2/3}))$ — a super-polynomial speedup. If a sufficiently large fault-tolerant quantum computer existed, RSA encryption would be broken. *Grover's algorithm* ([Grover 1996, *Proceedings of STOC '96*](https://doi.org/10.1145/237814.237866)) finds a marked item in an $N$-item unsorted database in $O(\sqrt{N})$ queries vs. $O(N)$ classically — a *quadratic* speedup. Most problems do not admit quantum speedup; many admit Grover-style quadratic speedup; a small number admit Shor-style exponential speedup.

As of 2026 [verify], the field is in the NISQ ("noisy intermediate-scale quantum") era — Preskill's 2018 coinage ([*Quantum* 2, 79](https://doi.org/10.22331/q-2018-08-06-79)). Current hardware [verify, 2026]: IBM's Condor processor announced at $\sim 1{,}100$ superconducting qubits in late 2023; Google's Sycamore family in published configurations through 70 qubits; Quantinuum's H2 trapped-ion system with high-fidelity all-to-all connectivity; Atom Computing demonstrating neutral-atom arrays at $> 1{,}000$ qubits. Google reported in 2023 ([Acharya et al. 2023, *Nature* 614, 676–681](https://doi.org/10.1038/s41586-022-05434-1)) the first below-threshold logical-qubit demonstration: increasing surface-code distance from 3 to 5 reduced the logical error rate — evidence that quantum error correction scales as theory predicts, though many orders of magnitude in error rate remain to fault-tolerant operation.

The honest framing: as of mid-2026, no quantum computer has demonstrated useful speedup on a practically important problem. The 2019 "quantum supremacy" claim ([Arute et al. 2019, *Nature* 574, 505–510](https://doi.org/10.1038/s41586-019-1666-5), Google Sycamore) was a *sampling task* with no practical utility — a benchmark, not a problem someone needed solved. The classical-simulation runtime estimate was revised downward by orders of magnitude within months as classical algorithms improved. The 2020 Jiuzhang photonic claim ([Zhong et al. 2020, *Science* 370, 1460–1463](https://doi.org/10.1126/science.abe8770)) is in the same category. These are demonstrations that quantum hardware can do something hard to simulate classically; they are not demonstrations that quantum hardware can solve a problem of practical interest. The latter has not happened as of 2026 [verify].

**Common misconception.** "Quantum computers will break all encryption by 2030." Shor's algorithm threatens RSA and ECC *if and only if* a fault-tolerant quantum computer of millions of logical qubits is built. Current physical-qubit counts ($\sim 10^3$) and gate error rates ($\sim 10^{-3}$ per gate) put us many generations of progress short of factoring 2048-bit RSA keys. The practical response is *post-quantum cryptography*: cryptographic schemes whose security does not rest on integer factorization or discrete logarithms. NIST finalized FIPS 203 (CRYSTALS-Kyber, for key encapsulation), FIPS 204 (CRYSTALS-Dilithium, for signatures), and FIPS 205 (SPHINCS+, for hash-based signatures) in August 2024 [verify; current standards page at [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography)]. Migration of internet infrastructure is in progress and will be a major focus of cryptographic engineering through the late 2020s. The migration is happening *now*, in anticipation of an eventual large quantum computer — not in response to a current threat.

**Worked example.** Apply a Hadamard followed by a CNOT to the initial state $|00\rangle$:

$$ |00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle). $$

The output is a *Bell state* — a maximally entangled two-qubit state. The same circuit, in two gates, generates the entangled state at the heart of every CHSH experiment. This is the "hello world" of quantum computing: superposition (Hadamard) plus controlled interaction (CNOT) produces entanglement.

### 4.5 Superconductivity

Heike Kamerlingh Onnes at Leiden discovered in 1911 that mercury's electrical resistance drops abruptly to zero below $4.2$ K (Onnes 1911, Communications from the Physical Laboratory at the University of Leiden, No. 122b). Nobel 1913 — for the liquefaction of helium that made the low-temperature measurements possible, not directly for superconductivity. The phenomenon — resistance exactly zero (or below detection limit; measurements of supercurrent decay in superconducting rings put lower bounds at $> 10^5$ years), persistent currents lasting effectively indefinitely — was the experimental fact. The theoretical explanation took 46 years.

BCS theory (Bardeen, Cooper, Schrieffer 1957, [*Physical Review* 108, 1175–1204](https://doi.org/10.1103/PhysRev.108.1175)) supplied the mechanism. The starting observation is Cooper's: in the presence of an arbitrarily weak attractive interaction between two electrons near the Fermi surface (mediated, in conventional superconductors, by phonons — lattice vibrations), the Fermi sea is unstable against the formation of bound "Cooper pairs" of opposite-momentum, opposite-spin electrons ([Cooper 1956, *Physical Review* 104, 1189–1190](https://doi.org/10.1103/PhysRev.104.1189)). The paired electrons together have integer spin and even momentum — they are composite bosons (Unit 8 §4.2). At low temperature, the Cooper pairs *condense* into a macroscopic quantum state with a definite phase, separated from excitations by an energy gap $\Delta$.

The BCS gap equation at zero temperature is

$$ 1 = N(0) V \int_0^{\hbar\omega_D} \frac{d\varepsilon}{\sqrt{\varepsilon^2 + \Delta^2}}, $$

where $N(0)$ is the electron density of states at the Fermi level, $V$ is the strength of the phonon-mediated attractive interaction, $\omega_D$ is the Debye frequency. The solution

$$ \Delta \approx 2 \hbar \omega_D\, e^{-1/N(0)V} $$

is *non-analytic* in $V$ — perturbation theory in the small attractive coupling cannot find it, because the function $e^{-1/V}$ has all its Taylor coefficients at $V = 0$ equal to zero. This is the "essential singularity" that made BCS hard to discover. Bardeen, Cooper, and Schrieffer found it through a variational ansatz (the BCS wave function), not perturbation theory.

Zero resistance follows. The current carriers are Cooper pairs; pair-breaking requires supplying energy $2\Delta$; at temperature $k_B T \ll \Delta$, no scattering process can supply this energy, and the supercurrent flows without dissipation. The supercurrent also expels magnetic flux from the interior of the material — the *Meissner effect* ([Meissner and Ochsenfeld 1933, *Naturwissenschaften* 21, 787–788](https://doi.org/10.1007/BF01504252)) — which distinguishes a superconductor from a hypothetical perfect conductor.

The BCS prediction $2\Delta/k_B T_c \approx 3.53$ is *universal* in the weak-coupling limit and holds across the conventional superconductors. For aluminum, $\Delta \approx 0.17$ meV predicts $T_c \approx 1.1$ K; measured $T_c = 1.18$ K. The prediction is within 7%, and this is the strongest evidence that BCS captures the conventional-superconductor mechanism correctly.

Bednorz and Müller's 1986 discovery of high-$T_c$ superconductivity in copper-oxide perovskites ([Bednorz and Müller 1986, *Zeitschrift für Physik B* 64, 189–193](https://doi.org/10.1007/BF01303701)) broke the picture. La$_{2-x}$Ba$_x$CuO$_4$ at $T_c \approx 35$ K (above the $\sim 30$ K theoretical ceiling for BCS phonon-mediated pairing); then YBa$_2$Cu$_3$O$_7$ at $T_c \approx 93$ K ([Wu et al. 1987, *Physical Review Letters* 58, 908](https://doi.org/10.1103/PhysRevLett.58.908)), above the liquid-nitrogen boiling point of 77 K and therefore economically practical; eventually HgBa$_2$Ca$_2$Cu$_3$O$_{8+\delta}$ at $T_c \approx 135$ K under ambient pressure. Nobel 1987, the fastest in the history of the prize. Under extreme pressure, hydrogen sulfide H$_3$S reaches $\sim 203$ K ([Drozdov et al. 2015, *Nature* 525, 73–76](https://doi.org/10.1038/nature14964)) and lanthanum hydride LaH$_{10}$ reaches $\sim 250$ K at $\sim 170$ GPa ([Somayazulu et al. 2019, *Physical Review Letters* 122, 027001](https://doi.org/10.1103/PhysRevLett.122.027001)). Room-temperature ambient-pressure superconductivity has not been demonstrated as of 2026 [verify]. The Dias retractions (2022–2024) and the LK-99 episode (2023, not reproduced and widely regarded as debunked) muddied the public discourse around recent claims; the lesson is that room-temperature superconductivity has a track record of false alarms, and any new claim should be evaluated against independent reproduction rather than press releases.

The high-$T_c$ mechanism remains contested. Phonon-mediated pairing of standard BCS form is too weak to account for $T_c \sim 100$ K in the cuprates. Spin-fluctuation-mediated pairing, charge-ordering instabilities, and other strong-correlation mechanisms are leading candidates but no single mechanism commands consensus as of 2026 [verify].

**Common misconception.** "Superconductors are perfect conductors." Not quite. A perfect conductor would maintain whatever flux it had when cooled through its transition; a superconductor *expels* flux entirely (Meissner). The Meissner effect distinguishes superconductors from hypothetical perfect conductors and falls out of BCS theory (the supercurrent screens the field within a London penetration depth $\sim 100$ nm).

### 4.6 Tunneling applications

Quantum tunneling — the WKB transmission formula from Unit 9 §4.4 — produces a long catalog of technologies and natural phenomena. The pop-sci book Ch. 9 has an excellent list; the companion adds the math.

**Scanning tunneling microscopy (STM).** Gerd Binnig and Heinrich Rohrer at IBM Zurich 1981–1982 ([Binnig et al. 1982, *Physical Review Letters* 49, 57–61](https://doi.org/10.1103/PhysRevLett.49.57)); Nobel 1986. A sharp metal tip is brought ångström-close to a conducting surface; electrons tunnel through the vacuum gap. The tunneling current depends exponentially on the gap distance $d$:

$$ I \propto e^{-2\kappa d}, \quad \kappa \approx \sqrt{2 m_e \phi}/\hbar, $$

where $\phi$ is the work function (typical metals: $\phi \approx 4$ eV, giving $\kappa \approx 1$ Å$^{-1}$). A 1 Å change in $d$ changes the current by a factor of $e^{2} \approx 7.4$. STM resolves individual atoms because the tunneling current is dominated by the single closest atom on the tip — the exponential sensitivity does the entire trick. Worked example: for a 5 Å gap with $\phi = 4$ eV, $e^{-2\kappa d} = e^{-10} \approx 4.5 \times 10^{-5}$; with reasonable tip and sample density of states the current is in the nanoamp range. STMs operate at picoamps to nanoamps; the math checks.

**Flash memory.** The floating-gate transistor ([Kahng and Sze 1967, *Bell System Technical Journal* 46, 1288](https://doi.org/10.1002/j.1538-7305.1967.tb01738.x)) writes a bit by tunneling electrons through a thin oxide layer onto an isolated "floating gate"; reads by sensing whether the charge on the floating gate has shifted the transistor's threshold voltage. The reason flash retains data for years without power is that the tunneling rate at low voltage is exponentially small — the same WKB exponential that makes alpha-decay half-lives span 24 orders of magnitude makes flash retain data over decades while still being writable at high voltage.

**Alpha decay.** Gamow 1928 ([*Zeitschrift für Physik* 51, 204–212](https://doi.org/10.1007/BF01343196)) modeled the alpha particle as a wave packet inside a finite-range nuclear potential, tunneling through the Coulomb barrier outside. The WKB tunneling formula reproduces the Geiger–Nuttall relation $\log(T_{1/2}) \propto Z/\sqrt{E_\alpha}$ from first principles — the first nuclear-physics calculation done with quantum mechanics.

**Josephson junctions and SQUIDs.** Cooper-pair tunneling across an insulating barrier between two superconductors ([Josephson 1962, *Physics Letters* 1, 251–253](https://doi.org/10.1016/0031-9163(62)91369-0)). The *DC Josephson effect* (supercurrent across the junction at zero voltage) and *AC Josephson effect* (oscillating current at frequency $2eV/\hbar$ under DC bias) underlie SQUIDs — superconducting quantum interference devices, the most sensitive magnetometers known — and the SI definition of the volt since 1990.

**Tunneling in biology.** Per-Olov Löwdin ([1963, *Reviews of Modern Physics* 35, 724](https://doi.org/10.1103/RevModPhys.35.724)) proposed proton tunneling in DNA base pairs as a possible source of spontaneous mutation: a tautomeric form of a base (proton shifted between two heteroatoms) mispairs with its normally-complementary base, and a replication event during the tautomer's lifetime fixes a point mutation. The mechanism is real; whether it is *quantitatively significant* compared to thermal tautomerization is debated. Other biological-tunneling claims range from well-established (electron tunneling in respiratory and photosynthetic electron-transport chains — Marcus theory) to disputed. The 2007 claim of long-lived quantum coherence in photosynthetic energy transfer ([Engel et al. 2007, *Nature* 446, 782–786](https://doi.org/10.1038/nature05678)) has been substantially walked back in subsequent literature [verify, 2024–2026]; current consensus is that coherences are present but short-lived and not the dominant mechanism for energy transfer efficiency. Avian magnetoreception via radical-pair chemistry ([Hore and Mouritsen 2016, *Annual Review of Biophysics* 45, 299](https://doi.org/10.1146/annurev-biophys-032116-094545)) is more durable as a quantum-biology candidate but the molecular details are still active research.

## 5. Worked example — the CHSH violation for the singlet state (full)

The signature mathematical calculation of this unit. Take Alice's and Bob's measurement axes (in the plane perpendicular to the photon propagation direction, parameterized by polarization angle):

$$ a_1 = 0, \quad a_2 = \pi/4, \quad b_1 = \pi/8, \quad b_2 = -\pi/8. $$

(One standard optimal choice — there are equivalent choices related by rotation.) The angles between Alice's and Bob's axes are:

$$ \theta_{11} = a_1 - b_1 = -\pi/8, \quad \theta_{12} = a_1 - b_2 = \pi/8, $$

$$ \theta_{21} = a_2 - b_1 = \pi/8, \quad \theta_{22} = a_2 - b_2 = 3\pi/8. $$

For the spin singlet, the correlation function is $E(\hat{n}_A, \hat{n}_B) = -\cos(\theta_{AB})$. Compute each:

$$ E(a_1, b_1) = -\cos(\pi/8), $$

$$ E(a_1, b_2) = -\cos(\pi/8), $$

$$ E(a_2, b_1) = -\cos(\pi/8), $$

$$ E(a_2, b_2) = -\cos(3\pi/8). $$

The CHSH combination:

$$ S = E(a_1, b_1) + E(a_1, b_2) + E(a_2, b_1) - E(a_2, b_2) $$

$$ S = -3\cos(\pi/8) + \cos(3\pi/8). $$

Use $\cos(\pi/8) = \cos(22.5°) \approx 0.9239$ and $\cos(3\pi/8) = \cos(67.5°) \approx 0.3827$:

$$ S \approx -3(0.9239) + 0.3827 \approx -2.772 + 0.383 \approx -2.389. $$

$|S| \approx 2.389$. This already violates the local hidden-variable bound of $2$, but it does not saturate the Tsirelson bound of $2\sqrt{2} \approx 2.828$.

The optimal axes for saturating Tsirelson are (one valid choice):

$$ a_1 = 0, \quad a_2 = \pi/2, \quad b_1 = \pi/4, \quad b_2 = -\pi/4. $$

With these angles, the four pairs are:

$$ \theta_{11} = -\pi/4, \quad \theta_{12} = \pi/4, \quad \theta_{21} = \pi/4, \quad \theta_{22} = 3\pi/4. $$

And:

$$ E(a_1, b_1) = -\cos(\pi/4) = -1/\sqrt{2}, $$

$$ E(a_1, b_2) = -\cos(\pi/4) = -1/\sqrt{2}, $$

$$ E(a_2, b_1) = -\cos(\pi/4) = -1/\sqrt{2}, $$

$$ E(a_2, b_2) = -\cos(3\pi/4) = +1/\sqrt{2}. $$

$$ S = -1/\sqrt{2} - 1/\sqrt{2} - 1/\sqrt{2} - 1/\sqrt{2} = -4/\sqrt{2} = -2\sqrt{2}. $$

$|S| = 2\sqrt{2} \approx 2.828$, saturating Tsirelson. The LHV bound is $2$; quantum mechanics gives $2\sqrt{2}$; the experimental measurement (in modern loophole-free tests) gives $S = 2\sqrt{2}$ within statistical error.

This is the calculation that turned EPR into experimental physics. Five lines of trigonometry, applied to the singlet state of two spin-1/2 particles, gives a number that no local hidden-variable theory can reproduce. The Nobel Committee gave the 2022 prize for the experiments that did the measurement; the experiments measure the same number this calculation predicts.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Entanglement, EPR, Bell | Ch. 12 (Afterword in 1st ed.; integrated in 3rd) | Ch. 7 ✅ | §4.1 (deep-dive: full CHSH derivation) |
| Lasers and stimulated emission | Ch. 9.3 | Ch. 14 ✅ | §4.2 (Einstein A/B, population inversion) |
| Semiconductors / band theory | Ch. 5.3 (3rd ed.) — Kronig–Penney | Ch. 4 (motivation only) | §4.3 (Bloch theorem, Kronig–Penney sketch, doping) |
| Quantum computing | not covered directly | Ch. 16 (motivation only) | §4.4 (qubits, gates, Shor/Grover, NISQ context) |
| Superconductivity | not covered directly | Ch. 17 ✅ historical | §4.5 (BCS gap equation, high-$T_c$ context) |
| Tunneling applications | Ch. 8 indirectly (WKB) | Ch. 9 ✅ excellent | §4.6 (STM math, flash, Josephson, biology) |

The pop-sci book pulls more weight in Unit 10 than in any other unit. Use Ch. 7 (entanglement), Ch. 9 (tunneling applications), Ch. 14 (lasers), Ch. 17 (superconductivity history) as the narrative motivation reading. This companion supplies the math each pop-sci chapter omits.

## 7. Exercises

**E1 (L1, Knowledge).** State the CHSH inequality and the Tsirelson bound. Write the Einstein $A/B$ coefficient relations. Write a single-qubit state in terms of two angles on the Bloch sphere. State the BCS universal ratio $2\Delta/k_B T_c$.

**E2 (L3, Application).** Compute the CHSH expression $S$ for the spin singlet at the measurement angles $a_1 = 0, a_2 = \pi/4, b_1 = \pi/8, b_2 = 3\pi/8$. Show your work and verify the result against the optimal $2\sqrt{2}$.

**E3 (L3, Application).** A two-qubit circuit applies a Hadamard to the first qubit, then a CNOT with the first qubit as control and the second qubit as target. The initial state is $|00\rangle$. Compute the final state. Identify it as one of the four Bell states.

**E4 (L3, Application).** Compute the STM tunneling-current ratio for a 1 Å change in tip-sample gap, assuming work function $\phi = 4$ eV. Use $\kappa \approx 1$ Å$^{-1}$ and $I \propto e^{-2\kappa d}$. Why does this single-number sensitivity matter for atomic-resolution imaging?

**E5 (L4, Analysis).** A 2024 press release claims a quantum computer has demonstrated "quantum advantage" on a problem. Identify the three things you would need to check before believing the claim: (a) the *task* being solved, (b) the *classical-runtime estimate* and the algorithms used in the estimate, and (c) whether the task has *practical utility*. Apply this checklist to one published claim of your choice — describe the task, the classical estimate, and whether the result was useful.

**E6 (L5, Evaluation).** Read the abstract of one of the three 2015 loophole-free Bell-test papers (Hensen et al. *Nature*, Giustina et al. *PRL*, or Shalm et al. *PRL*). Identify the loopholes the experiment claims to close and the statistical strength of the violation. What assumption of the Bell setup remains in principle un-closeable, and why?

**E7 (L6, Synthesis).** Derive the Einstein $A/B$ coefficient relations from Fermi's golden rule (Unit 9 §4.5) applied to the dipole coupling $\hat{H}'_{\text{dipole}} = -e \hat{\mathbf{r}} \cdot \mathbf{E}(t)$ between an atom and the radiation field. Use the photon density of states $\rho(\omega) = \omega^2 V/(\pi^2 c^3)$ for a quantized field in a box of volume $V$. Show that the ratio $A_{21}/B_{21}$ comes out to $8\pi h \nu^3/c^3$, matching Einstein's thermodynamic derivation.

## 8. What would change my mind

The aging structure of this chapter is asymmetric. Some claims are stable; others depend on specific numbers that will move.

*Stable claims (unlikely to age).* Local hidden-variable theories of the EPR form are ruled out by Bell tests. The Einstein $A/B$ relations and the laser principle hold. Bloch's theorem and band theory hold. BCS theory accounts for conventional superconductivity. WKB tunneling explains STM, flash memory, and alpha decay. These survive any reasonable update.

*Claims with aging risk over 1–2 years.* The current state of quantum-computing hardware (qubit counts, error rates, error-correction milestones) will be obsolete by 2027 [verify]; the *structure* of progress (NISQ era $\to$ early fault-tolerance demonstrations $\to$ eventual quantum advantage on useful problems) is more durable than any specific number. The current state of high-$T_c$ superconductivity records (highest $T_c$ under ambient pressure, highest $T_c$ under high pressure) will move; the *mechanism question* (whether cuprate pairing is phonon-mediated, spin-fluctuation-mediated, or otherwise) will likely still be contested in 2027 [verify]. Post-quantum cryptography adoption rates will change rapidly; the *standards themselves* (FIPS 203/204/205) are stable.

What would force a substantial rewrite of this chapter? Four scenarios:

A demonstration of *useful quantum advantage* — a quantum computer solving a problem of practical interest faster than any classical algorithm — would change §4.4 significantly. The structural prediction would survive, but the timeline framing would shift.

A *reproducible room-temperature, ambient-pressure superconductor* would change §4.5 significantly. This has been claimed several times in 2020–2024 and has not survived independent reproduction; if and when one does, that's news.

A *credible Bell-inequality experimental anomaly* — an experiment in a regime where QM predicts $S > 2$ that fails to find a violation — would force reconsideration of §4.1. None has been reported in sixty years of increasingly careful experiments.

A *loophole-free demonstration that quantum-biological coherence is essential to a biological function* (photosynthesis efficiency, enzymatic rate enhancement, magnetoreception) would strengthen §4.6's biology paragraph. The opposite outcome (further consensus that biological coherence is short-lived and not functionally significant) would weaken it. The field has been moving in the latter direction since 2014 [verify].

The general structure of the chapter — six topics, with the CHSH derivation as the signature math — survives all of these. The numbers will move; the framework should hold.

## 9. Still puzzling

- *Bell's theorem rules out local hidden variables, not "local realism."* The exact wording of what is ruled out depends on which assumptions you take as Bell's. The standard reading: counterfactual definiteness (each particle has a definite value for every possible measurement, whether or not the measurement is performed) plus locality (no influence between spacelike-separated events) plus freedom of choice (the experimenter's choices are not predetermined by some common cause) together imply CHSH $\leq 2$. The experiment rules out their conjunction. Different interpretations of QM (many-worlds, QBism, Bohmian, retrocausal, superdeterministic) drop different ones. The chapter does not relitigate the interpretation question — that is a different book.

- *Why is the spectrum of high-$T_c$ pairing mechanisms so wide?* Forty years after the 1986 discovery, no single mechanism commands consensus for the cuprates. Several candidates fit some data and not others. This may indicate that the cuprates are in a regime where multiple coupling channels compete; it may indicate that current theoretical methods cannot solve the relevant strongly-correlated electron problem. I find this honestly puzzling — it is one of the rare cases in modern condensed-matter physics where a major experimental phenomenon has resisted theoretical closure for decades.

- *What is the actual landscape of useful quantum algorithms?* Shor's algorithm gives exponential speedup for factoring. Grover's gives quadratic speedup for unstructured search. Quantum simulation of quantum systems gives plausible exponential speedup for certain Hamiltonians. Beyond that, the list of quantum algorithms with proven super-polynomial speedup on practically relevant problems is short. Whether the list will grow significantly is open. The complexity class BQP (problems solvable in polynomial time on a quantum computer) is *not* known to contain NP — quantum computers do not in general solve NP-complete problems in polynomial time.

- *Does anyone fully understand the laser?* The semiclassical theory (Einstein $A/B$ coefficients + rate equations + cavity Q factor) does everything most practical engineers need. The full quantum-optical theory (Glauber coherent states, quantum-mechanical phase noise, photon statistics in the lasing transition) does more. But the phase transition of the lasing threshold itself — at the onset of stimulated emission, what is the *quantum* nature of the field state? — remains a topic where I have read three textbooks and still feel I am being shown different pictures of the same elephant.

- *The 2022 Nobel and what it does not settle.* Aspect, Clauser, and Zeilinger established experimentally that local hidden variables of the EPR form do not describe quantum correlations. They did not settle which interpretation of QM is correct. They did not settle whether quantum mechanics is *foundationally complete* or whether it is the right large-scale limit of some more fundamental theory. They did not settle whether information is preserved in black holes, or whether quantum gravity exists, or whether the wave function is "real." The Nobel is for closing one specific argument — and an important one — but the foundational discussion continues.

**Tags:** entanglement, bell-theorem, chsh-inequality, epr-paradox, lasers, einstein-coefficients, semiconductors, bloch-theorem, band-theory, quantum-computing, qubits, shor-algorithm, grover-algorithm, superconductivity, bcs-theory, high-tc, tunneling-applications, stm, flash-memory, josephson-junction, post-quantum-cryptography, aspect-clauser-zeilinger-2022
