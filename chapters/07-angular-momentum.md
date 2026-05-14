# Unit 7 — Angular Momentum

> The cleanest demonstration in undergraduate quantum mechanics that an entire spectrum of measurable values can come out of an operator algebra and nothing else.

---

## 1. What this chapter is doing

Unit 6 wrote down four quantum numbers, used the operators $\hat{L}^2$ and $\hat{L}_z$, and asserted their eigenvalues. We owed you a derivation. This chapter pays the debt.

Three things will get built here from the ground up. First, the operator algebra of orbital angular momentum — the commutation relations and the ladder operators $\hat{L}_\pm$ — and a derivation of the eigenvalue spectrum $\hbar^2\ell(\ell+1)$ and $m\hbar$ from that algebra alone, with no reference to any spatial wave function. Second, the spin-1/2 representation: the Pauli matrices, the spinor character, the $720^\circ$ rotation. Third, the addition of two angular momenta — done explicitly for two spin-1/2 particles, ending at the construction of the singlet state $|0,0\rangle$.

The singlet is not a curiosity. It is the canonical maximally entangled two-qubit state. It is the state Bohm used to recast the Einstein–Podolsky–Rosen argument in 1951, and it is the state at the center of every Bell-inequality experiment ever run. When we build it here in §5, we are setting up Unit 10's encounter with Bell's theorem. Hold that in mind: the construction is not for its own sake. It is the bridge.

A note on conventions. We are going to use $\hat{L}$ for orbital angular momentum, $\hat{S}$ for spin, and $\hat{J}$ when we want to talk about *any* angular momentum (the algebra is the same; the labels differ by what space the operators act on). Whenever a derivation works for all three, we will use $\hat{J}$. When the specific commutation relation $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$ is doing work — which it does for spin too — read $\hat{L}$ as a stand-in for "any of them."

---

## 2. Learning objectives

By the end of this chapter you should be able to:

1. **Compute** the commutator $[\hat{L}_x, \hat{L}_y]$ directly from $\hat{L} = \hat{r} \times \hat{p}$ and the canonical commutator $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$.
2. **Derive** the eigenvalue spectrum of $\hat{J}^2$ and $\hat{J}_z$ using the ladder operators $\hat{J}_\pm$ and bounded-spectrum arguments.
3. **Apply** the Pauli matrices to compute expectation values, eigenstates, and measurement probabilities for spin-1/2 systems.
4. **Construct** the singlet and triplet states for two spin-1/2 particles using the ladder-operator method.
5. **Evaluate** the "vector model" picture of angular momentum — identify where it helps and where it actively misleads.
6. **Distinguish** orbital angular momentum (integer $\ell$ only) from spin angular momentum (half-integer allowed) and explain the topological reason for the distinction.

---

## 3. The motivating problem

A student raises her hand in office hours. She says: "I get that $\ell$ shows up in three places. It's the eigenvalue of $\hat{L}^2$ — well, with a $(\ell+1)$ factor I don't understand. It's the label on the state. And it determines the range of $m_\ell$ from $-\ell$ to $+\ell$. Why is the same letter doing three jobs? Where does any of this come from?"

She is asking the right question. Most introductory quantum-mechanics texts present $\hat{L}^2 \psi = \hbar^2\ell(\ell+1)\psi$ as if it descended from a mountain. The $(\ell+1)$ feels like an arbitrary correction. The fact that $|m_\ell| \leq \ell$ feels like a coincidence. The whole apparatus floats free of any derivation, and students absorb it as a memory exercise.

It does not have to be that way. The eigenvalue spectrum of angular momentum follows from one fact — that the components of $\hat{L}$ do not commute, $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$ — together with the requirement that physical operators have real expectation values and that the spectrum of $\hat{L}_z$ be bounded above and below in any finite-norm state. Run those constraints through the algebra of the ladder operators $\hat{L}_\pm = \hat{L}_x \pm i \hat{L}_y$ and the entire spectrum falls out. You can do the derivation in two pages. We will.

Once that is in hand, spin becomes a question of which representation of the same algebra you are using. Orbital angular momentum lives on functions of $\theta$ and $\phi$; integer $\ell$ only, because single-valuedness on the sphere demands it. Spin-1/2 lives on a two-dimensional complex vector space; half-integer is allowed, and that is where the Pauli matrices come from. The whole structure is one algebra in two representations.

This is the pivot of the undergraduate quantum-mechanics course. Get the ladder-operator derivation, and angular momentum is *yours*. Skip it, and you are memorizing tables for the rest of your physics education.

---

## 4. Concept blocks

### 4.1 Orbital angular momentum operators and their commutators

Classical angular momentum is $\vec{L} = \vec{r} \times \vec{p}$. Componentwise:

$$L_x = y p_z - z p_y, \quad L_y = z p_x - x p_z, \quad L_z = x p_y - y p_x.$$

