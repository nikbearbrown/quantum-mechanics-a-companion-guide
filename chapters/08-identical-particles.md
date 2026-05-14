# Unit 8 — Identical Particles

> Two electrons in helium are not "electron 1 and electron 2." Forgetting that throws away the helium spectrum, the periodic table, and the white dwarf.

---

## 1. What this chapter is doing

You have an instinct from classical mechanics that two billiard balls remain distinguishable forever — paint them red and blue and you can follow each trajectory through any collision you like. Quantum mechanics removes the paint. The wave function spreads each particle over a region; the regions overlap; when a detector clicks, there is no procedure available that says *which one* triggered it. That sounds like an inconvenience. It is, in fact, the entire reason chemistry exists. The architecture of multi-electron atoms — and therefore the periodic table, and therefore everything that has periodic-table structure underneath it — follows from one algebraic fact about identical particles: their multi-particle wave function is either symmetric or antisymmetric under exchange. This unit derives that fact, builds the antisymmetric construction (the Slater determinant), shows it kill the helium ground-state calculation if you ignore it, and then uses it to read the periodic table off as a consequence. Griffiths covers this material in Ch. 5 of *Introduction to Quantum Mechanics* — exchange symmetry in §5.1, helium and the periodic table in §5.2. The pop-sci companion ([*Quantum Physics for Beginners*, 2021]) narrates the periodic table well in its Ch. 13 but states the Pauli principle as a rule rather than deriving it from antisymmetry. This unit fills the derivation underneath.

## 2. Learning objectives

By the end of this unit, you should be able to:

- **State** the symmetric/antisymmetric postulate for identical particles and identify which sign applies to bosons and which to fermions. (Bloom L1)
- **Construct** the Slater determinant for $N=2$ and $N=3$ identical fermions in given single-particle orbitals. (L3)
- **Explain** why the antisymmetric two-fermion wave function vanishes when both particles occupy the same single-particle state (Pauli exclusion as a property of determinants). (L3)
- **Compute** the para- and orthohelium total wave functions by combining the spin singlet/triplet with the symmetric/antisymmetric spatial parts. (L4)
- **Predict** the spin multiplicity of the ground state of any first- or second-row atom using Aufbau plus Hund's rule. (L4)
- **Evaluate** which features of the periodic table follow from antisymmetry, which follow from Coulomb screening, and which fall out of Hund's rule. (L5)

## 3. The motivating problem

Set up the helium ground-state calculation the way a student who has just finished Unit 6 (the hydrogen atom) would set it up. The Hamiltonian is

$$ \hat{H} = -\frac{\hbar^2}{2m}\nabla_1^2 - \frac{\hbar^2}{2m}\nabla_2^2 - \frac{Ze^2}{4\pi\epsilon_0 r_1} - \frac{Ze^2}{4\pi\epsilon_0 r_2} + \frac{e^2}{4\pi\epsilon_0 r_{12}}, $$

