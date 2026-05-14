# Unit 2 — Mathematical Foundations

> Quantum mechanics is linear algebra over the complex numbers with an inner product and a Hermiticity condition. This unit builds the language. Every later unit speaks it.

---

## 1. What this chapter is doing

This is the unit where the pop-sci companion contributes nothing. TIKTOC marks every entry in this section as ❌ — complex numbers, vector spaces, Dirac notation, operators, Hermitian conjugation. *Quantum Physics for Beginners* (2021) makes no pretense of being a math book. Griffiths Ch. 3 ("Formalism," 3rd ed. 2018) is the canonical undergraduate treatment and is the spine of this unit; Shankar *Principles of Quantum Mechanics* (2nd ed. 1994) Ch. 1 is the alternative I will point you to when you want more rigor. This companion does the unit's full work — every concept, every derivation, every worked example. By the end you should be fluent in three languages: matrix notation in $\mathbb{C}^2$, the abstract Dirac notation, and the integral-and-derivative notation of wave functions on the real line. They are the same language, written three ways.

If Unit 1 told you why quantum mechanics has to exist, Unit 2 builds the apparatus that lets you say anything precise inside it.

## 2. Learning objectives

By the end of this unit, you should be able to:

- **State** Euler's formula, the inner product of two kets, the eigenvalue equation, and the Hermiticity condition. (Bloom L1)
- **Convert** an expression in Dirac notation to a matrix calculation in a chosen basis, and back. (L2)
- **Compute** the eigenvalues and eigenvectors of any $2 \times 2$ Hermitian matrix, including the three Pauli matrices. (L3)
- **Verify** that $\hat{p} = -i\hbar\,d/dx$ is Hermitian on the space of square-integrable functions vanishing at infinity. (L4)
- **Distinguish** Hermitian from symmetric, and explain why the distinction matters for complex matrices. (L5)
- **Construct** the Hermitian conjugate of a product $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger \hat{A}^\dagger$ and explain the order reversal. (L6)

## 3. The motivating problem

The double slit, run with single electrons, lands one particle at a time on a screen. Each particle arrives somewhere; over many particles, a pattern of bright and dark fringes appears. The pattern is identical to the one you would compute by adding two classical waves and squaring. So whatever describes the particle has to (a) be the kind of thing that can be added, (b) carry phase information so that the addition can produce constructive and destructive interference, and (c) be turned into a probability by some operation that throws away an overall sign or rotation.

Real numbers cannot do this. If $\psi_1$ and $\psi_2$ are real, then $|\psi_1 + \psi_2|^2 = \psi_1^2 + \psi_2^2 + 2\psi_1\psi_2$, and the cross term $2\psi_1\psi_2$ is a fixed sign — no oscillation. To get the bright-and-dark fringes, the cross term has to be $2\,\text{Re}(\psi_1^* \psi_2)$, an oscillating function of the path difference. Oscillation requires phase. Phase requires $e^{i\varphi}$. $e^{i\varphi}$ requires complex numbers.

So the first move of quantum mechanics is to insist that the *amplitudes* — the things you add — live in $\mathbb{C}$, and the *probabilities* — the things you observe — come from squaring the modulus. That single move, applied consistently, is the whole formalism.

A second motivating fact. The Franck–Hertz experiment from Unit 1 found that mercury's energy levels are discrete — 4.9 eV, then 9.8 eV, then 14.7 eV. Whatever the formalism is, it has to produce *discrete spectra* for bounded systems. In linear algebra, the natural way to get a discrete spectrum is from the eigenvalues of an operator on a finite-dimensional vector space (or a compactly-supported operator on an infinite-dimensional one). So the formalism has to be operator-based, with energies appearing as eigenvalues.

Complex amplitudes plus operators with eigenvalues. That's the math we have to build.

## 4. The five tools

### 4.1 Complex numbers — the smallest non-trivial extension of arithmetic

A complex number is $z = a + bi$, where $a$ and $b$ are real and $i^2 = -1$. The real part is $\text{Re}(z) = a$, the imaginary part is $\text{Im}(z) = b$. The *complex conjugate* is $z^* = a - bi$: flip the sign of the imaginary part. The *modulus* is

$$ |z| = \sqrt{z^* z} = \sqrt{a^2 + b^2}, $$

a non-negative real number. The modulus squared is just $|z|^2 = z^* z = a^2 + b^2$.

Euler's formula is the relation that makes complex numbers useful in physics:

$$ e^{i\theta} = \cos\theta + i\sin\theta. $$

