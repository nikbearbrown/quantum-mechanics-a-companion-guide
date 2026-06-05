# Chapter 3 — The Schrödinger Equation


## TL;DR

- This chapter delivers the dynamical law of quantum mechanics, presented as a postulate motivated by a plausibility argument, not a derivation.
- It covers the time-dependent and time-independent Schrödinger equations, the Born rule for $|\psi|^2$, conservation of normalization from Hermiticity, the continuity equation, stationary states and Bohr-frequency beating, the time-evolution algorithm, and free-particle wave packets.
- It states what the equation computes, why each structural feature matters, and what the equation does not determine.

*The dynamical law of quantum mechanics was guessed, not proved. Here is what it says, why it works, and what it refuses to tell you.*

---

Erwin Schrödinger developed his equation over the 1925–26 winter and published a sequence of four papers in *Annalen der Physik* beginning January 1926. Walter Moore's biography (*Schrödinger: Life and Thought*, Cambridge University Press, 1989) [*verify exact chapter*] records the period. The physics is not in dispute: the papers [Schrödinger, *Ann. Phys.* 79, 361–376](https://doi.org/10.1002/andp.19263840404) reproduced every known hydrogen energy level, explained the selection rules for atomic transitions, and supplied a usable formalism within months.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-schrodinger-equation-assertions.md -->

Heisenberg, Born, and Jordan had reached the same physics six months earlier through matrix mechanics, but matrix mechanics used unfamiliar arrays and multiplication rules. Schrödinger's formulation looked like a wave equation, a structure physicists already knew. It became the standard entry point almost immediately and remains so.

Position in the sequence: Unit 1 supplied the experimental evidence forcing quantum mechanics — blackbody radiation, the photoelectric effect, Compton scattering, de Broglie matter waves, Franck–Hertz. Unit 2 supplied the mathematics — complex Hilbert spaces, inner products, Hermitian operators, eigenvalue equations. What remains is a *dynamical law* governing how a quantum state changes in time, the analog of Newton's $\vec{F} = m\vec{a}$. The Schrödinger equation is that law.

The equation *cannot be derived*. Griffiths states this directly in §1.1 of the third edition: "Where did Schrödinger's equation come from? In a sense, it cannot be derived." A plausibility argument makes the form look natural given de Broglie and Einstein, and it is worth running, but it is not a derivation. The Schrödinger equation has the status of Newton's second law: a fundamental postulate accepted for what it explains, not because it follows from a deeper theory. Asking why nature uses this equation rather than a neighboring one has no deeper answer within non-relativistic quantum mechanics.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-schrodinger-equation-assertions.md -->

---

## The plausibility argument

Take de Broglie's matter wave for a free particle moving in the $+x$ direction:

$$\psi(x,t) = A\,e^{i(kx - \omega t)}, \qquad p = \hbar k, \qquad E = \hbar\omega.$$

Differentiate once in $t$:

$$\frac{\partial\psi}{\partial t} = -i\omega\,\psi = -\frac{iE}{\hbar}\psi \implies i\hbar\frac{\partial\psi}{\partial t} = E\psi.$$

Differentiate twice in $x$:

$$\frac{\partial^2\psi}{\partial x^2} = -k^2\psi = -\frac{p^2}{\hbar^2}\psi \implies -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} = \frac{p^2}{2m}\psi.$$

For a free particle $E = p^2/2m$, so the right sides of the last two equations are equal, giving the free-particle equation:

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}.$$

Add a potential energy $V(x,t)$ — kinetic plus potential equals total energy — to obtain the *time-dependent Schrödinger equation*:

$$\boxed{\;i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x,t)\,\psi(x,t).\;}$$

In operator language, with Hamiltonian $\hat{H} = \hat{p}^2/2m + V(\hat{x},t)$ and momentum operator $\hat{p} = -i\hbar\,\partial_x$ from Unit 2:

$$i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi.$$

![Anatomy of the time-dependent Schrödinger equation ](../images/03-the-schrodinger-equation-fig-01.png)
*Figure 3.1 — Anatomy of the time-dependent Schrödinger equation *

Three features the argument assembles but does not *prove*:

The equation is **linear**: if $\psi_1$ and $\psi_2$ are solutions, so is $\alpha\psi_1 + \beta\psi_2$. This is the superposition principle and the algebraic origin of interference. Nonlinear wave equations do not produce interference.

