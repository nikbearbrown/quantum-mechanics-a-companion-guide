# Chapter 6 — The Hydrogen Atom

## TL;DR

- Take the simplest thing the universe builds — one electron, one proton, the pull between them — and ask whether our theory can really account for it. This is the cleanest test we have.
- Watch the argument move: set up the central potential and split it apart, solve the 1s state and find where the famous numbers hide, take apart the picture of the electron going around in a circle, and uncover the secret symmetry that let Bohr stumble onto the right energies.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*One electron, one proton, a Coulomb potential — and the cleanest test we have of whether quantum mechanics is right about the world.*

---

Picture a Swiss schoolteacher in 1885, Johann Balmer, leaning over hydrogen's emission spectrum. Heat hydrogen in a discharge tube and it answers with a handful of sharp colored lines — just a few, always in the same places. Balmer did something nobody asks a schoolteacher to do. He stared at those wavelengths until he saw they obeyed a formula. Not a formula he derived from any law of nature. A pattern. Found by looking:

$$\lambda_n = B \cdot \frac{n^2}{n^2 - 4}, \qquad n = 3, 4, 5, \ldots$$

with $B \approx 364.5$ nm. [Balmer 1885, *Annalen der Physik* 261, 80–87](https://doi.org/10.1002/andp.18852610506) [verify]. He published it. He moved on. The thing worked beautifully, and nobody on Earth knew why.

Twenty-eight years went by.

Then, in 1913, Niels Bohr handed over a derivation. [Bohr 1913, *Philosophical Magazine* Series 6, 26, 1–25](https://doi.org/10.1080/14786441308634955). And his rule was almost outrageous in its bluntness: the electron circles the proton, but only certain circles are permitted — the ones where the angular momentum comes out to a whole number of $\hbar$. Feed that one postulate into Newton's second law for a charge going around a circle under the Coulomb pull, and out tumbles Balmer's formula with the right number in front. The energy levels were

$$E_n = -\frac{13.6\,\text{eV}}{n^2}.$$

The red line at 656 nm, the blue-green at 486 nm, the violet at 434 nm — every one of them, right where it should be.

![Hydrogen emission spectrum in the visible range ](../images/06-the-hydrogen-atom-fig-01.png)
*Figure 6.1 — Hydrogen emission spectrum in the visible range *

That was one of the great triumphs in all of physics. And here is the strange part — the part worth sitting with. We now know Bohr's model is wrong about nearly everything except the very numbers it nailed. His electron rides a definite circle at a definite radius. That picture is simply false. And yet the energies are dead right.

Now how can that be? A wrong picture giving right answers — that should make you uneasy. It made me uneasy. The full answer is what this whole chapter is for. But here is the short version, so you can carry the puzzle while we work: the Coulomb potential, the gentle $V \propto 1/r$, hides an extra symmetry — more than the obvious "it looks the same in every direction" — and that hidden symmetry forces every state with the same $n$ to share the same energy, no matter what the electron is actually doing. Bohr tripped over a consequence of a symmetry he never knew was there. And the luck runs out fast: try his trick on helium and it misses by 30%.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/06-the-hydrogen-atom-assertions.md (specific 30% figure should be sourced; magnitude correct ~30–40%) -->
 So that is the deep dive of this chapter: solve hydrogen honestly, watch where $a_0$ and $-13.6\,\text{eV}$ genuinely come from, and use the real solution to dismantle, piece by piece, the idea of the electron as a little planet on an orbit.

---

## The setup: central potential, separation of variables

Start with the energy operator for one electron held by one proton:

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}.$$

Look at what the potential depends on. Only $r$ — how far you are from the proton — and not which way you point. That is what we mean by a *central potential*. And that single fact is a gift: it gives us permission to switch to spherical coordinates and split the Schrödinger equation cleanly into a part about radius and a part about direction.

So guess that the wave function factors, $\psi(r,\theta,\phi) = R(r) \cdot Y(\theta,\phi)$, and push it into $\hat{H}\psi = E\psi$. The angular piece peels off on its own as an eigenvalue equation for the operator $\hat{L}^2/\hbar^2$ living on the sphere. Its solutions are the spherical harmonics $Y_{\ell m}(\theta,\phi)$, which Unit 7 builds from scratch. For now we just take them as given: they exist, two integers tag them — $\ell \geq 0$ and $-\ell \leq m \leq \ell$ — and they are orthonormal on the sphere. For the $1s$ state we have $\ell = 0$, and the lone spherical harmonic with $\ell = 0$ is simply the constant $Y_{00} = 1/\sqrt{4\pi}$.

The radial piece, after the clever substitution $u(r) = rR(r)$ that quietly turns it into a one-dimensional problem, reads

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} + \left[-\frac{e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2\ell(\ell+1)}{2m_e r^2}\right]u = Eu.$$

