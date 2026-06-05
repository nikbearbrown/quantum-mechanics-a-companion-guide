# Chapter 6 — The Hydrogen Atom


## TL;DR

- Delivers the exact quantum solution of the one-electron, one-proton Coulomb problem.
- Covers: central potential and separation of variables, the 1s solution and the origin of $a_0$ and $-13.6\,\text{eV}$, the failure of the orbit picture, the SO(4) symmetry behind the energy degeneracy, the four quantum numbers, spin, and the Pauli exclusion principle.
- Provides the vocabulary, the working formulas, and the judgment needed to apply them.

*One electron, one proton, a Coulomb potential — and the cleanest test we have of whether quantum mechanics is right about the world.*

---

Hydrogen's emission spectrum is a set of discrete colored lines produced in a discharge tube. In 1885 Johann Balmer fit their wavelengths to an empirical formula, derived from no physical principle:

$$\lambda_n = B \cdot \frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, \ldots$$

with $B \approx 364.5$ nm. [Balmer 1885, *Annalen der Physik* 261, 80–87](https://doi.org/10.1002/andp.18852610506) [verify]. The formula reproduced the data; it had no explanation.

In 1913 Niels Bohr supplied a derivation. [Bohr 1913, *Philosophical Magazine* Series 6, 26, 1–25](https://doi.org/10.1080/14786441308634955). His postulate: the electron moves in circular orbits, but only those for which the angular momentum is an integer multiple of $\hbar$ are allowed. Combining this rule with Newton's second law for circular motion under the Coulomb force reproduces Balmer's formula with the correct coefficient. The energy levels are

$$E_n = -\frac{13.6\,\text{eV}}{n^2}.$$

The visible lines — 656 nm, 486 nm, 434 nm — all come out correct.

![Hydrogen emission spectrum in the visible range ](../images/06-the-hydrogen-atom-fig-01.png)
*Figure 6.1 — Hydrogen emission spectrum in the visible range *

The result is historically important and physically misleading. Bohr's model assigns the electron a definite circular path at a definite radius. That picture is false. The energies are nonetheless correct.

The reason is structural. The Coulomb potential $V \propto 1/r$ carries a symmetry beyond the obvious rotational one, and that symmetry forces all states with the same $n$ to share an energy regardless of their actual behavior. Bohr's method exploited a consequence of this symmetry without identifying it. It is hydrogen-specific: applied to helium, the same method fails by about 30%.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-the-hydrogen-atom-assertions.md (specific 30% figure should be sourced; magnitude correct ~30–40%) -->
 This chapter solves hydrogen exactly, locates the origin of $a_0$ and $-13.6\,\text{eV}$, and uses the exact solution to discard the orbiting-particle picture.

---

## The setup: central potential, separation of variables

The Hamiltonian for one electron bound to one proton is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}.$$

The potential depends only on $r$, not on direction. A potential of this form is *central*. Use this property for any single-particle problem with rotational symmetry: it permits spherical coordinates and separation of the Schrödinger equation into radial and angular parts.

Set $\psi(r,\theta,\phi) = R(r) \cdot Y(\theta,\phi)$ and substitute into $\hat{H}\psi = E\psi$. The angular part reduces to an eigenvalue equation for $\hat{L}^2/\hbar^2$ on the sphere. Its solutions are the spherical harmonics $Y_{\ell m}(\theta,\phi)$, derived in Unit 7. Required facts: they exist, they carry two integer labels $\ell \geq 0$ and $-\ell \leq m \leq \ell$, and they are orthonormal on the sphere. The $1s$ state has $\ell = 0$, for which the single spherical harmonic is the constant $Y_{00} = 1/\sqrt{4\pi}$.

The radial equation, with $u(r) = rR(r)$ converting it to one dimension, is

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2m_e r^2}\right]u = Eu.$$

The bracketed term $\hbar^2\ell(\ell+1)/(2m_e r^2)$ is the *centrifugal barrier*. It comes from the separation itself, not from a classical assumption. For $\ell > 0$ this repulsive $1/r^2$ term excludes the electron from the nucleus. For $\ell = 0$ the term vanishes, and the electron carries significant probability near $r = 0$.

For the $1s$ state ($\ell = 0$):

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\varepsilon_0 r}u = Eu.$$

