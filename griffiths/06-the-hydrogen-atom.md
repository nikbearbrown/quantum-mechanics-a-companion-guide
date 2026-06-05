# Chapter 6 — The Hydrogen Atom


## TL;DR

- One electron, one proton, a Coulomb potential. It is the cleanest test we have of whether quantum mechanics describes the world, and it passes.
- We set up the central potential, separate variables, solve the 1s state from scratch, take apart the orbit picture, and trace why Bohr got the energies right by accident.
- Read it for the argument, the vocabulary, and the judgment it asks you to develop.

*One electron, one proton, a Coulomb potential — and the cleanest test we have of whether quantum mechanics is right about the world.*

---

In 1885 a Swiss schoolteacher named Johann Balmer looked at hydrogen's emission spectrum — the few sharp colored lines hydrogen throws off when you heat it in a discharge tube — and found that the wavelengths obeyed a formula. He did not derive it. He noticed it:

$$\lambda_n = B \cdot \frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, \ldots$$

with $B \approx 364.5$ nm. [Balmer 1885, *Annalen der Physik* 261, 80–87](https://doi.org/10.1002/andp.18852610506) [verify]. He published it and walked away. The formula worked. Nobody could say why.

Twenty-eight years went by.

Then in 1913 Niels Bohr supplied a derivation. [Bohr 1913, *Philosophical Magazine* Series 6, 26, 1–25](https://doi.org/10.1080/14786441308634955). The postulate was blunt: the electron circles the proton, but only on certain orbits — the ones where angular momentum is an integer times $\hbar$. With that single rule and Newton's second law for circular motion under the Coulomb force, Balmer's formula came out, coefficient and all. The energies were

$$E_n = -\frac{13.6\,\text{eV}}{n^2}.$$

The red line at 656 nm, the blue-green at 486 nm, the violet at 434 nm — every one of them, correct.

![Hydrogen emission spectrum in the visible range ](../images/06-the-hydrogen-atom-fig-01.png)
*Figure 6.1 — Hydrogen emission spectrum in the visible range *

It was one of the great triumphs in the history of physics. It was also, we now understand, built on a model that is wrong about nearly everything except the energies. Bohr's electron follows a definite circular path at a definite radius. That picture is false. The energies are right anyway.

How can that be? The whole answer is what this chapter is about. The short version: the Coulomb potential $V \propto 1/r$ carries a hidden symmetry — over and above the obvious rotational one — that pins every state of a given $n$ to the same energy, no matter how the state actually behaves. Bohr blundered into a consequence of that symmetry without suspecting it was there. The accident is hydrogen's alone; try Bohr's recipe on helium and it misses by 30%.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-the-hydrogen-atom-assertions.md (specific 30% figure should be sourced; magnitude correct ~30–40%) -->
 The deep dive here is to solve hydrogen honestly, show where $a_0$ and $-13.6\,\text{eV}$ actually originate, and use the exact solution to dismantle the picture of the electron as an orbiting particle.

---

## The setup: central potential, separation of variables

One electron bound to one proton has the Hamiltonian

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}.$$

The potential depends on $r$ alone — distance from the proton — not on direction. That is what *central potential* means, and it is our license to switch to spherical coordinates and split the Schrödinger equation into a radial part and an angular part.

Write $\psi(r,\theta,\phi) = R(r) \cdot Y(\theta,\phi)$ and feed it into $\hat{H}\psi = E\psi$. The angular piece separates off as an eigenvalue equation for $\hat{L}^2/\hbar^2$ on the sphere. Its solutions are the spherical harmonics $Y_{\ell m}(\theta,\phi)$, derived in Unit 7. Here we just borrow the result: they exist, they carry two integer labels $\ell \geq 0$ and $-\ell \leq m \leq \ell$, and they are orthonormal on the sphere. The $1s$ state has $\ell = 0$, and the lone spherical harmonic with $\ell = 0$ is the constant $Y_{00} = 1/\sqrt{4\pi}$.

The radial equation, after the substitution $u(r) = rR(r)$ that turns it into a one-dimensional problem, reads

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2m_e r^2}\right]u = Eu.$$

