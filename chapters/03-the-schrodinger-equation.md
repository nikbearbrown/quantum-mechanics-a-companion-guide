# Unit 3 — The Schrödinger Equation

> The equation that runs quantum mechanics was postulated, not derived. This unit shows you what it says, why $|\psi|^2$ is a probability, and how to read a stationary state without thinking it is static.

---

## 1. What this chapter is doing

Schrödinger's equation is the dynamical core of non-relativistic quantum mechanics. Griffiths Ch. 1 introduces it; Griffiths Ch. 2.1 unpacks stationary states and time evolution; Griffiths Ch. 2.4 covers the free particle. The pop-sci companion *Quantum Physics for Beginners* (2021) names the equation in its Ch. 12 — TIKTOC marks this ⚠️ because the equation appears but is not analyzed — and mentions $|\psi|^2$ briefly in Ch. 5 (also ⚠️). Neither source teaches the student to *use* the equation. The companion's job here is to take what is named in the pop-sci book and partially developed in Griffiths and turn it into a working tool. By the end of this unit, you should be able to write the time-dependent and time-independent Schrödinger equations, justify them with a plausibility argument while being honest that they are postulates, apply the Born rule to compute probabilities, check normalization, calculate a probability current, and read a stationary state without making the most common student error (thinking it is static).

This unit is the bridge from "we need a wave equation for matter" (Unit 1) and "here are the formal tools" (Unit 2) to "let's solve specific problems" (Unit 4).

## 2. Learning objectives

By the end of this unit, you should be able to:

- **Write** the time-dependent Schrödinger equation in one dimension and identify each term. (Bloom L1)
- **State** the Born rule and explain what $|\psi|^2 dx$ represents. (L1)
- **Verify** that a given $\psi(x,t)$ satisfies the time-dependent Schrödinger equation for a given $V(x,t)$. (L3)
- **Compute** the probability current for a given $\psi$, and check the continuity equation. (L3)
- **Show** that normalization is preserved by time evolution when $\hat{H}$ is Hermitian. (L4)
- **Derive** the time-independent Schrödinger equation by separation of variables from the time-dependent equation. (L4)
- **Construct** a superposition of two energy eigenstates and show that $\langle x \rangle(t)$ oscillates at the Bohr frequency $(E_2 - E_1)/\hbar$. (L6)

## 3. The motivating problem

In late 1925, Erwin Schrödinger took his Christmas vacation at the Villa Herwig in Arosa, in the Swiss Alps. Walter Moore's biography (*Schrödinger: Life and Thought*, Cambridge University Press, 1989) recounts the visit in some detail [*verify exact chapter*]. Schrödinger was 38, recently married, and had brought along the page proofs of an unpublished comment Einstein had made about de Broglie's matter-wave hypothesis. He had also, apparently, brought a companion who was not his wife — a historical detail his biographer treats with some delicacy and which has become a staple of physics folklore. By the time he came back down the mountain in January 1926, he had written what is now called the Schrödinger equation.

The first paper appeared in *Annalen der Physik* in January 1926 [Schrödinger, *Annalen der Physik* 79, 361–376](https://doi.org/10.1002/andp.19263840404). Three more papers followed within months, building the formalism and applying it to hydrogen. The motivating idea was to find a wave equation whose eigenvalue spectrum reproduced the Bohr energy levels of hydrogen — the discrete $E_n = -13.6\,\text{eV}/n^2$ that the Balmer, Lyman, and Paschen spectra demanded. Heisenberg, Born, and Jordan had reached the same physics through matrix mechanics six months earlier, but Schrödinger's wave-equation formulation looked more like what physicists were used to and rapidly became the standard pedagogical entry point.

Here is the problem you should hold in your head. Unit 1 gave you five constraints (Planck, photoelectric, Compton, de Broglie, Franck–Hertz) that any successor to classical physics has to meet. Unit 2 gave you the mathematical apparatus (Hilbert space, Hermitian operators, eigenvalues) that the formalism uses. What is missing is a *dynamical law* — an equation that tells you how the state evolves in time. Classical physics has Newton's $\vec{F} = m\vec{a}$ for that role. Quantum physics needs its analog. The Schrödinger equation is it.

But — and this is the honesty move that Unit 3 has to make explicitly — *the Schrödinger equation is not derived.* It is postulated. There is a plausibility argument that makes the equation seem natural given de Broglie's $\lambda = h/p$ and Einstein's $E = h\nu$; the argument is worth running because it gives the equation its right limiting structure. But running the argument is not the same as deriving the equation from anything more basic. The Schrödinger equation has the same status as Newton's second law: a fundamental law that we accept because of what it explains, not because we have a deeper theory it follows from.

## 4. Five tools, again

### 4.1 The Schrödinger equation is postulated, not derived

Griffiths is explicit about this in §1.1 of the 3rd edition: "Where did Schrödinger's equation come from? In a sense, it cannot be derived; it represents a radically new departure from classical physics." The companion echoes him because this is the single most common point of confusion for an undergraduate. You will see plausibility arguments in lectures and in popular treatments that look like derivations. They are not derivations. They are constructions that show the equation has the right limiting behavior. Why nature uses this equation rather than some neighboring one is a question without a deeper answer in the framework of non-relativistic QM.

**The plausibility argument.** Take de Broglie's matter wave for a free particle:

$$ \psi(x,t) = A\, e^{i(kx - \omega t)}, \quad p = \hbar k, \quad E = \hbar\omega. $$

Differentiate once in $t$:

$$ \frac{\partial\psi}{\partial t} = -i\omega \psi = -\frac{i}{\hbar} E \psi \implies i\hbar \frac{\partial\psi}{\partial t} = E\psi. $$

Differentiate twice in $x$:

$$ \frac{\partial^2\psi}{\partial x^2} = -k^2 \psi = -\frac{p^2}{\hbar^2}\psi \implies -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} = \frac{p^2}{2m}\psi. $$

