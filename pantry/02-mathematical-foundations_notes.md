# Research Notes: Unit 02 — Mathematical Foundations

**Source:** TIKTOC.md Unit 2 entry (lines 238–244)
**Notes file:** 02-mathematical-foundations_notes.md
**Corresponding chapter:** chapters/02-mathematical-foundations.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 2: Mathematical Foundations
> - Complex numbers — ❌ external source needed
> - Linear algebra, vector spaces, inner products — ❌
> - Dirac notation — ❌
> - Operators, eigenvalues, eigenstates — ❌
> - Hermitian operators and observables — ❌

TIKTOC Part II Verdict: "Essentially absent. This book is not a math book and makes no pretense of being one. Any QM course needs a full mathematical foundations unit — this text contributes nothing to it."

This is the unit where the companion does its most original work. The pop-sci reference contributes zero. Every concept, derivation, and worked example must come from outside that book. Griffiths Ch. 3 ("Formalism") is the canonical undergraduate treatment; Shankar Ch. 1 is the gold standard for QM-specific linear algebra. Sakurai Ch. 1 is more rigorous (graduate) and should be flagged as further reading, not primary.

---

## A. Conceptual foundations

### 1. Why quantum mechanics needs complex numbers

The argument that QM requires complex amplitudes is not aesthetic — it is forced. Three constraints together cannot be satisfied by real-valued amplitudes:

1. The Born rule: the probability of detecting a particle in a region is the squared modulus of an amplitude, |ψ|². This must be real, non-negative, and integrate to 1.
2. Linearity / superposition: amplitudes add. The double-slit experiment shows ψ_total = ψ_1 + ψ_2 at the screen, and probability density is |ψ_1 + ψ_2|². The cross term 2Re(ψ_1* ψ_2) produces the interference fringes.
3. Time evolution that conserves probability: the operator U(t) that takes |ψ(0)⟩ → |ψ(t)⟩ must preserve ⟨ψ|ψ⟩.

If ψ were real, the cross term in (2) would be 2ψ_1 ψ_2, with no oscillation in any physical phase variable, and the observed double-slit fringes could not arise. The cross term must oscillate; that requires phase; phase requires e^{iφ}; e^{iφ} requires complex numbers.

The mathematical objects the student needs are: complex modulus |z| = √(z*z), complex conjugate (a+bi)* = a−bi, Euler's formula e^{iθ} = cos θ + i sin θ, and the fact that |e^{iθ}| = 1 for any real θ. The last is the foundation of why "global phase" is unobservable: multiplying ψ by e^{iα} for any real α leaves |ψ|² unchanged.

**Common misconception:** "Complex numbers are a mathematical trick that gets cleaned up at the end." They are not — they are essential. Stueckelberg (1960) showed that you can do QM with real numbers only if you allow infinitely many of them (effectively pairing each complex amplitude with a doubled real Hilbert space), which is just complex amplitudes with more notation. The Renou et al. (2021, *Nature* 600, 625–629) experiment provided an empirical test ruling out "real quantum mechanics" on a Bell-inequality basis. [verify Nature pagination — generally well-cited but always check.]

**Worked example:** Given ψ_1 = (1/√2)e^{ikx} and ψ_2 = (1/√2)e^{ik(x − d sin θ)} at a screen far from a double slit, compute |ψ_1 + ψ_2|² and recover the standard double-slit interference pattern cos²(kd sin θ / 2). The phase difference, not the real-amplitude addition, generates the fringes.

**Source:** Griffiths Ch. 1.2–1.4 for the wave function introduction; Shankar *Principles of Quantum Mechanics* (2nd ed., 1994) Ch. 1 §1.1–1.3 for complex vector spaces.

### 2. State space as a complex vector space

A quantum state is represented by a vector in a complex Hilbert space H. The student's prior knowledge of real vector spaces from linear algebra survives almost completely intact, with one universal substitution: complex scalars and a Hermitian (conjugate-bilinear) inner product. The structure:

- **Vectors:** elements |ψ⟩ ∈ H.
- **Scalar multiplication:** α|ψ⟩ for α ∈ ℂ.
- **Addition:** |ψ⟩ + |φ⟩ ∈ H. Closure under linear combinations is *superposition.*
- **Inner product:** ⟨φ|ψ⟩ ∈ ℂ, antilinear in the first slot and linear in the second (physicist convention), with ⟨φ|ψ⟩* = ⟨ψ|φ⟩.
- **Norm:** ‖ψ‖ = √(⟨ψ|ψ⟩).
- **Completeness:** every Cauchy sequence converges. (For finite-dimensional spaces — spin systems — this is automatic. For infinite-dimensional spaces — wave functions on the line — this requires care; the formal object is L²(ℝ), the space of square-integrable functions.)

The dimension of H depends on the physical system: 2 for a single spin-1/2, 3 for a spin-1, infinite (countable) for a particle in a box, infinite (uncountable) for a particle on the real line. The companion should make this concrete — show the student a 2D example before the infinite-dimensional case.

**Common misconception:** "Hilbert space is a fancy name for a special space." No — it is just a complex vector space with an inner product, complete with respect to the norm that inner product defines. For finite-dimensional systems it is ℂⁿ with the standard inner product. Most of an undergraduate course never needs more.

**Worked example:** In ℂ², write a general state as α|0⟩ + β|1⟩ with |α|² + |β|² = 1. Show that the global phase α → e^{iφ}α, β → e^{iφ}β leaves all expectation values unchanged. Show that the *relative* phase α → α, β → e^{iφ}β changes interference observables. This previews qubits and lays the groundwork for the Bloch sphere (Unit 5 or 7).

**Source:** Griffiths Ch. 3.1–3.2; Shankar Ch. 1 §1.1–1.6 (the cleanest treatment).

### 3. Dirac notation: kets, bras, inner products, outer products

The bra-ket notation is Dirac's 1939 invention (*Mathematical Proceedings of the Cambridge Philosophical Society* 35, 416–418, "A new notation for quantum mechanics"). It packages four operations the student will perform thousands of times:

- **Ket** |ψ⟩ — the state vector.
- **Bra** ⟨ψ| — the dual vector, the linear functional that maps |φ⟩ → ⟨ψ|φ⟩ ∈ ℂ. Concretely, the bra is the conjugate transpose of the ket: if |ψ⟩ is a column of components, ⟨ψ| is the row of complex conjugates.
- **Inner product** ⟨ψ|φ⟩ — a complex number, the overlap.
- **Outer product** |ψ⟩⟨φ| — an operator, mapping |χ⟩ → |ψ⟩⟨φ|χ⟩.

Two identities the student must internalize:

- **Completeness relation:** for an orthonormal basis {|n⟩}, ∑_n |n⟩⟨n| = 1̂ (the identity operator). Inserting this between any two operators is a *constant move* in QM calculations.
- **Resolution of the identity in position basis:** ∫dx |x⟩⟨x| = 1̂, with ⟨x|ψ⟩ = ψ(x). This is the bridge between abstract Dirac notation and concrete wave functions — the wave function *is* the position-basis component of the abstract state vector.

The student should leave this unit able to translate fluently in both directions:
- Given ψ(x), write the state as |ψ⟩ = ∫dx ψ(x)|x⟩.
- Given |ψ⟩, recover ψ(x) = ⟨x|ψ⟩.
- Translate ⟨φ|ψ⟩ as ∫dx φ*(x)ψ(x).
- Translate ⟨φ|Â|ψ⟩ as ∫dx φ*(x)(Âψ)(x).

**Common misconception:** "⟨x| is a normal vector with norm 1." It is not — the position kets |x⟩ are not normalizable; ⟨x|x'⟩ = δ(x − x'), a Dirac delta, not a Kronecker delta. They form a *continuous* basis. This is the first place the student will trip on the distinction between proper vectors in Hilbert space and rigged-Hilbert-space distributions. The companion should flag this early — Griffiths handles it in a footnote (Ch. 3.3) but the student usually needs more attention than a footnote.

**Worked example:** Given |ψ⟩ = (3/5)|0⟩ + (4i/5)|1⟩ in ℂ², compute (a) the norm, (b) the probability of measuring outcome "0", (c) the expectation value ⟨ψ|Ẑ|ψ⟩ where Ẑ = |0⟩⟨0| − |1⟩⟨1|, (d) the state after a "0" outcome. This is the cleanest finite-dimensional Dirac-notation drill problem and previews measurement (Unit 5).

