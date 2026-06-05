# Chapter 2 — Mathematical Foundations


## TL;DR

- The language quantum mechanics is written in, and why no simpler language works.
- The chapter moves through The arithmetic of complex numbers, Vector spaces and inner products, Dirac notation, Operators and eigenvalues, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The language quantum mechanics is written in, and why no simpler language works.*

---

One experiment, all by itself, drags the entire mathematical apparatus into the room. The mathematics is not an aesthetic preference imposed by physicists who liked formalism. The experiment *demands* it, and you either go where it points or you abandon the attempt to describe what you see.

Send electrons through two slits, one electron at a time. Each lands somewhere on the screen behind. Let ten thousand of them accumulate and a pattern surfaces: bright stripes where many arrived, dark stripes where almost none did. The stripes are interference fringes — the very pattern water waves throw up after passing through a pair of gaps.

Yet these are electrons. Single electrons. For any one of them there is no second electron present to interfere *with*. Whatever is doing the interfering is each electron interfering with itself.

Here is the precise point at which the mathematics becomes unavoidable. To carve out those dark stripes, the two contributions from the two slits have to *cancel*. Not shrink to something small — cancel outright. Call the two contributions $\psi_1$ and $\psi_2$. Add them as $\psi_1 + \psi_2$, take the intensity to be $|\psi_1 + \psi_2|^2$, and cancellation becomes possible the moment $\psi_1 = -\psi_2$. So far, so good. But a single point of cancellation is not enough; you need the bright and dark stripes to march in alternation across the whole screen. The two contributions must slide smoothly in sign and in size as the angle shifts. They must carry a *phase* that varies continuously.

Objects with a continuously varying phase are built from $e^{i\varphi}$. And $e^{i\varphi}$ cannot exist without $i = \sqrt{-1}$, which cannot exist without complex numbers.

This is not a matter of convenience. The experiment leaves you no alternative.

![Double-slit experiment diagram with single-electron sequential buildup ](../images/02-mathematical-foundations-fig-01.png)
*Figure 2.1 — Double-slit experiment diagram with single-electron sequential buildup *

---

## The arithmetic of complex numbers

A complex number is $z = a + bi$ where $a$ and $b$ are ordinary real numbers and $i^2 = -1$. The real part is $a$, the imaginary part is $b$. The *complex conjugate* of $z$ is $z^{*} = a - bi$ — you flip the sign on the imaginary part. The *modulus* is

$$|z| = \sqrt{z^{*} z} = \sqrt{a^2 + b^2}.$$

That quantity is a non-negative real number. Picture $a$ and $b$ as coordinates in a plane — the "complex plane" — the real axis running left to right, the imaginary axis running up and down. The modulus is simply the distance from the origin.

Euler's formula is the single fact that turns complex numbers into a tool a physicist reaches for daily:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

If you want to convince yourself, expand $e^{i\theta}$, $\cos\theta$, and $\sin\theta$ in their Taylor series and watch the real and imaginary parts line up term by term. What it buys you is this: every complex number can be cast as $z = r\,e^{i\theta}$, with $r = |z|$ its distance from the origin and $\theta$ its angle. Multiply two complex numbers and their distances multiply while their angles *add*. Conjugate one and its angle flips: $(re^{i\theta})^{*} = re^{-i\theta}$.

Three facts will recur until they become reflexes:

![The complex plane showing a point z =](../images/02-mathematical-foundations-fig-02.png)
*Figure 2.2 — The complex plane showing a point z =*

- $|e^{i\theta}| = 1$ for any real $\theta$. A pure phase factor doesn't change the size of anything.
- $e^{i\theta_1} \cdot e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$. Phases add when complex numbers multiply.
- $(z_1 z_2)^{*} = z_1^{*} z_2^{*}$. Conjugation distributes over multiplication.

