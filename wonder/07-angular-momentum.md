# Chapter 7 — Angular Momentum

## TL;DR

- A student asks the right question in office hours — the kind of question that, once you really hear it, you cannot un-hear.
- Watch the argument move: write down the commutation relations, build the ladder operators and shake the whole spectrum out of them, see why half-integers work for spin but not for orbital motion on a sphere, and meet spin-1/2 and the Pauli matrices.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*One Commutation Relation. One Derivation. Every Eigenvalue You'll Ever Need.*

---

A student asks the right question in office hours. She says: the letter $\ell$ keeps showing up in three different places, and it bothers her. It is the eigenvalue of $\hat{L}^2$ — well, with this $(\ell+1)$ factor stuck on that she has never understood. It is the label slapped on the state. And it sets the range of $m_\ell$, from $-\ell$ all the way to $+\ell$. Why is one letter doing three jobs? Where does any of this come from?

She is right to be suspicious. Most introductory books just hand you $\hat{L}^2 \psi = \hbar^2\ell(\ell+1)\psi$ as though it were carried down from a mountaintop on stone tablets. That $(\ell+1)$ looks like an arbitrary fudge — a correction someone bolted on because it happened to fit. The rule that $|m_\ell| \leq \ell$ looks like another coincidence. The whole machine floats in the air, attached to no derivation, and students learn it the way you learn a table of train times — by memorizing it and hoping.

It does not have to be like that. Here is the beautiful part: the entire spectrum follows from one fact and two requirements. The fact is that the components of angular momentum refuse to commute, $[\hat{L}_x, \hat{L}_y] = i\hbar \hat{L}_z$. The two requirements are about as mild as physics requirements get — physical operators have real expectation values, and the spectrum of $\hat{L}_z$ cannot run off to infinity inside a state of finite norm. Run those constraints through the algebra of two cleverly chosen helper operators, and every eigenvalue falls out by itself. No spatial integration. No differential equations. Pure algebra.

Once you have that in hand, spin stops being mysterious — it is just a question of which representation of the same algebra you happen to be standing in. And that $(\ell+1)$ factor will stop looking arbitrary. It will look like the only thing it could possibly have been.

---

## The commutation relations

Classical angular momentum is $\vec{L} = \vec{r} \times \vec{p}$. In components:

$$L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x.$$

Now promote each variable to an operator. The single canonical commutator $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$ — together with $[\hat{x}_i, \hat{x}_j] = [\hat{p}_i, \hat{p}_j] = 0$ — is enough to make the angular momentum components fail to commute among themselves. That failure is the whole story, so let's actually watch it happen.

Let us run $[\hat{L}_x, \hat{L}_y]$ all the way through, because it is the cornerstone and almost no student has ever sat down and done it.

$$[\hat{L}_x, \hat{L}_y] = [\hat{y}\hat{p}_z - \hat{z}\hat{p}_y,\; \hat{z}\hat{p}_x - \hat{x}\hat{p}_z].$$

Expand using bilinearity. Most of the four resulting terms simply die, because the only pairs that fail to commute are $[\hat{x}_i, \hat{p}_i] = i\hbar$. Here is what lives:

- $[\hat{y}\hat{p}_z, \hat{z}\hat{p}_x] = \hat{y}[\hat{p}_z, \hat{z}]\hat{p}_x = \hat{y}(-i\hbar)\hat{p}_x = -i\hbar\,\hat{y}\hat{p}_x.$
- $[\hat{y}\hat{p}_z, \hat{x}\hat{p}_z] = 0$ (no shared index).
- $[\hat{z}\hat{p}_y, \hat{z}\hat{p}_x] = 0$ (likewise).
- $[\hat{z}\hat{p}_y, \hat{x}\hat{p}_z] = [\hat{z}, \hat{p}_z]\hat{p}_y\hat{x} = (i\hbar)\hat{p}_y\hat{x} = i\hbar\,\hat{x}\hat{p}_y.$

Add up the survivors:

$$[\hat{L}_x, \hat{L}_y] = -i\hbar\,\hat{y}\hat{p}_x + i\hbar\,\hat{x}\hat{p}_y = i\hbar(\hat{x}\hat{p}_y - \hat{y}\hat{p}_x) = i\hbar\hat{L}_z.$$