**Sources:**
- Dirac, P. A. M. (1939). "A new notation for quantum mechanics." *Mathematical Proceedings of the Cambridge Philosophical Society* 35(3), 416–418.
- Griffiths Ch. 3.3 (Dirac notation introduction).
- Shankar Ch. 1 §1.6–1.7.

### 4. Operators, eigenvalue equations, and the spectral theorem

A linear operator Â on H maps |ψ⟩ → Â|ψ⟩ ∈ H, with Â(α|ψ⟩ + β|φ⟩) = αÂ|ψ⟩ + βÂ|φ⟩. The eigenvalue equation

Â|a⟩ = a|a⟩

picks out vectors |a⟩ that the operator leaves in the same direction, scaled by a complex number a. The set of all such a is the *spectrum* of Â.

For a finite-dimensional Hermitian operator (defined below), the *spectral theorem* states that:
1. All eigenvalues are real.
2. Eigenvectors corresponding to distinct eigenvalues are orthogonal.
3. The eigenvectors form an orthonormal basis of H.

Consequence: any state can be expanded as |ψ⟩ = ∑_n c_n |a_n⟩ where c_n = ⟨a_n|ψ⟩, and the operator decomposes as Â = ∑_n a_n |a_n⟩⟨a_n|. This decomposition is the entire computational engine of QM — measurement probabilities, expectation values, time evolution.

For infinite-dimensional spaces the theorem extends but requires care: continuous spectra (position, momentum, free-particle Hamiltonian) involve eigen-distributions rather than eigenvectors, and the "orthonormal basis" becomes "complete set of generalized eigenvectors" in the rigged-Hilbert-space sense.

**Common misconception:** "Every operator has eigenvectors that form a basis." False for non-normal operators. The spectral theorem is specific to normal operators (those commuting with their adjoint), of which Hermitian and unitary operators are special cases. The companion should state this explicitly even though every operator encountered in introductory QM happens to be normal.

**Worked example:** Diagonalize Ĥ = ε(|0⟩⟨1| + |1⟩⟨0|) for a two-state system (a two-level atom with off-diagonal coupling). Show the eigenvalues are ±ε with eigenvectors (1/√2)(|0⟩ ± |1⟩). This is the simplest matrix-mechanics problem and previews the harmonic oscillator and the ammonia molecule.

**Source:** Griffiths Ch. 3.2–3.3; Shankar Ch. 1 §1.8–1.10.

### 5. Hermitian operators and observables

An operator Â is *Hermitian* (or self-adjoint, in finite dimensions equivalent) if Â† = Â, where † denotes the conjugate transpose. In matrix form, Â_ji = Â_ij* — element (j,i) is the complex conjugate of element (i,j). The diagonal entries are therefore real.

The First Postulate of QM relevant here: **observables correspond to Hermitian operators.** The reason: a measurement returns a real number. By the spectral theorem, the possible outcomes of a measurement are the eigenvalues of the corresponding operator, and Hermiticity is exactly the condition that guarantees those eigenvalues are real.

Three Hermitian operators the student needs by the end of Unit 2:
- **Position** x̂, with x̂|x⟩ = x|x⟩ in the position representation acting as multiplication by x.
- **Momentum** p̂ = −iℏ d/dx in the position representation.
- **Hamiltonian** Ĥ = p̂²/2m + V(x̂), the energy operator.

The Hermiticity of p̂ = −iℏd/dx is non-trivial — it requires integration by parts and the assumption that ψ → 0 at ±∞ (so the boundary terms vanish). This is the first place the student encounters that "Hermiticity" depends on the *domain* of square-integrable functions, not just on the formal operator expression. Griffiths Ch. 3.2 (Example 3.1) does this calculation; the companion should reproduce it in detail.

**Common misconception:** "Hermitian operator = symmetric matrix." This is the single most common error in a first QM course. For *real* matrices, Hermitian and symmetric coincide. For *complex* matrices they do not. The matrix [[0, i], [−i, 0]] (Pauli σ_y) is Hermitian but *not* symmetric. The companion must catch this in the first worked example.

