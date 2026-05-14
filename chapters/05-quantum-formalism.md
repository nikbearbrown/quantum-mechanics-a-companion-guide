# Unit 5 — Quantum Formalism

> The postulates are settled. The interpretation of measurement is not. This unit teaches you to tell which is which, derive the uncertainty principle the way Robertson actually proved it, and stop apologizing for the open question at the center of the theory.

---

## 1. What this chapter is doing

This unit takes the formalism you have been using piecewise — Hilbert spaces from Unit 2, the Schrödinger equation from Unit 3, the worked examples of Unit 4 — and assembles it into the five postulates of quantum mechanics. Griffiths Chapter 3 develops them; Cohen-Tannoudji, Diu, and Laloë Volume I §III.A states them as a numbered list. The pop-sci companion handles this material in two places: Chapter 2 (introduces uncertainty via a balloon analogy that TIKTOC Part V flags as misleading) and Chapter 7 (treats measurement and collapse informally, sometimes as "philosophy"). The companion's job here is heavier than in any previous unit. Three things: state the postulates cleanly, derive the Heisenberg–Robertson uncertainty inequality rigorously and correct the balloon analogy explicitly, and be honest about the measurement problem — name the live interpretations without pretending the field has settled on one. Postulates 1, 2, 3, and 5 are not in dispute among working physicists. Postulate 4 (collapse) is. You should leave this chapter able to tell those situations apart and to refuse, when pressed, to fake consensus where there is none.

## 2. Learning objectives

By the end of this chapter you should be able to:

