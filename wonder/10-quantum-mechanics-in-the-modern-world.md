# Chapter 10 — Quantum Mechanics in the Modern World

## TL;DR

- Bell's theorem is now a Nobel Prize. The strangeness has stopped being only philosophy and become measurement, industry, and a hardware race.
- Watch the argument move: entanglement, EPR, and the CHSH inequality; lasers and stimulated emission; semiconductors and band theory; and quantum computing.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Bell's theorem is now a Nobel Prize. Lasers are a ten-figure industry. Quantum computing is a hardware race. Foundational quantum mechanics has stopped being only philosophy.*

---

In October 2022 the Nobel Committee for Physics handed its prize to Alain Aspect, John Clauser, and Anton Zeilinger for experiments with entangled photons. The announcement named "quantum information science" as a field — a discipline that did not even exist when most of the cited work was done.

Now think about how unusual that target is. This is a Nobel Prize for *closing a philosophical argument*. Let me lay out the argument, because the prize only makes sense once you see what it settled. In 1935 Einstein, Podolsky, and Rosen published a thought experiment arguing that quantum mechanics must be incomplete — that there had to be hidden variables underneath the probabilistic predictions, restoring the determinism and locality the theory seemed to be throwing away. For decades it sat there as a matter of taste, a debate you could not referee. Then in 1964 John Bell did something extraordinary: he turned the philosophical argument into a *quantitative test*. An inequality that any local hidden-variable theory must obey, and that quantum mechanics predicts should be violated by about 41%. In 1981–1982 Aspect and collaborators measured the violation in the lab. In 2015 three independent groups slammed shut the remaining experimental loopholes at the same time. The verdict: local hidden-variable theories of the kind Einstein had in mind are ruled out at more than ten standard deviations. The 2022 Nobel is the physics community formally acknowledging that this argument is over.

And the mathematical content underneath all of it is about one page of algebra. It is worth doing carefully — because once you have done it, the Nobel stops being a news item and becomes something you understand.

This chapter wires six modern applications — entanglement and Bell's theorem, lasers, semiconductors, quantum computing, superconductivity, and tunneling — back to the formalism we built in earlier chapters. Every one of them is a place where quantum mechanics stopped being theoretical and turned into an industry, a Nobel Prize, or an open race.

*Aging note.* Specific qubit counts, post-quantum cryptography migration milestones, and high-$T_c$ records will be out of date within one or two years of this writing (2026). Numbers are labeled `[verify, 2026]` where this applies; the conceptual structure survives any reasonable update.

---

## Entanglement, EPR, and the CHSH inequality

Einstein, Podolsky, and Rosen's 1935 paper ([*Physical Review* 47, 777–780](https://doi.org/10.1103/PhysRev.47.777)) ran a thought experiment: two particles prepared in a correlated state and then carried far apart. Measure particle A; you instantly know what particle B would give for the same measurement. EPR's argument went like this: B was spacelike-separated from A at the time of the measurement; no physical influence could have crossed between them; therefore B's outcome must have been settled *before* the measurement — a "hidden variable." But quantum mechanics forbids assigning simultaneous definite values to non-commuting observables. So, EPR concluded, quantum mechanics must be incomplete. The logic is tight. That is what makes it worth answering with an experiment rather than a counter-argument.

David Bohm recast the argument in 1951 using two spin-1/2 particles in the singlet state (which you met in Unit 7 as the spin part of parahelium's ground state):

$$|\psi_\text{singlet}\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\rangle_A|\downarrow\rangle_B - |\downarrow\rangle_A|\uparrow\rangle_B\right).$$

Total spin zero. Any spin measurement along any axis perfectly anticorrelates the two outcomes. Bell's 1964 insight ([*Physics Physique Fizika* 1, 195–200](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195)) was the crucial one: this perfect anticorrelation, all by itself, is *not* enough to tell quantum mechanics apart from a hidden-variable theory — a pair of gloves in two boxes would do as much. But the *angular* dependence of the correlations, for non-parallel axes, is enough. That is where the two theories part ways.

