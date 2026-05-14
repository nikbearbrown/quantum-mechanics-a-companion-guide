# Unit 4 — One-Dimensional Problems

> Four toy systems — box, oscillator, finite well, barrier — are where quantum mechanics stops being slogans and starts being arithmetic. Solve these, and most of the rest of the course is variations on a theme.

---

## 1. What this chapter is doing

This unit is the place quantum mechanics becomes concrete. You have built the formalism (Units 2 and 3); now you use it on four exactly-soluble (or almost-soluble) one-dimensional problems: the infinite square well, the harmonic oscillator, the finite square well, and tunneling through a barrier. Griffiths covers all of this in Chapter 2 and the WKB material in Chapter 9. The pop-sci companion does not — except for tunneling, where its Chapter 9 supplies excellent qualitative motivation and a useful catalog of applications (TIKTOC Part IV rates that one chapter ✅, with the math gap as the obvious thing for a companion to fill). For boxes, oscillators, and wells, the pop-sci book is silent. That silence is the gap this chapter fills. What you will get here that you cannot get there: every wave function written down, every energy spectrum derived from first principles, ladder operators built from $\hat{x}$ and $\hat{p}$, the WKB integral applied to alpha decay, and a worked transmission calculation tied to scanning tunneling microscopy.

## 2. Learning objectives

By the end of this chapter you should be able to:

1. **Recall** the eigenfunctions and energy spectra of the infinite square well and the quantum harmonic oscillator. (Bloom: Remember.)
2. **Explain** why the ground state of any confined quantum system has nonzero energy, and connect this to the uncertainty principle. (Bloom: Understand.)
3. **Apply** the ladder-operator method to compute matrix elements and the ground-state wave function of the harmonic oscillator. (Bloom: Apply.)
4. **Compute** transmission probabilities through rectangular and non-rectangular barriers using the WKB approximation. (Bloom: Apply.)
5. **Analyze** the bound-state structure of the finite square well and identify where the wave function leaks into the classically forbidden region. (Bloom: Analyze.)
6. **Evaluate** a tunneling-application claim from the pop-sci book against the exponential transmission formula and decide whether the claim is well-stated, oversold, or wrong. (Bloom: Evaluate.)

## 3. The motivating problem

A student stares at an energy diagram for the infinite square well. The levels are labeled $E_1, E_2, E_3, \ldots$, climbing up the page like rungs on a ladder. She asks the question the textbook does not always pause for: *why is the bottom rung not at zero?*

In a classical picture, a particle bouncing between two walls can be made to sit still. Drop it gently against the wall, no kinetic energy, $E = 0$. Nothing in Newtonian mechanics forbids it. But the quantum particle in the same box has a ground-state energy

$$E_1 = \frac{\pi^2 \hbar^2}{2 m L^2}$$

which is strictly positive. Hand it a smaller box and the floor rises. Make the box too tight and the floor goes through the ceiling — the particle is no longer comfortably bound, you have to keep adding energy to keep it there.

This is the zero-point energy, and it is not a quirk of square wells. Every confined quantum system has it. The harmonic oscillator has zero-point energy $\hbar\omega/2$. A hydrogen atom has zero-point energy $-13.6$ eV (negative because it is a bound state, but the magnitude is the ground-state floor). Liquid helium does not freeze at atmospheric pressure all the way down to absolute zero because the zero-point motion of the atoms is enough to keep the liquid from settling into a lattice. The fact that the bottom rung is above the floor is the most distinctive thing about quantum mechanics, and a confined particle is the cleanest place to see why.

The why is the uncertainty principle in arithmetic form. Confine a particle to a region of width $L$. Its position uncertainty $\sigma_x$ is at most of order $L$. By the inequality you will prove in Unit 5, the momentum uncertainty $\sigma_p$ must be at least $\hbar/(2L)$. So the expected kinetic energy is at least

$$\langle T \rangle = \frac{\langle p^2 \rangle}{2m} \geq \frac{\sigma_p^2}{2m} \geq \frac{\hbar^2}{8 m L^2}$$