![Effective potential energy diagram for the hydrogen radial](../images/06-the-hydrogen-atom-fig-02.png)
*Figure 6.2 — Effective potential energy diagram for the hydrogen radial*

---

## Solving the 1s state: where the numbers come from

Use the ansatz $u(r) = Ar\,e^{-r/a}$, with $A$ a normalization constant and $a$ a length scale to be fixed. The factor of $r$ is mandatory: $R(r) = u(r)/r$ must be finite at the origin, so $u(0) = 0$. The exponential guarantees normalizability.

**Given.** The $\ell = 0$ radial equation above and the trial form $u(r) = Ar\,e^{-r/a}$.

**Find.** The length scale $a$ and the ground-state energy $E_1$.

**Solution.** Differentiate twice:

$$\frac{du}{dr} = Ae^{-r/a}\!\left(1 - \frac{r}{a}\right), \qquad \frac{d^2u}{dr^2} = Ae^{-r/a}\!\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

Substitute into the radial equation and divide through by $Ae^{-r/a}$:

$$\frac{\hbar^2}{m_e a} - \frac{\hbar^2 r}{2m_e a^2} - \frac{e^2}{4\pi\varepsilon_0} = Er.$$

The equation must hold for all $r$, so the constant terms and the $r$-linear terms each vanish independently.

Constant terms:
$$\frac{\hbar^2}{m_e a} = \frac{e^2}{4\pi\varepsilon_0} \implies a = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \equiv a_0.$$

Linear-in-$r$ terms:
$$E = -\frac{\hbar^2}{2m_e a_0^2}.$$

Evaluating: $E_1 \approx -13.6\,\text{eV}$.

**Check.** The Bohr radius $a_0 \approx 5.29 \times 10^{-11}$ m and the ionization energy $13.6\,\text{eV}$ follow directly from matching the constant and linear pieces. No quantization condition was imposed and no orbit assumed. The ansatz $u \propto re^{-r/a}$ is self-consistent only for $a = a_0$ and $E = E_1$, which fixes both.

Normalize. The full wave function is $\psi_{100} = R_{10}(r) \cdot Y_{00}$, with $R_{10}(r) = Ae^{-r/a_0}$ and $Y_{00} = 1/\sqrt{4\pi}$. The condition $\int|\psi|^2 d^3r = 1$ separates:

$$\int_0^\infty |R_{10}|^2 r^2\,dr \cdot \int |Y_{00}|^2\,d\Omega = 1.$$

The angular integral is 1; the radial integral gives $A = 2/a_0^{3/2}$. The normalized ground state is

$$\boxed{\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.}$$

![Plot of the 1s radial wave function R₁₀(r)](../images/06-the-hydrogen-atom-fig-03.png)
*Figure 6.3 — Plot of the 1s radial wave function R₁₀(r)*

---

## Dismantling the orbit picture

The Bohr model gives the energy correctly but describes the electron's location incorrectly. The exact solution settles the question.

The *radial probability density* — the probability of finding the electron in a shell of radius $r$ and thickness $dr$ — is

$$P(r) = |R_{10}(r)|^2 \cdot r^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

The $r^2$ factor is the spherical-coordinate Jacobian: a shell of fixed thickness has more volume at larger $r$. This factor competes against the decaying exponential.

**Given.** $P(r) = (4/a_0^3)\,r^2 e^{-2r/a_0}$.

**Find.** The most probable radius and the mean radius.

**Solution.** Maximize $P(r)$:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0 \implies r_{\text{mp}} = a_0.$$

Then compute the expectation value:

$$\langle r\rangle = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr = \frac{4}{a_0^3} \cdot \frac{6}{(2/a_0)^4} = \frac{3a_0}{2}.$$

**Check.** The most probable radius is $a_0$; the mean radius is $\tfrac{3}{2}a_0$. The two numbers differ because $P(r)$ peaks at $a_0$ but has a long tail toward larger $r$ that raises the average. A circular orbit at radius $a_0$ would put both quantities at $a_0$. Their disagreement is the signature of a distribution of radii rather than a single one. There is no orbit; there is a probability cloud.