The equation is **first-order in time**: specifying $\psi$ at one instant determines it at all later times. The classical wave equation $\partial_t^2\psi = c^2\partial_x^2\psi$ is second-order and requires both $\psi$ and $\partial_t\psi$ at $t = 0$. The Schrödinger equation requires only $\psi$.

The equation contains **the factor of $i$**: without it the equation becomes $\partial_t\psi = (\hbar/2m)\partial_x^2\psi$, the diffusion equation, whose solutions spread irreversibly. The $i$ converts diffusion into wave propagation and ensures $\int|\psi|^2 dx$ is conserved, proved below.

![Two side-by-side plots of an initially Gaussian wave](../images/03-the-schrodinger-equation-fig-02.png)
*Figure 3.2 — Two side-by-side plots of an initially Gaussian wave*

None of these follows from the plausibility argument; they are properties the equation carries. The argument motivates the *form*; experiment confirms nature uses it.

Self-consistency check: verify that $\psi(x,t) = A\,e^{i(kx-\omega t)}$ with $\omega = \hbar k^2/2m$ is a solution. Left side: $i\hbar\,\partial_t\psi = i\hbar(-i\omega)\psi = \hbar\omega\psi$. Right side: $-(\hbar^2/2m)\partial_x^2\psi = (\hbar^2 k^2/2m)\psi$. Equal iff $\hbar\omega = \hbar^2 k^2/2m$, i.e. $E = p^2/2m$. The dispersion relation is the free-particle energy-momentum relation, as required.

---

## The Born rule: what $|\psi|^2$ means

Schrödinger first proposed that $|\psi|^2$ was the electron's *charge density* — the electron as a smeared matter wave. That interpretation lasted weeks. Max Born proposed in 1926 [Born, *Z. Phys.* 37, 863–867](https://doi.org/10.1007/BF01397477) that

$$|\psi(x,t)|^2\,dx = \text{probability of finding the particle in } [x,\, x+dx] \text{ at time } t.$$

$\psi$ itself is not observable; $|\psi|^2$ is a probability density. Born received the Nobel Prize for this in 1954 — 28 years after the paper, indicating how contested the probabilistic interpretation was through the twenties and thirties.

Born's interpretation resolved two structural problems in the matter-wave picture. First: $\psi$ is complex, and there is no classical complex matter density; $\text{Re}(\psi)$ or $|\psi|$ would obey no linear equation, destroying superposition. Second: for two particles $\psi$ is a function of *six* coordinates, $\psi(x_1, y_1, z_1, x_2, y_2, z_2, t)$, which cannot be a physical wave in three-dimensional space. Probabilities are real and non-negative, and a probability distribution on configuration space is well defined in any dimension.

Three conditions make the Born rule a consistent probability assignment. Non-negativity: $|\psi|^2 \geq 0$ everywhere, automatic for a squared modulus. Normalization: $\int_{-\infty}^\infty |\psi(x,t)|^2\,dx = 1$, since the particle is somewhere. Conservation: if normalization holds at $t = 0$ it must hold at all later times. The third is not automatic; it is a theorem requiring the Hermiticity of $\hat{H}$.

**Worked example — probability in the left quarter of the infinite square well ground state.**

**Given.** The ground state of an infinite square well of width $L$,

$$\psi_1(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{\pi x}{L}\right),\quad 0 \leq x \leq L.$$

**Find.** The probability of finding the particle in the left quarter, $[0, L/4]$.

**Solution.**

$$P = \frac{2}{L}\int_0^{L/4}\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{1}{L}\int_0^{L/4}\left[1 - \cos\!\left(\frac{2\pi x}{L}\right)\right]dx = \frac{1}{4} - \frac{1}{2\pi} \approx 0.091.$$

**Check.** The result, about 9%, is below the uniform value of 25%, consistent with the ground-state density peaking at the center and depleting the edges. The number $1/4 - 1/2\pi$ comes entirely from the wave function's shape, not from any particle trajectory; there is no trajectory, only the squared amplitude.

![Plot of |ψ₁(x)|² = (2/L)sin²(πx/L) over [0, L]](../images/03-the-schrodinger-equation-fig-03.png)
*Figure 3.3 — Plot of |ψ₁(x)|² = (2/L)sin²(πx/L) over [0, L]*

