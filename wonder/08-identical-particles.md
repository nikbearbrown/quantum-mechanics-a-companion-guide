# Chapter 8 — Identical Particles

## TL;DR

- The two electrons in helium are not "electron 1 and electron 2" — and the moment you forget that, you have thrown away the helium spectrum, the periodic table, and the white dwarf.
- Watch the argument move: meet the exchange operator, build the Slater determinant, see how symmetry alone — with no force at all — shifts the energy, and pin down where helium's singlet-triplet splitting actually comes from.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Two electrons in helium are not "electron 1 and electron 2." Forgetting that throws away the helium spectrum, the periodic table, and the white dwarf.*

---

Here is a question that sounds like it ought to have a perfectly ordinary answer. You have two electrons in a helium atom. You measure the position of one and find it at $\mathbf{r}_1$. You measure the position of the other and find it at $\mathbf{r}_2$. Now: which electron did you measure first?

Go ahead and try to answer it. You can't. And the reason is not that you forgot to label them, and not that your apparatus was sloppy. The two electrons are genuinely, irreducibly indistinguishable. There is no physical procedure on Earth — no color, no tag, no trajectory you could have followed — that tells "electron 1" apart from "electron 2." The Schrödinger equation for the two electrons looks identical when you swap their labels, and the wave function knows it. A many-particle wave function that treats the two electrons as distinct is, in a precise sense, lying to you about the physics.

Now you might think this is the kind of philosophical hair-splitting that has no observable bite. It is not. Whether the two-electron wave function comes out symmetric or antisymmetric under exchange decides which spin states helium's excited configurations are allowed to have — which decides how often the two electrons sit close together — which decides the Coulomb energy by hundreds of millielectronvolts. The singlet-triplet splitting in helium — two families of states with measurably different energies, called parahelium and orthohelium since the early days — is an experimental fact that a theory built on labeled particles cannot even *write down*, let alone predict.

And it runs far past helium. Without the antisymmetry constraint, every electron in every atom would tumble straight into the $1s$ orbital. Shell structure: gone. The periodic table: gone. Chemistry: gone. The indistinguishability of electrons is not a technicality you are allowed to wave off. It is the foundation the whole material world stands on.

---

## The exchange operator

Let's give the swap a name. Define the *exchange operator* $\hat{P}_{12}$ acting on a two-particle wave function by

$$\hat{P}_{12}\,\psi(\mathbf{r}_1, \mathbf{r}_2) = \psi(\mathbf{r}_2, \mathbf{r}_1).$$

Two things follow right away. First, $\hat{P}_{12}^2 = \hat{1}$ — swap the labels twice and you are exactly back where you started — so $\hat{P}_{12}$ can only have eigenvalues $\pm 1$, nothing else. Second, if the particles are truly identical, every observable has to come out unchanged when you exchange them. In particular the Hamiltonian must commute with the exchange operator:

$$[\hat{H}, \hat{P}_{12}] = 0.$$

Operators that commute with $\hat{H}$ can be diagonalized alongside it. So we get to pick energy eigenstates that are simultaneously eigenstates of $\hat{P}_{12}$ — states that are either *symmetric* (eigenvalue $+1$) or *antisymmetric* (eigenvalue $-1$) under exchange.

And then nature makes one further choice that quantum mechanics itself does not derive: it picks one of the two options for each particle species, and it picks it permanently. Electrons, protons, neutrons, and every other half-integer-spin particle are *fermions* — their many-particle wave functions are antisymmetric under exchange. Photons, Higgs bosons, and every other integer-spin particle are *bosons* — their wave functions are symmetric. The connection between spin and statistics is not a postulate of non-relativistic quantum mechanics but a theorem — Pauli's spin-statistics theorem, proved in 1940 [Pauli, *Physical Review* 58, 716–722](https://doi.org/10.1103/PhysRev.58.716) — that you need relativistic quantum field theory to actually derive. Inside non-relativistic QM, the anti/symmetric assignment is something we put in by hand. You should know the deeper theorem is out there, and that reaching it takes tools we have not built yet.