![The orbit picture requires both markers to be at the same place. They are not.](../images/06-the-hydrogen-atom-fig-04.png)
*Figure 6.4 — P(r) = (4/a₀³)r²e^{−2r/a₀} plotted vs r/a₀ from 0*

There is likewise no instant at which the electron has a definite radius, speed, and direction. What exists is $|\psi_{100}|^2$ — a spherically symmetric cloud decaying exponentially from the nucleus, with $a_0$ as its length scale. Bohr obtained the correct length scale by assuming a circular orbit. The length scale is physical; the orbit is not.

---

## Why Bohr got the energies right: the hidden symmetry

The agreement between Bohr's incorrect model and the correct energies has a structural cause. The Coulomb potential $V = -e^2/(4\pi\varepsilon_0 r)$ carries extra symmetry. Beyond rotational symmetry $\mathrm{SO}(3)$, the $1/r$ potential has a second conserved quantity: the Laplace–Runge–Lenz vector, which points along the major axis of the classical ellipse and has fixed magnitude. The full symmetry group of the Coulomb problem is $\mathrm{SO}(4)$.

Pauli used this symmetry in early 1926 to solve hydrogen algebraically, ahead of Schrödinger's wave-mechanical solution. [Pauli 1926, *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify pages]. The consequence of $\mathrm{SO}(4)$: the energy depends only on the principal quantum number $n$, not on $\ell$. States with the same $n$ and different $\ell$ — $2s$ and $2p$, for instance — have identical energy. This is *accidental degeneracy*, a misnomer; it is forced by the symmetry.

Bohr's condition $L = n\hbar$ is incorrect about angular momentum: the eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, with $\ell$ ranging from $0$ to $n-1$. But because energy depends only on $n$, the energy formula is correct anyway. Apply the method to helium — two electrons, no clean $\mathrm{SO}(4)$, no accidental degeneracy — and it fails by about 30%. The success was always specific to hydrogen.

---

## The four quantum numbers

Each hydrogen state carries four quantum numbers.

The *principal quantum number* $n = 1, 2, 3, \ldots$ sets the energy $E_n = -13.6\,\text{eV}/n^2$. It labels the eigenvalue of $\hat{H}$.

The *orbital angular momentum quantum number* $\ell = 0, 1, \ldots, n-1$ sets the magnitude of orbital angular momentum: $\hat{L}^2\psi = \hbar^2\ell(\ell+1)\psi$. The spectroscopic letters $s, p, d, f$ denote $\ell = 0, 1, 2, 3$, retained by convention from pre-quantum spectroscopy ("sharp, principal, diffuse, fundamental").

The *magnetic quantum number* $m_\ell = -\ell, -\ell+1, \ldots, +\ell$ sets the projection of orbital angular momentum on a chosen axis: $\hat{L}_z\psi = m_\ell\hbar\psi$.

The *spin quantum number* $m_s = \pm 1/2$ sets the projection of spin angular momentum: $\hat{S}_z\psi = m_s\hbar\psi$.

The total number of states at level $n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2 \quad\text{(without spin)}, \qquad 2n^2 \quad\text{(with spin)}.$$

The $n^2$ factor follows from the $\mathrm{SO}(4)$ degeneracy. The $n=1$ shell holds 2 electrons, $n=2$ holds 8, $n=3$ holds 18 — the periodic-table row capacities, set by quantum mechanics and Pauli rather than by chemistry.

| $n$ | $\ell$ values | spectroscopic labels | $m_\ell$ values | orbitals | states with spin |
| --- | --- | --- | --- | ---: | ---: |
| 1 | 0 | 1s | 0 | 1 | 2 |
| 2 | 0, 1 | 2s, 2p | 0; -1, 0, +1 | 4 | 8 |
| 3 | 0, 1, 2 | 3s, 3p, 3d | 0; -1, 0, +1; -2, -1, 0, +1, +2 | 9 | 18 |
| 4 | 0, 1, 2, 3 | 4s, 4p, 4d, 4f | $m_\ell=-\ell,\ldots,+\ell$ | 16 | 32 |

Terminology: "orbital" does not mean "orbit." An orbital — the spherical $s$ cloud, the dumbbell $p$, the four-lobed $d$ — is an isocontour of $|\psi_{n\ell m}|^2$, conventionally drawn at the surface enclosing 90% of the probability. It records where the electron is likely to be found on measurement, not what it does between measurements. Quantum mechanics provides no between-measurements account. The orbital shape is the content; there is no trajectory.

