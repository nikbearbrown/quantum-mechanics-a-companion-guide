# Unit 9 — Approximation Methods

> Schrödinger never solved helium. Almost no quantum problem of practical interest is exactly solvable. This unit is the toolkit that does the actual work.

---

## 1. What this chapter is doing

Up to this point in the book, every Hamiltonian you have met has had an exact closed-form solution: the free particle, the harmonic oscillator, the infinite well, the hydrogen atom. This is a peculiarity of the curriculum, not of nature. The list of exactly-solvable Hamiltonians is short. Helium — three particles, one Coulomb interaction more than hydrogen — is already not on it. Real atoms, real molecules, real solids, every interacting many-body problem, the vast majority of perturbations to hydrogen-like systems: none of these admit closed-form eigenstates. Quantum mechanics as a working subject is approximation methods.

This unit develops five instruments: time-independent perturbation theory (non-degenerate and degenerate), the variational principle, the WKB approximation, time-dependent perturbation theory, and Fermi's golden rule. Each does a specific job, fails in specific ways, and earns its place in the curriculum because it produces numbers that match experiments. Griffiths covers them in Chapters 6 (perturbation), 7 (variational), 8 (WKB), and 9 (time-dependent perturbation, Fermi's golden rule) — four chapters compressed into one companion unit because the underlying logic is unified. The pop-sci companion contributes nothing to this material; approximation methods are absent from popularizations of QM, which is unfortunate because they are where the subject becomes quantitatively predictive. This unit is companion-original throughout, with the deep-dive on time-dependent perturbation theory leading to Fermi's golden rule because that single formula powers everything in Unit 10.

## 2. Learning objectives

By the end of this unit, you should be able to:

- **State** the first-order energy correction, first-order state correction, second-order energy correction, the variational principle, the WKB tunneling formula, and Fermi's golden rule. (Bloom L1)
- **Compute** the first-order Stark effect on hydrogen $n=2$ using degenerate perturbation theory. (L3)
- **Compute** the variational helium ground-state energy using effective nuclear charge $Z^*$ as the variational parameter. (L3)
- **Derive** Fermi's golden rule from time-dependent perturbation theory, identifying the long-time limit and the $\sin^2$ resonance shape. (L4)
- **Diagnose** which approximation method is appropriate for a given Hamiltonian and justify the choice. (L4)
- **Evaluate** Dyson's argument that QED perturbation theory must be an asymptotic series with zero radius of convergence. (L5)

## 3. The motivating problem

Take the helium Hamiltonian you met in Unit 8:

$$ \hat{H} = -\frac{\hbar^2}{2m}\nabla_1^2 - \frac{\hbar^2}{2m}\nabla_2^2 - \frac{Ze^2}{4\pi\epsilon_0 r_1} - \frac{Ze^2}{4\pi\epsilon_0 r_2} + \frac{e^2}{4\pi\epsilon_0 r_{12}}. $$