1. **State** the five postulates of quantum mechanics and identify which physical requirement each one enforces (Hermiticity → real outcomes, unitarity → conserved probability). (Bloom: Remember / Understand.)
2. **Derive** the Robertson uncertainty inequality from the Cauchy–Schwarz inequality and apply it to position and momentum. (Bloom: Apply.)
3. **Distinguish** preparation uncertainty (Robertson 1929) from measurement-disturbance uncertainty (Heisenberg's microscope; Ozawa 2003) and explain why the balloon analogy conflates them. (Bloom: Analyze.)
4. **Identify** when two observables are compatible from their commutator and construct a complete set of commuting observables (CSCO) for a given physical system. (Bloom: Apply / Analyze.)
5. **Name** the major interpretations of quantum mechanics, state what each one says about the measurement postulate, and articulate at least one empirical fact each one handles well and one each one handles awkwardly. (Bloom: Evaluate.)
6. **Compute** $\sigma_x \sigma_p$ for the harmonic-oscillator ground state and show that it saturates the Robertson bound. (Bloom: Apply.)

## 3. The motivating problem

Two students sit in a library with the original 1927 and 1929 papers. The first paper is Werner Heisenberg's "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik" in *Zeitschrift für Physik* — the one with the gamma-ray microscope thought experiment. The second is Howard P. Robertson's "The Uncertainty Principle" in *Physical Review* 34, 163, the four-page proof that the Heisenberg inequality is a corollary of the Cauchy–Schwarz inequality applied to any two Hermitian operators. The students are arguing.

The first student says: *uncertainty is about measurement*. You cannot find the position of an electron without bouncing a photon off it. The photon transfers momentum. Position measurement disturbs the momentum. That is the principle. The balloon analogy from their popular-physics book says the same thing — to find a balloon in the dark you have to bump into it, and bumping into it moves it. That is what $\Delta x\,\Delta p \gtrsim \hbar$ means.

The second student says: *that's how Heisenberg motivated it in 1927, but read Robertson 1929. The inequality is a property of the state. There is no measurement in the proof. The state itself has a width in position and a width in momentum, and the product of those widths is bounded below by $\hbar/2$. Nobody had to look at the particle for that bound to hold. The balloon analogy gets the answer right for the wrong reason.*

Both students are partially right. Heisenberg's microscope is a real physical effect (now formalized as measurement-disturbance uncertainty by Ozawa 2003). The Robertson bound is a *different* statement about state preparation. They are related, not identical, and the pop-sci balloon analogy conflates them. This is the chapter that pulls them apart. The argument the students are having is a productive one — the productive argument that ends with two different inequalities, two different physical meanings, and one clear statement about what the principle actually says.

This is also the chapter where the measurement problem comes up explicitly. After the formalism is in place, the next obvious question is: *what happens during a measurement?* And the honest answer is that physicists do not agree. The unit will not resolve that disagreement. It will teach you to see it clearly.

## 4. Concept blocks

### 4A. The five postulates

A theory is not its applications. A theory is the small set of statements from which the applications follow. Quantum mechanics has five postulates. Griffiths Chapter 3 develops them; Cohen-Tannoudji Volume I §III.A states them as a list; Sakurai, *Modern Quantum Mechanics*, 3rd ed., Chapter 1, gives an operator-first version. They follow.

**Postulate 1 (State).** Every isolated quantum system is associated with a complex Hilbert space $\mathcal{H}$. A pure state of the system is a normalized vector $|\psi\rangle \in \mathcal{H}$, defined up to a global phase. The vectors $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ represent the same physical state.

**Postulate 2 (Observables).** Every physical observable $A$ corresponds to a Hermitian (self-adjoint) operator $\hat{A}$ on $\mathcal{H}$. The eigenvalues of $\hat{A}$ are the possible outcomes of measuring $A$.

*Why Hermitian?* Because measurement outcomes are real numbers, and the eigenvalues of a Hermitian operator are guaranteed real. To see this in two lines: if $\hat{A}|a\rangle = a|a\rangle$ then $\langle a|\hat{A}|a\rangle = a$. Take the complex conjugate of both sides: $\overline{\langle a|\hat{A}|a\rangle} = \overline{a}$. But $\overline{\langle a|\hat{A}|a\rangle} = \langle a|\hat{A}^\dagger|a\rangle = \langle a|\hat{A}|a\rangle$ (using $\hat{A} = \hat{A}^\dagger$). So $a = \overline{a}$, which means $a$ is real. Hermiticity is not arbitrary; it is the algebraic encoding of "outcomes are real numbers."

**Postulate 3 (Born rule).** If a system is in state $|\psi\rangle$ and a measurement of observable $A$ is performed, the probability of obtaining eigenvalue $a_n$ is

$$P(a_n) = |\langle a_n | \psi \rangle|^2,$$

where $|a_n\rangle$ is the normalized eigenstate corresponding to $a_n$. For continuous spectra, replace the discrete projection with a probability density and an integral over the spectral measure.

**Postulate 4 (Collapse).** Immediately after the measurement yields outcome $a_n$, the state of the system is $|a_n\rangle$ (the corresponding eigenstate), up to normalization. This is the postulate that does almost all the philosophical work in QM. §4D returns to it in detail.

**Postulate 5 (Time evolution).** Between measurements, the state evolves unitarily according to the Schrödinger equation:

$$i\hbar\,\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle,$$

where $\hat{H}$ is the Hamiltonian (the operator corresponding to the observable "total energy"). Equivalently, $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$ with $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ for time-independent $\hat{H}$, and $\hat{U}$ is unitary: $\hat{U}^\dagger \hat{U} = \hat{1}$.

*Why unitary?* Because probability must be conserved: $\langle \psi(t)|\psi(t)\rangle = 1$ at all times. If $|\psi(t)\rangle = \hat{U}(t)|\psi(0)\rangle$, then

$$\langle \psi(t)|\psi(t)\rangle = \langle \psi(0)|\hat{U}^\dagger \hat{U}|\psi(0)\rangle = \langle \psi(0)|\psi(0)\rangle = 1$$

requires $\hat{U}^\dagger \hat{U} = \hat{1}$. Unitarity is not arbitrary; it is the algebraic encoding of "total probability is one, always."

**Structural observation, important.** Postulates 1, 2, 3, and 5 are uncontroversial among working physicists. Every interpretation of QM uses them. Postulate 4 is where the interpretations diverge. Copenhagen accepts collapse as a postulate. Many-Worlds denies that collapse happens at all. Bohmian mechanics replaces it with a deterministic guidance equation. QBism reads it as a Bayesian belief update. The mathematics is identical across these views; the *story* about what the math is describing is not. This unit returns to that disagreement in §4D, but you should hold the structure in mind from the start: four settled postulates, one contested postulate, and a century of literature trying to figure out what to do about the contested one.

### 4B. The Heisenberg–Robertson uncertainty principle

This is the central correction. The pop-sci book introduces uncertainty with a balloon analogy: to find a balloon in the dark you have to bump into it, the bump moves it, so you cannot know both where it is and how it is moving. TIKTOC Part V flags this as misleading. It is. Here is what is actually going on.

**The historically first version (Heisenberg 1927, microscope thought experiment).** Heisenberg argued — in his 1927 *Zeitschrift für Physik* paper, "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik" — that to measure an electron's position with resolution $\Delta x$, you have to illuminate it with light of wavelength $\lambda \lesssim \Delta x$. A photon of that wavelength carries momentum $p_\gamma \sim h/\lambda \sim h/\Delta x$. The photon-electron scattering transfers some of that momentum to the electron, kicking it by an amount $\Delta p \sim h/\Delta x$. Multiplying:

$$\Delta x \cdot \Delta p \sim h.$$

This is the right *answer*. It is also a story about *what one measurement does to a subsequent measurement*. The position measurement disturbs the momentum. The uncertainty here is *epistemic* — it is what we cannot simultaneously know because of how measurement interacts with the system.

Bohr corrected Heisenberg almost immediately. Heisenberg added a note to the proofs of his paper acknowledging Bohr's correction. The microscope picture is a useful intuition pump, but it is not the principle.

**The right statement (Robertson 1929 + Schrödinger 1930).** Howard P. Robertson, "The Uncertainty Principle," *Physical Review* 34, 163 (1 July 1929), proved a *theorem*: for any two Hermitian operators $\hat{A}$, $\hat{B}$ and any state $|\psi\rangle$ on which they both act,

$$\boxed{\sigma_A \,\sigma_B \;\geq\; \tfrac{1}{2}\,\bigl|\langle [\hat{A}, \hat{B}]\rangle\bigr|}$$

where $\sigma_A^2 = \langle \hat{A}^2\rangle - \langle\hat{A}\rangle^2$ is the variance and $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ is the commutator.

**Derivation.** This is short, and the chapter does not punt it. Define the shifted operators

$$\hat{A}' = \hat{A} - \langle\hat{A}\rangle, \qquad \hat{B}' = \hat{B} - \langle\hat{B}\rangle.$$

These are still Hermitian, with mean zero, and $\sigma_A^2 = \langle\hat{A}'^2\rangle$, $\sigma_B^2 = \langle\hat{B}'^2\rangle$. Define two vectors in the Hilbert space:

$$|f\rangle = \hat{A}'|\psi\rangle, \qquad |g\rangle = \hat{B}'|\psi\rangle.$$

Their norms are $\langle f|f\rangle = \sigma_A^2$ and $\langle g|g\rangle = \sigma_B^2$. The Cauchy–Schwarz inequality says

$$\langle f|f\rangle\,\langle g|g\rangle \;\geq\; |\langle f|g\rangle|^2.$$

So $\sigma_A^2 \sigma_B^2 \geq |\langle\psi|\hat{A}'\hat{B}'|\psi\rangle|^2$.

Write $|z|^2 = (\text{Re}\,z)^2 + (\text{Im}\,z)^2 \geq (\text{Im}\,z)^2$ for any complex number. So

$$\sigma_A^2 \sigma_B^2 \;\geq\; \bigl(\text{Im}\,\langle\psi|\hat{A}'\hat{B}'|\psi\rangle\bigr)^2.$$

Now compute the imaginary part. For any complex number $z$, $\text{Im}\,z = (z - \overline{z})/(2i)$, so

$$\text{Im}\,\langle\psi|\hat{A}'\hat{B}'|\psi\rangle = \frac{1}{2i}\bigl(\langle\psi|\hat{A}'\hat{B}'|\psi\rangle - \overline{\langle\psi|\hat{A}'\hat{B}'|\psi\rangle}\bigr) = \frac{1}{2i}\bigl(\langle\psi|\hat{A}'\hat{B}'|\psi\rangle - \langle\psi|\hat{B}'\hat{A}'|\psi\rangle\bigr) = \frac{1}{2i}\langle\psi|[\hat{A}', \hat{B}']|\psi\rangle.$$

(The conjugate of $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ is $\langle\psi|\hat{B}'^\dagger\hat{A}'^\dagger|\psi\rangle = \langle\psi|\hat{B}'\hat{A}'|\psi\rangle$ because the shifted operators are still Hermitian.) The commutator of the shifted operators equals the commutator of the originals: $[\hat{A}', \hat{B}'] = [\hat{A}, \hat{B}]$. So

$$\text{Im}\,\langle\psi|\hat{A}'\hat{B}'|\psi\rangle = \frac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle.$$

(Note: $[\hat{A}, \hat{B}]/i$ is Hermitian, so $\langle [\hat{A}, \hat{B}]\rangle/(2i)$ is real, which is what we want for the imaginary part.) Squaring and combining:

$$\sigma_A^2 \sigma_B^2 \;\geq\; \frac{1}{4}\bigl|\langle [\hat{A}, \hat{B}]\rangle\bigr|^2,$$

i.e., the Robertson bound. That is the whole derivation. Cauchy–Schwarz on shifted operators, take the imaginary part, the commutator falls out.

**For position and momentum**, $[\hat{x}, \hat{p}] = i\hbar$ (a constant — independent of the state), so $|\langle[\hat{x}, \hat{p}]\rangle| = \hbar$ for every state, and

$$\sigma_x \sigma_p \;\geq\; \frac{\hbar}{2}.$$

Note: $\hbar/2$, not $\hbar$. The factor of two is part of the answer. Many pop-sci treatments drop it; some textbook treatments do too. It is wrong to drop it.

**Schrödinger's strengthening (1930).** Erwin Schrödinger, "Zum Heisenbergschen Unschärfeprinzip," *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, Physikalisch-mathematische Klasse (1930), pp. 296–303 [verify pagination], added the real part to the bound:

$$\sigma_A^2 \sigma_B^2 \;\geq\; \left(\tfrac{1}{2}\langle\{\hat{A}', \hat{B}'\}\rangle\right)^2 + \left(\tfrac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle\right)^2$$

where $\{\hat{A}', \hat{B}'\} = \hat{A}'\hat{B}' + \hat{B}'\hat{A}'$ is the anticommutator of the shifted operators (its expectation is twice the covariance). When the covariance vanishes (state is uncorrelated in $A$ and $B$), Schrödinger's bound collapses to Robertson's. For states with nonzero covariance, Schrödinger's is tighter. The derivation is the same as above but keeps the real part of $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ as well as the imaginary part — apply $|z|^2 = (\text{Re}\,z)^2 + (\text{Im}\,z)^2$ instead of throwing the real part away.

**The balloon-analogy correction.** Now state it sharply. The Robertson bound $\sigma_A \sigma_B \geq \tfrac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$ is a statement about *the state*. It says: there is no quantum state $|\psi\rangle$ for which $\sigma_A$ and $\sigma_B$ are simultaneously smaller than allowed by the commutator. The bound holds *before anyone measures anything*. There is no apparatus in the inequality. There is no momentum kick. There is no balloon. The uncertainty is *intrinsic to the state*, derived from the algebra of non-commuting operators on a Hilbert space.

The balloon analogy gets $\Delta x \cdot \Delta p \gtrsim \hbar$ right at the level of order-of-magnitude intuition, and it is faithful to Heisenberg 1927's pedagogical motivation. But it gives a wrong picture of what the inequality *is*. A student who learns the balloon will conflate state preparation with measurement disturbance, which is exactly the conflation that physicists worked out of the theory by 1930 and that the Ozawa 2003 results (next paragraph) finally formalized into a separate inequality.

**The modern measurement-disturbance separation.** Masanao Ozawa, "Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement," *Physical Review A* 67, 042105 (2003), showed that the *measurement-disturbance* version — the one Heisenberg's microscope was actually about — requires a different inequality, one that mixes the state uncertainty with the noise of the measuring apparatus and the disturbance the apparatus inflicts on a subsequent measurement. Experimental tests (e.g., Erhart et al., *Nature Physics* 8, 185 (2012) [verify]) have verified Ozawa's version and have shown that the measurement-disturbance product can be made *smaller* than the naive Heisenberg microscope would suggest. The Robertson bound is *preparation uncertainty*; Ozawa's is *measurement-disturbance uncertainty*. They are related but not identical, and the failure to distinguish them is exactly the failure mode the balloon analogy reproduces.

If you take only one thing from this section: *the uncertainty principle is about quantum states, not about clumsy probes*. Quantum states cannot be simultaneously narrow in two non-commuting observables. That is the principle. The measurement story is a separate story, with its own (Ozawa) inequality.

### 4C. Commutators and compatible observables

The Robertson bound tells you what the commutator does — it sets the joint uncertainty floor. Two operators $\hat{A}$ and $\hat{B}$ are **compatible** if they commute, $[\hat{A}, \hat{B}] = 0$. Equivalently (theorem: Griffiths §3.5), compatible observables admit a common eigenbasis: a basis $\{|n\rangle\}$ such that every $|n\rangle$ is an eigenstate of both $\hat{A}$ and $\hat{B}$. The eigenvalues $(a_n, b_n)$ then label the state simultaneously, with no joint-uncertainty floor.

**Concrete examples.**

- $[\hat{x}, \hat{p}_y] = 0$. Position along one axis and momentum along a perpendicular axis are compatible. The state can be sharp in both.
- $[\hat{x}, \hat{p}_x] = i\hbar$. Position and momentum along the *same* axis are incompatible. The Robertson bound applies.
- $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$ (Unit 7). Components of angular momentum along different axes are incompatible.
- $[\hat{L}^2, \hat{L}_z] = 0$. The squared magnitude of angular momentum and one component are compatible. This is why hydrogen orbitals are labeled by $(n, \ell, m)$ (Unit 6): the operators $\hat{H}$, $\hat{L}^2$, $\hat{L}_z$ all commute, share an eigenbasis, and their eigenvalues label the state.

**The complete set of commuting observables (CSCO).** A CSCO is a maximal set of mutually commuting Hermitian operators whose joint eigenvalues uniquely label every basis state. The CSCO replaces the classical idea of "labels for the state." For hydrogen the CSCO is $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$, giving the labels $(n, \ell, m, m_s)$ — and that label set is exactly the quantum-number set the pop-sci book lists without explanation in its periodic-table chapter (TIKTOC Part VI). The reason there are these labels and not others is that this collection of operators commutes; no larger commuting set exists; the eigenvalues are dense enough to fix every state.

**Conservation and the Heisenberg picture.** In the Heisenberg picture, where operators evolve and states stay fixed, the time derivative of an operator $\hat{O}$ is

$$\frac{d\hat{O}}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{O}] + \frac{\partial\hat{O}}{\partial t}.$$

