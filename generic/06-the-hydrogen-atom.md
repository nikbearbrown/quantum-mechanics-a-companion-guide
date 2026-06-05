# Chapter 6 — The Hydrogen Atom

## TL;DR

- Take one electron, one proton, and the Coulomb potential between them. The result is the cleanest available check on whether quantum mechanics describes the real world.
- We work through the setup (a central potential and separation of variables), solve the 1s state to see where the numbers come from, take apart the orbit picture, and uncover why Bohr got the energies right through a hidden symmetry.
- Read it for the central argument, the new vocabulary, and the judgment it helps you build.

*One electron, one proton, a Coulomb potential — and the cleanest test we have of whether quantum mechanics is right about the world.*

---

In 1885 a Swiss schoolteacher named Johann Balmer studied hydrogen's emission spectrum — the small set of sharp colored lines hydrogen gives off when it is heated in a discharge tube. He noticed that the wavelengths of those lines obeyed a formula. He did not derive it from any physical principle; he simply recognized the pattern by looking at the numbers:

$$\lambda_n = B \cdot \frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, \ldots$$

with $B \approx 364.5$ nm. [Balmer 1885, *Annalen der Physik* 261, 80–87](https://doi.org/10.1002/andp.18852610506) [verify]. Balmer published the relation and moved on. It worked, and at the time no one could say why.

Almost three decades went by before an explanation arrived.

In 1913 Niels Bohr published a derivation. [Bohr 1913, *Philosophical Magazine* Series 6, 26, 1–25](https://doi.org/10.1080/14786441308634955). His starting assumption was simple and bold: the electron circles the proton, but only certain circular orbits are permitted — those whose angular momentum is an integer multiple of $\hbar$. Combining that single rule with Newton's second law for circular motion under the Coulomb force reproduced Balmer's formula, complete with the correct numerical coefficient. The energy levels came out as

$$E_n = -\frac{13.6\,\text{eV}}{n^2}.$$

The red line at 656 nm, the blue-green at 486 nm, the violet at 434 nm — every one of them was accounted for.

![Hydrogen emission spectrum in the visible range ](../images/06-the-hydrogen-atom-fig-01.png)
*Figure 6.1 — Hydrogen emission spectrum in the visible range *

This was one of the great successes in the history of physics. It was also, as we now understand, the product of a model that is wrong about nearly everything except the energies it predicts. In Bohr's picture the electron follows a definite circular path at a definite radius. That picture is false. Even so, the energies are correct.

How can both things be true? The full answer occupies this chapter. The short version is that the Coulomb potential $V \propto 1/r$ carries a hidden symmetry — one beyond its obvious rotational symmetry — and that hidden symmetry forces every state with the same $n$ to share the same energy, no matter how the state actually behaves. Bohr unknowingly tapped into a consequence of that symmetry. The lucky accident applies only to hydrogen; carry Bohr's method over to helium and it misses by 30%.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-the-hydrogen-atom-assertions.md (specific 30% figure should be sourced; magnitude correct ~30–40%) -->
 So our deep-dive in this chapter is this: solve hydrogen properly, show where $a_0$ and $-13.6\,\text{eV}$ genuinely come from, and use that exact solution to take apart the image of the electron as an orbiting particle.

---

## The setup: central potential, separation of variables

The Hamiltonian for a single electron bound to a single proton is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}.$$

Notice that the potential depends only on $r$ — the distance from the proton — and not on direction. We call a potential with this property a *central potential*. Its directional indifference is exactly what permits us to switch to spherical coordinates and split the Schrödinger equation into a radial part and an angular part.

We assume $\psi(r,\theta,\phi) = R(r) \cdot Y(\theta,\phi)$ and substitute into $\hat{H}\psi = E\psi$. The angular part separates into an eigenvalue equation for the operator $\hat{L}^2/\hbar^2$ acting on the sphere. Its solutions are the spherical harmonics $Y_{\ell m}(\theta,\phi)$, which we derive in Unit 7. Here we simply use the result: they exist, they carry two integer labels $\ell \geq 0$ and $-\ell \leq m \leq \ell$, and they are orthonormal on the sphere. For the $1s$ state we have $\ell = 0$, and the single spherical harmonic with $\ell = 0$ is the constant $Y_{00} = 1/\sqrt{4\pi}$.

Introducing the substitution $u(r) = rR(r)$ turns the radial equation into a one-dimensional problem:

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2m_e r^2}\right]u = Eu.$$

