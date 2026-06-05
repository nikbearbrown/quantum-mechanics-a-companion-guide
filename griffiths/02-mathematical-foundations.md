# Chapter 2 — Mathematical Foundations


## TL;DR

- The language quantum mechanics is written in — and why nothing simpler will do the job.
- Complex numbers, vector spaces and inner products, Dirac notation, operators and eigenvalues, and the rest of the working toolkit.
- Read it for the argument, the vocabulary, and the judgment it asks of you.

*The language quantum mechanics is written in, and why no simpler language works.*

---

One experiment forces the entire mathematical structure on you. Not because physicists wanted things to be hard — because the experiment *insists*, and you either follow it where it goes or you give up doing physics.

Send electrons, one at a time, through two slits. Each lands somewhere on the screen behind. After ten thousand of them, a pattern emerges: bright bands where many landed, dark bands where almost none did. The bands are interference fringes — the same pattern water waves make passing through two gaps.

But these are electrons. Single electrons. There is no second electron for any one of them to interfere *with*. Whatever interferes is the electron interfering with itself.

Here is where the mathematics is forced. To get the dark bands, the contributions from the two slits have to *cancel* — not add to something small, cancel. Call them $\psi_1$ and $\psi_2$. Add them as $\psi_1 + \psi_2$ and compute intensity as $|\psi_1 + \psi_2|^2$, and you can get cancellation when $\psi_1 = -\psi_2$. Fine, but one cancellation at one angle is not enough. You need alternating bright and dark bands across the whole screen, which means the two contributions have to slide smoothly in sign and magnitude as the angle changes. They need a continuously varying *phase*.

Objects with a continuously varying phase look like $e^{i\varphi}$. And $e^{i\varphi}$ requires $i = \sqrt{-1}$, which requires complex numbers.

This is not a stylistic preference. The experiment offers no alternative.

![Double-slit experiment diagram with single-electron sequential buildup ](../images/02-mathematical-foundations-fig-01.png)
*Figure 2.1 — Double-slit experiment diagram with single-electron sequential buildup *

---

## The arithmetic of complex numbers

A complex number is $z = a + bi$, with $a$ and $b$ ordinary reals and $i^2 = -1$. The real part is $a$, the imaginary part $b$. The *complex conjugate* of $z$ is $z^{*} = a - bi$ — flip the sign on the imaginary part. The *modulus* is

$$|z| = \sqrt{z^{*} z} = \sqrt{a^2 + b^2},$$

a non-negative real number. Picture $a$ and $b$ as coordinates in a plane — the "complex plane," real axis horizontal, imaginary axis vertical — and the modulus is just the distance from the origin.

The fact that makes complex numbers earn their keep in physics is Euler's formula:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

If you want to convince yourself, expand $e^{i\theta}$, $\cos\theta$, and $\sin\theta$ in Taylor series and check that real and imaginary parts match term by term. The upshot: every complex number can be written $z = r\,e^{i\theta}$, with $r = |z|$ its distance from the origin and $\theta$ its angle. Multiplying two complex numbers multiplies their distances and *adds* their angles; conjugating flips the angle, $(re^{i\theta})^{*} = re^{-i\theta}$.

The three facts you will use endlessly:

![The complex plane showing a point z =](../images/02-mathematical-foundations-fig-02.png)
*Figure 2.2 — The complex plane showing a point z =*

- $|e^{i\theta}| = 1$ for any real $\theta$. A pure phase factor never changes the size of anything.
- $e^{i\theta_1} \cdot e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$. Phases add when complex numbers multiply.
- $(z_1 z_2)^{*} = z_1^{*} z_2^{*}$. Conjugation distributes over multiplication.

Now return to the double slit. Label the slits. The amplitude reaching the screen from slit 1 is $\psi_1$, from slit 2 is $\psi_2$. The rule — stated precisely in Unit 3, used informally here — is that you *add the amplitudes* and then *square the modulus* to get intensity. The total amplitude is $\psi = \psi_1 + \psi_2$, and the intensity is $|\psi|^2$.

Take the simplest case: one slit a distance $r$ from the screen point, the other $r + d\sin\theta$ away. Assign equal magnitudes $1/\sqrt{2}$ and phases set by path length:

