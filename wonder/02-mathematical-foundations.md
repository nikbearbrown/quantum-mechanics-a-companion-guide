# Chapter 2 — Mathematical Foundations


## TL;DR

- This is the language quantum mechanics is written in — and the reason no simpler language will do the job.
- We move through the arithmetic of complex numbers, vector spaces and inner products, Dirac notation, operators and eigenvalues, and the ideas that hang off them.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The language quantum mechanics is written in, and why no simpler language works.*

---

There is one experiment — just one — that forces the entire mathematical machinery on you. And it is not that physicists sat around wanting to make life complicated. It is that the experiment *insists*. You either follow where it leads, or you give up doing physics. There is no third door.

Send electrons, one at a time, through two slits. Each electron lands somewhere on the screen behind. After ten thousand of them, a pattern shows up: bright bands where many landed, dark bands where almost none did. Those bands are interference fringes — the very same pattern you get watching water waves slip through two gaps in a harbor wall.

But these are electrons. *Single* electrons. There is no second electron around for each one to interfere *with*. So whatever is doing the interfering, the electron is doing it with itself.

Now here is where the math gets forced on you, and I want you to feel the squeeze. To make a dark band, you need the contributions from the two slits to *cancel*. Not add up to something small — *cancel*, to nothing. Call the two contributions $\psi_1$ and $\psi_2$. Add them as $\psi_1 + \psi_2$, then compute intensity as $|\psi_1 + \psi_2|^2$. You can get cancellation when $\psi_1 = -\psi_2$. Fine. But you don't need cancellation at one lonely angle — you need bright bands and dark bands *alternating* clear across the screen. The contributions have to swing smoothly in sign and size as the angle shifts. They need a *phase* that turns continuously.

And what kind of object has a smoothly turning phase? Something that looks like $e^{i\varphi}$. And $e^{i\varphi}$ demands $i = \sqrt{-1}$. Which demands complex numbers.

This is not a matter of taste or convenience. The experiment hands you no alternative. The dark bands are real, they alternate, and the only thing that makes them alternate is a turning phase. So in walk the complex numbers, whether you invited them or not.

![Double-slit experiment diagram with single-electron sequential buildup ](../images/02-mathematical-foundations-fig-01.png)
*Figure 2.1 — Double-slit experiment diagram with single-electron sequential buildup *

---

## The arithmetic of complex numbers

A complex number is $z = a + bi$ where $a$ and $b$ are ordinary real numbers and $i^2 = -1$. The real part is $a$, the imaginary part is $b$. The *complex conjugate* of $z$ is $z^{*} = a - bi$ — you flip the sign on the imaginary part. The *modulus* is

$$|z| = \sqrt{z^{*} z} = \sqrt{a^2 + b^2}.$$

That is a non-negative real number. Picture $a$ and $b$ as coordinates in a plane — the "complex plane" — with the real axis running left to right and the imaginary axis running up and down. The modulus is just the distance from the origin. Nothing exotic. A point on a plane and how far it sits from the center.

Euler's formula is the one fact that makes complex numbers genuinely useful in physics, and it is worth pausing on:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

Want to see why it's true? Expand $e^{i\theta}$, $\cos\theta$, and $\sin\theta$ in their Taylor series and watch the real and imaginary parts line up term by term — it falls right out. Here is what it buys you: *every* complex number can be written as $z = r\,e^{i\theta}$, where $r = |z|$ is its distance from the origin and $\theta$ is its angle. Multiply two of them, and you multiply their distances while you *add* their angles. Take the conjugate, and you flip the angle: $(re^{i\theta})^{*} = re^{-i\theta}$. The whole complex plane turns into a kind of clock arithmetic, and that is exactly the machinery a turning phase needs.

The three facts you will use over and over:

![The complex plane showing a point z =](../images/02-mathematical-foundations-fig-02.png)
*Figure 2.2 — The complex plane showing a point z =*