If $\hat{O}$ does not depend explicitly on time and $[\hat{H}, \hat{O}] = 0$, then $\hat{O}$ is a constant of the motion — its expectation value is conserved. The connection between conservation laws and commuting observables is direct: operators that commute with the Hamiltonian are conserved quantities; they label states stably over time. This is the Noether structure inside QM.

**Misconception.** "Non-commuting means you cannot measure both." More carefully: you cannot measure both *simultaneously to arbitrary precision*. You can measure them in sequence. The cost is that the second measurement disturbs the first. If you measure $\hat{x}$ and find $x = x_0$, the state collapses to (approximately) $|x_0\rangle$. If you then measure $\hat{p}$ and find $p = p_0$, the state collapses to $|p_0\rangle$. If you then re-measure $\hat{x}$, the outcome is no longer $x_0$ in general — the second measurement destroyed the first piece of information. Non-commuting observables have well-defined measurement procedures individually; they just do not have simultaneous values.

### 4D. Measurement, collapse, and the contested territory

Here the chapter must be honest. Postulate 4 — that the state collapses to the corresponding eigenstate upon measurement — does almost all of the philosophical work in QM, and is the postulate around which the entire foundations literature has been written for ninety years. Physicists do not agree on what it means, what it describes, or even whether it should be a postulate at all. The chapter will not resolve this. It will name it.