For a free particle, $E = p^2/2m$. So $i\hbar\partial_t \psi$ and $-(\hbar^2/2m)\partial_x^2 \psi$ are equal for the plane-wave solution. That gives the free-particle equation

$$ i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}. $$

Generalize by adding a potential $V(x,t)$ (which we accept as classically familiar — kinetic plus potential energy is the total energy in classical mechanics) and you get the *time-dependent Schrödinger equation*:

$$ \boxed{\, i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x,t)\,\psi(x,t).\,} $$

In operator language, with $\hat{H} = \hat{p}^2/2m + V(\hat{x},t)$ and $\hat{p} = -i\hbar\,\partial_x$,

$$ i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi. $$

Three features the argument does not prove but the equation builds in:

1. **Linearity.** The equation is linear in $\psi$, so if $\psi_1$ and $\psi_2$ are solutions, $\alpha\psi_1 + \beta\psi_2$ is also a solution. This is the superposition principle, and it is what makes interference possible.
2. **First-order in time.** Specifying $\psi$ at one instant determines $\psi$ at all later instants. Compare to the classical wave equation $\partial_t^2 \psi = c^2 \partial_x^2 \psi$, which is second-order in time and needs both $\psi$ and $\partial_t\psi$ at $t=0$ as initial data. The Schrödinger equation needs only $\psi$.
3. **The factor of $i$.** Without it, the equation would be the diffusion equation $\partial_t \psi = (\hbar/2m)\,\partial_x^2 \psi$, which spreads any initial condition irreversibly. The $i$ rotates this into a wave equation that preserves $\int|\psi|^2 dx$ — see §4.3.

Each of these is a postulate built into the equation, not a consequence of de Broglie and Einstein.

**Misconception alert.** "The Schrödinger equation comes from energy conservation, $E = K + V$." The form of the equation matches the *operator* version of this — $\hat{H} = \hat{p}^2/2m + V(\hat{x})$, where $\hat{p}$ acts as $-i\hbar\,\partial_x$. But the substitution $p \to -i\hbar\,\partial_x$ is the postulate. Classical energy conservation doesn't tell you momentum is a differential operator. The structural identification of $\hat{p}$ with $-i\hbar\,d/dx$ comes from the requirement that the canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$ hold, which is itself a postulate of the theory.

**Worked example: free-particle plane wave.** Verify that $\psi(x,t) = A\,e^{i(kx - \omega t)}$ with $\omega = \hbar k^2/2m$ solves the free-particle Schrödinger equation. Left side:

$$ i\hbar\,\partial_t \psi = i\hbar\,(-i\omega)\,\psi = \hbar\omega\,\psi. $$

Right side:

$$ -\frac{\hbar^2}{2m}\partial_x^2 \psi = -\frac{\hbar^2}{2m}(-k^2)\psi = \frac{\hbar^2 k^2}{2m}\psi. $$

These are equal iff $\hbar\omega = \hbar^2 k^2/2m$, i.e., $\omega = \hbar k^2/2m$. Solved. The dispersion relation $E = p^2/2m$ shows up as $\hbar\omega = (\hbar k)^2/2m$ in wave variables.

*The lesson:* the Schrödinger equation is consistent with the de Broglie–Einstein relations and reduces to classical mechanics in the appropriate limit. That makes it a candidate; experiment confirms it.

### 4.2 The Born rule: $|\psi|^2$ as probability density