If you want to derive it, expand both sides in Taylor series and check that the real and imaginary parts match $\cos$ and $\sin$ term by term. The point: every complex number can be written in *polar form* as $z = r\,e^{i\theta}$, where $r = |z| \geq 0$ is the modulus and $\theta = \arg(z) \in [0, 2\pi)$ is the phase. Multiplication of complex numbers is multiplication of moduli and addition of phases. Conjugation flips the phase sign: $(r\,e^{i\theta})^* = r\,e^{-i\theta}$.

Three facts you will use constantly:

- $|e^{i\theta}| = 1$ for any real $\theta$. (Hence multiplication by a phase factor doesn't change moduli.)
- $e^{i\theta_1} e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$. (Phases add when complex numbers multiply.)
- $(z_1 z_2)^* = z_1^* z_2^*$ and $(z_1 + z_2)^* = z_1^* + z_2^*$. (Conjugation distributes over both operations.)

**Why complex amplitudes are not optional.** Stueckelberg (1960) showed you can reformulate QM with real numbers if you double the dimension of the Hilbert space (one extra real dimension for each complex one). What you cannot do is reformulate it with real numbers in the same dimension. Renou et al. (2021) ran a Bell-inequality experiment that ruled out an entire class of real-amplitude reformulations as inconsistent with observation [Renou et al., *Nature* 600, 625–629, *verify pagination*]. The complex numbers are doing real work; they are not a calculational convenience.

**Worked example: double slit, two amplitudes.** Two slits at $x = \pm d/2$. Light of wavelength $\lambda$ (wavenumber $k = 2\pi/\lambda$) arrives at a screen far away, at angle $\theta$ from the central axis. The path difference between the two slits is $d \sin\theta$. So the two amplitudes at the screen are

$$ \psi_1 = \frac{1}{\sqrt{2}} e^{ikr}, \qquad \psi_2 = \frac{1}{\sqrt{2}} e^{ik(r + d\sin\theta)}. $$

The total amplitude is $\psi = \psi_1 + \psi_2$, and the intensity (probability density) is

$$ |\psi|^2 = \psi^* \psi = \tfrac{1}{2}\big[e^{-ikr} + e^{-ik(r + d\sin\theta)}\big]\big[e^{ikr} + e^{ik(r + d\sin\theta)}\big]. $$

Expand:

$$ |\psi|^2 = \tfrac{1}{2}\big[1 + e^{ikd\sin\theta} + e^{-ikd\sin\theta} + 1\big] = 1 + \cos(kd\sin\theta). $$

Use the identity $1 + \cos x = 2\cos^2(x/2)$:

$$ |\psi|^2 = 2\cos^2\!\left(\frac{kd\sin\theta}{2}\right). $$

The interference pattern. Maxima when $kd\sin\theta = 2n\pi$, i.e., $d\sin\theta = n\lambda$. Minima when $kd\sin\theta = (2n+1)\pi$, i.e., $d\sin\theta = (n + 1/2)\lambda$. The bright and dark fringes follow from the complex algebra; they do not exist in the real-amplitude version.

*The lesson:* phases produce interference. Phases require complex numbers.

### 4.2 Vector spaces and inner products — the structure that survives from linear algebra

You already know real vector spaces from a first linear algebra course. The picture: vectors are columns, you can add them, scale them by real numbers, take dot products, and find orthogonal bases. Almost all of that survives the move to complex vector spaces. One thing changes.

A *complex vector space* $V$ is a set of vectors closed under (a) addition $|\psi\rangle + |\phi\rangle \in V$ and (b) scalar multiplication by complex numbers $\alpha|\psi\rangle \in V$ for $\alpha \in \mathbb{C}$. The familiar example is $\mathbb{C}^n$, columns of $n$ complex numbers. An *inner product* on $V$ is a map $\langle \cdot|\cdot \rangle: V \times V \to \mathbb{C}$ satisfying:

1. **Conjugate symmetry:** $\langle \phi|\psi \rangle = \langle \psi|\phi \rangle^*$. (Reversing the order conjugates the result.)
2. **Linearity in the second slot:** $\langle \phi|\alpha\psi + \beta\chi\rangle = \alpha\langle\phi|\psi\rangle + \beta\langle\phi|\chi\rangle$.
3. **Positive-definite:** $\langle\psi|\psi\rangle \geq 0$, with equality only when $|\psi\rangle$ is the zero vector.

From (1) and (2) it follows that the inner product is *antilinear* in the first slot: $\langle\alpha\phi + \beta\chi|\psi\rangle = \alpha^*\langle\phi|\psi\rangle + \beta^*\langle\chi|\psi\rangle$. This is the physicist convention. Mathematicians sometimes use the opposite convention (linear in the first, antilinear in the second); we follow Griffiths and use the physicist convention throughout.

The *norm* is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$, a non-negative real number. A *Hilbert space* is a complex vector space with an inner product that is *complete* — meaning every Cauchy sequence converges. For finite-dimensional spaces (like $\mathbb{C}^n$) completeness is automatic and you don't need to think about it. For infinite-dimensional spaces — wave functions on the real line — the relevant Hilbert space is $L^2(\mathbb{R})$, the space of square-integrable functions, and completeness is non-trivial mathematics that an undergraduate course mostly elides.

**Concretely in $\mathbb{C}^n$.** Write a vector as a column $|\psi\rangle = (\alpha_1, \alpha_2, \ldots, \alpha_n)^T$. The inner product is

$$ \langle\phi|\psi\rangle = \sum_{i=1}^n \phi_i^* \psi_i. $$

That is the formula. Complex conjugate on the first slot's entries, ordinary multiplication, sum. You have done this calculation a hundred times in real linear algebra; the only difference is the conjugate.

**Concretely on $L^2(\mathbb{R})$.** Write a vector as a function $\psi(x)$ with $\int |\psi(x)|^2 dx < \infty$. The inner product is

$$ \langle\phi|\psi\rangle = \int_{-\infty}^{\infty} \phi^*(x)\, \psi(x)\, dx. $$

Same idea: conjugate the first slot, multiply, integrate (the continuous analog of summing).

**Misconception alert.** "Hilbert space is some special exotic space." It is not. For a single spin-1/2 system, Hilbert space is $\mathbb{C}^2$. For two spin-1/2 systems, it's $\mathbb{C}^4$. For a particle in a box, it's a countable-dimensional space spanned by the basis functions $\sqrt{2/L}\sin(n\pi x/L)$ for $n = 1, 2, 3, \ldots$. For a free particle on the line, it's $L^2(\mathbb{R})$. Each of these is an "inner-product space, complete with respect to the norm" — that's what Hilbert space means.

### 4.3 Dirac notation — the bookkeeping that does work

P. A. M. Dirac introduced bra-ket notation in 1939 [Dirac, *Mathematical Proceedings of the Cambridge Philosophical Society* 35, 416–418](https://doi.org/10.1017/S0305004100021162). It looks like ornament. It isn't. It packages four operations cleanly enough that calculations that would take half a page in indexed-vector notation take three lines in Dirac notation.

**Ket.** $|\psi\rangle$ is the state vector. In $\mathbb{C}^n$, think of it as a column.

**Bra.** $\langle\psi|$ is the *dual vector* — the linear functional that maps $|\phi\rangle \mapsto \langle\psi|\phi\rangle \in \mathbb{C}$. In $\mathbb{C}^n$, the bra is the conjugate transpose of the ket: if $|\psi\rangle = (\alpha_1, \alpha_2)^T$ then $\langle\psi| = (\alpha_1^*, \alpha_2^*)$ as a row. *Both conjugation and transposition.* This is the operation Hermitian conjugation does in general.

**Inner product.** $\langle\phi|\psi\rangle$ is a complex number, the bra acting on the ket. In matrix terms: row times column. In integrals: $\int \phi^*(x)\psi(x)\,dx$.

**Outer product.** $|\psi\rangle\langle\phi|$ is an *operator*: it takes a ket $|\chi\rangle$ to the ket $|\psi\rangle \langle\phi|\chi\rangle = (\text{number}) |\psi\rangle$. In matrix terms: column times row = $n \times n$ matrix.

You have to internalize two identities to use Dirac notation fluently.

**The completeness relation.** For any orthonormal basis $\{|n\rangle\}_{n=1}^N$,

$$ \sum_n |n\rangle\langle n| = \hat{I}, $$

where $\hat{I}$ is the identity operator. The reason: any $|\psi\rangle = \sum_n c_n |n\rangle$, and the components are $c_n = \langle n|\psi\rangle$, so $|\psi\rangle = \sum_n |n\rangle\langle n|\psi\rangle = (\sum_n |n\rangle\langle n|)|\psi\rangle$. The sum is the identity. Inserting it between operators — "resolving the identity" — is the single most common Dirac-notation maneuver in QM calculations.

**The position-basis resolution.** For the continuous case (a particle on a line),

$$ \int dx\, |x\rangle\langle x| = \hat{I}, \quad \text{with}\quad \langle x|\psi\rangle = \psi(x). $$

The position kets $|x\rangle$ are not normalizable — $\langle x|x'\rangle = \delta(x - x')$, a Dirac delta, not a Kronecker delta. They are not physical states. They are calculational devices, *generalized* eigenvectors that live in a larger space (the "rigged Hilbert space") than $L^2(\mathbb{R})$ itself. Griffiths handles this in a footnote in Ch. 3.3. The student should know about the issue, defer the rigor (Ballentine *Quantum Mechanics: A Modern Development* Ch. 1 is the standard reference), and proceed.

The big payoff: the wave function $\psi(x)$ is *the position-basis component* of the abstract state vector $|\psi\rangle$. Two notations, same object:

$$ |\psi\rangle = \int dx\, \psi(x) |x\rangle. $$

You can switch between abstract Dirac notation and concrete wave-function notation by inserting $\int dx |x\rangle\langle x|$ or its discrete-basis cousin $\sum_n |n\rangle\langle n|$.

**Worked example: norm and probabilities in $\mathbb{C}^2$.** Take

$$ |\psi\rangle = \frac{3}{5}|0\rangle + \frac{4i}{5}|1\rangle, $$

with $\{|0\rangle, |1\rangle\}$ an orthonormal basis of $\mathbb{C}^2$. The bra is

$$ \langle\psi| = \frac{3}{5}\langle 0| - \frac{4i}{5}\langle 1| $$

— *conjugate* the coefficients, not just transpose. Now compute the norm:

$$ \langle\psi|\psi\rangle = \left(\frac{3}{5}\right)\left(\frac{3}{5}\right) + \left(-\frac{4i}{5}\right)\left(\frac{4i}{5}\right) = \frac{9}{25} + \frac{16}{25} = 1. $$

The minus from conjugation and the $i^2 = -1$ combine to give $-(4i)(4i)/25 = +16/25$. The state is normalized.

Probability of measuring outcome "0": $|\langle 0|\psi\rangle|^2 = |3/5|^2 = 9/25 = 36\%$. Probability of "1": $|4i/5|^2 = 16/25 = 64\%$. They sum to 1, as they must.

**Misconception alert.** The single most common student error in matrix-element calculations: $\langle\phi|\hat{A}|\psi\rangle$ computed by writing $\phi$'s components as a row *without conjugating them*, multiplying by $\hat{A}$'s matrix, and contracting with $\psi$. The result is the wrong number (complex when it should be real, in general). Always conjugate when you turn a ket into a bra. If you find yourself with a complex-valued "expectation value" for a Hermitian observable, that is the bug. Look for the missing conjugation.

### 4.4 Operators and eigenvalue equations

A *linear operator* $\hat{A}$ on a vector space $V$ is a map $V \to V$ satisfying $\hat{A}(\alpha|\psi\rangle + \beta|\phi\rangle) = \alpha\hat{A}|\psi\rangle + \beta\hat{A}|\phi\rangle$. In $\mathbb{C}^n$, every linear operator is represented by an $n \times n$ matrix once a basis is chosen.

The *eigenvalue equation* is

$$ \hat{A}|a\rangle = a|a\rangle, $$

a vector $|a\rangle$ that the operator leaves in the same direction, scaled by a complex number $a$. The set of all eigenvalues $a$ is the *spectrum* of $\hat{A}$. You find the eigenvalues by solving the characteristic polynomial $\det(\hat{A} - a\hat{I}) = 0$, and for each eigenvalue you find the corresponding eigenvectors by solving $(\hat{A} - a\hat{I})|a\rangle = 0$.

**The spectral theorem** (finite-dimensional Hermitian case, which is everything you'll see in Unit 2): if $\hat{A}$ is Hermitian (defined below), then

1. All eigenvalues are real.
2. Eigenvectors corresponding to distinct eigenvalues are orthogonal.
3. The eigenvectors can be chosen to form an orthonormal basis of $V$.

The consequence: any state can be expanded in the eigenbasis of $\hat{A}$ as $|\psi\rangle = \sum_n c_n |a_n\rangle$ with $c_n = \langle a_n|\psi\rangle$, and the operator itself decomposes as

$$ \hat{A} = \sum_n a_n |a_n\rangle\langle a_n|. $$

This *spectral decomposition* is the computational engine of QM. Measurement probabilities, expectation values, and time evolution all reduce to algebra on this decomposition.

**Common misconception.** "Every operator has eigenvectors that form a basis." False for general operators. The spectral theorem is specific to *normal* operators — operators that commute with their adjoint, $\hat{A}\hat{A}^\dagger = \hat{A}^\dagger\hat{A}$. Hermitian operators (where $\hat{A}^\dagger = \hat{A}$) and unitary operators (where $\hat{A}^\dagger\hat{A} = \hat{I}$) are both normal, and these cover everything you'll meet in introductory QM. But you should know the constraint exists.

**Worked example: two-level atom with off-diagonal coupling.** Take

$$ \hat{H} = \varepsilon(|0\rangle\langle 1| + |1\rangle\langle 0|) = \varepsilon \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}. $$

Characteristic polynomial: $\det(\hat{H} - E\hat{I}) = E^2 - \varepsilon^2 = 0$, so $E = \pm\varepsilon$. For $E = +\varepsilon$, solve $(\hat{H} - \varepsilon\hat{I})|+\rangle = 0$:

$$ \varepsilon \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0 \implies a = b. $$

Normalized: $|+\rangle = (1/\sqrt{2})(|0\rangle + |1\rangle)$. For $E = -\varepsilon$ similarly: $|-\rangle = (1/\sqrt{2})(|0\rangle - |1\rangle)$. The eigenvectors are orthogonal: $\langle+|-\rangle = (1/2)(\langle 0| + \langle 1|)(|0\rangle - |1\rangle) = (1/2)(1 - 1) = 0$. Check.

This is the ammonia molecule's tunneling Hamiltonian, the simplest neutrino-oscillation Hamiltonian, and a basic model of every two-level atom. The same matrix, with different names attached.

### 4.5 Hermitian operators and observables

An operator $\hat{A}$ is *Hermitian* (or *self-adjoint* — the distinction matters in infinite dimensions; see flag below) if $\hat{A}^\dagger = \hat{A}$, where $\hat{A}^\dagger$ is the *adjoint*, defined by the inner-product relation

$$ \langle\phi|\hat{A}\psi\rangle = \langle \hat{A}^\dagger\phi|\psi\rangle \quad \text{for all } |\phi\rangle, |\psi\rangle. $$

In matrix form, $\hat{A}^\dagger$ is the *conjugate transpose* of $\hat{A}$. Component-wise: $(A^\dagger)_{ij} = A_{ji}^*$. *Both* swap the indices *and* take the complex conjugate. Hermitian means $A_{ij} = A_{ji}^*$. The diagonal entries are therefore real (since $A_{ii} = A_{ii}^*$ forces $\text{Im}(A_{ii}) = 0$).

**The first postulate of QM in operator language:** every observable is represented by a Hermitian operator. The eigenvalues of the operator are the possible measurement outcomes. The spectral theorem (eigenvalues real, eigenstates orthogonal, eigenstates a complete basis) is the *reason* measurement outcomes are real numbers, the *reason* the Born rule is well-defined, and the *reason* repeated measurements of the same observable give the same result.

**Misconception, the most important one in this unit:** "Hermitian = symmetric matrix." Wrong for complex matrices. For a real matrix, transpose = conjugate transpose, and Hermitian collapses to symmetric. For a complex matrix, they are different. The matrix

$$ \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} $$