**The bare statement.** Standard QM (Copenhagen, in the textbook sense) tells you:

- Between measurements, $|\psi\rangle$ evolves continuously and deterministically by Postulate 5 (unitary, generated by $\hat{H}$).
- During a measurement, $|\psi\rangle$ jumps discontinuously and stochastically to an eigenstate of the measured observable (Postulate 4, collapse).
- The probability of each outcome is given by the Born rule (Postulate 3).

There are two evolution laws — one unitary, one collapse — and the rule for switching between them is "when a measurement happens." But a measurement is itself a physical interaction between system and apparatus. Why is the apparatus described classically and the system quantum-mechanically? Where exactly is the dividing line? This is the **measurement problem**.

John Bell, "Against 'Measurement,'" *Physics World* 3, 33 (August 1990), put it directly: a fundamental theory should not have the word "measurement" in its postulates. The apparatus is made of quantum constituents; it should evolve by the same dynamics as the system. If collapse is real, it should follow from the dynamics, not be inserted by hand. Sixty-two years after Schrödinger, Bell said, the field deserved an exact formulation. As of 2026, it does not have one that physicists agree on. Bell's complaint remains live.

**The major live interpretations.** The chapter names them, not adjudicates.

1. **Copenhagen** (Bohr, Heisenberg, ~1927). Quantum systems described by $\psi$; classical apparatus described classically; collapse on measurement. The textbook version. Strength: operational, calculational, what working physicists default to. Weakness: where is the quantum-classical boundary, and what counts as a measurement?