- $|e^{i\theta}| = 1$ for any real $\theta$. A pure phase factor doesn't change the size of anything.
- $e^{i\theta_1} \cdot e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$. Phases add when complex numbers multiply.
- $(z_1 z_2)^{*} = z_1^{*} z_2^{*}$. Conjugation distributes over multiplication.

Now let's go back to the double slit and make it pay. Label the two slits. The amplitude arriving at a point on the screen from slit 1 is $\psi_1$; from slit 2, $\psi_2$. The rule of quantum mechanics — we'll state it carefully in Unit 3, but let's just use it here — is that you *add the amplitudes* and then *square the modulus* to get intensity. The total amplitude is $\psi = \psi_1 + \psi_2$, and the intensity is $|\psi|^2$.

Take a clean, simple case: one slit is a distance $r$ from the screen point, the other a distance $r + d\sin\theta$ away. Give them equal magnitudes $1/\sqrt{2}$ and phases set by the path lengths:

$$\psi_1 = \frac{1}{\sqrt{2}} e^{ikr}, \qquad \psi_2 = \frac{1}{\sqrt{2}} e^{ik(r + d\sin\theta)},$$

where $k = 2\pi/\lambda$ is the wavenumber. Now expand $|\psi_1 + \psi_2|^2$:

$$|\psi|^2 = \frac{1}{2}\left[e^{-ikr} + e^{-ik(r+d\sin\theta)}\right]\left[e^{ikr} + e^{ik(r+d\sin\theta)}\right]$$

$$= \frac{1}{2}\left[1 + e^{ikd\sin\theta} + e^{-ikd\sin\theta} + 1\right] = 1 + \cos(kd\sin\theta).$$

Using $1 + \cos x = 2\cos^2(x/2)$:

$$|\psi|^2 = 2\cos^2\!\left(\frac{kd\sin\theta}{2}\right).$$

Maxima where $d\sin\theta = n\lambda$; zeros where $d\sin\theta = (n + 1/2)\lambda$. Bright and dark bands, exactly as observed. Look at how little it took — four lines, and the complex exponentials did all the heavy lifting. Now try the same thing with plain real numbers: the cross term comes out as $2\psi_1\psi_2$, a fixed sign, no oscillation at all. No dark bands. No double-slit experiment. The complex numbers were not decoration; they were the gears.

![Plot of |ψ|² = 2cos²(kd sinθ / 2)](../images/02-mathematical-foundations-fig-03.png)
*Figure 2.3 — Plot of |ψ|² = 2cos²(kd sinθ / 2)*

Now you might wonder — is there really no way out? Stueckelberg showed in 1960 that you *can* rebuild quantum mechanics with real numbers, but only if you double the dimension of every space, sneaking in one extra real dimension to stand in for each complex one. What you cannot do is rebuild it with real numbers *in the same dimension*. And then Renou and collaborators went further, in 2021, and ran an actual experiment that tested a whole class of real-amplitude reformulations using Bell inequalities — and ruled them out [Renou et al., *Nature* 600, 625–629 (2021), *verify pagination*]. So the complex numbers are not a convention we settled on for convenience. They are *measured*. The universe checked the box for us.

---

## Vector spaces and inner products

A *vector space* over $\mathbb{C}$ is a set of objects — we'll call them states and write them $|\psi\rangle$ — with two operations: you can add any two of them ($|\psi\rangle + |\phi\rangle$), and you can multiply any one by a complex number ($\alpha|\psi\rangle$). These operations obey the usual sensible rules: addition commutes and associates, scalar multiplication distributes. The simplest example to keep in your head is $\mathbb{C}^n$, just columns of $n$ complex numbers.

An *inner product* is a way of measuring the "angle" between two states — a way of asking how much one points along another. It is a map $\langle\cdot|\cdot\rangle: V \times V \to \mathbb{C}$ obeying three conditions:

1. **Conjugate symmetry:** $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^{*}$.
2. **Linear in the second slot:** $\langle\phi|\alpha\psi + \beta\chi\rangle = \alpha\langle\phi|\psi\rangle + \beta\langle\phi|\chi\rangle$.
3. **Positive definite:** $\langle\psi|\psi\rangle \geq 0$, with equality only for the zero vector.