is *Hermitian* — $\sigma_y^\dagger$ swaps the off-diagonal entries and conjugates them, so the $-i$ at position (1,2) becomes $+i$ at position (2,1) (conjugate of $-i$), and the $+i$ at position (2,1) becomes $-i$ at position (1,2). Same matrix. Hermitian. But $\sigma_y$ is *not symmetric* — symmetric means $A_{ij} = A_{ji}$ without conjugation, and $-i \neq +i$. So $\sigma_y$ is the cleanest example of a Hermitian-but-not-symmetric matrix. The companion will use it as the canonical example whenever the distinction comes up.

**The three Pauli matrices.** These are the spin-1/2 observables along $x$, $y$, $z$. Memorize them.

$$ \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. $$

All three are Hermitian. All three square to the identity. All three have eigenvalues $\pm 1$. Their eigenvectors are different.

**Worked example: diagonalize $\sigma_z$.** The matrix is already diagonal. Eigenvalues $\pm 1$. Eigenvectors

$$ |\!\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}. $$

Check: $\sigma_z |\!\uparrow\rangle = (+1)|\!\uparrow\rangle$, $\sigma_z |\!\downarrow\rangle = (-1)|\!\downarrow\rangle$. These are the spin-up and spin-down states along the $z$-axis.

**Worked example: diagonalize $\sigma_x$.** Characteristic polynomial: $\det(\sigma_x - \lambda I) = \lambda^2 - 1 = 0$, so $\lambda = \pm 1$. For $\lambda = +1$, solve