which is positive and which scales as $1/L^2$, exactly as the box answer does. The numerical constant is wrong (the box answer is $\pi^2/2 \approx 4.93$ where the uncertainty estimate gives $1/8 = 0.125$ — they differ by a factor of $\sim 40$), but the *form* is right. Confinement forces motion. Motion costs energy. The bottom rung is not at zero because there is no quantum state where the particle is both localized and at rest. The chapter that follows shows this in detail for four specific potentials.

## 4. Concept blocks

### 4A. The infinite square well

**Plain language.** Trap a particle between two perfectly hard walls at $x = 0$ and $x = L$. Inside, no forces; outside, infinite potential. Find the allowed energies and the wave functions.

**Formal setup.** Time-independent Schrödinger equation in the region $0 < x < L$:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\,\psi$$

Outside the well, $V = \infty$ forces $\psi = 0$. Continuity of $\psi$ across the wall demands

$$\psi(0) = \psi(L) = 0.$$

**Derivation.** Define $k^2 = 2mE/\hbar^2$. The equation $\psi'' = -k^2 \psi$ has general solution

$$\psi(x) = A \sin(kx) + B \cos(kx).$$

Apply $\psi(0) = 0$: this kills the cosine, $B = 0$. Apply $\psi(L) = 0$: $A\sin(kL) = 0$, so $kL = n\pi$ for integer $n$. Each allowed $k$ fixes an allowed energy:

$$E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}, \qquad n = 1, 2, 3, \ldots$$

Normalize: $\int_0^L |\psi|^2\,dx = 1$ fixes $A = \sqrt{2/L}$, giving

$$\boxed{\psi_n(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right), \qquad E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}.}$$

This is Griffiths §2.2.

**Why $n = 0$ is excluded.** Setting $n = 0$ gives $\psi \equiv 0$ everywhere — the trivial solution. A wave function that vanishes everywhere cannot be normalized to unit probability; it does not describe a particle anywhere. So $n = 0$ is not a quantum state; it is the absence of a state. The ground state is $n = 1$, with strictly positive $E_1 = \pi^2\hbar^2/(2mL^2)$.

**Misconception.** "$n = 0$ is the ground state, with $E = 0$." No. Counting starts at $n = 1$. A student who memorizes "$E_n \propto n^2$" and starts the sum at zero will compute the wrong partition function in a thermodynamics course and conclude, incorrectly, that the heat capacity of a confined gas vanishes at low temperature for the wrong reason.

### 4B. The harmonic oscillator — algebraic method

**Plain language.** A particle in a parabolic potential $V(x) = \tfrac{1}{2}m\omega^2 x^2$. The classical version is a mass on a spring. The quantum version is the most-reused mechanism in physics: every smooth potential looks like this near a minimum, every electromagnetic-field mode is one of these, every phonon is one of these. Learn this single problem well and you are halfway to a graduate education.

**Hamiltonian.**

$$\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2.$$

**Ladder operators.** Define

$$\hat{a}_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\bigl(\mp i\hat{p} + m\omega\hat{x}\bigr).$$

Two facts do all the work.

*Fact 1: The commutator.* Using $[\hat{x}, \hat{p}] = i\hbar$,

$$[\hat{a}_-, \hat{a}_+] = \frac{1}{2\hbar m\omega}\bigl[i\hat{p} + m\omega\hat{x},\,-i\hat{p} + m\omega\hat{x}\bigr]$$

$$= \frac{1}{2\hbar m\omega}\bigl(-i m\omega[\hat{p}, \hat{x}] + i m\omega[\hat{x}, \hat{p}]\bigr) = \frac{1}{2\hbar m\omega}(2 m\omega \hbar) = 1.$$

So $[\hat{a}_-, \hat{a}_+] = 1$.

*Fact 2: Factorization of $\hat{H}$.* Expanding $\hat{a}_+\hat{a}_-$ and using $\hat{x}\hat{p} - \hat{p}\hat{x} = i\hbar$:

$$\hat{a}_+\hat{a}_- = \frac{1}{2\hbar m\omega}\bigl(\hat{p}^2 + m^2\omega^2\hat{x}^2 - m\omega\hbar\bigr) = \frac{\hat{H}}{\hbar\omega} - \frac{1}{2}.$$

Rearranging:

$$\hat{H} = \hbar\omega\!\left(\hat{a}_+\hat{a}_- + \frac{1}{2}\right).$$

**The step.** Compute $[\hat{H}, \hat{a}_\pm]$. Using $[\hat{H}, \hat{a}_-] = \hbar\omega[\hat{a}_+\hat{a}_-, \hat{a}_-]$ and the identity $[AB, C] = A[B,C] + [A,C]B$:

$$[\hat{H}, \hat{a}_\pm] = \pm \hbar\omega\,\hat{a}_\pm.$$

Now the magic. Suppose $\hat{H}|\psi\rangle = E|\psi\rangle$. Then

$$\hat{H}\hat{a}_+|\psi\rangle = (\hat{a}_+\hat{H} + [\hat{H}, \hat{a}_+])|\psi\rangle = \hat{a}_+(E + \hbar\omega)|\psi\rangle = (E + \hbar\omega)\,\hat{a}_+|\psi\rangle.$$

So $\hat{a}_+|\psi\rangle$ is an eigenstate of $\hat{H}$ with energy raised by $\hbar\omega$. Similarly $\hat{a}_-|\psi\rangle$ is an eigenstate with energy lowered by $\hbar\omega$. Energies climb and descend in steps of $\hbar\omega$ — this is the "ladder."

**The floor.** You cannot lower forever; the spectrum is bounded below, because $\hat{H}$ is a sum of squares of Hermitian operators and is non-negative. There must be a ground state $|0\rangle$ satisfying $\hat{a}_-|0\rangle = 0$. Then

$$\hat{H}|0\rangle = \hbar\omega\!\left(\hat{a}_+\hat{a}_- + \tfrac{1}{2}\right)|0\rangle = \frac{\hbar\omega}{2}|0\rangle$$

so the ground-state energy is $E_0 = \hbar\omega/2$. Every higher state is built by climbing: $|n\rangle \propto (\hat{a}_+)^n|0\rangle$, with energy

$$\boxed{E_n = \hbar\omega\!\left(n + \tfrac{1}{2}\right), \qquad n = 0, 1, 2, \ldots}$$

**Misconception.** "Ladder operators are just an algebraic trick to avoid solving the differential equation." No. The operators $\hat{a}_+$ and $\hat{a}_-$ have direct physical meaning. In the quantization of the electromagnetic field, the same operators (now called $\hat{a}^\dagger_k$ and $\hat{a}_k$) create and destroy *photons* of mode $k$. In condensed matter, they create and destroy phonons. The factorization $\hat{H} = \hbar\omega(\hat{N} + 1/2)$ with $\hat{N} = \hat{a}_+\hat{a}_-$ is the prototype for second quantization, and the chapter you are reading is the place that prototype gets built. Treat the algebra as the physics, not as a shortcut.

### 4C. The harmonic oscillator — analytic method

The differential-equation route, in parallel, because seeing two paths converge is one of Feynman's favorite teaching moves and Griffiths §2.3.2 lays it out cleanly.

Schrödinger's equation for the oscillator is

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2 x^2 \psi = E\psi.$$

Introduce the dimensionless variable $\xi = \sqrt{m\omega/\hbar}\,x$ and the energy parameter $K = 2E/(\hbar\omega)$. The equation becomes

$$\frac{d^2\psi}{d\xi^2} = (\xi^2 - K)\psi.$$

For large $|\xi|$, this is dominated by $\psi'' \approx \xi^2 \psi$, with solutions $\psi \sim e^{\pm\xi^2/2}$. Only the decaying exponential is normalizable. Strip it off: $\psi(\xi) = h(\xi)\,e^{-\xi^2/2}$. Substituting back gives the Hermite differential equation:

$$h'' - 2\xi h' + (K - 1)h = 0.$$

Try a power series $h(\xi) = \sum_j a_j \xi^j$. The recursion is

$$a_{j+2} = \frac{2j + 1 - K}{(j+1)(j+2)}\,a_j.$$

For the series to terminate (necessary for normalizability), some coefficient must satisfy $K = 2n + 1$ for an integer $n \geq 0$. This gives $E_n = \hbar\omega(n + 1/2)$ — the same spectrum as the algebraic route. The terminating polynomials are the Hermite polynomials $H_n(\xi)$, and the full wave functions are