Schrödinger initially proposed that $|\psi|^2$ was the *charge density* of an electron — that the electron was a smeared-out matter wave. The interpretation lasted weeks. Max Born proposed in 1926 [Born, *Zeitschrift für Physik* 37, 863–867](https://doi.org/10.1007/BF01397477) that

$$ |\psi(x,t)|^2 dx = \text{probability of finding the particle in } [x, x+dx] \text{ at time } t. $$

$\psi$ itself is not observable. $|\psi|^2$ is a probability density. Born received the 1954 Nobel Prize for this interpretation — 28 years after the paper, an unusual delay that partly reflects how controversial the probabilistic interpretation was through the 1920s and 1930s.

Schrödinger's matter-wave interpretation failed for two reasons. First, $\psi$ is complex, and there is no classical notion of a complex matter density. (You could try $\text{Re}(\psi)$ or $|\psi|$, but neither obeys a linear equation, and superposition would break.) Second, for two particles, $\psi$ is a function of *six* coordinates — $\psi(x_1, y_1, z_1, x_2, y_2, z_2, t)$ — and a function on six-dimensional configuration space cannot be a physical wave in three-dimensional space. Born's probability interpretation accommodated both: probabilities are real, and a probability distribution on configuration space is a perfectly well-defined object.

For the Born rule to be a consistent probability assignment, three conditions must hold:

1. **Non-negativity.** $|\psi|^2 \geq 0$ everywhere. Automatic: it is a squared modulus.
2. **Normalization.** $\int_{-\infty}^\infty |\psi(x,t)|^2\, dx = 1$. The particle has to be *somewhere* — total probability is 1.
3. **Conservation under time evolution.** If (2) holds at $t = 0$, it holds at all later $t$.

Condition (3) is non-trivial. It is what § 4.3 proves, and it ties directly to the Hermiticity of $\hat{H}$.

**Two misconceptions.**

*"$\psi$ is the particle."* No. $\psi$ is the probability amplitude. The particle is what registers in a detector. Before detection, what exists is the amplitude. After detection, what you have measured is a position (or whatever observable the detector measures). The image of a particle as "a cloud spread over a region" is wrong; the cloud is the cloud of *probabilities* for where the point will appear.

*"$|\psi|^2$ is a hidden variable telling us what we don't know about the particle's actual position."* No. Bell-inequality experiments — Aspect 1982, refined many times since, recognized with the 2022 Nobel to Aspect, Clauser, Zeilinger — rule out local hidden-variable theories that would make this story work. The probability is irreducible, not a stand-in for incomplete classical knowledge. Unit 5 will return to this.

**Worked example: ground state of an infinite square well.** Take a particle confined to $0 \leq x \leq L$ in the ground state $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$. (Unit 4 derives this; for now, take it.) Compute the probability of finding the particle in the left quarter of the well, $[0, L/4]$.

$$ P = \int_0^{L/4} |\psi_1(x)|^2\,dx = \frac{2}{L}\int_0^{L/4} \sin^2\!\left(\frac{\pi x}{L}\right)\,dx. $$

Use $\sin^2 u = (1 - \cos 2u)/2$:

$$ P = \frac{2}{L}\int_0^{L/4} \frac{1 - \cos(2\pi x/L)}{2}\,dx = \frac{1}{L}\left[x - \frac{L}{2\pi}\sin\!\left(\frac{2\pi x}{L}\right)\right]_0^{L/4}. $$

Evaluating:

$$ P = \frac{1}{L}\left[\frac{L}{4} - \frac{L}{2\pi}\sin\!\left(\frac{\pi}{2}\right) - 0\right] = \frac{1}{4} - \frac{1}{2\pi} \approx 0.25 - 0.159 = 0.091. $$

About 9%, not 25%. The ground state is *concentrated near the middle* of the well, so the leftmost quarter is depleted of probability. This is the cleanest calculation in this unit and illustrates how the Born rule is used in practice.

*The lesson:* a wave function is not a particle. Squared modulus, integrated over a region, is a probability. Always.

### 4.3 Normalization is preserved by time evolution

A wave function $\psi(x,t)$ is *normalizable* if $\int|\psi|^2\,dx$ is finite, and *normalized* if the integral equals 1. The key result of this section: if $\psi$ is normalized at $t = 0$ and $\psi$ evolves by the Schrödinger equation with a Hermitian Hamiltonian, then $\psi$ remains normalized for all $t$.

Differentiate the integral under the integral sign:

$$ \frac{d}{dt}\int_{-\infty}^\infty |\psi|^2\,dx = \int_{-\infty}^\infty \frac{\partial}{\partial t}(\psi^* \psi)\,dx = \int \left(\psi^* \frac{\partial\psi}{\partial t} + \frac{\partial\psi^*}{\partial t}\psi\right)dx. $$

From the Schrödinger equation, $\partial_t \psi = (\hat{H}\psi)/(i\hbar) = -(i/\hbar)\hat{H}\psi$. Taking the complex conjugate (and noting $\hat{H}^* = \hat{H}^\dagger$ acting on $\psi^*$, but for the standard real-potential Hamiltonian we have $\hat{H}^* = \hat{H}$ in the position representation):

$$ \frac{\partial\psi^*}{\partial t} = +\frac{i}{\hbar}(\hat{H}\psi)^* . $$

So

$$ \frac{d}{dt}\int|\psi|^2\,dx = \int \left[-\frac{i}{\hbar}\psi^*(\hat{H}\psi) + \frac{i}{\hbar}(\hat{H}\psi)^*\psi\right]dx = -\frac{i}{\hbar}\left[\int\psi^* \hat{H}\psi\,dx - \int(\hat{H}\psi)^*\psi\,dx\right]. $$

The bracket is $\langle\psi|\hat{H}\psi\rangle - \langle\hat{H}\psi|\psi\rangle$ in Dirac notation. By Hermiticity of $\hat{H}$, $\langle\psi|\hat{H}\psi\rangle = \langle\hat{H}\psi|\psi\rangle$, and the bracket vanishes:

$$ \frac{d}{dt}\int|\psi|^2\,dx = 0. $$

Normalization is preserved. Notice exactly what the proof used: the Hermiticity of $\hat{H}$. This is the structural reason QM postulates that observables are Hermitian operators — without Hermiticity, the Born rule would not be a probability assignment that survives time evolution.

**The probability current and the continuity equation.** Step back and look at this same calculation locally. Define $\rho(x,t) = |\psi(x,t)|^2$ — the probability density. Define the *probability current*

$$ j(x,t) = \frac{\hbar}{2mi}\left(\psi^*\frac{\partial\psi}{\partial x} - \psi\frac{\partial\psi^*}{\partial x}\right) = \frac{\hbar}{m}\,\text{Im}\!\left(\psi^*\frac{\partial\psi}{\partial x}\right). $$

The local conservation law is the *continuity equation*:

$$ \frac{\partial\rho}{\partial t} + \frac{\partial j}{\partial x} = 0. $$

This is the local statement of probability conservation. Probability does not vanish at one point and reappear elsewhere; it flows. If probability is leaving a region, it has to be flowing across the boundary, and the rate of flow is $j$.

**Deriving the continuity equation.** Compute $\partial_t \rho = \partial_t (\psi^* \psi) = \psi^* \partial_t\psi + \psi \partial_t \psi^*$. Use the Schrödinger equation for $\partial_t\psi$ (with $V$ real, so $V \psi^* = V^*\psi^*$):

$$ \partial_t \psi = \frac{1}{i\hbar}\left[-\frac{\hbar^2}{2m}\partial_x^2 \psi + V\psi\right], \qquad \partial_t \psi^* = -\frac{1}{i\hbar}\left[-\frac{\hbar^2}{2m}\partial_x^2 \psi^* + V\psi^*\right]. $$

Substitute:

$$ \partial_t \rho = \frac{1}{i\hbar}\left[\psi^*\left(-\frac{\hbar^2}{2m}\partial_x^2\psi + V\psi\right) - \psi\left(-\frac{\hbar^2}{2m}\partial_x^2 \psi^* + V\psi^*\right)\right]. $$

The $V$ terms cancel (the potential is real). What remains:

$$ \partial_t\rho = -\frac{\hbar}{2mi}\left[\psi^*\partial_x^2\psi - \psi\partial_x^2\psi^*\right]. $$

Now notice that $\partial_x(\psi^*\partial_x\psi - \psi\partial_x\psi^*) = \psi^*\partial_x^2\psi - \psi\partial_x^2\psi^*$ — the product-rule cross terms cancel. So

$$ \partial_t\rho = -\frac{\hbar}{2mi}\,\partial_x(\psi^*\partial_x\psi - \psi\partial_x\psi^*) = -\partial_x j. $$

That is the continuity equation. The derivation is purely local; integrate over all $x$ and the right side becomes a boundary term that vanishes for square-integrable $\psi$, giving the global statement $d/dt \int|\psi|^2 = 0$ as a consequence.

**Worked example: probability current for a plane wave.** For $\psi = A\,e^{i(kx - \omega t)}$, compute $j$. We have $\psi^* = A^* e^{-i(kx-\omega t)}$ and $\partial_x\psi = ik\,\psi$. Then

$$ \psi^* \partial_x \psi = A^* e^{-i(kx-\omega t)} \cdot ik\,A\,e^{i(kx-\omega t)} = ik|A|^2. $$

And $\psi\partial_x\psi^* = -ik|A|^2$ similarly. So

$$ j = \frac{\hbar}{2mi}(ik|A|^2 - (-ik|A|^2)) = \frac{\hbar}{2mi}(2ik|A|^2) = \frac{\hbar k}{m}|A|^2 = \frac{p}{m}|A|^2 = v|A|^2. $$

The probability current is density times velocity — the classical expression for a flowing fluid. This is reassuring: in the limit where the wave-function picture should look classical, the probability current behaves like a particle current.

**Misconception alert.** "Normalization is a technicality." It is not. It is the physical statement that the particle exists somewhere — total probability is 1. Wave functions that cannot be normalized — like the plane wave above, where $\int|A|^2\,dx = \infty$ — are not physical states. They are calculational devices that have to be assembled into wave packets (linear combinations) before they can describe an actual particle. § 4.5 will return to this.

### 4.4 Stationary states: time-independent Schrödinger equation

If the potential $V(x)$ does not depend on time, the time-dependent Schrödinger equation admits solutions of the form

$$ \psi(x,t) = \psi(x)\, e^{-iEt/\hbar}. $$

Such a $\psi$ is called a *stationary state*. Substitute into the Schrödinger equation:

$$ i\hbar\,\partial_t\left[\psi(x) e^{-iEt/\hbar}\right] = i\hbar\left(-\frac{iE}{\hbar}\right)\psi(x) e^{-iEt/\hbar} = E\,\psi(x)\,e^{-iEt/\hbar}. $$

Right side:

$$ \hat{H}\left[\psi(x) e^{-iEt/\hbar}\right] = e^{-iEt/\hbar} \hat{H}\psi(x). $$

The time-dependent phase factors out and cancels. What remains is the *time-independent Schrödinger equation*:

$$ \boxed{\, \hat{H}\psi(x) = E\,\psi(x).\,} $$

This is an *eigenvalue equation* for the Hamiltonian. The function $\psi(x)$ is an eigenfunction; the real number $E$ is the corresponding eigenvalue. The eigenvalues $E$ are the *allowed energies*.

Why "stationary"? Because $|\psi(x,t)|^2 = |\psi(x) e^{-iEt/\hbar}|^2 = |\psi(x)|^2$. The probability density is time-independent. The expectation value of any time-independent operator is also constant. Hence "stationary."

But notice carefully what is time-independent and what is not. The *probability density* is constant. The *amplitude* $\psi(x,t)$ rotates in the complex plane at angular frequency $E/\hbar$. The magnitude at each $x$ is fixed; the phase advances at rate $E/\hbar$. For a single stationary state in isolation, this phase rotation has no observable consequence, because every measurement probability depends only on $|\psi|^2$.

**The misconception that ruins everything.** "Stationary states are static." No. The phase rotates. The phase matters in *superpositions*. Take two stationary states $\psi_1(x)$ with energy $E_1$ and $\psi_2(x)$ with energy $E_2$, and form a superposition:

$$ \psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1 t/\hbar} + \psi_2(x)\,e^{-iE_2 t/\hbar}\right]. $$