$$\psi_1 = \frac{1}{\sqrt{2}} e^{ikr}, \qquad \psi_2 = \frac{1}{\sqrt{2}} e^{ik(r + d\sin\theta)},$$

with $k = 2\pi/\lambda$ the wavenumber. Expand $|\psi_1 + \psi_2|^2$:

$$|\psi|^2 = \frac{1}{2}\left[e^{-ikr} + e^{-ik(r+d\sin\theta)}\right]\left[e^{ikr} + e^{ik(r+d\sin\theta)}\right]$$

$$= \frac{1}{2}\left[1 + e^{ikd\sin\theta} + e^{-ikd\sin\theta} + 1\right] = 1 + \cos(kd\sin\theta).$$

Using $1 + \cos x = 2\cos^2(x/2)$:

$$|\psi|^2 = 2\cos^2\!\left(\frac{kd\sin\theta}{2}\right).$$

Maxima where $d\sin\theta = n\lambda$; zeros where $d\sin\theta = (n + 1/2)\lambda$. Bright and dark bands, exactly as observed. The complex exponentials carried that calculation in four lines. Try it with real numbers and the cross term is $2\psi_1\psi_2$ — a fixed sign, no oscillation, no dark bands, no double-slit experiment.

![Plot of |ψ|² = 2cos²(kd sinθ / 2)](../images/02-mathematical-foundations-fig-03.png)
*Figure 2.3 — Plot of |ψ|² = 2cos²(kd sinθ / 2)*

You might hope to escape with real numbers anyway. Stueckelberg showed in 1960 that you can — provided you double the dimension of every space, trading each complex dimension for an extra real one. What you cannot do is reformulate quantum mechanics with real numbers *in the same dimension*. And in 2021 Renou and collaborators tested a whole class of real-amplitude reformulations directly, using Bell inequalities, and ruled them out [Renou et al., *Nature* 600, 625–629 (2021), *verify pagination*]. The complex numbers are not a convention. They are measured.

---

## Vector spaces and inner products

A *vector space* over $\mathbb{C}$ is a set of objects — we'll call them states and write them $|\psi\rangle$ — with two operations: you can add any two ($|\psi\rangle + |\phi\rangle$), and you can multiply any one by a complex number ($\alpha|\psi\rangle$). These obey the usual rules: addition commutes and associates, scalar multiplication distributes. The simplest example is $\mathbb{C}^n$, columns of $n$ complex numbers.

An *inner product* measures the "angle" between two states. It is a map $\langle\cdot|\cdot\rangle: V \times V \to \mathbb{C}$ obeying three conditions:

1. **Conjugate symmetry:** $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^{*}$.
2. **Linear in the second slot:** $\langle\phi|\alpha\psi + \beta\chi\rangle = \alpha\langle\phi|\psi\rangle + \beta\langle\phi|\chi\rangle$.
3. **Positive definite:** $\langle\psi|\psi\rangle \geq 0$, with equality only for the zero vector.

From (1) and (2), the inner product is *anti-linear* in the first slot — scalars come out conjugated: $\langle\alpha\phi|\psi\rangle = \alpha^{*}\langle\phi|\psi\rangle$. This is the physicist convention, and it is the one used throughout.

The *norm* of a state is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$. A *Hilbert space* is a complex vector space with an inner product that is also *complete* — no sequences escape it. In finite dimensions (like $\mathbb{C}^n$) completeness comes for free. For wave functions on the line the relevant space is $L^2(\mathbb{R})$, the square-integrable functions, and there completeness is a genuine theorem rather than a freebie.

Concretely in $\mathbb{C}^n$: if $|\psi\rangle = (\alpha_1, \ldots, \alpha_n)^T$ and $|\phi\rangle = (\beta_1, \ldots, \beta_n)^T$, then

$$\langle\phi|\psi\rangle = \sum_{i=1}^n \beta_i^{*} \alpha_i.$$

Conjugate the first slot's entries, multiply, sum. Concretely on $L^2(\mathbb{R})$: if $\psi$ and $\phi$ are wave functions,

$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty \phi^{*}(x)\,\psi(x)\,dx.$$

Same idea, an integral in place of the sum.

---

## Dirac notation