Cycle the labels around and the identical calculation gives $[\hat{L}_y, \hat{L}_z] = i\hbar\hat{L}_x$ and $[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$. Those three relations together are the *defining relations* of an angular-momentum algebra. And here is the liberating thought: any three operators obeying this Lie-bracket structure deserve to be called angular momentum components — whether they were born from $\vec{r}\times\vec{p}$ or from somewhere else entirely. That "somewhere else" is going to turn out to be spin.

One consequence we get for free. The operator $\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2$ commutes with every single component. Watch the proof for $\hat{L}_z$:

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z] + [\hat{L}_z^2, \hat{L}_z].$$

The last term is zero on sight. For the first, $[\hat{L}_x^2, \hat{L}_z] = \hat{L}_x[\hat{L}_x, \hat{L}_z] + [\hat{L}_x, \hat{L}_z]\hat{L}_x = -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x)$. For the second, $[\hat{L}_y^2, \hat{L}_z] = +i\hbar(\hat{L}_y\hat{L}_x + \hat{L}_x\hat{L}_y)$. They cancel, term for term. So $[\hat{L}^2, \hat{L}_z] = 0$, which means $\hat{L}^2$ and $\hat{L}_z$ can be diagonalized at the same time — they share eigenstates.

Tag those shared eigenstates $|\ell, m\rangle$, with

$$\hat{L}^2 |\ell, m\rangle = \lambda |\ell, m\rangle, \quad \hat{L}_z |\ell, m\rangle = m\hbar |\ell, m\rangle.$$

We have *not yet* shown that $\lambda = \hbar^2\ell(\ell+1)$ or that $m$ is bounded. That is the work of the next two pages — and it is where the magic is.

---

## The ladder operators and the spectrum

Define

$$\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y.$$

These are not Hermitian — each is the other's adjoint, $\hat{L}_+^\dagger = \hat{L}_-$ — so they are not observables. Do not look for a meter that measures them. They are tools, nothing more. From the commutation relations:

$$[\hat{L}_z, \hat{L}_\pm] = \pm\hbar\hat{L}_\pm, \qquad [\hat{L}^2, \hat{L}_\pm] = 0.$$

Read what those two say. The second tells you $\hat{L}_\pm$ leaves the $\hat{L}^2$ eigenvalue alone. The first tells you it *shifts* the $\hat{L}_z$ eigenvalue. Concretely: if $\hat{L}_z|\ell, m\rangle = m\hbar|\ell, m\rangle$, then

$$\hat{L}_z(\hat{L}_+|\ell, m\rangle) = (\hat{L}_+\hat{L}_z + \hbar\hat{L}_+)|\ell, m\rangle = (m+1)\hbar\cdot\hat{L}_+|\ell, m\rangle.$$

So $\hat{L}_+|\ell, m\rangle$ is itself an eigenstate of $\hat{L}_z$, now with eigenvalue $(m+1)\hbar$. The raising operator climbs the ladder of $m$-values one rung at a time, holding the $\hat{L}^2$ eigenvalue fixed the whole way up. The lowering operator $\hat{L}_-$ walks back down one rung at a time. That is why they are called ladder operators — they literally are a ladder.

![Ladder diagram showing m-values from −ℓ to +ℓ](../images/07-angular-momentum-fig-01.png)
*Figure 7.1 — Ladder diagram showing m-values from −ℓ to +ℓ*

But a ladder cannot go up forever, and the reason is pure physics: expectation values cannot run off to infinity. Look at the operator $\hat{L}^2 - \hat{L}_z^2 = \hat{L}_x^2 + \hat{L}_y^2$. It is a sum of squares of Hermitian operators, so its expectation value can never be negative, in any state at all:

$$\langle \hat{L}_x^2 + \hat{L}_y^2 \rangle \geq 0.$$

In an eigenstate $|\ell, m\rangle$ this hands you $\lambda - m^2\hbar^2 \geq 0$, so $m^2 \leq \lambda/\hbar^2$. The $m$-values are boxed in. There has to be a top rung $|\ell, m_{\max}\rangle$ that the raising operator kills, and a bottom rung $|\ell, m_{\min}\rangle$ that the lowering operator kills. The ladder is finite. It has ends.