Here's a consequence worth noticing: from (1) and (2) together, the inner product turns out to be *anti-linear* in the first slot — scalars come out wearing a conjugate: $\langle\alpha\phi|\psi\rangle = \alpha^{*}\langle\phi|\psi\rangle$. That's the physicist's convention, and it's the one we follow throughout.

The *norm* of a state is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$ — the length of the state vector. A *Hilbert space* is a complex vector space with an inner product that is also *complete*, which is a fancy way of saying no sequences quietly leak out the edges of the space. In finite dimensions (like $\mathbb{C}^n$), completeness comes for free. For wave functions on the real line, the relevant Hilbert space is $L^2(\mathbb{R})$, the space of square-integrable functions, and there completeness is a genuine, hard-won theorem.

Concretely in $\mathbb{C}^n$: if $|\psi\rangle = (\alpha_1, \ldots, \alpha_n)^T$ and $|\phi\rangle = (\beta_1, \ldots, \beta_n)^T$, then

$$\langle\phi|\psi\rangle = \sum_{i=1}^n \beta_i^{*} \alpha_i.$$

Conjugate the first slot's entries; multiply; sum. And concretely on $L^2(\mathbb{R})$: if $\psi$ and $\phi$ are wave functions,

$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty \phi^{*}(x)\,\psi(x)\,dx.$$

Same idea, integral instead of sum. The sum just becomes a sum over a continuum.

---

## Dirac notation

P. A. M. Dirac introduced the bra-ket notation in 1939 [Dirac, *Math. Proc. Cambridge Phil. Soc.* 35, 416–418]. At first glance it looks like decoration — cute brackets, why bother. It is not decoration. It quietly packs four separate operations into a notation so clean that calculations which would sprawl across a page in indexed components collapse into three tidy lines. That's not a small thing. A good notation does some of your thinking for you.

**Ket.** $|\psi\rangle$ is the state vector. In $\mathbb{C}^n$, think of it as a column.

**Bra.** $\langle\psi|$ is the *dual vector* — the linear functional that, handed any ket $|\phi\rangle$, spits out the number $\langle\psi|\phi\rangle$. In $\mathbb{C}^n$, if $|\psi\rangle = (\alpha_1, \alpha_2)^T$, then $\langle\psi| = (\alpha_1^{*}, \alpha_2^{*})$ as a row. Notice that you do *both* things at once: conjugate the entries *and* transpose them. These are not two separate steps you do in sequence — they happen together, as a single move. The operation that does both is Hermitian conjugation, written $\dagger$, so $\langle\psi| = |\psi\rangle^\dagger$.

**Inner product.** $\langle\phi|\psi\rangle$ is a complex number: row times column, or the integral of $\phi^{*}\psi$, depending on which space you're in.

**Outer product.** $|\psi\rangle\langle\phi|$ is an *operator*: hand it a ket $|\chi\rangle$ and it returns the ket $|\psi\rangle\,(\langle\phi|\chi\rangle)$, which is a complex number times $|\psi\rangle$.

| name | symbol | what it is | concrete form in ℂ² |
| --- | --- | --- | --- |
| ket | $|\psi\rangle$ | state vector | $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$ |
| bra | $\langle\psi|$ | dual vector | $\begin{pmatrix}\alpha^* & \beta^*\end{pmatrix}$ |
| inner product | $\langle\phi|\psi\rangle$ | complex number | $\phi_1^*\alpha+\phi_2^*\beta$ |
| outer product | $|\psi\rangle\langle\phi|$ | operator | $\begin{pmatrix}\alpha\phi_1^* & \alpha\phi_2^*\\ \beta\phi_1^* & \beta\phi_2^*\end{pmatrix}$ |

Two identities anchor everything that follows, and they are worth knowing in your bones. The first is the *completeness relation*. Take any orthonormal basis $\{|n\rangle\}$ of the space — a set of mutually perpendicular unit vectors that spans the whole space, meaning $\langle m|n\rangle = \delta_{mn}$ and every state can be expanded in them. Then:

$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Why? Take any $|\psi\rangle$. Expand it as $|\psi\rangle = \sum_n c_n|n\rangle$ where $c_n = \langle n|\psi\rangle$. Then $\sum_n |n\rangle\langle n|\psi\rangle = \sum_n c_n|n\rangle = |\psi\rangle$. So the operator $\sum_n|n\rangle\langle n|$ does nothing — it acts as the identity. And here is the practical magic: "inserting the identity" — slipping $\hat{I} = \sum_n|n\rangle\langle n|$ in between two other operators — is the single most common calculational trick in all of quantum mechanics. You will do it a thousand times. It is the crowbar that pries open almost every calculation.

The second identity: the wave function $\psi(x)$ is nothing more exotic than the *position-basis component* of the abstract state $|\psi\rangle$. There exist generalized position eigenstates $|x\rangle$ (they're not normalizable; they live in an extended sense just outside $L^2(\mathbb{R})$, but they're tremendously useful) with $\langle x|x'\rangle = \delta(x - x')$, and

$$\int dx\,|x\rangle\langle x| = \hat{I}, \qquad \langle x|\psi\rangle = \psi(x).$$

So $|\psi\rangle = \int dx\,\psi(x)|x\rangle$ — the wave function is just the expansion coefficients of $|\psi\rangle$ in the position basis. Let that sink in: the abstract Dirac notation and the concrete wave-function notation are the *same object* written two different ways. To pass from one to the other, you insert $\int dx|x\rangle\langle x|$. Same crowbar.

And now a warning, because this is the single most common error students make. They compute a matrix element $\langle\phi|\hat{A}|\psi\rangle$ by writing $\phi$'s components as a row *without conjugating them*. The result is wrong — typically complex when it ought to be real. Always conjugate when you turn a ket into a bra. So here's a free debugging rule: if you get a complex expectation value for something you believe is a genuine observable, look for the missing conjugation first. Nine times out of ten, that's it.

---

## Operators and eigenvalues

A *linear operator* $\hat{A}$ on $V$ maps $V \to V$ and respects addition and scalar multiplication: $\hat{A}(\alpha|\psi\rangle + \beta|\phi\rangle) = \alpha\hat{A}|\psi\rangle + \beta\hat{A}|\phi\rangle$. In $\mathbb{C}^n$, every linear operator is just an $n \times n$ matrix.

The *eigenvalue equation* is

$$\hat{A}|a\rangle = a|a\rangle.$$

Picture it: a vector $|a\rangle$ that the operator leaves pointing in exactly the same direction, only stretched (or shrunk, or flipped) by a complex number $a$. Most vectors get knocked sideways when an operator hits them. The eigenvectors are the special few that don't. The eigenvalues come from the characteristic polynomial $\det(\hat{A} - a\hat{I}) = 0$.

Now here is where Hermitian operators step into the center of the stage and refuse to leave. An operator is *Hermitian* if $\hat{A}^\dagger = \hat{A}$, where $\hat{A}^\dagger$ is defined by the requirement that $\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle$ for all $|\phi\rangle$, $|\psi\rangle$. In matrix form, $\hat{A}^\dagger$ is the conjugate transpose: $(A^\dagger)_{ij} = A_{ji}^{*}$. So Hermitian means $A_{ij} = A_{ji}^{*}$.

The *spectral theorem* for Hermitian operators says three things, and each one earns its keep:

1. All eigenvalues are real.
2. Eigenvectors for different eigenvalues are orthogonal.
3. The eigenvectors form an orthonormal basis.

The proof of (1) is a single line, and I'll show it to you because it is the kind of thing you should be able to reconstruct in your sleep. If $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A} = \hat{A}^\dagger$, take the inner product of both sides with $|a\rangle$:

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle.$$

