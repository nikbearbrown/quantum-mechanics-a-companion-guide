# Chapter 7 — Angular Momentum

## TL;DR

- We start from a single fact about angular momentum and build outward from it.
- We move through the commutation relations, the ladder operators and the spectrum, the spherical harmonics and why half-integers fail for orbital angular momentum, and spin-1/2 with the Pauli matrices.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*One Commutation Relation. One Derivation. Every Eigenvalue You'll Ever Need.*

---

It is fair to be uneasy about the letter $\ell$. It appears in three places at once. It is the eigenvalue of $\hat{L}^2$ — though with a puzzling $(\ell+1)$ factor attached. It is the label on the state. And it sets the range of $m_\ell$ from $-\ell$ to $+\ell$. When the same symbol does three different jobs, it is reasonable to ask where any of it comes from.

That unease is well placed. Many introductory treatments present $\hat{L}^2 \psi = \hbar^2\ell(\ell+1)\psi$ as though it arrived fully formed, with no derivation behind it. The $(\ell+1)$ can look like an arbitrary correction that happens to fit, and the condition $|m_\ell| \leq \ell$ can look like a second unexplained coincidence. Presented this way, the whole structure seems to float free of any reasoning, and students end up memorizing it as a table.

We do not have to settle for that. The entire spectrum follows from one fact and two requirements. The fact is that the components of angular momentum do not commute: $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$. The requirements are that physical operators have real expectation values, and that the spectrum of $\hat{L}_z$ stays bounded in any finite-norm state. Feed those constraints through the algebra of two auxiliary operators, and every eigenvalue emerges. No spatial integration, no differential equations — just algebra.

Once we have that, spin becomes simply a matter of which representation of the same algebra we are using. The $(\ell+1)$ factor will stop looking arbitrary. It will look like the only thing it could possibly be.

---

## The commutation relations

Classical angular momentum is $\vec{L} = \vec{r} \times \vec{p}$. In components:

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x.$$

Now we promote each variable to an operator. The canonical commutator $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$ — together with $[\hat{x}_i, \hat{x}_j] = [\hat{p}_i, \hat{p}_j] = 0$ — gives the angular momentum components non-trivial commutators among themselves.

Let us compute $[\hat{L}_x, \hat{L}_y]$ in full, because it is the cornerstone of everything that follows and it rewards being worked out by hand:

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y,\; \hat{z}\hat{p}_x - \hat{x}\hat{p}_z].$$

Expand using bilinearity. Most of the four terms drop out, since the only non-commuting pairs are $[\hat{x}_i, \hat{p}_i] = i\hbar$. Here is what survives:

- $[\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] = \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x = \hat{y}(-i\hbar)\hat{p}_x = -i\hbar\,\hat{y}\hat{p}_x.$
- $[\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] = 0$ (no shared index).
- $[\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] = 0$ (likewise).
- $[\hat{z}\hat{p}_y, \hat{x}\hat{p}_z] = [\hat{z}, \hat{p}_z]\hat{p}_y\hat{x} = (i\hbar)\hat{p}_y\hat{x} = i\hbar\,\hat{x}\hat{p}_y.$

Adding them up:

$$[\hat{L}_x, \hat{L}_y] = -i\hbar\,\hat{y}\hat{p}_x + i\hbar\,\hat{x}\hat{p}_y = i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\hat{L}_z.$$