| particle family | spin | exchange symmetry | examples | statistical behavior | key consequence |
| --- | --- | --- | --- | --- | --- |
| Fermions | half-integer | antisymmetric | electron, proton, neutron | Fermi-Dirac | Pauli exclusion and shell structure |
| Bosons | integer | symmetric | photon, Higgs, $^4$He atom | Bose-Einstein | condensation and coherent fields |

One note on what this postulate covers: it is not just about electrons that happen to be near each other. Two electrons at opposite ends of the galaxy are still identical, and in principle the wave function spanning all electrons in the universe is antisymmetric under the exchange of any pair. In practice, exchange effects between electrons in distant atoms are negligible because the overlap integral between their localized orbitals shrinks exponentially with distance. The antisymmetry holds everywhere; it only *matters* nearby.

And one note for completeness, because it is genuinely surprising: in two spatial dimensions, the whole argument breaks down. When two particles trade places in 2D, the path of exchange can wind around the relative-position singularity in topologically distinct ways, and the exchange phase is no longer stuck at $\pm 1$ — it can be any complex number $e^{i\theta}$. Particles with such intermediate statistics are *anyons*, and they have actually been observed in the fractional quantum Hall effect [Bartolomei et al. 2020, *Science* 368, 173–177](https://doi.org/10.1126/science.aaz5601). The clean $\pm 1$ dichotomy is a property of living in three spatial dimensions — not a property of quantum mechanics as such.

---

## The Slater determinant

For $N$ identical fermions, there is a wonderfully clean way to write down the antisymmetric many-particle wave function. Label the single-particle *spin-orbitals* (spatial wave function times spin state) as $\phi_1, \phi_2, \ldots, \phi_N$, and label the particles $1, 2, \ldots, N$. The antisymmetric state is a determinant:

$$\psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} \phi_1(1) & \phi_1(2) & \cdots & \phi_1(N) \\ \phi_2(1) & \phi_2(2) & \cdots & \phi_2(N) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_N(1) & \phi_N(2) & \cdots & \phi_N(N) \end{vmatrix}.$$

Slater introduced this in 1929 [*Physical Review* 34, 1293–1322](https://doi.org/10.1103/PhysRev.34.1293), and the determinant structure does two jobs for you automatically — for free, with no extra effort.

![N=3 Slater determinant ](../images/08-identical-particles-fig-01.png)
*Figure 8.1 — N=3 Slater determinant *

First, antisymmetry is built right in. Swap two particle labels — which means swapping two columns of the determinant — and the determinant flips sign. That is just what determinants do when you trade two columns. The algebra enforces the postulate; you did not have to lift a finger.

Second — and this is the one that runs all of atomic physics: if two of the spin-orbitals are identical, then two rows of the determinant are the same, and a determinant with two equal rows is zero. The wave function vanishes, identically, everywhere. You cannot put two identical fermions into the same single-particle state — not because of some memorized rule about quantum numbers, but because the antisymmetric wave function you would build from two identical orbitals is simply zero. That is Pauli exclusion, reborn as a property of determinants.

For $N=2$, the Slater determinant reads

$$\psi(1,2) = \frac{1}{\sqrt{2}}\left[\phi_a(1)\phi_b(2) - \phi_a(2)\phi_b(1)\right].$$

For $N=3$, with spin-orbitals $\phi_a, \phi_b, \phi_c$, the determinant fans out into $3! = 6$ terms with alternating signs — every permutation of the three particles among the three orbitals, each weighted by the sign of the permutation. The general $N$-particle case has $N!$ terms.

The Slater determinant is also the bedrock of Hartree–Fock theory — the workhorse of computational quantum chemistry. The approximation goes like this: assume the $N$-electron ground state is a single Slater determinant, then minimize $\langle\psi|\hat{H}|\psi\rangle$ over the choice of single-particle orbitals. Everything in computational chemistry that lives beyond Hartree–Fock — configuration interaction, coupled cluster, density-functional theory — is some correction to that single-determinant guess. This is not a computational footnote. It is the direct consequence of the antisymmetry postulate, applied to atoms.

---

## The exchange correlation: why symmetry affects energy

Before we tackle helium, a simpler example to build intuition. Take two non-interacting identical particles in a 1D infinite well. Particle A is in orbital $\psi_1(x)$; particle B is in orbital $\psi_2(x)$. For distinguishable particles, the joint wave function is just $\psi_1(x_1)\psi_2(x_2)$ and the joint probability density is $|\psi_1(x_1)|^2|\psi_2(x_2)|^2$. Nothing strange yet.

For identical fermions with symmetric spin (both spin-up, so the spin part is symmetric), the spatial wave function is forced to be antisymmetric:

$$\psi_A(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1)\right].$$

