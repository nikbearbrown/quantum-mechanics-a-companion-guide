# Unit 1 — Why Quantum Mechanics?

> Five experiments killed classical physics between 1900 and 1927. This unit shows you the math each one forced.

---

## 1. What this chapter is doing

Five experimental results — Planck's blackbody fit, the photoelectric threshold, Compton scattering, electron diffraction, and the Franck–Hertz current curve — broke classical physics one at a time over roughly a quarter century. The pop-sci companion ([Quantum Physics for Beginners, 2021]) covers four of these well as history (its Ch. 3, 4, 5, 6, 10, 11), but it does no math. Griffiths covers the same material in his introduction to Ch. 1 of *Introduction to Quantum Mechanics* (1st ed. 1994; 3rd ed. 2018), but compresses it because his real interest is the formalism in Ch. 2 onward. This companion unit does the math each experiment forces — the algebra a student needs to compute a threshold wavelength, a Compton shift, a de Broglie wavelength — so the rest of the course can stand on quantitative ground. The pop-sci book is your motivation reading; Griffiths is your formal reference; this unit is the calculator the other two leave out.

## 2. Learning objectives

By the end of this unit, you should be able to:

- **State** Planck's distribution, the photoelectric equation, the Compton wavelength-shift formula, the de Broglie relation, and the Franck–Hertz threshold condition. (Bloom L1)
- **Explain** in plain language *which classical prediction* each of the five experiments contradicts. (L2)
- **Compute** threshold wavelengths and photoelectron kinetic energies from a given work function and incident wavelength. (L3)
- **Derive** the Compton shift from energy–momentum conservation for a photon scattering off a free electron. (L4)
- **Predict** electron diffraction angles from the de Broglie relation plus the Bragg condition. (L4)
- **Distinguish** Planck's 1900 quantization of oscillators in the cavity walls from Einstein's 1905 quantization of the radiation field itself. (L5)

## 3. The motivating problem

On 27 April 1900, Lord Kelvin gave a Royal Institution address in which he is widely remembered for saying that nineteenth-century physics was a finished theory with "two small clouds" remaining on the horizon — one about the luminiferous ether (the Michelson–Morley result), the other about the equipartition of energy in blackbody radiation. The exact wording of Kelvin's talk has been the subject of historiographical argument [verify — the popular quotation comes from the printed version "Nineteenth-Century Clouds Over the Dynamical Theory of Heat and Light," *Philosophical Magazine* 6th series, vol. 2 (1901), pp. 1–40]. What is not in dispute: a generation of physicists in 1900 believed the basic laws were known. Mechanics from Newton, electrodynamics from Maxwell, statistical mechanics from Boltzmann, thermodynamics from Clausius. The rest was decimal places.

The decimal places turned out to be a different physics.

The trouble was that classical physics — Newton plus Maxwell plus Boltzmann — gave specific quantitative predictions about how matter and light should behave. When experimentalists pushed those predictions into new regimes (very short wavelengths, very weak light, very small particles, very precise spectroscopy), the predictions failed. Not as small corrections. As infinities, qualitative reversals, threshold effects classical physics had no language for. The five experiments below are the ones that, between them, made the failure unsurvivable.

You don't need quantum mechanics to read this unit. You need calculus, vectors, special relativity at the level of $E^2 = (pc)^2 + (mc^2)^2$, and the willingness to watch classical physics fail five times in a row and ask what replaces it.

## 4. Five experiments and the math they forced

### 4.1 Blackbody radiation and Planck's law

A blackbody is an idealization of a perfect absorber and emitter — a hot cavity with a tiny hole, in practice. Classical statistical mechanics, applied to the electromagnetic modes inside the cavity, gives a clean prediction. Each mode has on average $k_B T$ of energy by the equipartition theorem (half each for kinetic and potential). Count the modes in a frequency interval $[\nu, \nu+d\nu]$, multiply by $k_B T$, and you get the Rayleigh–Jeans spectral energy density:

$$ \rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T. $$

This rises without bound as $\nu \to \infty$. The total energy in the cavity, $\int_0^\infty \rho_{\text{RJ}}(\nu, T)\, d\nu$, diverges. Paul Ehrenfest, writing in 1911, called this the "ultraviolet catastrophe." A finite cavity at finite temperature should — according to classical physics — contain infinite energy in its short-wavelength modes. It doesn't. Otto Lummer and Ernst Pringsheim, working at the Physikalisch-Technische Reichsanstalt in Berlin (a national metrology lab, of all places), had been measuring blackbody spectra to high accuracy through the late 1890s. The measurements peaked at a finite frequency and fell off exponentially at high frequency. There was no catastrophe in nature.

