# QM Course TOC — Diagnostic Map
**Reference text:** *Quantum Physics for Beginners* (2021, anonymous)
**Purpose:** Identify coverage gaps, teaching quality, and build/borrow decisions for course design

---

## Rating Key
- ✅ **Covered adequately** — conceptually present, usable as-is or with light supplement
- ⚠️ **Touched but weak** — topic appears but lacks depth, rigor, or accuracy for course use
- ❌ **Absent** — not covered; requires external source
- 🚫 **Actively misleading** — coverage present but contains errors or framing that would need correction

---

## PART I: Historical and Conceptual Foundations

| Topic | Book Coverage | Notes |
|---|---|---|
| Failures of classical physics | ⚠️ | Mentioned in passing; no systematic treatment of UV catastrophe, equipartition failure |
| Blackbody radiation and Planck's law | ✅ | Ch. 3 — conceptually solid, formula presented, Planck constant introduced correctly |
| Photoelectric effect | ✅ | Ch. 4 — history, Einstein's explanation, Nobel context covered; good for motivation |
| Compton scattering | ⚠️ | Ch. 10 — qualitative description adequate; Klein-Nishina formula named but not derived |
| Wave-particle duality | ⚠️ | Ch. 11 — historical framing good; double-slit described but interference math absent |
| de Broglie hypothesis | ✅ | Ch. 5 — formula λ=h/mv stated and numerically illustrated with electron example |
| Young's double-slit with electrons | ⚠️ | Ch. 11 — Jönsson, Tonomura experiments cited; no mathematical treatment |
| Franck-Hertz experiment | ✅ | Ch. 6 — unusually detailed for a pop-sci book; qualitative curve analysis solid |

**Part I Verdict:** Best section of the book. Historical narrative is coherent and accurate. Usable as motivational reading before you introduce formalism. No math, so students need a second source for everything quantitative.

---

## PART II: Mathematical Foundations

| Topic | Book Coverage | Notes |
|---|---|---|
| Complex numbers and functions | ❌ | Not mentioned |
| Linear algebra review (vectors, matrices) | ❌ | Not mentioned |
| Hilbert space and state vectors | ❌ | Not mentioned |
| Dirac bra-ket notation | ❌ | Not mentioned |
| Operators and eigenvalue equations | ❌ | Not mentioned |
| Hermitian operators | ❌ | Not mentioned |
| Commutators | ❌ | Not mentioned |
| Probability amplitudes and Born rule | ⚠️ | Born interpretation mentioned briefly in Ch. 2 (ψ² as probability density); no derivation |
| Fourier analysis and momentum representation | ❌ | Not mentioned |
| Expectation values | ❌ | Not mentioned |

**Part II Verdict:** Essentially absent. This book is not a math book and makes no pretense of being one. Any QM course needs a full mathematical foundations unit — this text contributes nothing to it.

---

## PART III: The Schrödinger Equation

| Topic | Book Coverage | Notes |
|---|---|---|
| Time-dependent Schrödinger equation | ⚠️ | Ch. 12 — equation written out; described as "wave equation" but not derived or analyzed |
| Time-independent Schrödinger equation | ⚠️ | Ch. 12 — mentioned; eigenvalue form H^ψ=Eψ stated without explanation of H^ |
| Wave function normalization | ❌ | Not covered |
| Probability density ψ² | ⚠️ | Ch. 5 — briefly introduced in context of atomic orbitals; not general |
| Stationary states | ❌ | Not covered |
| Superposition principle | ⚠️ | Implied in Ch. 7 (entanglement) and Ch. 16 (qubits); never stated as formal principle |
| Continuity conditions at boundaries | ❌ | Not covered |

**Part III Verdict:** The Schrödinger equation appears but is treated as a fact to be named rather than a tool to be used. The Hamiltonian operator is written without any explanation of what it means. Students will not be able to solve anything after reading this.

---

## PART IV: One-Dimensional Potential Problems

| Topic | Book Coverage | Notes |
|---|---|---|
| Infinite square well (particle in a box) | ❌ | Not covered |
| Finite square well | ❌ | Not covered |
| Quantum harmonic oscillator | ❌ | Not covered |
| Free particle / wave packets | ❌ | Not covered |
| Delta function potential | ❌ | Not covered |
| Step potential and reflection/transmission | ❌ | Not covered |
| Quantum tunneling | ✅ | Ch. 9 — best coverage in the book; qualitative mechanism solid; WKB not discussed but applications section is excellent |
| Transmission coefficient | ⚠️ | Defined qualitatively; formula not given |