Now let's pin down $\lambda$. There is a handy product identity:

$$\hat{L}_-\hat{L}_+ = (\hat{L}_x - i\hat{L}_y)(\hat{L}_x + i\hat{L}_y) = \hat{L}_x^2 + \hat{L}_y^2 + i[\hat{L}_x, \hat{L}_y] = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z.$$

Apply it to the top rung, where $\hat{L}_+|\ell, m_{\max}\rangle = 0$:

$$0 = \hat{L}_-\hat{L}_+|\ell, m_{\max}\rangle = (\hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z)|\ell, m_{\max}\rangle = (\lambda - m_{\max}^2\hbar^2 - m_{\max}\hbar^2)|\ell, m_{\max}\rangle.$$

So

$$\lambda = m_{\max}(m_{\max} + 1)\hbar^2.$$

Call $\ell \equiv m_{\max}$, and there it is, the thing the student couldn't get past:

$$\lambda = \hbar^2\ell(\ell+1).$$

Look at where the $(\ell+1)$ came from. It is not a correction anyone bolted on. It is the cross-term $i[\hat{L}_x, \hat{L}_y] = -\hbar\hat{L}_z$ that surfaced when we expanded $\hat{L}_-\hat{L}_+$. The non-commutativity of the components leaves its fingerprint, irreducibly, right inside the eigenvalue. If the components *had* commuted, the eigenvalue would have been a tidy $\ell^2\hbar^2$, the bottom rung would sit symmetrically at $-\ell$, and there would be no asymmetry at all. Because they refuse to commute, the algebra forces both the asymmetry and the extra factor. The $(\ell+1)$ was never arbitrary. It was the only thing it could be.

Run the same calculation on the bottom rung — using $\hat{L}_+\hat{L}_- = \hat{L}^2 - \hat{L}_z^2 + \hbar\hat{L}_z$ and $\hat{L}_-|\ell, m_{\min}\rangle = 0$ — and you get $\lambda = m_{\min}(m_{\min}-1)\hbar^2$. Set that equal to $\ell(\ell+1)\hbar^2$, and the equation $m_{\min}(m_{\min}-1) = \ell(\ell+1)$ has two roots, $m_{\min} = -\ell$ and $m_{\min} = \ell+1$. The second contradicts $m_{\min} \leq m_{\max} = \ell$, so it is thrown out. We are left with $m_{\min} = -\ell$.

So the ladder runs from $m = -\ell$ up to $m = +\ell$ in unit steps. That means $2\ell$ has to be a non-negative integer, so $\ell \in \{0, \frac{1}{2}, 1, \frac{3}{2}, 2, \ldots\}$. Notice — the algebra is generous. It permits both integers *and* half-integers. Which ones nature actually uses depends entirely on which Hilbert space the operators are acting on. That is the next question.

---

## Spherical harmonics and why half-integers fail for orbital angular momentum

When $\hat{L}^2$ and $\hat{L}_z$ act on functions of $(\theta, \phi)$ living on the sphere, their shared eigenfunctions are the spherical harmonics $Y_{\ell m}(\theta, \phi)$. In spherical coordinates $\hat{L}_z = -i\hbar\partial/\partial\phi$, so the $\phi$-dependence of $Y_{\ell m}$ is just $e^{im\phi}$.

And here is the constraint that decides everything. For the wave function to be single-valued — for $\psi(\phi)$ to agree with $\psi(\phi + 2\pi)$, since going all the way around brings you back to the same point — we need $e^{im \cdot 2\pi} = 1$. That forces $m$ to be a whole integer. And since the ladder runs from $-\ell$ to $+\ell$ in unit steps, $\ell$ has to be a non-negative integer too. Half-integer orbital angular momentum is simply ruled out by the geometry of the sphere. The algebra was happy to allow $\ell = 1/2$; the shape of $S^2$ says no.

This is the real divide between orbital and spin angular momentum, and it is worth saying plainly. Orbital angular momentum lives on spaces of functions over the sphere — integers only. Spin lives on a separate, finite-dimensional complex vector space that has no spatial interpretation at all — and half-integers are perfectly welcome there, because the single-valuedness argument never even gets a chance to apply.