with $Z=2$ and $r_{12} = |\mathbf{r}_1 - \mathbf{r}_2|$. Drop the electron-electron repulsion term for a moment as "small" (it isn't, but you have to start somewhere). The remaining Hamiltonian separates into two hydrogenic problems with effective charge $Z=2$, and the ground state of each is the $1s$ orbital $\psi_{100}(\mathbf{r})$ with energy $E_1 = -Z^2 \cdot 13.6 \text{ eV} = -54.4$ eV. Two electrons, two such orbitals, total zeroth-order energy $-108.8$ eV. Now add the Coulomb repulsion as a first-order perturbation. The first-order energy correction (we will derive this carefully in Unit 9) is

$$ E^{(1)} = \langle \psi_0 | \frac{e^2}{4\pi\epsilon_0 r_{12}} | \psi_0 \rangle $$

evaluated on the unperturbed two-electron ground state. So far, so undergraduate.

The question is: *what is* $|\psi_0\rangle$? Write it as $\psi_{100}(\mathbf{r}_1) \psi_{100}(\mathbf{r}_2)$ — electron 1 in the $1s$ orbital, electron 2 in the $1s$ orbital — and the integral evaluates to $(5/4) Z \cdot 13.6$ eV $= 34.0$ eV. Combined with the zeroth-order $-108.8$ eV, this gives a predicted ionization energy of $-108.8 + 34.0 = -74.8$ eV. Experimentally, helium's ground-state energy is $-79.0$ eV, measured spectroscopically with five-significant-figure precision ([NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database)). The prediction is off by 4 eV — a 5% error, large by spectroscopic standards but tolerable for a first-order calculation.

This is the right number, by accident.

What you actually did was write a wave function $\psi_{100}(\mathbf{r}_1) \psi_{100}(\mathbf{r}_2)$ that treats the two electrons as labeled. The labels are an artifact of the way you set up the problem; nature has no procedure to enforce them. The correct two-electron ground state must respect the fact that the two electrons are identical, and as we will show in §4.1, this forces the spatial wave function to be either symmetric or antisymmetric under particle exchange. For two electrons both in the $1s$ orbital, the symmetric spatial wave function is just $\psi_{100}(\mathbf{r}_1)\psi_{100}(\mathbf{r}_2)$ — the labels were "accidentally" symmetric, so the answer happens to be correct. But this only works because we put both electrons in the *same* spatial orbital. Try the same shortcut for helium's first excited state (one electron in $1s$, one in $2s$) and the symmetry of the spatial wave function becomes an actual choice — and choosing wrong gives the wrong energy ordering and the wrong spectrum.

The helium $1s2s$ excited state is observed to come in two flavors with measurably different energies: *parahelium* (singlet) at $-58.4$ eV and *orthohelium* (triplet) at $-59.2$ eV, with the triplet lower by about 0.8 eV ([NIST]). A theory that treats the electrons as labeled distinct particles has no language for this splitting. The labels themselves are the bug.

## 4. Concept blocks

### 4.1 The exchange operator and the symmetric/antisymmetric dichotomy

Define the exchange operator $\hat{P}_{12}$ on the two-particle Hilbert space by

$$ \hat{P}_{12} \psi(\mathbf{r}_1, \mathbf{r}_2) = \psi(\mathbf{r}_2, \mathbf{r}_1). $$

Two things follow immediately. First, $\hat{P}_{12}^2 = \hat{1}$ — swap the labels twice and you are back where you started — so the eigenvalues of $\hat{P}_{12}$ are $\pm 1$. Second, if the two particles are genuinely identical, every observable, including the Hamiltonian, must be invariant under their exchange:

$$ [\hat{H}, \hat{P}_{12}] = 0. $$

Commuting observables can be simultaneously diagonalized, so eigenstates of $\hat{H}$ can be chosen as eigenstates of $\hat{P}_{12}$ — that is, as either symmetric ($+1$ eigenvalue) or antisymmetric ($-1$ eigenvalue) under exchange. As far as we have measured in 3+1 dimensions, nature picks one of these two options per particle species and sticks with it.

This is a postulate of non-relativistic quantum mechanics, not a derivation. Griffiths states it in §5.1: "It is a fact that all the particles known to nature fall into one of two categories." The deeper theorem — that integer-spin particles are bosons (symmetric) and half-integer-spin particles are fermions (antisymmetric) — is the *spin-statistics theorem*, proved by Pauli in 1940 ([*Physical Review* 58, 716–722](https://doi.org/10.1103/PhysRev.58.716)) and requiring relativistic quantum field theory to derive. The argument runs through the requirement that field operators at spacelike-separated points commute (for integer spin) or anticommute (for half-integer spin) so that causality is not violated. Inside a non-relativistic QM course you should know the theorem exists, that its proof requires QFT, and that within your current toolkit the connection is a postulate.

In two dimensions, the story breaks down. The two-particle exchange can wind around the relative-position singularity in topologically distinct ways, so the exchange phase is not restricted to $\pm 1$ — it can be any complex phase $e^{i\theta}$, and the resulting particles are *anyons*. They have been observed in the fractional quantum Hall effect ([Bartolomei et al. 2020, *Science* 368, 173–177](https://doi.org/10.1126/science.aaz5601)) and are the substrate of topological quantum computation. Our $\pm 1$ dichotomy is dimension-specific.

**Common misconception.** "Identical particles are identical because they look the same." More precise: identical particles are identical because the Hamiltonian is exchange-symmetric *and* the wave function is symmetric or antisymmetric under exchange. Two electrons in distant atoms are still formally identical; the wave function across all the electrons in the universe is, in principle, antisymmetric. Exchange effects between distant electrons are negligible only because the overlap integral between their localized orbitals is exponentially small, not because the symmetry stops applying.

**Worked example.** Two non-interacting spin-1/2 particles in a one-dimensional infinite well of width $L$. The single-particle eigenstates are $\psi_n(x) = \sqrt{2/L} \sin(n\pi x/L)$ with energies $E_n = n^2 \pi^2 \hbar^2/(2mL^2)$. For both particles in the $n=1$ orbital with antisymmetric spatial wave function:

$$ \psi_A(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_1(x_1)\psi_1(x_2) - \psi_1(x_2)\psi_1(x_1)\right] = 0. $$

The antisymmetric combination is identically zero — Pauli exclusion has fallen out of antisymmetry by construction. You cannot put two identical fermions in the same single-particle state because the antisymmetric wave function constructed from that state vanishes.

### 4.2 Bosons, fermions, and the absence of an "exchange force"

Particles whose multi-particle wave function is symmetric under exchange are *bosons*; particles whose wave function is antisymmetric are *fermions*. The empirical correspondence — observed in every experiment ever performed, derived in QFT via the spin-statistics theorem — is:

- **Bosons** (integer spin $0, 1, 2, \dots$): photon (spin 1), gluon (spin 1), W and Z (spin 1), Higgs (spin 0), and composite particles with an even total number of constituent fermions, like helium-4 atoms (2 protons + 2 neutrons + 2 electrons = 6 fermions, even).
- **Fermions** (half-integer spin $1/2, 3/2, \dots$): electron, proton, neutron, neutrino (all spin 1/2), and composite particles with an odd total number of constituent fermions, like helium-3 atoms (1 proton + 2 neutrons + 2 electrons would be 5 — actually 2 protons + 1 neutron + 2 electrons = 5; the point is the parity).

The statistics that follow are different in kind. For $N$ bosons in single-particle states with occupation numbers $\{n_i\}$, the equilibrium occupation at temperature $T$ is *Bose–Einstein*,

$$ \langle n_i \rangle_{\text{BE}} = \frac{1}{e^{(E_i - \mu)/k_B T} - 1}. $$

For $N$ fermions, the antisymmetrized state has at most one particle per single-particle state, and the occupation is *Fermi–Dirac*,

$$ \langle n_i \rangle_{\text{FD}} = \frac{1}{e^{(E_i - \mu)/k_B T} + 1}. $$

The sign in the denominator is the entire story. At low temperature and high density, bosons crowd into the ground state — *Bose–Einstein condensation*, first observed in dilute rubidium-87 gas at 170 nK by Cornell, Wieman, and collaborators ([Anderson et al. 1995, *Science* 269, 198–201](https://doi.org/10.1126/science.269.5221.198)) and weeks later in sodium by Ketterle's group at MIT ([Davis et al. 1995, *Physical Review Letters* 75, 3969](https://doi.org/10.1103/PhysRevLett.75.3969)); Nobel 2001. At the other extreme, fermions stack into the lowest available states up to the Fermi energy, and the resulting *degeneracy pressure* supports stellar remnants — Chandrasekhar showed in 1931 that electron degeneracy pressure cannot support a white dwarf above $M \approx 1.4 M_\odot$ ([Chandrasekhar 1931, *Astrophysical Journal* 74, 81–82](https://doi.org/10.1086/143324)). Without Pauli, every white dwarf would collapse.

**Common misconception.** "Bosons attract; fermions repel." There is no statistical *force* in the ordinary sense — no term in the Hamiltonian that couples to particle identity. What there is, is a correlation in the joint probability density $|\psi(\mathbf{r}_1, \mathbf{r}_2)|^2$ that emerges from (anti)symmetrization. For two identical fermions in symmetric spin states, the spatial wave function must be antisymmetric, so $|\psi(\mathbf{r}_1, \mathbf{r}_2)|^2 \to 0$ as $\mathbf{r}_1 \to \mathbf{r}_2$ — the particles avoid coincidence. For two identical bosons, the symmetric spatial wave function enhances the probability at coincidence. Call this an *exchange correlation*, not an exchange force. The distinction matters because the helium calculation in §4.4 only gives the right answer if you keep the bookkeeping straight: the Coulomb repulsion is a real force in the Hamiltonian; the (anti)symmetry of the spatial wave function controls how often the electrons sit close enough for that repulsion to matter.

**Worked example.** For two identical particles in adjacent infinite-well orbitals ($n=1$ and $n=2$), compute $\langle (x_1 - x_2)^2 \rangle$ for three cases: distinguishable, identical bosons (symmetric spatial), and identical fermions (antisymmetric spatial). Griffiths walks the calculation in §5.1.2; the result is

$$ \langle (x_1 - x_2)^2 \rangle_{\text{fermion}} > \langle (x_1 - x_2)^2 \rangle_{\text{distinguishable}} > \langle (x_1 - x_2)^2 \rangle_{\text{boson}}. $$

No interaction has been turned on. The fermions "push apart" and the bosons "pull together" purely as a function of the symmetry of the spatial wave function. This is what an exchange correlation looks like.

### 4.3 The Slater determinant

For $N$ identical fermions, the antisymmetric multi-particle wave function is most cleanly written as the determinant of an $N \times N$ matrix whose entries are single-particle orbitals $\phi_i$ evaluated at single-particle coordinates $j$ (including spin):

$$ \psi(1, 2, \dots, N) = \frac{1}{\sqrt{N!}} \det\left[\phi_i(j)\right] = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_1(1) & \phi_1(2) & \cdots & \phi_1(N) \\ \phi_2(1) & \phi_2(2) & \cdots & \phi_2(N) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_N(1) & \phi_N(2) & \cdots & \phi_N(N) \end{vmatrix}. $$

Slater introduced this construction in 1929 ([*Physical Review* 34, 1293–1322](https://doi.org/10.1103/PhysRev.34.1293)) to handle multi-electron atomic spectra systematically. It has two virtues that should be the pedagogical center of the unit.

*First*: antisymmetry is built into the structure. Swap two particle labels (two columns) and the determinant changes sign — that is what determinants do. No work required; the algebra enforces the postulate.

*Second*: if two orbitals are identical (two rows the same), the determinant is zero. This is Pauli exclusion as a property of determinants. The Bohr-era statement "no two electrons can have the same four quantum numbers" is a *consequence* of antisymmetry, not a primitive rule. Students who learn Pauli as a rule about quantum numbers carry the misconception into solid-state physics, where the "quantum numbers" are band indices and crystal momenta and the rule needs re-deriving anyway. Deliver it once, correctly, in Unit 8.

For $N=2$:

$$ \psi(1, 2) = \frac{1}{\sqrt{2}}\left[\phi_a(1)\phi_b(2) - \phi_a(2)\phi_b(1)\right]. $$

For $N=3$, with three spin-orbitals $\phi_a, \phi_b, \phi_c$:

$$ \psi(1, 2, 3) = \frac{1}{\sqrt{6}} \det\begin{pmatrix} \phi_a(1) & \phi_a(2) & \phi_a(3) \\ \phi_b(1) & \phi_b(2) & \phi_b(3) \\ \phi_c(1) & \phi_c(2) & \phi_c(3) \end{pmatrix}. $$

Expanded out, this is a sum of $3! = 6$ terms with alternating signs — every permutation of the three particles among the three orbitals, with the sign of the permutation as the coefficient. The general $N$-particle case has $N!$ terms.

**Common misconception.** "The Slater determinant is just notational shorthand for antisymmetry." It is more than that. It is the *minimal* antisymmetric construction from product states — the simplest antisymmetric thing you can build from $N$ independent single-particle orbitals. And it underlies the Hartree–Fock approximation, the workhorse of computational quantum chemistry: assume the $N$-electron ground state is a single Slater determinant, then minimize $\langle\psi|\hat{H}|\psi\rangle$ over the orbitals. Everything beyond that — configuration interaction, coupled cluster, density-functional theory — is a correction to the single-determinant ansatz. Unit 9 will come back to this when we develop the variational principle.

### 4.4 Helium: the singlet–triplet splitting

The two-electron helium atom is the simplest non-trivial multi-fermion problem and the cleanest place to see exchange effects produce a measurable energy splitting. Each electron has a spatial wave function and a spin state. The total wave function is the product of a spatial part and a spin part — and the total must be antisymmetric under exchange of both particles.

For two spin-1/2 particles, the spin states decompose (Unit 7) into a *spin singlet* (antisymmetric under exchange, total spin $S=0$, one state) and a *spin triplet* (symmetric under exchange, total spin $S=1$, three states):

$$ |\text{singlet}\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle), $$

$$ |\text{triplet}\rangle \in \left\{ |\uparrow\uparrow\rangle,\, \tfrac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle),\, |\downarrow\downarrow\rangle \right\}. $$

To make the *total* wave function (spatial $\times$ spin) antisymmetric:

- **Spin singlet** (antisym) $\otimes$ **spatial symmetric** $\to$ *parahelium*.
- **Spin triplet** (sym) $\otimes$ **spatial antisymmetric** $\to$ *orthohelium*.

The ground state of helium is both electrons in the $1s$ orbital, which forces the spatial wave function to be symmetric (only one symmetric combination of $\phi_{1s}(1)\phi_{1s}(2)$ with itself), which forces the spin to be singlet. The ground state is necessarily parahelium with $S=0$.

The interesting case is the first excited state: $1s2s$ configuration. Now the spatial wave function has two flavors:

$$ \psi_{\text{spatial}}^{\pm}(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}}\left[\psi_{1s}(\mathbf{r}_1)\psi_{2s}(\mathbf{r}_2) \pm \psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1)\right]. $$

The $+$ combination is symmetric and pairs with spin singlet (parahelium, $S=0$). The $-$ combination is antisymmetric and pairs with spin triplet (orthohelium, $S=1$). The zeroth-order energies (ignoring electron-electron repulsion) are degenerate — both have one electron in $1s$ and one in $2s$. The Coulomb repulsion $V_{ee} = e^2/(4\pi\epsilon_0 r_{12})$ splits them.

Compute the first-order correction $\langle V_{ee} \rangle$ on the symmetric and antisymmetric spatial states. Expand the squared spatial wave function:

$$ |\psi_{\text{spatial}}^{\pm}|^2 = \frac{1}{2}\left[|\psi_{1s}(1)|^2|\psi_{2s}(2)|^2 + |\psi_{1s}(2)|^2|\psi_{2s}(1)|^2 \pm 2\,\text{Re}[\psi_{1s}^*(1)\psi_{2s}^*(2)\psi_{1s}(2)\psi_{2s}(1)] \right]. $$

The first two terms in brackets are identical under the integration (they differ only by which electron's label you call "1"); their contribution to $\langle V_{ee} \rangle$ is the *direct (Coulomb) integral*

$$ J = \int\!\!\int |\psi_{1s}(\mathbf{r}_1)|^2 |\psi_{2s}(\mathbf{r}_2)|^2 \frac{e^2}{4\pi\epsilon_0 |\mathbf{r}_1 - \mathbf{r}_2|} d^3r_1\, d^3r_2. $$

This is the classical Coulomb repulsion between two charge distributions $|\psi_{1s}|^2$ and $|\psi_{2s}|^2$, with no exchange content. The cross term gives the *exchange integral*

$$ K = \int\!\!\int \psi_{1s}^*(\mathbf{r}_1)\psi_{2s}^*(\mathbf{r}_2) \frac{e^2}{4\pi\epsilon_0 |\mathbf{r}_1 - \mathbf{r}_2|} \psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1) d^3r_1\, d^3r_2. $$

$K$ has no classical analog. It arises purely from the antisymmetrization (the cross term in the squared wave function). For the $1s2s$ configuration with real orbitals, $K > 0$. Combining,

$$ \langle V_{ee}\rangle_{\pm} = J \pm K. $$

The symmetric spatial state (parahelium, $S=0$) has energy $E_0 + J + K$; the antisymmetric spatial state (orthohelium, $S=1$) has energy $E_0 + J - K$, lower by $2K$. *Orthohelium lies below parahelium for the $1s2s$ configuration*. Empirically: $-59.2$ eV vs. $-58.4$ eV, splitting about 0.8 eV ([NIST]), and the lower state has $S=1$. (Sign convention here follows [Griffiths §5.2.1, 3rd ed.][verify against your edition]; some texts absorb sign factors differently and write the splitting with the opposite sign on $K$.)

The deeper point: the spins do not interact directly at this order. There is no $\hat{S}_1 \cdot \hat{S}_2$ term in the Hamiltonian (until you add spin-orbit coupling, which is much smaller). What is happening is that *the spin state forces the symmetry of the spatial wave function*, which forces how often the electrons sit close to each other, which controls the Coulomb energy. The triplet has antisymmetric spatial, the electrons stay further apart, the Coulomb energy is lower. The spin label is just a marker — the Coulomb repulsion is doing the work, channeled by antisymmetry.

This generalizes to *Hund's first rule*: for a given electron configuration, the term with maximum total spin lies lowest in energy. Parallel spins force the spatial wave function to be antisymmetric in those orbitals, which reduces the Coulomb repulsion. Hund's rule is exchange physics applied configuration by configuration ([Hund 1925, *Zeitschrift für Physik* 33, 345–371](https://doi.org/10.1007/BF01328319)).

**Common misconception.** "Hund's rule says parallel spins repel less." The opposite: parallel spins *force the spatial wave function to be antisymmetric*, which keeps the electrons apart, which reduces the Coulomb repulsion. The spins themselves do not interact at this order. The exchange correlation does all the work; the spin label only tells you which spatial-symmetry sector you are in.

### 4.5 The periodic table as antisymmetry plus screening

The architecture of the periodic table follows from three ingredients: the approximate hydrogenic energy ordering (modified by screening of one electron by the others), the Pauli principle from antisymmetry (at most two electrons per spatial orbital — one spin-up, one spin-down), and Hund's rule from exchange (within a partially-filled subshell, parallel spins fill distinct $m_\ell$ orbitals before any pairing).

The *Aufbau* ("building-up") principle is the recipe: fill orbitals in order of increasing energy, respecting Pauli, with Hund's rule resolving ties. The *Madelung rule* ([Madelung 1936, *Die mathematischen Hilfsmittel des Physikers*]) gives the empirical filling order as "lowest $n + \ell$ first; for equal $n + \ell$, lowest $n$ first":

$$ 1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p,\ 6s,\ 4f,\ 5d,\ 6p,\ 7s,\ 5f,\ 6d,\ 7p. $$

The pattern reflects screening: an outer electron in a high-$\ell$ orbital is more thoroughly screened from the nucleus by the inner electrons than an electron in a low-$\ell$ orbital of the same principal quantum number, because low-$\ell$ orbitals penetrate the inner shells. So the $4s$ orbital ends up below $3d$ in energy for light atoms — Madelung's rule encodes the screening empirically.

The rule is not exact. Chromium is observed as $[\text{Ar}]\,3d^5 4s^1$ rather than the Madelung-predicted $3d^4 4s^2$, because the half-filled $d^5$ configuration is stabilized by exchange (five parallel spins maximize the spin multiplicity and minimize the Coulomb energy through Hund's rule), and the $4s$–$3d$ energy gap is small enough that the exchange stabilization wins. Copper is $3d^{10}4s^1$ for the analogous reason (fully-filled $d^{10}$ stability). There are roughly twenty such exceptions across the periodic table, mostly in the $d$- and $f$-blocks where orbital energies become near-degenerate ([NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database) lists the experimental ground-state configuration of every element).

The deeper move worth making explicit: chemistry is the low-energy effective theory of atoms whose ground states are dictated by fermionic antisymmetry plus Coulomb. Without antisymmetry, every electron in every atom would crash into the $1s$ orbital and there would be no chemistry at all — just $N$ copies of helium-like systems with increasing nuclear charge, no shell structure, no valence electrons, no periodicity. The periodic table is a direct empirical signature of the antisymmetric structure of the electronic wave function.

**Common misconception.** "Madelung's rule is exact." It is a good first-order rule. Real atoms have $\sim 20$ exceptions and the rule fails increasingly badly in the heaviest elements where relativistic effects (the $6s$ contraction, the lanthanide and actinide contractions) become significant. Students should not be asked to memorize Madelung; they should be shown that screening flips the energy ordering and that the $n + \ell$ rule is a useful summary, not a derived law.

## 5. Worked example — the carbon ground state

Take carbon, $Z=6$. The Aufbau prescription is

$$ 1s^2\ 2s^2\ 2p^2. $$

Six electrons. The $1s$ subshell is full (two electrons, opposite spins, spin singlet by Pauli — no choice). The $2s$ subshell is full (same reason). The interesting subshell is $2p$, which contains two electrons in three orbitals ($m_\ell = -1, 0, +1$).

By Hund's first rule, the two $2p$ electrons go into *distinct* $m_\ell$ orbitals with *parallel* spins — that is, the spin state is the symmetric triplet ($S=1$), and the spatial state is antisymmetric in the two singly-occupied $2p$ orbitals. Pick $m_{\ell,1} = +1$ and $m_{\ell,2} = 0$ (any choice within the three available works at this order); the total orbital angular momentum projection is $M_L = m_{\ell,1} + m_{\ell,2} = +1$. By symmetry across all the choices, the maximum total $L = 1$, and the ground term is

$$ {}^{2S+1}L_J = {}^{3}P_J,\ \text{with } J = |L - S|, \dots, L + S = 0, 1, 2. $$

By Hund's third rule (the spin-orbit coupling rule, which we will derive in the fine-structure section of Unit 9), for a less-than-half-filled subshell the lowest $J$ is the ground state, so the carbon ground term is ${}^3P_0$. The NIST atomic spectra database lists carbon's ground term as ${}^3P_0$ ([NIST Atomic Spectra: C I](https://physics.nist.gov/PhysRefData/ASD/levels_form.html)) at energy $0$, with ${}^3P_1$ at $16.4$ cm$^{-1}$ above and ${}^3P_2$ at $43.4$ cm$^{-1}$ above — fine-structure splittings on the order of $5 \times 10^{-3}$ eV, consistent with the spin-orbit coupling being a small perturbation on the much larger ($\sim$ eV) exchange splitting that put $S=1$ at the bottom in the first place.

The same exercise predicts the ground term of the entire first row: H is ${}^2S_{1/2}$, He is ${}^1S_0$, Li is ${}^2S_{1/2}$, Be is ${}^1S_0$, B is ${}^2P_{1/2}$, C is ${}^3P_0$, N is ${}^4S_{3/2}$, O is ${}^3P_2$, F is ${}^2P_{3/2}$, Ne is ${}^1S_0$. Cross-check against NIST for any of these — every prediction agrees.

What the exercise teaches: antisymmetry plus Hund's rule, applied to a known electron configuration, predicts the spin multiplicity and approximate orbital angular momentum of the ground state of any atom in the first two rows of the periodic table. Beyond that, configuration interaction (multiple Slater determinants contributing to the ground state) and relativistic effects become important, and the simple rule breaks down. Inside its domain of validity it is exact, and the domain covers the chemistry most students care about.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Exchange symmetry | §5.1 ("Two-Particle Systems") | not covered | §4.1 (operator, $\pm 1$ postulate, anyon aside) |
| Bosons and fermions | §5.1.1–5.1.2 | Ch. 18 (superfluids, touches) | §4.2 (BE/FD statistics, exchange correlation) |
| Slater determinant | §5.2 (multi-electron atoms) | not covered | §4.3 (construction, Pauli-from-determinants) |
| Helium singlet/triplet | §5.2.1 (helium) | not covered | §4.4 (full exchange-integral derivation) |
| Periodic table | §5.2.2 | Ch. 13 ✅ | §4.5 (antisymmetry + screening + Hund) |

The pop-sci book Ch. 13 is the right narrative reading for the periodic-table material. Griffiths Ch. 5 is the right formal reference. This companion supplies the antisymmetry derivation underneath, which Ch. 13 omits and Griffiths compresses.

## 7. Exercises

**E1 (L1, Knowledge).** State the symmetric/antisymmetric postulate. Write the $N=2$ Slater determinant explicitly. Identify which sign goes with bosons and which with fermions.

**E2 (L3, Application).** Construct the Slater determinant for the ground state of lithium ($1s^2 2s^1$). Three electrons in three spin-orbitals: $1s\uparrow$, $1s\downarrow$, $2s\uparrow$. Write the $3\times 3$ determinant, expand it as a sum of six terms with alternating signs, and verify by direct computation that exchanging any two particle labels flips the sign of the wave function.

**E3 (L3, Application).** Two non-interacting spin-1/2 particles sit in a 1D infinite well of width $L$, in spatial orbitals $n_1 = 1$ and $n_2 = 2$, both with spin up (spin state $|\uparrow\uparrow\rangle$, symmetric). Write the total wave function with the correct symmetry. Now sketch $|\psi(x_1, x_2)|^2$ along the line $x_1 = x_2$ from $0$ to $L$ and confirm it vanishes there.

**E4 (L4, Analysis).** Show that the antisymmetric two-particle spatial wave function $\psi_A(x_1, x_2) = (1/\sqrt{2})[\psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1)]$ has $\langle (x_1 - x_2)^2 \rangle$ strictly greater than the corresponding symmetric combination, for any two orthonormal one-particle states $\psi_1$ and $\psi_2$. (Hint: expand the squared wave function and identify the cross term.)

**E5 (L4, Application).** Predict the ground-state term symbol ${}^{2S+1}L_J$ of nitrogen ($Z=7$). Use Aufbau to get the configuration, Hund's first rule to set $S$, Hund's second rule (maximum $L$ consistent with maximum $S$ and Pauli) to set $L$, Hund's third rule to set $J$. Then cross-check against the NIST Atomic Spectra Database.

**E6 (L5, Evaluation).** Chromium has the experimentally observed configuration $[\text{Ar}]\, 3d^5 4s^1$, contradicting the Madelung prediction $3d^4 4s^2$. Identify the two competing energy scales (the $4s$–$3d$ energy gap, and the exchange stabilization of the half-filled $3d^5$ subshell), estimate their relative size, and explain why a strict Madelung-based "rule" does not capture this. What does the chromium anomaly tell you about the level of theory at which Aufbau is a useful organizing principle?

**E7 (L6, Synthesis).** Derive Hund's first rule from antisymmetry plus Coulomb repulsion. Start with two electrons in two orthogonal spatial orbitals $\phi_a$ and $\phi_b$. Show by explicit construction that the spin-triplet state forces an antisymmetric spatial wave function, that the antisymmetric spatial wave function has $\langle 1/r_{12} \rangle$ smaller than the symmetric one (by an exchange integral $K > 0$), and that this puts the triplet $2K$ below the singlet. Generalize: more parallel spins $\to$ more antisymmetric spatial pieces $\to$ lower Coulomb energy. State the rule and the limit (it applies within a configuration; it does not predict the configuration itself).

## 8. What would change my mind

A controlled experiment that demonstrated an *exchange phase* other than $+1$ or $-1$ for ordinary electrons or other 3+1-dimensional matter particles — for instance, a Pauli-principle-violating atomic transition in a regime where the antisymmetry postulate forbids it. The VIP and VIP-2 collaborations at Gran Sasso have searched for exactly this kind of violation in copper and have placed limits on the probability of Pauli-violating electronic transitions at the part-per-$10^{29}$ level ([Curceanu et al. 2017, *Acta Physica Polonica B* 48, 1741; verify the most recent VIP-2 bound, likely 2023–2024 *Physics Letters B* or *Physical Review Letters*][verify]). A positive signal at any level would force the central postulate of this chapter to be revised. None has appeared. Separately, an experimental demonstration that the spin-statistics theorem fails — for instance, an integer-spin fundamental particle that behaved as a fermion — would force a revision of relativistic quantum field theory, not just this chapter. No such particle has been observed.

The aging risk on this unit's specific numbers is low. Helium's measured ground state and the singlet/triplet splittings have been known to high precision since the 1960s; the periodic-table assignments are stable. The frontier is in two-dimensional anyonic systems (where the $\pm 1$ postulate does not apply by construction, so this chapter's claims are not at risk — it is the *dimensionality* of the system that lets the postulate generalize) and in topological quantum computation. Both deserve their own treatment and neither contradicts the 3+1-dimensional postulate this chapter is built on.

## 9. Still puzzling

- *Why is the spin-statistics connection exact?* Pauli's 1940 proof relies on relativistic causality (operators at spacelike separation commute or anticommute) and on the structure of representations of the Lorentz group. Both are non-negotiable inside QFT, so the conclusion is non-negotiable inside QFT. But QFT itself rests on assumptions — Lorentz invariance, locality, microcausality — that we have not derived from anything more fundamental. The connection is exact within the theory; whether the theory is exact is the harder question.

- *What is happening in two dimensions?* Anyons exist because the topology of two-particle exchange in 2D admits more than two equivalence classes. The 3+1-dimensional postulate is not "true everywhere"; it is true wherever the topology allows only two classes. The cleanest pedagogical version of this argument is in Wilczek's 1990 *Fractional Statistics and Anyon Superconductivity*. Whether anyon-based topological quantum computation will become practical is a separate, hardware question.

- *Why does Madelung's rule have exceptions?* The standard answer — that the exchange stabilization of half-filled or fully-filled shells competes with the orbital energy ordering — is correct but unsatisfying as a *predictive* rule. There is no closed-form expression for "when does exchange beat orbital energy"; you have to compute. Computational quantum chemistry handles this routinely (Hartree–Fock, post-Hartree–Fock methods, DFT), but the chapter-level rule is empirical because the underlying physics is genuinely a balance of several effects of comparable magnitude.

- *Is the universe one big antisymmetric electron wave function?* In principle, yes. In practice, the overlap integral between localized orbitals on widely separated atoms is exponentially small in the distance, so the antisymmetry between, say, an electron in your hand and an electron in Andromeda contributes nothing measurable. The reductio — "you are entangled with every electron in your light cone" — is technically defensible and operationally useless. I prefer to label the wave function "locally antisymmetric for atoms within overlap distance" and leave the cosmological extension as a thought experiment.

**Tags:** identical-particles, exchange-symmetry, slater-determinant, pauli-exclusion, helium-spectrum, periodic-table, hunds-rule, spin-statistics-theorem, griffiths-ch5