Two misconceptions to dispose of. First: "$\psi$ is the particle." No — $\psi$ is the probability amplitude; the particle is what registers in a detector. Before detection, what exists is the amplitude. Second: "$|\psi|^2$ encodes ignorance about a definite but unmeasured position." No. Bell-inequality experiments — Aspect 1982, refined since, awarded the 2022 Nobel Prize to Aspect, Clauser, and Zeilinger — rule out the local hidden-variable theories that would support this reading. The probability is irreducible, not a stand-in for incomplete classical knowledge.

---

## Normalization is preserved, and why Hermiticity is the reason

Differentiate the normalization integral under the integral sign:

$$\frac{d}{dt}\int_{-\infty}^\infty|\psi|^2\,dx = \int\left(\psi^{*}\frac{\partial\psi}{\partial t} + \frac{\partial\psi^{*}}{\partial t}\psi\right)dx.$$

From the Schrödinger equation, $\partial_t\psi = -(i/\hbar)\hat{H}\psi$. For real $V$, $\partial_t\psi^{*} = +(i/\hbar)(\hat{H}\psi)^{*}$. Substituting:

$$\frac{d}{dt}\int|\psi|^2\,dx = -\frac{i}{\hbar}\left[\int\psi^{*}\hat{H}\psi\,dx - \int(\hat{H}\psi)^{*}\psi\,dx\right] = -\frac{i}{\hbar}\left[\langle\psi|\hat{H}\psi\rangle - \langle\hat{H}\psi|\psi\rangle\right].$$

By Hermiticity of $\hat{H}$, $\langle\psi|\hat{H}\psi\rangle = \langle\hat{H}\psi|\psi\rangle$. The bracket is zero. Normalization is preserved.

The proof used exactly one fact: Hermiticity of $\hat{H}$. This is the structural reason quantum mechanics postulates that observables are Hermitian operators — not an aesthetic preference. Without Hermiticity the Born rule would fail to define a probability assignment that survives time evolution, and the apparatus would collapse.

The same argument applied locally gives the *continuity equation*. Define the probability density $\rho(x,t) = |\psi|^2$ and the probability current

$$j(x,t) = \frac{\hbar}{2mi}\left(\psi^{*}\frac{\partial\psi}{\partial x} - \psi\frac{\partial\psi^{*}}{\partial x}\right) = \frac{\hbar}{m}\,\text{Im}\!\left(\psi^{*}\frac{\partial\psi}{\partial x}\right).$$

Then

$$\frac{\partial\rho}{\partial t} + \frac{\partial j}{\partial x} = 0.$$

This is the local statement of probability conservation: probability does not vanish at one point and reappear discontinuously elsewhere, it flows. Probability leaving a region crosses the boundary at rate $j$.

![Diagram of a 1D region [a, b] with](../images/03-the-schrodinger-equation-fig-04.png)
*Figure 3.4 — Diagram of a 1D region [a, b] with*

Derivation: compute $\partial_t(\psi^{*}\psi)$, substitute the Schrödinger equation for $\partial_t\psi$ and $\partial_t\psi^{*}$, observe the potential terms cancel because $V$ is real, and recognize the remainder as $\partial_x(\psi^{*}\partial_x\psi - \psi\partial_x\psi^{*})$ from the product rule. The derivation is a half-page exercise applying the Schrödinger equation twice.

For a plane wave $\psi = Ae^{i(kx-\omega t)}$, the current is $j = (\hbar k/m)|A|^2 = v|A|^2$ — density times velocity, the classical expression for a moving fluid. In the regime where the wave picture should look classical, the probability current matches a particle current, a consistency check on the formalism.

---

## Stationary states

If $V$ is time-independent, the Schrödinger equation admits separated solutions:

$$\psi(x,t) = \psi(x)\,e^{-iEt/\hbar}.$$

Substituting, the left side gives $E\psi(x)e^{-iEt/\hbar}$ and the right side gives $\hat{H}\psi(x)$ times $e^{-iEt/\hbar}$. The time-dependent phase cancels, leaving:

$$\boxed{\;\hat{H}\psi(x) = E\,\psi(x).\;}$$

This is the *time-independent Schrödinger equation*, an eigenvalue equation for the Hamiltonian. The function $\psi(x)$ is an energy eigenfunction and the real number $E$ is the allowed energy.

The term "stationary" applies because $|\psi(x,t)|^2 = |\psi(x)|^2$ — the probability density is time-independent, and every measurement probability for any time-independent observable is constant.