A few spherical harmonics, just to anchor things:

$$Y_{0,0} = \frac{1}{\sqrt{4\pi}}, \qquad Y_{1,0} = \sqrt{\frac{3}{4\pi}}\cos\theta, \qquad Y_{1,\pm 1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}.$$

![Polar plots of |Y_{ℓm}(θ,φ)|² for ℓ = 0](../images/07-angular-momentum-fig-02.png)
*Figure 7.2 — Polar plots of |Y_{ℓm}(θ,φ)|² for ℓ = 0*

One thing about the chemists' $p$ orbitals, because this confusion trips up nearly everyone. The familiar $p_x$ and $p_y$ orbitals are real-valued combinations of $Y_{1,\pm 1}$:

$$p_x = \frac{1}{\sqrt{2}}(Y_{1,-1} - Y_{1,1}), \qquad p_y = \frac{i}{\sqrt{2}}(Y_{1,-1} + Y_{1,1}).$$

Only $p_z = Y_{1,0}$ is an honest eigenstate of $\hat{L}_z$ (with eigenvalue 0). The real combinations $p_x$ and $p_y$ are *not* $\hat{L}_z$ eigenstates — each is an equal-weight superposition of $m = +1$ and $m = -1$. Chemists reach for the real basis because it gives those clean dumbbell shapes that can be drawn on paper and that point neatly along bond axes. Physicists working in magnetic fields reach for the complex $Y_{\ell m}$ basis, because $\hat{L}_z$ is exactly what the magnetic field couples to. Both bases are valid; they are simply different ways of slicing up the same subspace. And the lesson underneath is worth keeping: which basis you choose is your bookkeeping convenience, not a statement about what the state actually is.

---

## Spin-1/2 and the Pauli matrices

Spin operators obey the very same algebra:

$$[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z, \quad \text{and cyclically.}$$

So the entire derivation from the previous section carries over word for word — we do not have to do any of it again. For spin-1/2 in particular, the smallest non-trivial representation of this algebra lives on a two-dimensional complex space, with $s = 1/2$ and $m_s = \pm 1/2$.

Write $\hat{S}_i = (\hbar/2)\sigma_i$. The **Pauli matrices** are:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

Four properties carry the entire load:

1. $\sigma_i^2 = I$.
2. $\mathrm{Tr}(\sigma_i) = 0$.
3. Anticommutation: $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$.
4. Commutation: $[\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k$.

Properties 3 and 4 fold together into $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$. The Pauli matrices are not magic, despite their reputation — they are nothing more than the simplest non-trivial matrices that satisfy the angular-momentum algebra in two dimensions. In the $\hat{S}_z$ basis the eigenstates are

$$|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix},$$

and the eigenstates of $\hat{S}_x$ and $\hat{S}_y$ are

$$|+x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + |\downarrow\rangle), \quad |-x\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - |\downarrow\rangle), \quad |+y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle + i|\downarrow\rangle), \quad |-y\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\rangle - i|\downarrow\rangle).$$

Prepare a spin in $|+z\rangle$ and measure it along $\hat{x}$, and you get $\pm\hbar/2$, each with probability $1/2$ — because $|\uparrow\rangle$ is a perfectly even mixture of $|+x\rangle$ and $|-x\rangle$. Knowing $S_z$ exactly tells you absolutely nothing about $S_x$. That is not a failure of the apparatus; it is the Robertson bound from Chapter 5 with $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$ saying precisely this.

---

## The $720^\circ$ rotation: spinors are not vectors

Here is the deepest structural fact about spin, and it is genuinely weird, so let's not rush past it. A classical vector in three-dimensional space comes back to itself after a $360^\circ$ rotation. Of course it does — spin it all the way around and it is back where it started. A spin-1/2 wave function does not.

Under a rotation by angle $\theta$ about axis $\hat{n}$, a spin-1/2 state transforms by

$$\hat{U}(\theta, \hat{n}) = \exp\!\left(-i\frac{\theta}{2}\hat{n}\cdot\vec{\sigma}\right).$$