Now look hard at that second term in the brackets — $\hbar^2\ell(\ell+1)/(2m_e r^2)$ — because it appeared out of nowhere. We did not put it in by hand. It fell out of the separation itself. It is the *centrifugal barrier*, and it pushes back. For electrons with $\ell > 0$, this repulsive $1/r^2$ wall keeps them away from the nucleus. But for $\ell = 0$ the barrier vanishes entirely, and the electron is perfectly free to have a real, sizable chance of being found right near $r = 0$. Keep that in mind — it is going to matter.

For the $1s$ state ($\ell = 0$) the radial equation simplifies to

$$-\frac{\hbar^2}{2m_e}\frac{d^2u}{dr^2} - \frac{e^2}{4\pi\varepsilon_0 r}u = Eu.$$

![Effective potential energy diagram for the hydrogen radial](../images/06-the-hydrogen-atom-fig-02.png)
*Figure 6.2 — Effective potential energy diagram for the hydrogen radial*

---

## Solving the 1s state: where the numbers come from

Let's guess. That is honestly how this goes — you guess a shape and check whether the equation will accept it. Try $u(r) = Ar\,e^{-r/a}$, with $A$ a normalization constant and $a$ a length we do not yet know. Why that factor of $r$ out front? Because $R(r) = u(r)/r$ has to stay finite at the origin, which means $u(0) = 0$. And why the decaying exponential? Because the electron has to be somewhere — the wave function must be normalizable, so it had better die off far away.

Take two derivatives:

$$\frac{du}{dr} = Ae^{-r/a}\!\left(1 - \frac{r}{a}\right), \qquad \frac{d^2u}{dr^2} = Ae^{-r/a}\!\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

Drop these into the radial equation and divide out the common $Ae^{-r/a}$:

$$\frac{\hbar^2}{m_e a} - \frac{\hbar^2 r}{2m_e a^2} - \frac{e^2}{4\pi\varepsilon_0} = Er.$$

Here is the trick that makes the whole thing close. Sort by powers of $r$. The pieces with no $r$ and the pieces linear in $r$ each have to vanish on their own — because the equation must hold for *every* $r$, not just one lucky value. One equation has secretly become two:

**Constant terms:**
$$\frac{\hbar^2}{m_e a} = \frac{e^2}{4\pi\varepsilon_0} \implies a = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \equiv a_0.$$

**Linear-in-$r$ terms:**
$$E = -\frac{\hbar^2}{2m_e a_0^2}.$$

Put in the numbers and you get $E_1 \approx -13.6\,\text{eV}$.

Stop and notice what just happened. The Bohr radius $a_0 \approx 5.29 \times 10^{-11}$ m and the ionization energy $13.6\,\text{eV}$ came straight out of matching two slices of one equation. We never postulated a quantization condition. We never mentioned a circular orbit. The guess $u \propto re^{-r/a}$ was the only thing we put in by hand — and the equation only tolerates it when $a = a_0$ and $E = E_1$. The numbers were forced.

Now normalize. The full wave function is $\psi_{100} = R_{10}(r) \cdot Y_{00}$, with $R_{10}(r) = Ae^{-r/a_0}$ and $Y_{00} = 1/\sqrt{4\pi}$. The demand that $\int|\psi|^2 d^3r = 1$ splits apart cleanly:

$$\int_0^\infty |R_{10}|^2 r^2\,dr \cdot \int |Y_{00}|^2\,d\Omega = 1.$$

The angular integral is just 1. The radial integral hands you $A = 2/a_0^{3/2}$. And there is the ground state of hydrogen, fully normalized:

$$\boxed{\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}.}$$

![Plot of the 1s radial wave function R₁₀(r)](../images/06-the-hydrogen-atom-fig-03.png)
*Figure 6.3 — Plot of the 1s radial wave function R₁₀(r)*

---

## Dismantling the orbit picture

Now we get to the place where the Bohr model falls apart. Not in the energy — Bohr got the energy. It falls apart in everything it tries to tell you about *where the electron is*.

Ask: how likely am I to find the electron in a thin shell at radius $r$, a shell of thickness $dr$? That is the *radial probability density*:

$$P(r) = |R_{10}(r)|^2 \cdot r^2 = \frac{4}{a_0^3}\,r^2 e^{-2r/a_0}.$$