Return now to the double slit. Label the two slits. The amplitude reaching the screen from slit 1 is $\psi_1$; from slit 2, $\psi_2$. The governing rule of quantum mechanics — stated precisely in Unit 3, borrowed here in advance — is that you *add the amplitudes* and then *square the modulus* to read off intensity. The total amplitude is $\psi = \psi_1 + \psi_2$, and the intensity is $|\psi|^2$.

Pin down a concrete case: one slit lies a distance $r$ from the chosen point on the screen, the other a distance $r + d\sin\theta$ away. Give them equal magnitudes $1/\sqrt{2}$ and phases set by path length:

$$\psi_1 = \frac{1}{\sqrt{2}} e^{ikr}, \qquad \psi_2 = \frac{1}{\sqrt{2}} e^{ik(r + d\sin\theta)},$$

where $k = 2\pi/\lambda$ is the wavenumber. Expand $|\psi_1 + \psi_2|^2$:

$$|\psi|^2 = \frac{1}{2}\left[e^{-ikr} + e^{-ik(r+d\sin\theta)}\right]\left[e^{ikr} + e^{ik(r+d\sin\theta)}\right]$$

$$= \frac{1}{2}\left[1 + e^{ikd\sin\theta} + e^{-ikd\sin\theta} + 1\right] = 1 + \cos(kd\sin\theta).$$

Using $1 + \cos x = 2\cos^2(x/2)$:

$$|\psi|^2 = 2\cos^2\!\left(\frac{kd\sin\theta}{2}\right).$$

Maxima where $d\sin\theta = n\lambda$; zeros where $d\sin\theta = (n + 1/2)\lambda$. Bright and dark bands, exactly as observed. The complex exponentials carried that calculation through in four lines. Attempt it with real numbers instead and the cross term comes out as $2\psi_1\psi_2$, a quantity of fixed sign that never oscillates. No dark bands. No double-slit experiment.

![Plot of |ψ|² = 2cos²(kd sinθ / 2)](../images/02-mathematical-foundations-fig-03.png)
*Figure 2.3 — Plot of |ψ|² = 2cos²(kd sinθ / 2)*

You might wonder whether the complex numbers could be smuggled away. Stueckelberg showed in 1960 that you can indeed recast quantum mechanics in real numbers — provided you double the dimension of every space, trading one extra real dimension for each complex one you discard. What cannot be done is to recast it in real numbers *at the same dimension*. And in 2021 Renou and collaborators built an experiment that put an entire family of real-amplitude reformulations to a direct test using Bell inequalities — and excluded them [Renou et al., *Nature* 600, 625–629 (2021), *verify pagination*]. The complex numbers are not a convention. They are measured.

---

## Vector spaces and inner products

A *vector space* over $\mathbb{C}$ is a collection of objects — here we call them states and write them $|\psi\rangle$ — equipped with two operations: any two may be added ($|\psi\rangle + |\phi\rangle$), and any one may be scaled by a complex number ($\alpha|\psi\rangle$). The familiar rules hold: addition commutes and associates, scalar multiplication distributes. The plainest example is $\mathbb{C}^n$, columns of $n$ complex numbers.

An *inner product* supplies a way to gauge the "angle" between two states. It is a map $\langle\cdot|\cdot\rangle: V \times V \to \mathbb{C}$ obeying three conditions:

1. **Conjugate symmetry:** $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^{*}$.
2. **Linear in the second slot:** $\langle\phi|\alpha\psi + \beta\chi\rangle = \alpha\langle\phi|\psi\rangle + \beta\langle\phi|\chi\rangle$.
3. **Positive definite:** $\langle\psi|\psi\rangle \geq 0$, with equality only for the zero vector.

Conditions (1) and (2) together force the inner product to be *anti-linear* in the first slot — scalars emerge conjugated: $\langle\alpha\phi|\psi\rangle = \alpha^{*}\langle\phi|\psi\rangle$. This is the physicist's convention, and the one used here throughout.