$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2^n n!}}\,H_n\!\left(\sqrt{m\omega/\hbar}\,x\right)\,\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right).$$

For $n = 0$, $H_0(\xi) = 1$, and the ground state is the famous Gaussian:

$$\boxed{\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right).}$$

You can derive this directly from $\hat{a}_-|0\rangle = 0$, which in position representation reads

$$\frac{1}{\sqrt{2\hbar m\omega}}\!\left(\hbar\frac{d}{dx} + m\omega x\right)\psi_0 = 0 \quad\Longrightarrow\quad \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\,\psi_0.$$

That is a first-order linear ODE with exponential solution $\psi_0 \propto e^{-m\omega x^2/(2\hbar)}$, and normalization fixes the prefactor. The algebraic and the analytic routes give the same answer. (Of course they do. They are the same physics. But seeing it explicitly is teaching.)

### 4D. The finite square well

Pull the walls down to a finite depth. Let $V(x) = -V_0$ for $|x| < a$ and $V(x) = 0$ otherwise. Now two new things happen.

**First**: there are two kinds of solutions. For $E < 0$ (energy below the asymptotic potential), the particle is *bound* — it cannot escape to infinity, and the spectrum is discrete. For $E > 0$, the particle is *scattering* — it comes in from infinity, interacts with the well, and leaves, and the spectrum is continuous.

**Second**: bound-state wave functions are nonzero in the classically forbidden region outside the well. Inside, $\psi$ oscillates ($k = \sqrt{2m(E + V_0)}/\hbar$ is real). Outside, the Schrödinger equation reads $\psi'' = \kappa^2 \psi$ with $\kappa = \sqrt{-2mE}/\hbar > 0$, and the normalizable solution is $\psi(x) \propto e^{-\kappa|x|}$. An *exponentially decaying tail* extends out into the region where, classically, the particle would have negative kinetic energy. The particle leaks. It is not stuck inside the walls in the way a classical particle would be.

Matching $\psi$ and $\psi'$ at $x = \pm a$ yields a transcendental equation. For even-parity bound states the condition is (after a standard manipulation; Griffiths §2.6):

$$z \tan z = \sqrt{z_0^2 - z^2}, \qquad z = ka, \quad z_0^2 = \frac{2 m V_0 a^2}{\hbar^2}.$$

The dimensionless depth $z_0$ controls how many bound states fit. For very shallow wells, only one even bound state exists. For deep wells, many. The number is roughly $z_0/(\pi/2)$, rounded up. In one dimension a finite well always has at least one bound state, no matter how shallow. (Worth flagging: this is special to 1D. The same statement fails in 3D — a spherical well must exceed a critical depth before it binds anything. Griffiths §4.1.3 makes this precise. The student who has only seen 1D wells is in danger of generalizing the wrong lesson.)

**Misconception.** "The particle cannot exist outside the classically forbidden region." It can. The wave function is exponentially suppressed but not zero. At distance $d$ into the barrier the probability density is reduced by $\exp(-2\kappa d)$. For an electron with $V_0 - E = 1$ eV and $d = 1$ nm: $\kappa = \sqrt{2 m_e \times 1\text{ eV}}/\hbar \approx 5.1\text{ nm}^{-1}$, so $\exp(-2\kappa d) \approx \exp(-10.2) \approx 3.7 \times 10^{-5}$. Small. Not zero. STMs read out signals at exactly these suppression levels and turn them into atomic-resolution images. The leakage is small enough to look negligible and large enough to image atoms.

### 4E. Tunneling and the WKB approximation

If the wave function leaks into a forbidden region, it can leak *through*. A classical ball thrown at a wall it cannot climb bounces back, every time. A quantum particle has a nonzero probability of appearing on the other side. This is tunneling.

**Rectangular barrier.** For a barrier of height $V_0$ and width $L$, with particle energy $E < V_0$, the transmission coefficient (the standard textbook result, Griffiths §2.7) is

$$T = \left[1 + \frac{V_0^2}{4E(V_0 - E)}\sinh^2(\kappa L)\right]^{-1}, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}.$$