Compute $|\psi|^2$:

$$ |\psi|^2 = \frac{1}{2}\left[|\psi_1|^2 + |\psi_2|^2 + 2\,\text{Re}\!\left(\psi_1^*\psi_2\,e^{-i(E_2 - E_1)t/\hbar}\right)\right]. $$

The cross term *oscillates*. It contains the factor $e^{-i(E_2-E_1)t/\hbar}$, which has real part $\cos(\omega t)$ with $\omega = (E_2 - E_1)/\hbar$ — the *Bohr frequency*. The probability density rocks back and forth at this frequency. The atom radiates a photon of this energy when it decays. This is the source of every spectral line in atomic physics. It exists because the phases of stationary states are not zero; they rotate; their relative rotation produces the observable oscillation.

If you take only one thing from this unit, take this: stationary states are stationary in *probability density*, not in *amplitude*. Their phases rotate, and the phases matter the moment you superpose them.

**Why stationary states are the computational basis.** By the spectral theorem (Unit 2 §4.4), the eigenfunctions of a Hermitian operator form a complete orthonormal basis. So *any* state $\psi(x, 0)$ can be expanded as

$$ \psi(x, 0) = \sum_n c_n \psi_n(x), \quad c_n = \int \psi_n^*(x)\,\psi(x,0)\,dx. $$