The *norm* of a state is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$. A *Hilbert space* is a complex vector space carrying an inner product and, in addition, *complete* — meaning no sequence of states can converge to something outside the space. In finite dimensions (such as $\mathbb{C}^n$) completeness comes for free. For wave functions on the real line the relevant Hilbert space is $L^2(\mathbb{R})$, the square-integrable functions, and there completeness is a genuine theorem.

Made concrete in $\mathbb{C}^n$: if $|\psi\rangle = (\alpha_1, \ldots, \alpha_n)^T$ and $|\phi\rangle = (\beta_1, \ldots, \beta_n)^T$, then

$$\langle\phi|\psi\rangle = \sum_{i=1}^n \beta_i^{*} \alpha_i.$$

Conjugate the first slot's entries, multiply, sum. Made concrete on $L^2(\mathbb{R})$: if $\psi$ and $\phi$ are wave functions,

$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty \phi^{*}(x)\,\psi(x)\,dx.$$

The same idea, with an integral standing in for the sum.

---

## Dirac notation

P. A. M. Dirac introduced the bra-ket notation in 1939 [Dirac, *Math. Proc. Cambridge Phil. Soc.* 35, 416–418]. It can look like ornament. It is nothing of the kind. It folds four operations into a notation clean enough that calculations costing a full page in indexed components collapse into three lines.

**Ket.** $|\psi\rangle$ is the state vector. In $\mathbb{C}^n$, think of it as a column.

**Bra.** $\langle\psi|$ is the *dual vector* — the linear functional that, handed any ket $|\phi\rangle$, returns the number $\langle\psi|\phi\rangle$. In $\mathbb{C}^n$, if $|\psi\rangle = (\alpha_1, \alpha_2)^T$, then $\langle\psi| = (\alpha_1^{*}, \alpha_2^{*})$ as a row. You *both* conjugate the entries *and* transpose. These are not two separate moves; they occur as one. The operation carrying out both is Hermitian conjugation, written $\dagger$, so $\langle\psi| = |\psi\rangle^\dagger$.

**Inner product.** $\langle\phi|\psi\rangle$ is a complex number: row times column, or integral of $\phi^{*}\psi$, depending on the space.

**Outer product.** $|\psi\rangle\langle\phi|$ is an *operator*: it carries a ket $|\chi\rangle$ to the ket $|\psi\rangle\,(\langle\phi|\chi\rangle)$, a complex number times $|\psi\rangle$.

| name | symbol | what it is | concrete form in ℂ² |
| --- | --- | --- | --- |
| ket | $|\psi\rangle$ | state vector | $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$ |
| bra | $\langle\psi|$ | dual vector | $\begin{pmatrix}\alpha^* & \beta^*\end{pmatrix}$ |
| inner product | $\langle\phi|\psi\rangle$ | complex number | $\phi_1^*\alpha+\phi_2^*\beta$ |
| outer product | $|\psi\rangle\langle\phi|$ | operator | $\begin{pmatrix}\alpha\phi_1^* & \alpha\phi_2^*\\ \beta\phi_1^* & \beta\phi_2^*\end{pmatrix}$ |

Two identities hold up everything that follows. The first is the *completeness relation*. Take any orthonormal basis $\{|n\rangle\}$ of the space — a set of mutually orthogonal unit vectors spanning the whole space, so that $\langle m|n\rangle = \delta_{mn}$ and every state expands in them. Then:

$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Why? Take any $|\psi\rangle$ and expand it as $|\psi\rangle = \sum_n c_n|n\rangle$ with $c_n = \langle n|\psi\rangle$. Then $\sum_n |n\rangle\langle n|\psi\rangle = \sum_n c_n|n\rangle = |\psi\rangle$. The operator $\sum_n|n\rangle\langle n|$ behaves as the identity. "Inserting the identity" — slipping $\hat{I} = \sum_n|n\rangle\langle n|$ between two other operators — is the single most frequent calculational move in all of quantum mechanics.