**Part IV Verdict:** Quantum tunneling is the one bright spot — applications (STM, flash memory, fusion, Josephson junctions, radioactive decay) are listed with enough detail to motivate the topic. Everything else is absent.

---

## PART V: Quantum Formalism

| Topic | Book Coverage | Notes |
|---|---|---|
| Measurement postulate | ⚠️ | Discussed informally in Ch. 7 (Copenhagen interpretation); no formal statement |
| Collapse of the wave function | ⚠️ | Copenhagen interpretation mentioned; treated as philosophy rather than postulate |
| Heisenberg uncertainty principle | ⚠️ | Ch. 2 — conceptually framed but the balloon analogy is misleading; Robertson inequality absent |
| Generalized uncertainty principle | ❌ | Not covered |
| Complementarity | ⚠️ | Ch. 7 — described well in the entanglement context; not stated as a general principle |
| Time-energy uncertainty | ⚠️ | Ch. 2 — mentioned as "relativistic version"; not derived |
| Compatible observables / simultaneous measurements | ❌ | Not covered |
| No-cloning theorem | ❌ | Not covered |
| Density matrix / mixed states | ❌ | Not covered |

**Part V Verdict:** Weak. The uncertainty principle coverage has an error in framing — the balloon analogy for ΔE·Δt does not correctly represent the position-momentum version, and the two are conflated. This would need to be corrected explicitly in a course.

---

## PART VI: Atomic Structure

| Topic | Book Coverage | Notes |
|---|---|---|
| Bohr model of hydrogen | ✅ | Ch. 5 — energy levels, radius quantization, emission/absorption; well explained |
| Bohr model limitations | ✅ | Ch. 5 — multi-electron failure, Zeeman effect, spectral intensity; correctly identified |
| Quantum mechanical hydrogen atom | ⚠️ | Ch. 5 — orbital shapes shown; quantum numbers listed; no derivation |
| Quantum numbers (n, l, m, s) | ⚠️ | Ch. 5 — mentioned; spin quantum number introduced via Stern-Gerlach |
| Electron spin and Stern-Gerlach | ✅ | Ch. 5 — experiment described correctly; spin-up/down explained |
| Pauli exclusion principle | ⚠️ | Ch. 5 — stated; not derived from antisymmetry |
| Multi-electron atoms / electron configurations | ⚠️ | Ch. 13 (Periodic Table) — Pauli + quantum numbers used to explain periodic structure; qualitative only |
| Spectroscopic notation | ❌ | Not covered |
| Selection rules | ❌ | Not covered |
| Zeeman effect | ⚠️ | Mentioned as a failure of Bohr model; not explained |
| Fine structure / spin-orbit coupling | ❌ | Not covered |

**Part VI Verdict:** Bohr model coverage is the best pure-physics section in the book. Quantum mechanical atom is illustrated but not derived. Periodic table chapter is a surprising addition — connects quantum numbers to chemistry usefully.

---

## PART VII: Angular Momentum and Spin

| Topic | Book Coverage | Notes |
|---|---|---|
| Orbital angular momentum operators | ❌ | Not covered |
| Spherical harmonics | ❌ | Not covered |
| Spin-1/2 formalism | ⚠️ | Ch. 5 — spin states described verbally; Pauli matrices absent |
| Addition of angular momenta | ❌ | Not covered |
| Clebsch-Gordan coefficients | ❌ | Not covered |
| Spinors | ❌ | Not covered |
| Magnetic moment and spin | ⚠️ | Stern-Gerlach implies it; never stated quantitatively |

**Part VII Verdict:** Entirely absent at the level needed for a QM course.

---

## PART VIII: Identical Particles and Symmetry

| Topic | Book Coverage | Notes |
|---|---|---|
| Exchange symmetry | ❌ | Not covered |
| Symmetric / antisymmetric wave functions | ❌ | Not covered |
| Fermions and bosons | ⚠️ | Ch. 18 — mentioned in superfluids context (He-4 as composite boson); not developed |
| Slater determinants | ❌ | Not covered |
| Pauli exclusion from antisymmetry | ❌ | Not covered (Pauli principle stated but not derived) |