That factor of $r^2$ is not arbitrary — it is the geometry of the sphere. There is simply more room out at larger $r$. A shell of fixed thickness $dr$ holds more space the farther out you go. So you have a contest: the geometric factor wants to pull you outward, the decaying exponential wants to pull you in.

Where does the contest balance? Maximize $P(r)$:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left(2r - \frac{2r^2}{a_0}\right)e^{-2r/a_0} = 0 \implies r_{\text{mp}} = a_0.$$

The most probable radius is $a_0$. Bohr got this right too. But now watch — compute the *average* radius, the expectation value of $r$:

$$\langle r\rangle = \frac{4}{a_0^3}\int_0^\infty r^3 e^{-2r/a_0}\,dr = \frac{4}{a_0^3} \cdot \frac{6}{(2/a_0)^4} = \frac{3a_0}{2}.$$

The most probable radius is $a_0$. The average radius is $\tfrac{3}{2}a_0$.

Two different numbers. Now this is strange. How can the most likely place and the average place disagree? Let's think it through. They disagree because the distribution is lopsided: $P(r)$ peaks at $a_0$, but it drags a long tail out toward larger $r$, and that tail tugs the average upward. Here is the whole point. If the electron really rode a circular orbit at radius $a_0$, there would be exactly one radius. "Most probable" and "average" would be the same number, because there would be nothing to average over. The fact that they differ is the mathematical fingerprint that the electron lives across a *spread* of radii — not on a single circle. There is no orbit. There is a cloud of probability.

![The orbit picture requires both markers to be at the same place. They are not.](../images/06-the-hydrogen-atom-fig-04.png)
*Figure 6.4 — P(r) = (4/a₀³)r²e^{−2r/a₀} plotted vs r/a₀ from 0*

And there is no instant at which the electron sits at a definite radius, moving at a definite speed, headed a definite way. What there is — all there is — is $|\psi_{100}|^2$: a spherically symmetric cloud fading exponentially away from the nucleus. The number $a_0$ shows up inside that cloud as the length scale that sets its size. Bohr found the right length scale by betting on a circular orbit. He got lucky. The length scale is real. The orbit is a fiction.

---

## Why Bohr got the energies right: the hidden symmetry

So we are back to the coincidence — the wrong model that coughed up right energies — and now we can name what is underneath it. The Coulomb potential $V = -e^2/(4\pi\varepsilon_0 r)$ carries more symmetry than meets the eye. Yes, there is the obvious rotational symmetry $\mathrm{SO}(3)$: the potential looks identical from every direction. But the $1/r$ form smuggles in a second conserved quantity — the Laplace–Runge–Lenz vector, which in the classical orbit points along the long axis of the ellipse and never changes its length. Stitch the two symmetries together and the full symmetry group of the Coulomb problem is $\mathrm{SO}(4)$.

Wolfgang Pauli rode this symmetry in early 1926 to solve hydrogen by pure algebra, before Schrödinger's wave solution had even arrived. [Pauli 1926, *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify pages]. And here is what $\mathrm{SO}(4)$ buys you: the energy of a hydrogen state depends only on the principal quantum number $n$, and not at all on $\ell$. States with the same $n$ but different $\ell$ — $2s$ and $2p$, say — land on exactly the same energy. The standard name for this is *accidental degeneracy*, which is a terrible name, because it is not accidental in the least. It is forced by the symmetry.

Bohr's rule $L = n\hbar$ is flatly wrong about angular momentum — the true eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, and $\ell$ can run anywhere from $0$ up to $n-1$. But because the energy ignores $\ell$ and listens only to $n$, Bohr's formula for the energies comes out accidentally correct. Now take that same method to helium — two electrons, no clean $\mathrm{SO}(4)$ symmetry, no accidental degeneracy — and it fails by roughly 30%. The success was never general. It was hydrogen, and only hydrogen, all along.

---

## The four quantum numbers

Every state of hydrogen wears four quantum numbers, like a name tag with four lines.

The *principal quantum number* $n = 1, 2, 3, \ldots$ fixes the energy: $E_n = -13.6\,\text{eV}/n^2$. It is the label that comes with $\hat{H}$.

The *orbital angular momentum quantum number* $\ell = 0, 1, \ldots, n-1$ fixes how much orbital angular momentum there is: $\hat{L}^2\psi = \hbar^2\ell(\ell+1)\psi$. The spectroscopic letters $s, p, d, f$ stand for $\ell = 0, 1, 2, 3$ — leftovers from pre-quantum spectroscopy ("sharp, principal, diffuse, fundamental"), kept around purely out of habit.

The *magnetic quantum number* $m_\ell = -\ell, -\ell+1, \ldots, +\ell$ fixes the projection of orbital angular momentum onto an axis you pick: $\hat{L}_z\psi = m_\ell\hbar\psi$.