Time evolution then becomes trivial:

$$ \psi(x,t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}. $$

Each component picks up its own phase factor. That is the entire algorithm for time evolution under a time-independent Hamiltonian. Find the energy eigenstates, expand your initial condition in them, attach a phase to each, sum back. Almost every solvable problem in QM (particle in a box, harmonic oscillator, hydrogen atom — all of Unit 4 and Unit 6) is an instance of this algorithm.

**Worked example: Bohr oscillation in a particle-in-a-box.** Take a 50-50 superposition of the ground state $\psi_1$ and first excited state $\psi_2$ of a particle in a box of width $L$:

$$ \psi_n(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right),\quad E_n = \frac{n^2\pi^2 \hbar^2}{2mL^2}. $$

The superposition $\psi(x,t) = (1/\sqrt{2})[\psi_1(x)\,e^{-iE_1 t/\hbar} + \psi_2(x)\,e^{-iE_2 t/\hbar}]$. Compute $\langle x\rangle$:

$$ \langle x\rangle = \int_0^L x\,|\psi|^2\,dx = \frac{1}{2}\int x[|\psi_1|^2 + |\psi_2|^2]\,dx + \int x\,\text{Re}\!\left(\psi_1^*\psi_2 e^{-i(E_2 - E_1)t/\hbar}\right)dx. $$