**Part VIII Verdict:** Absent.

---

## PART IX: Approximation Methods

| Topic | Book Coverage | Notes |
|---|---|---|
| Time-independent perturbation theory | ❌ | Not covered |
| Degenerate perturbation theory | ❌ | Not covered |
| Variational method | ❌ | Not covered |
| WKB approximation | ❌ | Not covered (tunneling chapter would be natural home for this) |
| Time-dependent perturbation theory | ❌ | Not covered |
| Fermi's Golden Rule | ❌ | Not covered |
| Sudden and adiabatic approximations | ❌ | Not covered |

**Part IX Verdict:** Entirely absent. This is arguably the most practically important section of any QM course and the book contributes nothing.

---

## PART X: Applications and Modern Topics

| Topic | Book Coverage | Notes |
|---|---|---|
| Quantum entanglement | ✅ | Ch. 7 — best conceptual chapter; EPR, Bell's theorem, GHZ all covered; accurate |
| Bell's theorem and non-locality | ✅ | Ch. 2 and Ch. 7 — Aspect experiment cited; Bell's theorem explained qualitatively |
| Many-worlds interpretation | ⚠️ | Ch. 7 — mentioned in entangled histories context; not critically evaluated |
| Lasers and stimulated emission | ✅ | Ch. 14 — thorough; 3-level/4-level systems, types, applications; best applications chapter |
| Semiconductors and band theory | ⚠️ | Ch. 4 — valence/conduction bands explained in photoelectric context; no k-space or Bloch theorem |
| LEDs | ⚠️ | Ch. 15 — conceptually correct; p-n junction physics assumed; no detail |
| Quantum computing | ⚠️ | Ch. 16 — qubits, superposition, entanglement correctly described; no gates, circuits, or algorithms |
| Superconductivity | ⚠️ | Ch. 17 — good historical narrative; BCS theory named; Cooper pairs mentioned; no math |
| Superfluids | ⚠️ | Ch. 18 — He-4 superfluidity, Meissner effect analogy; qualitative only |
| Quantum dots | ⚠️ | Ch. 19 — size-dependent optical properties explained; medical applications detailed |
| MRI | ⚠️ | Ch. 20 — mechanism explained at clinical level; no NMR physics or Larmor precession |
| Quantum tunneling applications | ✅ | Ch. 9 — STM, tunnel diodes, flash memory, nuclear fusion, radioactive decay; excellent catalog |
| Particle creation/annihilation | ⚠️ | Ch. 8 — electron-positron pair described; Higgs boson mentioned; clearly QFT not QM |
| Blackbody / thermal radiation applications | ❌ | Not covered beyond the basic spectrum |
| Quantum cryptography | ⚠️ | Ch. 16 — quantum encryption mentioned briefly in computing context |

**Part X Verdict:** Mixed. Entanglement and lasers are genuinely good chapters. Quantum computing is well-motivated but has no technical content. The applications catalog for tunneling is excellent for motivating the topic. MRI and superconductivity are at a science-literacy level, not a physics level.

---

## Summary Assessment

### Where this book is useful for course design

| Use | Chapters | Quality |
|---|---|---|
| Motivational reading before wave mechanics | Ch. 3, 4, 6, 11 | Good narrative, accurate history |
| Intuition for tunneling before WKB | Ch. 9 | Applications list is excellent |
| Conceptual entanglement introduction | Ch. 7 | Accurate; better than many textbooks |
| Lasers as QM application | Ch. 14 | Thorough; good for applied unit |
| Bohr model introduction | Ch. 5 (first half) | Clear and correct |
| Connecting QM to periodic table | Ch. 13 | Unusual; useful if you cover many-electron atoms |

### Where this book cannot be used

Every topic requiring:
- Mathematical derivation
- Operator algebra
- Exact solutions (square well, harmonic oscillator, hydrogen)
- Approximation methods
- Spin formalism beyond verbal description
- Angular momentum theory
- Symmetry arguments

This is roughly 70% of a standard QM course.