The second bracketed term, $\hbar^2\ell(\ell+1)/(2m_e r^2)$, is the *centrifugal barrier*. It dropped out of the separation on its own; nothing classical was assumed. For $\ell > 0$ this repulsive $1/r^2$ term holds electrons off the nucleus. For $\ell = 0$ it is gone, and the electron can pile up significant probability right at $r = 0$.

With $\ell = 0$ the radial equation collapses to

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\varepsilon_0 r}u = Eu.$$

![Effective potential energy diagram for the hydrogen radial](../images/06-the-hydrogen-atom-fig-02.png)
*Figure 6.2 — Effective potential energy diagram for the hydrogen radial*

---

## Solving the 1s state: where the numbers come from

Guess $u(r) = Ar\,e^{-r/a}$, with $A$ a normalization constant and $a$ a length scale yet to be fixed. The factor of $r$ is forced: $R(r) = u(r)/r$ has to stay finite at the origin, so $u(0) = 0$. The exponential keeps things normalizable.

Differentiate twice:

$$\frac{du}{dr} = Ae^{-r/a}\!\left(1 - \frac{r}{a}\right), \qquad \frac{d^2u}{dr^2} = Ae^{-r/a}\!\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

Drop these into the radial equation and divide out $Ae^{-r/a}$:

$$\frac{\hbar^2}{m_e a} - \frac{\hbar^2 r}{2m_e a^2} - \frac{e^2}{4\pi\varepsilon_0} = Er.$$

Sort by powers of $r$. The equation has to hold for every $r$, so the constant terms and the $r$-linear terms must each vanish on their own:

**Constant terms:**
$$\frac{\hbar^2}{m_e a} = \frac{e^2}{4\pi\varepsilon_0} \implies a = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \equiv a_0.$$

**Linear-in-$r$ terms:**
$$E = -\frac{\hbar^2}{2m_e a_0^2}.$$

Put in numbers: $E_1 \approx -13.6\,\text{eV}$.

The Bohr radius $a_0 \approx 5.29 \times 10^{-11}$ m and the ionization energy $13.6\,\text{eV}$ fall straight out of matching the constant and linear pieces. No quantization condition was imposed. No orbits. The one guess we made was $u \propto re^{-r/a}$, and it is self-consistent only when $a = a_0$ and $E = E_1$.

Normalize. The full wave function is $\psi_{100} = R_{10}(r) \cdot Y_{00}$, with $R_{10}(r) = Ae^{-r/a_0}$ and $Y_{00} = 1/\sqrt{4\pi}$. The condition $\int|\psi|^2 d^3r = 1$ factors:

$$\int_0^\infty |R_{10}|^2 r^2\,dr \cdot \int |Y_{00}|^2\,d\Omega = 1.$$

The angular integral is 1. The radial integral gives $A = 2/a_0^{3/2}$. The normalized ground state is

$$\boxed{\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.}$$

![Plot of the 1s radial wave function R₁₀(r)](../images/06-the-hydrogen-atom-fig-03.png)
*Figure 6.3 — Plot of the 1s radial wave function R₁₀(r)*

---

## Dismantling the orbit picture

This is where the Bohr model falls apart. Not in the energy — Bohr nailed the energy — but in everything it asserts about where the electron sits.

The *radial probability density* — the chance of finding the electron in a thin spherical shell of radius $r$ and thickness $dr$ — is

$$P(r) = |R_{10}(r)|^2 \cdot r^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

The $r^2$ is the spherical Jacobian. There is more room at large $r$, so a shell of fixed thickness $dr$ grows as you move outward. That geometric factor pulls against the decaying exponential.

Maximize $P(r)$:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0 \implies r_{\text{mp}} = a_0.$$

The most probable radius is $a_0$. Bohr got this one right. But now take the *expectation value* of $r$ — the average distance:

$$\langle r\rangle = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr = \frac{4}{a_0^3} \cdot \frac{6}{(2/a_0)^4} = \frac{3a_0}{2}.$$

