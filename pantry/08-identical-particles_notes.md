# Research Notes: Unit 08 — Identical Particles

**Source:** TIKTOC.md Unit 8 entry (lines 276–279), Part VIII diagnostic (lines 138–148)
**Notes file:** 08-identical-particles_notes.md
**Corresponding chapter:** chapters/08-identical-particles.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 8: Identical Particles
> - Exchange symmetry — ❌
> - Bosons and fermions — ❌ (Ch. 18 touches this; insufficient)
> - Many-electron atoms and periodic table **[BOOK: Ch. 13 for narrative; Pauli connection]**

TIKTOC Part VIII Verdict: "Absent." The pop-sci book mentions bosons and fermions only in the superfluid context (Ch. 18), and states the Pauli principle in Ch. 5 without deriving it from antisymmetry. The companion's job in Unit 8 is therefore total: introduce the exchange operator, prove (within standard QM) that its eigenvalues are ±1, postulate the connection to spin (the full proof requires QFT), construct the Slater determinant, and explain why the periodic table looks the way it does. The Ch. 13 periodic-table narrative is the one reusable piece — assign it as motivational reading and add the antisymmetry derivation underneath.

---

## A. Conceptual foundations

### 1. Indistinguishability and the exchange operator

In classical mechanics, two identical billiard balls are still distinguishable by their trajectories — you can label one "ball 1" at time t = 0 and follow its worldline forward. In quantum mechanics that move is no longer available. The wave function ψ(r₁, r₂) spreads each particle over a region; the regions overlap; and there is no physical procedure that can tell you, when a detector clicks, which of the two indistinguishable particles registered. Indistinguishability is not a confession of experimental ignorance — it is a statement about which observables exist.

Define the exchange operator P̂₁₂ on the two-particle Hilbert space by

P̂₁₂ ψ(r₁, r₂) = ψ(r₂, r₁).

Two facts follow immediately. First, P̂₁₂² = 1 (swap twice and you are back where you started), so the eigenvalues of P̂₁₂ are ±1. Second, if the two particles are genuinely identical, the Hamiltonian must be invariant under their exchange, [Ĥ, P̂₁₂] = 0, so eigenstates of Ĥ can be chosen as eigenstates of P̂₁₂ — that is, as either symmetric (+1) or antisymmetric (−1) under exchange. Nature, as far as we have measured in 3+1 dimensions, picks one of these two options per particle species and sticks with it.

The companion should be explicit that the symmetric/antisymmetric dichotomy is *imposed* in non-relativistic QM, not derived. Griffiths states this clearly in Ch. 5.1: "It is a fact that all the particles known to nature fall into one of two categories." The deeper derivation — the spin-statistics theorem, which forces integer-spin particles to be symmetric (bosons) and half-integer-spin particles to be antisymmetric (fermions) — requires quantum field theory and the relativistic requirement that operators at spacelike separation commute (for integer spin) or anticommute (for half-integer spin). Pauli proved this in 1940. The undergraduate QM student should know that the theorem exists, that it requires QFT, and that within their current toolkit it is a postulate.

In 2D, the story breaks. The two-particle exchange can wind around the relative-position singularity in topologically distinct ways, so the exchange phase is not restricted to ±1. The resulting particles — *anyons* — have been observed experimentally in the fractional quantum Hall effect and are the substrate for topological quantum computation. The companion should mention this as a one-paragraph aside that *our* postulate is dimension-specific.

**Common misconception:** "Identical particles are identical because they look the same." More precise: identical particles are identical because the Hamiltonian is exchange-symmetric *and* the wave function is symmetric or antisymmetric under exchange. Two electrons in distant atoms are still formally identical — the wave function is still antisymmetric across the labels. The reason exchange effects are negligible in distant atoms is that the overlap integral is tiny, not that the symmetry stops applying.