Max Planck presented his fit to the data on 14 December 1900 — the date traditionally marked as the birth of quantum theory. The Planck distribution is

$$ \rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}. $$

The constant $h$ Planck fitted to Lummer and Pringsheim's measurements as $6.55 \times 10^{-27}$ erg·s, within 1% of today's defined value $h = 6.62607015 \times 10^{-34}$ J·s (exact since the 2019 SI redefinition, per the [BIPM]).

**The mechanism.** Planck's derivation went as follows. Consider an oscillator in the cavity wall at frequency $\nu$. Classically, this oscillator can exchange energy with the radiation field continuously, in any amount. Planck postulated instead that energy exchange happens only in discrete units of $E = h\nu$ — that the oscillator can emit or absorb energy only in integer multiples of $h\nu$. With this restriction, the average thermal energy of an oscillator at temperature $T$ is no longer $k_B T$ (equipartition); it's

$$ \langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}} = \frac{h\nu}{e^{h\nu/k_B T} - 1}. $$

The second equality is the standard geometric-series computation: let $x = e^{-h\nu/k_B T}$, and use $\sum n x^n = x/(1-x)^2$ and $\sum x^n = 1/(1-x)$. At low frequency ($h\nu \ll k_B T$), $\langle E \rangle \to k_B T$ — equipartition is recovered. At high frequency ($h\nu \gg k_B T$), $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$ — exponentially suppressed. The catastrophe is gone, replaced by a quiet exponential fall-off.

Multiply $\langle E \rangle$ by the mode-counting density $8\pi\nu^2/c^3$ (which is purely classical mode-counting, unchanged) and you get the Planck distribution above.

**The misconception.** "Planck quantized light." He did not. He quantized the energy exchange between oscillators in the cavity walls and the radiation field. The radiation itself, in Planck's 1900 picture, was still a continuous electromagnetic wave. The discrete packets lived in the walls, not in the field. This was a defensible move at the time — it preserved Maxwell's equations and asked only for a strange property of matter. Einstein's 1905 photoelectric paper is what quantized the field.

**Worked example: photon energy from a 500 nm line.** A green photon at $\lambda = 500$ nm has frequency $\nu = c/\lambda = (3.00 \times 10^8\ \text{m/s})/(5.00 \times 10^{-7}\ \text{m}) = 6.00 \times 10^{14}$ Hz, and energy $E = h\nu = (6.626 \times 10^{-34}\ \text{J·s})(6.00 \times 10^{14}\ \text{Hz}) = 3.97 \times 10^{-19}\ \text{J} = 2.48$ eV. Use this often. Photon energies in eV and wavelengths in nm satisfy $E[\text{eV}] \cdot \lambda[\text{nm}] = 1240$, a number worth memorizing.

*The lesson:* the discreteness of energy exchange — not of the radiation field, yet — is enough to fix the spectrum.

*The limit:* Planck himself did not believe in light quanta. The next experiment is the one that pushed the quantization into the field.

### 4.2 The photoelectric effect

Philipp Lenard in 1902 reported the experimental anomaly that broke the classical picture of light–matter interaction. Shine ultraviolet light on a clean metal surface; electrons come off. Reasonable. But the *kinetic energy of the ejected electrons depended on the frequency of the light, not on the intensity.* A very bright red beam (high intensity, low frequency) produced no electrons at all from certain metals. A dim ultraviolet beam (low intensity, high frequency) produced electrons immediately. Classically, intensity should matter — a brighter wave delivers more energy per unit time per unit area, and an electron tied to the surface should eventually accumulate enough energy to escape, given a long enough wait.

The wait does not come. The threshold is sharp. The kinetic energy scales with frequency above threshold, linearly. The classical picture fails on three counts simultaneously.

Einstein's 1905 paper [Einstein 1905, *Annalen der Physik* 17, 132–148](https://doi.org/10.1002/andp.19053220607) proposed that light itself is delivered in discrete energy packets — light quanta, later called photons — of energy $E = h\nu$. An electron bound to the metal with binding energy $\phi$ (the work function) absorbs one quantum, escapes if $h\nu > \phi$, and emerges with kinetic energy