The second term inside the brackets — $\hbar^2\ell(\ell+1)/(2m_e r^2)$ — is the *centrifugal barrier*. It appeared on its own through the separation, with no classical assumption behind it. For electrons with $\ell > 0$, this repulsive $1/r^2$ term holds them away from the nucleus. When $\ell = 0$ the term vanishes, leaving the electron free to have substantial probability right near $r = 0$.

For the $1s$ state, where $\ell = 0$, the radial equation reduces to

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\varepsilon_0 r}u = Eu.$$

![Effective potential energy diagram for the hydrogen radial](../images/06-the-hydrogen-atom-fig-02.png)
*Figure 6.2 — Effective potential energy diagram for the hydrogen radial*

---

## Solving the 1s state: where the numbers come from

We start from the trial form $u(r) = Ar\,e^{-r/a}$, where $A$ is a normalization constant and $a$ is a length scale we still have to pin down. The factor of $r$ is not optional: since $R(r) = u(r)/r$ must stay finite at the origin, we need $u(0) = 0$. The exponential decay guarantees that the function is normalizable.

Differentiating twice gives

$$\frac{du}{dr} = Ae^{-r/a}\!\left(1 - \frac{r}{a}\right), \qquad \frac{d^2u}{dr^2} = Ae^{-r/a}\!\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

We substitute these into the radial equation and divide through by $Ae^{-r/a}$:

$$\frac{\hbar^2}{m_e a} - \frac{\hbar^2 r}{2m_e a^2} - \frac{e^2}{4\pi\varepsilon_0} = Er.$$

Now we group by powers of $r$. Because the equation has to hold for every value of $r$, the constant terms and the terms linear in $r$ must each vanish on their own — giving us two conditions:

**Constant terms:**
$$\frac{\hbar^2}{m_e a} = \frac{e^2}{4\pi\varepsilon_0} \implies a = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \equiv a_0.$$

**Linear-in-$r$ terms:**
$$E = -\frac{\hbar^2}{2m_e a_0^2}.$$

Putting in the numbers gives $E_1 \approx -13.6\,\text{eV}$.

So the Bohr radius $a_0 \approx 5.29 \times 10^{-11}$ m and the ionization energy $13.6\,\text{eV}$ emerge directly from matching the constant and linear pieces of the equation. We postulated no quantization condition and assumed no circular orbits. Our only guess was the trial form $u \propto re^{-r/a}$, and it is self-consistent only when $a = a_0$ and $E = E_1$.

Now we normalize. The full wave function is $\psi_{100} = R_{10}(r) \cdot Y_{00}$, with $R_{10}(r) = Ae^{-r/a_0}$ and $Y_{00} = 1/\sqrt{4\pi}$. The normalization condition $\int|\psi|^2 d^3r = 1$ separates cleanly:

$$\int_0^\infty |R_{10}|^2 r^2\,dr \cdot \int |Y_{00}|^2\,d\Omega = 1.$$

The angular integral equals 1, and the radial integral gives $A = 2/a_0^{3/2}$. The normalized ground-state wave function is therefore

$$\boxed{\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.}$$

![Plot of the 1s radial wave function R₁₀(r)](../images/06-the-hydrogen-atom-fig-03.png)
*Figure 6.3 — Plot of the 1s radial wave function R₁₀(r)*

---

## Dismantling the orbit picture

This is the point where the Bohr model falls apart. Not in its energies — Bohr got those right — but in everything it claims about where the electron actually is.

The *radial probability density* gives the probability of finding the electron in a thin spherical shell of radius $r$ and thickness $dr$:

$$P(r) = |R_{10}(r)|^2 \cdot r^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

The $r^2$ factor is the Jacobian that comes from spherical coordinates. Because there is more volume at larger $r$, a spherical shell of fixed thickness $dr$ grows as you move outward. This geometric growth competes against the decaying exponential.

To find the peak of $P(r)$, we maximize it:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0 \implies r_{\text{mp}} = a_0.$$

So the most probable radius is $a_0$ — and here Bohr was right. But now let us compute the *expectation value* of $r$, the average distance:

$$\langle r\rangle = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr = \frac{4}{a_0^3} \cdot \frac{6}{(2/a_0)^4} = \frac{3a_0}{2}.$$

The most probable radius is $a_0$. The average radius is $\tfrac{3}{2}a_0$.

These two numbers differ because the distribution is lopsided: $P(r)$ peaks at $a_0$ but trails off in a long tail toward larger $r$, and that tail drags the average upward. If the electron really moved on a circular orbit at radius $a_0$, there would be only one radius, and "most probable" and "average" would both come out to $a_0$. Their disagreement is the mathematical fingerprint of an electron spread across a distribution of radii rather than fixed at one. There is no orbit. There is a probability cloud.

![The orbit picture requires both markers to be at the same place. They are not.](../images/06-the-hydrogen-atom-fig-04.png)
*Figure 6.4 — P(r) = (4/a₀³)r²e^{−2r/a₀} plotted vs r/a₀ from 0*

Nor is there any instant at which the electron sits at a definite radius, moving at a definite speed in a definite direction. What exists instead is $|\psi_{100}|^2$ — a spherically symmetric cloud that falls off exponentially away from the nucleus. The quantity $a_0$ shows up in that cloud as its length scale. Bohr found the right length scale by assuming a circular orbit. He was fortunate: the length scale is real; the orbit is not.

---

## Why Bohr got the energies right: the hidden symmetry

The fact that Bohr's wrong model still delivered the right energies has a structural explanation. The Coulomb potential $V = -e^2/(4\pi\varepsilon_0 r)$ has more symmetry than meets the eye. On top of the rotational symmetry $\mathrm{SO}(3)$ — the potential looks identical from every direction — the $1/r$ potential carries a second conserved quantity: the Laplace–Runge–Lenz vector, which points along the major axis of the classical elliptical orbit and keeps a constant magnitude. Taken together, the symmetries of the Coulomb problem form the group $\mathrm{SO}(4)$.

In early 1926 Wolfgang Pauli exploited this symmetry to solve hydrogen algebraically, before Schrödinger's wave-mechanical solution appeared. [Pauli 1926, *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify pages]. The consequence of $\mathrm{SO}(4)$ is that a hydrogen state's energy depends only on the principal quantum number $n$, not on $\ell$. States that share the same $n$ but differ in $\ell$ — $2s$ and $2p$, say — have precisely the same energy. We call this *accidental degeneracy*, though the name misleads: nothing about it is accidental, since the symmetry forces it.

Bohr's quantization condition $L = n\hbar$ is wrong about angular momentum — the true eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, and $\ell$ can run anywhere from $0$ to $n-1$. But since the energy depends only on $n$ and not on $\ell$, Bohr's energy formula turns out to be accidentally correct. Apply the same method to helium — two electrons, no clean $\mathrm{SO}(4)$ symmetry, no accidental degeneracy — and the model misses by about 30%. The success was hydrogen-specific from the start.

---

## The four quantum numbers

Every hydrogen state carries four quantum numbers.

The *principal quantum number* $n = 1, 2, 3, \ldots$ sets the energy: $E_n = -13.6\,\text{eV}/n^2$. It is the eigenvalue label for $\hat{H}$.

The *orbital angular momentum quantum number* $\ell = 0, 1, \ldots, n-1$ sets the magnitude of the orbital angular momentum: $\hat{L}^2\psi = \hbar^2\ell(\ell+1)\psi$. The spectroscopic letters $s, p, d, f$ stand for $\ell = 0, 1, 2, 3$ respectively — a holdover from pre-quantum spectroscopy ("sharp, principal, diffuse, fundamental") kept purely by convention.

The *magnetic quantum number* $m_\ell = -\ell, -\ell+1, \ldots, +\ell$ sets the projection of orbital angular momentum onto a chosen axis: $\hat{L}_z\psi = m_\ell\hbar\psi$.

The *spin quantum number* $m_s = \pm 1/2$ sets the projection of spin angular momentum: $\hat{S}_z\psi = m_s\hbar\psi$.

The total number of states at energy level $n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2 \quad\text{(without spin)}, \qquad 2n^2 \quad\text{(with spin)}.$$