For identical bosons, the symmetric spatial wave function is

$$\psi_S(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_1(x_1)\psi_2(x_2) + \psi_1(x_2)\psi_2(x_1)\right].$$

Now evaluate $\langle(x_1-x_2)^2\rangle$ for each case. Expand the squared wave functions, integrate, and the cross terms produce an *exchange integral* that adds to the fermion average separation and subtracts from the boson one. The result (Griffiths §5.1.2 carries this calculation):

$$\langle(x_1-x_2)^2\rangle_\text{fermion} > \langle(x_1-x_2)^2\rangle_\text{distinguishable} > \langle(x_1-x_2)^2\rangle_\text{boson}.$$

Now stop and look at what this says, because it is genuinely surprising. We never turned on an interaction term. The particles are non-interacting — there is no force between them at all. And yet the average separation comes out different for the three cases. The entire difference comes from the symmetry of the spatial wave function. Fermions stay statistically farther apart than distinguishable particles would; bosons huddle statistically closer. This is the *exchange correlation* — and you should call it that, not an "exchange force." There is no extra term in the Hamiltonian. There is only the Coulomb force and the antisymmetry constraint on the wave function. The antisymmetry dictates how often the two electrons sit close enough for the Coulomb repulsion to bite. That is the entire mechanism behind the helium spectrum, and we are about to watch it work.

![No interaction. No force. Just the symmetry of the wave function.](../images/08-identical-particles-fig-02.png)
*Figure 8.2 — Three plots of |ψ(x₁, x₂)|² as a 2D*

---

## Helium: where the singlet-triplet splitting comes from

For two spin-1/2 particles, the spin states split into a *singlet* (antisymmetric under exchange, total spin $S=0$) and a *triplet* (symmetric under exchange, total spin $S=1$):

$$|\text{singlet}\rangle = \frac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle), \qquad |\text{triplet}\rangle \in \left\{|\!\uparrow\uparrow\rangle,\; \tfrac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle),\; |\!\downarrow\downarrow\rangle\right\}.$$

The total wave function — spatial times spin — has to be antisymmetric for electrons (they are fermions). So here is the trade that gets forced on you:

- Spin singlet (antisymmetric) must pair with spatial symmetric: *parahelium*.
- Spin triplet (symmetric) must pair with spatial antisymmetric: *orthohelium*.

Take the helium ground state first, both electrons in the $1s$ orbital. The only spatial wave function you can build from two copies of $\psi_{1s}$ is the symmetric product $\psi_{1s}(\mathbf{r}_1)\psi_{1s}(\mathbf{r}_2)$ — it is automatically symmetric, because there is only the one spatial orbital to work with. That forces the spin to be singlet. The ground state of helium is necessarily $S=0$ parahelium, with no other option available. The choice was made for it.

The first excited state is where it gets interesting: one electron in $1s$, one in $2s$. Now the spatial wave function can go either way — symmetric or antisymmetric:

$$\psi_\pm(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}}\left[\psi_{1s}(\mathbf{r}_1)\psi_{2s}(\mathbf{r}_2) \pm \psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1)\right].$$

The $+$ combination (symmetric) pairs with spin singlet to give parahelium. The $-$ combination (antisymmetric) pairs with spin triplet to give orthohelium. Both start at the same zeroth-order energy — one electron in $1s$, one in $2s$. What splits them is the Coulomb repulsion $e^2/(4\pi\varepsilon_0 r_{12})$.

So compute $\langle V_{ee}\rangle$ on the two spatial states. Expand $|\psi_\pm|^2$, and the diagonal terms give the *direct (Coulomb) integral*