$$ K_{\max} = h\nu - \phi. $$

That is the photoelectric equation. Below the threshold frequency $\nu_0 = \phi/h$ no electrons emerge, regardless of intensity. Above it, intensity controls *how many* electrons emerge per second (one per absorbed photon), and frequency controls *how much energy* each one has. The classical prediction — that more intensity buys more energy per electron — is wrong because each electron interacts with one photon, not with the average field.

Robert Millikan spent four years (1912–1916) trying to disprove Einstein's hypothesis with the most careful photoelectric measurements ever performed. He measured the stopping potential $V_s$ (the retarding voltage that just stops the most energetic electrons; $eV_s = K_{\max}$) as a function of incident frequency. The slope, by Einstein's equation, should be $h/e$. Millikan got $h = 6.57 \times 10^{-27}$ erg·s, within 0.5% of Planck's blackbody value [Millikan 1916, *Physical Review* 7, 355–388](https://doi.org/10.1103/PhysRev.7.355). He published the result with the now-famous concession that the photoelectric equation worked despite his belief that the underlying photon hypothesis was "untenable." The experiment confirmed Einstein; Einstein won the 1921 Nobel Prize specifically for this — *not* for relativity, which was still considered speculative.

**The misconception.** "The photoelectric effect proves light is particles." More precisely: it shows that the energy delivered to a single bound electron arrives in indivisible packets of $h\nu$, and the *rate* of ejection (not the energy per ejection) scales with intensity. Light is neither a classical wave nor a classical particle. Unit 2 and Unit 3 of this companion are about what it actually is.

**Worked example: sodium.** Sodium has work function $\phi \approx 2.28$ eV [CRC Handbook value; *verify*]. The threshold wavelength is

$$ \lambda_0 = \frac{hc}{\phi} = \frac{1240\ \text{eV·nm}}{2.28\ \text{eV}} \approx 544\ \text{nm}. $$

That's green light. Below 544 nm — blue, violet, UV — sodium emits photoelectrons. Above 544 nm — yellow, orange, red — it doesn't, regardless of how intense the beam is.

Now illuminate sodium with $\lambda = 400$ nm (violet). Photon energy $h\nu = 1240/400 = 3.10$ eV. Kinetic energy of the most energetic photoelectron:

$$ K_{\max} = h\nu - \phi = 3.10\ \text{eV} - 2.28\ \text{eV} = 0.82\ \text{eV}. $$

If you set up a stopping voltage of $V_s = 0.82$ V, you stop these electrons exactly.

*The lesson:* one photon, one electron. Energy comes in packets, the packets are delivered indivisibly, and the threshold is sharp.

*The limit:* this experiment quantizes the field but does not yet pin down the photon's momentum.

### 4.3 Compton scattering

In 1923 Arthur Holly Compton at Washington University in St. Louis scattered X-rays off graphite and measured the scattered wavelength as a function of angle [Compton 1923, *Physical Review* 21, 483–502](https://doi.org/10.1103/PhysRev.21.483). The classical picture (Thomson scattering) predicts that the electrons in the target oscillate at the driving frequency and re-radiate at the same frequency — no wavelength shift, just a redistribution in angle. Compton found a shift. The scattered light came out *redder* (longer wavelength) than the incident light, by an amount that depended only on the scattering angle:

$$ \Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta). $$

The combination $h/m_e c = 2.426 \times 10^{-12}$ m is called the Compton wavelength of the electron. The shift is small (picometers) but unmistakable.

The derivation is the cleanest piece of math in this unit. We use special relativity: the photon has energy $E_\gamma = h\nu$ and momentum $p_\gamma = h\nu/c = h/\lambda$ (these are the two relations $E = h\nu$ and $\lambda = h/p$ specialized to a massless particle). The electron is initially at rest, with energy $m_e c^2$ and zero momentum. After the collision, the photon has energy $E_\gamma' = hc/\lambda'$ and momentum $h/\lambda'$ in a new direction; the electron has some energy $E_e$ and momentum $p_e$.

*Conservation of energy:*

$$ h\nu + m_e c^2 = h\nu' + E_e. $$

*Conservation of momentum* (two components, with $\theta$ the photon scattering angle and $\phi$ the electron recoil angle):