The second identity: the wave function $\psi(x)$ is the *position-basis component* of the abstract state $|\psi\rangle$. There exist generalized position eigenstates $|x\rangle$ (not normalizable; they live, in an extended sense, outside $L^2(\mathbb{R})$, but they earn their keep) with $\langle x|x'\rangle = \delta(x - x')$, and

$$\int dx\,|x\rangle\langle x| = \hat{I}, \qquad \langle x|\psi\rangle = \psi(x).$$

So $|\psi\rangle = \int dx\,\psi(x)|x\rangle$ — the wave function holds the expansion coefficients of $|\psi\rangle$ in the position basis. Abstract Dirac notation and concrete wave-function notation are one object written two ways. Insert $\int dx|x\rangle\langle x|$ to pass between them.

The error students commit most often: computing a matrix element $\langle\phi|\hat{A}|\psi\rangle$ by writing $\phi$'s components as a row *without conjugating them*. The answer comes out wrong — complex where it ought to be real, as a rule. Always conjugate when you turn a ket into a bra. If an expectation value you expected to be real comes out complex, look first for the missing conjugation.

---

## Operators and eigenvalues

A *linear operator* $\hat{A}$ on $V$ maps $V \to V$ and respects addition and scalar multiplication: $\hat{A}(\alpha|\psi\rangle + \beta|\phi\rangle) = \alpha\hat{A}|\psi\rangle + \beta\hat{A}|\phi\rangle$. In $\mathbb{C}^n$, every linear operator is an $n \times n$ matrix.

The *eigenvalue equation* is

$$\hat{A}|a\rangle = a|a\rangle.$$

A vector $|a\rangle$ the operator leaves pointing the same way, merely rescaled by a complex number $a$. The eigenvalues fall out of the characteristic polynomial $\det(\hat{A} - a\hat{I}) = 0$.

It is here that Hermitian operators step forward as the central object. An operator is *Hermitian* if $\hat{A}^\dagger = \hat{A}$, where $\hat{A}^\dagger$ is fixed by the requirement that $\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle$ for all $|\phi\rangle$, $|\psi\rangle$. In matrix form, $\hat{A}^\dagger$ is the conjugate transpose: $(A^\dagger)_{ij} = A_{ji}^{*}$. Hermitian means $A_{ij} = A_{ji}^{*}$.

The *spectral theorem* for Hermitian operators makes three promises:

1. All eigenvalues are real.
2. Eigenvectors for different eigenvalues are orthogonal.
3. The eigenvectors form an orthonormal basis.

The proof of (1) is a single line: if $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A} = \hat{A}^\dagger$, take the inner product of both sides with $|a\rangle$:

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle.$$

But equally $\langle a|\hat{A}|a\rangle = \langle \hat{A}a|a\rangle = \langle a|a\rangle\, a^{*}$. So $a\langle a|a\rangle = a^{*}\langle a|a\rangle$. Since $\langle a|a\rangle > 0$, we conclude $a = a^{*}$, so $a$ is real.

These three properties are precisely why every observable in quantum mechanics is a Hermitian operator: real eigenvalues, because the numbers a measurement returns are real; orthogonal eigenstates, because distinct outcomes have to be distinguishable; a complete eigenbasis, because the measurement is obliged to yield *some* outcome with probability 1.

---

## The three Pauli matrices

The spin-1/2 system is the simplest quantum system that exists: a two-dimensional Hilbert space $\mathbb{C}^2$, three Hermitian observables, every essential feature on display in $2 \times 2$ matrix arithmetic.

The three Pauli matrices are the spin observables along the $x$, $y$, and $z$ axes:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

All three are Hermitian — verify $(A^\dagger)_{ij} = A_{ji}^{*}$ for each. All three carry eigenvalues $\pm 1$. Their eigenvectors differ, and that difference is the very substance of quantum measurement.

$\sigma_z$ is already diagonal. Eigenvectors:

$$|\!\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

These are spin-up and spin-down along the $z$-axis.

For $\sigma_x$: characteristic polynomial $\lambda^2 - 1 = 0$, eigenvalues $\pm 1$. For $\lambda = +1$, the eigenvector equation $(\sigma_x - I)|v\rangle = 0$ gives equal components. Normalized:

$$|+_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + |\!\downarrow\rangle), \qquad |-_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - |\!\downarrow\rangle).$$

For $\sigma_y$: same eigenvalues. For $\lambda = +1$, the equation $(\sigma_y - I)|v\rangle = 0$ gives $-v_1 - iv_2 = 0$, so $v_2 = iv_1$. Normalized:

$$|+_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + i|\!\downarrow\rangle), \qquad |-_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - i|\!\downarrow\rangle).$$

That $i$ sitting in the component of $|+_y\rangle$ is the entire point. No real-coefficient basis diagonalizes $\sigma_y$. Try to build a real, symmetric $2\times 2$ matrix with eigenvalues $\pm 1$ that is physically equivalent to $\sigma_y$ — and you cannot, because the chirality of $\sigma_y$ is locked into the complex structure. $\sigma_y$ is the spot in the introductory course where you can no longer look at the $i$ and reassure yourself that it is mere notation.

Now weigh what it means for measurements to fail to commute. Begin with the state $|\!\uparrow\rangle$ and apply $\sigma_x$:

$$\sigma_x|\!\uparrow\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle.$$

The spin-$z$-up state is not a spin-$x$ eigenstate; acting with $\sigma_x$ flings it to the orthogonal state. To extract the measurement probabilities, expand $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis. Inverting the relations above gives $|\!\uparrow\rangle = (1/\sqrt{2})(|+_x\rangle + |-_x\rangle)$. The probability of measuring $\sigma_x = +1$ in the state $|\!\uparrow\rangle$ is $|\langle +_x|\!\uparrow\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$. Fifty-fifty. A particle known with certainty to be spin-up along $z$ is wholly undetermined along $x$. That is the Stern–Gerlach experiment, rendered as the arithmetic of a change of basis.

![Stern-Gerlach apparatus diagram showing sequential measurements ](../images/02-mathematical-foundations-fig-04.png)
*Figure 2.4 — Stern-Gerlach apparatus diagram showing sequential measurements *

---

## Hermitian operators in infinite dimensions: checking $\hat{p}$

The momentum operator in the position representation is $\hat{p} = -i\hbar\,d/dx$. Let us check that it is Hermitian on the space of square-integrable functions that vanish at infinity.

We must confirm $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$, that is,

$$\int_{-\infty}^\infty \phi^{*}(x)\left(-i\hbar\frac{d\psi}{dx}\right)dx = \int_{-\infty}^\infty \left(-i\hbar\frac{d\phi}{dx}\right)^{*}\psi(x)\,dx.$$

The right side is $\int (+i\hbar\,d\phi^{*}/dx)\,\psi\,dx$. Integrate the left side by parts:

$$\int \phi^{*}\frac{d\psi}{dx}\,dx = \left[\phi^{*}\psi\right]_{-\infty}^\infty - \int\frac{d\phi^{*}}{dx}\psi\,dx.$$

The boundary term $[\phi^{*}\psi]_{-\infty}^\infty$ dies because both $\phi$ and $\psi$ are square-integrable — were they not to vanish at infinity, $\int|\psi|^2\,dx$ would diverge. So

$$\int\phi^{*}\frac{d\psi}{dx}\,dx = -\int\frac{d\phi^{*}}{dx}\psi\,dx.$$

Multiply both sides by $-i\hbar$:

$$-i\hbar\int\phi^{*}\frac{d\psi}{dx}\,dx = +i\hbar\int\frac{d\phi^{*}}{dx}\psi\,dx. \checkmark$$