P. A. M. Dirac introduced the bra-ket notation in 1939 [Dirac, *Math. Proc. Cambridge Phil. Soc.* 35, 416–418]. It looks like decoration. It is not. It folds four operations into a notation clean enough that calculations which would sprawl across a page in indexed components fit in three lines.

**Ket.** $|\psi\rangle$ is the state vector. In $\mathbb{C}^n$, think of it as a column.

**Bra.** $\langle\psi|$ is the *dual vector* — the linear functional that, fed any ket $|\phi\rangle$, returns the number $\langle\psi|\phi\rangle$. In $\mathbb{C}^n$, if $|\psi\rangle = (\alpha_1, \alpha_2)^T$, then $\langle\psi| = (\alpha_1^{*}, \alpha_2^{*})$ as a row. You conjugate the entries *and* transpose — together, not as separate steps. The single operation that does both is Hermitian conjugation, written $\dagger$, so $\langle\psi| = |\psi\rangle^\dagger$.

**Inner product.** $\langle\phi|\psi\rangle$ is a complex number: row times column, or the integral of $\phi^{*}\psi$, depending on the space.

**Outer product.** $|\psi\rangle\langle\phi|$ is an *operator*: it sends a ket $|\chi\rangle$ to $|\psi\rangle\,(\langle\phi|\chi\rangle)$, a complex number times $|\psi\rangle$.

| name | symbol | what it is | concrete form in ℂ² |
| --- | --- | --- | --- |
| ket | $|\psi\rangle$ | state vector | $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$ |
| bra | $\langle\psi|$ | dual vector | $\begin{pmatrix}\alpha^* & \beta^*\end{pmatrix}$ |
| inner product | $\langle\phi|\psi\rangle$ | complex number | $\phi_1^*\alpha+\phi_2^*\beta$ |
| outer product | $|\psi\rangle\langle\phi|$ | operator | $\begin{pmatrix}\alpha\phi_1^* & \alpha\phi_2^*\\ \beta\phi_1^* & \beta\phi_2^*\end{pmatrix}$ |

Two identities anchor everything that follows. The first is the *completeness relation*. Take any orthonormal basis $\{|n\rangle\}$ — mutually orthogonal unit vectors that span the space, so $\langle m|n\rangle = \delta_{mn}$ and every state expands in them. Then:

$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Why? Take any $|\psi\rangle$ and expand it as $|\psi\rangle = \sum_n c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$. Then $\sum_n |n\rangle\langle n|\psi\rangle = \sum_n c_n|n\rangle = |\psi\rangle$. The operator $\sum_n|n\rangle\langle n|$ does nothing — it acts as the identity. "Inserting the identity" — slipping $\hat{I} = \sum_n|n\rangle\langle n|$ between two other operators — is the single most common move in all of quantum mechanics.

The second identity: the wave function $\psi(x)$ is just the *position-basis component* of the abstract state $|\psi\rangle$. There exist generalized position eigenstates $|x\rangle$ (not normalizable — they live in an extended sense outside $L^2(\mathbb{R})$, but they are useful anyway) with $\langle x|x'\rangle = \delta(x - x')$, and

$$\int dx\,|x\rangle\langle x| = \hat{I}, \qquad \langle x|\psi\rangle = \psi(x).$$

So $|\psi\rangle = \int dx\,\psi(x)|x\rangle$ — the wave function is the set of expansion coefficients of $|\psi\rangle$ in the position basis. Abstract Dirac notation and concrete wave-function notation are the same object in two costumes. Insert $\int dx|x\rangle\langle x|$ to pass from one to the other.

A word on the error nearly everyone makes at least once: computing a matrix element $\langle\phi|\hat{A}|\psi\rangle$ by writing $\phi$'s components as a row *without conjugating them*. The result is wrong — complex when it should be real, usually. Always conjugate when you turn a ket into a bra. If you ever get a complex expectation value for something you believe is an observable, look for the missing conjugation first.

---

## Operators and eigenvalues

A *linear operator* $\hat{A}$ on $V$ maps $V \to V$ and respects addition and scalar multiplication: $\hat{A}(\alpha|\psi\rangle + \beta|\phi\rangle) = \alpha\hat{A}|\psi\rangle + \beta\hat{A}|\phi\rangle$. In $\mathbb{C}^n$, every linear operator is an $n \times n$ matrix.