The $n^2$ factor is a direct consequence of the $\mathrm{SO}(4)$ degeneracy. The $n=1$ shell holds 2 electrons; the $n=2$ shell holds 8; the $n=3$ shell holds 18. These are the row capacities of the periodic table — set by quantum mechanics and Pauli, not by chemistry.

| $n$ | $\ell$ values | spectroscopic labels | $m_\ell$ values | orbitals | states with spin |
| --- | --- | --- | --- | ---: | ---: |
| 1 | 0 | 1s | 0 | 1 | 2 |
| 2 | 0, 1 | 2s, 2p | 0; -1, 0, +1 | 4 | 8 |
| 3 | 0, 1, 2 | 3s, 3p, 3d | 0; -1, 0, +1; -2, -1, 0, +1, +2 | 9 | 18 |
| 4 | 0, 1, 2, 3 | 4s, 4p, 4d, 4f | $m_\ell=-\ell,\ldots,+\ell$ | 16 | 32 |

One vocabulary correction before we go on: the word "orbital" does not mean "orbit." An orbital — the spherical $s$ cloud, the dumbbell-shaped $p$, the four-lobed $d$ — is an isocontour of $|\psi_{n\ell m}|^2$, usually drawn as the surface enclosing 90% of the probability. It tells us where the electron is *likely to be found if we measure it*. It says nothing about what the electron does between measurements, because quantum mechanics tells no between-measurements story at all. The orbital shape is everything; the trajectory is nothing.

![90%-probability isosurface renderings of the 1s, 2s, 2p_z,](../images/06-the-hydrogen-atom-fig-05.png)
*Figure 6.5 — 90%-probability isosurface renderings of the 1s, 2s, 2p_z,*

---

## Spin: the internal angular momentum that cannot be rotation

