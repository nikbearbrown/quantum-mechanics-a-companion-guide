# Unit 6 — The Hydrogen Atom

> One electron, one proton, a Coulomb potential — and the cleanest test we have of whether quantum mechanics is right about the world.

---

## 1. What this chapter is doing

This chapter solves hydrogen. Not metaphorically — we will write the Schrödinger equation for a single electron bound to a single proton, separate it into radial and angular pieces, and produce the ground-state wave function explicitly. You will see where the four quantum numbers $(n, \ell, m_\ell, m_s)$ come from, why hydrogen has exactly the energy spectrum that Balmer fit by eye in 1885, why Bohr's 1913 model gives the right energies for the wrong reasons, and why "spin" is not — really, definitively, not — the electron rotating on its axis.

Three things to keep in mind before we begin. First, hydrogen is exceptional. It is the only neutral atom for which the Schrödinger equation has a clean closed-form solution. Every other atom requires approximations. The reason hydrogen is special is a hidden symmetry (the $\mathrm{SO}(4)$ symmetry of the Coulomb potential) that Pauli exploited algebraically in 1926. We will name this; we will not derive it.

Second, the deep-dive of this chapter is the $1s$ state. We will solve the radial equation for $n=1, \ell=0$ on the page, compute the most probable radius and the expectation value of $r$, and use the gap between those two numbers to dismantle the "orbital is a path" picture that almost every student arrives with.

Third, this chapter uses operators ($\hat{L}^2$, $\hat{L}_z$, $\hat{S}_z$) without yet deriving their full machinery. Unit 7 supplies that machinery. You will leave this chapter holding an IOU; Unit 7 pays it.

---

## 2. Learning objectives

By the end of this chapter you should be able to:

1. **Apply** separation of variables to the Schrödinger equation in spherical coordinates, identifying the radial and angular pieces.
2. **Derive** the Bohr-model energy levels and the Bohr radius from angular-momentum quantization plus Newtonian circular-orbit mechanics.
3. **Solve** the radial equation for the hydrogen $1s$ state and compute $\langle r \rangle$ and the most probable radius $r_{\text{mp}}$.
4. **Explain** the four quantum numbers $(n, \ell, m_\ell, m_s)$ — what each one is the eigenvalue of, and what range it can take.
5. **Evaluate** the classical-rotation picture of electron spin and show, by computing equatorial speed, that it is physically impossible.
6. **State** the Pauli exclusion principle in its four-quantum-number form and connect it to the $2n^2$ degeneracy of hydrogen-like shells.

---

## 3. The motivating problem

In 1885 a Swiss schoolteacher named Johann Balmer was looking at hydrogen's visible emission spectrum. Hydrogen, heated in a discharge tube, emits light at very specific wavelengths — a red line at 656 nm, a blue-green line at 486 nm, a violet line at 434 nm, and so on. Not a continuous spectrum. A handful of sharp lines.

Balmer noticed that the wavelengths $\lambda_n$ of the visible hydrogen lines fit the formula

$$\lambda_n = B \cdot \frac{n^2}{n^2 - 4}, \quad n = 3, 4, 5, \ldots$$