To go quantum, promote each position and momentum to an operator. The canonical commutator $[\hat{x}_i, \hat{p}_j] = i\hbar \delta_{ij}$ — and $[\hat{x}_i, \hat{x}_j] = [\hat{p}_i, \hat{p}_j] = 0$ — gives the angular-momentum components non-trivial commutators among themselves. Let's compute $[\hat{L}_x, \hat{L}_y]$ explicitly because it is the cornerstone of the chapter and almost no student has actually run the calculation.

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y, \,\hat{z}\hat{p}_x - \hat{x}\hat{p}_z].$$

Expand using bilinearity:

$$= [\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] - [\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] - [\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] + [\hat{z}\hat{p}_y, \hat{x}\hat{p}_z].$$

Now use $[AB, CD] = A[B,C]D + AC[B,D] + [A,C]DB + C[A,D]B$ — but more efficiently, notice that most terms vanish because almost every pair of operators here commutes. The only non-commuting pairs are $[\hat{x}_i, \hat{p}_i] = i\hbar$. Working through:

- $[\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] = \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x = \hat{y}(-i\hbar)\hat{p}_x = -i\hbar\,\hat{y}\hat{p}_x.$
- $[\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] = 0$ (no shared $x_i / p_i$ pair).
- $[\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] = 0$ (likewise).
- $[\hat{z}\hat{p}_y, \hat{x}\hat{p}_z] = [\hat{z}, \hat{p}_z]\hat{p}_y \hat{x} = (i\hbar)\hat{p}_y\hat{x} = i\hbar\,\hat{x}\hat{p}_y.$

Sum:

$$[\hat{L}_x, \hat{L}_y] = -i\hbar\,\hat{y}\hat{p}_x + i\hbar\,\hat{x}\hat{p}_y = i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar \hat{L}_z.$$

Cyclically:

$$\boxed{[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z, \quad [\hat{L}_y, \hat{L}_z] = i\hbar \hat{L}_x, \quad [\hat{L}_z, \hat{L}_x] = i\hbar \hat{L}_y.}$$

Read these as the *defining relations* of an angular-momentum algebra. Any three operators satisfying this Lie-bracket structure deserve to be called components of an angular momentum — whether they came from $\vec{r}\times\vec{p}$ or from somewhere else entirely (like spin).

A useful consequence: $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$ commutes with every component. Quick proof for $\hat{L}_z$:

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z] + [\hat{L}_z^2, \hat{L}_z].$$