**Worked example:** Take two non-interacting spin-1/2 particles in a one-dimensional infinite well of width L. Construct the symmetric and antisymmetric two-particle spatial wave functions from the single-particle eigenstates ψ_n(x) = √(2/L) sin(nπx/L). Show that for n = m, the antisymmetric combination ψ_n(x₁)ψ_n(x₂) − ψ_n(x₂)ψ_n(x₁) = 0 — Pauli exclusion falls out of antisymmetry by construction. Griffiths Ch. 5 problem set.

**Sources:**
- Griffiths, D. J. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 5.1, "Two-Particle Systems."
- Pauli, W. (1940). "The Connection Between Spin and Statistics." *Physical Review* 58, 716–722. [The original spin-statistics theorem.]
- Leinaas, J. M. and Myrheim, J. (1977). "On the Theory of Identical Particles." *Il Nuovo Cimento B* 37, 1–23. [First treatment of anyons in 2D.]

### 2. Bosons, fermions, and the spin-statistics connection

Particles whose multi-particle wave function is symmetric under exchange are *bosons*; particles whose wave function is antisymmetric are *fermions*. The empirical correlation — observed in every experiment and proved in QFT — is that integer-spin particles are bosons and half-integer-spin particles are fermions. Photons (spin 1), gluons (spin 1), W and Z (spin 1), Higgs (spin 0), and composite particles like helium-4 atoms (two electrons + two protons + two neutrons = even number of fermions) are bosons. Electrons (spin 1/2), protons (spin 1/2), neutrons (spin 1/2), neutrinos (spin 1/2), and composite particles like helium-3 (odd number of fermions) are fermions.

The statistics that follow are different in kind. For N bosons in single-particle states with occupation numbers {n_i}, the multi-particle state is the symmetrized tensor product, and the equilibrium occupation at temperature T is Bose–Einstein,

⟨n_i⟩_BE = 1 / (e^((E_i − μ)/kT) − 1).

For N fermions, the antisymmetrized state has at most one particle per single-particle state (Pauli), and the occupation is Fermi–Dirac,

⟨n_i⟩_FD = 1 / (e^((E_i − μ)/kT) + 1).

The sign in the denominator is the entire story. At low temperature and high density, bosons crowd into the ground state (Bose–Einstein condensation, observed in dilute alkali gases by Cornell and Wieman 1995 *Science*, and Ketterle 1995 *Physical Review Letters*; Nobel 2001). Fermions stack into the lowest available states up to the Fermi energy — electron degeneracy pressure supports white dwarfs (Chandrasekhar 1931 *Astrophysical Journal* 74, 81–82, "The Maximum Mass of Ideal White Dwarfs"), neutron degeneracy pressure supports neutron stars.

**Common misconception:** "Bosons attract, fermions repel." There is no statistical *force* in the ordinary sense — no term in the Hamiltonian that couples to particle identity. What there is, is a correlation in the joint probability density |ψ(r₁, r₂)|² that emerges from the (anti)symmetrization. For two identical fermions in symmetric spin states, the spatial wave function must be antisymmetric, so |ψ(r₁, r₂)|² → 0 as r₁ → r₂ — the particles avoid coincidence. For two identical bosons, the symmetric spatial wave function enhances coincidence. The companion should call this an *exchange correlation*, not an exchange force. The distinction matters because students who think "fermions push each other apart" will be unable to do the helium calculation (Section A.5) correctly.

**Worked example:** Compute ⟨(x₁ − x₂)²⟩ for two identical bosons and two identical fermions in adjacent infinite-well levels (n = 1 and n = 2), spatial-only. Show that ⟨(x₁ − x₂)²⟩_fermion > ⟨(x₁ − x₂)²⟩_distinguishable > ⟨(x₁ − x₂)²⟩_boson, with no interaction. The bosons "pull together," the fermions "push apart" — without any potential. Griffiths Ch. 5.1.2 walks the calculation.

**Sources:**
- Chandrasekhar, S. (1931). "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal* 74, 81–82.
- Anderson, M. H., Ensher, J. R., Matthews, M. R., Wieman, C. E., and Cornell, E. A. (1995). "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science* 269(5221), 198–201.
- Davis, K. B., Mewes, M.-O., Andrews, M. R., van Druten, N. J., Durfee, D. S., Kurn, D. M., and Ketterle, W. (1995). "Bose-Einstein Condensation in a Gas of Sodium Atoms." *Physical Review Letters* 75(22), 3969–3973.