2. **Many-Worlds / Everett** (Hugh Everett III, "'Relative State' Formulation of Quantum Mechanics," *Reviews of Modern Physics* 29, 454 (1957)). There is no collapse. The combined system + apparatus + observer evolves unitarily; the apparent collapse is the observer becoming correlated with one branch of a larger superposition. Strength: removes the postulate that bothered Bell. Weakness: probabilities now refer to "branches" — what does it mean to say outcome $a_n$ has probability $|\langle a_n|\psi\rangle|^2$ when all outcomes occur in different branches? (The literature has answers — decision-theoretic derivations by Deutsch and Wallace — but they are contested.)

3. **Bohmian / pilot-wave** (de Broglie 1927, Bohm 1952; David Bohm, "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables," *Physical Review* 85, 166 and 180 (1952)). Particles have definite positions at all times, guided by a "pilot wave" $\psi$ that evolves by Schrödinger's equation. Apparent collapse follows from the dynamics, not from a separate postulate. Strength: deterministic, no measurement problem. Weakness: explicitly nonlocal in a way that fits uncomfortably with special relativity (no problem at the level of standard QM predictions, but awkward for extension to QFT).

4. **QBism (Quantum Bayesianism)** (Caves, Fuchs, Schack, ~2002 onward; Christopher Fuchs, "QBism, the Perimeter of Quantum Bayesianism," arXiv:1003.5209 (2010)). The wave function $\psi$ is the *agent's degree of belief* about future measurement outcomes; the Born rule is a normative rule for updating those beliefs given evidence; collapse is the update. Strength: dissolves the measurement problem by reframing $\psi$ epistemically. Weakness: rejects the realist reading; some find it unacceptably anti-realist about quantum systems.

5. **Dynamical collapse models** (Ghirardi, Rimini, Weber, "Unified dynamics for microscopic and macroscopic systems," *Physical Review D* 34, 470 (1986); Continuous Spontaneous Localization, Pearle 1989; review in Angelo Bassi, Kinjalk Lochan, Seema Satin, Tejinder P. Singh, Hendrik Ulbricht, "Models of wave-function collapse, underlying theories, and experimental tests," *Reviews of Modern Physics* 85, 471 (2013)). The Schrödinger equation is *modified* by a small nonlinear, stochastic term that causes spontaneous localization at a rate proportional to mass. The collapse is a physical process, not a postulate. Strength: testable in principle — predicts small deviations from standard QM that can be probed experimentally. Weakness: the parameters were tuned post hoc to be invisible at known scales; no positive experimental signal has been seen. Cantilever and matter-wave experiments (e.g., Vinante et al., *Physical Review Letters* (2017) and follow-ups [verify current best bounds]) have steadily tightened the bounds on the GRW/CSL parameters without confirming the models.