Stare at the exponent. There is a factor of $\theta/2$ in there — not $\theta$. That little $1/2$ is everything. Set $\theta = 2\pi$. Using $(\hat{n}\cdot\vec{\sigma})^2 = I$ and expanding the exponential:

$$\hat{U}(2\pi) = \cos\pi \cdot I - i\sin\pi\cdot(\hat{n}\cdot\vec{\sigma}) = -I.$$

A full $360^\circ$ rotation sends every spin-1/2 state to its own negative. The state only returns to itself after $720^\circ$ — two full turns. Now this is strange. How can turning something all the way around leave it changed? You want to say it must be a bookkeeping artifact, a phase nobody can see. But it is not.

In 1975 Werner, Colella, Overhauser, and Eagen split a beam of neutrons, rotated one path by $2\pi$ with a magnetic field, and recombined the two paths in an interferometer. The interference pattern shifted by exactly $\pi$ — confirming that the rotated beam had picked up a minus sign relative to the beam that stayed put. That same year, Rauch and collaborators confirmed it independently. A $360^\circ$ rotation changes the quantum state of a neutron in a way you can actually measure on a screen. A $720^\circ$ rotation does not. The strange thing is real.

The language for this is: spin-1/2 lives in a spinor space that transforms under $\mathrm{SU}(2)$, the group of $2\times 2$ unitary matrices with determinant one. This group is a *double cover* of the ordinary rotation group $\mathrm{SO}(3)$: two distinct $\mathrm{SU}(2)$ elements, $+I$ and $-I$, correspond to the very same physical rotation. The factor of two in the exponential is the same factor of two in the $720^\circ$ story — and it has been pinned down in the laboratory.

So this rules out, dead, any picture of spin as a classical rotation. A classical spinning top returns to itself after $360^\circ$. Spin-1/2 does not. That behavior is not a quirk of the formalism. It is measured.

---

## The singlet: two spins, one state, and the bridge to Bell

Two spin-1/2 particles. Total Hilbert space dimension: $2 \times 2 = 4$. The algebra tells us the total angular momentum can take values $j \in \{0, 1\}$, which gives $1 + 3 = 4$ states — one singlet and one triplet. Let's build all four with the ladder operators and watch them appear.

Start at the very top. The state with both spins up has total $\hat{S}_z$ eigenvalue $+\hbar$, so

$$|1, +1\rangle = |\uparrow\uparrow\rangle.$$

Apply the total lowering operator $\hat{S}_- = \hat{S}_{1-} + \hat{S}_{2-}$. For one spin-1/2, $\hat{S}_-|\uparrow\rangle = \hbar|\downarrow\rangle$ and $\hat{S}_-|\downarrow\rangle = 0$. So:

$$\hat{S}_-|\uparrow\uparrow\rangle = \hbar|\downarrow\uparrow\rangle + \hbar|\uparrow\downarrow\rangle.$$

The general lowering formula tells us $\hat{S}_-|1,+1\rangle = \hbar\sqrt{2}\,|1,0\rangle$. Set the two equal:

$$|1, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle).$$

One more step down gives $|1, -1\rangle = |\downarrow\downarrow\rangle$. So the triplet is:

$$|1, +1\rangle = |\uparrow\uparrow\rangle, \qquad |1, 0\rangle = \tfrac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle), \qquad |1, -1\rangle = |\downarrow\downarrow\rangle.$$

The singlet has $j = 0$, so $m = 0$. It lives in the $m = 0$ subspace spanned by $\{|\uparrow\downarrow\rangle, |\downarrow\uparrow\rangle\}$. By orthogonality to $|1, 0\rangle$, it has to be the other combination in that subspace:

$$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle).$$

Quick check: $\hat{S}_z|0,0\rangle = 0$ (trivially — the two terms cancel). For $\hat{S}^2$, use $\hat{S}^2 = \hat{S}_1^2 + \hat{S}_2^2 + 2\hat{S}_1\cdot\hat{S}_2$ and verify $\hat{S}^2|0,0\rangle = 0$ — confirming $j = 0$.

Now the singlet has three properties worth naming slowly, one at a time, because each one carries weight.