The *spin quantum number* $m_s = \pm 1/2$ fixes the projection of spin angular momentum: $\hat{S}_z\psi = m_s\hbar\psi$.

Count the states sitting at energy level $n$:

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2 \quad\text{(without spin)}, \qquad 2n^2 \quad\text{(with spin)}.$$

That $n^2$ is a direct child of the $\mathrm{SO}(4)$ degeneracy. The shell at $n=1$ holds 2 electrons; at $n=2$, 8; at $n=3$, 18. And those — look at them — are the row lengths of the periodic table. Handed down not by chemistry, but by quantum mechanics and Pauli.

| $n$ | $\ell$ values | spectroscopic labels | $m_\ell$ values | orbitals | states with spin |
| --- | --- | --- | --- | ---: | ---: |
| 1 | 0 | 1s | 0 | 1 | 2 |
| 2 | 0, 1 | 2s, 2p | 0; -1, 0, +1 | 4 | 8 |
| 3 | 0, 1, 2 | 3s, 3p, 3d | 0; -1, 0, +1; -2, -1, 0, +1, +2 | 9 | 18 |
| 4 | 0, 1, 2, 3 | 4s, 4p, 4d, 4f | $m_\ell=-\ell,\ldots,+\ell$ | 16 | 32 |

One word we have to clean up before going on: "orbital" does not mean "orbit." An orbital — the round $s$ cloud, the dumbbell $p$, the four-lobed $d$ — is an isocontour of $|\psi_{n\ell m}|^2$, usually the surface drawn to enclose 90% of the probability. It tells you where the electron is *likely to turn up if you measure*. It says nothing about what the electron is doing between measurements, because quantum mechanics tells no between-measurements story at all. The shape is everything. The trajectory is nothing.

![90%-probability isosurface renderings of the 1s, 2s, 2p_z,](../images/06-the-hydrogen-atom-fig-05.png)
*Figure 6.5 — 90%-probability isosurface renderings of the 1s, 2s, 2p_z,*

---

## Spin: the internal angular momentum that cannot be rotation