Two points deserve notice. First: the $-i$ in $\hat{p} = -i\hbar\,d/dx$ does real work. Strip it away and $d/dx$ is *anti-Hermitian* ($\hat{A}^\dagger = -\hat{A}$) by the identical argument; the $-i$ is what rotates anti-Hermitian back into Hermitian. Every elementary QM operator drags along its factors of $i$ for exactly this reason. Second: the proof leaned on the boundary conditions. On a finite interval, with states that fail to vanish at the endpoints, the boundary term need not disappear, and $\hat{p}$ may not be Hermitian on that domain. The domain is part of what defines the operator. In infinite dimensions, *Hermitian* and *self-adjoint* part ways — a Hermitian operator may possess eigenstates yet lack a complete eigenbasis, or fail to admit a single unambiguous extension to its full domain. Griffiths' footnotes acknowledge this; Reed and Simon, *Methods of Modern Mathematical Physics* Vol. 2, is the reference for when it matters. It will matter again in Unit 4, when half-line problems first surface.

![Integration-by-parts steps for the momentum Hermiticity proof ](../images/02-mathematical-foundations-fig-05.png)
*Figure 2.5 — Integration-by-parts steps for the momentum Hermiticity proof *

---

## What the formalism looks like in one picture

Quantum states are vectors in a complex Hilbert space. Observables are Hermitian operators on that space. The eigenvalues of an observable are the outcomes a measurement can return. A state $|\psi\rangle$ expanded in the eigenbasis of $\hat{A}$ as $|\psi\rangle = \sum_n c_n|a_n\rangle$ has probability $|c_n|^2$ of producing outcome $a_n$. The expectation value is

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \sum_n a_n|c_n|^2.$$

Five tools: complex numbers, vector spaces with inner products, Dirac notation, eigenvalue equations, Hermitian operators. That is the complete mathematical vocabulary of quantum mechanics. Everything in the units ahead — the Schrödinger equation, spin, identical particles, entanglement, scattering — is this vocabulary turned loose on particular problems.

---

## What would change my mind

That quantum mechanics requires complex amplitudes is settled, at the operational level, by a century of experiments. Renou et al. (2021) drew the noose tighter, ruling out a broad class of real-amplitude reformulations on Bell-inequality grounds. What would force a revision: a reproducible experiment showing that a real-amplitude theory at the same Hilbert-space dimension reproduces the measured probabilities — surviving, in particular, the Bell test Renou designed. None has appeared.

The Hermitian-operator postulate rests on the spectral theorem together with the demand that measurement outcomes be real. Should an open quantum system require non-Hermitian operators — as in $\mathcal{PT}$-symmetric theories (Bender and Boettcher, 1998) — the story turns more intricate. That is an active research area, and not the framework assumed here. The unit's claims stay confined to closed systems.

---

## Still puzzling

**Why $\mathbb{C}$ and not $\mathbb{H}$?** The Stueckelberg argument bars real QM in fixed dimension; the Renou result sharpens it in the laboratory. Yet the quaternions $\mathbb{H}$ also furnish a sensible-looking inner-product structure (Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995). Why should nature favor $\mathbb{C}$? The standard reply is that no experiment has yet demanded $\mathbb{H}$. That is not the same as an argument.

**The rigged Hilbert space.** Position eigenstates $|x\rangle$ do not live in $L^2(\mathbb{R})$. They inhabit a strictly larger space — the "rigged Hilbert space," or Gelfand triple. Undergraduate courses slide past this. Ballentine, *Quantum Mechanics: A Modern Development* Ch. 1, treats it with care.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/02-mathematical-foundations-assertions.md -->

**Why is the state space projective?** The states $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ deliver identical physical predictions for every observable. The "real" state space is the normalized vectors taken modulo a global phase — projective Hilbert space. The formalism carries a redundancy the physics never asked for. One answer: that redundancy is the toll exacted by linearity, which you need in order to have superposition at all. Whether some deeper structural reason lies beneath remains open.

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