Note carefully: *stationary states are not static.* The *probability density* is constant, but the *amplitude* $\psi(x,t) = \psi(x)\,e^{-iEt/\hbar}$ rotates in the complex plane at angular frequency $E/\hbar$. The magnitude at each $x$ is fixed; the phase advances at rate $E/\hbar$. For a single isolated stationary state this rotation has no observable consequence, because measurements depend only on $|\psi|^2$ and $|e^{-iEt/\hbar}| = 1$. With two stationary states, the rotation becomes the dominant effect.

![A single phasor rotating invisibly. Two phasors beating visibly.](../images/03-the-schrodinger-equation-fig-05.png)
*Figure 3.5 — Diagram *

Form a superposition of states at energies $E_1$ and $E_2$:

$$\psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1 t/\hbar} + \psi_2(x)\,e^{-iE_2 t/\hbar}\right].$$

Compute $|\psi|^2$:

$$|\psi|^2 = \frac{1}{2}\left[|\psi_1|^2 + |\psi_2|^2 + 2\,\text{Re}\!\left(\psi_1^{*}\psi_2\,e^{-i(E_2 - E_1)t/\hbar}\right)\right].$$

The cross term oscillates with a factor $\cos((E_2 - E_1)t/\hbar)$ — the *Bohr frequency* $(E_2 - E_1)/\hbar$. The probability density oscillates at this frequency, and so does the expectation value of position. When an atom in a higher energy state decays to a lower one, it emits a photon of energy $E_2 - E_1$, producing a spectral line at frequency $(E_2 - E_1)/h$. Every spectral line in atomic physics — Balmer, Lyman, Paschen — exists because the phases of stationary states rotate, and their *relative* rotation at the Bohr frequency becomes observable under superposition.

**Worked example — position oscillation in a two-state superposition.**

**Given.** The first two stationary states of an infinite square well of width $L$,

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right),\quad E_n = \frac{n^2\pi^2\hbar^2}{2mL^2},$$

in the equal-amplitude superposition $\psi = (1/\sqrt{2})[\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar}]$.

**Find.** The expectation value $\langle x\rangle(t)$.

**Solution.** The time-independent piece is $(1/2)[\langle x\rangle_1 + \langle x\rangle_2] = L/2$, by symmetry. The time-dependent piece requires

$$\frac{2}{L}\int_0^L x\sin\!\left(\frac{\pi x}{L}\right)\sin\!\left(\frac{2\pi x}{L}\right)dx.$$

Using $\sin a\sin b = (1/2)[\cos(a-b) - \cos(a+b)]$ and integrating by parts, this integral equals $-16L/(9\pi^2)$. So

$$\langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos(\omega t),\qquad \omega = \frac{E_2 - E_1}{\hbar} = \frac{3\pi^2\hbar}{2mL^2}.$$

**Check.** The expectation value oscillates about the well midpoint with amplitude $16L/9\pi^2 \approx 0.18L$ at the Bohr frequency. The particle is not moving classically — there is no trajectory, velocity, or definite position — yet the center of the probability distribution swings back and forth. This is a quantum state that radiates.

![Animation-ready sequence of three snapshots of |ψ(x,t)|² for](../images/03-the-schrodinger-equation-fig-06.png)
*Figure 3.6 — Animation-ready sequence of three snapshots of |ψ(x,t)|² for*

---

## The time-evolution algorithm

The spectral theorem from Unit 2 states that the energy eigenfunctions of a Hermitian Hamiltonian form a complete orthonormal basis. Any initial state expands:

$$\psi(x, 0) = \sum_n c_n\,\psi_n(x),\qquad c_n = \int\psi_n^{*}(x)\,\psi(x,0)\,dx.$$

Time evolution attaches a phase to each component:

$$\psi(x,t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

This is the complete algorithm for time evolution under a time-independent Hamiltonian: find the energy eigenstates, expand the initial condition, attach a phase to each term, sum. Nearly every solvable problem — the infinite square well, the harmonic oscillator, hydrogen — runs this algorithm with a different $V(x)$ and therefore a different set of eigenfunctions $\psi_n$ and energies $E_n$.

The probability that an energy measurement yields $E_n$ is $|c_n|^2$, constant in time. Energy probabilities never change under Hamiltonian evolution, because each phase $e^{-iE_n t/\hbar}$ has modulus 1, so $|c_n e^{-iE_n t/\hbar}|^2 = |c_n|^2$. Only expectation values of other observables — position, momentum — oscillate, through cross terms between energy eigenstates with different phases.

This requires a time-independent $V$. For time-dependent potentials the eigenstates shift with time and time-dependent perturbation theory is needed. That is Unit 9.

---

## The free particle and why plane waves are not states

When $V = 0$, the time-independent Schrödinger equation is $-(\hbar^2/2m)\,d^2\psi/dx^2 = E\psi$. Set $k = \sqrt{2mE}/\hbar$. The general solution is

$$\psi_k(x) = Ae^{ikx} + Be^{-ikx},$$

right-moving and left-moving plane waves at momentum $\pm\hbar k$. The full time-dependent solution carries the phase $e^{-iEt/\hbar}$ with $E = \hbar^2 k^2/2m$.

These plane waves are not normalizable: $\int|Ae^{ikx}|^2\,dx = |A|^2\int_\infty^\infty 1\,dx = \infty$. They violate the Born rule, since total probability cannot be infinite. They are not physical states.

This is not a defect of the formalism. Plane waves are generalized eigenfunctions, as flagged in Unit 2 — they live in the extended space beyond $L^2(\mathbb{R})$ and serve as calculational tools, like the position eigenstates $|x\rangle$. Physical states are *wave packets*: superpositions of plane waves with a normalizable weight function. Write

$$\psi(x, 0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty \phi(k)\,e^{ikx}\,dk.$$

This is a Fourier expansion; $\phi(k)$ is the momentum-space wave function. If $\phi(k)$ is peaked near $k_0$ with spread $\Delta k$, then $\psi(x,0)$ is a localized packet of position spread of order $1/\Delta k$ — the Heisenberg uncertainty relation: narrow in momentum, broad in position.

Time evolution attaches a phase $e^{-i\omega(k)t}$ to each component, with $\omega(k) = \hbar k^2/2m$:

$$\psi(x,t) = \frac{1}{\sqrt{2\pi}}\int\phi(k)\,e^{i(kx - \omega(k)t)}\,dk.$$

Because $\omega(k)$ is quadratic, not linear, components at different momenta move at different speeds and the packet *spreads*. For a Gaussian initial packet of width $\sigma_0$, the position-space width grows as $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/2m\sigma_0^2)^2}$ — slowly at early times, linearly in $t$ at late times. This spreading is computable, checkable, and has no classical analog: a baseball thrown in a definite direction stays on its trajectory; a quantum particle disperses.

![Plot of Gaussian wave-packet width σ(t) vs](../images/03-the-schrodinger-equation-fig-07.png)
*Figure 3.7 — Plot of Gaussian wave-packet width σ(t) vs*

---

## What the equation does and does not tell you

The dynamical law is now in hand. An accounting of what it supplies and what it does not.