Repeating the same calculation cyclically gives $[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$ and $[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$. Together, these three relations are the *defining relations* of an angular-momentum algebra. Any three operators that obey this Lie-bracket structure earn the name angular momentum components — whether they came from $\vec{r}\times\vec{p}$ or from somewhere else entirely. That "somewhere else" turns out to be spin.

One consequence follows right away. The operator $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$ commutes with every component. Here is the proof for $\hat{L}_z$:

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z] + [\hat{L}_z^2, \hat{L}_z].$$

The last term vanishes. For the first, $[\hat{L}_x^2, \hat{L}_z] = \hat{L}_x[\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x = -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x)$. For the second, $[\hat{L}_y^2, \hat{L}_z] = +i\hbar(\hat{L}_y\hat{L}_x + \hat{L}_x\hat{L}_y)$. The two cancel exactly. So $[\hat{L}^2, \hat{L}_z] = 0$, which means $\hat{L}^2$ and $\hat{L}_z$ can be simultaneously diagonalized.

We label their common eigenstates $|\ell, m\rangle$, with

$$\hat{L}^2 |\ell, m\rangle = \lambda |\ell, m\rangle, \quad \hat{L}_z |\ell, m\rangle = m\hbar |\ell, m\rangle.$$

We have not yet shown that $\lambda = \hbar^2\ell(\ell+1)$ or that $m$ is bounded. That comes over the next two pages.

---

## The ladder operators and the spectrum

We define

$$\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y.$$

These operators are not Hermitian — they are each other's adjoints, $\hat{L}_+^\dagger = \hat{L}_-$ — so they are not observables. They are tools. From the commutation relations:

$$[\hat{L}_z, \hat{L}_\pm] = \pm\hbar\hat{L}_\pm, \qquad [\hat{L}^2, \hat{L}_\pm] = 0.$$

The second relation tells us that $\hat{L}_\pm$ leaves the $\hat{L}^2$ eigenvalue unchanged. The first tells us that it shifts the $\hat{L}_z$ eigenvalue. To be precise: if $\hat{L}_z|\ell, m\rangle = m\hbar|\ell, m\rangle$, then

$$\hat{L}_z(\hat{L}_+|\ell, m\rangle) = (\hat{L}_+\hat{L}_z + \hbar\hat{L}_+)|\ell, m\rangle = (m+1)\hbar\cdot\hat{L}_+|\ell, m\rangle.$$

So $\hat{L}_+|\ell, m\rangle$ is an eigenstate of $\hat{L}_z$ with eigenvalue $(m+1)\hbar$. The raising operator climbs the ladder of $m$-values one rung at a time, holding the $\hat{L}^2$ eigenvalue fixed all the while. The lowering operator $\hat{L}_-$ steps down by one rung.

![Ladder diagram showing m-values from −ℓ to +ℓ](../images/07-angular-momentum-fig-01.png)
*Figure 7.1 — Ladder diagram showing m-values from −ℓ to +ℓ*

The ladder cannot continue without end, because expectation values are bounded. The operator $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$ is a sum of squared Hermitian operators, so its expectation value can never be negative in any state:

$$\langle \hat{L}_x^2 + \hat{L}_y^2 \rangle \geq 0.$$

In an eigenstate $|\ell, m\rangle$, this gives $\lambda - m^2\hbar^2 \geq 0$, so $m^2 \leq \lambda/\hbar^2$. The $m$-values are bounded. There has to be a top rung $|\ell, m_{\max}\rangle$ that the raising operator annihilates, and a bottom rung $|\ell, m_{\min}\rangle$ that the lowering operator annihilates.

Now we compute $\lambda$. A useful product identity helps:

$$\hat{L}_-\hat{L}_+ = (\hat{L}_x - i\hat{L}_y)(\hat{L}_x + i\hat{L}_y) = \hat{L}_x^2 + \hat{L}_y^2 + i[\hat{L}_x, \hat{L}_y] = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z.$$

Apply it to the top rung, where $\hat{L}_+|\ell, m_{\max}\rangle = 0$:

$$0 = \hat{L}_-\hat{L}_+|\ell, m_{\max}\rangle = (\hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z)|\ell, m_{\max}\rangle = (\lambda - m_{\max}^2\hbar^2 - m_{\max}\hbar^2)|\ell, m_{\max}\rangle.$$

So

$$\lambda = m_{\max}(m_{\max} + 1)\hbar^2.$$

Define $\ell \equiv m_{\max}$, and there it is:

$$\lambda = \hbar^2\ell(\ell+1).$$

The $(\ell+1)$ is not a correction. It comes straight from the cross-term $i[\hat{L}_x, \hat{L}_y] = -\hbar\hat{L}_z$ that appears when we expand $\hat{L}_-\hat{L}_+$. The non-commutativity of the components shows up, unavoidably, in the eigenvalue. If the components commuted, the eigenvalue would be $\ell^2\hbar^2$ rather than $\ell(\ell+1)\hbar^2$, and the bottom rung would sit at $-\ell$ with no asymmetry. Because they do not commute, the algebra forces both the asymmetry and the factor.

Running the same calculation on the bottom rung — using $\hat{L}_+\hat{L}_- = \hat{L}^2 - \hat{L}_z^2 + \hbar\hat{L}_z$ and $\hat{L}_-|\ell, m_{\min}\rangle = 0$ — gives $\lambda = m_{\min}(m_{\min}-1)\hbar^2$. Combined with $\lambda = \ell(\ell+1)\hbar^2$, the equation $m_{\min}(m_{\min}-1) = \ell(\ell+1)$ has solutions $m_{\min} = -\ell$ and $m_{\min} = \ell+1$. The second contradicts $m_{\min} \leq m_{\max} = \ell$, so we are left with $m_{\min} = -\ell$.

The ladder therefore runs from $m = -\ell$ to $m = +\ell$ in unit steps. This means $2\ell$ must be a non-negative integer, so $\ell \in \{0, \frac{1}{2}, 1, \frac{3}{2}, 2, \ldots\}$. The algebra permits both integers and half-integers. Which values are physically realized depends on the Hilbert space the operators act on.

---

## Spherical harmonics and why half-integers fail for orbital angular momentum

When $\hat{L}^2$ and $\hat{L}_z$ act on functions of $(\theta, \phi)$ on the sphere, their simultaneous eigenfunctions are the spherical harmonics $Y_{\ell m}(\theta, \phi)$. In spherical coordinates $\hat{L}_z = -i\hbar\partial/\partial\phi$, so the $\phi$-dependence of $Y_{\ell m}$ is $e^{im\phi}$.

Here is where a constraint enters. For a wave function to be single-valued — for $\psi(\phi)$ to equal $\psi(\phi + 2\pi)$ — we need $e^{im \cdot 2\pi} = 1$, which forces $m$ to be an integer. Since the ladder of $m$-values runs from $-\ell$ to $+\ell$ in unit steps, $\ell$ must also be a non-negative integer. Single-valuedness on the sphere therefore rules out half-integer orbital angular momentum. The algebra permits $\ell = 1/2$; the geometry of $S^2$ does not.

This is the structural divide between orbital and spin angular momentum. Orbital angular momentum lives on function spaces over the sphere, and there only integer values are allowed. Spin lives on a separate finite-dimensional complex vector space with no spatial interpretation; half-integer values are allowed there because the single-valuedness constraint never enters.

For orientation, here are the first few spherical harmonics:

$$Y_{0,0} = \frac{1}{\sqrt{4\pi}}, \qquad Y_{1,0} = \sqrt{\frac{3}{4\pi}}\cos\theta, \qquad Y_{1,\pm 1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}.$$

![Polar plots of |Y_{ℓm}(θ,φ)|² for ℓ = 0](../images/07-angular-momentum-fig-02.png)
*Figure 7.2 — Polar plots of |Y_{ℓm}(θ,φ)|² for ℓ = 0*

A word about the chemists' $p$ orbitals is worth adding here, because the confusion around them is so common. The familiar $p_x$ and $p_y$ orbitals are real-valued combinations of $Y_{1,\pm 1}$:

$$p_x = \frac{1}{\sqrt{2}}(Y_{1,-1} - Y_{1,1}), \qquad p_y = \frac{i}{\sqrt{2}}(Y_{1,-1} + Y_{1,1}).$$

Only $p_z = Y_{1,0}$ is an eigenstate of $\hat{L}_z$ (with eigenvalue 0). The real combinations $p_x$ and $p_y$ are *not* $\hat{L}_z$ eigenstates — each is an equal-weight superposition of $m = +1$ and $m = -1$. Chemists prefer the real basis because it produces dumbbell-shaped orbitals that draw clearly and point along specific bond axes. Physicists working in magnetic fields prefer the complex $Y_{\ell m}$ basis because $\hat{L}_z$ is what the magnetic field couples to. Both are valid; they are different bases for the same subspace. The lesson is that choosing a basis is not the same as making a physical statement about the state.

---

## Spin-1/2 and the Pauli matrices

Spin operators satisfy the very same algebra:

$$[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z, \quad \text{and cyclically.}$$

The derivation from the previous section carries over word for word. For spin-1/2 in particular, the smallest non-trivial representation of this algebra lives on a two-dimensional complex space, with $s = 1/2$ and $m_s = \pm 1/2$.

We write $\hat{S}_i = (\hbar/2)\sigma_i$. The **Pauli matrices** are:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

Four properties carry all the load:

1. $\sigma_i^2 = I$.
2. $\mathrm{Tr}(\sigma_i) = 0$.
3. Anticommutation: $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$.
4. Commutation: $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$.

Properties 3 and 4 combine into $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$. The Pauli matrices are not magic — they are simply the simplest non-trivial matrices that satisfy the angular-momentum algebra in two dimensions. In the $\hat{S}_z$ basis, the eigenstates are

$$|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix},$$

and the eigenstates of $\hat{S}_x$ and $\hat{S}_y$ are

$$|+x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + |\downarrow\rangle), \quad |-x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - |\downarrow\rangle), \quad |+y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + i|\downarrow\rangle), \quad |-y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - i|\downarrow\rangle).$$