6. **Decoherence** (Zurek and others, ~1970s onward; Maximilian Schlosshauer, *Decoherence and the Quantum-to-Classical Transition* (Springer, 2007)). Not strictly an interpretation but a mechanism: interaction with the environment rapidly suppresses interference between macroscopically distinct states, producing apparent classical behavior. Decoherence does *not* by itself solve the measurement problem — it explains why the off-diagonal coherences vanish (so you do not see superposition of "alive cat" and "dead cat"), but it does not explain which definite outcome you actually observe. Decoherence is consistent with Copenhagen, with Many-Worlds (it picks out the branches), with collapse models, and with Bohmian mechanics. It is part of the answer that every interpretation has to incorporate, not an interpretation in itself.

**Schlosshauer, Kofler, and Zeilinger conducted a survey** of physicists at a foundations conference and published the results as "A snapshot of foundational attitudes toward quantum mechanics," *Studies in History and Philosophy of Modern Physics* 44, 222 (2013). Among 33 respondents at a small specialist meeting, the most popular position was Copenhagen-flavored (around 42%), followed by information-based / QBism-adjacent views (~24%) and Many-Worlds (~18%), with smaller percentages for Bohmian, collapse models, and others [verify exact percentages against the published article]. The sample was small and self-selected and should not be over-read, but the headline result is robust: *there is no consensus*. Working physicists disagree about what their own most successful theory describes.

**The misconception that needs explicit correction: "the observer's consciousness causes wave-function collapse."** This is the von Neumann–Wigner interpretation. Eugene Wigner sketched it in "Remarks on the Mind-Body Question" in *The Scientist Speculates: An Anthology of Partly-Baked Ideas*, edited by I. J. Good (Heinemann, 1961), reprinted in Wheeler & Zurek, *Quantum Theory and Measurement* (Princeton, 1983). Wigner himself later abandoned the position. It is *not* the mainstream view among working physicists. The 2013 survey above found essentially no support for consciousness-causes-collapse. The pop-sci book's flirtation with "observer creates reality" framing (TIKTOC line 222) is exactly the place a careful student should push back: there is a measurement problem; consciousness is not the standard answer; decoherence is the standard mechanism for the apparent quantum-to-classical transition; the interpretive disagreement is about whether decoherence-plus-something-else (and which something else) solves the problem completely.

**Recent foundational developments.** Daniela Frauchiger and Renato Renner, "Quantum theory cannot consistently describe the use of itself," *Nature Communications* 9, 3711 (2018), constructed a thought experiment in which different observers, reasoning consistently within quantum mechanics, reach contradictory conclusions about a measurement outcome. The paper has generated active debate. Each interpretation resolves the apparent paradox by giving up a different assumption — Copenhagen by restricting which observers count, Many-Worlds by clarifying what "outcome" means across branches, and so on. A 2024 reply by V. Vilasini and collaborators in *Nature Communications* 15, 2782 (2024) [verify] re-examines which assumption Frauchiger-Renner forces each interpretation to drop. The chapter cites Frauchiger-Renner as evidence that the foundations are still under active construction.

**Weak measurement.** Yakir Aharonov, David Z. Albert, and Lev Vaidman, "How the result of a measurement of a component of the spin of a spin-1/2 particle can turn out to be 100," *Physical Review Letters* 60, 1351 (1988), introduced the formal framework for measurements that disturb the state weakly and extract less than full information. Weak measurements have moved from foundations curiosity to a precision-metrology tool — used, for example, to amplify small spin signals and to characterize quantum trajectories.

**A working physicist's honest position.** The five postulates work. They predict experimental outcomes to many decimal places in every domain they have been tested in. The fourth postulate has an interpretation problem; the other four do not. A working physicist can compute with the postulates without committing to an interpretation; the calculation gives the same answer regardless. The interpretation question matters for *what we think the theory is describing*, and that question is open. The chapter that ends here does not pretend it is closed.

## 5. Worked example: the harmonic-oscillator ground state saturates the Robertson bound

This is the unit-bridging example. In Unit 4 you built the harmonic-oscillator ground state explicitly:

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right).$$

In Unit 5 you test it against Robertson.

**Compute $\sigma_x^2$.** By symmetry, $\langle\hat{x}\rangle = 0$, so $\sigma_x^2 = \langle\hat{x}^2\rangle$. For a Gaussian of the form $\psi_0 \propto e^{-\alpha x^2/2}$ with $\alpha = m\omega/\hbar$:

$$\langle x^2 \rangle = \int_{-\infty}^{\infty} x^2 |\psi_0(x)|^2\,dx = \int_{-\infty}^{\infty} x^2 \sqrt{\frac{\alpha}{\pi}}\,e^{-\alpha x^2}\,dx = \frac{1}{2\alpha} = \frac{\hbar}{2m\omega}.$$

So $\sigma_x = \sqrt{\hbar/(2m\omega)}$.

**Compute $\sigma_p^2$.** By symmetry, $\langle \hat{p}\rangle = 0$, so $\sigma_p^2 = \langle\hat{p}^2\rangle$. Use $\hat{p} = -i\hbar\,d/dx$:

$$\hat{p}\,\psi_0 = -i\hbar\,\frac{d\psi_0}{dx} = -i\hbar\,(-\alpha x)\,\psi_0 = i\hbar\alpha x\,\psi_0.$$