It supplies a precise algorithm: write down $\hat{H}$, find its eigenstates and eigenvalues, expand the initial condition, attach phases, sum. Predictions for every measurement outcome at any later time, for any observable, follow. The predictions are probabilities — not from ignorance but because the theory is genuinely probabilistic at the level of individual outcomes (Bell's theorem makes this unavoidable). The equation is linear, first-order in time, and Hermitian; normalization is preserved and spectral lines come out correct.

It does not supply an explanation of *why* this equation rather than its neighbors. The postulate status is honest, not evasive; Newton's second law has the same status inside classical mechanics. The Schrödinger equation is tested by its consequences, which include the hydrogen spectrum, tunneling, the laser, the transistor, and the MRI machine. That is its justification.

It also does not tell you what $\psi$ *is* — a real physical field, a representation of an observer's knowledge, or a guiding wave for a hidden particle. The equation is agnostic. All interpretations — many-worlds, Copenhagen, Bohmian mechanics, relational QM, epistemic approaches — agree on the predictions of the Schrödinger equation and disagree on what it describes. Unit 5 returns to this. For now: the formalism works regardless of interpretation, and the predictions are the same either way.

---

## What would change my mind

The Schrödinger equation's central claim — that state evolution under $i\hbar\partial_t\psi = \hat{H}\psi$ with $\hat{H}$ Hermitian gives the right probabilities via the Born rule — has survived a century of experimental tests in the non-relativistic regime. Spontaneous collapse models (GRW: Ghirardi, Rimini, Weber, 1986) propose a small violation, and ongoing experiments — including searches for collapse-induced X-ray emission in solids — are testing this. To date, standard Schrödinger evolution has held. A confirmed deviation would force a different equation here. Absent one, the equation given is the correct one for non-relativistic quantum mechanics.

---

## Still puzzling

**Why a postulate?** Every fundamental theory has a point where its laws stop having deeper explanations and become axioms. Newton's second law occupies the same position. "Postulate" is not a confession of ignorance but the correct description of where a theory begins. Why the Schrödinger equation has its specific form — why $i\hbar\partial_t$ and not something else — is a question that likely belongs to quantum field theory or to a still-undiscovered framework.

**The interpretation problem.** The Schrödinger equation gives $\psi$; the Born rule gives $|\psi|^2$ as a probability. Neither says what $\psi$ is. The formalism is silent, and the silence is not a defect — all interpretations agree on the predictions. Unit 5 takes this up directly.

**The measurement problem.** The Schrödinger equation describes unitary, deterministic evolution; measurement, in the standard formulation, is a non-unitary, stochastic update. These are in apparent tension. Decoherence (Zurek, 2003) gives a partial answer by showing that environmental interactions rapidly suppress macroscopic superpositions, but it does not explain how a definite outcome emerges from unitary evolution. Open at the level of foundations, closed at the level of computing predictions.

**The arrow of time.** The Schrödinger equation is time-reversal symmetric. Wave packets spread, but the equation run backward narrows a broad packet. Physical experience singles out the spreading direction. The explanation likely lies in thermodynamics and initial conditions, not in the equation itself.

---

## LLM exercises

The following exercises are designed to be worked interactively with a language model. Use the model to check your reasoning step by step — not to generate answers, but to test whether you can explain each step clearly enough that the model can follow and push back.

**L1.** Dictate the plausibility argument for the Schrödinger equation to the model, starting only from "a free particle is described by a wave $\psi = Ae^{i(kx-\omega t)}$" and the de Broglie and Einstein relations. Ask the model to identify every step that is a genuine logical consequence and every step that is an assumption or postulate. Count the postulates.

**L2.** Give the model a specific wave function — say $\psi(x,t) = A e^{-x^2/a^2} e^{-iEt/\hbar}$ for some constants $A$, $a$, $E$ you choose — and ask: is this a solution of the time-independent Schrödinger equation for some $V(x)$? If so, what is $V(x)$? Work out the answer yourself by computing $\hat{H}\psi/\psi$ and compare with the model.

**L3.** State in plain language, to the model, why the Hermiticity of $\hat{H}$ guarantees that $d/dt\int|\psi|^2 dx = 0$ — without writing any integrals. Ask the model to convert your verbal explanation into the mathematical proof and flag any steps you described imprecisely.

**L4.** Construct a normalized superposition of the first two infinite-square-well eigenstates. Ask the model to compute $\langle x\rangle(t)$ step by step. Do the calculation yourself first. Compare not just the final answer but each intermediate step — the expansion of $|\psi|^2$, the identification of the cross term, the integral of $x\psi_1\psi_2$, the Bohr frequency. Identify any step where your approach and the model's diverged.

**L5.** Ask the model to explain why a free-particle plane wave $\psi = Ae^{ikx}$ is not a physical state, even though it satisfies the Schrödinger equation. Then give your own explanation. Ask the model to compare the two explanations and identify which one is more physically precise — and whether "not normalizable" is a sufficient explanation or whether there is something deeper to say about the role of wave packets and the Fourier representation.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Schrödinger, E. "Quantisierung als Eigenwertproblem (Erste Mitteilung)." *Annalen der Physik* 79, 361–376 (1926). https://doi.org/10.1002/andp.19263840404
2. Born, M. "Zur Quantenmechanik der Stoßvorgänge." *Zeitschrift für Physik* 37, 863–867 (1926). https://doi.org/10.1007/BF01397477
3. The Nobel Prize in Physics 1954 — Max Born. https://www.nobelprize.org/prizes/physics/1954/born/facts/
4. Aspect, A., Grangier, P. & Roger, G. "Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment." *Physical Review Letters* 49, 91 (1982).
5. The Nobel Prize in Physics 2022 — Aspect, Clauser, Zeilinger. https://www.nobelprize.org/prizes/physics/2022/
6. Ghirardi, G. C., Rimini, A. & Weber, T. "Unified dynamics for microscopic and macroscopic systems." *Physical Review D* 34, 470–491 (1986).
7. Zurek, W. H. "Decoherence, einselection, and the quantum origins of the classical." *Reviews of Modern Physics* 75, 715–775 (2003). https://doi.org/10.1103/RevModPhys.75.715