A spin prepared in $|+z\rangle$ and measured along $\hat{x}$ gives $\pm\hbar/2$ each with probability $1/2$, because $|\uparrow\rangle$ is a uniform superposition of $|+x\rangle$ and $|-x\rangle$. Knowing $S_z$ exactly tells us nothing about $S_x$. The Robertson bound from Chapter 5, applied with $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$, says precisely this.

---

## The $720^\circ$ rotation: spinors are not vectors

We now come to the deepest structural fact about spin. A classical vector in three-dimensional space returns to itself after a $360^\circ$ rotation. A spin-1/2 wave function does not.

Under a rotation by angle $\theta$ around axis $\hat{n}$, a spin-1/2 state transforms by

$$\hat{U}(\theta, \hat{n}) = \exp\!\left(-i\frac{\theta}{2}\hat{n}\cdot\vec{\sigma}\right).$$

The crucial feature is the factor of $\theta/2$ — not $\theta$. Set $\theta = 2\pi$. Using $(\hat{n}\cdot\vec{\sigma})^2 = I$ and expanding the exponential:

$$\hat{U}(2\pi) = \cos\pi \cdot I - i\sin\pi\cdot(\hat{n}\cdot\vec{\sigma}) = -I.$$

A $360^\circ$ rotation sends every spin-1/2 state to its negative. The state comes back to itself only after $720^\circ$. This is not a mathematical curiosity.