$$ \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0 \implies a = b. $$

Normalized: $|+_x\rangle = (1/\sqrt{2})(1, 1)^T = (1/\sqrt{2})(|\!\uparrow\rangle + |\!\downarrow\rangle)$. For $\lambda = -1$: $|-_x\rangle = (1/\sqrt{2})(1, -1)^T = (1/\sqrt{2})(|\!\uparrow\rangle - |\!\downarrow\rangle)$.

The spin-x eigenstates are *superpositions* of the spin-z eigenstates. This is the central fact about non-commuting observables: if you know the spin along $z$, you don't know it along $x$. The math is just basis change.

**Worked example: diagonalize $\sigma_y$.** Characteristic polynomial: $\det(\sigma_y - \lambda I) = \lambda^2 - i \cdot (-i) = \lambda^2 - 1 = 0$, so $\lambda = \pm 1$. For $\lambda = +1$:

$$ \begin{pmatrix} -1 & -i \\ i & -1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0 \implies -a - ib = 0 \implies b = ia. $$

Normalized: $|+_y\rangle = (1/\sqrt{2})(1, i)^T = (1/\sqrt{2})(|\!\uparrow\rangle + i|\!\downarrow\rangle)$. For $\lambda = -1$: $|-_y\rangle = (1/\sqrt{2})(1, -i)^T = (1/\sqrt{2})(|\!\uparrow\rangle - i|\!\downarrow\rangle)$.