But also $\langle a|\hat{A}|a\rangle = \langle \hat{A}a|a\rangle = \langle a|a\rangle\, a^{*}$. So $a\langle a|a\rangle = a^{*}\langle a|a\rangle$. Since $\langle a|a\rangle > 0$, we get $a = a^{*}$, so $a$ is real. That's it. The Hermitian condition, applied once, forces the eigenvalue to equal its own conjugate.

And those three properties are *exactly why* every observable in quantum mechanics is a Hermitian operator. Real eigenvalues, because measurement outcomes are real numbers — you never read "$3 + 2i$ volts" off a meter. Orthogonal eigenstates, because distinct outcomes have to be distinguishable results. A complete eigenbasis, because the measurement must produce *some* outcome with probability 1. The mathematics and the physics fit together like a key and a lock, and the spectral theorem is the cut of the key.

---

## The three Pauli matrices

The spin-1/2 system is the cleanest quantum system there is — the lab rat of the whole subject. Two-dimensional Hilbert space $\mathbb{C}^2$, three Hermitian observables, and every essential feature laid bare in plain $2 \times 2$ matrix arithmetic. If you want to understand quantum mechanics without drowning in calculus, this is where you go.

The three Pauli matrices are the spin observables along the $x$, $y$, and $z$ axes:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

All three are Hermitian — check $(A^\dagger)_{ij} = A_{ji}^{*}$ for each, it takes ten seconds. All three have eigenvalues $\pm 1$. But their eigenvectors are *different*, and that difference — the fact that being sharp along one axis means being undecided along another — is the whole substance of quantum measurement.

$\sigma_z$ is already diagonal, so it hands you its eigenvectors for free:

$$|\!\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

These are spin-up and spin-down along the $z$-axis.

For $\sigma_x$: characteristic polynomial $\lambda^2 - 1 = 0$, eigenvalues $\pm 1$. For $\lambda = +1$, the eigenvector equation $(\sigma_x - I)|v\rangle = 0$ gives equal components. Normalized:

$$|+_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + |\!\downarrow\rangle), \qquad |-_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - |\!\downarrow\rangle).$$

For $\sigma_y$: same eigenvalues. For $\lambda = +1$, the equation $(\sigma_y - I)|v\rangle = 0$ gives $-v_1 - iv_2 = 0$, so $v_2 = iv_1$. Normalized:

$$|+_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + i|\!\downarrow\rangle), \qquad |-_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - i|\!\downarrow\rangle).$$

That $i$ sitting in the second component of $|+_y\rangle$ — that is the whole point, and I want you to stare at it. There is *no* real-coefficient basis that diagonalizes $\sigma_y$. Go ahead and try: write down a real $2\times 2$ symmetric matrix with eigenvalues $\pm 1$ that is physically equivalent to $\sigma_y$. You cannot do it, because the *handedness* of $\sigma_y$ — its chirality — is locked up inside the complex structure itself. This is the spot in the introductory course where you finally cannot look at the $i$ and reassure yourself that it's "just notation." The $i$ is doing physical work.

Now let's see what it means for measurements to refuse to commute. Start with the state $|\!\uparrow\rangle$. Apply $\sigma_x$:

$$\sigma_x|\!\uparrow\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle.$$

The spin-$z$-up state is not a spin-$x$ eigenstate at all; hit it with $\sigma_x$ and it flips clean over to the orthogonal state. To find the actual measurement probabilities, expand $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis. Inverting the relations above: $|\!\uparrow\rangle = (1/\sqrt{2})(|+_x\rangle + |-_x\rangle)$. The probability of measuring $\sigma_x = +1$ in the state $|\!\uparrow\rangle$ is $|\langle +_x|\!\uparrow\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$. Fifty-fifty. A particle you know for certain is spin-up along $z$ is completely undetermined along $x$ — a coin flip, every time. That, written out in plain basis-change arithmetic, *is* the Stern–Gerlach experiment.

![Stern-Gerlach apparatus diagram showing sequential measurements ](../images/02-mathematical-foundations-fig-04.png)
*Figure 2.4 — Stern-Gerlach apparatus diagram showing sequential measurements *