The *eigenvalue equation* is

$$\hat{A}|a\rangle = a|a\rangle.$$

A vector $|a\rangle$ that the operator leaves pointing the same way, merely rescaled by a complex number $a$. The eigenvalues are the roots of the characteristic polynomial $\det(\hat{A} - a\hat{I}) = 0$.

Here is where Hermitian operators step forward as the central object. An operator is *Hermitian* if $\hat{A}^\dagger = \hat{A}$, where $\hat{A}^\dagger$ is defined by the requirement $\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle$ for all $|\phi\rangle$, $|\psi\rangle$. In matrix form $\hat{A}^\dagger$ is the conjugate transpose, $(A^\dagger)_{ij} = A_{ji}^{*}$, so Hermitian means $A_{ij} = A_{ji}^{*}$.

The *spectral theorem* for Hermitian operators says three things:

1. All eigenvalues are real.
2. Eigenvectors for different eigenvalues are orthogonal.
3. The eigenvectors form an orthonormal basis.

The proof of (1) is one line. If $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A} = \hat{A}^\dagger$, take the inner product of both sides with $|a\rangle$:

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle.$$

But equally $\langle a|\hat{A}|a\rangle = \langle \hat{A}a|a\rangle = \langle a|a\rangle\, a^{*}$. So $a\langle a|a\rangle = a^{*}\langle a|a\rangle$, and since $\langle a|a\rangle > 0$, we get $a = a^{*}$ — $a$ is real.

These three properties are exactly why every observable in quantum mechanics is a Hermitian operator: real eigenvalues because measurement outcomes are real; orthogonal eigenstates because distinct outcomes are distinguishable; a complete eigenbasis because every measurement must yield *some* outcome with probability 1.

---

## The three Pauli matrices

The spin-1/2 system is the cleanest quantum system there is: a two-dimensional Hilbert space $\mathbb{C}^2$, three Hermitian observables, every essential feature on display in $2 \times 2$ arithmetic.

The three Pauli matrices are the spin observables along $x$, $y$, and $z$:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

All three are Hermitian — check $(A^\dagger)_{ij} = A_{ji}^{*}$ for each. All three have eigenvalues $\pm 1$. Their eigenvectors differ, and that difference is the whole substance of quantum measurement.

$\sigma_z$ is already diagonal. Eigenvectors:

$$|\!\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

Spin-up and spin-down along $z$.

For $\sigma_x$: characteristic polynomial $\lambda^2 - 1 = 0$, eigenvalues $\pm 1$. For $\lambda = +1$, the equation $(\sigma_x - I)|v\rangle = 0$ forces equal components. Normalized:

$$|+_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + |\!\downarrow\rangle), \qquad |-_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - |\!\downarrow\rangle).$$

For $\sigma_y$: same eigenvalues. For $\lambda = +1$, $(\sigma_y - I)|v\rangle = 0$ gives $-v_1 - iv_2 = 0$, so $v_2 = iv_1$. Normalized:

$$|+_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + i|\!\downarrow\rangle), \qquad |-_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - i|\!\downarrow\rangle).$$

That $i$ in the component of $|+_y\rangle$ is the entire point. No real-coefficient basis diagonalizes $\sigma_y$. Try to build a real $2\times 2$ symmetric matrix with eigenvalues $\pm 1$ that is physically equivalent to $\sigma_y$ — you cannot, because the chirality of $\sigma_y$ is encoded in the complex structure itself. $\sigma_y$ is the spot in the introductory course where you can no longer look at the $i$ and tell yourself it's just notation.

Now consider what non-commuting measurements mean. Start with $|\!\uparrow\rangle$ and apply $\sigma_x$:

$$\sigma_x|\!\uparrow\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle.$$

The spin-$z$-up state is not a spin-$x$ eigenstate; $\sigma_x$ carries it to the orthogonal state. To get the measurement probabilities, expand $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis. Inverting the relations above gives $|\!\uparrow\rangle = (1/\sqrt{2})(|+_x\rangle + |-_x\rangle)$, so the probability of measuring $\sigma_x = +1$ in the state $|\!\uparrow\rangle$ is $|\langle +_x|\!\uparrow\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$. Fifty-fifty. A particle known to be spin-up along $z$ is completely undetermined along $x$. That is the Stern–Gerlach experiment, written out as basis-change arithmetic.