### 3. The Slater determinant

For N identical fermions, the antisymmetric multi-particle wave function is the Slater determinant — the determinant of an N×N matrix whose entries are single-particle orbitals evaluated at single-particle coordinates:

ψ(1, 2, ..., N) = (1/√N!) det[ φ_i(j) ]

where φ_i is the i-th single-particle orbital and j labels the particle coordinate (including spin). For N = 2:

ψ(1, 2) = (1/√2) [ φ_a(1)φ_b(2) − φ_a(2)φ_b(1) ]

Slater introduced the construction in 1929 (*Physical Review* 34, 1293–1322, "The Theory of Complex Spectra") to handle multi-electron atomic spectra systematically. The determinant has two pedagogical virtues. First, antisymmetry is built into the structure — swap two particle labels (two columns) and the determinant flips sign. Second, if two orbitals are identical (two rows the same), the determinant is zero — Pauli exclusion as a property of determinants.

The companion should derive Pauli exclusion this way rather than stating it. The Bohr-era statement "no two electrons can have the same four quantum numbers" is a *consequence* of antisymmetry, not a postulate. Students who learn Pauli as a rule about quantum numbers carry that misconception into solid-state physics, where the "quantum numbers" are band indices and crystal momenta — and they need to recover the deeper reason then anyway. Cleaner to deliver it once, correctly, in Unit 8.

**Common misconception:** "The Slater determinant is just a notational trick for keeping track of antisymmetry." It is more than that — it is the *minimal* antisymmetric construction from product states, and it underlies the Hartree–Fock approximation, the workhorse of computational quantum chemistry. The Hartree–Fock approximation is exactly "assume the N-electron ground state is a single Slater determinant, then minimize ⟨ψ|Ĥ|ψ⟩ over the orbitals." Everything beyond that — configuration interaction, coupled cluster, DFT — is a correction to the single-determinant ansatz.

**Worked example:** Construct the Slater determinant for the ground state of lithium (1s² 2s¹). Three electrons in three spin-orbitals: 1s↑, 1s↓, 2s↑ (or 2s↓ — degenerate). Write out the 3×3 determinant explicitly, expand it, and verify antisymmetry under any pair exchange. This is the calculation that motivates the Hartree–Fock orbitals computed in any quantum-chemistry course.

**Sources:**
- Slater, J. C. (1929). "The Theory of Complex Spectra." *Physical Review* 34, 1293–1322.
- Griffiths Ch. 5.2 (multi-electron atoms and the periodic table).
- Szabo, A. and Ostlund, N. S. (1996). *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory.* Dover. [Standard reference for Hartree–Fock from a Slater-determinant starting point.]

### 4. Helium, exchange integrals, and singlet-triplet splitting

The two-electron helium atom is the simplest non-trivial multi-fermion problem and the cleanest place to see exchange effects produce a real, measurable energy splitting. The total electron wave function is the product of a spatial part and a spin part. For two spin-1/2 particles, the spin states decompose into a spin-singlet (antisymmetric, total spin S = 0) and a spin-triplet (symmetric, total spin S = 1). To make the total wave function antisymmetric:

- Spin singlet (antisym) ⊗ Spatial symmetric → parahelium.
- Spin triplet (sym) ⊗ Spatial antisymmetric → orthohelium.

The two cases give different expectation values of the electron-electron repulsion e²/(4πε₀|r₁ − r₂|), because the spatial wave function controls how often the electrons sit close to each other. The first-order correction splits into a *direct* (Coulomb) term J and an *exchange* term K:

⟨V⟩_para = J + K (singlet, lower spatial symmetry, electrons can coincide → larger ⟨1/r₁₂⟩ — *wait, check sign convention; Griffiths § 5.2.1*).