For a thick barrier ($\kappa L \gg 1$), $\sinh(\kappa L) \approx \tfrac{1}{2}e^{\kappa L}$, and the formula collapses to

$$T \approx 16\,\frac{E}{V_0}\!\left(1 - \frac{E}{V_0}\right)\,e^{-2\kappa L}.$$

The exponential controls everything. Halve $L$ and $T$ grows by a factor of $e^{\kappa L}$ — typically several orders of magnitude. This is why the scanning tunneling microscope (Binnig & Rohrer, *Physical Review Letters* 49, 57 (1982); Nobel Prize 1986) can image atoms: the tunneling current depends exponentially on the tip-sample distance, so a 0.1 nm height change moves the current by roughly a factor of ten.

**WKB for non-rectangular barriers.** Real barriers are rarely rectangular. The Coulomb barrier confronting an alpha particle in a nucleus is shaped like $1/r$. The Wentzel-Kramers-Brillouin approximation generalizes the rectangular formula by replacing the exponent with an integral. For a slowly-varying potential (slow on the scale of the local de Broglie wavelength), the wave function in the classically forbidden region looks like

$$\psi(x) \approx \frac{1}{\sqrt{|p(x)|}}\exp\!\left(-\frac{1}{\hbar}\int_a^x |p(x')|\,dx'\right), \qquad |p(x)| = \sqrt{2m(V(x) - E)},$$

and the transmission probability across a region $[a, b]$ where $V > E$ is

$$\boxed{T \approx \exp\!\left(-\frac{2}{\hbar}\int_a^b \sqrt{2m\bigl(V(x) - E\bigr)}\,dx\right).}$$

Griffiths Chapter 9 develops this carefully. The semiclassical condition (slowly varying $V$) means WKB is approximate; it fails near the classical turning points (where $V = E$ and $|p| = 0$), and the standard connection-formula machinery (Griffiths §9.3) patches the approximation across those points.

## 5. Worked examples

### Worked Example 1: Probability in the central third of the box

For a particle in the infinite square well of width $L$, compute the probability of finding it in the central third, $L/3 \leq x \leq 2L/3$, in the states $n = 1$ and $n = 2$.

For general $n$, the probability density is $|\psi_n(x)|^2 = (2/L)\sin^2(n\pi x/L)$. The probability over the central third is

$$P_n = \frac{2}{L}\int_{L/3}^{2L/3} \sin^2\!\left(\frac{n\pi x}{L}\right) dx.$$

Use $\sin^2\theta = (1 - \cos 2\theta)/2$:

$$P_n = \frac{1}{L}\int_{L/3}^{2L/3}\!\left[1 - \cos\!\left(\frac{2n\pi x}{L}\right)\right] dx = \frac{1}{L}\!\left[\frac{L}{3} - \frac{L}{2n\pi}\sin\!\left(\frac{2n\pi x}{L}\right)\Big|_{L/3}^{2L/3}\right].$$

Simplify:

$$P_n = \frac{1}{3} - \frac{1}{2n\pi}\!\left[\sin\!\left(\frac{4n\pi}{3}\right) - \sin\!\left(\frac{2n\pi}{3}\right)\right].$$

For $n = 1$: $\sin(4\pi/3) = -\sqrt{3}/2$, $\sin(2\pi/3) = +\sqrt{3}/2$, so the bracket is $-\sqrt{3}$, and

$$P_1 = \frac{1}{3} + \frac{\sqrt{3}}{2\pi} \approx 0.333 + 0.276 \approx 0.609.$$

For $n = 2$: $\sin(8\pi/3) = \sin(2\pi/3) = +\sqrt{3}/2$, $\sin(4\pi/3) = -\sqrt{3}/2$, so the bracket is $+\sqrt{3}$, and

$$P_2 = \frac{1}{3} - \frac{\sqrt{3}}{4\pi} \approx 0.333 - 0.138 \approx 0.196.$$

**Lesson.** For $n = 1$ the wave function piles up in the middle (no nodes inside the well), so the central third carries more than a third of the probability. For $n = 2$ the wave function has a node exactly at $x = L/2$, so the central third is depleted. The structure of the probability density is the structure of the wave function squared — there is nothing hidden behind it.

**Limit.** This calculation works for any $n$ and any sub-interval; the integrals are elementary. For large $n$, the rapid oscillation of $\sin^2$ averages to $1/2$, so $P_n \to 1/3$ (the classical answer — a uniform distribution gives equal probability per equal length). This is one face of the correspondence principle.

### Worked Example 2: Gamow's alpha-decay calculation

A heavy nucleus emits an alpha particle. Classically, the alpha sits inside the nucleus at the bottom of a strong attractive nuclear potential, surrounded by a Coulomb barrier on the outside. The barrier height at the nuclear surface (radius $R \approx 7$ fm for a uranium nucleus) is roughly

$$V_C = \frac{2(Z-2)e^2}{4\pi\epsilon_0 R}$$

where the alpha has charge $+2e$ and the residual nucleus has charge $(Z-2)e$. For $Z = 92$ (uranium-238), $V_C \approx 28$ MeV. But emitted alpha particles from U-238 carry only about $4.27$ MeV of kinetic energy [verify: standard nuclear data tables, e.g., NNDC]. Classically the alpha could never escape. Quantum-mechanically, it tunnels.

Apply the WKB formula. Inside the barrier (between the nuclear radius $r_1 = R$ and the outer turning point $r_2$ where $V(r) = E$), the potential is Coulombic, $V(r) = 2(Z-2)e^2 / (4\pi\epsilon_0 r)$, and the transmission exponent is

$$\gamma = \frac{2}{\hbar}\int_{r_1}^{r_2}\sqrt{2m\bigl(V(r) - E\bigr)}\,dr.$$

The outer turning point satisfies $V(r_2) = E$, i.e., $r_2 = 2(Z-2)e^2/(4\pi\epsilon_0 E)$. Doing the integral (it has a closed form involving $\arccos$; see Griffiths §9.4) in the thick-barrier limit $r_2 \gg r_1$ gives the Gamow factor:

$$\gamma \approx \frac{2}{\hbar}\sqrt{2m E}\cdot\frac{\pi}{2}(r_2 - 2\sqrt{r_1 r_2}) \approx \pi\,\frac{2(Z-2)e^2}{4\pi\epsilon_0\hbar v}$$

where $v = \sqrt{2E/m}$ is the asymptotic velocity. Plug in numbers: $E = 4.27$ MeV gives $v \approx 1.43 \times 10^7$ m/s, and $(Z-2) = 90$. The Coulomb-tunneling factor $2(Z-2)e^2/(4\pi\epsilon_0 \hbar v)$ evaluates to about $\sim 28$, so $\gamma \approx 28\pi \approx 88$. The transmission probability per assault on the barrier is $T = e^{-2\gamma} \approx e^{-176} \approx 10^{-77}$ [order-of-magnitude estimate; the precise value depends on the exact treatment of $r_1$ and the pre-exponential factor — see Griffiths §9.4 for the careful derivation].

To get a half-life, multiply by the assault frequency $v/R \approx 2 \times 10^{21}$ s$^{-1}$:

$$\tau^{-1} \approx \frac{v}{R}\,e^{-2\gamma}, \qquad \tau \approx \frac{R}{v}\,e^{2\gamma}.$$

This gives a half-life on the order of $10^{17}$ seconds, or roughly $10^9$ years. The measured half-life of U-238 is $4.5 \times 10^9$ years. Order-of-magnitude agreement, from a one-page calculation that George Gamow published in 1928 (*Zeitschrift für Physik* 51, 204) [verify pagination against original]. Gurney and Condon published an independent version in *Nature* the next day.

**Lesson.** The half-life depends *exponentially* on $\gamma$, which depends only on $Z$ and $E$. Alpha-decay half-lives across the periodic table span 24 orders of magnitude (from microseconds for Po-212 to $10^{17}$ years for Th-232) [verify: standard nuclear data]. That entire range is generated by modest changes in $Z$ and $E$ inside an exponential. Exponentials are unforgiving — a small change in the input becomes a large change in the output. This is why the Geiger-Nuttall law (empirical fit relating alpha energy to half-life) had been mysterious for decades and why Gamow's calculation, when it landed, was the first major quantitative success of quantum mechanics applied to nuclei.

**Limit.** The numerical agreement is order-of-magnitude. Improving it requires better treatment of the assault frequency, the nuclear-surface boundary condition, and the angular-momentum structure of the alpha (forbidden transitions tighten the half-life). The WKB skeleton is right; the details are 90 years of subsequent nuclear physics.

### Worked Example 3: The harmonic oscillator ground state from $\hat{a}_-|0\rangle = 0$

Already shown in 4C above: requiring $\hat{a}_-|0\rangle = 0$ in position representation gives

$$\frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\,\psi_0,$$

whose normalized solution is

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-m\omega x^2/(2\hbar)}.$$