Most probable radius: $a_0$. Average radius: $\tfrac{3}{2}a_0$.

The two numbers differ because the distribution is lopsided. $P(r)$ peaks at $a_0$ but trails off into a long tail at large $r$, and that tail drags the mean upward. An electron on a circular orbit of radius $a_0$ would have exactly one radius, and "most probable" and "average" would coincide. That they do not coincide is the mathematical fingerprint of an electron spread over a range of radii rather than parked at one. There is no orbit. There is a probability cloud.

![The orbit picture requires both markers to be at the same place. They are not.](../images/06-the-hydrogen-atom-fig-04.png)
*Figure 6.4 — P(r) = (4/a₀³)r²e^{−2r/a₀} plotted vs r/a₀ from 0*

Nor is there any moment at which the electron sits at a definite radius, moving at a definite speed in a definite direction. What exists is $|\psi_{100}|^2$ — a spherically symmetric cloud that falls off exponentially from the nucleus. The quantity $a_0$ shows up in that cloud as a length scale. Bohr recovered the right length scale by assuming a circular orbit. He got lucky: the length scale is real; the orbit is not.

---

## Why Bohr got the energies right: the hidden symmetry

The coincidence — a wrong model producing the right energies — has a structural cause. The Coulomb potential $V = -e^2/(4\pi\varepsilon_0 r)$ has more symmetry than meets the eye. Beyond the rotational symmetry $\mathrm{SO}(3)$ (the potential looks identical from every direction), the $1/r$ potential conserves a second quantity: the Laplace–Runge–Lenz vector, which points along the major axis of the classical elliptical orbit and keeps a constant magnitude. The full symmetry group of the Coulomb problem is $\mathrm{SO}(4)$.

Wolfgang Pauli exploited this in early 1926 to solve hydrogen algebraically, before Schrödinger's wave-mechanical solution turned up. [Pauli 1926, *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify pages]. The upshot of $\mathrm{SO}(4)$ is that a hydrogen state's energy depends only on the principal quantum number $n$, not on $\ell$. States with the same $n$ and different $\ell$ — $2s$ and $2p$, say — have exactly the same energy. This goes by the name *accidental degeneracy*, a poor choice of words: nothing accidental about it, the symmetry forces it.

Bohr's quantization $L = n\hbar$ is wrong about angular momentum — the true eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, with $\ell$ running from $0$ to $n-1$. But because the energy hangs on $n$ alone and ignores $\ell$, his energy formula comes out accidentally correct. Run his method on helium — two electrons, no clean $\mathrm{SO}(4)$, no accidental degeneracy — and it misses by about 30%. The success was always hydrogen's alone.

---

## The four quantum numbers

Four quantum numbers label every hydrogen state.

The *principal quantum number* $n = 1, 2, 3, \ldots$ fixes the energy: $E_n = -13.6\,\text{eV}/n^2$. It is the eigenvalue label for $\hat{H}$.

The *orbital angular momentum quantum number* $\ell = 0, 1, \ldots, n-1$ fixes the magnitude of orbital angular momentum: $\hat{L}^2\psi = \hbar^2\ell(\ell+1)\psi$. The spectroscopic letters $s, p, d, f$ stand for $\ell = 0, 1, 2, 3$ — leftovers from pre-quantum spectroscopy ("sharp, principal, diffuse, fundamental"), kept by pure convention.

The *magnetic quantum number* $m_\ell = -\ell, -\ell+1, \ldots, +\ell$ fixes the projection of orbital angular momentum on a chosen axis: $\hat{L}_z\psi = m_\ell\hbar\psi$.

The *spin quantum number* $m_s = \pm 1/2$ fixes the projection of spin: $\hat{S}_z\psi = m_s\hbar\psi$.

The total count of states at level $n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2 \quad\text{(without spin)}, \qquad 2n^2 \quad\text{(with spin)}.$$