[verify sign convention against Griffiths 3rd ed. — the result is that for excited configurations like 1s2s, the triplet (orthohelium) lies *lower* in energy than the singlet (parahelium), because the antisymmetric spatial wave function keeps the electrons apart and reduces Coulomb repulsion. This is the empirical fact — measured spectroscopically — and Hund's rule generalizes it: for a given configuration, higher total spin lies lower in energy.]

The companion should walk this calculation explicitly. The exchange integral

K = ∫∫ φ_a*(r₁)φ_b*(r₂) [e²/(4πε₀ r₁₂)] φ_a(r₂)φ_b(r₁) dr₁ dr₂

has no classical analog. It arises purely from the antisymmetrization. Working through K for the 1s2s configuration of helium is one of the cleanest demonstrations in the curriculum that an apparently abstract symmetry requirement (antisymmetry of fermions) produces a measurable energy ordering (Hund's rule, ortho-para splitting, ferromagnetism in the right limit).

**Common misconception:** "Hund's rule says parallel spins repel less." The opposite: parallel spins force the spatial wave function to be antisymmetric, which keeps the electrons apart, which reduces the Coulomb repulsion. The spins themselves do not interact (at this order); the exchange effect is purely a Pauli consequence operating through the Coulomb energy.

**Worked example:** Compute the first-order Coulomb correction for helium 1s² ground state — gives ionization energy ≈ 74.8 eV vs. experimental 79.0 eV. Then run the variational calculation (Unit 9!) with effective Z as the variational parameter to get ≈ 77.5 eV. The companion can use this as a forward-reference: "We will do better in Unit 9 with a variational principle." Griffiths Ch. 7 actually places the helium variational calculation in the variational-methods chapter, which is pedagogically right — the helium ground state is too hard for first-order perturbation alone.

**Sources:**
- Griffiths Ch. 5.2.1 (helium); Ch. 7.2 (variational calculation of helium ground state).
- Hund, F. (1925). "Zur Deutung verwickelter Spektren, insbesondere der Elemente Scandium bis Nickel." *Zeitschrift für Physik* 33, 345–371. [Original statement of Hund's rules.]

### 5. The periodic table as antisymmetry + Coulomb

The architecture of the periodic table — why noble gases are inert, why alkali metals are reactive, why the d-block sits where it sits — falls out of three ingredients: the hydrogenic energy ordering (modified by screening), the Pauli principle from antisymmetry, and Hund's rule from exchange. The Aufbau ("building-up") principle is the recipe: fill orbitals in order of increasing energy, respecting Pauli (at most two electrons per spatial orbital, opposite spins), with Hund's rule resolving ties (parallel spins fill distinct m_ℓ before pairing).

The Madelung rule (n + ℓ ordering, lowest first; for equal n + ℓ, lowest n first) gives the empirical filling order: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p. Madelung published this in 1936 (Klechkovskii independently in 1962); the rule is not exact — chromium (3d⁵4s¹ instead of 3d⁴4s²) and copper (3d¹⁰4s¹ instead of 3d⁹4s²) are the classic exceptions, where half-filled and fully-filled d-shell stability outweighs the 4s/3d energy gap. There are roughly twenty such exceptions across the table, mostly in the d- and f-blocks where orbital energies become near-degenerate.

The pop-sci book Ch. 13 gives a clean narrative of this. The companion adds the antisymmetry derivation underneath and shows where the rule breaks. The intellectual move worth making explicit: chemistry is the low-energy effective theory of atoms whose ground states are dictated by fermionic antisymmetry plus Coulomb. Without antisymmetry, every electron would crash into the 1s orbital and there would be no chemistry at all — just N copies of helium-like systems with increasing nuclear charge.

**Common misconception:** "Madelung's rule is exact." It is not — it is a good first-order rule built on the average energy ordering of hydrogenic-like orbitals with screening. The exceptions are real physics (relativistic effects in the heaviest elements; the lanthanide and actinide contractions; the 4s/3d quasi-degeneracy) and worth naming rather than glossing.

**Worked example:** Predict the ground-state electron configuration of carbon (Z = 6). Aufbau fills 1s² 2s² 2p². Hund's rule places the two 2p electrons in different m_ℓ orbitals with parallel spins — total S = 1, total L = 1, term symbol ³P. Verify against the NIST atomic spectra database [https://www.nist.gov/pml/atomic-spectra-database].

**Sources:**
- Madelung, E. (1936). *Die mathematischen Hilfsmittel des Physikers*. Berlin: Springer. [Original Madelung rule.]
- NIST Atomic Spectra Database [https://www.nist.gov/pml/atomic-spectra-database] — primary source for ground-state configurations and term symbols of all elements.
- Griffiths Ch. 5.2.2 (the periodic table).

---

## B. Domain examples and cases

### Case 1 — Bose–Einstein condensation in dilute alkali gases (1995)

Cornell and Wieman at JILA cooled rubidium-87 atoms to 170 nK using laser cooling and evaporative cooling in a magnetic trap, producing the first dilute-gas Bose–Einstein condensate. Anderson et al. *Science* 269, 198 (1995). Ketterle's group at MIT produced the second, in sodium, weeks later. Both Nobel Prize 2001. The companion can use this as the experimental realization of bosonic statistics: 2,000 atoms condensed into a single quantum state, observed by time-of-flight imaging as a sharp peak in the momentum distribution. Rubidium-87 is a boson because 87 = 37 protons + 50 neutrons + 37 electrons = 124 fermions (even); the composite-particle counting works.

### Case 2 — White dwarf mass limit (Chandrasekhar 1931)

A white dwarf is a stellar remnant supported by electron degeneracy pressure — Pauli exclusion forcing electrons into ever-higher momentum states as the star contracts. Chandrasekhar showed in 1931 (*Astrophysical Journal* 74, 81) that this pressure cannot support arbitrarily massive stars: above M ≈ 1.4 solar masses, the electrons become relativistic and the equation of state softens, leading to gravitational collapse. The Chandrasekhar limit is one of the most directly astrophysical consequences of fermionic antisymmetry — without Pauli, every white dwarf would collapse, and Type Ia supernovae (used as cosmological standard candles) would not exist with the regularity that makes them useful.

### Case 3 — Helium-3 vs helium-4 superfluidity

Liquid helium-4 (bosonic — two protons, two neutrons, two electrons, all even-count fermions → composite boson) undergoes a superfluid transition at 2.17 K, the lambda point. Helium-3 (fermionic — one fewer neutron, so total fermion count is odd) does not become superfluid by this mechanism; instead, it forms BCS-like Cooper pairs and becomes superfluid only below 2.5 mK, three orders of magnitude colder. This is the cleanest experimental signature that bosonic vs fermionic statistics determines low-temperature collective behavior. Osheroff, Richardson, Lee — Nobel 1996 for the helium-3 superfluid discovery (1972).

### Failure case — "Identical particles in cosmology must have always been identical"

A subtler trap: identical electrons today are identical because the Standard Model puts them in a single field representation. Whether this would still be true under a putative grand unified theory that broke electron number is an open question. The companion should not promise students that "all electrons in the universe are forever identical" — what's true is that *within the Standard Model and at scales we have probed*, all electrons are excitations of the same field. Don't overclaim.

---

## C. Connections and dependencies

**Prerequisites:** Unit 6 (hydrogen atom, quantum numbers); Unit 7 (angular momentum and spin) — students need to know that two spin-1/2 particles combine into a singlet (antisymmetric, S = 0) and a triplet (symmetric, S = 1), and what the corresponding spin wave functions look like. Linear algebra at the level of determinants of small matrices (for Slater determinants).

**Unlocks:** Unit 9 (approximation methods) — the helium variational calculation, Hartree–Fock approximation. Unit 10 (modern applications) — fermionic vs bosonic many-body systems include semiconductors (electrons obey Pauli, hence band structure has finite Fermi energy), superconductivity (Cooper pairs are composite bosons), and quantum computing in solid-state platforms (qubits as fermionic two-level systems).

**Adjacent unit connections:**
- Unit 7 → Unit 8: The spin-singlet/triplet decomposition is the algebraic input that, combined with antisymmetry of total wave function, produces the parahelium/orthohelium splitting.
- Unit 8 → Unit 9: First-order perturbation theory applied to the electron-electron Coulomb interaction in helium gives a quantitative result that depends on the *symmetry* of the spatial wave function — exchange integrals are the bridge.
- Unit 8 → Unit 10: Bose–Einstein condensation, superconductivity (Cooper pairing of fermions into composite bosons), and the Fermi sea in metals are all direct consequences of the statistics established here.

---

## D. Current state of the field

**Settled:** The spin-statistics theorem (Pauli 1940) is one of the most secure predictions of relativistic quantum field theory; no experimental violation has ever been observed despite searches at the part-per-10²⁷ level for electron-Pauli-principle violations (Ramberg and Snow 1990 *Physics Letters B* 238, 438; tests via X-ray emission limits from transitions that would be forbidden by Pauli). The fermion/boson dichotomy is universal in 3+1 dimensions, full stop.

**Active research:**
- Anyons in 2D systems. The first direct observation of anyonic exchange statistics in the fractional quantum Hall regime was reported by Bartolomei et al. (2020) *Science* 368, 173–177, "Fractional statistics in anyon collisions." [verify: also Nakamura, Liang, Gardner, Manfra 2020 *Nature Physics* 16, 931–936 for an independent demonstration.] This is the frontier the companion should *flag* but not develop.
- Majorana zero modes — fermionic excitations that are their own antiparticles, predicted to appear at the boundaries of topological superconductors. Experimental claims (Mourik et al. 2012 *Science*) have not been confirmed; Microsoft retracted a major 2018 claim in 2022. [verify status as of 2025–2026.]
- Topological quantum computation. Builds on anyons. Active engineering effort at Microsoft Station Q, but a working topological qubit has not been demonstrated as of 2026 [verify].

**Key references:**
- Griffiths, Ch. 5 (2018 third edition).
- Sakurai, J. J. and Napolitano, J. (2017). *Modern Quantum Mechanics*, 2nd ed. Cambridge University Press. Ch. 7 (Identical Particles) is more rigorous and worth pointing strong students toward.
- Wilczek, F. (1990). *Fractional Statistics and Anyon Superconductivity.* World Scientific. [The anyon reference, for advanced readers.]

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **"Why does antisymmetry imply Pauli exclusion?"** Many students learn Pauli as a quantum-number rule and have never been shown that putting two electrons in the same spin-orbital makes the Slater determinant identically zero. The companion should make this single algebraic fact the pedagogical center of gravity.

2. **"What's the difference between Pauli exclusion and the Coulomb repulsion of electrons?"** Pauli is a statement about the structure of the multi-electron wave function; Coulomb is a statement about the Hamiltonian. They are distinct, and they combine to produce Hund's rule. Most introductory treatments blur them. The helium calculation separates them cleanly: the zeroth-order energies are degenerate (singlet and triplet); the first-order Coulomb correction splits them; the splitting size is the exchange integral K.

3. **"Why does the periodic table not just go 1s → 2s → 2p → 3s → 3p → 3d → 4s ...?"** Because the 4s orbital lies lower than 3d in atoms with low Z — screening makes high-ℓ orbitals less stable at fixed n. The Madelung rule encodes this empirically. Students should not be asked to memorize Madelung; they should be shown that screening flips the ordering and that the n + ℓ rule is a useful summary, not a derived law.

**Analogies that work:**
- Slater determinant as "the unique antisymmetric thing you can build from N independent ingredients" — anchors the structure rather than memorizing the form.
- Helium singlet/triplet as "the spins decide the spatial geometry, the spatial geometry decides the Coulomb energy" — gets the exchange-integral intuition right.

**Analogies that mislead:**
- "Bosons like to be together, fermions don't." Cute, wrong-flavored. Replace with "the joint probability density for bosons is enhanced at coincidence; for fermions it vanishes at coincidence — no force, just a correlation in the wave function."
- "Electron clouds repel like rubber balloons." Confuses Coulomb (real force) with antisymmetry (correlation in the wave function). They are independent ingredients.

**Exercises (Bloom's level):**
- **Knowledge:** State the symmetric/antisymmetric postulate; write the Slater determinant for N = 2 and N = 3. (L1)
- **Application:** Construct singlet and triplet spin states for two electrons; assemble the para- and orthohelium total wave functions; predict the spin multiplicity of the ground state of N, P, As, Sb. (L3)
- **Analysis:** Show that the antisymmetric two-particle wave function in an infinite well has lower probability density at x₁ = x₂ than the symmetric one. (L4)
- **Evaluation:** Given the chromium anomaly (3d⁵4s¹), evaluate the competing energy scales (3d/4s ordering vs. half-filled-shell stabilization) and decide whether Madelung "predicts" or "fails to predict" the configuration. (L5)
- **Synthesis:** Derive Hund's first rule from antisymmetry plus Coulomb repulsion, using the exchange integral K. (L6)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 5 (Identical Particles) is the spine of the unit. The 1st edition (pantry text: `822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt`) presents the core material; helium variational in Ch. 7. Cross-check Ch./section numbers against the 3rd edition if that is the adopted text.
- **Liboff, *Introductory Quantum Mechanics*** (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`) — handles identical particles with somewhat more linear-algebra emphasis; useful for the construction of symmetrizer and antisymmetrizer operators if the chapter wants to formalize.
- **Pop-sci references** (Quantum Physics for Beginners 2021): Ch. 13 (Periodic Table) is the assignable narrative for the periodic-table portion. Ch. 18 (superfluids) mentions He-4 as a composite boson — usable as one paragraph of motivation. Both ⚠️ in TIKTOC; companion fills the math.
- **`_lib_QM-Into-the-Light-Beginners.md`** — pop-sci reference notes; relevant for the narrative framing of Pauli's discovery and the "why no two electrons" question students arrive with.
- **`_lib_Significant-Figures-Stewart.md`** — Stewart's chapter on Dirac (if present) might supply the historical context for the spin-statistics connection; check notes for relevance.

---

## G. Gaps and flags

- **FLAG:** The sign convention for the singlet/triplet exchange-integral splitting in helium varies across textbooks. Some define K positive (so triplet lower by K), some define it with the convention absorbed into the Hamiltonian. The companion should pick one (recommend: Griffiths 3rd ed. convention) and stick with it. [verify against Griffiths § 5.2.1 before drafting the calculation.]
- **FLAG:** Hartree–Fock as a topic — should the chapter introduce it or push it to a quantum-chemistry course? Recommendation: name it ("the Slater-determinant ansatz, when minimized variationally over the orbitals, is called Hartree–Fock; Unit 9 will revisit this") but do not develop the equations. This keeps Unit 8 a QM unit rather than drifting into computational chemistry.
- **FLAG:** Anyons and topological quantum computing are tempting because they are exciting current research, but they require 2D topology and braid-group representations that are well beyond an introductory QM course. Recommendation: one paragraph aside in §A.1 noting that the ±1 dichotomy is 3+1-dimensional, and a one-sentence pointer in §D.
- **FLAG:** Recent Pauli-violation tests (VIP experiment at LNGS; Borexino; etc.) put limits at part-per-10²⁷ to 10²⁹ on the probability of a Pauli-violating transition. [verify most recent published limit — VIP-2 collaboration, *Physical Review Letters* or *Physics Letters B*, 2023 or 2024 timeframe.]
- **GAP:** The pop-sci book's Ch. 5 statement of Pauli exclusion is verbal-only and gives no hint that it is derivable from antisymmetry. Companion chapter should explicitly correct this — not as polemic, but as completion. Ch. 5 of the pop-sci book is itself ⚠️ in TIKTOC, so the correction is in keeping with the companion's role.
- **GAP:** Composite bosons (atoms with even fermion count) — the cleanest derivation that He-4 is a boson because all its constituent fermions can be exchanged simultaneously requires care about the *combined* exchange of all six constituents (2 protons + 2 neutrons + 2 electrons). The companion should note that this is a non-trivial calculation in QFT, but state the rule cleanly for the chemistry-oriented student.