**First: antisymmetry.** Swap particles 1 and 2, and $|\uparrow\downarrow\rangle \to |\downarrow\uparrow\rangle$ and back, so $|0,0\rangle \to -|0,0\rangle$. The triplet states are symmetric under exchange; the singlet is antisymmetric. This is the seed of the spin-statistics theorem that Chapter 8 grows into a forest.

**Second: rotational invariance.** Rotate both spins the same way, and $|0,0\rangle$ is unchanged, up to overall phase. The singlet is the *only* state in the two-particle space that survives every simultaneous rotation untouched. That is a direct consequence of $j = 0$ — a state of total angular momentum zero looks the same from every direction, because it has no direction.

**Third: maximal entanglement.** You cannot write the singlet as a product $|\alpha\rangle_1|\beta\rangle_2$ for any choice of single-spin states. The two particles do not *have* individual spin states; they have only a joint one. Measure $S_z$ on particle 1 and get $+\hbar/2$: particle 2 is now $|\downarrow\rangle$ with certainty. Get $-\hbar/2$: particle 2 is $|\uparrow\rangle$. Perfect anti-correlation.

So far, you could shrug this off as classical — like a pair of gloves split into two boxes, each one definite but unknown until you peek. The non-classical part is the rotational invariance. Because the singlet wears the same form in every basis, the same perfect anti-correlation holds for $S_x$, for $S_y$, for *any* axis $\hat{n}$ you like: the two outcomes always come out opposite. Check it: write $|0,0\rangle$ in the $|+x\rangle, |-x\rangle$ basis and you get $(1/\sqrt{2})(|+x\rangle_1|-x\rangle_2 - |-x\rangle_1|+x\rangle_2)$. Perfect anti-correlation along $\hat{x}$, not just $\hat{z}$. The gloves would not do that.

![Two-particle singlet measurement schematic ](../images/07-angular-momentum-fig-03.png)
*Figure 7.3 — Two-particle singlet measurement schematic *

And this is exactly the question Einstein, Podolsky, and Rosen raised in 1935: does each particle secretly "carry" a pre-existing definite value for $S_z$, $S_x$, and every other direction all at once — values the measurement merely uncovers? David Bohm recast their argument in terms of the spin singlet in 1951, making it far more tractable. John Bell answered it in 1964 with an inequality: if pre-existing definite values exist, the correlations between measurements on the two particles must obey a certain bound. Quantum mechanics, through this very singlet, predicts a violation of that bound. And experiment has confirmed the violation, over and over. Chapter 10 does the full calculation. What this chapter has done is build the state the whole argument rests on. You now know where $|0,0\rangle$ came from, what its three properties mean, and why it cannot be boiled down to anything simpler.

---

## What the algebra has built

Let's look back at the road we took. From $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ alone — no coordinates, no wave functions, no integrals — we showed that $\hat{L}^2$ has eigenvalues $\hbar^2\ell(\ell+1)$ and $\hat{L}_z$ has eigenvalues $m\hbar$ running from $-\ell$ to $+\ell$ in unit steps, with $\ell$ an integer or half-integer. The $(\ell+1)$ factor came from the cross-term in $\hat{L}_-\hat{L}_+$; the boundedness of $m$ came from the non-negativity of $\hat{L}_x^2 + \hat{L}_y^2$. Single-valuedness on the sphere stripped out the half-integers for orbital angular momentum. The Pauli matrices handed us the half-integer representation explicitly. And the singlet state fell out of the ladder operators applied to two spin-1/2 particles, by orthogonality.

The wonderful thing is that this same algebraic skeleton — commutation relations, ladder operators, a bounded spectrum — shows up again in the harmonic oscillator (Chapter 4), in the hydrogen atom (Chapter 6), and in quantum field theory, where the same $\hat{a}_\pm$ algebra creates and destroys whole particles. Learning it once, here, in the setting of angular momentum where the physical meaning is most transparent, is the investment that keeps paying out for the rest of the course.

And the student who asked the right question in office hours now has her answer. The letter $\ell$ does three jobs because it comes from one piece of algebra — the bounded-spectrum argument applied to the ladder operators — and that one piece simultaneously fixes the $\hat{L}^2$ eigenvalue, the label on the state, and the range of $m$. They were never three coincidences. They are one result, wearing three hats.

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