The $n^2$ is a direct consequence of the $\mathrm{SO}(4)$ degeneracy. The $n=1$ shell holds 2 electrons; $n=2$, 8; $n=3$, 18. Those are the row capacities of the periodic table — set by quantum mechanics and Pauli, not by chemistry.

| $n$ | $\ell$ values | spectroscopic labels | $m_\ell$ values | orbitals | states with spin |
| --- | --- | --- | --- | ---: | ---: |
| 1 | 0 | 1s | 0 | 1 | 2 |
| 2 | 0, 1 | 2s, 2p | 0; -1, 0, +1 | 4 | 8 |
| 3 | 0, 1, 2 | 3s, 3p, 3d | 0; -1, 0, +1; -2, -1, 0, +1, +2 | 9 | 18 |
| 4 | 0, 1, 2, 3 | 4s, 4p, 4d, 4f | $m_\ell=-\ell,\ldots,+\ell$ | 16 | 32 |

One correction in terminology before we go on: "orbital" does not mean "orbit." An orbital — the spherical $s$ cloud, the dumbbell $p$, the four-lobed $d$ — is an isocontour of $|\psi_{n\ell m}|^2$, usually drawn at the surface enclosing 90% of the probability. It tells you where the electron is *likely to be found if measured*. It says nothing about what the electron does between measurements, because quantum mechanics tells no such story. The shape is everything; the trajectory is nothing.

![90%-probability isosurface renderings of the 1s, 2s, 2p_z,](../images/06-the-hydrogen-atom-fig-05.png)
*Figure 6.5 — 90%-probability isosurface renderings of the 1s, 2s, 2p_z,*

---

## Spin: the internal angular momentum that cannot be rotation