---

## Hermitian operators in infinite dimensions: checking $\hat{p}$

The momentum operator in the position representation is $\hat{p} = -i\hbar\,d/dx$. Let's roll up our sleeves and actually check that it's Hermitian on the space of square-integrable functions that vanish at infinity. No hand-waving — let's do it.

We need to confirm $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$, that is,

$$\int_{-\infty}^\infty \phi^{*}(x)\left(-i\hbar\frac{d\psi}{dx}\right)dx = \int_{-\infty}^\infty \left(-i\hbar\frac{d\phi}{dx}\right)^{*}\psi(x)\,dx.$$

The right side is $\int (+i\hbar\,d\phi^{*}/dx)\,\psi\,dx$. Integrate the left side by parts:

$$\int \phi^{*}\frac{d\psi}{dx}\,dx = \left[\phi^{*}\psi\right]_{-\infty}^\infty - \int\frac{d\phi^{*}}{dx}\psi\,dx.$$

Now watch the boundary term $[\phi^{*}\psi]_{-\infty}^\infty$ — it dies, and it dies for a physical reason: both $\phi$ and $\psi$ are square-integrable, so they must go to zero at infinity, otherwise $\int|\psi|^2\,dx$ would blow up. So

$$\int\phi^{*}\frac{d\psi}{dx}\,dx = -\int\frac{d\phi^{*}}{dx}\psi\,dx.$$

Multiply both sides by $-i\hbar$:

$$-i\hbar\int\phi^{*}\frac{d\psi}{dx}\,dx = +i\hbar\int\frac{d\phi^{*}}{dx}\psi\,dx. \checkmark$$

Two things to notice, and both are quietly profound. First: that $-i$ in $\hat{p} = -i\hbar\,d/dx$ is *load-bearing*. Strip it out and $d/dx$ by itself is *anti-Hermitian* ($\hat{A}^\dagger = -\hat{A}$), by the very same argument we just ran — the integration by parts flips the sign and nothing turns it back. The $-i$ is what rotates anti-Hermitian into Hermitian. Every basic QM operator carries these factors of $i$ for exactly this reason; they are not noise. Second: the proof leaned entirely on the boundary conditions. On a finite interval, with states that don't vanish at the endpoints, the boundary term does *not* automatically die, and $\hat{p}$ may fail to be Hermitian on that domain. The domain is part of the definition of the operator — you cannot specify the operator without specifying where it lives. In infinite dimensions, *Hermitian* and *self-adjoint* are not quite the same thing — a Hermitian operator can have eigenstates yet lack a complete eigenbasis, or fail to admit a unique unambiguous extension to its full domain. Griffiths' footnotes nod at this; Reed and Simon, *Methods of Modern Mathematical Physics* Vol. 2, is the place to go when it bites. And it will bite again in Unit 4, when half-line problems first appear.

![Integration-by-parts steps for the momentum Hermiticity proof ](../images/02-mathematical-foundations-fig-05.png)
*Figure 2.5 — Integration-by-parts steps for the momentum Hermiticity proof *

---

## What the formalism looks like in one picture

Let me step back and give you the whole skeleton in one breath. Quantum states are vectors in a complex Hilbert space. Observables are Hermitian operators on that space. The eigenvalues of an observable are the possible measurement outcomes. A state $|\psi\rangle$ expanded in the eigenbasis of $\hat{A}$ as $|\psi\rangle = \sum_n c_n|a_n\rangle$ has probability $|c_n|^2$ of yielding outcome $a_n$. And the expectation value is

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \sum_n a_n|c_n|^2.$$

Five tools. That's all it is: complex numbers, vector spaces with inner products, Dirac notation, eigenvalue equations, Hermitian operators. That is the *complete* mathematical vocabulary of quantum mechanics. Everything in the units ahead — the Schrödinger equation, spin, identical particles, entanglement, scattering — is this same handful of tools, pointed at one particular problem after another. Learn these five things well and you have learned the language. The rest is conversation.

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