**Worked example: diagonalize σ_z.** The Pauli operator σ_z = [[1, 0], [0, −1]] is already diagonal in the standard basis with eigenvalues ±1 and eigenvectors |↑⟩ = (1,0)ᵀ, |↓⟩ = (0,1)ᵀ. This is the spin-1/2 measurement operator along the z-axis. Drill the student through the calculation explicitly so they can do σ_x and σ_y by themselves.

**Worked example: diagonalize σ_x.** σ_x = [[0, 1], [1, 0]]. Characteristic polynomial λ² − 1 = 0, eigenvalues ±1, eigenvectors |+⟩ = (1/√2)(1, 1)ᵀ, |−⟩ = (1/√2)(1, −1)ᵀ. These are the spin-x eigenstates — superpositions of |↑⟩ and |↓⟩.

**Worked example: diagonalize σ_y.** σ_y = [[0, −i], [i, 0]]. Eigenvalues ±1, eigenvectors (1/√2)(1, ±i)ᵀ. The complex components are essential — there is no real matrix that gives this spectrum in a basis-preserving way. This is the worked example where the student sees, concretely, why complex numbers are not optional.

**Source:** Griffiths Ch. 3.2 (Hermitian operators and observables); Sakurai *Modern Quantum Mechanics* Ch. 1.1–1.4 [advanced — flag as further reading].

---

## B. Domain examples and cases

### Case 1 — The spin-1/2 system as the smallest non-trivial Hilbert space

A single spin-1/2 (electron spin, qubit, NMR two-level system) is the entire mathematical foundations unit running in two dimensions. Every concept — vector, inner product, operator, eigenvalue, expectation, measurement — has a finite, computable analog. The companion should anchor as much of Unit 2 as possible in ℂ². The infinite-dimensional generalization (wave functions on a line) then becomes "everything you just did, with sums replaced by integrals and Kronecker deltas replaced by Dirac deltas."

### Case 2 — The polarization of a photon

Photon linear polarization is also a two-state system: horizontal and vertical, |H⟩ and |V⟩. Diagonal polarizations are superpositions: |D⟩ = (1/√2)(|H⟩ + |V⟩). Right-circular polarization is |R⟩ = (1/√2)(|H⟩ + i|V⟩) — here the complex coefficient is *not* a calculational artifact; it is the rotational chirality. Measuring a diagonal photon in the {|H⟩, |V⟩} basis gives H or V with probability 1/2 each — a clean physical realization of measurement collapse the student can build intuition around.

### Case 3 — The position and momentum bases as Fourier transforms of each other

The position-basis wave function ψ(x) = ⟨x|ψ⟩ and the momentum-basis wave function φ(p) = ⟨p|ψ⟩ are related by the Fourier transform:

φ(p) = (1/√(2πℏ)) ∫dx e^{−ipx/ℏ} ψ(x)

This is one of the central computational facts of QM. Griffiths Ch. 3.4 covers it; the companion should make the Dirac-notation derivation explicit: φ(p) = ⟨p|ψ⟩ = ⟨p|(∫dx |x⟩⟨x|)|ψ⟩ = ∫dx ⟨p|x⟩ ψ(x), with ⟨p|x⟩ = (1/√(2πℏ)) e^{−ipx/ℏ}.

### Failure case — Forgetting the conjugate

The most common student error in matrix-element computation: ⟨φ|Â|ψ⟩ computed by taking φ's components, multiplying by Â's matrix, and contracting with ψ — *without* conjugating φ's components. Numerically the answer is wrong; conceptually it produces a complex "expectation value" for an observable. The companion should give the student a worked example with both calculations side by side: the correct one yielding a real number, the incorrect one yielding a complex number, and label the bug.

---

## C. Connections and dependencies

**Prerequisites:** Linear algebra at the level of Strang *Introduction to Linear Algebra* Ch. 1–6 (vectors, matrices, eigenvalues over the real numbers). Single-variable calculus through partial differentiation and improper integrals. No prior complex analysis required — the companion teaches Euler's formula and complex conjugation in §A.1. Familiarity with the *idea* of a Fourier series helps but is not required.