This is the entire content of the ground state. The width of the Gaussian is $x_0 = \sqrt{\hbar/(m\omega)}$ — set by $\hbar$ and the spring constant alone. The state is a *coherent* Gaussian; it does not oscillate or move; it has zero-point energy $\hbar\omega/2$ and saturates the Robertson uncertainty bound (you will verify $\sigma_x \sigma_p = \hbar/2$ in Unit 5).

## 6. Reading map

| Topic | Griffiths (4th ed.) | Pop-sci book | Companion |
|---|---|---|---|
| Infinite square well | §2.2 | (absent — TIKTOC IV) | §4A |
| Harmonic oscillator (algebraic) | §2.3.1 | (absent) | §4B |
| Harmonic oscillator (analytic) | §2.3.2 | (absent) | §4C |
| Finite square well | §2.6 | (absent) | §4D |
| Tunneling, rectangular barrier | §2.7 | Ch. 9 [BOOK ✅] | §4E |
| WKB approximation | Ch. 9 | (absent) | §4E |
| Alpha decay (Gamow 1928) | §9.4 | Ch. 9 (qualitative) | Worked Ex. 2 |
| STM application | (not standard) | Ch. 9 (catalog) | §4E |

## 7. Exercises

**1. (Bloom: Remember.)** Write down the eigenfunctions and energy spectra for (a) the infinite square well of width $L$ and (b) the one-dimensional harmonic oscillator with frequency $\omega$. State the ground-state energy in each case and identify the source of the nonzero zero-point energy in plain English.