In 1975, Werner, Colella, Overhauser, and Eagen split a beam of neutrons, rotated one path by $2\pi$ using a magnetic field, and recombined the two paths in an interferometer. The interference pattern shifted by exactly $\pi$ — confirming that the rotated beam had picked up a minus sign relative to the unrotated beam. That same year, Rauch and collaborators confirmed the effect independently. A $360^\circ$ rotation changes the quantum state of a neutron in a physically measurable way. A $720^\circ$ rotation does not.

The language for this is as follows: spin-1/2 lives in a spinor space that transforms under $\mathrm{SU}(2)$, the group of $2\times 2$ unitary matrices with unit determinant. This group is a *double cover* of the ordinary rotation group $\mathrm{SO}(3)$: two distinct $\mathrm{SU}(2)$ elements, $+I$ and $-I$, correspond to the same physical rotation. The factor of two in the exponential is the same factor of two in the $720^\circ$ story, and it has been confirmed in the laboratory.

This rules out any classical-rotation picture for spin. A classical spinning top returns to itself after $360^\circ$; spin-1/2 does not. The behavior is not a quirk of the theory — it is measured.

---

## The singlet: two spins, one state, and the bridge to Bell

Consider two spin-1/2 particles. The total Hilbert space has dimension $2 \times 2 = 4$. The algebra tells us the total angular momentum takes values $j \in \{0, 1\}$, giving $1 + 3 = 4$ states — one singlet and one triplet.

We build them from the ladder operators. Start at the top: the state with both spins up has total $\hat{S}_z$ eigenvalue $+\hbar$, so