**Unlocks:** Unit 3 (the Schrödinger equation acts on Hilbert space vectors; the Born rule is the squared-modulus map from amplitudes to probabilities). Unit 4 (one-dimensional problems use the position and momentum operators directly). Unit 5 (the formalism unit is *built on* Unit 2; the postulates are statements about Hermitian operators on Hilbert space). Unit 7 (angular momentum is operator algebra; spin-1/2 is the smallest example). Everything downstream.

**Adjacent unit connections:**
- Unit 1 → Unit 2: the historical experiments motivate the need for complex amplitudes (double-slit interference requires phase).
- Unit 2 → Unit 3: the Hamiltonian is the operator whose action governs time evolution; the SE is a statement about Hermitian operators acting on state vectors.
- Unit 2 → Unit 5: measurement postulate, expectation values, and Heisenberg uncertainty all live in operator language.
- Unit 2 → Unit 7: Pauli matrices introduced here become the spin-1/2 generators in Unit 7.

---

## D. Current state of the field

**Settled:** Linear algebra on complex Hilbert spaces is standard mathematics, well-defined since von Neumann (1932) *Mathematische Grundlagen der Quantenmechanik.* No genuine controversy in the formalism itself.

**Contested (philosophy of QM, not math):** Whether the state vector is *ontic* (the actual physical state) or *epistemic* (a representation of an observer's information) is contested. Pusey, Barrett, and Rudolph (2012, *Nature Physics* 8, 475–478, "On the reality of the quantum state") proved a theorem ruling out a broad class of purely epistemic interpretations, but the debate continues. For Unit 2 this is a flag for Unit 5; the math is the same either way.

**Key references:**
- von Neumann, J. (1932). *Mathematische Grundlagen der Quantenmechanik.* Springer. English translation: *Mathematical Foundations of Quantum Mechanics,* Princeton University Press, 1955. [The foundational rigorous treatment.]
- Dirac, P. A. M. (1930). *The Principles of Quantum Mechanics.* Oxford University Press. [Source of the notation.]
- Griffiths, *Introduction to Quantum Mechanics,* 3rd ed. (2018), Ch. 3.
- Shankar, R. (1994). *Principles of Quantum Mechanics,* 2nd ed. Plenum. [The best undergraduate linear-algebra-first treatment.]
- Sakurai, J. J. and Napolitano, J. (2017). *Modern Quantum Mechanics,* 3rd ed. Cambridge. Ch. 1. [Graduate-level rigor.]

**Recent developments (last 3 years):** Renou et al. (2021) *Nature* 600, 625–629, "Quantum theory based on real numbers can be experimentally falsified" — an experimental Bell-type test ruling out the hypothesis that "real-amplitude QM" reproduces all predictions. Confirms operationally what the formalism requires structurally. [verify Nature pagination.]

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **The conjugate transpose.** Students from a real linear algebra background routinely forget to conjugate when taking the dual. Repeated drilling on (M†)_ij = M_ji* is essential.
2. **Position-basis kets are not normalizable.** ⟨x|x⟩ = δ(0) = ∞. The student worries this is a problem. It is — for mathematical hygiene — but operationally one works with wave packets ⟨x|ψ⟩ that *are* square-integrable. The companion should defer rigorous discussion to a footnote and reassure the student that the formal machinery (rigged Hilbert space) works.
3. **The bra-as-row, ket-as-column confusion.** Students often write ⟨ψ|φ⟩ as a column-column product and get confused when it should be a complex number. Establishing the convention early — column ket, row bra, with conjugation on the bra entries — saves hours.
4. **The continuum-discrete jump.** Students comfortable with ℂ² struggle when ∑ becomes ∫ and δ_ij becomes δ(x − x'). The companion should make this transition gradual with a side-by-side correspondence table.

**Analogies that work:**
- "A vector in Hilbert space is a column of complex numbers, the way a vector in ℝ³ is a column of real numbers." Almost literally true in finite dimensions; students should not over-mystify.
- "The operator does to the vector what the matrix does to the column." Direct.

**Analogies that mislead:**
- "Hilbert space is the space of all possible quantum states." Not quite — it is the space of *normalizable* state vectors, up to a global phase, which is more precisely projective Hilbert space. Pedagogically the loose version is fine if it is corrected by the time the student reaches Unit 5.
- "The bra-ket is just a notational convenience." It is more than that — it encodes the duality between vectors and functionals in a way ordinary index notation does not. Don't let the student dismiss it.

**Exercises (Bloom's level):**
- **Knowledge:** State the Hermitian condition Â† = Â. Define the inner product. Write Euler's formula. (L1)
- **Comprehension:** Convert ⟨φ|Â|ψ⟩ from Dirac notation to a matrix-element calculation in a chosen basis. (L2)
- **Application:** Diagonalize the three Pauli matrices. Find the expectation value of σ_y in a generic |ψ⟩ ∈ ℂ². (L3)
- **Analysis:** Show that the commutator of two Hermitian operators is anti-Hermitian. Show that p̂ = −iℏ d/dx is Hermitian on the space of square-integrable functions vanishing at infinity. (L4)
- **Synthesis:** Construct the Hermitian conjugate of a product (ÂB̂)† = B̂†Â† and explain why the order reverses. (L6)
- **Evaluation:** Given an operator expressed in one basis, decide whether it is observable (Hermitian), evolution-generating (anti-Hermitian or unitary exponential of), or neither. (L5)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 3 ("Formalism") is the spine for this unit. Sections 3.1 (Hilbert space), 3.2 (observables), 3.3 (eigenfunctions of Hermitian operators), 3.4 (generalized statistical interpretation). Solution manual gives worked-out Pauli-matrix problems. (`822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt`, `993201189-Solution-Manual-Introduction-to-Quantum-Mechanics-3e-Griffiths.txt`.)
- **Liboff, *Introductory Quantum Mechanics*** — Ch. 3–4 cover operator algebra and Hermitian operators at a similar level to Griffiths; alternative pedagogical sequence. (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`.)
- **Pop-sci references** — contribute nothing to this unit. TIKTOC is explicit: ❌ across the board. Do not assign as reading for this unit; the student will be confused by the absence of any math.
- **`_lib_Penrose-Emperors-New-Mind.md`** — Penrose discusses Hilbert space and operators in his QM chapters; can be assigned as supplementary "view from above" reading, but the level is uneven.
- **`_lib_The-Blind-Spot.md`** — useful if the chapter wants to discuss the philosophical status of the state vector (ontic vs epistemic) as a sidebar.

**Out of scope for pantry:** *A First Book of Quantum Field Theory* (Lahiri & Pal) is too advanced — its operator algebra is QFT-flavored. Skip for Unit 2.

---

## G. Gaps and flags

- **FLAG:** The Pauli matrix conventions (σ_x, σ_y, σ_z order and signs) are universal but the spin-state labeling (|0⟩/|1⟩ vs |↑⟩/|↓⟩ vs |+⟩/|−⟩) varies by textbook. The companion should pick one convention and stick to it. Recommended: |↑⟩, |↓⟩ for spin-1/2; |0⟩, |1⟩ for qubits — clearly distinguish the two contexts.
- **FLAG:** Hermitian vs. self-adjoint distinction matters in infinite dimensions (Reed & Simon, *Methods of Modern Mathematical Physics,* Vol. 1) but is typically elided in undergraduate texts. The companion should mention it in a sidebar and refer the curious student to Griffiths Ch. 3 footnotes.
- **GAP:** Rigged Hilbert space (the formal home of position and momentum eigenvectors) is rarely covered in undergraduate QM. The companion should acknowledge the gap and recommend Ballentine *Quantum Mechanics: A Modern Development* (1998) Ch. 1 for the curious student.
- **GAP:** The relationship between the Dirac formalism and tensor-product structure (needed for entanglement in Unit 10) is not introduced in Unit 2. Flag forward: composite systems will require |ψ⟩_A ⊗ |φ⟩_B notation, which extends Unit 2 naturally.
- **FLAG:** Renou et al. (2021) result on real vs. complex QM — [verify Nature volume and page numbers] before publication. Published online December 2021, print January 2022; pagination should be checked.
- **GAP:** The Stone–von Neumann theorem (unitary equivalence of all representations of canonical commutation relations) is the deep theorem behind why the position and momentum representations are interchangeable. Out of scope for an undergraduate course but worth a footnote-level mention.