So $\hat{p}^2 \psi_0 = -\hbar^2\,d^2\psi_0/dx^2$. Compute the second derivative:

$$\frac{d^2\psi_0}{dx^2} = \frac{d}{dx}(-\alpha x\,\psi_0) = (-\alpha + \alpha^2 x^2)\psi_0.$$

Therefore $\hat{p}^2\psi_0 = \hbar^2(\alpha - \alpha^2 x^2)\psi_0$, and

$$\langle\hat{p}^2\rangle = \hbar^2 \alpha - \hbar^2 \alpha^2 \langle x^2\rangle = \hbar^2 \alpha - \hbar^2 \alpha^2 \cdot \frac{1}{2\alpha} = \hbar^2\alpha - \frac{\hbar^2\alpha}{2} = \frac{\hbar^2\alpha}{2} = \frac{\hbar m\omega}{2}.$$

So $\sigma_p = \sqrt{\hbar m\omega/2}$.

**Product.**

$$\sigma_x \sigma_p = \sqrt{\frac{\hbar}{2m\omega}}\cdot\sqrt{\frac{\hbar m\omega}{2}} = \sqrt{\frac{\hbar^2}{4}} = \frac{\hbar}{2}.$$

Exactly the Robertson floor. The oscillator ground state is the *minimum-uncertainty state* — equality, not inequality. This is why coherent states (Gaussians built on the ladder-operator algebra) are called "minimum-uncertainty" states: $\psi_0$ is the simplest example, and every coherent state $|\alpha\rangle = D(\alpha)|0\rangle$ (where $D$ is a displacement operator) inherits the saturation.

For $n \geq 1$, the same computation (using ladder operators, exercise 4 below) gives

$$\sigma_x \sigma_p = \bigl(n + \tfrac{1}{2}\bigr)\hbar,$$

which exceeds $\hbar/2$ for every $n \geq 1$. Only the ground state saturates the bound. Connect this back to Unit 4: the zero-point energy $\hbar\omega/2$ and the saturation of the Robertson bound are *the same fact*. The state's product-of-widths floor and the state's energy floor are two faces of one constraint — confined quantum states cannot have zero kinetic energy and cannot be simultaneously sharp in $x$ and $p$, and these are the same impossibility.

**Lesson.** Robertson is not abstract algebra. It is a concrete bound on real wave functions, saturated by the simplest real ground state you have already computed. The balloon-analogy reader sees the bound as a measurement constraint; the Robertson reader sees it as a property of the Gaussian. Both readers get $\sigma_x \sigma_p \geq \hbar/2$. Only the second reader knows why.

**Limit.** Saturating the bound is a special property of the *ground state of a quadratic Hamiltonian*. For non-Gaussian states (excited oscillator states, particle-in-a-box eigenstates, the hydrogen ground state in 3D), the product $\sigma_x \sigma_p$ exceeds $\hbar/2$. Exercise 4 verifies this for the infinite square well.

## 6. Reading map

| Topic | Griffiths (4th ed.) | Pop-sci book | Companion |
|---|---|---|---|
| The five postulates | §3.1–3.4 | (scattered; not as postulates) | §4A |
| Hermitian operators and real eigenvalues | §3.3 | (absent) | §4A |
| Heisenberg microscope (motivation) | (historical preamble) | Ch. 2 [BOOK; balloon analogy] | §4B |
| Robertson uncertainty derivation | §3.5 | (absent — TIKTOC V) | §4B |
| Schrödinger uncertainty refinement | (not in Griffiths) | (absent) | §4B |
| Compatible observables, CSCO | §3.5, §4.3 | (absent) | §4C |
| Measurement & collapse postulate | §3.4 (briefly) | Ch. 7 (informally) | §4D |
| Major interpretations | (not in Griffiths) | Ch. 7 (selective) | §4D |
| Decoherence | (not in Griffiths) | (absent) | §4D |
| Frauchiger-Renner 2018 | (not in Griffiths) | (absent) | §4D |

## 7. Exercises

**1. (Bloom: Remember.)** State the five postulates of quantum mechanics in one sentence each. Identify which physical requirement each postulate enforces (e.g., "real outcomes" or "conserved probability").

**2. (Bloom: Understand.)** Prove that the eigenvalues of any Hermitian operator are real. Then prove that eigenvectors corresponding to distinct eigenvalues are orthogonal. (Both are two-line proofs; do them explicitly.)

**3. (Bloom: Apply.)** Compute $[\hat{x}, \hat{p}]$ from the operator definitions $\hat{x}\psi = x\psi$ and $\hat{p}\psi = -i\hbar\,\partial_x \psi$ by acting on an arbitrary test function $\psi(x)$. You should recover $[\hat{x}, \hat{p}]\psi = i\hbar\,\psi$ for all $\psi$, i.e., $[\hat{x}, \hat{p}] = i\hbar\,\hat{1}$.