$$|1, +1\rangle = |\uparrow\uparrow\rangle.$$

Apply the total lowering operator $\hat{S}_- = \hat{S}_{1-} + \hat{S}_{2-}$. For a single spin-1/2, $\hat{S}_-|\uparrow\rangle = \hbar|\downarrow\rangle$ and $\hat{S}_-|\downarrow\rangle = 0$. So:

$$\hat{S}_-|\uparrow\uparrow\rangle = \hbar|\downarrow\uparrow\rangle + \hbar|\uparrow\downarrow\rangle.$$

The general lowering formula gives $\hat{S}_-|1,+1\rangle = \hbar\sqrt{2}\,|1,0\rangle$. Setting these equal:

$$|1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle).$$

One more step down gives $|1, -1\rangle = |\downarrow\downarrow\rangle$. The triplet is:

$$|1, +1\rangle = |\uparrow\uparrow\rangle, \qquad |1, 0\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle), \qquad |1, -1\rangle = |\downarrow\downarrow\rangle.$$

The singlet has $j = 0$, so $m = 0$. It lives in the $m = 0$ subspace spanned by $\{|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle\}$. By orthogonality to $|1, 0\rangle$, it has to be the other linear combination in that subspace:

$$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle).$$

A quick check confirms it: $\hat{S}_z|0,0\rangle = 0$ (the two terms cancel). For $\hat{S}^2$, use $\hat{S}^2 = \hat{S}_1^2 + \hat{S}_2^2 + 2\hat{S}_1\cdot\hat{S}_2$ and verify $\hat{S}^2|0,0\rangle = 0$ — confirming $j = 0$.

The singlet has three properties worth naming slowly.

**First: antisymmetry.** Swapping particles 1 and 2 sends $|\uparrow\downarrow\rangle \to |\downarrow\uparrow\rangle$ and vice versa, so $|0,0\rangle \to -|0,0\rangle$. The triplet states are symmetric under exchange; the singlet is antisymmetric. This is the seed of the spin-statistics theorem, which we develop in Chapter 8.

**Second: rotational invariance.** Apply the same rotation to both spins, and $|0,0\rangle$ is unchanged, up to overall phase. The singlet is the unique state in the two-particle space that stays invariant under all simultaneous rotations. This follows directly from $j = 0$ — a state of total angular momentum zero looks the same from every direction.

**Third: maximal entanglement.** The singlet cannot be written as a product $|\alpha\rangle_1|\beta\rangle_2$ for any choice of single-spin states. The two particles have no individual spin state; they have only a joint state. Measure $S_z$ on particle 1 and get $+\hbar/2$, and particle 2 is then in $|\downarrow\rangle$ with certainty. Measure $S_z$ on particle 1 and get $-\hbar/2$, and particle 2 is in $|\uparrow\rangle$. Perfect anti-correlation.

So far this could be classical — like a pair of gloves separated into two boxes, each definite but unknown until opened. The non-classical part is the rotational invariance. Because the singlet has the same form in every basis, the same perfect anti-correlation holds for $S_x$, $S_y$, or any axis $\hat{n}$: the two outcomes are always opposite. We can verify this directly: writing $|0,0\rangle$ in the $|+x\rangle, |-x\rangle$ basis gives $(1/\sqrt{2})(|+x\rangle_1|-x\rangle_2 - |-x\rangle_1|+x\rangle_2)$. Perfect anti-correlation along $\hat{x}$, not just $\hat{z}$.

![Two-particle singlet measurement schematic ](../images/07-angular-momentum-fig-03.png)
*Figure 7.3 — Two-particle singlet measurement schematic *

The question Einstein, Podolsky, and Rosen raised in 1935 is this: does each particle "carry" a pre-existing definite value for $S_z$, $S_x$, and every other direction at once — values that the measurement merely reveals? David Bohm recast their argument in terms of the spin singlet in 1951, which made it more tractable. John Bell answered it in 1964 with an inequality: if pre-existing definite values exist, the correlations between measurements on the two particles must obey a certain bound. Quantum mechanics, through the singlet, predicts a violation of that bound. Experiment has confirmed the violation again and again. Chapter 10 carries out the full calculation. What this chapter has done is build the state on which the whole argument rests. We now know where $|0,0\rangle$ came from, what its three properties mean, and why it cannot be reduced to anything simpler.