**2. (Bloom: Understand.)** Sketch $\psi_n(x)$ and $|\psi_n(x)|^2$ for $n = 1, 2, 3$ in the infinite square well. Mark all nodes and antinodes. Explain why $|\psi_3|^2$ averaged over any interval longer than $L/3$ approaches the classical result $1/L$.

**3. (Bloom: Apply.)** Repeat Worked Example 1 for the *left* third of the box ($0 \leq x \leq L/3$) in the $n = 2$ state. By symmetry, your answer should be the same as the *right* third (it is). Then compute the *full* probability sum $P_{\text{left}} + P_{\text{middle}} + P_{\text{right}}$ and confirm it equals $1$.

**4. (Bloom: Apply.)** Use the ladder operators to compute $\langle\hat{x}^2\rangle$ and $\langle\hat{p}^2\rangle$ in the $n$-th eigenstate of the harmonic oscillator. (Hint: write $\hat{x}$ and $\hat{p}$ in terms of $\hat{a}_\pm$, then use $\hat{a}_-|n\rangle = \sqrt{n}|n-1\rangle$, $\hat{a}_+|n\rangle = \sqrt{n+1}|n+1\rangle$.) Show that $\langle\hat{x}^2\rangle\langle\hat{p}^2\rangle = (n + 1/2)^2 \hbar^2$, so the Robertson bound $\sigma_x\sigma_p \geq \hbar/2$ is saturated only for $n = 0$.

**5. (Bloom: Analyze.)** For a finite square well of depth $V_0 = 50$ eV and width $2a = 0.5$ nm, holding an electron, compute the dimensionless depth $z_0$. Solve the even-parity transcendental equation $z\tan z = \sqrt{z_0^2 - z^2}$ graphically. How many bound states does the well support? Estimate the ground-state energy.