The first piece is time-independent: $(1/2)[\langle x\rangle_1 + \langle x\rangle_2] = (1/2)[L/2 + L/2] = L/2$. (Each stationary state is symmetric about $L/2$.) The second piece carries the time dependence. Since $\psi_1, \psi_2$ are real,

$$ \int x\,\psi_1\psi_2 \cos((E_2 - E_1)t/\hbar)\,dx = \cos(\omega t)\int_0^L x\,\sqrt{\frac{2}{L}}\sin\!\left(\frac{\pi x}{L}\right)\sqrt{\frac{2}{L}}\sin\!\left(\frac{2\pi x}{L}\right)dx, $$

with $\omega = (E_2 - E_1)/\hbar = 3\pi^2\hbar/(2mL^2)$. Evaluate the integral:

$$ \frac{2}{L}\int_0^L x\sin\!\left(\frac{\pi x}{L}\right)\sin\!\left(\frac{2\pi x}{L}\right)dx. $$

Use $\sin a \sin b = (1/2)[\cos(a-b) - \cos(a+b)]$ with $a = \pi x/L, b = 2\pi x/L$: $\sin a\sin b = (1/2)[\cos(\pi x/L) - \cos(3\pi x/L)]$. So the integral becomes

$$ \frac{1}{L}\int_0^L x\cos\!\left(\frac{\pi x}{L}\right)dx - \frac{1}{L}\int_0^L x\cos\!\left(\frac{3\pi x}{L}\right)dx. $$

Each piece is $\int_0^L x\cos(n\pi x/L)\,dx$ with $n = 1$ and $n = 3$. Integration by parts: $\int x\cos(\alpha x)\,dx = (x/\alpha)\sin(\alpha x) + (1/\alpha^2)\cos(\alpha x)$. For $\alpha = n\pi/L$, evaluated from 0 to $L$: $(L^2/(n\pi))\sin(n\pi) + (L^2/(n\pi)^2)[\cos(n\pi) - 1] = (L/(n\pi))^2 \cdot L \cdot [(-1)^n - 1]$. This is $-2L^2/(n\pi)^2$ for odd $n$, zero for even $n$.

So the integral is $(1/L)[-2L^2/\pi^2] - (1/L)[-2L^2/(3\pi)^2] = -2L/\pi^2 + 2L/(9\pi^2) = -(2L/\pi^2)(1 - 1/9) = -16L/(9\pi^2)$.

Putting it together:

$$ \langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos(\omega t),\qquad \omega = \frac{3\pi^2\hbar}{2mL^2}. $$

The expectation value of position oscillates at the Bohr frequency, around the midpoint of the well, with amplitude $16L/(9\pi^2) \approx 0.18 L$. Pure stationary states are stationary; superpositions are not.

*The lesson:* time evolution in QM is computed by expanding in stationary states, attaching phases, and summing. The phase rotation of each stationary state is invisible in isolation but creates observable oscillations in superpositions.

*The limit:* this approach requires a time-independent $V$. For time-dependent potentials, the eigenstates themselves change in time, and you need time-dependent perturbation theory (Unit 9).

### 4.5 The free particle and the wave-packet problem

The free particle has $V = 0$, so the time-independent Schrödinger equation is

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi. $$

Let $k = \sqrt{2mE}/\hbar$. The general solution is

$$ \psi_k(x) = A\,e^{ikx} + B\,e^{-ikx}, $$

a superposition of right-moving and left-moving plane waves with momentum $\pm\hbar k$. The time-dependent stationary state is $\psi(x,t) = \psi_k(x)\,e^{-iEt/\hbar}$ with $E = \hbar^2 k^2/2m$.

The free-particle plane waves *are not normalizable*. Compute $\int|e^{ikx}|^2 dx = \int 1\,dx = \infty$. They are not physical states. They violate condition (2) of the Born rule from §4.2.

How does the formalism survive this? By recognizing that plane waves are *generalized* eigenfunctions in the rigged-Hilbert-space sense (we flagged this in Unit 2 §4.3) and that *physical* states are *wave packets* — linear combinations of plane waves with a normalizable weight function. Write