---

## What the algebra has built

Here is the path the derivation took. From $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ alone — no coordinates, no wave functions — we showed that $\hat{L}^2$ has eigenvalues $\hbar^2\ell(\ell+1)$ and $\hat{L}_z$ has eigenvalues $m\hbar$ running from $-\ell$ to $+\ell$ in unit steps, with $\ell$ an integer or half-integer. The $(\ell+1)$ factor came from the cross-term in $\hat{L}_-\hat{L}_+$; the boundedness of $m$ came from the non-negativity of $\hat{L}_x^2 + \hat{L}_y^2$. Single-valuedness on the sphere removed the half-integers for orbital angular momentum. The Pauli matrices gave the half-integer representation explicitly. And the singlet state followed from the ladder operators applied to two spin-1/2 particles, by orthogonality.

The same algebraic skeleton — commutation relations, ladder operators, bounded spectrum — reappears in the harmonic oscillator (Chapter 4), in the hydrogen atom (Chapter 6), and in quantum field theory, where the same $\hat{a}_\pm$ algebra creates and destroys particles. Learning it once, here, in the setting of angular momentum where the physical meaning is clearest, is an investment that pays off for the rest of the course.

So the three jobs the letter $\ell$ does are not three coincidences. The letter $\ell$ does three jobs because it comes from one piece of algebra — the bounded-spectrum argument applied to the ladder operators — and that one piece of algebra determines the $\hat{L}^2$ eigenvalue, the label on the state, and the range of $m$ all at once. They are one result, seen from three angles.

---

## Exercises

**Warm-up**

**W1.** Compute $[\hat{L}_y, \hat{L}_z]$ explicitly from $\hat{L}_y = \hat{z}\hat{p}_x - \hat{x}\hat{p}_z$ and $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x$, using only $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$. Show that the result equals $i\hbar\hat{L}_x$. Run every step — do not cite the cyclic argument without verifying it. *(The cyclic pattern is correct, but the student who has only been told it exists will miss why it holds for the second commutator as well as the first.)*

**W2.** A spin-1/2 particle is prepared in $|\uparrow\rangle = |+z\rangle$. Compute the probabilities of the two outcomes $\pm\hbar/2$ when $\hat{S}_x$ is measured. Then: after the $|+x\rangle$ output is selected, compute the probabilities when $\hat{S}_z$ is measured again. What has happened to the original $z$-spin information, and why? *(Direct application of Born rule plus collapse; the answer to "what happened" requires naming the non-commutativity of $\hat{S}_x$ and $\hat{S}_z$.)*

**W3.** Verify directly that $p_x = (Y_{1,-1} - Y_{1,1})/\sqrt{2}$ is not an eigenstate of $\hat{L}_z$. Compute $\langle p_x | \hat{L}_z | p_x \rangle$ and $\langle p_x | \hat{L}_z^2 | p_x \rangle$. What do the two numbers tell you about the outcome distribution of a $\hat{L}_z$ measurement on an electron in the $p_x$ orbital? *(Tests whether the student can work with linear combinations of spherical harmonics rather than treating them as isolated states.)*

**Application**

**A1.** Using $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$, prove the identity $(\vec{a}\cdot\vec{\sigma})(\vec{b}\cdot\vec{\sigma}) = (\vec{a}\cdot\vec{b})I + i(\vec{a}\times\vec{b})\cdot\vec{\sigma}$ for arbitrary three-vectors $\vec{a}$, $\vec{b}$. Use this to compute $(\hat{n}\cdot\vec{\sigma})^2$ for a unit vector $\hat{n}$, and from that derive the rotation operator formula $\hat{U}(\theta, \hat{n}) = \cos(\theta/2)I - i\sin(\theta/2)\hat{n}\cdot\vec{\sigma}$. Then verify that $\hat{U}(2\pi, \hat{n}) = -I$ for any $\hat{n}$. *(Chains the Pauli identity through to the $720°$ result; a student who can do this owns the rotation operator.)*