### Errors and framings to correct if you assign this
1. **Balloon analogy for uncertainty** (Ch. 2): conflates position-momentum and energy-time uncertainty in a way that misleads about the physics
2. **Faster-than-light framing of entanglement** (Ch. 2): the book raises this as a problem and then half-resolves it; students may leave thinking FTL signaling is real
3. **Particle-antiparticle annihilation** (Ch. 8): this is QFT content presented without that context; it does not belong in a QM course unless you label it explicitly
4. **"Observer creates reality"** (Ch. 2, Copenhagen): treated as a literal claim rather than an interpretation; needs nuance

---

## Recommended Course TOC (with source gap map)

The following is a full QM course TOC. Entries marked **[BOOK]** can use this text as supplementary reading. All others require a primary textbook (Griffiths, Sakurai, or equivalent).

### Unit 1: Why Quantum Mechanics?
- Classical physics and its failures **[BOOK: Ch. 3, 11]**
- Blackbody radiation **[BOOK: Ch. 3]**
- Photoelectric effect **[BOOK: Ch. 4]**
- Compton scattering **[BOOK: Ch. 10]**
- de Broglie waves and wave-particle duality **[BOOK: Ch. 5, 11]**
- Franck-Hertz experiment **[BOOK: Ch. 6]**

### Unit 2: Mathematical Foundations
- Complex numbers — ❌ external source needed
- Linear algebra, vector spaces, inner products — ❌
- Dirac notation — ❌
- Operators, eigenvalues, eigenstates — ❌
- Hermitian operators and observables — ❌

### Unit 3: The Schrödinger Equation
- Derivation and structure — ❌
- Wave function interpretation and Born rule — ❌ (Ch. 12 names it; insufficient)
- Normalization and probability current — ❌
- Stationary states and time evolution — ❌

### Unit 4: One-Dimensional Problems
- Particle in a box — ❌
- Harmonic oscillator — ❌
- Finite well and bound states — ❌
- Tunneling and the WKB approximation — **[BOOK: Ch. 9 for motivation and applications]**

### Unit 5: Quantum Formalism
- Postulates of QM — ❌
- Uncertainty principle (rigorous) — **[BOOK: Ch. 2 for intuition only; correct the balloon analogy]**
- Compatible observables and commutators — ❌
- Measurement and collapse — ❌

### Unit 6: The Hydrogen Atom
- Central potential and separation of variables — ❌
- Bohr model as limiting case **[BOOK: Ch. 5 first half]**
- Quantum numbers and orbitals **[BOOK: Ch. 5 second half — orbital pictures only]**
- Spin and Stern-Gerlach **[BOOK: Ch. 5]**
- Pauli exclusion principle **[BOOK: Ch. 5 — verbal statement only]**

### Unit 7: Angular Momentum
- Orbital angular momentum operators — ❌
- Spherical harmonics — ❌
- Spin-1/2, Pauli matrices — ❌
- Addition of angular momenta — ❌

### Unit 8: Identical Particles
- Exchange symmetry — ❌
- Bosons and fermions — ❌ (Ch. 18 touches this; insufficient)
- Many-electron atoms and periodic table **[BOOK: Ch. 13 for narrative; Pauli connection]**

### Unit 9: Approximation Methods
- Time-independent perturbation theory — ❌
- Variational principle — ❌
- WKB approximation — ❌
- Time-dependent perturbation theory — ❌
- Fermi's Golden Rule — ❌

### Unit 10: Quantum Mechanics in the Modern World
- Entanglement, Bell's theorem, EPR **[BOOK: Ch. 7 — strong; use directly]**
- Lasers and stimulated emission **[BOOK: Ch. 14 — use directly]**
- Semiconductors and band theory — ❌ (Ch. 4 provides motivation only)
- Quantum computing: motivation and qubits **[BOOK: Ch. 16 — for motivation only]**
- Superconductivity: overview **[BOOK: Ch. 17 — historical narrative is good]**
- Tunneling applications: STM, flash, biology **[BOOK: Ch. 9 — excellent]**

---

## Bottom Line

This book covers approximately **30% of a standard QM course**, and that 30% is almost entirely the historical foundations and applications layer. It has zero mathematical content suitable for a course. It should not be the primary text for anything — but it is a well-written motivational supplement for Units 1, 4, 6, and 10, and the entanglement chapter (Ch. 7) is genuinely good enough to assign as a conceptual reading before you develop the formalism.

If you're building a course, use this as "why does this matter" reading. Griffiths or Shankar carries the course.