with $B \approx 364.5$ nm. He had no theoretical justification. The formula just worked. ([Balmer 1885, *Annalen der Physik* 261, 80–87](https://doi.org/10.1002/andp.18852610506) [verify].)

Twenty-eight years passed before anyone could say why. Then in July 1913 a 27-year-old Niels Bohr published a paper in *Philosophical Magazine* — "On the Constitution of Atoms and Molecules" — that derived the Balmer formula from a single bold postulate. ([Bohr 1913, *Philosophical Magazine* Series 6, 26, 1–25](https://doi.org/10.1080/14786441308634955).) Bohr's claim was that the electron orbiting the proton can only occupy orbits whose angular momentum is an integer multiple of $\hbar$:

$$L = n\hbar, \quad n = 1, 2, 3, \ldots$$

From that one rule, plus Newtonian mechanics for circular motion under the Coulomb force, every visible line of hydrogen fell out with the right numerical coefficient.

This was a triumph. It was also, in retrospect, deeply weird. Bohr's electron was still circling the proton like a planet around the sun — a definite path, a definite radius, a definite speed. Quantum mechanics in its mature form (after 1925) abandons that picture entirely. And yet Bohr's model gives the right energies for hydrogen.

Why?

The puzzle has two parts. First, where does Balmer's empirical formula come from physically? Second, why does Bohr's semi-classical picture — which we now know is wrong about how electrons behave — nevertheless produce the right energy spectrum? This chapter answers both. The first answer is the full Schrödinger solution. The second answer is a hidden symmetry that hydrogen happens to have and most atoms do not. Bohr got lucky.

We will also build the apparatus you need for the rest of atomic physics: the four quantum numbers, the orbital shapes, electron spin, and the exclusion principle. By the end of the chapter you will understand why the periodic table has the row structure it does — and why "orbital" does not mean "orbit."

---

## 4. Concept blocks

### 4.1 Central potentials and separation of variables

The hydrogen Hamiltonian is

$$\hat{H} = -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{e^2}{4\pi\varepsilon_0 r}$$

where $m_e$ is the electron mass and $r$ is the electron's distance from the proton. (We are treating the proton as a fixed point; the small correction for finite proton mass uses the reduced mass $\mu = m_e m_p / (m_e + m_p)$, which is a tiny adjustment.) The potential $V(r) = -e^2/(4\pi\varepsilon_0 r)$ depends only on $r$, not on the polar angle $\theta$ or the azimuthal angle $\phi$. This is what we mean by a *central potential*.

Spherical symmetry is the mathematical license for separation of variables. We assume

$$\psi(r, \theta, \phi) = R(r) \cdot Y(\theta, \phi)$$

and substitute into the time-independent Schrödinger equation $\hat{H}\psi = E\psi$. In spherical coordinates, the Laplacian is

$$\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial}{\partial \theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2}{\partial \phi^2}.$$

Substituting $\psi = RY$ into $\hat{H}\psi = E\psi$ and multiplying through by $-2m_e r^2 / (\hbar^2 R Y)$, the equation splits into a part that depends only on $r$ and a part that depends only on $(\theta, \phi)$. The two parts must each equal a constant — call it $\ell(\ell+1)$ for reasons that will become clear. We get two equations:

**Angular equation:**

$$-\frac{1}{\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial Y}{\partial \theta}\right) - \frac{1}{\sin^2\theta}\frac{\partial^2 Y}{\partial \phi^2} = \ell(\ell+1) Y.$$

This is an eigenvalue equation for the operator $\hat{L}^2/\hbar^2$ on the sphere. Its solutions, the spherical harmonics $Y_{\ell m}(\theta, \phi)$, will be derived in Unit 7. For now: they exist, they are labeled by two integers $\ell \geq 0$ and $|m| \leq \ell$, and they are orthonormal on the sphere.

**Radial equation:**

$$-\frac{\hbar^2}{2m_e}\frac{1}{r^2}\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right) + \left[V(r) + \frac{\hbar^2 \ell(\ell+1)}{2m_e r^2}\right] R = E R.$$

Two things to notice. First, the term $\hbar^2\ell(\ell+1)/(2m_e r^2)$ appeared in the radial equation as a consequence of the separation — it is not a classical centrifugal term that we put in by hand. The angular kinetic energy, when restricted to an eigenstate of $\hat{L}^2$, looks like a repulsive $1/r^2$ potential. This is the *centrifugal barrier*, and it keeps electrons with $\ell > 0$ from collapsing into the nucleus.

Second, the substitution $u(r) = r R(r)$ converts the radial equation into a one-dimensional Schrödinger equation:

$$-\frac{\hbar^2}{2m_e}\frac{d^2 u}{dr^2} + \left[V(r) + \frac{\hbar^2 \ell(\ell+1)}{2m_e r^2}\right] u = E u.$$

This is the equation we will solve in §5 for the $1s$ state.

(Griffiths §4.1 develops the separation in spherical coordinates; §4.2 attacks the hydrogen radial equation via the Frobenius method and gets the full $(n, \ell)$ spectrum. We are extracting the $1s$ piece here.)

### 4.2 Bohr's model as a limiting case — and why it got lucky

Bohr's 1913 derivation runs in three lines.

Postulate: $L = m_e v r = n\hbar$.

Newton's second law for circular motion under the Coulomb force:

$$\frac{m_e v^2}{r} = \frac{e^2}{4\pi\varepsilon_0 r^2}.$$

Combine. Solve for $r$:

$$r_n = \frac{4\pi\varepsilon_0 \hbar^2 n^2}{m_e e^2} = a_0 \cdot n^2$$

where the Bohr radius is

$$a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 5.29 \times 10^{-11} \text{ m} = 0.529 \text{ Å}.$$

Now the energy. Total energy is kinetic plus potential, and for a circular orbit under an inverse-square attraction the kinetic energy equals minus half the potential (this is the virial theorem). So

$$E_n = -\frac{1}{2} \cdot \frac{e^2}{4\pi\varepsilon_0 r_n} = -\frac{m_e e^4}{2(4\pi\varepsilon_0)^2 \hbar^2 n^2} = -\frac{13.6 \text{ eV}}{n^2}.$$

That is the Rydberg formula. Plugging in $n_i \to n_f$ transitions gives Balmer's lines exactly. Bohr's paper landed in *Philosophical Magazine* in three parts that year and the spectrum problem was, on a certain reading, solved.

Here is the catch. Bohr's electron is on a definite circular orbit at a definite radius — a picture quantum mechanics rejects. So why are the *energies* right?

The answer is that the Coulomb potential $V \propto 1/r$ has a hidden symmetry beyond the obvious rotational symmetry $\mathrm{SO}(3)$. There is an additional conserved vector — the Laplace–Runge–Lenz vector — and the combined symmetry group is $\mathrm{SO}(4)$. Wolfgang Pauli used this symmetry in early 1926 to solve hydrogen algebraically before Schrödinger's wave-mechanical solution appeared. ([Pauli 1926, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik," *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify pages].) The $\mathrm{SO}(4)$ symmetry forces the energy to depend only on a single quantum number $n$, not on $\ell$ — and that single quantum number can be derived in either of two ways, semi-classically (Bohr) or quantum-mechanically (Schrödinger).

Bohr's quantization condition $L = n\hbar$ is wrong as a statement about angular momentum (the actual eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, and $\ell$ ranges from $0$ to $n-1$). It happens to produce the right energies because of the $\mathrm{SO}(4)$ degeneracy. Apply it to helium, lithium, anything with more than one electron, and it fails. The hydrogen-only success is a coincidence with a deep reason, not a sign that classical mechanics "almost works."

### 4.3 Quantum numbers and orbitals

Four quantum numbers label every hydrogen state:

| Symbol | Name | Range | Eigenvalue equation |
|---|---|---|---|
| $n$ | principal | $1, 2, 3, \ldots$ | $\hat{H}\psi = -\frac{13.6 \text{ eV}}{n^2}\psi$ |
| $\ell$ | orbital angular momentum | $0, 1, \ldots, n-1$ | $\hat{L}^2 \psi = \hbar^2 \ell(\ell+1)\psi$ |
| $m_\ell$ | magnetic | $-\ell, -\ell+1, \ldots, +\ell$ | $\hat{L}_z \psi = m_\ell \hbar \psi$ |
| $m_s$ | spin projection | $\pm 1/2$ | $\hat{S}_z \psi = m_s \hbar \psi$ |

The spectroscopic letters $s, p, d, f$ correspond to $\ell = 0, 1, 2, 3$. They come from pre-quantum spectroscopy — "sharp, principal, diffuse, fundamental" — and are arbitrary labels at this point. They stuck.

The total number of states at a given energy $E_n$ is

$$\sum_{\ell=0}^{n-1}(2\ell+1) = n^2 \quad \text{(without spin)}, \quad 2n^2 \quad \text{(with spin)}.$$

This is the degeneracy at the $n$-th shell. The $n^2$ comes from the $\mathrm{SO}(4)$ symmetry mentioned above; the factor of two is spin.

**Common misconception, named directly.** An "orbital" is not a path the electron traces. The electron does not orbit. What we draw as an orbital — the spherical $s$ cloud, the dumbbell $p$, the four-lobed $d$ — is an isocontour of $|\psi_{n\ell m}|^2$, typically the surface that encloses (say) 90% of the probability. The shape comes from $|Y_{\ell m}(\theta, \phi)|^2$ times $|R_{n\ell}(r)|^2$. It describes where the electron is *likely to be found if we measure its position*. It does not describe what the electron is doing between measurements.

This is the single most damaging picture in introductory chemistry. We will demolish it concretely in §5.

### 4.4 Spin and the Stern–Gerlach experiment

In 1922 Otto Stern and Walther Gerlach sent a beam of neutral silver atoms through an inhomogeneous magnetic field. Classically, atoms with magnetic moments at all orientations should produce a continuous smear on the detector. What Stern and Gerlach saw was *two* discrete spots. ([Stern & Gerlach 1922, "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld," *Zeitschrift für Physik* 9, 349–352](https://doi.org/10.1007/BF01326983) [verify pages].)

Silver has electron configuration $[\mathrm{Kr}]\,4d^{10}\,5s^1$ — a closed-shell core plus one unpaired $5s$ electron. The two spots correspond to the two projections of that electron's spin angular momentum onto the magnetic-field axis: $S_z = +\hbar/2$ and $S_z = -\hbar/2$.

Historical footnote, because students rarely hear it: Stern and Gerlach in 1922 did not believe they were measuring electron spin. Spin had not been proposed. They thought they were observing "space quantization" of the orbital angular momentum predicted by Sommerfeld's old quantum theory. The correct interpretation — that the splitting reflects $S_z$ of the unpaired electron — came only after Uhlenbeck and Goudsmit proposed electron spin in 1925. ([Uhlenbeck & Goudsmit 1925, *Die Naturwissenschaften* 13, 953–954](https://doi.org/10.1007/BF01558878) [verify].) Friedrich and Herschbach's 2003 *Physics Today* piece is the careful historical reconstruction. ([Friedrich & Herschbach 2003, *Physics Today* 56(12), 53–59](https://doi.org/10.1063/1.1650229).)

What is spin, then? It is intrinsic angular momentum. Every electron carries angular momentum of magnitude $\sqrt{s(s+1)}\hbar = \sqrt{3}/2 \cdot \hbar$ with $s = 1/2$ — and that's it. It is not orbital, it is not motion through space, it is a property the electron has the way it has charge or mass. The full mathematical machinery (Pauli matrices, $\mathrm{SU}(2)$ representations, the spinor character) is Unit 7's job. What this chapter needs is the negative claim: spin is *not* a classical rotation. Here is the proof.

**The classical-rotation picture, taken seriously, fails by orders of magnitude.** Suppose the electron is a tiny ball of radius $r_e$ rotating about its axis with angular speed $\omega$. Its spin angular momentum would be of order $S \sim m_e r_e^2 \omega$. Setting this equal to $\hbar/2$ and solving for the equatorial speed $v = r_e \omega$ gives

$$v = \frac{\hbar/2}{m_e r_e}.$$

The "classical electron radius" — the size you'd estimate if all the electron's rest energy came from electrostatic self-energy — is

$$r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.82 \times 10^{-15} \text{ m}.$$

Plugging in:

$$v \approx \frac{1.05 \times 10^{-34} / 2}{(9.11 \times 10^{-31})(2.82 \times 10^{-15})} \approx \frac{5.27 \times 10^{-35}}{2.57 \times 10^{-45}} \approx 2.0 \times 10^{10} \text{ m/s}.$$

That is roughly seventy times the speed of light. If you use a smaller radius for the electron — and experiment is consistent with the electron being pointlike down to at least $10^{-18}$ m — the required speed becomes vastly larger. The classical picture does not just struggle. It is geometrically impossible.

The picture survives in pedagogy because the language is convenient. The picture is wrong.

Where does spin actually come from? Dirac showed in 1928 that if you demand a quantum-mechanical wave equation be Lorentz-invariant — that is, consistent with special relativity — spin-1/2 falls out automatically as a consequence of the algebra. Spin is what you get when you do quantum mechanics correctly for relativistic particles. ([Dirac 1928, "The Quantum Theory of the Electron," *Proceedings of the Royal Society A* 117, 610–624](https://doi.org/10.1098/rspa.1928.0023).) The classical-rotation picture has no place in the explanation. We will return to this in Unit 7.

### 4.5 The Pauli exclusion principle

Wolfgang Pauli in 1925 proposed that no two electrons in an atom can have all four quantum numbers $(n, \ell, m_\ell, m_s)$ the same. ([Pauli 1925, "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren," *Zeitschrift für Physik* 31, 765–783](https://doi.org/10.1007/BF02980631).) This was Pauli's solution to a puzzle in atomic spectra — the observed pattern of which shells fill with how many electrons. The rule states a fact; it does not explain the fact. The deeper version, that fermionic wave functions are antisymmetric under particle exchange, $\psi(1,2) = -\psi(2,1)$, is Unit 8's territory. The exclusion principle as Pauli stated it is a corollary of that antisymmetry.

For now, the operational consequence: a hydrogen-like shell with principal quantum number $n$ has $2n^2$ available states. Two electrons fit per orbital (one with $m_s = +1/2$, one with $m_s = -1/2$). The $K$ shell ($n=1$) holds 2; the $L$ shell ($n=2$) holds 8; the $M$ shell ($n=3$) holds 18. These are the row lengths of the periodic table (modulo some reordering at higher $n$ that comes from the actual energy ordering of $4s$ vs $3d$ — a real-atom complication that the hydrogen story does not capture).

The reason atoms do not collapse — the reason solid matter takes up space at all — is Pauli. The exclusion principle is what makes electrons stack into shells rather than all piling into the $1s$ state. Without it, every atom would be the size of hydrogen and chemistry would not exist.

---

## 5. Worked example: solving the 1s state

This is the chapter's deep-dive. We compute the hydrogen ground state from the radial equation, then use the result to dismantle the orbit picture.

For $n=1, \ell=0$, the radial equation in the $u(r) = rR(r)$ form is

$$-\frac{\hbar^2}{2m_e}\frac{d^2 u}{dr^2} - \frac{e^2}{4\pi\varepsilon_0 r} u = E u.$$

The centrifugal term has vanished because $\ell=0$. We try the ansatz

$$u(r) = A r e^{-r/a}$$

with $A$ a normalization constant and $a$ a length scale to be determined. The factor of $r$ ensures $u(0) = 0$ (required because $R(0)$ must be finite, so $u/r$ must be finite at the origin); the exponential decay ensures normalizability at large $r$.

Differentiate twice:

$$\frac{du}{dr} = A e^{-r/a}\left(1 - \frac{r}{a}\right), \quad \frac{d^2 u}{dr^2} = A e^{-r/a}\left(-\frac{2}{a} + \frac{r}{a^2}\right).$$

Substitute into the radial equation:

$$-\frac{\hbar^2}{2m_e} A e^{-r/a}\left(-\frac{2}{a} + \frac{r}{a^2}\right) - \frac{e^2}{4\pi\varepsilon_0 r} A r e^{-r/a} = E \cdot A r e^{-r/a}.$$

Divide through by $A e^{-r/a}$:

$$\frac{\hbar^2}{m_e a} - \frac{\hbar^2 r}{2 m_e a^2} - \frac{e^2}{4\pi\varepsilon_0} = E r.$$

Group the constant terms and the $r$-linear terms separately:

**Constant terms:** $\dfrac{\hbar^2}{m_e a} - \dfrac{e^2}{4\pi\varepsilon_0} = 0 \implies a = \dfrac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} = a_0.$

**Linear-in-$r$ terms:** $-\dfrac{\hbar^2}{2 m_e a^2} = E \implies E = -\dfrac{\hbar^2}{2 m_e a_0^2}.$

Plug in numerical values:

$$E_1 = -\frac{(1.055 \times 10^{-34})^2}{2 \cdot (9.11 \times 10^{-31}) \cdot (5.29 \times 10^{-11})^2} \approx -2.18 \times 10^{-18} \text{ J} \approx -13.6 \text{ eV}.$$

That is the hydrogen ionization energy. We have just derived it from the Schrödinger equation, using nothing but the ansatz and a length-scale matching.

Now normalize. The full wave function is $\psi_{100}(r, \theta, \phi) = R_{10}(r) Y_{00}(\theta, \phi)$ with $Y_{00} = 1/\sqrt{4\pi}$ and $R_{10}(r) = u(r)/r = A e^{-r/a_0}$. The normalization condition is

$$\int |\psi_{100}|^2 \, d^3r = \int_0^\infty |R_{10}|^2 r^2 \, dr \int |Y_{00}|^2 \, d\Omega = 1.$$

The angular integral is 1 (since $Y_{00}$ is already normalized on the sphere). The radial integral is

$$\int_0^\infty A^2 e^{-2r/a_0} r^2 \, dr = A^2 \cdot \frac{2}{(2/a_0)^3} = A^2 \cdot \frac{a_0^3}{4} = 1 \implies A = \frac{2}{a_0^{3/2}}.$$

So the normalized $1s$ wave function is

$$\boxed{\psi_{100}(r) = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}.}$$

(This matches Griffiths §4.2, Table 4.7 [verify exact location].)

Now the punchline.

**Most probable radius.** The radial probability density — the probability of finding the electron in a spherical shell of radius $r$, thickness $dr$ — is

$$P(r) = |R_{10}(r)|^2 \cdot r^2 = \frac{4}{a_0^3} r^2 e^{-2r/a_0}.$$

The factor $r^2$ is the Jacobian from spherical coordinates: there is more spherical-shell volume at larger $r$. Maximize $P(r)$ by setting $dP/dr = 0$:

$$\frac{dP}{dr} = \frac{4}{a_0^3}\left[2r - \frac{2r^2}{a_0}\right] e^{-2r/a_0} = 0 \implies r_{\text{mp}} = a_0.$$

The most probable radius equals the Bohr radius exactly. Bohr got the right length scale. He just got the meaning of that length scale catastrophically wrong — it is not the radius of a circular orbit; it is the peak of a probability distribution.

**Expectation value of $r$.**

$$\langle r \rangle = \int_0^\infty r \cdot |R_{10}|^2 \cdot r^2 \, dr = \frac{4}{a_0^3} \int_0^\infty r^3 e^{-2r/a_0} \, dr = \frac{4}{a_0^3} \cdot \frac{6}{(2/a_0)^4} = \frac{3 a_0}{2}.$$

So $\langle r \rangle = 1.5 a_0$, not $a_0$.

Read those two numbers carefully. The most probable radius is $a_0$; the average distance from the nucleus is $1.5 a_0$. These are different numbers because the distribution is asymmetric — it peaks at $a_0$ but has a long tail to large $r$, and that tail drags the mean upward.

This is the single fact that breaks the orbit picture. If the electron were on a circular orbit at radius $a_0$, then "most probable" and "average" would both equal $a_0$ — there is only one radius. The fact that they differ tells you the electron is not on any one radius. The $1s$ wave function is a probability cloud, not a path.

(There is a related calculation: the radial probability $P(r)$ is zero at $r=0$ — the electron is *not* most likely to be at the nucleus. This surprises some students; it is the $r^2$ Jacobian doing the work. We will come back to this in the exercises.)

---

## 6. Reading map

| Source | Where |
|---|---|
| Schrödinger in spherical coordinates; separation of variables | Griffiths §4.1 |
| Hydrogen radial equation; Frobenius solution; full spectrum | Griffiths §4.2 |
| Spin, Stern–Gerlach, spin matrices (preview for Unit 7) | Griffiths §4.4 |
| Bohr model historical narrative | Pop-sci Ch. 5 first half |
| Orbital pictures (correct the path misreading) | Pop-sci Ch. 5 second half |
| Pauli exclusion (verbal statement) | Pop-sci Ch. 5 |
| Periodic-table consequence (Unit 8 will deepen) | Pop-sci Ch. 13 |
| Companion §5 worked example, §4.4 classical-spin disproof | This chapter |
| Pauli's algebraic solution; $\mathrm{SO}(4)$ degeneracy | [Pauli 1926, *Zeitschrift für Physik* 36, 336–363](https://doi.org/10.1007/BF01450175) [verify] |

The pop-sci book is good motivating reading before lecture; it does not replace Griffiths for any technical purpose. Assign Ch. 5 the night before; correct the orbital-shape misreading in class.

---

## 7. Exercises

**Exercise 6.1 — Verify the normalization** [Bloom: Apply]
Show that $\psi_{100}(r) = (1/\sqrt{\pi a_0^3}) e^{-r/a_0}$ is normalized by computing $\int |\psi_{100}|^2 \, d^3 r$ explicitly in spherical coordinates. (You will need $\int_0^\infty r^n e^{-\alpha r} dr = n!/\alpha^{n+1}$.)

**Exercise 6.2 — Most-probable vs. expectation for 2s** [Bloom: Apply / Analyze]
The $2s$ wave function is $\psi_{200}(r) = (1/\sqrt{32\pi a_0^3})(2 - r/a_0) e^{-r/(2a_0)}$. Compute (a) the locations of the radial node ($P(r) = 0$ for $r > 0$), (b) the most probable radius (you will find more than one local max; identify which is the global max), and (c) $\langle r \rangle$. Compare to the $1s$ case. Why is $\langle r \rangle_{2s} > \langle r \rangle_{1s}$ by a factor of about four?

**Exercise 6.3 — Bohr model applied to helium fails** [Bloom: Evaluate]
Naïvely applying Bohr's quantization to helium ($Z=2$, two electrons), one might write $E \approx -Z^2 \cdot 13.6 \text{ eV} \cdot 2 = -108.8$ eV (treating each electron independently in a $Z=2$ Coulomb field). The actual ground-state energy of helium, inferred from the sum of the first and second ionization energies, is approximately $-79.0$ eV. (Sources: [NIST Atomic Spectra Database](https://physics.nist.gov/PhysRefData/ASD/levels_form.html) [verify URL].) (a) State the size and sign of the discrepancy. (b) Identify the physical effect Bohr's model leaves out. (c) What does this say about whether Bohr's model "almost works" for atoms in general?

**Exercise 6.4 — Disprove the classical-spin picture for a different particle** [Bloom: Analyze]
Repeat the equatorial-speed estimate for a *proton* — assume the proton is a solid sphere of radius $\sim 0.84$ fm ([proton charge radius from CODATA 2018](https://physics.nist.gov/cgi-bin/cuu/Value?rp) [verify]), with spin $\hbar/2$. Is the required equatorial speed superluminal? What does this tell you about whether "spin = rotation" can be rescued by going to heavier particles?

**Exercise 6.5 — Predict the row lengths of the periodic table** [Bloom: Create]
Using the quantum-number constraints $\ell \leq n-1$, $|m_\ell| \leq \ell$, $m_s = \pm 1/2$, derive the maximum number of electrons in each shell $n = 1, 2, 3, 4$. Compare to the actual row lengths in the periodic table (2, 8, 8, 18, 18, 32, 32 — or 2, 8, 18, 32 if you count by $n$). Where do the discrepancies between "shell capacity" and "row length" come from? You do not need to fully resolve this — name the effect.

---

## 8. What would change my mind

If a precision hydrogen spectroscopy experiment measured an energy level that the Schrödinger solution (with the usual QED corrections — Lamb shift, hyperfine, etc.) cannot account for, the entire framework would need revisiting. So far, every refinement has gone the other way: hydrogen agrees with theory to extraordinary precision. The "proton radius puzzle" — a discrepancy between proton radii inferred from muonic hydrogen ([Pohl et al. 2010, *Nature* 466, 213–216](https://doi.org/10.1038/nature09250)) and electron-hydrogen spectroscopy — appeared to threaten this in the 2010s, but more recent measurements ([Bezginov et al. 2019, *Science* 365, 1007–1012](https://doi.org/10.1126/science.aau7807) [verify]) are converging on the smaller (muonic) value. The framework holds. What would shake me: a hydrogen spectral line that does not fit, persistently and reproducibly. We do not have one.

## 9. Still puzzling

The $\mathrm{SO}(4)$ symmetry of the Coulomb potential — the reason hydrogen's energy depends only on $n$, not on $\ell$ — has the flavor of a coincidence even though it is mathematically forced by the $1/r$ potential. Pauli's 1926 derivation makes the algebra explicit; it does not make the symmetry feel inevitable. Why does the inverse-square law have this extra symmetry while, say, a $1/r^2$ potential does not? There is a clean answer in classical mechanics (closed orbits via Bertrand's theorem) and a related one in quantum mechanics (the Laplace–Runge–Lenz vector). I find both explanations technically convincing and aesthetically incomplete. The fact that hydrogen is a soluble two-body problem feels, to me, more like a piece of luck than I am fully comfortable with.

---

**Tags:** hydrogen-atom, bohr-model, schrodinger-equation, spin, pauli-exclusion, spherical-coordinates, quantum-numbers, orbitals
