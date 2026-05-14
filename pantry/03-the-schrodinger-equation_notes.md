# Research Notes: Unit 03 — The Schrödinger Equation

**Source:** TIKTOC.md Unit 3 entry (lines 245–249)
**Notes file:** 03-the-schrodinger-equation_notes.md
**Corresponding chapter:** chapters/03-the-schrodinger-equation.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 3: The Schrödinger Equation
> - Derivation and structure — ❌
> - Wave function interpretation and Born rule — ❌ (Ch. 12 names it; insufficient)
> - Normalization and probability current — ❌
> - Stationary states and time evolution — ❌

TIKTOC Part III Verdict: "The Schrödinger equation appears but is treated as a fact to be named rather than a tool to be used. The Hamiltonian operator is written without any explanation of what it means. Students will not be able to solve anything after reading this."

The companion's job in Unit 3: turn the named equation into a working tool. The student should leave able to (a) state the SE in both time-dependent and time-independent forms, (b) interpret ψ correctly via the Born rule, (c) check normalization and compute probability currents, (d) understand stationary states as the natural basis for time evolution, and (e) solve the free-particle SE and recognize the wave-packet difficulty that motivates Unit 4.

---

## A. Conceptual foundations

### 1. The Schrödinger equation is postulated, not derived

This is the single most important honesty move in Unit 3. Griffiths is explicit about it in §1.1 of *Introduction to Quantum Mechanics* (3rd ed., 2018): "Where did Schrödinger's equation come from? In a sense, it cannot be derived; it represents a radically new departure from classical physics." The companion should say this too — bluntly. What undergraduates often see (in pop-sci or in lecture-shortcut form) is a "derivation" from de Broglie's λ = h/p and Einstein's E = hν that looks compelling. It is a *plausibility argument*, not a derivation. It tells you what equation has the right limiting behavior; it does not tell you why nature uses *this* equation.

The plausibility argument runs like this. Take a plane wave with the de Broglie identifications:

ψ(x,t) = A e^{i(kx − ωt)}, with p = ℏk and E = ℏω.

Differentiate: ∂ψ/∂t = −iωψ = −(i/ℏ)Eψ, so iℏ ∂ψ/∂t = Eψ.
Differentiate twice in x: ∂²ψ/∂x² = −k²ψ = −(p²/ℏ²)ψ, so −(ℏ²/2m)∂²ψ/∂x² = (p²/2m)ψ.

For a free particle E = p²/2m, so

iℏ ∂ψ/∂t = −(ℏ²/2m) ∂²ψ/∂x²

generalizes (by writing E = p²/2m + V) to the time-dependent Schrödinger equation:

**iℏ ∂ψ/∂t = −(ℏ²/2m) ∂²ψ/∂x² + V(x,t) ψ**

This is consistent with de Broglie–Einstein and with classical mechanics in the limit. It is also linear (so superposition holds) and first-order in time (so the state at one instant determines the state at all later instants). Each of these features is a postulate built into the equation, not a consequence of the de Broglie relations.

Schrödinger himself published the equation in a four-paper series in *Annalen der Physik* in 1926: "Quantisierung als Eigenwertproblem" parts I–IV (vol. 79, pp. 361, 489; vol. 80, p. 437; vol. 81, p. 109). His route was different — he was looking for a wave equation whose eigenvalue spectrum reproduced the Bohr energy levels of hydrogen, motivated by Hamilton–Jacobi theory and de Broglie's matter waves.

**Common misconception:** "The Schrödinger equation comes from energy conservation E = K + V." The form of the kinetic term in the SE matches the *classical* expression p²/2m via the substitution p → −iℏ d/dx, but this substitution is the postulate, not a derivation from energy conservation. Classical energy conservation does not tell you that momentum is a differential operator.

**Worked example:** Verify that ψ(x,t) = A e^{i(kx − ωt)} with ω = ℏk²/2m solves the free-particle SE. Then verify that any linear combination of such plane waves also solves it (linearity). This is Griffiths §2.4 territory.

**Sources:**
- Schrödinger, E. (1926). "Quantisierung als Eigenwertproblem (I)." *Annalen der Physik* 79, 361–376. (And three further papers in the same year.)
- Griffiths Ch. 1.1–1.2.

### 2. The Born rule: |ψ|² as probability density