**6. (Bloom: Apply.)** A particle of energy $E$ encounters a triangular barrier $V(x) = V_0(1 - x/L)$ for $0 \leq x \leq L$ (and zero outside). Use the WKB formula to compute the transmission coefficient and compare to the rectangular-barrier result for the same area-under-the-curve. Which transmits more? (Hint: do the WKB integral; the triangle has half the area of a rectangle of the same height and width.)

**7. (Bloom: Synthesize / Evaluate.)** Read the pop-sci book's Chapter 9 description of quantum tunneling. Pick one specific factual claim it makes about an application (STM, flash memory, fusion, alpha decay, biological tunneling). State the claim in one sentence. Then use the math from this chapter to either confirm, sharpen, or correct it. If the claim is qualitatively right but quantitatively unmotivated, supply the quantitative argument the pop-sci book left out.

**8. (Bloom: Synthesize.)** Estimate the half-life of polonium-212 ($Z = 84$, alpha energy $E \approx 8.78$ MeV) [verify against nuclear data tables] using the Gamow approach in Worked Example 2. Compare to the measured value ($\sim 0.3 \mu$s). Then redo the estimate for thorium-232 ($Z = 90$, $E \approx 4.08$ MeV) and compare to its measured $1.4 \times 10^{10}$-year half-life. Comment on the dynamic range.

## 8. What would change my mind

The chapter rests on two empirical claims: (1) one-dimensional toy models predict real laboratory observables, and (2) the exponential dependence of tunneling on barrier integral is correct. If experiments routinely showed transmission probabilities that did *not* follow $T \sim e^{-2\gamma}$ — for example, if STM tunneling currents varied as a power law rather than an exponential in tip-sample distance, or if alpha-decay half-lives did not collapse onto a Geiger-Nuttall line when plotted against $Z/\sqrt{E}$ — the WKB framework would be in trouble. If, alternatively, careful experiments showed that confined quantum systems can have ground-state energy *exactly* zero, the entire uncertainty-principle scaffolding of this chapter would collapse. Neither of these has happened in a century of measurement. A specific result that would force revision: an attoclock experiment demonstrating that an electron tunnels with a *negative* group delay through a thick Coulomb barrier in a way no WKB-based theory can accommodate. The 2019 Sainadh et al. *Nature* result on hydrogen attoclock tunneling [verify volume/page] is currently the most provocative result in this neighborhood, and the interpretation remains under debate.

## 9. Still puzzling

1. **Tunneling time.** The transmission probability is uncontroversial; how long the particle "spends in the barrier" is not. Multiple definitions (Wigner time, Larmor time, Büttiker-Landauer time) give different answers, and recent attoclock experiments (Sainadh et al. 2019, [verify]) have reopened the question. The math from this chapter gives $T$, not $\tau_{\text{tunnel}}$.

2. **Zero-point energy and the cosmological constant.** Every quantum mode has $\hbar\omega/2$ ground-state energy. Summing over all modes of the vacuum electromagnetic field gives a vacuum energy density off by 120 orders of magnitude from the cosmological observation. The arithmetic in this chapter is correct; what we should do with the sum is not understood.

3. **The harmonic-oscillator generality.** Every smooth minimum looks quadratic *to leading order*. Anharmonic corrections are perturbative, but for some systems (loose floppy molecules, very low-frequency lattice modes) the harmonic picture badly underestimates physical observables. When does the harmonic approximation stop being useful, and what replaces it cleanly? Standard answers exist (Morse potential, anharmonic perturbation theory) but no single clean replacement.

4. **The 1D-to-3D transition.** A 1D well always binds; a 3D well needs critical depth. This is a sharp dimensional discontinuity. The student should understand it not as a quirk but as a genuine feature of the dimensionality of space. Why dimension matters here — and exactly here — for binding is something a careful student should be unsettled by even after computing the math.

---

**Tags:** infinite-square-well, harmonic-oscillator, ladder-operators, WKB, tunneling, alpha-decay, Gamow, STM, Griffiths-Ch-2, zero-point-energy

*Draft for Nik's review. Voice-anchored against root style/. Flags: HCl spectroscopy numbers not used in this draft (deferred); Gamow page numbers and Sainadh citation tagged `[verify]`.*