![90%-probability isosurface renderings of the 1s, 2s, 2p_z,](../images/06-the-hydrogen-atom-fig-05.png)
*Figure 6.5 — 90%-probability isosurface renderings of the 1s, 2s, 2p_z,*

---

## Spin: the internal angular momentum that cannot be rotation

In 1922 Stern and Gerlach passed a beam of neutral silver atoms through an inhomogeneous magnetic field. Classically, magnetic moments at all orientations should produce a continuous smear at the detector. The observed result was two discrete spots. [Stern & Gerlach 1922, *Zeitschrift für Physik* 9, 349–352](https://doi.org/10.1007/BF01326983) [verify pages].

Silver has one unpaired $5s$ electron. The two spots correspond to the two projections of its spin on the field axis, $S_z = +\hbar/2$ and $S_z = -\hbar/2$ — two outcomes, not a continuum.

![Two spots where classical physics predicts a smear. The discreteness is spin.](../images/06-the-hydrogen-atom-fig-06.png)
*Figure 6.6 — Stern-Gerlach apparatus diagram *

Historical point: in 1922 Stern and Gerlach did not read their result as electron spin, which had not yet been proposed. They interpreted it as "space quantization" of orbital angular momentum. The correct reading — splitting due to the unpaired $5s$ electron's spin — came only after Uhlenbeck and Goudsmit proposed intrinsic electron spin in 1925. [Uhlenbeck & Goudsmit 1925, *Die Naturwissenschaften* 13, 953–954](https://doi.org/10.1007/BF01558878) [verify]. The experiment preceded its interpretation by three years.

Spin is intrinsic angular momentum. Every electron carries angular momentum of magnitude $\sqrt{s(s+1)}\hbar = (\sqrt{3}/2)\hbar$ with $s = 1/2$. It is not angular momentum of spatial motion; it is a property the electron possesses, like charge or mass. The Dirac equation — the relativistic Schrödinger equation — produces spin automatically: requiring a quantum wave equation to be Lorentz-invariant forces spin-1/2 as an algebraic consequence. [Dirac 1928, *Proceedings of the Royal Society A* 117, 610–624](https://doi.org/10.1098/rspa.1928.0023). Spin cannot be excluded.

The spinning-ball picture is ruled out by a direct calculation.

**Given.** Model the electron as a uniform solid sphere of radius $r_e$ rotating about its axis, with $I = \frac{2}{5}m_e r_e^2$, and require its angular momentum to equal $\hbar/2$. The classical electron radius is $r_e \approx 2.82 \times 10^{-15}$ m.

**Find.** The required equatorial speed.

**Solution.** For the angular momentum to equal $\hbar/2$,

$$v = \omega r_e = \frac{Lr_e}{I} = \frac{5\hbar}{4m_e r_e}.$$

Insert the classical electron radius (obtained by equating the electron's rest-mass energy to its electrostatic self-energy):

$$v \approx \frac{5(1.055\times10^{-34})}{4(9.11\times10^{-31})(2.82\times10^{-15})} \approx 5.1 \times 10^{10}\,\text{m/s}.$$

**Check.** That is roughly 170 times the speed of light, matching the solid-sphere estimate in the reference spin chapter. Experiment constrains the electron to be pointlike down to at least $10^{-18}$ m; a smaller radius drives the required speed far higher still. The spinning-ball model is geometrically impossible, not merely imprecise.

The picture persists in introductory texts as convenient shorthand. The calculation above is sufficient to retire it.

---

## The Pauli exclusion principle

In 1925, before the Schrödinger equation existed, Pauli proposed that no two electrons in an atom share all four quantum numbers $(n, \ell, m_\ell, m_s)$. [Pauli 1925, *Zeitschrift für Physik* 31, 765–783](https://doi.org/10.1007/BF02980631). He reached it from atomic-spectra patterns — shell-filling counts and the rules governing which spectral lines appear. The rule fit the data without an underlying explanation.

The deeper account, developed in Unit 8: electrons are fermions, so their multi-particle wave function is antisymmetric under exchange of any two particles, $\psi(1,2) = -\psi(2,1)$. Two electrons in the same state would require the wave function to equal its own negative, hence to vanish; no such state exists. Exclusion is a corollary. The operational consequence: each orbital $(n, \ell, m_\ell)$ holds at most two electrons, one spin-up and one spin-down.

The $n=1$ shell has $2(1)^2 = 2$ states, $n=2$ has $2(2)^2 = 8$, $n=3$ has $2(3)^2 = 18$ — the row structure of the periodic table.

The exclusion principle also accounts for the spatial extent of matter. Without it, every electron in every atom would occupy the $1s$ ground state, every atom would be hydrogen-sized, and chemistry would not exist. Exclusion is, precisely, the principle that makes matter occupy volume rather than collapse.

---

## What would change my mind

Hydrogen spectroscopy is quantum mechanics' best-tested prediction. Each refinement has added confirmation: the Lamb shift from quantum electrodynamics, hyperfine structure from nuclear spin, fine structure from relativistic corrections — all computed, measured, and matched. The "proton radius puzzle" — a discrepancy between the proton radius from muonic hydrogen [Pohl et al. 2010, *Nature* 466, 213–216](https://doi.org/10.1038/nature09250) and from ordinary electron-hydrogen spectroscopy — looked threatening briefly, but newer measurements [Bezginov et al. 2019, *Science* 365, 1007–1012](https://doi.org/10.1126/science.aau7807) [verify] are converging toward the smaller muonic value. The framework holds. A persistent, reproducible hydrogen line that no extension of the theory can fit would overturn it. None exists.

---

## Still puzzling

The $\mathrm{SO}(4)$ symmetry of the Coulomb potential — the source of hydrogen's energy depending only on $n$, not $\ell$ — reads like a coincidence despite being forced by the $1/r$ form of the potential. Pauli's 1926 derivation makes the algebra explicit and clean without making the symmetry feel inevitable. Why does the inverse-square law carry this extra conserved quantity while a $1/r^2$ potential does not? Classical mechanics gives a clean answer — Bertrand's theorem: only $1/r$ and $r^2$ produce closed orbits — and there is a corresponding quantum answer via the Laplace–Runge–Lenz vector. Both are technically correct and aesthetically unsatisfying. That hydrogen, alone among one-electron atoms, is cleanly soluble feels like a coincidence with a deep reason rather than a deep reason fully understood.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Balmer, J. J. "Notiz über die Spectrallinien des Wasserstoffs." *Annalen der Physik* 261, 80–87 (1885). https://doi.org/10.1002/andp.18852610506
2. Bohr, N. "On the Constitution of Atoms and Molecules." *Philosophical Magazine* (Series 6) 26, 1–25 (1913). https://doi.org/10.1080/14786441308634955
3. Pauli, W. "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik." *Zeitschrift für Physik* 36, 336–363 (1926). https://doi.org/10.1007/BF01450175
4. Gerlach, W. & Stern, O. "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld." *Zeitschrift für Physik* 9, 349–352 (1922). https://doi.org/10.1007/BF01326983
5. Uhlenbeck, G. E. & Goudsmit, S. "Ersetzung der Hypothese vom unmechanischen Zwang..." *Die Naturwissenschaften* 13, 953–954 (1925). https://doi.org/10.1007/BF01558878
6. Dirac, P. A. M. "The Quantum Theory of the Electron." *Proceedings of the Royal Society A* 117, 610–624 (1928). https://doi.org/10.1098/rspa.1928.0023
7. Pauli, W. "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren." *Zeitschrift für Physik* 31, 765–783 (1925). https://doi.org/10.1007/BF02980631
8. Pohl, R. et al. "The size of the proton." *Nature* 466, 213–216 (2010). https://doi.org/10.1038/nature09250
9. Bezginov, N. et al. "A measurement of the atomic hydrogen Lamb shift and the proton charge radius." *Science* 365, 1007–1012 (2019). https://doi.org/10.1126/science.aau7807
10. NIST CODATA 2018: Rydberg constant, Bohr radius. https://physics.nist.gov/cuu/Constants/
11. *Physics Quantum Mechanics Scrap*, Chapter 6, "Spin," reference chapter in `physics-quantum-mechanics-scrap/pantry` and `chapters`, solid-sphere spinning-electron estimate.