$$ \psi(x, 0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty \phi(k)\,e^{ikx}\,dk. $$

This is a Fourier expansion; $\phi(k)$ is the momentum-space wave function. If $\phi(k)$ is concentrated near some $k_0$ — say a Gaussian peak of width $\Delta k$ — then $\psi(x, 0)$ is a localized wave packet whose width in position is roughly $1/\Delta k$. This is the Heisenberg uncertainty relation in its sharpest form: a narrow momentum distribution is a broad position distribution and vice versa.

Time evolution is straightforward: each plane-wave component picks up its own phase $e^{-i\omega(k)t}$ with $\omega(k) = \hbar k^2/(2m)$. So

$$ \psi(x,t) = \frac{1}{\sqrt{2\pi}}\int \phi(k)\,e^{i(kx - \omega(k)t)}\,dk. $$

Because $\omega(k)$ is not linear in $k$, different components move at different group velocities, and the wave packet *spreads* as it propagates. Griffiths Ch. 2.4 carries through the Gaussian case explicitly; the position-space width grows as $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/(2m\sigma_0^2))^2}$ for a Gaussian of initial width $\sigma_0$. The wave packet starts narrow, broadens slowly, broadens linearly in $t$ at late times. This spreading is one of the first quantitative effects of QM the student can compute and is the bridge to Unit 4.

**Misconception alert.** "Plane waves are unphysical, so the formalism is broken." The formalism is fine. Plane waves are calculational tools — generalized eigenstates of the momentum operator. They are not physical states because they are not normalizable, but linear combinations of them (wave packets) are perfectly normalizable physical states. The same distinction in Unit 2: the position kets $|x\rangle$ are not normalizable, but they are the basis in which physical states are expanded.

## 5. Synthesis: the equation as a working tool

You now know what the Schrödinger equation says, what $|\psi|^2$ means, how normalization is preserved, how to read a stationary state, and why the free-particle plane wave is a tool rather than a state. Unit 4 is going to take this machinery and apply it to specific potentials — the infinite square well, the harmonic oscillator, the step potential, the tunneling barrier. Each is a different choice of $V(x)$ in the time-independent Schrödinger equation. Each gives a different eigenvalue spectrum. Once you have the eigenstates and the energies, you have everything: time evolution is the algorithm in § 4.4, probability is the Born rule, normalization is automatic if $\hat{H}$ is Hermitian.

The honest moves of Unit 3 are worth restating. The Schrödinger equation is postulated, not derived. The Born rule is postulated, not derived. Both are accepted because of what they explain. The plausibility arguments are useful for orientation; they are not derivations. This is the same status Newton's laws had in classical mechanics, and there is nothing scandalous about it — fundamental laws are tested by their consequences, not by their parentage.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Derivation and structure of the SE | Ch. 1.1–1.2 | Ch. 12 [BOOK ⚠️ — equation named, not derived] | §4.1 (plausibility argument with honesty about postulate status) |
| Wave function interpretation, Born rule | Ch. 1.3 | Ch. 5 [BOOK ⚠️ — brief mention] | §4.2 (full Born rule + worked example) |
| Normalization, probability current | Ch. 1.4–1.5 | ❌ | §4.3 (continuity equation derivation) |
| Stationary states, time evolution | Ch. 2.1 | ❌ | §4.4 (separation of variables, Bohr oscillation) |
| Free particle, wave packets | Ch. 2.4 | ❌ | §4.5 (plane waves, spreading) |

Griffiths Ch. 1 and Ch. 2.1 are essential reading alongside this companion. The pop-sci book's Ch. 12 names the Schrödinger equation; treat it as a one-paragraph piece of historical orientation, then come here for the content. Shankar Ch. 5 is a good second reference. Cohen-Tannoudji, Diu, Laloë *Quantum Mechanics* Vol. 1 Ch. 1 is the rigorous graduate alternative — flagged for later, not needed now.

## 7. Exercises

**E1 (L1, Knowledge).** Write the time-dependent Schrödinger equation in one dimension. Identify the kinetic energy term, the potential energy term, and the time-derivative term. Then write the time-independent version and explain in one sentence how the two are related.

**E2 (L3, Application).** A particle in an infinite square well of width $L$ is in the second excited state $\psi_3(x) = \sqrt{2/L}\sin(3\pi x/L)$. Compute (a) the probability of finding the particle in the central third of the well, $[L/3, 2L/3]$, (b) the expectation value of position $\langle x\rangle$, (c) the energy $E_3$. *Check that (a) is greater than 1/3 — the third excited state is concentrated more in the middle than in the wings.*

**E3 (L3, Application).** Compute the probability current $j(x,t)$ for the wave function $\psi(x,t) = A\,e^{ikx}\cos(\omega t)$, with $A, k, \omega$ real. Is the current zero, constant, or time-dependent? Interpret physically.