Max Born's 1926 paper "Zur Quantenmechanik der Stoßvorgänge" (*Zeitschrift für Physik* 37, 863–867 and 38, 803–827) introduced the probabilistic interpretation. ψ itself is not directly observable; |ψ(x,t)|² dx is the probability of finding the particle in the interval [x, x+dx] at time t. Born received the 1954 Nobel Prize specifically for this interpretation.

The probabilistic move was Born's own; Schrödinger initially resisted it, hoping ψ would be a real wave of matter that the particle "rode." Schrödinger's interpretation failed because (a) ψ is complex, and complex matter has no classical meaning, and (b) for many-particle systems ψ is a function on 3N-dimensional configuration space, not on 3-space — it cannot be a physical wave in real space.

For the Born rule to be consistent, three conditions must hold:
1. **Non-negativity:** |ψ|² ≥ 0 everywhere. (Automatic — it's a squared modulus.)
2. **Normalization:** ∫|ψ|² dx = 1. (Conservable — see below.)
3. **Conservation under time evolution:** if true at t=0, true at all later t.

The third condition is non-trivial and tied to the Hermiticity of the Hamiltonian. The proof: d/dt ∫|ψ|² dx = 0 follows from the SE if Ĥ is Hermitian. Griffiths §1.4 carries the calculation through; the companion should reproduce it because it is the single cleanest justification for the Hermiticity postulate.

**Common misconception:** "ψ *is* the particle." It is not. ψ is the probability amplitude. The particle, when detected, registers as a point in a detector. ψ tells you, before detection, what the probabilities are for where that point will appear. The "particle as a spread-out cloud" image is the cloud of *detection probabilities,* not the particle itself.

**Common misconception (subtler):** "|ψ|² is a hidden variable telling us what we don't know about a real position." No — the Bell-inequality experiments (Aspect 1982; the 2022 Nobel for Clauser, Aspect, Zeilinger) rule out local hidden-variable theories. The probability is irreducible, not a stand-in for incomplete knowledge.

**Worked example:** A particle in a box of length L has ground-state wave function ψ_1(x) = √(2/L) sin(πx/L). Compute the probability of finding the particle in [0, L/4]. (Answer: integrate |ψ_1|² over [0, L/4]; result is 1/4 − 1/(2π), about 9%.) This is Griffiths Ch. 2.2 problem 2.4 [verify problem number against edition].

**Sources:**
- Born, M. (1926). "Zur Quantenmechanik der Stoßvorgänge." *Zeitschrift für Physik* 37, 863–867.
- Born, M. (1926). "Quantenmechanik der Stoßvorgänge." *Zeitschrift für Physik* 38, 803–827.
- Griffiths Ch. 1.3 (statistical interpretation), Ch. 1.4 (normalization).

### 3. Normalization and probability conservation

A wave function ψ(x,t) is *normalizable* if ∫|ψ|² dx is finite, and *normalized* if the integral equals 1. Normalization is preserved under time evolution when Ĥ is Hermitian — this is not coincidence, it is the structural requirement that makes the Born rule consistent.

The proof (Griffiths §1.4): differentiate the integral under the integral sign, use the SE to replace ∂ψ/∂t by terms involving Ĥψ, and find:

d/dt ∫|ψ|² dx = (1/iℏ) ∫(ψ* Ĥψ − (Ĥψ)* ψ) dx = 0 when Ĥ† = Ĥ.

For the standard Hamiltonian Ĥ = −(ℏ²/2m) ∂²/∂x² + V(x), this reduces (after integration by parts) to the **probability current** identity:

j(x,t) = (ℏ/2mi)(ψ* ∂ψ/∂x − ψ ∂ψ*/∂x)

and the **continuity equation**:

∂ρ/∂t + ∂j/∂x = 0, where ρ = |ψ|².

This is the local statement of probability conservation: probability cannot vanish at one point and reappear elsewhere; it has to flow.

**Common misconception:** "Normalization is a technicality." It is the physical statement that the particle exists somewhere — total probability equals 1. Wave functions that cannot be normalized (plane waves, position eigenstates) are not physical states; they are calculational devices that must be assembled into wave packets to represent actual particles.

**Worked example: probability current for a plane wave.** For ψ(x,t) = A e^{i(kx − ωt)}, j = (ℏk/m)|A|² = (p/m)|A|² = v|A|². The current is density times velocity — exactly the classical expression for a flowing fluid. This is the worked example that gives the student physical intuition for what j means. Griffiths §1.5.

**Sources:** Griffiths Ch. 1.4 (normalization), Ch. 1.5 (momentum and probability current); Shankar Ch. 5 §5.3 (probability current).

### 4. Stationary states and time evolution

A *stationary state* is a state of the form

ψ(x,t) = ψ(x) e^{−iEt/ℏ}

where ψ(x) satisfies the time-independent Schrödinger equation:

**Ĥ ψ(x) = E ψ(x)**

— an eigenvalue equation for the Hamiltonian operator with eigenvalue E (the energy).

The name "stationary" refers to the fact that |ψ(x,t)|² = |ψ(x)|² is time-independent — the probability density does not change. Expectation values of any time-independent operator are also constant. This is the place where, if the student is not careful, they conclude that stationary states are "static." They are not. The phase e^{−iEt/ℏ} rotates in the complex plane at rate E/ℏ; the *spatial structure* of |ψ|² is what is static.

The deep significance: by the spectral theorem applied to Hermitian Ĥ, the energy eigenstates form a complete basis. *Any* state can be expanded as

ψ(x,t) = ∑_n c_n ψ_n(x) e^{−iE_n t/ℏ}

with c_n = ∫ψ_n*(x) ψ(x,0) dx. Time evolution becomes trivial in the energy basis: each term picks up its own phase factor. This is the *engine* of how time evolution is computed in practice. Griffiths Ch. 2.1 develops this systematically.

**Common misconception:** "Stationary states are static." No. The time-dependent phase matters for *superpositions.* Consider ψ(x,t) = (1/√2)[ψ_1(x)e^{−iE_1 t/ℏ} + ψ_2(x)e^{−iE_2 t/ℏ}]. Then |ψ|² = (1/2)[|ψ_1|² + |ψ_2|² + 2 Re(ψ_1* ψ_2 e^{−i(E_2 − E_1)t/ℏ})] — and the cross term oscillates at the Bohr frequency ω = (E_2 − E_1)/ℏ. This oscillation is *observable* in atomic transitions; it is the source of every spectral line in atomic physics.

**Common misconception:** "The energy E in the time-independent SE is a property of ψ." It is the eigenvalue of Ĥ corresponding to ψ — a property of the *pair* (Ĥ, ψ). A given spatial function is a stationary state only relative to a specific Hamiltonian.

**Worked example:** Show that the time-dependent SE applied to a stationary state ψ(x,t) = ψ(x) e^{−iEt/ℏ} reduces to Ĥψ(x) = Eψ(x). This is the derivation that justifies the time-independent SE — done by separation of variables in Griffiths §2.1.

**Worked example: Bohr oscillation.** Construct a 50-50 superposition of two energy eigenstates ψ_1 and ψ_2 with energies E_1 and E_2 in a particle-in-a-box. Compute ⟨x⟩(t) and show it oscillates at angular frequency (E_2 − E_1)/ℏ. This is the cleanest demonstration that "stationary" is a property of the components, not the superposition.

**Source:** Griffiths Ch. 2.1 (stationary states); Shankar Ch. 5 §5.1–5.2.

### 5. The free particle and the wave-packet problem

The free particle (V = 0) has time-independent SE

−(ℏ²/2m) d²ψ/dx² = E ψ

with general solutions ψ_k(x) = A e^{ikx} + B e^{−ikx} for k = √(2mE)/ℏ. These are not normalizable: ∫|e^{ikx}|² dx = ∫1 dx = ∞. Plane-wave momentum eigenstates are not physical states of a particle.

The resolution: physical states are *wave packets,* linear combinations of plane waves:

ψ(x,0) = (1/√(2π)) ∫ φ(k) e^{ikx} dk

where φ(k) is the momentum-amplitude function. If φ(k) is concentrated near some k_0, ψ(x,0) is a localized wave packet whose width in position is set by the width of φ in momentum — Heisenberg uncertainty in its sharpest form. Time evolution adds an e^{−iω(k)t} factor inside the integral with ω(k) = ℏk²/2m, and the wave packet spreads as it propagates because different k-components move at different group velocities.

This is the bridge to Unit 4. The companion should be explicit: free-particle plane waves cannot be normalized, so to talk about an actual particle we must build packets, and the spreading of those packets is one of the first quantitative consequences of QM the student computes.

**Common misconception:** "Plane waves are unphysical, so the formalism breaks." The formalism is fine — plane waves are *generalized* eigenfunctions in the rigged-Hilbert-space sense, and wave packets built from them are perfectly normalizable. The unphysicality is of the mathematical idealization, not the framework.

**Worked example: Gaussian wave packet.** ψ(x,0) = (1/(2πσ²)^{1/4}) exp(ik_0 x) exp(−x²/4σ²). Compute φ(k), compute ψ(x,t), show that the position-space width grows as σ(t) = σ √(1 + (ℏt/2mσ²)²). This is Griffiths Ch. 2.4 / problem 2.21 [verify].

**Sources:** Griffiths Ch. 2.4 (free particle); Shankar Ch. 5 §5.3, Ch. 8 (the propagator).

---

## B. Domain examples and cases

### Case 1 — The particle in a box (preview of Unit 4)

The infinite square well of width L is the simplest non-trivial system where the SE is solvable in closed form. Boundary conditions ψ(0) = ψ(L) = 0 quantize the allowed wavenumbers k_n = nπ/L, giving energies E_n = n²π²ℏ²/(2mL²). The full time-dependent solutions are ψ_n(x,t) = √(2/L) sin(nπx/L) e^{−iE_n t/ℏ}. Each is a stationary state; superpositions oscillate.

This belongs in Unit 4 fully, but Unit 3 should preview it as the proof of concept that the Schrödinger equation is computable. The student leaves Unit 3 with the SE postulated and the formalism in hand; Unit 4 then runs the solution machinery.

### Case 2 — The hydrogen atom energy levels (preview of Unit 6)

Schrödinger's original motivation for the equation was to reproduce the Bohr energy spectrum of hydrogen — E_n = −13.6 eV / n² — from a wave equation. The full derivation requires three-dimensional separation of variables and Laguerre polynomials (Unit 6 material). What the student should know in Unit 3: the time-independent SE for hydrogen has a discrete bound-state spectrum that matches the Balmer formula, and the matching was Schrödinger's empirical justification for the equation.

### Case 3 — Stationary states in atomic emission

Why don't atoms in their ground state radiate, even though electrons are accelerating? Classical electrodynamics predicts that an accelerating charge radiates and an atom should collapse in 10⁻¹¹ s. The QM answer: the ground state is a stationary state with time-independent |ψ|² — there is no oscillating charge distribution to radiate. Emission occurs only when the atom is in a *superposition* of two states with different energies, in which case the charge density |ψ|² oscillates at the Bohr frequency and the atom radiates a photon of energy ℏω = E_2 − E_1. This is one of the cleanest pedagogical payoffs of the stationary-state concept.

### Failure case — Schrödinger's matter-wave interpretation

Schrödinger initially proposed that |ψ|² was the *charge density* of a real wave — the electron was a smeared-out matter wave in space. This failed for two reasons. First, ψ is complex, and there is no classical notion of a complex matter density. Second, for two electrons ψ is a function of six coordinates (x_1, y_1, z_1, x_2, y_2, z_2), and a function on six-dimensional configuration space cannot be a physical wave in three-dimensional space. Born's probabilistic interpretation accommodated both — probabilities are real, and a probability distribution on configuration space is a perfectly sensible object.

The historical lesson is worth a paragraph in the chapter: Schrödinger had the right equation and the wrong interpretation, Born had the right interpretation, and the two together became standard within months.

---

## C. Connections and dependencies

**Prerequisites:** Unit 1 (the de Broglie and Einstein relations motivate the SE's form). Unit 2 (Hilbert space, Hermitian operators, eigenvalue equations) is essential — without it, the SE is "an equation"; with it, the SE is an eigenvalue problem in a vector space with a defined inner product. Partial differential equations through separation of variables and the heat equation. Fourier analysis (transform pairs, Parseval's theorem).

**Unlocks:** Unit 4 (every one-dimensional potential problem is the time-independent SE in a specific V). Unit 5 (the measurement postulate references the SE for time evolution between measurements). Unit 6 (the hydrogen atom is a 3D SE). Unit 9 (perturbation theory perturbs the Hamiltonian and watches the energy spectrum shift). Essentially every later chapter.

**Adjacent unit connections:**
- Unit 2 → Unit 3: the SE is iℏ ∂ψ/∂t = Ĥψ — a first-order linear differential equation on Hilbert space, generated by the Hermitian operator Ĥ. Without Unit 2 this is just a string of symbols.
- Unit 3 → Unit 4: stationary states ψ_n(x) for various potentials are the bread and butter of Unit 4. Particle-in-a-box, harmonic oscillator, hydrogen atom — each is a different V in the time-independent SE.
- Unit 3 → Unit 5: the SE provides time evolution *between* measurements; the measurement postulate provides the discontinuous update at the moment of measurement. The two together constitute the dynamical content of QM.

---

## D. Current state of the field

**Settled:** The SE is the empirically validated equation for non-relativistic quantum mechanics. Its predictions for atomic spectra, molecular structure, condensed matter physics, and quantum chemistry have been confirmed to absurd precision (the electron g-factor from QED, the SE's relativistic generalization, matches experiment to 12 significant figures).

**Contested (interpretations — preview of Unit 5):**
- **Copenhagen interpretation** (Bohr, Heisenberg): the wave function represents knowledge; collapse on measurement is fundamental.
- **Many-worlds interpretation** (Everett, 1957, *Reviews of Modern Physics* 29, 454–462, "Relative state formulation of quantum mechanics"): the wave function is real; no collapse; measurement is branching of the universal wave function.
- **Bohmian / pilot-wave interpretation** (de Broglie 1927, Bohm 1952): particles have definite positions guided by the wave function.
- **Spontaneous collapse** (GRW: Ghirardi, Rimini, Weber 1986): the SE is approximate; real dynamics includes a small nonlinear stochastic collapse term.

All four reproduce the standard predictions of QM to the precision that has been tested. They disagree about ontology. The companion's Unit 3 should not adjudicate — the student needs the formalism before they can evaluate interpretations. Flag forward to Unit 5.

**Key references:**
- Schrödinger, E. (1926). The four-paper *Annalen der Physik* series, vols. 79–81.
- Born, M. (1926). The two-paper *Zeitschrift für Physik* series, vols. 37–38.
- Griffiths, *Introduction to Quantum Mechanics,* 3rd ed. (2018), Ch. 1–2.
- Shankar, *Principles of Quantum Mechanics,* 2nd ed. (1994), Ch. 5.
- Cohen-Tannoudji, Diu, Laloë, *Quantum Mechanics,* Vol. 1, Ch. 1 [advanced reference].

**Recent developments (last 3 years):** Loophole-free Bell-test experiments (Hensen et al. 2015, *Nature* 526, 682–686; subsequent refinements 2022–2024) continue to rule out local hidden-variable completions of QM. The 2022 Nobel Prize to Aspect, Clauser, and Zeilinger formalized the experimental verdict. None of this changes the SE; all of it constrains its *interpretation.*

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **"Where does the SE come from?"** Students want a derivation and feel cheated by "it is postulated." The companion should acknowledge this directly and explain *why* a postulate is the right move epistemically — the equation's status is that of Newton's second law: a fundamental law tested by its consequences, not derived from anything more basic.

2. **The complex phase confusion.** Students try to interpret e^{−iEt/ℏ} as a "rotation in time" without understanding that it is rotation in the complex plane of the amplitude. Reframe: at each x, ψ(x,t) is a complex number; as t advances, that complex number rotates at angular frequency E/ℏ; the magnitude is fixed.

3. **Why stationary states matter.** Students initially think stationary states are uninteresting because nothing happens. The chapter must make explicit that *all* time evolution is computed by decomposing into stationary states. Stationary states are interesting because they are *easy* — and they form the basis in which every other state's evolution becomes trivial.

4. **The particle-vs-wave function distinction.** "Is the electron really a wave?" — the student's question. Answer: no, ψ is not the electron. The electron is what you detect. ψ is the probability amplitude whose squared modulus tells you the detection probability. Hold the distinction firmly and the student stops being confused about double-slit "which path" questions.

**Analogies that work:**
- "The wave function is like a weather forecast for where the particle will turn up." Imperfect (it omits phase and interference) but useful for the Born rule.
- "Stationary state = standing wave on a violin string." For bound-state spatial structure, this is genuinely illuminating. Each n is a different harmonic. Breaks down for the time evolution (the violin string vibrates; the QM stationary state has time-independent |ψ|²).

**Analogies that mislead:**
- "ψ is a wave traveling through space." Sometimes true (free particle), often misleading (bound states have no traveling-wave structure). Cut.
- "The particle smears out into a cloud." Reinforces the wrong ontology. ψ is amplitude; particles register as points.

**Exercises (Bloom's level):**
- **Knowledge:** Write the time-dependent and time-independent SE. State the Born rule. Define the probability current. (L1)
- **Application:** Verify that a given ψ is normalized. Compute the expectation value of x and p for a Gaussian wave packet. Compute the probability current for a plane wave. (L3)
- **Analysis:** Show that the SE preserves normalization, using the Hermiticity of Ĥ. Show that the time-independent SE is what you get from separation of variables in the time-dependent SE. (L4)
- **Synthesis:** Given two energy eigenstates of a particle in a box, construct the superposition and show that ⟨x⟩(t) oscillates at the Bohr frequency. (L6)
- **Evaluation:** Read Schrödinger's original 1926 statement of his matter-wave interpretation and explain why Born's probabilistic interpretation displaced it. (L5)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 1 (wave function, normalization, expectation values) and Ch. 2.1 + Ch. 2.4 (stationary states and the free particle). This is the spine of the unit. Solution manual covers Gaussian wave packet problems and probability current calculations. (`822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt`, `993201189-Solution-Manual-Introduction-to-Quantum-Mechanics-3e-Griffiths.txt`.)
- **Liboff, *Introductory Quantum Mechanics*** — Ch. 3 covers SE and Born rule with more pedagogical exposition; alternative pacing. (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`.)
- **Pop-sci references** — Ch. 12 names the SE and Ch. 5 mentions ψ² as probability density. TIKTOC marks both ⚠️. Assign Ch. 12 as a "see the equation" reading only; the companion provides the content.
- **`_lib_Davies-Demon-in-the-Machine.md`** — Davies discusses the SE and Born rule in his treatments of quantum biology; can supply illustrative case material if the chapter needs a non-atomic application.
- **`_lib_Penrose-Emperors-New-Mind.md`** — Penrose's Ch. 6 develops the SE for a general readership; some illustrative passages may be useful but his agenda (introducing his own gravity-induced-collapse views later) should be flagged.

**Out of scope:** Lahiri & Pal QFT text is the wrong framework — non-relativistic SE is the territory of the chapter, not the Dirac equation.

---

## G. Gaps and flags

- **FLAG:** Griffiths problem numbers shift between editions. The pantry text is 1st edition (1994); the 3rd edition (2018) renumbers some material. The chapter author should cross-check before citing specific problem numbers.
- **FLAG:** Schrödinger's 1926 paper citations are bibliographically clean (vol. 79 pp. 361, 489; vol. 80 p. 437; vol. 81 p. 109) but the English translation history is fragmented. The standard English collection is Schrödinger, *Collected Papers on Wave Mechanics* (Blackie & Son, 1928; reissued Chelsea/AMS). [verify page numbers for vol. 80 and vol. 81 from a primary source — most references give the leading page only.]
- **FLAG:** Born's 1954 Nobel Prize citation is correct but the timing — the work was 1926, the Nobel was 1954 — is worth noting in passing. The 28-year gap is unusual and partly explained by the controversy around the probabilistic interpretation in the 1920s and 1930s.
- **GAP:** The propagator formulation of time evolution (Feynman's path-integral picture) is the natural complement to the SE but is typically not in undergraduate texts. The companion should mention it as a "different but equivalent" formulation, citing Shankar Ch. 8 or Feynman & Hibbs *Quantum Mechanics and Path Integrals* (1965).
- **GAP:** Probability current for systems with a magnetic vector potential A includes an extra (e/m)A|ψ|² term. Out of scope for Unit 3 but the companion should flag it for the curious student — relevant later for the Aharonov–Bohm effect.
- **FLAG:** The Renou et al. 2021 *Nature* paper on real-vs-complex QM is relevant to *why* the SE has the complex i in front of ∂/∂t. Cross-reference with Unit 2 notes if the chapter wants to make the "why complex" argument quantitative.
- **GAP:** Decoherence as a partial answer to the measurement problem (Zurek 2003, *Reviews of Modern Physics* 75, 715–775) is the modern refinement of the Copenhagen-vs-many-worlds debate. Out of scope for Unit 3 but the Unit 5 chapter author should know it exists.