**4. (Bloom: Apply.)** For the $n = 1$ infinite-square-well state $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$, compute $\sigma_x$ and $\sigma_p$ explicitly. Show that $\sigma_x \sigma_p > \hbar/2$, so the Robertson bound is satisfied but not saturated. (Compare to the worked example for the oscillator, where saturation occurs.)

**5. (Bloom: Apply.)** Use the ladder operators to compute $\sigma_x$ and $\sigma_p$ for the $n$-th harmonic-oscillator eigenstate, and show that $\sigma_x \sigma_p = (n + 1/2)\hbar$. Identify which states (if any) saturate the Robertson bound.

**6. (Bloom: Analyze.)** A beam of spin-1/2 particles is prepared in the state $|\uparrow_z\rangle$. It passes successively through three Stern–Gerlach magnets oriented along $z$, $x$, $z$. Using the postulates, compute the fraction of particles that emerge in each of the four possible measurement-sequence outcomes. (Hint: $|\uparrow_x\rangle = (|\uparrow_z\rangle + |\downarrow_z\rangle)/\sqrt{2}$.) Then explain why a third $z$-measurement gives 50/50 outcomes even though the original beam was pure $|\uparrow_z\rangle$.

**7. (Bloom: Evaluate.)** Read the pop-sci book's Chapter 2 introduction to the uncertainty principle (the balloon analogy). In 300–500 words: (a) state what the analogy gets right at the level of intuition, (b) identify the specific way it conflates preparation uncertainty with measurement-disturbance uncertainty, and (c) explain how the Robertson derivation in §4B supplies the correct framing. Reference Ozawa 2003 if you use the measurement-disturbance distinction.

**8. (Bloom: Synthesize / Evaluate.)** Pick one interpretation of quantum mechanics from §4D (Copenhagen, Many-Worlds, Bohmian, QBism, dynamical collapse, decoherence-as-mechanism). State, in your own words, what that interpretation says about the collapse postulate. Identify one empirical fact it explains naturally and one it handles awkwardly. Conclude with whether you find the interpretation compelling and why — name your reasons. (This is the companion-guide exercise: there is no right answer, only honest ones.)

## 8. What would change my mind

The Robertson derivation is a theorem; it does not have a "could be wrong" face. The interpretation of measurement is a different matter. Three empirical results would force major revision. **First**: a positive experimental signal of dynamical collapse (GRW/CSL-style spontaneous localization) at a parameter point distinguishable from standard QM. The current matter-wave and cantilever experiments have been tightening upper bounds without finding signal; a positive detection would move dynamical-collapse interpretations from "consistent possibility" to "the answer." **Second**: an experimental test of Frauchiger-Renner-style self-referential reasoning that decisively rules out a class of interpretations (currently the paradox is interpretation-dependent; a cleaner version that picks one resolution would matter). **Third**: a working derivation of the Born rule from the unitary postulates alone, without additional structure — this would remove the collapse postulate's special status by making it derivable rather than imposed. Decision-theoretic derivations within Many-Worlds (Deutsch 1999, Wallace 2010 [verify]) attempt this but remain contested. A clean, broadly accepted derivation would be a substantial revision of how this chapter is taught.

## 9. Still puzzling

1. **The measurement problem itself.** Bell's 1990 complaint is still live in 2026. The field has not produced a fundamental theory in which "measurement" follows from the dynamics rather than being inserted as a postulate. The interpretation literature offers candidates; none commands majority assent.

2. **The status of probability.** The Born rule is a postulate. In Many-Worlds, where all outcomes occur, what does $P(a_n) = |\langle a_n|\psi\rangle|^2$ mean operationally? Decision-theoretic arguments (Deutsch, Wallace) try to derive the Born rule from rational betting; critics dispute whether the derivation is circular. In Copenhagen the Born rule is operational; in Bohm it follows from quantum equilibrium; in QBism it is a Bayesian normative rule. The same equation supports very different ontological commitments.

3. **What "the wave function" is.** A physical thing (collapse models, Bohmian guidance field)? An informational object (QBism, ensemble interpretations)? A branching multiversal structure (Many-Worlds)? The math is the same; the metaphysical commitments are not. Working physicists move forward without choosing; the field has not figured out how to make the choice empirical.

4. **The dimensional special-case of "the apparatus."** Decoherence explains *why* macroscopic systems behave classically (off-diagonal coherences decay fast). It does not explain *which* diagonal outcome you actually see. Solving the measurement problem requires answering both — the decay *and* the selection. Decoherence answers half. The other half is where the interpretations live.

---

**Tags:** postulates, Born-rule, Robertson-uncertainty, balloon-analogy-correction, commutators, CSCO, measurement-problem, Copenhagen, Many-Worlds, QBism, collapse-models, decoherence, Frauchiger-Renner, Griffiths-Ch-3

*Draft for Nik's review. Voice-anchored against root style/. Honest about interpretation status — no interpretation endorsed; consensus refused where none exists. Flags: Schrödinger 1930 pagination, Erhart 2012 citation, Vilasini 2024 reply, Wallace/Deutsch decision-theory citations, Schlosshauer-Kofler-Zeilinger 2013 survey percentages all tagged `[verify]`.*