In 1922 Otto Stern and Walther Gerlach fired a beam of neutral silver atoms through a non-uniform magnetic field. Classically, atoms with magnetic moments at every orientation ought to smear out across the detector. What appeared was two discrete spots. [Stern & Gerlach 1922, *Zeitschrift für Physik* 9, 349–352](https://doi.org/10.1007/BF01326983) [verify pages].

Silver has one unpaired electron in a $5s$ state. The two spots are the two projections of that electron's spin onto the field axis: $S_z = +\hbar/2$ and $S_z = -\hbar/2$. Two outcomes, not a continuum.

![Two spots where classical physics predicts a smear. The discreteness is spin.](../images/06-the-hydrogen-atom-fig-06.png)
*Figure 6.6 — Stern-Gerlach apparatus diagram *

A historical point worth making: Stern and Gerlach in 1922 did not read their result as electron spin. Spin had not been proposed yet. They thought they were watching "space quantization" of orbital angular momentum. The right reading — that the splitting comes from the spin of the unpaired $5s$ electron — arrived only after Uhlenbeck and Goudsmit proposed intrinsic electron spin in 1925. [Uhlenbeck & Goudsmit 1925, *Die Naturwissenschaften* 13, 953–954](https://doi.org/10.1007/BF01558878) [verify]. The experiment ran three years before anyone knew what it had measured.

So what is spin? Intrinsic angular momentum. Every electron carries angular momentum of magnitude $\sqrt{s(s+1)}\hbar = (\sqrt{3}/2)\hbar$ with $s = 1/2$, full stop. It is not angular momentum from motion through space. It is a property of the electron the way charge or mass is. The Dirac equation — the relativistic Schrödinger equation — generates spin on its own: demand that a quantum wave equation be Lorentz-invariant, and spin-1/2 drops out as an algebraic necessity. [Dirac 1928, *Proceedings of the Royal Society A* 117, 610–624](https://doi.org/10.1098/rspa.1928.0023). You do not put spin in; you cannot keep it out.

The usual alternative — the electron as a tiny spinning ball — dies to a single calculation. Model the electron as a uniform solid sphere of radius $r_e$ spinning on its axis. For a solid sphere $I = \frac{2}{5}m_er_e^2$, so for the angular momentum to equal $\hbar/2$ the equatorial speed would have to be

$$v = \omega r_e = \frac{Lr_e}{I} = \frac{5\hbar}{4m_e r_e}.$$

The classical electron radius — set by equating the electron's rest-mass energy to its electrostatic self-energy — is $r_e \approx 2.82 \times 10^{-15}$ m. Substitute:

$$v \approx \frac{5(1.055\times10^{-34})}{4(9.11\times10^{-31})(2.82\times10^{-15})} \approx 5.1 \times 10^{10}\,\text{m/s}.$$

That is roughly 170 times the speed of light, matching the solid-sphere estimate from the reference spin chapter. Make the electron smaller than $r_e$ — and experiment pins it as pointlike down to at least $10^{-18}$ m — and the required speed grows beyond absurdity. The classical spinning-ball picture is not merely sloppy. It is geometrically impossible.

The picture survives in introductory texts because it is handy shorthand. The calculation above should be enough to retire it.

---

## The Pauli exclusion principle

In 1925, before the Schrödinger equation existed, Pauli proposed that no two electrons in an atom can share all four quantum numbers $(n, \ell, m_\ell, m_s)$. [Pauli 1925, *Zeitschrift für Physik* 31, 765–783](https://doi.org/10.1007/BF02980631). He reached it by studying patterns in atomic spectra — which shells fill with how many electrons, which lines exist. The rule fit every datum. He had no idea yet why.

The deeper account, developed in Unit 8, is that electrons are fermions: their many-particle wave function must be antisymmetric under exchange of any two, $\psi(1,2) = -\psi(2,1)$. Put two electrons in the same state and the wave function has to equal its own negative, hence vanish — so no such state exists. Exclusion is a corollary. Here we need only the consequence: each orbital, labeled by $(n, \ell, m_\ell)$, holds at most two electrons, one spin-up and one spin-down.

The $n=1$ shell has $2(1)^2 = 2$ states. The $n=2$ shell has $2(2)^2 = 8$. The $n=3$ shell has $2(3)^2 = 18$. That is the row structure of the periodic table.

More fundamentally: the reason solid matter takes up room, the reason your hand does not pass through the table, the reason atoms have size — all of it traces to Pauli. Drop the exclusion principle and every electron in every atom would collapse into the $1s$ ground state, and every atom would be the size of hydrogen. Chemistry would not exist. The exclusion principle is, in a precise sense, the principle that the material world is built out of solid objects rather than collapsing blobs.

---

## What would change my mind

Hydrogen spectroscopy is quantum mechanics' best-tested prediction. Every refinement has added confirmation: the Lamb shift from quantum electrodynamics, the hyperfine structure from nuclear spin, the fine structure from relativistic corrections — all computed, all measured, all in agreement. The "proton radius puzzle" — a mismatch between the proton radius from muonic hydrogen [Pohl et al. 2010, *Nature* 466, 213–216](https://doi.org/10.1038/nature09250) and from ordinary electron-hydrogen spectroscopy — looked threatening for a few years, but newer measurements [Bezginov et al. 2019, *Science* 365, 1007–1012](https://doi.org/10.1126/science.aau7807) [verify] are settling toward the smaller muonic value. The framework holds. What would shake it: a hydrogen line that no extension of the current theory can fit, persistently and reproducibly. We do not have one.

---

## Still puzzling

The $\mathrm{SO}(4)$ symmetry of the Coulomb potential — the hidden symmetry that makes hydrogen's energy depend on $n$ alone, not $\ell$ — still feels like a coincidence, even though the $1/r$ form forces it mathematically. Pauli's 1926 derivation lays the algebra out, clean and explicit. It does not make the symmetry feel inevitable. Why does the inverse-square law come with this extra conserved quantity when, say, a $1/r^2$ potential does not? Classical mechanics has a clean answer — Bertrand's theorem, which says the only potentials producing closed orbits are $1/r$ and $r^2$ — and there is a matching quantum answer through the Laplace–Runge–Lenz vector. I find both technically correct and somehow aesthetically unsatisfying. That hydrogen, and only hydrogen among the one-electron atoms, is cleanly soluble feels like a coincidence with a deep reason behind it rather than a deep reason I fully grasp.

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