Notice that the components are *complex* — $|+_y\rangle$ has a real first component and an imaginary second component. There is no real-coefficient eigenvector of $\sigma_y$. This is the worked example where the student sees, concretely, that complex numbers are not optional. Try to write a real $2 \times 2$ matrix with eigenvalues $\pm 1$ that has *only real eigenvectors* and is unitarily equivalent to $\sigma_y$. You can't. The chirality is built into the complex structure.

*The lesson:* the three Pauli matrices are three Hermitian operators on $\mathbb{C}^2$ with the same spectrum $\{+1, -1\}$ and three different eigenbases. Linear algebra over $\mathbb{C}$ is what makes them distinct.

**Apply this to $\sigma_x|\!\uparrow\rangle$.** Compute:

$$ \sigma_x |\!\uparrow\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle. $$

So $\sigma_x |\!\uparrow\rangle = |\!\downarrow\rangle$. The spin-up state is *not* a $\sigma_x$ eigenstate — applying $\sigma_x$ takes it to the orthogonal state.

Now expand $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis. From the worked examples, $|+_x\rangle = (1/\sqrt{2})(|\!\uparrow\rangle + |\!\downarrow\rangle)$ and $|-_x\rangle = (1/\sqrt{2})(|\!\uparrow\rangle - |\!\downarrow\rangle)$. Inverting:

$$ |\!\uparrow\rangle = \frac{1}{\sqrt{2}}(|+_x\rangle + |-_x\rangle). $$

The probability of measuring $\sigma_x = +1$ given the state $|\!\uparrow\rangle$ is $|\langle +_x|\!\uparrow\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$. Same for $\sigma_x = -1$. A spin-up-along-$z$ particle is 50/50 along $x$. This is the linear-algebra statement of the Stern–Gerlach experiment when you rotate the second magnet.

### 4.6 Verifying $\hat{p} = -i\hbar\,d/dx$ is Hermitian

The momentum operator in the position representation is $\hat{p} = -i\hbar\,d/dx$. It is Hermitian on the space of square-integrable functions vanishing at infinity. The verification is the cleanest example of how Hermiticity works for differential operators, and Griffiths Ch. 3.2 Example 3.1 does this calculation. It is worth stepping through here.

We want to check $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$, i.e.,

$$ \int_{-\infty}^\infty \phi^*(x)\left(-i\hbar \frac{d\psi}{dx}\right) dx = \int_{-\infty}^\infty \left(-i\hbar \frac{d\phi}{dx}\right)^* \psi(x)\, dx. $$

The right-hand side is $\int (+i\hbar\, d\phi^*/dx)\,\psi\, dx$. So we need

$$ -i\hbar \int \phi^* \frac{d\psi}{dx}\, dx \stackrel{?}{=} +i\hbar \int \frac{d\phi^*}{dx}\,\psi\, dx. $$

Integrate the left side by parts:

$$ \int_{-\infty}^\infty \phi^* \frac{d\psi}{dx}\, dx = \left[\phi^* \psi\right]_{-\infty}^\infty - \int_{-\infty}^\infty \frac{d\phi^*}{dx}\,\psi\, dx. $$

For square-integrable functions, $\phi^* \psi \to 0$ as $|x| \to \infty$ (otherwise the integral $\int|\psi|^2$ diverges). The boundary term vanishes. So