The last term is zero. For the first two, $[\hat{L}_x^2, \hat{L}_z] = \hat{L}_x[\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x = -i\hbar(\hat{L}_x \hat{L}_y + \hat{L}_y \hat{L}_x)$, and similarly $[\hat{L}_y^2, \hat{L}_z] = +i\hbar(\hat{L}_y \hat{L}_x + \hat{L}_x \hat{L}_y)$. They cancel. So

$$[\hat{L}^2, \hat{L}_z] = 0.$$

Same for $\hat{L}_x$ and $\hat{L}_y$. The takeaway: $\hat{L}^2$ and any single component can be simultaneously diagonalized. The components themselves cannot — $[\hat{L}_x, \hat{L}_y] \neq 0$ — so a state of definite $L_x$ is not a state of definite $L_y$. They are incompatible observables.

By convention we diagonalize $\hat{L}^2$ and $\hat{L}_z$ together. The simultaneous eigenstates we will label $|\ell, m\rangle$, with

$$\hat{L}^2 |\ell, m\rangle = \lambda |\ell, m\rangle, \quad \hat{L}_z |\ell, m\rangle = m\hbar |\ell, m\rangle.$$

We have not yet shown that $\lambda = \hbar^2\ell(\ell+1)$ or that $m$ is bounded. We will, in §4.2.

### 4.2 Ladder operators and the eigenvalue spectrum — the deep dive

Define

$$\hat{L}_\pm \equiv \hat{L}_x \pm i \hat{L}_y.$$

These are *not* Hermitian — they are each other's adjoints, $\hat{L}_+^\dagger = \hat{L}_-$ — so they are not observables. They are tools.

**Step 1: Compute the relevant commutators.**

$$[\hat{L}_z, \hat{L}_\pm] = [\hat{L}_z, \hat{L}_x] \pm i [\hat{L}_z, \hat{L}_y] = i\hbar \hat{L}_y \pm i(-i\hbar \hat{L}_x) = \pm \hbar (\hat{L}_x \pm i\hat{L}_y) = \pm \hbar \hat{L}_\pm.$$

So $[\hat{L}_z, \hat{L}_\pm] = \pm \hbar \hat{L}_\pm$. Also $[\hat{L}^2, \hat{L}_\pm] = 0$ (since $\hat{L}^2$ commutes with each component, hence with their sum).

**Step 2: Show that $\hat{L}_\pm$ raise and lower $m$ by one.**

Suppose $|\ell, m\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $m\hbar$. Then

$$\hat{L}_z (\hat{L}_+ |\ell, m\rangle) = (\hat{L}_+ \hat{L}_z + [\hat{L}_z, \hat{L}_+]) |\ell, m\rangle = \hat{L}_+ (m\hbar) |\ell, m\rangle + \hbar \hat{L}_+ |\ell, m\rangle = (m+1)\hbar \cdot \hat{L}_+ |\ell, m\rangle.$$

So $\hat{L}_+ |\ell, m\rangle$ is also an eigenstate of $\hat{L}_z$, with eigenvalue $(m+1)\hbar$. Similarly $\hat{L}_- |\ell, m\rangle$ has $\hat{L}_z$ eigenvalue $(m-1)\hbar$. The raising and lowering does not change $\hat{L}^2$ (because $[\hat{L}^2, \hat{L}_\pm] = 0$). So $\hat{L}_\pm$ moves us up or down a ladder of $\hat{L}_z$ eigenvalues, all sharing the same $\hat{L}^2$ eigenvalue $\lambda$.

**Step 3: The spectrum is bounded.**

Here is the key observation. The operator $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$ is a sum of squares of Hermitian operators. Its expectation value in any state is non-negative:

$$\langle \hat{L}_x^2 + \hat{L}_y^2 \rangle = \langle \hat{L}_x \psi | \hat{L}_x \psi\rangle + \langle \hat{L}_y \psi | \hat{L}_y \psi\rangle \geq 0.$$

In an eigenstate $|\ell, m\rangle$, this says

$$\lambda - m^2 \hbar^2 \geq 0 \implies m^2 \leq \lambda/\hbar^2.$$

The values of $m$ on any rung of the ladder are bounded above by $+\sqrt{\lambda/\hbar^2}$ and below by $-\sqrt{\lambda/\hbar^2}$. The ladder cannot extend forever in either direction. There must be a top rung $|\ell, m_{\max}\rangle$ that $\hat{L}_+$ annihilates and a bottom rung $|\ell, m_{\min}\rangle$ that $\hat{L}_-$ annihilates.

**Step 4: Compute $\lambda$.**

We use a useful identity. Multiply out:

$$\hat{L}_- \hat{L}_+ = (\hat{L}_x - i\hat{L}_y)(\hat{L}_x + i\hat{L}_y) = \hat{L}_x^2 + \hat{L}_y^2 + i[\hat{L}_x, \hat{L}_y] = \hat{L}^2 - \hat{L}_z^2 - \hbar \hat{L}_z.$$

Apply this to the top rung $|\ell, m_{\max}\rangle$. Since $\hat{L}_+ |\ell, m_{\max}\rangle = 0$:

$$0 = \hat{L}_- \hat{L}_+ |\ell, m_{\max}\rangle = (\hat{L}^2 - \hat{L}_z^2 - \hbar \hat{L}_z)|\ell, m_{\max}\rangle = (\lambda - m_{\max}^2 \hbar^2 - m_{\max} \hbar^2)|\ell, m_{\max}\rangle.$$

So

$$\lambda = m_{\max}(m_{\max} + 1)\hbar^2.$$

Define $\ell \equiv m_{\max}$. Then

$$\boxed{\lambda = \hbar^2\ell(\ell + 1).}$$

There it is. The $(\ell+1)$ factor is not a correction. It comes from the algebra. Specifically, it comes from the fact that $\hat{L}_+\hat{L}_-$ contains the cross-term $i[\hat{L}_x,\hat{L}_y] = -\hbar \hat{L}_z$, which adds a $-\hbar \hat{L}_z$ to the would-be $\hat{L}_x^2 + \hat{L}_y^2$. The non-commutativity of the components shows up in the spectrum.

The same calculation on the bottom rung — using $\hat{L}_+ \hat{L}_- = \hat{L}^2 - \hat{L}_z^2 + \hbar \hat{L}_z$ and $\hat{L}_- |\ell, m_{\min}\rangle = 0$ — gives $\lambda = m_{\min}(m_{\min} - 1)\hbar^2$. Combined with $\lambda = \ell(\ell+1)\hbar^2$:

$$m_{\min}(m_{\min} - 1) = \ell(\ell+1) \implies m_{\min} = -\ell.$$

**Step 5: $m$ goes from $-\ell$ to $+\ell$ in integer steps.**

The ladder goes from $-\ell$ to $+\ell$ by applying $\hat{L}_+$ repeatedly. Each application increases $m$ by 1. So the difference $\ell - (-\ell) = 2\ell$ must be an integer. So $\ell$ itself is either an integer ($0, 1, 2, \ldots$) or a half-integer ($1/2, 3/2, \ldots$).

For *orbital* angular momentum, we will see in §4.3 that half-integer $\ell$ is excluded by single-valuedness of the spatial wave function. Half-integer values are allowed only for spin and other purely internal angular momenta. The algebra alone does not distinguish — both kinds of representation exist.

**Summary of the derivation.** From the single fact $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$ plus the non-negativity of expectation values of $\hat{L}_x^2 + \hat{L}_y^2$, we have derived:

- $\hat{L}^2$ has eigenvalues $\hbar^2 \ell(\ell+1)$ with $\ell \in \{0, 1/2, 1, 3/2, 2, \ldots\}$.
- $\hat{L}_z$ has eigenvalues $m\hbar$ with $m \in \{-\ell, -\ell+1, \ldots, +\ell\}$ — exactly $(2\ell+1)$ values.

No spatial integration. No differential equations. Pure algebra. (Griffiths §4.3.1 walks through essentially this derivation; the version above slows it down. [Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch. 3](https://www.cambridge.org/highereducation/books/modern-quantum-mechanics/05A2BF93C73B5BB91EC0E63D45D4DD78) [verify edition] gives the same construction using the symbol $\hat{J}$ for generality.)

### 4.3 Spherical harmonics — the position representation

When $\hat{L}^2$ and $\hat{L}_z$ act on functions of $(\theta, \phi)$ on the sphere, their simultaneous eigenfunctions are the *spherical harmonics* $Y_{\ell m}(\theta, \phi)$:

$$\hat{L}^2 Y_{\ell m} = \hbar^2 \ell(\ell+1) Y_{\ell m}, \quad \hat{L}_z Y_{\ell m} = m\hbar Y_{\ell m}.$$

In spherical coordinates, $\hat{L}_z = -i\hbar \frac{\partial}{\partial \phi}$, so the $\phi$-dependence of $Y_{\ell m}$ is $e^{im\phi}$. The full form involves the associated Legendre polynomials $P_\ell^{|m|}(\cos\theta)$:

$$Y_{\ell m}(\theta, \phi) = \mathcal{N}_{\ell m} \cdot P_\ell^{|m|}(\cos\theta) \cdot e^{im\phi}$$

with $\mathcal{N}_{\ell m}$ a normalization constant fixed by the orthonormality condition $\int Y_{\ell' m'}^* Y_{\ell m} \, d\Omega = \delta_{\ell\ell'}\delta_{mm'}$.

The first few:

$$Y_{0,0} = \frac{1}{\sqrt{4\pi}}, \qquad Y_{1,0} = \sqrt{\frac{3}{4\pi}}\cos\theta, \qquad Y_{1,\pm 1} = \mp \sqrt{\frac{3}{8\pi}}\sin\theta \, e^{\pm i\phi}.$$

**Why integer $\ell$ only.** The $\phi$-dependence is $e^{im\phi}$. For the wave function to be single-valued — that is, for $\psi(\phi) = \psi(\phi + 2\pi)$ — we need $e^{im\cdot 2\pi} = 1$, which means $m$ is an integer. Since the ladder of $m$-values spans $-\ell$ to $+\ell$ in integer steps, $\ell$ itself must be a non-negative integer. Half-integer orbital angular momentum is *not allowed* — single-valuedness on the sphere kills it.

This is the punchline that distinguishes orbital from spin. The algebra allows half-integer values; the spatial-wave-function constraint disallows them. Spin lives on a different Hilbert space — a two-dimensional complex spinor space, not a function space on the sphere — and has no analogous constraint. That is why spin-1/2 exists and "orbital 1/2" does not.

**The chemists' $p$ orbitals are not $L_z$ eigenstates.** A point worth pausing on, because it confuses students. The familiar $p_x, p_y, p_z$ orbitals from chemistry are *real-valued* combinations:

$$p_z = Y_{1,0}, \quad p_x = \frac{1}{\sqrt{2}}(Y_{1,-1} - Y_{1,1}), \quad p_y = \frac{i}{\sqrt{2}}(Y_{1,-1} + Y_{1,1}).$$

Only $p_z$ is an eigenstate of $\hat{L}_z$ (with eigenvalue 0). The real combinations $p_x$ and $p_y$ are eigenstates of $\hat{L}^2$ but *not* of $\hat{L}_z$ — they are equal-magnitude superpositions of $m = +1$ and $m = -1$. The complex $Y_{1,\pm 1}$ have $|\psi|^2$ that is azimuthally symmetric (a torus around the $z$-axis); the real $p_x, p_y$ have $|\psi|^2$ that is dumbbell-shaped along the $x$ or $y$ axis. Same Hilbert space, different basis. Chemists choose the real basis because they want to draw real-valued surfaces. Physicists working in a magnetic field choose the complex basis because $\hat{L}_z$ matters there.

### 4.4 Spin-1/2 and the Pauli matrices

Spin operators satisfy the *same* algebra as orbital angular momentum:

$$[\hat{S}_x, \hat{S}_y] = i\hbar \hat{S}_z, \quad \text{cyclic.}$$

So the eigenvalue derivation of §4.2 applies. The novelty: spin lives on a *two-dimensional* Hilbert space for a spin-1/2 particle. The spin operators are $2\times 2$ matrices.

Conventionally write $\hat{S}_i = (\hbar/2) \hat{\sigma}_i$ where the $\hat{\sigma}_i$ are the **Pauli matrices**:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

(Introduced in [Pauli 1927, "Zur Quantenmechanik des magnetischen Elektrons," *Zeitschrift für Physik* 43, 601–623](https://doi.org/10.1007/BF01397326) [verify pages].)

**Four properties to commit to memory.**

1. $\sigma_i^2 = I$ for each $i$. (Square them out: $\sigma_x^2 = \begin{pmatrix} 0&1\\1&0 \end{pmatrix}\begin{pmatrix} 0&1\\1&0 \end{pmatrix} = \begin{pmatrix} 1&0\\0&1 \end{pmatrix}$.)
2. $\mathrm{Tr}(\sigma_i) = 0$.
3. Anticommutation: $\{\sigma_i, \sigma_j\} \equiv \sigma_i \sigma_j + \sigma_j \sigma_i = 2\delta_{ij} I$.
4. Commutation: $[\sigma_i, \sigma_j] = 2i \epsilon_{ijk}\sigma_k$.

Properties 3 and 4 together can be combined: $\sigma_i \sigma_j = \delta_{ij} I + i\epsilon_{ijk}\sigma_k$. The Pauli matrices are not magic — they are the simplest non-trivial matrices satisfying the angular-momentum algebra in two dimensions. They are the generators of $\mathrm{SU}(2)$, the group of $2\times 2$ unitary matrices with unit determinant.

**Eigenstates.** In the $\hat{S}_z$ basis,

$$|\uparrow\rangle = |+z\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = |-z\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix},$$

with $\hat{S}_z |\uparrow\rangle = +(\hbar/2)|\uparrow\rangle$ and $\hat{S}_z |\downarrow\rangle = -(\hbar/2)|\downarrow\rangle$. The eigenstates of $\hat{S}_x$ and $\hat{S}_y$ are linear combinations:

$$|+x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + |\downarrow\rangle), \quad |-x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - |\downarrow\rangle),$$
$$|+y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + i|\downarrow\rangle), \quad |-y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - i|\downarrow\rangle).$$