$$J = \int\!\!\int |\psi_{1s}(\mathbf{r}_1)|^2\,|\psi_{2s}(\mathbf{r}_2)|^2\,\frac{e^2}{4\pi\varepsilon_0 r_{12}}\,d^3r_1\,d^3r_2,$$

which is just the classical Coulomb repulsion between the two charge clouds. The cross term, on the other hand, gives the *exchange integral*

$$K = \int\!\!\int \psi_{1s}^{*}(\mathbf{r}_1)\psi_{2s}^{*}(\mathbf{r}_2)\,\frac{e^2}{4\pi\varepsilon_0 r_{12}}\,\psi_{1s}(\mathbf{r}_2)\psi_{2s}(\mathbf{r}_1)\,d^3r_1\,d^3r_2.$$

And $K$ has no classical analog whatsoever. It exists only because the wave function was antisymmetrized — the cross term in $|\psi_\pm|^2$ is there purely on account of the $\pm$ structure. For real $1s$ and $2s$ orbitals, $K > 0$. The energy corrections come out:

$$\langle V_{ee}\rangle_\pm = J \pm K.$$

So parahelium (symmetric spatial, $S=0$) has energy $E_0 + J + K$. Orthohelium (antisymmetric spatial, $S=1$) has energy $E_0 + J - K$. Orthohelium lies *lower*, by $2K$.

And the numbers agree: the orthohelium $1s2s$ state sits at $-59.2$ eV, the parahelium at $-58.4$ eV, a splitting of about 0.8 eV [NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database). Orthohelium lower, exactly as the calculation predicts.

![Helium energy level diagram ](../images/08-identical-particles-fig-03.png)
*Figure 8.3 — Helium energy level diagram *

Now look back at what actually happened here, because it is subtle and worth getting right. The spins did not interact directly — there is no $\hat{S}_1 \cdot \hat{S}_2$ term in the Hamiltonian at this order. What happened is that the spin state *forced the symmetry of the spatial wave function*, which forced how often the electrons sit near each other, which changed the Coulomb energy. The triplet has antisymmetric spatial structure: the electrons keep their distance, the Coulomb repulsion drops, the energy goes down. The spin label is acting as a marker for which spatial symmetry sector you are in. The Coulomb force is doing the work; the antisymmetry is steering it.

This grows into *Hund's first rule*: for a given electron configuration, the term with maximum total spin lies lowest in energy. More parallel spins force more antisymmetric pieces of the spatial wave function, which keeps electrons farther apart, which trims the Coulomb repulsion. The rule is exchange physics, applied configuration by configuration. [Hund 1925, *Zeitschrift für Physik* 33, 345–371](https://doi.org/10.1007/BF01328319).

---

## The periodic table as antisymmetry plus screening

Once you have Pauli exclusion in hand — and we got it straight from antisymmetry — the whole architecture of the periodic table follows from three ingredients: the roughly hydrogenic energy ordering, modified by electron screening; the requirement that each spin-orbital hold at most one electron; and Hund's rule for partially filled subshells.

The *Aufbau* principle is the filling recipe. The *Madelung rule* encodes the empirical filling order: fill orbitals in order of increasing $n + \ell$, and for equal $n + \ell$ fill in order of increasing $n$:

$$1s,\ 2s,\ 2p,\ 3s,\ 3p,\ 4s,\ 3d,\ 4p,\ 5s,\ 4d,\ 5p, \ldots$$

The physical content is screening. An outer electron in a high-$\ell$ orbital is screened from the nucleus more effectively by the inner shells than an electron in a low-$\ell$ orbital at the same $n$, because low-$\ell$ orbitals dive more deeply into the inner shells and feel a larger effective nuclear charge. This is why $4s$ sits below $3d$ in energy for light atoms — the $4s$ electron, despite its larger principal quantum number, burrows into the core more effectively than the $3d$ electron and ends up less screened.

![The Madelung diagonal-filling diagram ](../images/08-identical-particles-fig-04.png)
*Figure 8.4 — The Madelung diagonal-filling diagram *