$$ \int \phi^* \frac{d\psi}{dx}\, dx = -\int \frac{d\phi^*}{dx}\,\psi\, dx, $$

and multiplying both sides by $-i\hbar$:

$$ -i\hbar\int \phi^* \frac{d\psi}{dx}\, dx = +i\hbar\int \frac{d\phi^*}{dx}\,\psi\, dx. $$

Which is what we needed. So $\hat{p}^\dagger = \hat{p}$ on this space.

Two morals. First: the Hermiticity of $\hat{p}$ depends on the *boundary conditions*. For a particle on a finite interval with non-zero boundary values, the proof above fails; $\hat{p}$ may not be Hermitian on that domain, and you have to specify the domain explicitly. This is the Hermitian-versus-self-adjoint distinction in disguise, and it's why Reed and Simon (*Methods of Modern Mathematical Physics*, Vol. 1) is the reference when this matters in earnest. Second: the factor of $-i$ in $\hat{p}$ is essential. Without the $i$, the operator $d/dx$ is *anti-Hermitian* — $\hat{A}^\dagger = -\hat{A}$ — by the same integration-by-parts argument. Multiplying by $i$ rotates anti-Hermitian to Hermitian. That is one structural reason QM's basic operators all carry $i$'s.

## 5. Synthesis: the abstract picture

Quantum states are vectors in a complex Hilbert space. Observables are Hermitian operators on that space. The eigenvalues of an observable are the possible outcomes of a measurement; the eigenvectors form an orthonormal basis in which the state expands as $|\psi\rangle = \sum_n c_n |a_n\rangle$. The probability of getting outcome $a_n$ is $|c_n|^2 = |\langle a_n|\psi\rangle|^2$. The expectation value is $\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \sum_n a_n |c_n|^2$.

This is the whole formalism. Five tools: complex numbers, vector spaces with inner products, Dirac notation, eigenvalue equations, Hermitian operators. With them you can state the Schrödinger equation (Unit 3), solve specific potential problems (Unit 4), build the measurement postulate and the uncertainty principle (Unit 5), and proceed through the rest of QM. Without them — as in the pop-sci book — QM is a list of facts to memorize. With them, it is a working theory you can do calculations in.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Complex numbers | not in Griffiths proper; assumed prerequisite | ❌ | §4.1 (full treatment) |
| Vector spaces and inner products | Ch. 3.1 | ❌ | §4.2 |
| Dirac notation | Ch. 3.3 | ❌ | §4.3 |
| Operators and eigenvalue equations | Ch. 3.2 | ❌ | §4.4 |
| Hermitian operators and observables | Ch. 3.2 (Example 3.1) | ❌ | §4.5, §4.6 |
| Pauli matrices | Ch. 4.4 (briefly; spin systems) | ❌ | §4.5 worked examples |