In 1922 Otto Stern and Walther Gerlach passed a beam of neutral silver atoms through an inhomogeneous magnetic field. Classically, atoms whose magnetic moments point in all directions should smear out continuously across the detector. Instead they saw two discrete spots. [Stern & Gerlach 1922, *Zeitschrift für Physik* 9, 349–352](https://doi.org/10.1007/BF01326983) [verify pages].

Silver carries one unpaired electron in a $5s$ state. The two spots correspond to the two projections of that electron's spin onto the magnetic-field axis: $S_z = +\hbar/2$ and $S_z = -\hbar/2$. Two outcomes, not a continuum.

![Two spots where classical physics predicts a smear. The discreteness is spin.](../images/06-the-hydrogen-atom-fig-06.png)
*Figure 6.6 — Stern-Gerlach apparatus diagram *

A historical note is worth making here. Stern and Gerlach in 1922 did not read their result as electron spin, because spin had not yet been proposed. They believed they were observing "space quantization" of orbital angular momentum. The correct interpretation — that the splitting traces to the spin of the unpaired $5s$ electron — arrived only after Uhlenbeck and Goudsmit introduced the idea of intrinsic electron spin in 1925. [Uhlenbeck & Goudsmit 1925, *Die Naturwissenschaften* 13, 953–954](https://doi.org/10.1007/BF01558878) [verify]. The experiment ran three years before anyone understood what it was measuring.

So what is spin? It is intrinsic angular momentum. Every electron carries angular momentum of magnitude $\sqrt{s(s+1)}\hbar = (\sqrt{3}/2)\hbar$ with $s = 1/2$, and that is all there is to it. It is not angular momentum produced by motion through space. It is a property the electron simply has, in the same way it has charge or mass. The Dirac equation — the relativistic counterpart of the Schrödinger equation — generates spin automatically: insist that a quantum wave equation be Lorentz-invariant, and spin-1/2 emerges as an algebraic necessity. [Dirac 1928, *Proceedings of the Royal Society A* 117, 610–624](https://doi.org/10.1098/rspa.1928.0023). You do not put spin in by hand; you cannot keep it out.

The familiar alternative explanation — that the electron is a tiny spinning ball — can be ruled out with a single calculation. Suppose the electron is a uniform solid sphere of radius $r_e$ spinning about its axis. For a solid sphere, $I = \frac{2}{5}m_er_e^2$, so for the angular momentum to equal $\hbar/2$ the equatorial speed would have to be

$$v = \omega r_e = \frac{Lr_e}{I} = \frac{5\hbar}{4m_e r_e}.$$

The classical electron radius — estimated by setting the electron's rest-mass energy equal to its electrostatic self-energy — is $r_e \approx 2.82 \times 10^{-15}$ m. Substituting:

$$v \approx \frac{5(1.055\times10^{-34})}{4(9.11\times10^{-31})(2.82\times10^{-15})} \approx 5.1 \times 10^{10}\,\text{m/s}.$$

That is roughly 170 times the speed of light, matching the solid-sphere estimate used in the reference spin chapter. If the electron is smaller than $r_e$ — and experiment constrains it to be pointlike down to at least $10^{-18}$ m — the required speed becomes vastly larger still. The classical spinning-ball picture is not merely imprecise. It is geometrically impossible.

The picture lingers in introductory texts because it is convenient shorthand. The calculation above should be enough to set it aside.

---

## The Pauli exclusion principle

In 1925, before the Schrödinger equation existed, Pauli proposed that no two electrons in an atom can share all four quantum numbers $(n, \ell, m_\ell, m_s)$. [Pauli 1925, *Zeitschrift für Physik* 31, 765–783](https://doi.org/10.1007/BF02980631). He reached this conclusion by studying the patterns in atomic spectra — which shells fill with how many electrons, and what rules govern which spectral lines appear. The principle fit all the data, even though he did not yet know why.

The deeper explanation, which we develop in Unit 8, is that electrons are fermions: their multi-particle wave function must be antisymmetric under exchange of any two particles, $\psi(1,2) = -\psi(2,1)$. If two electrons occupied the same state, the wave function would have to equal its own negative and therefore be zero — meaning no such state exists. The exclusion principle is a corollary of this. For now we only need its consequence: each orbital, labeled by $(n, \ell, m_\ell)$, holds at most two electrons — one spin-up and one spin-down.

The $n=1$ shell has $2(1)^2 = 2$ states. The $n=2$ shell has $2(2)^2 = 8$. The $n=3$ shell has $2(3)^2 = 18$. This is the row structure of the periodic table.

There is a more fundamental point as well. The reason solid matter takes up space, the reason your hand does not pass through the table, the reason atoms have size — all of it traces back to Pauli. Without the exclusion principle, every electron in every atom would collapse into the $1s$ ground state, and every atom would be the size of hydrogen. Chemistry would not exist. In a precise sense, the exclusion principle is the principle that the material world consists of solid objects rather than collapsing blobs.

---

## What would change my mind

Hydrogen spectroscopy is quantum mechanics' best-tested prediction. Every refinement has only added more confirmation: the Lamb shift from quantum electrodynamics, the hyperfine structure from nuclear spin, the fine structure from relativistic corrections — all computed, all measured, all in agreement. The "proton radius puzzle" — a discrepancy between the proton radius inferred from muonic hydrogen [Pohl et al. 2010, *Nature* 466, 213–216](https://doi.org/10.1038/nature09250) and from ordinary electron-hydrogen spectroscopy — looked threatening for a few years, but more recent measurements [Bezginov et al. 2019, *Science* 365, 1007–1012](https://doi.org/10.1126/science.aau7807) [verify] are converging toward the smaller muonic value. The framework holds. What would shake it: a hydrogen spectral line that no extension of the current theory can fit, persistently and reproducibly. We do not have one.

---

## Still puzzling

The $\mathrm{SO}(4)$ symmetry of the Coulomb potential — the hidden symmetry that makes hydrogen's energy depend only on $n$, not on $\ell$ — still feels like a coincidence even though it is mathematically forced by the $1/r$ form of the potential. Pauli's 1926 derivation lays the algebra out explicitly and cleanly. What it does not do is make the symmetry feel inevitable. Why does the inverse-square law carry this extra conserved quantity while a $1/r^2$ potential, say, does not? Classical mechanics offers a clean answer — Bertrand's theorem, which states that the only potentials producing closed orbits are $1/r$ and $r^2$ — and quantum mechanics offers a matching answer involving the Laplace–Runge–Lenz vector. Both explanations are technically correct, and both leave me somehow aesthetically unsatisfied. The fact that hydrogen, alone among the one-electron atoms, is cleanly soluble feels like a coincidence with a deep reason behind it rather than a deep reason I have fully grasped.

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