But Madelung's rule is not exact, and the exceptions are instructive. Chromium's observed ground configuration is $[\text{Ar}]\,3d^5 4s^1$, not the predicted $3d^4 4s^2$. The half-filled $3d^5$ subshell is stabilized by exchange — five parallel spins, one per $d$-orbital, maximizing the spin multiplicity and trimming the intra-subshell Coulomb energy through Hund's rule — and the $4s$–$3d$ gap is small enough that the exchange stabilization wins the contest. Copper is $3d^{10} 4s^1$ for the same reason. There are roughly twenty such exceptions across the periodic table, clustered in the $d$- and $f$-blocks where orbital energies crowd together. These exceptions are not failures of quantum mechanics; they are places where the Madelung heuristic's approximations crack and the actual energy competition has to be computed.

Take carbon as the worked case. $Z=6$: configuration $1s^2\,2s^2\,2p^2$. The filled $1s$ and $2s$ subshells contribute nothing interesting — Pauli requires paired opposite spins, and there is no choice to make. The action is in the $2p$ subshell: two electrons among three available orbitals ($m_\ell = -1, 0, +1$). By Hund's first rule, the two electrons go into *distinct* $m_\ell$ orbitals with *parallel* spins, total $S = 1$, spatial wave function antisymmetric in those two orbitals. The orbital angular momentum picks up $M_L = m_{\ell,1} + m_{\ell,2}$, and by Hund's second rule (maximum $L$ consistent with maximum $S$ and Pauli), the total orbital angular momentum is $L=1$. By Hund's third rule (for a less-than-half-filled subshell, minimum $J$ is the ground state), $J = |L - S| = 0$. The ground term is ${}^3P_0$. And the NIST Atomic Spectra Database lists carbon's ground term as exactly that, ${}^3P_0$ [NIST: C I](https://physics.nist.gov/PhysRefData/ASD/levels_form.html), with ${}^3P_1$ at $16.4\,\text{cm}^{-1}$ and ${}^3P_2$ at $43.4\,\text{cm}^{-1}$ above — fine-structure splittings of a few meV, consistent with spin-orbit coupling acting as a small perturbation on the much larger exchange splitting that already set $S=1$ at the bottom.

The same procedure predicts the ground term of the entire first row. H: ${}^2S_{1/2}$. He: ${}^1S_0$. Li: ${}^2S_{1/2}$. Be: ${}^1S_0$. B: ${}^2P_{1/2}$. C: ${}^3P_0$. N: ${}^4S_{3/2}$. O: ${}^3P_2$. F: ${}^2P_{3/2}$. Ne: ${}^1S_0$. Every prediction checks against NIST.

---

## What the statistics look like at large scale

The antisymmetric structure of fermion wave functions has consequences reaching far past atomic physics. When many fermions fill a band of single-particle states, they stack from the bottom up — each state holds at most one fermion — and at low temperature the distribution sharpens into a step at the Fermi energy. The resulting *Fermi–Dirac distribution* is

$$\langle n_i\rangle_\text{FD} = \frac{1}{e^{(E_i - \mu)/k_BT} + 1}.$$

For bosons, the symmetric wave function allows any number of them to pile into a single state. At low temperature, bosons cascade into the ground state. The *Bose–Einstein distribution* is

$$\langle n_i\rangle_\text{BE} = \frac{1}{e^{(E_i - \mu)/k_BT} - 1}.$$

Look closely — the only difference is the sign in the denominator. A plus for fermions, a minus for bosons. And that single sign is the whole story. At high temperature and low density, both distributions melt into the same classical Maxwell–Boltzmann form. But at low temperature they split apart into two different universes: bosons condense, fermions refuse.

![One sign difference in the denominator. Two different universes at low temperature.](../images/08-identical-particles-fig-05.png)
*Figure 8.5 — Plot of ⟨n_i⟩ vs (E_i − μ)/k_BT for*

Bose–Einstein condensation in dilute gases was first seen in rubidium-87 at 170 nK by Cornell and Wieman's group at Boulder [Anderson et al. 1995, *Science* 269, 198–201](https://doi.org/10.1126/science.269.5221.198), and days later in sodium at MIT by Ketterle's group [Davis et al. 1995, *Physical Review Letters* 75, 3969](https://doi.org/10.1103/PhysRevLett.75.3969). Nobel Prize 2001.

On the fermion side: Chandrasekhar showed in 1931 [*Astrophysical Journal* 74, 81–82](https://doi.org/10.1086/143324) that the *degeneracy pressure* from a Fermi sea of electrons holds up white dwarfs against gravity — up to a limiting mass of $\approx 1.4\,M_\odot$, the Chandrasekhar limit. Above that mass, electron degeneracy pressure cannot win, and the star collapses to a neutron star or a black hole. The same antisymmetry that governs the helium spectrum governs the fate of dying stars.

---

## What would change my mind

The VIP and VIP-2 collaborations at Gran Sasso have been hunting for Pauli-violating atomic transitions in copper — transitions that would simply be forbidden if the antisymmetry postulate held exactly. They have pushed the limits on the probability of such violations down to the part-per-$10^{29}$ level [Curceanu et al. 2017, *Acta Physica Polonica B* 48, 1741; verify most recent VIP-2 bound, likely 2023–2024 *Physics Letters B* or *Physical Review Letters*][verify]. A positive signal at any level would force the central postulate of this chapter to be rewritten. None has appeared. Separately, an integer-spin fundamental particle that behaved like a fermion would force a revision of the spin-statistics theorem, and therefore of relativistic QFT itself. No such particle has ever been seen.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/08-identical-particles-assertions.md -->

---

## Still puzzling

**Why is the spin-statistics connection exact?** Pauli's 1940 proof runs through relativistic causality — operators at spacelike separation must commute or anticommute, depending on spin, so that measurements outside each other's light cone cannot interfere. Both causality and Lorentz invariance are ingredients. Inside QFT these are non-negotiable, so the theorem is non-negotiable inside QFT. Whether QFT itself is the whole story is the harder question.

**What is happening in two dimensions?** Anyons exist because the topology of 2D particle exchange admits more than two equivalence classes of paths. The $\pm 1$ postulate is a statement about 3D topology, not about quantum mechanics. The cleanest exposition is in Wilczek's 1990 *Fractional Statistics and Anyon Superconductivity*. Whether anyon-based topological quantum computation becomes practical is a hardware question open at the time of writing.

**Why does Madelung's rule have exceptions?** The honest answer is that the exchange stabilization of half-filled and full-filled shells competes with orbital energy ordering, and there is no closed-form rule for when one wins. Computational quantum chemistry handles this by computing, not by applying a rule. The Madelung heuristic is a good first-order organizer; it is not derivable from first principles without the calculation.

**Is the universe one large antisymmetric electron wave function?** In principle, yes. In practice, the overlap between localized orbitals at macroscopic separations is exponentially small, and the exchange effects are correspondingly negligible. The global antisymmetry holds; it produces no measurable consequence outside the atomic scale. Whether it is worth thinking about cosmologically is a thought experiment rather than a physics question.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Pauli, W. "The Connection Between Spin and Statistics." *Physical Review* 58, 716–722 (1940). https://doi.org/10.1103/PhysRev.58.716
2. Slater, J. C. "The Theory of Complex Spectra." *Physical Review* 34, 1293–1322 (1929). https://doi.org/10.1103/PhysRev.34.1293
3. Bartolomei, H. et al. "Fractional statistics in anyon collisions." *Science* 368, 173–177 (2020). https://doi.org/10.1126/science.aaz5601
4. Hund, F. "Zur Deutung verwickelter Spektren..." *Zeitschrift für Physik* 33, 345–371 (1925). https://doi.org/10.1007/BF01328319
5. Anderson, M. H. et al. "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science* 269, 198–201 (1995). https://doi.org/10.1126/science.269.5221.198
6. Davis, K. B. et al. "Bose-Einstein Condensation in a Gas of Sodium Atoms." *Physical Review Letters* 75, 3969–3973 (1995). https://doi.org/10.1103/PhysRevLett.75.3969
7. Chandrasekhar, S. "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal* 74, 81–82 (1931). https://doi.org/10.1086/143324
8. NIST Atomic Spectra Database. https://physics.nist.gov/PhysRefData/ASD/levels_form.html