Pop-sci book is unusable here. Griffiths Ch. 3 is the spine; read it after working through this companion. Shankar Ch. 1 ([2nd ed., 1994](https://link.springer.com/book/10.1007/978-1-4757-0576-8)) is the alternative reference, more rigorous and longer; if you have the time, read it for a second pass. Sakurai *Modern Quantum Mechanics* Ch. 1 is graduate-level and should be on your shelf for later.

## 7. Exercises

**E1 (L1, Knowledge).** State (a) Euler's formula, (b) the definition of the inner product in $\mathbb{C}^n$, (c) the eigenvalue equation, (d) the Hermiticity condition in matrix-element form $A_{ij} = A_{ji}^*$, and (e) the completeness relation $\sum_n |n\rangle\langle n| = \hat{I}$.

**E2 (L2, Comprehension).** Translate the following from Dirac notation to wave-function notation: $\langle\phi|\hat{p}|\psi\rangle$ where $\hat{p} = -i\hbar\,d/dx$. Write it as an integral over $x$. Then translate back.

**E3 (L3, Application).** Diagonalize the Hamiltonian

$$ \hat{H} = \begin{pmatrix} E_0 & V \\ V^* & E_0 \end{pmatrix} $$

for real $E_0$ and complex $V$. Find the eigenvalues and eigenvectors explicitly. Check that the eigenvectors are orthogonal.

**E4 (L3, Application).** Take the state $|\psi\rangle = (1/\sqrt{5})(|+_y\rangle + 2|-_y\rangle)$ in the $\sigma_y$ eigenbasis. (a) Verify the state is normalized. (b) Compute $\langle\sigma_y\rangle = \langle\psi|\sigma_y|\psi\rangle$. (c) Compute $\langle\sigma_z\rangle$ by first re-expressing $|\psi\rangle$ in the $\{|\!\uparrow\rangle, |\!\downarrow\rangle\}$ basis. *Check that $\langle\sigma_y\rangle$ is real.*

**E5 (L4, Analysis).** Show that the *commutator* of two Hermitian operators, $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$, is anti-Hermitian — that is, $[\hat{A}, \hat{B}]^\dagger = -[\hat{A}, \hat{B}]$. Use the rule for Hermitian conjugation of a product: $(\hat{A}\hat{B})^\dagger = \hat{B}^\dagger\hat{A}^\dagger$. (You should derive this rule too, if you haven't already.)

**E6 (L4, Analysis).** Compute the commutators $[\sigma_x, \sigma_y]$, $[\sigma_y, \sigma_z]$, $[\sigma_z, \sigma_x]$ directly from the matrix definitions. You should find $[\sigma_i, \sigma_j] = 2i\,\varepsilon_{ijk}\sigma_k$ (with $\varepsilon_{ijk}$ the Levi-Civita symbol). This is the spin-1/2 angular momentum algebra; it will return in Unit 7.

**E7 (L5, Evaluation).** Consider the matrix

$$ M = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}. $$

Is it Hermitian? Is it symmetric? Is it unitary ($M^\dagger M = I$)? Does it have a basis of orthonormal eigenvectors? Justify each answer with a direct calculation.

**E8 (L6, Synthesis).** Show that $\hat{x}$, $\hat{p}$, and the Hamiltonian $\hat{H} = \hat{p}^2/2m + V(\hat{x})$ are all Hermitian on the space of square-integrable functions on the line. You may use the result for $\hat{p}$ from §4.6 directly. State precisely what assumptions about the boundary behavior of $\psi$ and $V$ you are using.

## 8. What would change my mind

The structural argument of this unit — that quantum mechanics requires complex amplitudes, Hermitian operators on a Hilbert space, and a Born-rule probability formula $|\langle a|\psi\rangle|^2$ — is settled at the operational level by a century of experimental success. Renou et al. (2021) tightened the screw on the complex-amplitude requirement specifically, ruling out a broad class of real-amplitude reformulations on Bell-inequality grounds [Renou et al., *Nature* 600, 625–629, *verify*]. What would force me to revise the unit's claim: a reproducible experiment in which complex amplitudes were demonstrably *not* required to reproduce the measured probabilities (i.e., a real-amplitude theory that survived a stringent Bell-inequality test). None has appeared. A weaker revision — adopting a non-Hermitian "$\mathcal{PT}$-symmetric" extension of QM for certain open systems (Bender & Boettcher 1998) — has been proposed in the literature and remains contested; the standard mathematical foundations here apply to closed systems, and the unit's claim is restricted accordingly.

## 9. Still puzzling

- *Why complex numbers, not quaternions?* The Stueckelberg argument rules out real-only QM in fixed dimension; the Renou result tightens it experimentally. But you could in principle replace $\mathbb{C}$ with the quaternions $\mathbb{H}$ and still have a sensible-looking formalism (Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995). Why does nature pick $\mathbb{C}$ specifically? Open question; the conventional answer is "no experimental need for $\mathbb{H}$ has appeared."

- *The rigged Hilbert space.* Position and momentum eigenvectors $|x\rangle$ and $|p\rangle$ are not normalizable; they live in a larger space than $L^2(\mathbb{R})$ itself. This is mathematically clean (Gelfand triples, distribution theory) but it is genuinely outside the formalism of a Hilbert space proper. Undergraduate texts elide this; the curious student is pointed to Ballentine *Quantum Mechanics: A Modern Development*, Ch. 1.

- *Hermitian versus self-adjoint.* In finite dimensions these coincide. In infinite dimensions they don't always, and the distinction has physical content — a Hermitian operator that fails self-adjointness on a given domain may have ambiguous physical interpretation (e.g., a "particle in a half-line" requires a boundary condition that pins down which self-adjoint extension you mean). Reed & Simon Vol. 2 is the reference. The companion will return to this in Unit 4 when half-line problems first appear.

- *Why is the state space projective?* If $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ produce the same physical predictions for all $\alpha$, then the "real" state space is the set of normalized vectors modulo the global phase — projective Hilbert space, $\mathbb{CP}^{n-1}$ for finite dimensions. Why should the mathematical formalism carry this redundancy? One answer: the redundancy is the price of linearity (you need vectors so you can superpose, but vectors carry extra information that physical states do not). Whether there is a deeper reason is open.

**Tags:** dirac-notation, hermitian-operators, pauli-matrices, complex-amplitudes, hilbert-space, eigenvalues, griffiths-ch3, linear-algebra