(You can check: $\hat{S}_x |+x\rangle = (\hbar/2)|+x\rangle$ by direct matrix multiplication. We'll do one in §5.)

**Operational meaning.** These are the states selected by a Stern–Gerlach apparatus oriented along each axis. A spin prepared in $|+z\rangle$ and passed through an $x$-oriented Stern–Gerlach gives outputs $\pm \hbar/2$ each with probability $1/2$ — because $|+z\rangle$ is a uniform superposition of $|+x\rangle$ and $|-x\rangle$. Knowing $S_z$ exactly tells you nothing about $S_x$.

### 4.5 The $720^\circ$ rotation — spinors are not vectors

Here is the deepest difference between spin and orbital angular momentum. A vector in three-dimensional space — say, the electric field — returns to itself after a $360^\circ$ rotation. A spin-1/2 state does not. Under a rotation by angle $\theta$ around an axis $\hat{n}$, a spin-1/2 wave function picks up the operator

$$\hat{U}(\theta, \hat{n}) = \exp\left(-i\frac{\theta}{2}\hat{n}\cdot\vec{\sigma}\right).$$

The factor of $\theta/2$ — not $\theta$ — is the spinor signature. Set $\theta = 2\pi$:

$$\hat{U}(2\pi) = \exp(-i\pi \hat{n}\cdot\vec{\sigma}) = -I.$$

(The last step uses $(\hat{n}\cdot\vec{\sigma})^2 = I$ and the series expansion of $\cos\pi + i\sin\pi \cdot (\hat{n}\cdot\vec{\sigma}) = -1$.) A $360^\circ$ rotation sends $|\psi\rangle$ to $-|\psi\rangle$. A full $720^\circ$ rotation is needed to return to the original state.

This is not a mathematical curiosity. It has been measured. Werner et al. (1975) and Rauch et al. (1975) used neutron interferometry to split a beam of neutrons, rotate one path by $2\pi$ in a magnetic field, and recombine. The interference pattern shifted by $\pi$ — confirming directly that the rotated path picked up a minus sign. ([Werner et al. 1975, *Physical Review Letters* 35, 1053–1055](https://doi.org/10.1103/PhysRevLett.35.1053); [Rauch et al. 1975, *Physics Letters A* 54, 425–427](https://doi.org/10.1016/0375-9601(75)90798-7) [verify volumes].)

The point: a spin-1/2 state is a *spinor*, not a vector. It lives in a two-component complex space that transforms under $\mathrm{SU}(2)$ rather than the rotation group $\mathrm{SO}(3)$. The two groups are not the same — $\mathrm{SU}(2)$ is a double cover of $\mathrm{SO}(3)$, meaning two distinct $\mathrm{SU}(2)$ elements ($+I$ and $-I$) map to the same $\mathrm{SO}(3)$ rotation. The factor-of-two is exactly the $720^\circ$ versus $360^\circ$ behavior.

This is the experimental death of the classical-rotation picture for spin. A classical rotating object returns to itself after $360^\circ$. Spin-1/2 doesn't. End of debate.

### 4.6 Addition of angular momenta

Suppose we have two angular-momentum systems — call their operators $\hat{J}_1$ and $\hat{J}_2$, on Hilbert spaces of dimension $(2j_1+1)$ and $(2j_2+1)$ respectively. Examples: two spin-1/2 particles ($j_1 = j_2 = 1/2$); orbital $\hat{L}$ plus spin $\hat{S}$ in a single atom ($j_1 = \ell$, $j_2 = 1/2$).

Define the *total* angular momentum $\hat{J} = \hat{J}_1 + \hat{J}_2$. Question: what are the eigenvalues of $\hat{J}^2$ in the combined system?

Answer (Clebsch–Gordan): the total $j$ takes integer steps in the range

$$j \in \{|j_1 - j_2|,\, |j_1 - j_2| + 1,\, \ldots,\, j_1 + j_2\},$$

each appearing exactly once. For each total $j$, the magnetic quantum number $m$ ranges from $-j$ to $+j$ in integer steps. The total Hilbert space dimension is

$$(2j_1 + 1)(2j_2 + 1) = \sum_{j} (2j + 1).$$

The matrix elements that change basis from the product representation $|j_1 m_1\rangle |j_2 m_2\rangle$ to the total-angular-momentum representation $|j, m\rangle$ are the *Clebsch–Gordan coefficients* $\langle j_1 m_1; j_2 m_2 | j m\rangle$. Tabulated in any quantum-mechanics text (Griffiths §4.4.3 gives them for the cases we will use; [the Particle Data Group's review article on Clebsch–Gordan coefficients](https://pdg.lbl.gov/) [verify URL] has the standard tables).

We are going to do exactly one case: two spin-1/2 particles. That gives us the singlet — the bridge to Bell's theorem.

---

## 5. Worked example: the singlet state from ladder operators

This is the chapter's second deep-dive and the bridge forward. Two spin-1/2 particles. $j_1 = j_2 = 1/2$. Total dimension: $2\times 2 = 4$. Allowed total $j$: $|1/2 - 1/2| = 0$ up to $1/2 + 1/2 = 1$, so $j \in \{0, 1\}$. The total dimension splits as $4 = 1 + 3$ — one state with $j=0$ (the *singlet*) and three states with $j=1$ (the *triplet*).

We will construct the four states explicitly using ladder operators on the total angular momentum.

**Start at the top of the triplet.** The state with the largest possible $m$ value is $m_1 = m_2 = +1/2$, i.e., $|\uparrow\uparrow\rangle$. Its total $\hat{S}_z$ eigenvalue is $+\hbar$. This must be $|1, +1\rangle$:

$$|1, +1\rangle = |\uparrow\uparrow\rangle.$$

**Step down with the total lowering operator.** Define $\hat{S}_- = \hat{S}_{1-} + \hat{S}_{2-}$, where $\hat{S}_{i-}$ lowers the $i$-th spin's $S_z$. For a single spin-1/2, $\hat{S}_- |\uparrow\rangle = \hbar|\downarrow\rangle$ and $\hat{S}_- |\downarrow\rangle = 0$. (We are using a normalization in which $\hat{S}_\pm |s, m\rangle = \hbar\sqrt{s(s+1) - m(m\pm 1)} |s, m\pm 1\rangle$; for $s = 1/2$, $m = \pm 1/2$, the coefficient is $\hbar\sqrt{1/2 \cdot 3/2 - (\pm 1/2)(\pm 1/2 \pm 1)} = \hbar$.)

Apply $\hat{S}_-$ to $|1, +1\rangle = |\uparrow\uparrow\rangle$:

$$\hat{S}_- |\uparrow\uparrow\rangle = (\hat{S}_{1-} + \hat{S}_{2-})|\uparrow\uparrow\rangle = \hbar|\downarrow\uparrow\rangle + \hbar|\uparrow\downarrow\rangle.$$

The general formula for $|j, m\rangle$ also tells us $\hat{S}_- |1, +1\rangle = \hbar\sqrt{1\cdot 2 - 1 \cdot 0}\,|1, 0\rangle = \hbar\sqrt{2}\,|1, 0\rangle$. Setting the two expressions equal:

$$\hbar\sqrt{2}\,|1, 0\rangle = \hbar(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle) \implies |1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle).$$

Step down once more, from $|1, 0\rangle$ to $|1, -1\rangle$. (Exercise: verify $\hat{S}_-|1, 0\rangle = \hbar\sqrt{2}\,|1, -1\rangle$ matches.) The result is:

$$|1, -1\rangle = |\downarrow\downarrow\rangle.$$

That gives us the triplet.

$$\boxed{|1, +1\rangle = |\uparrow\uparrow\rangle, \qquad |1, 0\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle), \qquad |1, -1\rangle = |\downarrow\downarrow\rangle.}$$

**Now build the singlet.** It has $j = 0$, so $m = 0$ is its only value. It lives somewhere in the four-dimensional product space. By orthogonality, it must be orthogonal to $|1, 0\rangle$ within the $m = 0$ subspace. The $m = 0$ subspace is spanned by $\{|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle\}$; one combination is $|1, 0\rangle = (|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)/\sqrt{2}$; the orthogonal combination is

$$\boxed{|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle).}$$

That is the singlet. Quick check: apply $\hat{S}^2$ to it. The total $\hat{S}^2 = \hat{S}_1^2 + \hat{S}_2^2 + 2\hat{S}_1 \cdot \hat{S}_2$, and one shows after a few lines of algebra that $\hat{S}^2 |0,0\rangle = 0$ — confirming $j = 0$. Also, $\hat{S}_z |0,0\rangle = 0$ trivially (the two terms cancel). Good.

**The singlet's defining properties.**

1. It is *antisymmetric* under particle exchange: swapping particles 1 and 2 sends $|0,0\rangle$ to $-|0,0\rangle$. The triplet states are *symmetric*. (This is the genesis of the spin-statistics connection that will be Unit 8's business.)
2. It is *rotationally invariant*. Apply the same rotation to both spins, and $|0,0\rangle$ comes back to $|0,0\rangle$ unchanged (up to overall phase). The triplet does not have this property — its three states rotate among themselves.
3. It is *maximally entangled*. You cannot write $|0,0\rangle$ as a product $|\alpha\rangle_1 |\beta\rangle_2$ for any choice of single-spin states $|\alpha\rangle, |\beta\rangle$. The two particles do not have definite individual spin states.

**Why the singlet is the pivot.** Property 3 is the one that drives the rest of the quantum-mechanics curriculum. In the singlet, measure $S_z$ on particle 1 and get $+\hbar/2$: particle 2 is then in state $|\downarrow\rangle$ with certainty. Measure $S_z$ on particle 1 and get $-\hbar/2$: particle 2 is in $|\uparrow\rangle$. The two outcomes are perfectly anti-correlated. So far this looks unremarkable — classical correlated particles can do the same.

The strange part is property 2. Suppose instead of measuring $S_z$ on both particles, both observers measure $S_x$. The singlet is rotationally invariant — it has the same form in any basis. Compute: $|0,0\rangle = (1/\sqrt{2})(|+x\rangle_1|-x\rangle_2 - |-x\rangle_1|+x\rangle_2)$. The anti-correlation persists, exactly. It also persists if both observers measure along any other common axis $\hat{n}$.

The persistence is the puzzle Einstein, Podolsky, and Rosen named in 1935. ([Einstein, Podolsky, Rosen 1935, *Physical Review* 47, 777–780](https://doi.org/10.1103/PhysRev.47.777).) Their position-momentum formulation was unwieldy; David Bohm in 1951 ([Bohm, *Quantum Theory*, Prentice-Hall §22](https://archive.org/details/quantumtheory0000bohm) [verify]) recast it in the spin singlet, which is cleaner. The classical question — does each particle "carry" a definite hidden value for $S_z$, $S_x$, $S_y$, etc., that the measurement merely reveals? — turns out to be experimentally answerable. John Bell answered it in 1964 with the inequality that bears his name. ([Bell 1964, "On the Einstein Podolsky Rosen Paradox," *Physics* 1, 195–200](https://cds.cern.ch/record/111654/files/vol1p195-200_001.pdf) [verify URL]. *Physics* is the correct journal title; it was a short-lived publication, not *Physical Review*.)

Bell's theorem is Unit 10's business. What this chapter has done is built the state on which the entire argument rests. Now you know what $|0,0\rangle$ is, where it came from, and why it cannot be reduced to a product of single-particle states. That is the singlet.

---

## 6. Reading map

| Source | Where |
|---|---|
| Orbital angular momentum commutators, ladder operators | Griffiths §4.3.1 |
| Eigenvalue spectrum of $\hat{L}^2$ and $\hat{L}_z$ from ladder algebra | Griffiths §4.3.1; companion §4.2 (slowed down) |
| Spherical harmonics, explicit forms | Griffiths §4.1.2, Tables 4.2–4.3 |
| Pauli matrices, spin operators | Griffiths §4.4.1 |
| Addition of two spin-1/2; Clebsch–Gordan | Griffiths §4.4.3 |
| General $\hat{J}$-framework (orbital + spin uniformly) | [Sakurai & Napolitano, Ch. 3](https://www.cambridge.org/highereducation/books/modern-quantum-mechanics/05A2BF93C73B5BB91EC0E63D45D4DD78) [verify edition] |
| Stern–Gerlach pedagogy as the central thread | [Feynman, Leighton, Sands, *Lectures on Physics* Vol. III, Ch. 5–6](https://www.feynmanlectures.caltech.edu/III_toc.html) |
| Neutron interferometry and the $2\pi$ sign flip | [Werner et al. 1975, *PRL* 35, 1053](https://doi.org/10.1103/PhysRevLett.35.1053); [Rauch et al. 1975, *Phys. Lett. A* 54, 425](https://doi.org/10.1016/0375-9601(75)90798-7) [verify] |
| Original Pauli-matrix paper | [Pauli 1927, *Z. Physik* 43, 601](https://doi.org/10.1007/BF01397326) [verify] |
| EPR original / Bohm reformulation / Bell | EPR [1935 *Phys. Rev.* 47, 777](https://doi.org/10.1103/PhysRev.47.777); Bohm 1951 §22; [Bell 1964 *Physics* 1, 195](https://cds.cern.ch/record/111654/files/vol1p195-200_001.pdf) [verify] |

---

## 7. Exercises

**Exercise 7.1 — Verify the commutator** [Bloom: Apply]
Compute $[\hat{L}_y, \hat{L}_z]$ explicitly from $\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z$ and $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$, using only $[\hat{x}_i, \hat{p}_j] = i\hbar \delta_{ij}$. Show that the result equals $i\hbar \hat{L}_x$. Run every step.

**Exercise 7.2 — $S_x$ measurement on a $S_z$ eigenstate** [Bloom: Apply / Analyze]
A spin-1/2 particle is prepared in $|+z\rangle = |\uparrow\rangle$. It is passed through a Stern–Gerlach magnet oriented along $\hat{x}$. (a) Compute the probabilities of the two possible outcomes $+\hbar/2$ and $-\hbar/2$. (b) After the $\hat{x}$ measurement, the $|+x\rangle$ output is selected and passed through a third Stern–Gerlach magnet oriented along $\hat{z}$. Compute the probabilities of $\pm \hbar/2$ outcomes. (c) What does this sequence demonstrate about $[\hat{S}_x, \hat{S}_z]$?

**Exercise 7.3 — Pauli matrix identities** [Bloom: Apply]
Using $\sigma_i \sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$, prove the identity $(\vec{a}\cdot\vec{\sigma})(\vec{b}\cdot\vec{\sigma}) = (\vec{a}\cdot\vec{b})I + i(\vec{a}\times\vec{b})\cdot\vec{\sigma}$ for arbitrary three-vectors $\vec{a}, \vec{b}$. Use this to compute $(\hat{n}\cdot\vec{\sigma})^2$ and verify the rotation-operator calculation $\exp(-i\theta\,\hat{n}\cdot\vec{\sigma}/2) = \cos(\theta/2) I - i\sin(\theta/2) \hat{n}\cdot\vec{\sigma}$.

**Exercise 7.4 — Singlet rotational invariance** [Bloom: Evaluate]
Show that the singlet state $|0,0\rangle = (1/\sqrt{2})(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ has the same form when expressed in the $|+x\rangle, |-x\rangle$ basis: that is, $|0,0\rangle = (1/\sqrt{2})(|+x\rangle_1|-x\rangle_2 - |-x\rangle_1|+x\rangle_2)$ up to overall phase. Use this to argue that an $\hat{x}$-axis $S_x$ measurement on the singlet produces perfectly anti-correlated outcomes — the same as a $\hat{z}$-axis measurement.

**Exercise 7.5 — $p$-orbital basis change** [Bloom: Analyze]
Show that the chemists' $p_x$ orbital, $p_x = (Y_{1,-1} - Y_{1,1})/\sqrt{2}$, is not an eigenstate of $\hat{L}_z$. Compute $\langle p_x | \hat{L}_z | p_x \rangle$ and $\langle p_x | \hat{L}_z^2 | p_x \rangle$. What do these tell you about a measurement of $L_z$ on a $p_x$-state electron?

**Exercise 7.6 — Vector-model failure** [Bloom: Evaluate]
The semi-classical vector model imagines $\vec{L}$ as a vector of magnitude $\sqrt{\ell(\ell+1)}\hbar$ precessing on a cone around the $z$-axis at fixed $L_z = m_\ell \hbar$. For $\ell = 1, m_\ell = 0$: (a) what does the vector model say about $\langle L_x \rangle$ and $\langle L_x^2 \rangle$? (b) Compute $\langle L_x \rangle$ and $\langle L_x^2 \rangle$ in the actual eigenstate $|1, 0\rangle$ using the operator formalism. (c) Where does the vector model give the right number? Where does it give the wrong picture even when the number is right?

---

## 8. What would change my mind

A confirmed measurement of an orbital angular momentum with half-integer $\ell$ would force a serious reconsideration of the single-valuedness argument that excludes it. So far, nothing of the kind has been observed in any system that admits a clean orbital-vs-spin separation; the few claims in the literature about "half-integer orbital states" turn out, on inspection, to be about effective composite excitations rather than fundamental orbital angular momentum. A clean violation would shake the structure of §4.3 directly. On the spin side, a definitive failure of the $720^\circ$ result — a neutron interferometry experiment that shows spin-1/2 wave functions returning to themselves after $360^\circ$ — would falsify the spinor picture and require something genuinely new. Werner et al. and Rauch et al. found the predicted $2\pi$ sign-flip in 1975 and the result has held since. I would update sharply on a clean reproduction failing.

## 9. Still puzzling

The most honest gap I have is conceptual. The ladder-operator derivation gives the eigenvalue spectrum from the algebra alone — beautiful and exact. But the algebra itself, $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$, ultimately traces back to the canonical commutator $[\hat{x}, \hat{p}] = i\hbar$, which is asserted, not derived. There are paths to motivate it (Fourier analysis, the de Broglie relation, the unitarity of time evolution), but none feels to me like an *explanation* — they feel like consistency checks. Why does the world have non-commuting observables at all? Why $i\hbar$ and not some other algebraic structure? I do not have a satisfying answer. The undergraduate course teaches you to use the algebra fluently; the deeper question of where it comes from is still open enough that I find it worth flagging rather than papering over.

---

**Tags:** angular-momentum, ladder-operators, pauli-matrices, spin-half, spherical-harmonics, singlet-state, clebsch-gordan, entanglement-preview