Here is the CHSH inequality derivation ([Clauser, Horne, Shimony, Holt 1969, *PRL* 23, 880–884](https://doi.org/10.1103/PhysRevLett.23.880)). Alice has two measurement settings $a_1$ and $a_2$; Bob has $b_1$ and $b_2$. Each measurement spits out a binary outcome in $\{+1, -1\}$. In any local hidden-variable theory, the outcomes are fixed by a shared hidden variable $\lambda$ and the local setting:

$$A_i = A_i(a_i, \lambda) \in \{+1,-1\}, \qquad B_j = B_j(b_j, \lambda) \in \{+1,-1\}.$$

For each $\lambda$, form the combination

$$S(\lambda) = A_1 B_1 + A_1 B_2 + A_2 B_1 - A_2 B_2 = A_1(B_1 + B_2) + A_2(B_1 - B_2).$$

Now watch this little argument, because it is the whole thing. Since $B_1, B_2 \in \{+1,-1\}$: either $B_1 = B_2$, in which case $B_1 + B_2 = \pm 2$ and $B_1 - B_2 = 0$; or $B_1 = -B_2$, in which case $B_1 + B_2 = 0$ and $B_1 - B_2 = \pm 2$. Either way, exactly one of the two parentheses is $\pm 2$ and the other is $0$. So $|S(\lambda)| = 2$ for *every* $\lambda$. No exceptions. Average over the distribution of hidden variables:

$$|\langle S\rangle_\text{LHV}| \leq 2.$$

In terms of the experimentally measurable correlation functions $E(a_i, b_j) = \langle A_i B_j\rangle$:

$$\boxed{|E(a_1,b_1) + E(a_1,b_2) + E(a_2,b_1) - E(a_2,b_2)| \leq 2 \quad \text{(CHSH, any LHV).}}$$

And that derivation rests on exactly one assumption: outcomes are predetermined functions of $\lambda$ and the local setting, with no faster-than-light coordination between Alice's side and Bob's. That is the assumption nature is about to break.

Now compute the same combination for the quantum singlet. The correlation function for spin-1/2 measurements along directions separated by angle $\theta_{AB}$ is

$$E_\text{QM}(\hat{n}_A, \hat{n}_B) = -\cos\theta_{AB}.$$

Choose the angles that push $|S|$ as high as it will go. Take $a_1 = 0$, $a_2 = \pi/2$, $b_1 = \pi/4$, $b_2 = -\pi/4$. The four angle differences are all $\pi/4$ except $\theta_{22} = 3\pi/4$. Computing:

$$E(a_1,b_1) = -\cos(\pi/4) = -1/\sqrt{2},$$
$$E(a_1,b_2) = -\cos(\pi/4) = -1/\sqrt{2},$$
$$E(a_2,b_1) = -\cos(\pi/4) = -1/\sqrt{2},$$
$$E(a_2,b_2) = -\cos(3\pi/4) = +1/\sqrt{2}.$$

$$S = -1/\sqrt{2} - 1/\sqrt{2} - 1/\sqrt{2} - 1/\sqrt{2} = -4/\sqrt{2} = -2\sqrt{2}.$$

$$|S|_\text{QM} = 2\sqrt{2} \approx 2.828.$$

Look at the two numbers side by side. Local hidden variables are boxed in at 2. Quantum mechanics gives $2\sqrt{2}$. The gap is about 41% — and it is not a small effect you have to squint at, it is a chasm. The Tsirelson bound ([Tsirelson 1980, *Letters in Mathematical Physics* 4, 93–100](https://doi.org/10.1007/BF00417500)) says no quantum state, with any measurement axes at all, can climb past $2\sqrt{2}$; the singlet at these axes sits right at that ceiling.

![The CHSH bound separates classical from quantum. The Tsirelson bound separates quantum from anything faster-than-light.](../images/10-quantum-mechanics-in-the-modern-world-fig-01.png)
*Figure 10.1 — Number line or bar diagram showing three regions*

Aspect, Grangier, and Roger in 1981–1982 measured $S = 2.697 \pm 0.015$ with polarization-entangled photons from a calcium cascade source ([*PRL* 49, 91](https://doi.org/10.1103/PhysRevLett.49.91); *PRL* 49, 1804](https://doi.org/10.1103/PhysRevLett.49.1804)). That violates the CHSH bound by tens of standard deviations — but it left two loopholes open, and skeptics were right to press on them: detection efficiency (most photons missed the detectors entirely — maybe the detected subsample was not representative) and locality (could a signal have sneaked between the detectors during the measurement?). In 2015, three independent loophole-free experiments shut both at once:

- Hensen et al. ([*Nature* 526, 682–686](https://doi.org/10.1038/nature15759)), Delft, NV centers in diamond, 1.3 km apart.
- Giustina et al. ([*PRL* 115, 250401](https://doi.org/10.1103/PhysRevLett.115.250401)), Vienna, entangled photons.
- Shalm et al. ([*PRL* 115, 250402](https://doi.org/10.1103/PhysRevLett.115.250402)), NIST Boulder, entangled photons.

The verdict: local hidden-variable theories of the EPR form are ruled out at $>10\sigma$. The only escape routes still standing are exotic — signals racing faster than light in a way that somehow permits no controllable communication, or superdeterminism (the experimenters' measurement choices were themselves predestined to fake the violation). Neither one is popular, and for good reason.

One important clarification, because people get this wrong constantly: entanglement does not allow faster-than-light communication. The marginal probability for Bob's outcome is completely unchanged by what Alice chooses to measure — this is the no-signaling theorem, a *theorem* in quantum mechanics, not an assumption tacked on to make us feel safe. To learn anything about the *correlation* (which is the non-classical part), Alice and Bob have to bring their data together and compare it, and that comparison travels at the speed of light like everything else.

---

## Lasers and stimulated emission

In 1917 Einstein introduced three radiative processes between atomic levels of energies $E_1 < E_2$ ([*Physikalische Zeitschrift* 18, 121–128](https://en.wikisource.org/wiki/Translation:On_the_Quantum_Theory_of_Radiation)): absorption (rate $\propto B_{12}\rho(\nu)N_1$), spontaneous emission (rate $\propto A_{21}N_2$, independent of the field), and stimulated emission (rate $\propto B_{21}\rho(\nu)N_2$, proportional to the field, with the emitted photon coherent with the stimulating field). Stimulated emission was the new piece, and the way Einstein got at it is lovely: he deduced its necessity from pure thermodynamic consistency. In thermal equilibrium the rates have to balance and the field has to follow Planck's distribution. Set absorption equal to total emission, demand consistency, and out comes

$$\frac{A_{21}}{B_{21}} = \frac{8\pi h\nu^3}{c^3}, \qquad B_{21} = B_{12}.$$

Read what these say. The first relation tells you spontaneous emission dominates at high frequency (that $\nu^3$ scaling) and stimulated emission at low frequency — which is exactly why lasing is easy in the infrared and very nearly impossible in the gamma-ray regime. The second says the matrix element governing emission and absorption is identical, which follows straight from Fermi's golden rule applied to the dipole coupling between atom and field.

Lasing needs *population inversion*: $N_2 > N_1$. In thermal equilibrium this is flatly impossible — Boltzmann piles most of the population into the lower level, as it must. You get inversion by pumping atoms into a third or fourth level, from which they drop down into the upper laser level faster than the laser transition itself drains it. Theodore Maiman built the first laser in May 1960 at Hughes Research Labs — a ruby rod pumped by a flashlamp, throwing out 694.3 nm red light in pulses ([Maiman 1960, *Nature* 187, 493–494](https://doi.org/10.1038/187493a0)). And here is a detail to savor: *Physical Review Letters* rejected the paper as too incremental. Within a year there were HeNe, semiconductor, and CO$_2$ lasers.

By 2026 [verify], lasers are a ten-figure annual industry — fiber-optic communications, surgical and industrial cutting, optical storage, spectroscopy, precision metrology, ranging. And the principle has not changed one bit since 1917. What Einstein computed from sheer thermodynamic consistency, thinking about a single pair of energy levels, became a technology that rewired the world's communications infrastructure.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/10-quantum-mechanics-in-the-modern-world-assertions.md -->

![Energy level diagram ](../images/10-quantum-mechanics-in-the-modern-world-fig-02.png)
*Figure 10.2 — Energy level diagram *

---

## Semiconductors and band theory

Felix Bloch's 1928 thesis ([*Zeitschrift für Physik* 52, 555–600](https://doi.org/10.1007/BF01339455)) established that the eigenstates of a single electron in a perfectly periodic crystal potential take the form

$$\psi_{n,\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}}\,u_{n,\mathbf{k}}(\mathbf{r}),$$

where $u_{n,\mathbf{k}}$ has the same periodicity as the lattice — Bloch's theorem. The energy $E_n(\mathbf{k})$ forms a *band*, and between the bands there are forbidden gaps. The Kronig–Penney model ([Kronig and Penney 1931, *Proceedings of the Royal Society A* 130, 499](https://doi.org/10.1098/rspa.1931.0019)) makes this concrete for a 1D periodic array of barriers: apply Bloch's theorem, match the boundary conditions, and you get

$$\cos(ka) = \cos(qa) + \frac{mV_0 a}{\hbar^2 q}\sin(qa),$$

where $q = \sqrt{2mE}/\hbar$. Now look at the structure. The left side is bounded between $\pm 1$ — it is a cosine, it cannot do anything else. But the right side has stretches where $|\text{RHS}| > 1$, and in those stretches no real $k$ exists at all. Those stretches are the forbidden gaps. Bands and gaps emerge from simply solving the Schrödinger equation in a periodic potential — no extra assumptions, no fudging.

*Conductors* have a partially-filled band, with empty states sitting just above filled ones, so electrons can move. *Insulators* have a fully-filled valence band separated from the empty conduction band by $\sim 5$ eV — and thermal energy ($k_BT \approx 0.025$ eV at room temperature) simply cannot bridge that. *Semiconductors* sit in the middle, with gaps of 0.5–2 eV: silicon at 1.12 eV, gallium arsenide at 1.43 eV. There, thermal excitation pushes a measurable number of electrons up into the conduction band at room temperature. That intermediate position is the entire reason semiconductors are useful.

![Three side-by-side band diagrams ](../images/10-quantum-mechanics-in-the-modern-world-fig-03.png)
*Figure 10.3 — Three side-by-side band diagrams *

Doping shifts the populations. Add phosphorus (five valence electrons) to silicon (four valence electrons) and you inject electrons into the conduction band — n-type. Add boron (three valence electrons) and you create holes in the valence band — p-type. A pn junction develops a built-in electric field in its depletion region, and that junction is the beating heart of every diode, LED, photovoltaic cell, and transistor. The MOSFET switches current with a gate-voltage-controlled inversion layer. The Intel 4004 of 1971 had 2,300 transistors; current chips have tens of billions — and every one of them rests on Bloch's 1928 theorem and the Born-rule probability interpretation of $|\psi|^2$.

---

## Quantum computing

A *qubit* is a two-level quantum system. The general state is

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1.$$

A computation is a unitary operation on $N$-qubit Hilbert space of dimension $2^N$, built as a circuit of one- and two-qubit gates, with a measurement at the end that collapses the state to a classical bit string with Born-rule probabilities. Two ingredients separate quantum from classical, and it is worth being precise about both: superposition (a qubit can be in any complex linear combination of $|0\rangle$ and $|1\rangle$, carrying phases that let amplitudes interfere) and entanglement (an $N$-qubit state has $2^N$ complex amplitudes, exponentially more than the $2N$ real numbers you need for $N$ independent classical bits). That exponential gap is where all the hope lives.

The single-qubit gates include the Pauli matrices ($\hat{X}$ for bit flip, $\hat{Z}$ for phase flip) and the Hadamard

$$\hat{H} = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\\1 & -1\end{pmatrix}, \qquad \hat{H}|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad \hat{H}|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

The two-qubit CNOT flips the target qubit whenever the control is $|1\rangle$. And here is the satisfying part — Hadamard plus CNOT generates entanglement out of a plain product state:

$$|00\rangle \xrightarrow{H\otimes I} \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle).$$

That output is a Bell state — the very same maximally entangled state at the heart of every CHSH experiment from the start of this chapter — produced here in just two gates. CNOT plus arbitrary single-qubit unitaries forms a universal gate set ([DiVincenzo 1995, *Physical Review A* 51, 1015](https://doi.org/10.1103/PhysRevA.51.1015)) — every multi-qubit unitary decomposes into this set with polynomially many gates.

![Two gates. One entangled state. The same state that violates Bell by 41%.](../images/10-quantum-mechanics-in-the-modern-world-fig-04.png)
*Figure 10.4 — Quantum circuit diagram for the Bell-state generation *

Two algorithms anchor the whole field. *Shor's algorithm* ([Shor 1994; 1997, *SIAM Journal on Computing* 26, 1484](https://doi.org/10.1109/SFCS.1994.365700)) factors an $n$-bit integer in $O(n^3)$ operations on a quantum computer, against the best known classical algorithm's $\exp(O(n^{1/3}(\log n)^{2/3}))$ — a super-polynomial speedup. A large enough fault-tolerant quantum computer would break RSA. *Grover's algorithm* ([Grover 1996](https://doi.org/10.1145/237814.237866)) searches an $N$-item unsorted database in $O(\sqrt{N})$ queries against the classical $O(N)$ — a quadratic speedup, real and useful but not exponential. The distinction matters enormously, and people blur it all the time.

![Not all quantum speedups are the same. Grover wins by a constant factor on the log scale. Shor wins by the whole game.](../images/10-quantum-mechanics-in-the-modern-world-fig-05.png)
*Figure 10.5 — Log-log plot of runtime vs*

As of 2026 [verify], the field is in the NISQ era (Preskill 2018, [*Quantum* 2, 79](https://doi.org/10.22331/q-2018-08-06-79)) — hardware with hundreds to thousands of noisy qubits, not yet error-corrected to fault tolerance. IBM's Condor processor announced around 1,100 superconducting qubits in late 2023; Google's Sycamore family has been demonstrated through 70 qubits; Quantinuum's H2 trapped-ion system offers high-fidelity all-to-all connectivity; Atom Computing has demonstrated neutral-atom arrays exceeding 1,000 qubits [verify, 2026]. Google's 2023 paper ([Acharya et al. 2023, *Nature* 614, 676–681](https://doi.org/10.1038/s41586-022-05434-1)) demonstrated below-threshold logical qubits — pushing the surface-code distance from 3 to 5 reduced the logical error rate — which is the first experimental evidence that quantum error correction scales the way the theory promised. But from a below-threshold demonstration to fault-tolerant factoring of 2048-bit keys, the engineering distance is enormous. Do not let the headlines collapse it.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/10-quantum-mechanics-in-the-modern-world-assertions.md -->

The honest framing: as of 2026 no quantum computer has demonstrated a useful speedup on a practically important problem. The 2019 "quantum supremacy" result (Google Sycamore, [*Nature* 574, 505](https://doi.org/10.1038/s41586-019-1666-5)) was a sampling task with no practical utility, and the classical-simulation runtime estimate that made it look impressive was revised downward by orders of magnitude within months. These experiments show that quantum hardware can do something hard to simulate classically. They do not show that quantum hardware can solve problems people actually need solved. Those are very different claims.

The practical response to the *future* threat from Shor's algorithm is *post-quantum cryptography*. NIST finalized FIPS 203 (CRYSTALS-Kyber), FIPS 204 (CRYSTALS-Dilithium), and FIPS 205 (SPHINCS+) in August 2024 [verify; current standards at [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography)]. Internet infrastructure migration is underway right now — in anticipation of a large quantum computer that does not yet exist. The timeline is set by prudence about hardware progress, not by any existing threat. That is a strange thing to do, and entirely rational.

---

## Superconductivity

Heike Kamerlingh Onnes discovered in 1911 that mercury's resistance drops abruptly to zero below 4.2 K (Onnes 1911). The phenomenon — resistance exactly zero, persistent currents that last effectively forever — was the fact, sitting there plainly. The *explanation* took 46 years to arrive. Hold that gap in mind; it tells you how hard this was.

BCS theory (Bardeen, Cooper, Schrieffer 1957, [*Physical Review* 108, 1175](https://doi.org/10.1103/PhysRev.108.1175)) supplied the mechanism. Cooper's key result ([*Physical Review* 104, 1189](https://doi.org/10.1103/PhysRev.104.1189)) was startling: in the presence of *any* attractive interaction between two electrons near the Fermi surface, however weak, the Fermi sea is unstable against forming bound pairs of opposite-momentum, opposite-spin electrons — "Cooper pairs." However weak. That is the surprise. These pairs have integer spin and behave as composite bosons (Unit 8). At low temperature they condense into a single macroscopic quantum state with a definite phase, separated from single-particle excitations by an energy gap $\Delta$.

The BCS gap equation at zero temperature gives

$$\Delta \approx 2\hbar\omega_D\,e^{-1/N(0)V},$$

where $N(0)$ is the density of states at the Fermi level, $V$ is the attractive coupling, and $\omega_D$ is the Debye frequency. Now look at that $e^{-1/V}$ dependence, because it is the reason superconductivity hid for so long. It is non-analytic at $V=0$ — every Taylor coefficient of $e^{-1/V}$ at $V=0$ is exactly zero — so no perturbation theory in small $V$ can ever find this result. You could expand forever and get nothing. BCS found it through a variational ansatz, not perturbation theory, which is why it had to wait for someone to guess the right wave function.

The prediction $2\Delta/k_BT_c \approx 3.53$ is universal in the weak-coupling limit. For aluminum: $\Delta \approx 0.17$ meV predicts $T_c \approx 1.1$ K; the measured value is $T_c = 1.18$ K, within 7%. Zero resistance follows because breaking a pair costs energy $2\Delta$; at $k_BT \ll \Delta$ no scattering process has that energy on hand, so there is nothing to scatter off. The supercurrent also expels magnetic flux — the Meissner effect ([Meissner and Ochsenfeld 1933, *Naturwissenschaften* 21, 787](https://doi.org/10.1007/BF01504252)) — which is what distinguishes a real superconductor from a hypothetical merely-perfect conductor, and which falls out of BCS through the London equations.

Then Bednorz and Müller's 1986 discovery ([*Zeitschrift für Physik B* 64, 189](https://doi.org/10.1007/BF01303701)) of superconductivity in copper-oxide perovskites at $T_c \approx 35$ K broke the comfortable picture. YBa$_2$Cu$_3$O$_7$ followed at $T_c \approx 93$ K — above liquid nitrogen's 77 K boiling point, which made economically practical high-$T_c$ materials suddenly real overnight. Nobel 1987, the fastest in the history of the prize. Under extreme pressure, hydrogen sulfide reaches $\sim 203$ K ([Drozdov et al. 2015, *Nature* 525, 73](https://doi.org/10.1038/nature14964)) and lanthanum hydride reaches $\sim 250$ K at $\sim 170$ GPa ([Somayazulu et al. 2019, *PRL* 122, 027001](https://doi.org/10.1103/PhysRevLett.122.027001)). Room-temperature ambient-pressure superconductivity has not been demonstrated as of 2026 [verify]. And the mechanism for cuprate superconductivity — forty years after the discovery — is still contested. That is worth sitting with: a major experimental phenomenon, unexplained after four decades of effort.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/10-quantum-mechanics-in-the-modern-world-assertions.md -->

![Timeline of superconductor T_c records from 1911 to](../images/10-quantum-mechanics-in-the-modern-world-fig-06.png)
*Figure 10.6 — Timeline of superconductor T_c records from 1911 to*

---

## Tunneling applications

The WKB tunneling formula from Unit 9 produces an exponential dependence of tunneling current on barrier width, and that single exponential generates a long catalog of technologies and natural phenomena. Once you see how violently sensitive an exponential is, the catalog stops being a list of coincidences and becomes one idea wearing many costumes.

*Scanning tunneling microscopy.* Binnig and Rohrer at IBM Zurich in 1981–1982 ([*PRL* 49, 57](https://doi.org/10.1103/PhysRevLett.49.57)); Nobel 1986. A sharp metal tip is brought ångström-close to a conducting surface, and electrons tunnel across the vacuum gap. The current depends exponentially on the gap distance $d$:

$$I \propto e^{-2\kappa d}, \qquad \kappa \approx \sqrt{2m_e\phi}/\hbar,$$

where $\phi$ is the work function. For $\phi = 4$ eV, $\kappa \approx 1\,\text{Å}^{-1}$, so a 1 Å change in $d$ changes the current by $e^2 \approx 7.4$. That is the whole trick. STM resolves individual atoms because the exponential sensitivity means the tunneling current is dominated by the single closest atom on the tip — change the gap by the width of one atom and the current jumps by a factor of seven. The exponential does all the spatial resolution work; the rest is engineering.

![The atom's height changes by 1 Å. The tunneling current changes by a factor of 7. That factor is why STM sees atoms.](../images/10-quantum-mechanics-in-the-modern-world-fig-07.png)
*Figure 10.7 — STM cross-section diagram *

*Flash memory.* The floating-gate transistor writes a bit by tunneling electrons through a thin oxide layer onto an isolated gate; the gate charge then shifts the transistor's threshold voltage. Flash retains data for years without power because the tunneling rate at read-bias voltage is exponentially small — the very same WKB exponential that spans 24 orders of magnitude in alpha-decay half-lives is what lets flash hold its data over decades while still being writable at write voltage. One exponential, two jobs that seem to contradict each other, reconciled by how steep it is.

*Alpha decay.* Gamow 1928 ([*Zeitschrift für Physik* 51, 204](https://doi.org/10.1007/BF01343196)) modeled the alpha particle as a wave packet tunneling through the Coulomb barrier outside the nuclear potential. The WKB formula reproduces the Geiger–Nuttall relation $\log(T_{1/2}) \propto Z/\sqrt{E_\alpha}$ — the first nuclear-physics calculation ever done with quantum mechanics.

*Josephson junctions.* Cooper-pair tunneling across an insulating barrier between two superconductors ([Josephson 1962, *Physics Letters* 1, 251](https://doi.org/10.1016/0031-9163(62)91369-0)) produces a supercurrent at zero voltage (DC Josephson effect) and an oscillating current at frequency $2eV/\hbar$ under DC bias (AC Josephson effect). SQUIDs — superconducting quantum interference devices built on Josephson junctions — are the most sensitive magnetometers known, and they underlie the SI definition of the volt since 1990.

*Biological tunneling.* Electron tunneling in respiratory and photosynthetic electron-transport chains is well-established (Marcus theory). Proton tunneling in DNA base pairs was proposed by Löwdin ([*Reviews of Modern Physics* 35, 724, 1963](https://doi.org/10.1103/RevModPhys.35.724)) as a source of spontaneous mutation — the mechanism is real; whether it is quantitatively significant compared to thermal tautomerization is debated. The 2007 claim of long-lived quantum coherence in photosynthetic energy transfer ([Engel et al., *Nature* 446, 782](https://doi.org/10.1038/nature05678)) has been substantially walked back; the current consensus is that coherences are present but short-lived and not the dominant mechanism for energy-transfer efficiency [verify, 2024–2026].
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/10-quantum-mechanics-in-the-modern-world-assertions.md -->

---

## What would change my mind

Some of this chapter's claims are rock-solid; others carry aging risk, and honesty means flagging which is which.

*Stable*: local hidden-variable theories of the EPR form are ruled out by Bell tests. The Einstein $A/B$ relations hold. Bloch's theorem and band theory hold. BCS accounts for conventional superconductivity. WKB tunneling explains STM, flash memory, and alpha decay.

*Aging within 1–2 years*: quantum-computing hardware metrics (qubit counts, error rates, error-correction milestones) [verify 2026]; high-$T_c$ records; post-quantum cryptography migration rates. The *structure* of the progress is far more durable than any single number.

Four scenarios would force a substantial rewrite. A demonstration of *useful quantum advantage* — a quantum computer beating every classical algorithm on a practically important problem — would shift §4.4's timeline framing. A *reproducible room-temperature ambient-pressure superconductor* would shift §4.5 significantly; this has been claimed and not reproduced several times between 2020–2024. A *credible Bell-inequality experimental anomaly* — an experiment that fails to find the predicted violation — would force reconsideration of the entanglement section; none has appeared in sixty years of increasingly careful experiments. And a *loophole-free demonstration that quantum-biological coherence is essential to a biological function* would strengthen the tunneling-biology paragraph; the field has been moving in the opposite direction since 2014 [verify].

---

## Still puzzling

**Bell's theorem rules out local hidden variables, not everything.** The experiment rules out the conjunction of counterfactual definiteness, locality, and freedom of choice. Different interpretations of quantum mechanics drop different ones: many-worlds keeps all three and adds branches; Bohmian mechanics is explicitly non-local; QBism drops counterfactual definiteness. The theorem closes one specific argument — an important one — without settling the interpretation question.

**Why has high-$T_c$ cuprate pairing resisted theoretical closure for forty years?** Multiple coupling channels likely compete in a regime where current theoretical methods have genuine trouble. This is one of the rare cases in modern condensed-matter physics where a major experimental phenomenon has not been explained after decades of effort. I find it honestly puzzling.

**What is the actual landscape of useful quantum algorithms?** Shor's algorithm gives exponential speedup for factoring. Grover's gives quadratic speedup for unstructured search. Quantum simulation gives plausible exponential speedup for certain Hamiltonians. Beyond that, the list of quantum algorithms with proven super-polynomial speedup on practically relevant problems is short. The complexity class BQP is not known to contain NP — quantum computers do not in general solve NP-complete problems in polynomial time.

**What is the 2022 Nobel's actual scope?** Aspect, Clauser, and Zeilinger established experimentally that local hidden variables of the EPR form do not describe quantum correlations. They did not settle which interpretation of quantum mechanics is correct, whether quantum mechanics is foundationally complete, or whether it is the large-scale limit of some more fundamental theory. The Nobel closes one specific argument. The foundational discussion continues.

---

## References

*Added by fact-check pass 2026-05-14.*

1. The Nobel Prize in Physics 2022 — Aspect, Clauser, Zeilinger. https://www.nobelprize.org/prizes/physics/2022/
2. Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. "Proposed Experiment to Test Local Hidden-Variable Theories." *Physical Review Letters* 23, 880–884 (1969). https://doi.org/10.1103/PhysRevLett.23.880
3. Cirel'son, B. S. "Quantum generalizations of Bell's inequality." *Letters in Mathematical Physics* 4, 93–100 (1980). https://doi.org/10.1007/BF00417500
4. Aspect, A., Dalibard, J. & Roger, G. "Experimental Test of Bell's Inequalities Using Time-Varying Analyzers." *Physical Review Letters* 49, 1804–1807 (1982). https://doi.org/10.1103/PhysRevLett.49.1804
5. Hensen, B. et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." *Nature* 526, 682 (2015). https://doi.org/10.1038/nature15759
6. Giustina, M. et al. "Significant-Loophole-Free Test of Bell's Theorem with Entangled Photons." *Physical Review Letters* 115, 250401 (2015).
7. Shalm, L. K. et al. "Strong Loophole-Free Test of Local Realism." *Physical Review Letters* 115, 250402 (2015).
8. Einstein, A. "Zur Quantentheorie der Strahlung." *Physikalische Zeitschrift* 18, 121–128 (1917).
9. Maiman, T. H. "Stimulated Optical Radiation in Ruby." *Nature* 187, 493–494 (1960). https://doi.org/10.1038/187493a0
10. Bloch, F. "Über die Quantenmechanik der Elektronen in Kristallgittern." *Zeitschrift für Physik* 52, 555–600 (1928).
11. Kronig, R. de L. & Penney, W. G. *Proceedings of the Royal Society A* 130, 499 (1931).
12. Shor, P. W. "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer." *SIAM Journal on Computing* 26, 1484 (1997).
13. DiVincenzo, D. P. "Two-bit gates are universal for quantum computation." *Physical Review A* 51, 1015 (1995). https://doi.org/10.1103/PhysRevA.51.1015
14. Bardeen, J., Cooper, L. N. & Schrieffer, J. R. "Theory of Superconductivity." *Physical Review* 108, 1175–1204 (1957). https://doi.org/10.1103/PhysRev.108.1175
15. Bednorz, J. G. & Müller, K. A. "Possible high-T_c superconductivity in the Ba−La−Cu−O system." *Zeitschrift für Physik B* 64, 189 (1986).
16. Drozdov, A. P. et al. *Nature* 525, 73 (2015). https://doi.org/10.1038/nature14964
17. Somayazulu, M. et al. *Physical Review Letters* 122, 027001 (2019).
18. Binnig, G., Rohrer, H., Gerber, Ch. & Weibel, E. "Surface Studies by Scanning Tunneling Microscopy." *Physical Review Letters* 49, 57–61 (1982). https://doi.org/10.1103/PhysRevLett.49.57
19. Josephson, B. D. "Possible new effects in superconductive tunnelling." *Physics Letters* 1, 251–253 (1962).
20. Acharya, R. et al. "Suppressing quantum errors by scaling a surface code logical qubit." *Nature* 614, 676 (2023). https://doi.org/10.1038/s41586-022-05434-1
21. NIST FIPS 203/204/205 (Aug 2024). https://csrc.nist.gov/projects/post-quantum-cryptography