Schrödinger published the equation that bears his name in 1926. He solved the hydrogen atom that year. He did not solve helium in any closed form — nobody has. The three-body Coulomb problem in QM has no analytic solution. What Hylleraas published in 1929 ([*Zeitschrift für Physik* 54, 347–366](https://doi.org/10.1007/BF01375457)) was a *variational* calculation: pick a trial wave function with adjustable parameters, compute $\langle\psi|\hat{H}|\psi\rangle$ as a function of the parameters, minimize. With a six-parameter trial function, Hylleraas reproduced the experimental ground-state energy of helium to four significant figures. The number was right. The wave function was *approximate*. This is the working mode of practical quantum mechanics: an approximate wave function that gives the right energy is good enough to build the next decade of physics on.

This unit develops five such methods. The order is roughly: perturb if you have a small parameter; vary if you do not; semi-classical-expand if your potential is slowly varying; time-dependent-perturb if your perturbation has a clock attached. Then add a continuum of final states and you get Fermi's golden rule, which is the formula underneath spontaneous emission, beta decay, scattering cross sections, photoionization, and Raman scattering. The unit ends there because that single formula powers most of Unit 10.

You do not need any new physics to read this unit. You need linear algebra at the level of inner products and matrix diagonalization, calculus through Taylor series, and Unit 5 (formalism — the completeness relation $\sum_n |n\rangle\langle n| = \hat{1}$ is the technical move underneath every derivation).

## 4. Concept blocks

### 4.1 Time-independent perturbation theory (non-degenerate)

The setup. An exactly-solvable Hamiltonian $\hat{H}_0$ with known eigenstates $|n^{(0)}\rangle$ and energies $E_n^{(0)}$:

$$ \hat{H}_0 |n^{(0)}\rangle = E_n^{(0)} |n^{(0)}\rangle. $$

A small correction $\hat{H}'$ such that the full Hamiltonian is $\hat{H} = \hat{H}_0 + \lambda \hat{H}'$. The parameter $\lambda$ is a bookkeeping device — it labels orders of the expansion, and at the end you set $\lambda = 1$. The assumption is that the exact eigenstates $|n\rangle$ and energies $E_n$ can be expanded in powers of $\lambda$:

$$ |n\rangle = |n^{(0)}\rangle + \lambda |n^{(1)}\rangle + \lambda^2 |n^{(2)}\rangle + \cdots, $$

$$ E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots. $$

This assumption is wrong in general (see the misconception below). It is approximately right for the first few orders when $\hat{H}'$ is small in the appropriate operator-norm sense, and that is enough to do useful physics.

Substitute into $\hat{H}|n\rangle = E_n |n\rangle$ and match powers of $\lambda$. The $\lambda^0$ equation is just $\hat{H}_0 |n^{(0)}\rangle = E_n^{(0)} |n^{(0)}\rangle$ — the unperturbed problem. The $\lambda^1$ equation is

$$ \hat{H}_0 |n^{(1)}\rangle + \hat{H}' |n^{(0)}\rangle = E_n^{(0)} |n^{(1)}\rangle + E_n^{(1)} |n^{(0)}\rangle. $$

Project onto $\langle n^{(0)}|$ from the left. The first and third terms cancel (because $\langle n^{(0)}| \hat{H}_0 = E_n^{(0)} \langle n^{(0)}|$), and $\langle n^{(0)} | n^{(0)} \rangle = 1$, leaving the *first-order energy correction*:

$$ \boxed{E_n^{(1)} = \langle n^{(0)} | \hat{H}' | n^{(0)} \rangle.} $$

This is the simplest formula in perturbation theory and the one you will use most often. Sandwich the perturbation between the unperturbed state and read off the energy shift. Why this works: only the diagonal matrix element of $\hat{H}'$ in the unperturbed basis contributes at first order.

For the first-order *state* correction, project the same $\lambda^1$ equation onto $\langle m^{(0)}|$ for $m \neq n$. This time the first and third terms give $E_m^{(0)} \langle m^{(0)} | n^{(1)} \rangle - E_n^{(0)} \langle m^{(0)} | n^{(1)} \rangle = (E_m^{(0)} - E_n^{(0)}) \langle m^{(0)} | n^{(1)} \rangle$, and the second term gives $\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle$, and the fourth term is zero (because $\langle m^{(0)} | n^{(0)} \rangle = 0$ for $m \neq n$). Solving:

$$ \langle m^{(0)} | n^{(1)} \rangle = \frac{\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}}, $$

so the first-order state correction is

$$ \boxed{|n^{(1)}\rangle = \sum_{m \neq n} \frac{\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle.} $$

The state mixes in contributions from every other unperturbed state, weighted by the off-diagonal matrix element of $\hat{H}'$ and divided by the unperturbed energy gap. The smaller the gap, the larger the mixing — and the more suspicious you should be that the expansion is converging.

The *second-order energy correction* comes from matching $\lambda^2$. The derivation parallels the first-order case; the result is

$$ \boxed{E_n^{(2)} = \sum_{m \neq n} \frac{|\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}.} $$

For the ground state ($n=0$), every denominator $E_0^{(0)} - E_m^{(0)}$ is negative; every numerator is non-negative. So $E_0^{(2)} \leq 0$. *The second-order correction to the ground-state energy is always non-positive.* This is *level repulsion*: a perturbation pushes the ground state down and excited states up, more strongly the closer the unperturbed levels. The effect is important in band-structure physics (avoided crossings), nuclear physics (random-matrix models), and quantum chemistry.

**Common misconception.** "Perturbation theory always converges if $\hat{H}'$ is small." No. Even for the harmonic oscillator with a quartic perturbation $\hat{H}' = \lambda \hat{x}^4$, the perturbation series in $\lambda$ has zero radius of convergence ([Bender and Wu 1969, *Physical Review* 184, 1231–1260](https://doi.org/10.1103/PhysRev.184.1231)). The series is *asymptotic*: the first few terms give excellent numerical estimates, the series then diverges if you keep summing. Dyson argued in 1952 ([*Physical Review* 85, 631–632](https://doi.org/10.1103/PhysRev.85.631)) that QED perturbation theory must be asymptotic for a physical reason: the vacuum is unstable against pair creation when you flip the sign of the coupling from $+e$ to $-e$, so the series cannot be analytic at $e = 0$. The lesson: perturbation theory is useful precisely because the first few terms are accurate, not because the series converges.

**Worked example.** First-order Stark effect on the hydrogen *ground* state. The perturbation is $\hat{H}' = e\hat{z} \mathcal{E}$ for an electric field $\mathcal{E}$ in the $z$-direction. The first-order correction is

$$ E_1^{(1)} = \langle 1s | e\hat{z}\mathcal{E} | 1s \rangle = e\mathcal{E} \int |\psi_{1s}|^2 z\, d^3r = 0, $$

because $|\psi_{1s}|^2$ is spherically symmetric and $z$ is an odd function — the integrand is odd, the integral over all space is zero. *The first-order Stark effect on hydrogen $1s$ is zero.* The atom has no permanent electric dipole moment in the ground state. The Stark effect on $1s$ appears at *second* order, scaling as $\mathcal{E}^2$, because the perturbation mixes $|1s\rangle$ with excited states that do carry a non-zero $\langle z \rangle$, and second-order perturbation captures that mixing. The $n=2$ manifold of hydrogen is different — see §4.2.

### 4.2 Degenerate perturbation theory

When two or more unperturbed states share the same energy, the first-order state-correction denominator $E_n^{(0)} - E_m^{(0)} \to 0$ and the non-degenerate formula diverges. The fix: choose the *right* basis within the degenerate subspace before applying the perturbation.

Specifically, restrict $\hat{H}'$ to the degenerate subspace, diagonalize the resulting matrix. The eigenvalues are the first-order energy corrections; the eigenvectors are the "good" zeroth-order states for the perturbation problem. For a two-fold degeneracy with degenerate states $|a^{(0)}\rangle$ and $|b^{(0)}\rangle$, the matrix is

$$ W = \begin{pmatrix} \langle a^{(0)} | \hat{H}' | a^{(0)} \rangle & \langle a^{(0)} | \hat{H}' | b^{(0)} \rangle \\ \langle b^{(0)} | \hat{H}' | a^{(0)} \rangle & \langle b^{(0)} | \hat{H}' | b^{(0)} \rangle \end{pmatrix}. $$

Eigenvalues of $W$ are the first-order corrections to the previously-degenerate energy. The conceptual content: the unperturbed degeneracy did not pick out a preferred basis, so any orthonormal pair $\{|a^{(0)}\rangle, |b^{(0)}\rangle\}$ was as good as any other. The perturbation breaks the tie and tells you which basis was appropriate all along.

**Worked example.** Linear Stark effect on hydrogen $n=2$. The four degenerate states are $|2s\rangle$, $|2p_x\rangle$, $|2p_y\rangle$, $|2p_z\rangle$. The perturbation $\hat{H}' = e\hat{z}\mathcal{E}$ has matrix elements that, by symmetry (parity, and the requirement that the dipole operator $z$ connect states of opposite parity), are non-zero only between $|2s\rangle$ and $|2p_z\rangle$. The two-by-two block in the $\{|2s\rangle, |2p_z\rangle\}$ basis is

$$ W = \begin{pmatrix} 0 & -3e\mathcal{E} a_0 \\ -3e\mathcal{E} a_0 & 0 \end{pmatrix}, $$

where $a_0$ is the Bohr radius and the matrix element $\langle 2s | e\hat{z}\mathcal{E} | 2p_z \rangle = -3e\mathcal{E} a_0$ falls out of the hydrogen radial integrals (Griffiths §6.4 walks the computation explicitly). Eigenvalues $\pm 3e\mathcal{E} a_0$. The $|2p_x\rangle$ and $|2p_y\rangle$ states are unaffected — the perturbation has no matrix elements involving them, so they remain at the unperturbed $n=2$ energy. The $n=2$ manifold of hydrogen splits *linearly* with the electric field, with the two outer states shifted by $\pm 3e\mathcal{E} a_0$ and the two inner states unshifted. This is the linear Stark effect ([Stark 1914, *Annalen der Physik* 43, 965; Nobel 1919][verify]), and it occurs only because of the degeneracy of $|2s\rangle$ and $|2p_z\rangle$ in hydrogen.

### 4.3 The variational principle

The variational principle. For any normalized trial state $|\psi_{\text{trial}}\rangle$,

$$ \boxed{\langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle \geq E_{\text{ground}}.} $$

The proof is two lines. Expand $|\psi_{\text{trial}}\rangle$ in the (unknown) energy eigenbasis: $|\psi_{\text{trial}}\rangle = \sum_n c_n |n\rangle$ with $\sum_n |c_n|^2 = 1$. Then

$$ \langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle = \sum_n |c_n|^2 E_n \geq \sum_n |c_n|^2 E_{\text{ground}} = E_{\text{ground}}, $$

with equality only when $|\psi_{\text{trial}}\rangle = |\text{ground}\rangle$ (all the weight on the ground state).

The strategy: parameterize a trial state with a small number of adjustable parameters, compute $\langle\hat{H}\rangle$ as a function of those parameters, minimize. The minimum is your best upper bound on the ground-state energy *from within the chosen family of trial states*. Three virtues.

*One.* No expansion parameter is required. Perturbation theory needs a small $\hat{H}'$; the variational method does not.

*Two.* The bound is one-sided. You can never *overestimate* the ground-state energy with this method — only fail to find it.

*Three.* The error is *second order* in the deviation of $|\psi_{\text{trial}}\rangle$ from $|\text{ground}\rangle$. If your trial state is close to the ground state, the energy estimate is much closer to the true ground-state energy than the wave-function error would suggest. The method is forgiving.

**Worked example — variational helium.** Trial state: product of two $1s$-like hydrogenic orbitals, with an effective nuclear charge $Z^*$ as a variational parameter rather than the bare $Z = 2$. The idea is that each electron partially screens the nucleus from the other, so the *effective* charge each electron sees is less than $Z$.

$$ \psi_{\text{trial}}(\mathbf{r}_1, \mathbf{r}_2) = \frac{(Z^*)^3}{\pi a_0^3} e^{-Z^*(r_1 + r_2)/a_0}. $$

Compute $\langle \hat{H} \rangle$ in three pieces. In atomic units (where $\hbar = m_e = e^2/4\pi\epsilon_0 = a_0 = 1$, and energies are in Hartrees, 1 Hartree $= 27.2$ eV):

- *Kinetic energy.* Each $1s$-like orbital with effective charge $Z^*$ has kinetic energy $\langle T \rangle = (Z^*)^2 / 2$ per electron; two electrons give $\langle T \rangle_{\text{total}} = (Z^*)^2$.
- *Electron-nucleus attraction.* Each electron in a hydrogenic $1s$ with effective charge $Z^*$ has $\langle 1/r \rangle = Z^*$, so the actual electron-nucleus term (with true charge $Z=2$) is $-Z\langle 1/r \rangle = -Z Z^*$ per electron; total $-2Z Z^*$.
- *Electron-electron repulsion.* For two electrons in $1s$-like orbitals with effective charge $Z^*$, $\langle 1/r_{12} \rangle = (5/8) Z^*$ (Griffiths Ch. 7 has the integral worked out).

Combining,

$$ \langle \hat{H} \rangle(Z^*) = (Z^*)^2 - 2 Z Z^* + \frac{5}{8} Z^*. $$

Differentiate and minimize:

$$ \frac{d\langle\hat{H}\rangle}{dZ^*} = 2 Z^* - 2 Z + \frac{5}{8} = 0 \implies Z^* = Z - \frac{5}{16}. $$

For helium, $Z = 2$, so $Z^* = 27/16 \approx 1.6875$. The variational ground-state energy is

$$ E_{\text{var}} = -(Z^*)^2 = -(27/16)^2 \approx -2.848\ \text{Hartree} \approx -77.5\ \text{eV}. $$

Compare to experimental $-79.0$ eV ([NIST]). The variational result is within 2% of the experimental value and captures the essential physics — each electron sees an effective charge of about 1.69 because the other electron partially screens the nucleus. This is the calculation Hylleraas reported in 1928 with one parameter; his 1929 six-parameter version improved the result to four significant figures.

**Common misconception.** "Variational gives you the ground state." It gives you the *energy*, with an upper bound. The trial state itself is only as good as your ansatz, and the energy converges much faster than the wave function — so variational *energies* are reliable to many digits in modern calculations, while variational *wave functions* (and observables sensitive to them, like charge density at a point) are less reliable. This is why quantum-chemistry papers report energies to five decimal places but treat charge densities with more caution.

### 4.4 The WKB approximation

The WKB ("semi-classical") approximation is the leading term in an expansion of the Schrödinger equation in powers of $\hbar$. Three physicists derived it independently in 1926: Wentzel ([*Zeitschrift für Physik* 38, 518–529](https://doi.org/10.1007/BF01397171)), Kramers ([*Zeitschrift für Physik* 39, 828–840](https://doi.org/10.1007/BF01451751)), and Brillouin ([*Comptes Rendus* 183, 24–26]). Write $\psi(x) = A(x) \exp(i S(x)/\hbar)$ and substitute into the time-independent Schrödinger equation. To leading order in $\hbar$,

$$ \psi(x) \approx \frac{C}{\sqrt{|p(x)|}} \exp\left(\pm \frac{i}{\hbar} \int p(x')\, dx' \right), $$

where $p(x) = \sqrt{2m(E - V(x))}$ is the *local classical momentum* in the classically allowed region ($E > V$), and $p(x) = i|p(x)|$ (purely imaginary) in the classically forbidden region ($E < V$). The wave function has a slowly varying amplitude $1/\sqrt{|p|}$ and a rapidly oscillating phase whose derivative is the classical momentum. The approximation is valid when the de Broglie wavelength $\lambda = h/p$ changes slowly compared to itself — quantitatively, when $|d\lambda/dx| \ll 1$, or equivalently when the potential is approximately constant over one wavelength.

Two applications earn their place.

**Tunneling.** For a barrier from $x = a$ to $x = b$ with $E < V(x)$ in between (the classically forbidden region), the wave function inside the barrier decays exponentially:

$$ \psi(x) \approx \frac{C}{\sqrt{|p(x)|}} \exp\left(-\frac{1}{\hbar} \int_a^x |p(x')|\, dx'\right) = \frac{C}{\sqrt{|p(x)|}} \exp\left(-\frac{1}{\hbar} \int_a^x \sqrt{2m(V(x') - E)}\, dx'\right). $$

The transmission coefficient — probability of tunneling through the barrier — is the squared amplitude ratio between $x = a$ and $x = b$:

$$ \boxed{T \approx \exp\left(-\frac{2}{\hbar} \int_a^b \sqrt{2m(V(x) - E)}\, dx\right).} $$

The integral inside the exponential is the *action across the barrier*. The exponential dependence on action means small changes in barrier shape produce large changes in tunneling probability — alpha-decay half-lives span 24 orders of magnitude (from $\sim 10^{-6}$ s for short-lived nuclei to $\sim 10^{18}$ s for thorium-232) for alpha-particle energies varying by only a factor of two ([Geiger and Nuttall 1911, *Philosophical Magazine* 22, 613]). Gamow's 1928 paper ([*Zeitschrift für Physik* 51, 204–212](https://doi.org/10.1007/BF01343196)) gave the first nuclear-physics derivation of this empirical relation from WKB tunneling through the Coulomb barrier; Gurney and Condon arrived independently at the same conclusion the same year ([*Physical Review* 33, 127–140](https://doi.org/10.1103/PhysRev.33.127)).

**Bohr–Sommerfeld quantization.** For a particle bound between classical turning points $a$ and $b$ at energy $E$, the WKB quantization condition is

$$ \oint p(x)\, dx = 2 \int_a^b p(x)\, dx = (n + \tfrac{1}{2}) \cdot 2\pi\hbar. $$

The $+1/2$ is the *Maslov index*. It arises from the connection formulas at the turning points: at each soft turning point, the WKB wave function must be matched to an Airy function (the exact solution of the Schrödinger equation in a locally linear potential), and the matching gives a phase loss of $\pi/4$. Two turning points, total phase loss $\pi/2 = (1/2) \cdot \pi$, hence the $1/2$ in the quantization rule. Deriving this matching is standard but lengthy — Bender and Orszag's *Advanced Mathematical Methods* Ch. 10 has the cleanest derivation. For our purposes, take it as given.

The WKB+1/2 condition recovers the *exact* harmonic-oscillator spectrum $E_n = (n + 1/2)\hbar\omega$. It recovers the hydrogen levels in their simplest (non-relativistic, spinless) form. It misses fine-structure and finite-size corrections, which require more careful methods.

**Common misconception.** "WKB is valid for high-energy states." More precise: WKB is valid where the potential varies slowly compared to the local wavelength. For high-energy states above smooth potentials, the wavelength is short and the potential varies slowly per wavelength — WKB is excellent. For low-energy states near the bottom of a steep well, the wavelength is long and the potential variation per wavelength is large — WKB fails. For tunneling, WKB works best for wide smooth barriers and degrades for sharp narrow ones (where the connection formulas at the turning points matter relatively more).

**Worked example.** WKB tunneling through a rectangular barrier of height $V_0$ and width $L$ for $E < V_0$. The integral is trivial because $V$ is constant inside:

$$ T_{\text{WKB}} \approx \exp\left(-\frac{2L}{\hbar} \sqrt{2m(V_0 - E)}\right). $$

The exact result from solving the Schrödinger equation in three regions is

$$ T_{\text{exact}} = \frac{1}{1 + \frac{V_0^2}{4 E(V_0 - E)} \sinh^2(\kappa L)}, $$

where $\kappa = \sqrt{2m(V_0 - E)}/\hbar$. For wide barriers ($\kappa L \gg 1$), $\sinh^2(\kappa L) \approx (1/4) e^{2\kappa L}$, and the exact result reduces to

$$ T_{\text{exact}} \approx 16 \frac{E}{V_0}\left(1 - \frac{E}{V_0}\right) e^{-2\kappa L}. $$

The WKB result is the exponential $e^{-2\kappa L}$. The pre-factor (the $16 (E/V_0)(1 - E/V_0)$) is missing from WKB. WKB captures the order of magnitude correctly — typically that is the part you care about, since tunneling probabilities span many orders of magnitude — and misses the multiplicative pre-factor.

### 4.5 Time-dependent perturbation theory and Fermi's golden rule (deep-dive)

Now the perturbation has a clock attached: $\hat{H}'(t)$ depends on time. The setup: an unperturbed Hamiltonian $\hat{H}_0$ with eigenstates $|n\rangle$ and energies $E_n$. At $t = 0$, turn on $\hat{H}'(t)$. The system starts in state $|i\rangle$. What is the probability of finding it in $|f\rangle \neq |i\rangle$ at time $t$?

Expand the time-evolving state in the interaction picture:

$$ |\psi(t)\rangle = \sum_n c_n(t)\, e^{-i E_n t/\hbar}\, |n\rangle, $$

with $c_n(0) = \delta_{ni}$. Substitute into the time-dependent Schrödinger equation $i\hbar \partial_t |\psi\rangle = (\hat{H}_0 + \hat{H}'(t)) |\psi\rangle$. The unperturbed part of the Hamiltonian acts trivially on the basis states; the perturbation gives, after projecting onto $\langle f |$,

$$ i\hbar\, \dot{c}_f(t) = \sum_n \langle f | \hat{H}'(t) | n \rangle\, e^{i\omega_{fn} t}\, c_n(t), $$

where $\omega_{fn} = (E_f - E_n)/\hbar$. So far this is exact (an infinite set of coupled equations for the $c_n$).

*First-order perturbation theory*: replace $c_n(t) \approx \delta_{ni}$ on the right-hand side. Then only the $n = i$ term survives:

$$ i\hbar\, \dot{c}_f^{(1)}(t) = \langle f | \hat{H}'(t) | i \rangle\, e^{i \omega_{fi} t}. $$

Integrate from $0$ to $t$ with $c_f^{(1)}(0) = 0$:

$$ \boxed{c_f^{(1)}(t) = \frac{1}{i\hbar} \int_0^t \langle f | \hat{H}'(t') | i \rangle\, e^{i\omega_{fi} t'}\, dt'.} $$

The squared amplitude $|c_f^{(1)}(t)|^2$ is the *transition probability* from $|i\rangle$ to $|f\rangle$ at time $t$, to first order in $\hat{H}'$.

Now specialize to a *sinusoidal* perturbation: $\hat{H}'(t) = \hat{V} \cdot 2\cos(\omega t) = \hat{V}(e^{i\omega t} + e^{-i\omega t})$ for $t > 0$. The transition amplitude becomes

$$ c_f^{(1)}(t) = \frac{\langle f | \hat{V} | i \rangle}{i\hbar} \int_0^t \left[ e^{i(\omega_{fi} + \omega)t'} + e^{i(\omega_{fi} - \omega)t'} \right] dt'. $$

For $\omega$ near $\omega_{fi}$ (resonant absorption: the perturbation supplies energy $\hbar\omega \approx E_f - E_i$), the second exponential is slowly varying and dominates after integration; the first exponential averages to zero. Keep the resonant term:

$$ c_f^{(1)}(t) \approx \frac{\langle f | \hat{V} | i \rangle}{i\hbar} \cdot \frac{e^{i(\omega_{fi} - \omega)t} - 1}{i(\omega_{fi} - \omega)}. $$

Squaring:

$$ |c_f^{(1)}(t)|^2 = \frac{|\langle f | \hat{V} | i \rangle|^2}{\hbar^2} \cdot \frac{4 \sin^2\left[(\omega_{fi} - \omega) t / 2\right]}{(\omega_{fi} - \omega)^2}. $$

This is the central formula. Let $\Omega = \omega_{fi} - \omega$ be the *detuning* from resonance. The shape of $|c_f^{(1)}(t)|^2$ as a function of $\Omega$ is

$$ |c_f^{(1)}|^2 \propto \frac{\sin^2(\Omega t / 2)}{\Omega^2}. $$

This function has a peak at $\Omega = 0$ (exact resonance) with height $(t/2)^2 \to t^2/4$, and width $\sim 1/t$. As $t \to \infty$, the function becomes infinitely sharp and infinitely tall — it approaches a *delta function in $\Omega$ times $t$*. Mathematically, the identity

$$ \lim_{t \to \infty} \frac{\sin^2(\Omega t/2)}{\Omega^2} = \frac{\pi t}{2} \delta(\Omega) $$

holds in the distributional sense. (Sketch: integrate both sides against a smooth test function; the change of variable $u = \Omega t/2$ gives $\int (\sin^2 u / u^2) \cdot (2/t)\, du = \pi/t \cdot (t/2)$ at $\Omega = 0$, and the result follows. Griffiths §9.2 walks this in more detail.)

Plug in:

$$ |c_f^{(1)}(t)|^2 \to \frac{|\langle f | \hat{V} | i \rangle|^2}{\hbar^2} \cdot \frac{4 \cdot \pi t}{2}\, \delta(\omega_{fi} - \omega) = \frac{2\pi t}{\hbar^2}\, |\langle f | \hat{V} | i \rangle|^2\, \delta(\omega_{fi} - \omega). $$

The transition probability grows *linearly* in $t$ (the standard symptom of a random-walk transition rate), and the *transition rate per unit time* is the coefficient:

$$ W_{i \to f} = \frac{2\pi}{\hbar^2}\, |\langle f | \hat{V} | i \rangle|^2\, \delta(\omega_{fi} - \omega) = \frac{2\pi}{\hbar}\, |\langle f | \hat{V} | i \rangle|^2\, \delta(E_f - E_i - \hbar\omega), $$

using $\delta(\omega) = \hbar\, \delta(\hbar\omega) = \hbar\, \delta(E)$ in the last step.

This is the transition rate to a *single* final state $|f\rangle$ at exactly the resonance energy. In most applications, the final state is part of a *continuum* with density of states $\rho(E_f)$ — the number of available states per unit energy near $E_f$. Sum (integrate) over the continuum:

$$ W_{i \to f} = \int \frac{2\pi}{\hbar}\, |\langle f | \hat{V} | i \rangle|^2\, \delta(E_f - E_i - \hbar\omega)\, \rho(E_f)\, dE_f. $$

The delta function picks out $E_f = E_i + \hbar\omega$, and we get

$$ \boxed{W_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}' | i \rangle|^2\, \rho(E_f).} $$

(In the standard convention, the matrix element here is of the full sinusoidal perturbation $\hat{H}'$ at the resonance frequency, which differs from $\hat{V}$ by a factor of 2 depending on how you define the perturbation amplitude. Griffiths absorbs the factor into $\hat{H}'$; Sakurai keeps it separate. Pick a convention and stick with it.)

This is *Fermi's golden rule*. Dirac derived it first, in his 1927 paper on the emission and absorption of radiation ([Dirac 1927, *Proceedings of the Royal Society A* 114, 243–265](https://doi.org/10.1098/rspa.1927.0039)). Fermi named it "Golden Rule No. 2" in his lecture notes ([Fermi 1950, *Nuclear Physics: A Course Given by Enrico Fermi*, University of Chicago Press]). The misattribution stuck. Use Fermi's name and remember whose math it was.

The conditions for the rule:
- *Long-time limit.* Time $t$ must be long compared to $1/\omega_{fi}$, so the delta-function approximation holds.
- *First-order validity.* Time $t$ must be short enough that $|c_f^{(1)}|^2 \ll 1$, so first-order perturbation theory is adequate.
- *Continuum.* The final states must be densely packed near $E_f = E_i + \hbar\omega$. For transitions between discrete bound states, you do *not* get a linear-in-$t$ rate; you get Rabi oscillations instead.

Applications: spontaneous emission rates (Einstein $A$ coefficients), beta decay (Fermi's original use case), neutron capture cross sections, photoionization, Raman scattering, LED radiative recombination, photovoltaic quantum efficiency, atomic line widths. Anywhere a quantum system transitions from a discrete state into a continuum under a time-dependent perturbation, Fermi's golden rule supplies the rate.

**Common misconception.** "Fermi's golden rule is exact." It is first-order perturbation theory applied to transitions into a continuum. It is excellent when its three assumptions hold and arbitrarily bad when they do not. Bound-state-to-bound-state transitions (no continuum) require a different treatment — Rabi oscillation formulas, two-level dynamics. Strong-field transitions ($\hat{H}'$ not small) require higher orders or non-perturbative methods (Floquet theory for periodic driving, exact numerics for arbitrary time dependence).

## 5. Worked example — relativistic correction to hydrogen $1s$

A worked first-order perturbation calculation that connects to fine-structure and gives an empirical handle on how big perturbation corrections typically are.

The non-relativistic kinetic energy operator is $\hat{T} = \hat{p}^2/(2m)$. The exact relativistic kinetic energy is $T = \sqrt{p^2 c^2 + m^2 c^4} - mc^2$. Expand in powers of $p/(mc)$:

$$ T = \frac{p^2}{2m} - \frac{p^4}{8 m^3 c^2} + \cdots. $$

The first correction is

$$ \hat{H}'_{\text{rel}} = -\frac{\hat{p}^4}{8 m^3 c^2}. $$

For hydrogen, compute the first-order energy correction to the ground state $|1s\rangle$:

$$ E_{1s}^{(1)} = \langle 1s | \hat{H}'_{\text{rel}} | 1s \rangle = -\frac{1}{8 m^3 c^2} \langle 1s | \hat{p}^4 | 1s \rangle. $$

The cleanest way to evaluate $\langle 1s | \hat{p}^4 | 1s \rangle$ is to use $\hat{p}^2 = 2m(\hat{H}_0 - \hat{V}) = 2m(\hat{H}_0 + e^2/(4\pi\epsilon_0 r))$. Then $\hat{p}^4 = [2m(\hat{H}_0 - \hat{V})]^2$. Sandwich between $|1s\rangle$ states:

$$ \langle 1s | \hat{p}^4 | 1s \rangle = 4 m^2 \langle 1s | (\hat{H}_0 - \hat{V})^2 | 1s \rangle = 4 m^2 \left[ E_1^2 - 2 E_1 \langle V \rangle + \langle V^2 \rangle \right]. $$

For hydrogen $1s$:
- $E_1 = -13.6$ eV $= -(1/2) m c^2 \alpha^2$ (where $\alpha = e^2/(4\pi\epsilon_0 \hbar c) \approx 1/137$ is the fine-structure constant)
- $\langle 1/r \rangle_{1s} = 1/a_0 = m c \alpha / \hbar$, so $\langle V \rangle = -e^2/(4\pi\epsilon_0 a_0) = -2 E_1 \cdot (-1) = 2 E_1 \cdot \text{(sign)}$... carefully: $\langle V \rangle = -e^2/(4\pi\epsilon_0) \cdot \langle 1/r \rangle = 2 E_1$ (using the virial theorem $\langle T \rangle = -E_1$, $\langle V \rangle = 2 E_1$).
- $\langle 1/r^2 \rangle_{1s} = 2/a_0^2$, so $\langle V^2 \rangle = (e^2/4\pi\epsilon_0)^2 \cdot 2/a_0^2 = 2 \cdot (2 E_1)^2 \cdot a_0^2/a_0^2 \cdot (\dots)$ — the algebra cleans up after substituting $a_0 = \hbar/(m c \alpha)$.

After grinding through, the result (Griffiths §6.3 walks it cleanly) is

$$ E_{1s}^{(1)} = -\frac{\alpha^2}{4} \cdot 13.6\ \text{eV} \cdot \left( 4 - 1 \right) = -\frac{\alpha^2}{2} |E_1| \cdot \text{(numerical factor)}. $$

A cleaner statement: the relativistic correction to hydrogen $1s$ is of order $\alpha^2 \cdot |E_1| \approx (1/137)^2 \cdot 13.6$ eV $\approx 7 \times 10^{-4}$ eV. This is small — about a part in $20{,}000$ of the binding energy. That smallness is what makes perturbation theory work for fine structure: the fine-structure constant $\alpha \approx 1/137$ is small, so the perturbation series in $\alpha^2$ converges fast and the first few terms suffice. The full fine-structure calculation (relativistic kinetic correction, spin-orbit, Darwin term) gives splittings of order $\alpha^2 \cdot |E_1| \sim 10^{-4}$ eV, which matches the observed hydrogen fine structure to high precision.

The lesson: first-order perturbation theory is the everyday workhorse. When $\alpha$ is small, the series in $\alpha^2$ is small, and the leading correction tells you almost everything you can measure about fine structure.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Time-independent PT (non-degenerate) | Ch. 6.1 | not covered | §4.1 (full derivation, Stark example) |
| Degenerate PT | Ch. 6.2 | not covered | §4.2 (Stark $n=2$ as worked example) |
| Variational principle | Ch. 7 | not covered | §4.3 (helium with $Z^*$ as parameter) |
| WKB approximation | Ch. 8 | not covered | §4.4 (tunneling + Bohr–Sommerfeld + Maslov pointer) |
| Time-dependent PT | Ch. 9.1–9.2 | not covered | §4.5 first half (interaction picture, $c_f^{(1)}$) |
| Fermi's golden rule | Ch. 9.2–9.3 | not covered | §4.5 second half (full derivation) |

The pop-sci book contributes nothing to this unit. Griffiths Chapters 6–9 are the formal reference. This unit takes the four chapters, picks the deep-dive on Fermi's golden rule because it powers Unit 10, and treats the other four methods at "derivation + worked example + sources" depth.

## 7. Exercises

**E1 (L1, Knowledge).** State the four formulas from this unit: first-order energy correction, first-order state correction, second-order energy correction, Fermi's golden rule. For each, name the conditions under which it applies.

**E2 (L3, Application).** Compute the first-order Stark effect on hydrogen $n=2$. The four degenerate states are $|2s\rangle, |2p_x\rangle, |2p_y\rangle, |2p_z\rangle$ with perturbation $\hat{H}' = e\hat{z}\mathcal{E}$. Identify by symmetry which matrix elements vanish. Build the $4\times 4$ matrix in the degenerate subspace. Diagonalize the surviving $2\times 2$ block in $\{|2s\rangle, |2p_z\rangle\}$. Report the four corrected energies.

**E3 (L3, Application).** Run the helium variational calculation with the one-parameter trial state $\psi(\mathbf{r}_1, \mathbf{r}_2) = e^{-Z^*(r_1 + r_2)/a_0}$ (unnormalized). Compute the kinetic, electron-nucleus, and electron-electron expectation values as functions of $Z^*$ (you may quote $\langle 1/r_{12}\rangle = (5/8) Z^*$ in atomic units without derivation). Minimize over $Z^*$, report the optimal $Z^*$ and the resulting ground-state energy in eV.

**E4 (L3, Application).** WKB transmission through a triangular barrier. The potential is $V(x) = V_0 (1 - x/L)$ for $0 \leq x \leq L$ and $V = 0$ outside. For a particle of energy $E < V_0$ incident from the left, compute $T_{\text{WKB}}$. (You should get an exponential whose argument involves an integral of $\sqrt{V(x) - E}$ from the turning point to $x = L$; do the integral.)

**E5 (L4, Analysis).** You are handed a Hamiltonian and asked to find the ground state. Decide which approximation method is appropriate, and justify your choice in one paragraph:
  (a) Anharmonic oscillator $\hat{H} = \hat{p}^2/2m + (1/2)m\omega^2 \hat{x}^2 + \lambda \hat{x}^4$ for small $\lambda$.
  (b) Helium ground state.
  (c) Electron tunneling through a $1$ nm oxide barrier in a flash-memory cell.
  (d) Hydrogen atom in a constant electric field of $10^7$ V/m.
  (e) Photoionization rate of a hydrogen atom in a continuous-wave laser field.

**E6 (L5, Evaluation).** Read the abstract and first paragraph of Dyson's 1952 paper "Divergence of Perturbation Theory in Quantum Electrodynamics" ([*Physical Review* 85, 631–632](https://doi.org/10.1103/PhysRev.85.631)). In your own words, explain why analyticity at $\alpha = 0$ fails. What does this imply about the convergence properties of QED perturbation theory? Does it threaten the *usefulness* of QED predictions, or only their *mathematical structure*?

**E7 (L6, Synthesis).** Derive Fermi's golden rule from time-dependent perturbation theory. Start from the first-order transition amplitude $c_f^{(1)}(t) = (1/i\hbar)\int_0^t \langle f | \hat{H}'(t') | i \rangle e^{i\omega_{fi}t'}\, dt'$. Specialize to a sinusoidal perturbation $\hat{H}' = \hat{V} \cdot 2\cos(\omega t)$ for $t > 0$. Compute $|c_f^{(1)}|^2$ in the resonant approximation. Take the long-time limit using $\sin^2(\Omega t/2)/\Omega^2 \to (\pi t / 2)\, \delta(\Omega)$. Integrate over a continuum of final states with density $\rho(E_f)$. Identify (a) the long-time condition and (b) the small-$\hat{H}'$ condition, and explain the tension between them.

## 8. What would change my mind

The methods themselves are not in dispute — they are derivations from the time-(in)dependent Schrödinger equation under stated assumptions, and the derivations are checked by sixty years of agreement with experiment. What could revise this unit is a demonstration that one of the *stated assumptions* fails in a regime where the textbook predicts it should hold. Two specific possibilities:

A QED measurement at large coupling where the perturbation series, summed with Borel resummation and the standard resurgence machinery, *fails* to reproduce the experimental result. This would force a more radical rethinking of how non-perturbative information is encoded in perturbative series — an active research program ([Costin and Dunne, multiple papers 2017–2023, on resurgence; verify state of the art 2026]). Current resurgent analysis of QED, QCD, and related theories agrees with high-precision measurements.

A controlled experiment in which Fermi's golden rule fails in a regime where the long-time and continuum conditions are well-satisfied. Such an experiment would be evidence either of a missing term in first-order perturbation theory or of a breakdown of one of the rule's stated assumptions in a regime that should be clean. No such failure has been reported.

The unit's aging risk is low. These methods are textbook physics from the 1930s onward; their successes are too numerous to enumerate. New applications appear constantly (variational quantum eigensolvers on quantum hardware, tensor-network methods for many-body systems), but the underlying mathematics is stable.

## 9. Still puzzling

- *Why does the asymptotic series work so well?* Perturbation theory diverges in many physical theories (QED, the anharmonic oscillator). Yet truncating at the optimal order gives results accurate to many decimal places. The mathematical theory of asymptotic series, Borel summation, and resurgence (Écalle 1980s) gives a framework for *why*, but the practical question — "given a divergent series, how do I extract the right physical answer?" — is still an active research area at the intersection of mathematical physics and number theory. I am comfortable using the first few terms; I am not comfortable with the claim that physicists fully understand the relationship between divergent expansions and exact answers.

- *Where does the $+1/2$ in Bohr–Sommerfeld really come from?* The Maslov index can be derived by matching WKB to Airy functions at each turning point. But it has a deeper interpretation as the winding number of a Lagrangian submanifold in phase space — a piece of symplectic geometry that does not typically appear in an undergraduate course. The cleanest statement: the $+1/2$ is a topological correction to the naive Bohr quantization, encoded by the geometry of phase-space trajectories. The full story belongs to a graduate course in mathematical physics.

- *Is the variational method always trustworthy for the ground state?* For the *energy*, yes (the bound is one-sided, by the principle). For *other observables*, no — the variational wave function is not constrained to give good values of, say, $\langle r^2 \rangle$ or charge density at a point. Modern quantum chemistry routinely reports variational energies to six decimal places and treats charge densities as an order-of-magnitude estimate. Why one observable is so much easier to compute well than another is a question about the geometry of the trial-state manifold near the true ground state, and not one I think undergraduate physics handles cleanly.

- *Why does Fermi's golden rule fail for strong fields?* Because first-order perturbation theory fails when $\hat{H}'$ is not small. The standard upgrades — Floquet theory for periodic driving, time-dependent DFT, exact numerical integration of the Schrödinger equation — are computational rather than analytic. Strong-field laser physics (attosecond science, high-harmonic generation) lives in this regime and is one of the active research frontiers in atomic physics. The first-order rule is one corner of a much larger landscape.

**Tags:** perturbation-theory, variational-principle, wkb-approximation, fermi-golden-rule, time-dependent-perturbation-theory, asymptotic-series, helium-variational, alpha-decay, hydrogen-fine-structure, griffiths-ch6-9