$$ \frac{h\nu}{c} = \frac{h\nu'}{c}\cos\theta + p_e \cos\phi, $$
$$ 0 = \frac{h\nu'}{c}\sin\theta - p_e \sin\phi. $$

Solve for $p_e \cos\phi$ and $p_e \sin\phi$, square and add to eliminate $\phi$:

$$ p_e^2 c^2 = (h\nu)^2 - 2(h\nu)(h\nu')\cos\theta + (h\nu')^2. $$

From energy conservation, $E_e = h(\nu - \nu') + m_e c^2$, so

$$ E_e^2 = h^2(\nu - \nu')^2 + 2 m_e c^2 h(\nu - \nu') + (m_e c^2)^2. $$

Use the relativistic energy-momentum relation $E_e^2 = p_e^2 c^2 + (m_e c^2)^2$:

$$ p_e^2 c^2 = h^2(\nu - \nu')^2 + 2 m_e c^2 h(\nu - \nu'). $$

Set the two expressions for $p_e^2 c^2$ equal:

$$ h^2(\nu - \nu')^2 + 2 m_e c^2 h(\nu - \nu') = (h\nu)^2 - 2(h\nu)(h\nu')\cos\theta + (h\nu')^2. $$

Expand $(h\nu - h\nu')^2 = (h\nu)^2 - 2(h\nu)(h\nu') + (h\nu')^2$ on the left and cancel:

$$ -2(h\nu)(h\nu') + 2 m_e c^2 h(\nu - \nu') = -2(h\nu)(h\nu')\cos\theta. $$

Divide by $2(h\nu)(h\nu')$:

$$ \frac{m_e c^2 (\nu - \nu')}{\nu \nu'} = 1 - \cos\theta. $$

Use $\nu = c/\lambda$ so that $(\nu - \nu')/(\nu\nu') = (\lambda' - \lambda)/c$:

$$ \frac{m_e c (\lambda' - \lambda)}{1} = h(1 - \cos\theta) \cdot \frac{c}{c} \implies \Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta). $$

Half a page of algebra and the answer drops out, no quantum mechanics required beyond treating the photon as a relativistic particle with $E = h\nu$ and $p = h/\lambda$.

**The misconception.** The pop-sci book mentions the Klein–Nishina formula in this context. Klein and Nishina (1929) computed the *differential cross section* for photon–electron scattering using Dirac's relativistic electron theory — it tells you the angular distribution of scattering events. The wavelength shift above is purely kinematic and was derived by Compton in 1923 (and independently by Debye the same year, in *Physikalische Zeitschrift* — [verify exact citation]). Klein–Nishina answers "how often does scattering happen at angle $\theta$"; Compton answers "what wavelength does the scattered photon have." Two different formulas, frequently confused.

**Worked example: Compton's Mo Kα experiment.** Compton used molybdenum Kα X-rays at $\lambda = 0.0711$ nm. At $\theta = 90°$, $\cos\theta = 0$, so $\Delta\lambda = h/m_e c = 2.43$ pm = 0.00243 nm. Scattered wavelength: $\lambda' = 0.0735$ nm. Compton measured (after careful angular discrimination) 0.0734 nm. The agreement was the moment the photon picture became unavoidable.

*The lesson:* the photon carries momentum $h/\lambda$. The two earlier experiments quantized energy in the field; this one quantized momentum, and so completed the photon as a relativistic particle.

*The limit:* the photon is still being treated like a billiard ball with definite energy and momentum. Unit 3 will show this is a calculational idealization — physical photons live in normalizable wave packets, not as pure plane waves.

### 4.4 The de Broglie hypothesis

Louis de Broglie's 1924 doctoral thesis at the University of Paris took the symmetric move. Einstein had given light, conventionally a wave, a particle nature. De Broglie proposed that particles, conventionally points, should have a wave nature. Specifically:

$$ \lambda = \frac{h}{p}. $$

Same relation as for the photon, applied to matter. A particle with momentum $p$ has an associated wavelength $\lambda$.

The numerical consequence is the reason you don't notice this in daily life. A 1 kg cricket ball moving at 1 m/s has $\lambda = (6.6 \times 10^{-34}\ \text{J·s})/(1\ \text{kg·m/s}) = 6.6 \times 10^{-34}\ \text{m}$ — twenty orders of magnitude smaller than a proton. No interference experiment in the universe could detect that wavelength. An electron, on the other hand, accelerated through 54 V (kinetic energy 54 eV), has $\lambda$ of order 0.17 nm — comparable to atomic spacings in a crystal. So an electron should diffract off a crystal lattice the way X-rays do.

Clinton Davisson and Lester Germer at Bell Labs found this in 1927, three years after de Broglie's prediction [Davisson & Germer 1927, *Physical Review* 30, 705–740](https://doi.org/10.1103/PhysRev.30.705). They scattered 54 eV electrons off a nickel crystal and saw a sharp diffraction peak at the angle Bragg's condition predicts for $\lambda = 0.167$ nm. George Paget Thomson, independently, confirmed it with thin metal foils the same year and shared the 1937 Nobel for the work. (G. P. Thomson's father, J. J. Thomson, had won the 1906 Nobel for showing the electron was a particle. The history of physics has a sense of humor.)

**The misconception.** "The de Broglie wavelength is the size of the particle." It is not — it is the wavelength of the *amplitude* associated with motion at momentum $p$, and you don't have the language yet for what that amplitude is (Unit 3 supplies it). When the particle is detected, it registers as a point in a detector. The wavelength shows up in interference patterns built from many detections.

**Worked example: Davisson–Germer.** Electrons accelerated through $V = 54$ V have kinetic energy $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Their momentum is

$$ p = \sqrt{2 m_e K} = \sqrt{2 (9.11 \times 10^{-31}\ \text{kg})(8.65 \times 10^{-18}\ \text{J})} \approx 3.97 \times 10^{-24}\ \text{kg·m/s}. $$

De Broglie wavelength:

$$ \lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10}\ \text{m} = 0.167\ \text{nm}. $$

Nickel has surface (111) plane spacing $d = 0.215$ nm. The Bragg condition for first-order constructive interference is $n\lambda = 2 d \sin\theta_B$, with $\theta_B$ measured from the surface. But the Davisson–Germer geometry is back-scattering, and the angle they reported is $\phi = 50°$ from the incident direction. Translating, the Bragg condition for surface diffraction gives $\lambda = d \sin\phi$, so $\sin\phi = 0.167/0.215 = 0.777$, $\phi = 51°$. They measured 50°. Agreement to within a degree.

The single-electron version of this experiment was first done as a continuous-buildup video by Akira Tonomura's group at Hitachi in 1989 ([Tonomura et al., *American Journal of Physics* 57(2), 117–120](https://doi.org/10.1119/1.16104), [verify pagination]). Electrons arrive one at a time, each as a point on the detector. The pattern of points, accumulated over hours, is a diffraction pattern. There is no classical reading of this — a single particle "interferes with itself" in a way that has no analog in Newtonian language.

*The lesson:* matter has wave properties, and the wave properties are encoded in an amplitude whose squared modulus gives detection probability.

*The limit:* this is a relation, not a wave equation. You can compute wavelengths from momenta; you cannot yet propagate a wave function in time. Unit 3 supplies the equation.

### 4.5 Franck–Hertz: discrete atomic energy levels

In 1914 James Franck and Gustav Hertz reported the experiment that, in retrospect, was the cleanest direct evidence for discrete atomic energy levels [Franck & Hertz 1914, *Verhandlungen der Deutschen Physikalischen Gesellschaft* 16, 457–467]. They accelerated electrons through a vapor of mercury atoms and measured the current reaching a collector as a function of the accelerating voltage. The current rose, then dipped sharply at 4.9 V, then rose again, then dipped at 9.8 V (twice 4.9), then dipped at 14.7 V (three times). The dips were periodic, with spacing 4.9 V.

The interpretation: an electron with kinetic energy below 4.9 eV scatters elastically off a mercury atom — bouncing around like a marble — and continues to gain energy from the accelerating field. At 4.9 eV the electron can lose exactly that amount to excite the mercury atom from its ground state to its first excited state, an *inelastic* collision. After the inelastic collision the electron is too slow to reach the collector against the retarding field, hence the dip. With more accelerating voltage the electron regains enough energy to reach the collector — until 9.8 V, at which point it can excite *two* mercury atoms inelastically, and so on.

The 4.9 eV value corresponds to the $6\,{}^1S_0 \to 6\,{}^3P_1$ transition in mercury. If the interpretation is right, the excited mercury atoms should emit photons when they decay back to the ground state, and those photons should have energy 4.9 eV. Wavelength:

$$ \lambda = \frac{hc}{E} = \frac{1240\ \text{eV·nm}}{4.9\ \text{eV}} \approx 253\ \text{nm}. $$

In the ultraviolet. Franck and Hertz built a spectroscope and saw it: a sharp emission line at 253.7 nm whenever the accelerating voltage exceeded 4.9 V.

This was the direct experimental demonstration that atoms have discrete internal energy levels. The spectroscopic evidence (Balmer series, Lyman, Paschen) was already known — but spectroscopy is indirect, you see the emitted photons and back-infer the levels. Franck–Hertz is direct: you watch the electron lose energy in discrete chunks.

**The misconception.** "Franck–Hertz proves the Bohr model." It proves that mercury has discrete energy levels and the first one is 4.9 eV above the ground state. It does not prove the *specific* level structure of hydrogen Bohr proposed. The Bohr model was the first theoretical account that predicted a discrete level structure for hydrogen, but the full quantum-mechanical solution (Unit 6) refines it substantially. Franck–Hertz is robust under that refinement; the Bohr model is only approximately right.

**Worked example: the threshold photon.** From the 4.9 V threshold, predict the wavelength of the emitted UV photon. Compare to the measured 253.7 nm. Agreement to within experimental precision. The two completely different experimental probes — electron stopping voltage and photon wavelength — give the same energy, and that energy is a property of the mercury atom, not of either probe.

*The lesson:* atomic energy levels are discrete. This is a fact about matter, not about light, and it was established by an experiment that did not require any quantum theory of light to interpret.

*The limit:* the experiment names the levels but does not predict them. Predicting them requires the Schrödinger equation for the hydrogen atom (Unit 6) or, in the multi-electron mercury case, computational quantum chemistry that goes well beyond an undergraduate course.

## 5. Synthesis: what these five experiments demand

After 1927, five quantitative facts had to be accommodated by any successor to classical physics:

1. Energy is exchanged between matter and the radiation field in discrete units of $h\nu$ (Planck).
2. The electromagnetic field itself carries energy in indivisible packets of $h\nu$ (Einstein, photoelectric).
3. Those packets carry momentum $h/\lambda$ (Compton).
4. Matter has wavelike properties with wavelength $h/p$ (de Broglie, Davisson–Germer).
5. Atomic systems have discrete internal energy levels (Franck–Hertz).

Three corollary requirements follow. The new theory must give a *probabilistic* account of detection — you cannot predict where a single electron in the two-slit experiment lands; you can only predict the long-run distribution. It must have *wave-equation structure* — to handle the interference and the matter-wave behavior. And it must have *eigenvalue structure* — to handle the discrete energy levels.

Unit 2 builds the mathematics: complex vector spaces, Hermitian operators, eigenvalues. Unit 3 supplies the wave equation: the Schrödinger equation. The five experiments above are the constraints; the next two units are the theory that meets them.

## 6. Reading map

| TIKTOC topic | Griffiths reference | Pop-sci book | This companion |
|---|---|---|---|
| Classical physics and its failures | Ch. 1 introduction | Ch. 3, 11 (motivation) [BOOK] | §3, §4 (frames the failures with math) |
| Blackbody radiation | Ch. 1 intro + Afterword on thermal radiation | Ch. 3 [BOOK ✅] | §4.1 (Planck derivation) |
| Photoelectric effect | Ch. 1 intro | Ch. 4 [BOOK ✅] | §4.2 (work function, threshold) |
| Compton scattering | brief in Ch. 1 intro; full derivation in Griffiths *Elementary Particles* | Ch. 10 [BOOK ⚠️ — Klein–Nishina error] | §4.3 (full kinematic derivation) |
| de Broglie + wave-particle | Ch. 1 intro | Ch. 5, 11 [BOOK ✅/⚠️] | §4.4 (Davisson–Germer worked) |
| Franck–Hertz | not in Griffiths | Ch. 6 [BOOK ✅] | §4.5 (threshold + UV photon) |

The pop-sci book is the right "first read" for the history. Griffiths Ch. 1 is the right second read for the physics, and is unusually compressed because his book proper begins at Ch. 1.1 with the wave function. This companion fills the quantitative middle.

## 7. Exercises

**E1 (L1, Knowledge).** State the five formulas of this chapter from memory: Planck's distribution, the photoelectric equation, the Compton shift, the de Broglie relation, and the Franck–Hertz threshold condition.

**E2 (L3, Application).** A potassium surface ($\phi = 2.30$ eV) is illuminated by light of wavelength 350 nm. Compute (a) the threshold wavelength for photoemission, (b) the maximum kinetic energy of the photoelectrons, (c) the stopping voltage you would need to halt the most energetic electrons. *Hint: use $E[\text{eV}] \cdot \lambda[\text{nm}] = 1240$.*

**E3 (L3, Application).** An X-ray photon of wavelength 0.020 nm scatters off a free electron at $\theta = 60°$. Compute the wavelength shift, the scattered wavelength, and the kinetic energy gained by the electron.

**E4 (L4, Analysis).** Derive the Compton wavelength-shift formula yourself, starting from energy and momentum conservation. Do not refer back to §4.3 until you are stuck. After you derive it, take the non-relativistic limit ($h\nu \ll m_e c^2$) and check that the electron recoil is small compared to $m_e c$.

**E5 (L4, Analysis).** An electron is accelerated through a potential difference of 1000 V. Compute its de Broglie wavelength. (You may use the non-relativistic relation $p = \sqrt{2 m_e K}$ at this energy — check after the fact that this is justified.) Compare to the X-ray wavelength used in Compton's original experiment (0.0711 nm). Which is shorter?

**E6 (L5, Evaluation).** Read Millikan's 1916 paper introduction (*Physical Review* 7, 355–388). Identify two places where Millikan describes his expectations going into the experiment. Now identify the sentence where he concedes the result. What does the gap between expectation and result tell you about how empirical science actually proceeds when a theorist proposes something physicists do not yet believe?

**E7 (L6, Synthesis).** A hypothetical 1925 experimentalist accelerates electrons through 200 V and aims them at a crystal with interplanar spacing 0.30 nm. Predict the angle of the first-order diffraction peak from the de Broglie wavelength and the Bragg condition. Then design a single sentence describing what the experimentalist would conclude if the peak appeared at the predicted angle, and a second sentence describing what they would conclude if it did not appear at all.

## 8. What would change my mind

A reproducible experiment that recovered classical wave or particle behavior in a regime where the five experiments above predict quantum behavior — say, photoelectric emission below the threshold frequency at sufficiently high intensity, or electron diffraction wavelengths that did not scale as $h/p$ — would force a fundamental revision of this unit's central claim. The current claim is conservative and well-tested: in the regimes accessible to these five experiments, classical physics is *quantitatively* wrong, and the quantum corrections all scale with Planck's constant $h$. A demonstration that $h$ effectively goes to zero in any of these regimes would rewrite the unit. None has appeared in over a century of attempts.

## 9. Still puzzling

- *What is a photon, really?* The operational definition — a quantum of the electromagnetic field with energy $h\nu$ and momentum $h\nu/c$ — works for all the calculations in this unit. The ontological question is harder. Willis Lamb argued in 1995 ([*Applied Physics B* 60, 77–84](https://doi.org/10.1007/BF01135846)) that the term "photon" should be retired in favor of "QED field excitation." Most working physicists keep the word and leave the ontology unresolved. The companion takes the operational position throughout.

- *Why these constants?* Planck's constant has a specific value, $6.626 \times 10^{-34}$ J·s. Why this value, and not another? The Standard Model treats $h$ as an empirical input — it sets the scale at which classical descriptions fail. Whether $h$ is determined by some deeper theory or is a brute fact about our universe is open and probably unresolvable within non-relativistic QM.

- *Schrödinger's interpretive failure.* By 1926 Schrödinger had the right wave equation but the wrong interpretation of $\psi$ — he wanted it to be a literal matter wave. Born's probabilistic interpretation displaced his within months. Why did the right equation come with the wrong story attached? Unit 3 will return to this; the short answer is that the equation is forced by the experimental constraints above, while the interpretation requires an additional postulate that no single experiment compels.

- *Mercury's level structure.* Franck–Hertz tells you mercury's first excited state is 4.9 eV up. Predicting that number from first principles requires multi-electron quantum chemistry and is genuinely hard — beyond this course. The fact that the experiment exists, and that the level is sharp and reproducible, is what matters for now.

**Tags:** blackbody-radiation, photoelectric-effect, compton-scattering, de-broglie, franck-hertz, classical-failures, planck-constant, quantum-history, griffiths-ch1