**A2.** Show that the singlet state $|0,0\rangle = (1/\sqrt{2})(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ has the same form when expressed in the $|+x\rangle, |-x\rangle$ basis: $|0,0\rangle = (1/\sqrt{2})(|+x\rangle_1|-x\rangle_2 - |-x\rangle_1|+x\rangle_2)$, up to overall phase. Use this to compute the probability of each outcome pair $(\pm\hbar/2, \pm\hbar/2)$ when both particles are measured along $\hat{x}$. Confirm that the outcomes are perfectly anti-correlated. *(The calculation makes rotational invariance concrete rather than asserted; if the student can repeat it for $\hat{y}$, they are ready for Chapter 10.)*

**Synthesis**

**S1.** The ladder-operator derivation showed that $\ell$ can be an integer or half-integer, and that single-valuedness on the sphere excludes the half-integers for orbital angular momentum. Construct the analogous argument for spin: explain why the single-valuedness constraint does not apply to spin, and identify what Hilbert space spin-1/2 lives on instead of the function space $L^2(S^2)$. Then state clearly why both representations — integer $\ell$ for orbital, half-integer $s$ for spin — satisfy the same commutation relations $[\hat{J}_x, \hat{J}_y] = i\hbar\hat{J}_z$, and why this is sufficient for the eigenvalue spectrum derived in this chapter to apply to both. *(Forces the student to articulate the orbital/spin distinction in terms of representation theory rather than just memorizing that one is integer and the other is not.)*

**S2.** The triplet state $|1,0\rangle = (1/\sqrt{2})(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle)$ and the singlet $|0,0\rangle = (1/\sqrt{2})(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ differ by a single sign. (a) Show that measuring $\hat{S}_z$ on each particle gives the same outcome distribution $\{(+\hbar/2,-\hbar/2), (-\hbar/2,+\hbar/2)\}$ each with probability $1/2$ for both states. (b) Show that measuring $\hat{S}_x$ on each particle gives anti-correlated outcomes for the singlet but correlated outcomes for $|1,0\rangle$. (c) What single experiment distinguishes the singlet from the $m=0$ triplet state? *(The sign difference is physically meaningful and can be detected; part (c) requires the student to identify which measurement axis reveals the distinction and why.)*

**Challenge**

**C1.** The derivation of this chapter showed that the eigenvalue of $\hat{L}^2$ is $\hbar^2\ell(\ell+1)$, not $\hbar^2\ell^2$. The difference comes from the commutator cross-term. Now ask the question in reverse: suppose you were told the eigenvalue is $\hbar^2\ell^2$ (no $(\ell+1)$ factor). What would have to be different about the angular momentum algebra for this to be true — specifically, what would have to be true about $[\hat{L}_x, \hat{L}_y]$? Describe the physical consequences: would the Robertson bound $\sigma_{L_x}\sigma_{L_y} \geq \tfrac{1}{2}|\langle[\hat{L}_x,\hat{L}_y]\rangle|$ still constrain simultaneous measurements, and would there still be a ladder structure? *(A counterfactual that forces the student to understand which feature of the algebra produces each feature of the spectrum, rather than treating the derivation as a black box.)*

---

## References

*Added by fact-check pass 2026-05-14.*

1. Werner, S. A., Colella, R., Overhauser, A. W. & Eagen, C. F. "Observation of the Phase Shift of a Neutron Due to Precession in a Magnetic Field." *Physical Review Letters* 35, 1053 (1975). https://doi.org/10.1103/PhysRevLett.35.1053
2. Rauch, H., Zeilinger, A., Badurek, G., Wilfing, A., Bauspiess, W. & Bonse, U. "Verification of coherent spinor rotation of fermions." *Physics Letters A* 54, 425–427 (1975).
3. Einstein, A., Podolsky, B. & Rosen, N. "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Physical Review* 47, 777–780 (1935). https://doi.org/10.1103/PhysRev.47.777
4. Bohm, D. *Quantum Theory*. Prentice Hall, 1951, Ch. 22.
5. Bell, J. S. "On the Einstein-Podolsky-Rosen paradox." *Physics Physique Fizika* 1, 195–200 (1964).