**E4 (L4, Analysis).** Show that the time-dependent Schrödinger equation, applied to a separable wave function $\psi(x,t) = \psi(x)\,T(t)$, forces $T(t) = e^{-iEt/\hbar}$ and $\hat{H}\psi(x) = E\psi(x)$. Carry out the separation of variables explicitly. State precisely what hypothesis you have to make about the time-independence of $V$.

**E5 (L4, Analysis).** Verify that $\psi(x,t) = A\exp\!\left(-\frac{x^2}{2a^2}\right)\exp\!\left(-i\frac{\hbar t}{2ma^2}\right)$ is *not* a solution of the free-particle Schrödinger equation, even though both factors look like they might form a stationary state. Identify which equation the function does satisfy. *Hint: compute $\partial_t \psi$ and $-\partial_x^2 \psi$ and compare. You will find the time-dependence is wrong.*

**E6 (L6, Synthesis).** Take a particle in an infinite square well of width $L$ in the equal-amplitude superposition $\psi(x,t) = (1/\sqrt{2})[\psi_1(x)e^{-iE_1 t/\hbar} + \psi_3(x)e^{-iE_3 t/\hbar}]$ (note the indices 1 and 3, not 1 and 2). Compute $\langle x\rangle(t)$. Does it oscillate? Why or why not? *Hint: examine the symmetry of $\psi_1$ and $\psi_3$ about $x = L/2$.*

**E7 (L5, Evaluation).** Read Schrödinger's 1926 introduction (first paper, *Annalen der Physik* 79, 361–376) in which he describes $\psi$ as a real wave of matter. Then read Born's 1926 short paper (*Zeitschrift für Physik* 37, 863–867) introducing the probability interpretation. State in your own words two specific reasons Born's interpretation displaced Schrödinger's within months. *Avoid the temptation to argue Born "was right" — your job is to identify what the physics demanded.*

## 8. What would change my mind

The Schrödinger equation's central claim — that the state of a non-relativistic quantum system evolves under $i\hbar\partial_t\psi = \hat{H}\psi$ with $\hat{H}$ Hermitian, and that $|\psi|^2$ gives a probability density via the Born rule — is the empirical core of the equation. The structural arguments of this unit (normalization preserved, eigenvalue spectrum gives measurement outcomes, stationary states form a complete basis) are theorems that follow from the postulates. What would force me to revise the unit's central claim: a reproducible experiment in a non-relativistic regime where Born-rule probabilities failed to be reproduced by any Hermitian Hamiltonian evolution, or where time evolution provably violated probability conservation. Spontaneous collapse models (GRW: Ghirardi, Rimini, Weber, 1986) propose exactly such a small violation, and ongoing experiments — including searches for collapse-induced X-ray emission in solids — are testing this. To date, the standard Schrödinger evolution has held. A confirmed deviation would force a different equation in this unit; absent one, the equation here is the right one for non-relativistic QM.

## 9. Still puzzling

- *Why a postulate?* Students often feel cheated by the "the equation is postulated" honesty. The companion's position: every fundamental theory has a place where its laws stop having deeper explanations and become axioms. Newton's second law is in the same epistemic position. The status of "postulate" is not a confession of ignorance; it is the right description of where a theory begins. Asking *why* the Schrödinger equation has the form it does — rather than some neighbor — is an open question that probably belongs to a theory beyond non-relativistic QM, perhaps to quantum field theory or to some still-undiscovered framework.

- *The interpretation problem.* The Schrödinger equation gives you $\psi$; the Born rule tells you $|\psi|^2$ is a probability; experiments verify the predictions. None of this tells you what $\psi$ *is*. Is it a real field in some ontological sense (many-worlds), a representation of an observer's information (epistemic interpretations), or a guiding wave for hidden particles (Bohmian mechanics)? The companion is agnostic on this question through Unit 4; Unit 5 will return to it directly. For now, the formalism works regardless of which interpretation you adopt.

- *The measurement problem.* The Schrödinger equation describes unitary, deterministic time evolution. Measurement — according to the standard formulation — is a non-unitary, stochastic update of the state. These two prescriptions are in apparent tension. Decoherence (Zurek 2003) gives a partial answer by showing that interactions with the environment rapidly suppress macroscopic superpositions, but it does not by itself solve the problem of how a definite outcome emerges. Open at the level of foundations; not open at the level of computing experimental predictions.

- *The arrow of time.* The Schrödinger equation is time-reversal symmetric (more precisely, antiunitary symmetry $T: \psi(x,t) \to \psi^*(x,-t)$). Wave packets spread, but they don't *have* to — running the equation backward, a broad packet narrows. Why does physical experience seem to single out the spreading direction? The answer probably lies in thermodynamics and initial conditions, not in the equation itself. The puzzle is real and is not specifically a QM puzzle.

**Tags:** schrödinger-equation, born-rule, probability-current, stationary-states, wave-packets, bohr-frequency, griffiths-ch1, griffiths-ch2, normalization