![Stern-Gerlach apparatus diagram showing sequential measurements ](../images/02-mathematical-foundations-fig-04.png)
*Figure 2.4 — Stern-Gerlach apparatus diagram showing sequential measurements *

---

## Hermitian operators in infinite dimensions: checking $\hat{p}$

The momentum operator in the position representation is $\hat{p} = -i\hbar\,d/dx$. Let us check that it is Hermitian on the square-integrable functions that vanish at infinity.

We need $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$, that is,

$$\int_{-\infty}^\infty \phi^{*}(x)\left(-i\hbar\frac{d\psi}{dx}\right)dx = \int_{-\infty}^\infty \left(-i\hbar\frac{d\phi}{dx}\right)^{*}\psi(x)\,dx.$$

The right side is $\int (+i\hbar\,d\phi^{*}/dx)\,\psi\,dx$. Integrate the left side by parts:

$$\int \phi^{*}\frac{d\psi}{dx}\,dx = \left[\phi^{*}\psi\right]_{-\infty}^\infty - \int\frac{d\phi^{*}}{dx}\psi\,dx.$$

The boundary term $[\phi^{*}\psi]_{-\infty}^\infty$ vanishes, because square-integrability forces $\phi$ and $\psi$ to zero at infinity — if they didn't go to zero, $\int|\psi|^2\,dx$ would diverge. So

$$\int\phi^{*}\frac{d\psi}{dx}\,dx = -\int\frac{d\phi^{*}}{dx}\psi\,dx.$$

Multiply both sides by $-i\hbar$:

$$-i\hbar\int\phi^{*}\frac{d\psi}{dx}\,dx = +i\hbar\int\frac{d\phi^{*}}{dx}\psi\,dx. \checkmark$$

Two things to take away. First: the $-i$ in $\hat{p} = -i\hbar\,d/dx$ is load-bearing. Without it, $d/dx$ is *anti-Hermitian* ($\hat{A}^\dagger = -\hat{A}$) by the very same argument; the $-i$ rotates anti-Hermitian into Hermitian. Every basic QM operator carries its factors of $i$ for exactly this reason. Second: the proof leaned on the boundary conditions. On a finite interval with states that don't vanish at the endpoints, the boundary term need not vanish, and $\hat{p}$ may fail to be Hermitian on that domain. The domain is part of the definition of the operator. In infinite dimensions, *Hermitian* and *self-adjoint* are not the same thing — a Hermitian operator can have eigenstates yet lack a complete eigenbasis, or fail to admit a unique extension to its full domain. Griffiths' footnotes acknowledge this; Reed and Simon, *Methods of Modern Mathematical Physics* Vol. 2, is the reference when it bites. It will bite again in Unit 4, the first time a half-line problem shows up.

![Integration-by-parts steps for the momentum Hermiticity proof ](../images/02-mathematical-foundations-fig-05.png)
*Figure 2.5 — Integration-by-parts steps for the momentum Hermiticity proof *

---

## What the formalism looks like in one picture

Quantum states are vectors in a complex Hilbert space. Observables are Hermitian operators on that space. The eigenvalues of an observable are the possible measurement outcomes. A state $|\psi\rangle$ expanded in the eigenbasis of $\hat{A}$ as $|\psi\rangle = \sum_n c_n|a_n\rangle$ has probability $|c_n|^2$ of yielding outcome $a_n$. The expectation value is

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \sum_n a_n|c_n|^2.$$

Five tools: complex numbers, vector spaces with inner products, Dirac notation, eigenvalue equations, Hermitian operators. That is the complete mathematical vocabulary of quantum mechanics. Everything in the units ahead — the Schrödinger equation, spin, identical particles, entanglement, scattering — is this same vocabulary turned loose on particular problems.

---

## What would change my mind

The claim that quantum mechanics requires complex amplitudes is settled at the operational level by a century of experiments. Renou et al. (2021) tightened it further, ruling out a broad class of real-amplitude reformulations on Bell-inequality grounds. What would force a revision: a reproducible experiment showing that a real-amplitude theory in the same Hilbert-space dimension reproduces the measured probabilities — specifically, surviving the Bell test Renou designed. None has appeared.