In 1922 Otto Stern and Walther Gerlach sent a beam of neutral silver atoms through a magnetic field that was deliberately lopsided — stronger on one side than the other. Now think about what classical physics expects. The atoms carry magnetic moments pointing every which way, so they should fan out and smear into a continuous streak on the detector. That is the prediction. What Stern and Gerlach actually saw was two spots. [Stern & Gerlach 1922, *Zeitschrift für Physik* 9, 349–352](https://doi.org/10.1007/BF01326983) [verify pages]. Two. Not a smear.

Silver has one lonely unpaired electron in a $5s$ state. The two spots are the two possible projections of that electron's spin onto the field axis: $S_z = +\hbar/2$ and $S_z = -\hbar/2$. Two outcomes. No continuum.

![Two spots where classical physics predicts a smear. The discreteness is spin.](../images/06-the-hydrogen-atom-fig-06.png)
*Figure 6.6 — Stern-Gerlach apparatus diagram *

Here is a historical wrinkle worth telling. Stern and Gerlach in 1922 did not read their two spots as electron spin. Spin had not been dreamed up yet. They thought they were watching "space quantization" of orbital angular momentum. The correct reading — that the splitting comes from the spin of the unpaired $5s$ electron — only arrived after Uhlenbeck and Goudsmit proposed intrinsic electron spin in 1925. [Uhlenbeck & Goudsmit 1925, *Die Naturwissenschaften* 13, 953–954](https://doi.org/10.1007/BF01558878) [verify]. The experiment ran a full three years before anybody understood what it had measured.

So what *is* spin? It is intrinsic angular momentum. Every electron carries angular momentum of magnitude $\sqrt{s(s+1)}\hbar = (\sqrt{3}/2)\hbar$ with $s = 1/2$, and that is the end of it. It is not angular momentum from anything moving through space. It is a property the electron simply has, the way it has charge, the way it has mass. The Dirac equation — Schrödinger's equation made compatible with relativity — produces spin all by itself: demand that a quantum wave equation respect Lorentz invariance, and spin-1/2 drops out as an algebraic inevitability. [Dirac 1928, *Proceedings of the Royal Society A* 117, 610–624](https://doi.org/10.1098/rspa.1928.0023). You do not get to put spin in. You cannot keep it out.

Now, the seductive picture — the electron is just a tiny spinning ball — can be killed with a single calculation, and it is worth doing because it cures you of the picture forever. Suppose the electron is a uniform solid sphere of radius $r_e$, spinning about its axis. For a solid sphere, $I = \frac{2}{5}m_er_e^2$, so to make the angular momentum come out to $\hbar/2$, the equator would have to be moving at

$$v = \omega r_e = \frac{Lr_e}{I} = \frac{5\hbar}{4m_e r_e}.$$

Take the classical electron radius — estimated by setting the electron's rest energy equal to its own electrostatic energy — which is $r_e \approx 2.82 \times 10^{-15}$ m. Plug in:

$$v \approx \frac{5(1.055\times10^{-34})}{4(9.11\times10^{-31})(2.82\times10^{-15})} \approx 5.1 \times 10^{10}\,\text{m/s}.$$

That is about 170 times the speed of light, matching the solid-sphere estimate used in the reference spin chapter. And if the electron is smaller than $r_e$ — experiment pins it down as pointlike to at least $10^{-18}$ m — the required speed only gets more absurd. So the spinning-ball picture is not merely sloppy. It is geometrically impossible. The surface would have to outrun light, and badly.

The picture survives in introductory books because it is handy shorthand. The calculation above should be enough to put it to rest.

---

## The Pauli exclusion principle

In 1925, before the Schrödinger equation even existed, Pauli proposed a rule: no two electrons in an atom may share all four quantum numbers $(n, \ell, m_\ell, m_s)$. [Pauli 1925, *Zeitschrift für Physik* 31, 765–783](https://doi.org/10.1007/BF02980631). He got there by squinting at the patterns in atomic spectra — which shells fill with how many electrons, which spectral lines appear and which do not. The rule fit every scrap of data. He did not yet know why it was true.

The deeper reason, which Unit 8 unfolds, is that electrons are fermions: their many-particle wave function must flip sign whenever you swap any two of them, $\psi(1,2) = -\psi(2,1)$. Now suppose two electrons tried to occupy the very same state. Then the wave function would have to equal its own negative — which forces it to be zero. No such state exists. The exclusion principle is just the corollary. For now we only need the consequence: each orbital, labeled by $(n, \ell, m_\ell)$, holds at most two electrons — one spin-up, one spin-down.

The $n=1$ shell has $2(1)^2 = 2$ states. The $n=2$ shell has $2(2)^2 = 8$. The $n=3$ shell has $2(3)^2 = 18$. There is the row structure of the periodic table again.

But here is the part that should genuinely amaze you. The reason solid matter takes up space — the reason your hand does not pass straight through the table, the reason atoms have any size at all — traces back to Pauli. Turn off the exclusion principle and every electron in every atom would cascade down into the $1s$ ground state, and every atom would shrink to the size of hydrogen. Chemistry would not exist. The exclusion principle is, in a precise and literal sense, the principle that the material world is built from solid objects instead of collapsing into blobs.

---

## What would change my mind

Hydrogen spectroscopy is quantum mechanics' best-tested prediction, full stop. Every refinement we have ever added has only piled on more confirmation: the Lamb shift from quantum electrodynamics, the hyperfine structure from nuclear spin, the fine structure from relativistic corrections — all computed, all measured, all in agreement. There was a scare for a few years — the "proton radius puzzle," a mismatch between the proton radius read off from muonic hydrogen [Pohl et al. 2010, *Nature* 466, 213–216](https://doi.org/10.1038/nature09250) and from ordinary electron-hydrogen spectroscopy — but newer measurements [Bezginov et al. 2019, *Science* 365, 1007–1012](https://doi.org/10.1126/science.aau7807) [verify] are settling toward the smaller muonic value. The framework holds. What would shake it: a hydrogen spectral line that no extension of the present theory can fit, stubbornly and reproducibly. We do not have one.

---

## Still puzzling

The $\mathrm{SO}(4)$ symmetry of the Coulomb potential — the hidden symmetry that makes hydrogen's energy listen to $n$ alone and ignore $\ell$ — still feels like a coincidence to me, even though it is mathematically forced by the $1/r$ shape of the potential. Pauli's 1926 derivation lays the algebra out plainly and cleanly. It does not make the symmetry *feel* inevitable. Why does the inverse-square law carry this extra conserved quantity when, say, a $1/r^2$ potential does not? There is a clean classical answer — Bertrand's theorem, which says the only potentials giving closed orbits are $1/r$ and $r^2$ — and a matching quantum answer running through the Laplace–Runge–Lenz vector. I find both of them technically airtight and somehow aesthetically unsatisfying. That hydrogen, and only hydrogen among the one-electron atoms, comes apart so cleanly feels like a coincidence with a deep reason hiding behind it — rather than a deep reason I can honestly say I understand.

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