The Hermitian-operator postulate rests on the spectral theorem and the requirement that measurement outcomes be real. If an open quantum system requires non-Hermitian operators — as in $\mathcal{PT}$-symmetric theories (Bender and Boettcher, 1998) — the story becomes more complicated. This is an active research area and is not the framework assumed here. The unit's claims are restricted to closed systems.

---

## Still puzzling

**Why $\mathbb{C}$ and not $\mathbb{H}$?** The Stueckelberg argument rules out real QM in fixed dimension; the Renou result sharpens it experimentally. But the quaternions $\mathbb{H}$ also give a sensible-looking inner-product structure (Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995). Why does nature prefer $\mathbb{C}$? The conventional answer is that no experiment has required $\mathbb{H}$. That is not the same as an argument.

**The rigged Hilbert space.** Position eigenstates $|x\rangle$ are not in $L^2(\mathbb{R})$. They live in a strictly larger space — the "rigged Hilbert space" or Gelfand triple construction. Undergraduate courses elide this. Ballentine *Quantum Mechanics: A Modern Development* Ch. 1 handles it carefully.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/02-mathematical-foundations-assertions.md -->

**Why is the state space projective?** The state $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ make identical physical predictions for every observable. The "real" state space is normalized vectors modulo global phase — projective Hilbert space. The formalism carries a redundancy the physics doesn't need. One answer: the redundancy is the price of linearity, which you need for superposition. Whether there is a deeper structural reason remains open.

---

## LLM exercises

The following exercises are designed to be worked interactively with a language model. Use the model to check your reasoning step by step — not to generate answers, but to test whether you can explain each step clearly enough that the model can follow and push back.

**L1.** Ask the model to give you a random normalized state in $\mathbb{C}^2$ with complex coefficients. Compute its bra by hand. Then compute the norm $\langle\psi|\psi\rangle$ step by step and verify it equals 1. Have the model check each arithmetic step and explain where you are applying the conjugation rule.

**L2.** Give the model any $2 \times 2$ Hermitian matrix you construct. Ask it to compute the eigenvalues and eigenvectors. Then do the same computation yourself from scratch using the characteristic polynomial. Compare the results and ask the model to explain any discrepancy in terms of the steps in the derivation.

**L3.** Dictate a proof to the model that $\hat{p} = -i\hbar\,d/dx$ is Hermitian, in natural language — no formulas allowed in your explanation. Ask the model to translate your words into the integral calculation and identify any step you described incorrectly or imprecisely.

**L4.** Construct the operator $|\!\uparrow\rangle\langle\!\downarrow|$ as a $2 \times 2$ matrix. Ask the model: is this operator Hermitian? What are its eigenvalues? Can you use it as an observable? Walk through each question yourself before asking. Then ask the model whether your conclusions about Hermitian, non-Hermitian, and anti-Hermitian operators were correct.

**L5.** Ask the model to generate a state $|\psi\rangle \in \mathbb{C}^2$ and then walk you through computing $\langle\sigma_z\rangle$, $\langle\sigma_x\rangle$, and $\langle\sigma_y\rangle$ in sequence. After each calculation, check that the result is real. If any result is not real, identify the error before asking the model where it is.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Stueckelberg, E. C. G. "Quantum theory in real Hilbert space." *Helvetica Physica Acta* 33, 727–752 (1960).
2. Renou, M.-O. et al. "Quantum theory based on real numbers can be experimentally falsified." *Nature* 600, 625–629 (2021). https://doi.org/10.1038/s41586-021-04160-4
3. Dirac, P. A. M. "A new notation for quantum mechanics." *Mathematical Proceedings of the Cambridge Philosophical Society* 35, 416–418 (1939). https://doi.org/10.1017/S0305004100021162
4. Reed, M. & Simon, B. *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness*. Academic Press, 1975.
5. Bender, C. M. & Boettcher, S. "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry." *Physical Review Letters* 80, 5243 (1998). https://doi.org/10.1103/PhysRevLett.80.5243
6. Adler, S. L. *Quaternionic Quantum Mechanics and Quantum Fields*. Oxford University Press, 1995.
