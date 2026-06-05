# Chapter 1 — Why Quantum Mechanics?

## TL;DR

- A universe that broke nearly every prediction classical physics handed it, and the theory that grew up to explain the wreckage.
- Five experiments, one constant, and the moment physics stopped being finished. Blackbody radiation, the photoelectric effect, Compton scattering, matter waves, Franck–Hertz.
- Read it for the argument, the vocabulary, and the judgment it asks of you.

*The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.*

---

Consider the situation around 1900. The leading physicists of the day were, by and large, convinced the subject was nearly done. Newton owned mechanics, Maxwell owned electrodynamics, Boltzmann owned statistical mechanics, Clausius owned thermodynamics. The laws were in hand; what remained, supposedly, was bookkeeping — pinning down a few more decimal places.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

Those decimal places turned out to hide a different universe.

The trouble was not philosophical; it was quantitative, which is worse. Classical physics — all four pillars working together — made sharp, testable claims about how matter and light should behave. When experimenters pushed into the corners — very short wavelengths, very faint beams, very precise spectroscopy — the predictions did not miss by a hair. They returned infinities where the apparatus returned finite peaks. They returned smooth onsets where the apparatus returned sharp cutoffs. And in some cases they had no language at all for results that were reproducible, crisp, and utterly foreign to the theory.

Five experiments, spread over roughly a quarter century, did the damage. I want to take them one at a time and show you the mathematics each one forced — not as a history lesson, but as a sequence of confrontations between a beautiful theory and a universe that declined to cooperate.

---

## The first confrontation: infinite energy in a box

Begin with something innocent: a hollow metal box, walls held at a fixed temperature. The walls glow, emitting electromagnetic radiation that rattles around inside until it reaches thermal equilibrium with them. The question is how that energy distributes itself across frequencies.

Classical statistical mechanics answers cleanly. Each electromagnetic mode in the cavity gets, on average, energy $k_B T$ by equipartition — and there are infinitely many modes, since you can always go to a higher frequency. The number of modes in a frequency interval $[\nu, \nu + d\nu]$ is $8\pi\nu^2/c^3$ per unit volume. Multiply by $k_B T$:

$$\rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T.$$

![Plot of Rayleigh–Jeans vs](../images/01-why-quantum-mechanics-fig-01.png)
*Figure 1.1 — Plot of Rayleigh–Jeans vs*

This climbs without limit as the frequency rises. The total energy, $\int_0^\infty \rho_{\text{RJ}} \, d\nu$, diverges. Taken seriously, a box at room temperature holds infinite energy in its short-wavelength modes — a conclusion Paul Ehrenfest later named the "ultraviolet catastrophe."

Nature, of course, declined to oblige. Otto Lummer and Ernst Pringsheim, at the Physikalisch-Technische Reichsanstalt in Berlin, were measuring blackbody spectra with extraordinary care through the late 1890s. Their data showed a finite peak at a characteristic frequency and then an exponential fall-off above it. There was no catastrophe out in the world — only a shape, and the shape demanded an explanation.

Max Planck supplied one on 14 December 1900. His distribution is:

$$\rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}.$$

He fixed the constant $h$ by fitting the data: $6.55 \times 10^{-27}$ erg·s, within 1% of today's value $h = 6.626 \times 10^{-34}$ J·s.

Here is the move. Suppose the oscillators in the cavity walls — the atoms absorbing and re-emitting radiation — cannot trade energy with the field continuously. Suppose instead they trade it only in discrete chunks of size $h\nu$: whole multiples of an energy quantum. Then the average thermal energy of an oscillator at frequency $\nu$ is no longer $k_B T$ but:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}}.$$

Set $x = e^{-h\nu/k_B T}$. The numerator is $h\nu \sum n x^n = h\nu \cdot x/(1-x)^2$; the denominator is $\sum x^n = 1/(1-x)$. Divide:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_B T} - 1}.$$

At low frequencies, $h\nu \ll k_B T$, so $e^{h\nu/k_B T} - 1 \approx h\nu/k_B T$ and $\langle E \rangle \to k_B T$ — equipartition is back. At high frequencies, $h\nu \gg k_B T$, and $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$ — exponentially crushed. The catastrophe is gone. Multiply by the (classical, unchanged) mode-counting density $8\pi\nu^2/c^3$ and Planck's distribution drops out.

One point to settle before moving on, because everyone gets it wrong: Planck did not quantize light. He quantized the energy *exchange* between the cavity walls and the radiation field. In his 1900 picture the radiation itself was still a continuous electromagnetic wave; the discrete packets lived in the walls, not the field. Putting the packets in the field took Einstein, five years later.

---

## The second confrontation: a threshold that shouldn't exist

Shine light on a clean metal surface and electrons come off. That much was known. What Philipp Lenard reported in 1902 was the part that had no business happening: the kinetic energy of the ejected electrons depended on the *frequency* of the light, not its *intensity*. A blindingly bright red beam — enormous power per unit area — produced no electrons at all from certain metals, while a feeble ultraviolet beam produced them instantly.

Classical wave theory insists intensity should matter. A brighter wave delivers more energy per second, so a bound electron ought to be able to accumulate enough to escape, given time. The time never comes; the threshold is sharp. The classical picture fails three ways at once: wrong variable (frequency, not intensity), wrong threshold behavior (a sharp cutoff, not a gradual onset), wrong scaling (kinetic energy linear in frequency above threshold, not in intensity).

Einstein's 1905 paper proposed that light itself arrives in indivisible energy packets — photons — each carrying energy $E = h\nu$. An electron bound to the metal with binding energy $\phi$ (the work function, a property of the metal) absorbs one photon. If $h\nu > \phi$, it escapes with kinetic energy:

$$K_{\max} = h\nu - \phi.$$

Below the threshold frequency $\nu_0 = \phi/h$, nothing emerges no matter how intense the beam. Above it, intensity sets how many electrons come out per second; frequency sets how much energy each one carries.

![Stopping potential V_s vs](../images/01-why-quantum-mechanics-fig-02.png)
*Figure 1.2 — Stopping potential V_s vs*

Robert Millikan spent four years (1912–1916) trying to demolish this. He measured the stopping potential $V_s$ — the retarding voltage that just halts the most energetic electrons, so $eV_s = K_{\max}$ — against frequency. Einstein's equation predicts a slope of $h/e$. Millikan got $h = 6.57 \times 10^{-27}$ erg·s — within 0.5% of Planck's blackbody value, extracted from an entirely unrelated experiment. He published it while conceding that the equation worked even though he still regarded the hypothesis behind it as "untenable." The data did not care about his convictions.

**A worked example.** Sodium has work function $\phi \approx 2.36$ eV (NIST clean-surface value; see references). The threshold wavelength is:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240 \, \text{eV·nm}}{2.36 \, \text{eV}} \approx 525 \, \text{nm}.$$

Green light. Illuminate instead with $\lambda = 400$ nm (violet). The photon energy is $h\nu = 1240/400 = 3.10$ eV, so the most energetic photoelectron leaves with:

$$K_{\max} = 3.10 \, \text{eV} - 2.36 \, \text{eV} = 0.74 \, \text{eV}.$$

A retarding voltage of 0.74 V stops it cold.

The lesson: one photon, one electron. Energy arrives in indivisible packets; the threshold is sharp because a packet either carries enough or it doesn't; intensity sets the rate, not the energy per electron.

---

## The third confrontation: the wrong color comes back

In 1923, Arthur Holly Compton, at Washington University, scattered X-rays off graphite and measured the wavelength of the scattered radiation as a function of angle. The classical prediction — Thomson scattering — has the electron oscillating at the driving frequency and re-radiating at the *same* frequency. No wavelength shift; just a redistribution in angle.

Compton found a shift. The scattered X-rays came out longer in wavelength than the incident ones, by an amount that depended only on the scattering angle $\theta$:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The combination $h/m_e c = 2.426 \times 10^{-12}$ m is the Compton wavelength of the electron. The shifts are tiny — picometers — but unmistakable and perfectly reproducible.

The derivation is the cleanest piece of mathematics in this chapter. Treat the photon as a relativistic particle with energy $E_\gamma = h\nu$ and momentum $p_\gamma = h/\lambda$. The electron starts at rest. Write down conservation of energy and conservation of momentum (two components), then eliminate the electron's recoil angle.

![Compton scattering geometry ](../images/01-why-quantum-mechanics-fig-03.png)
*Figure 1.3 — Compton scattering geometry *

*Conservation of energy:*
$$h\nu + m_e c^2 = h\nu' + E_e.$$

*Conservation of momentum:*
$$\frac{h\nu}{c} = \frac{h\nu'}{c}\cos\theta + p_e \cos\phi, \qquad 0 = \frac{h\nu'}{c}\sin\theta - p_e \sin\phi.$$

Solve for $p_e \cos\phi$ and $p_e \sin\phi$, square and add to kill $\phi$:

$$p_e^2 c^2 = (h\nu)^2 - 2(h\nu)(h\nu')\cos\theta + (h\nu')^2.$$

From energy conservation, $E_e = h(\nu - \nu') + m_e c^2$, and the relativistic relation $E_e^2 = p_e^2 c^2 + (m_e c^2)^2$ gives:

$$p_e^2 c^2 = h^2(\nu - \nu')^2 + 2m_e c^2 h(\nu - \nu').$$

Set the two expressions equal, expand $(h\nu - h\nu')^2$ on the left, cancel the common terms, divide by $2(h\nu)(h\nu')$:

$$\frac{m_e c^2(\nu - \nu')}{\nu\nu'} = 1 - \cos\theta.$$

Since $(\nu - \nu')/(\nu\nu') = (\lambda' - \lambda)/c$:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

Half a page of algebra, and no quantum mechanics beyond treating the photon as a relativistic particle with $E = h\nu$ and $p = h/\lambda$.

**In Compton's original experiment** he used molybdenum Kα X-rays at $\lambda = 0.0711$ nm. At $\theta = 90°$, $\cos\theta = 0$, so $\Delta\lambda = h/m_e c = 2.43$ pm. He measured 2.23 pm. That agreement was the moment the photon picture became impossible to avoid.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The lesson: the photon carries momentum $h/\lambda$. Planck quantized energy exchange; Einstein quantized the field; Compton quantized the momentum, finishing the photon off as a fully relativistic particle.

---

## The fourth confrontation: the electron as a wave

If light — conventionally a wave — behaves like a particle, the symmetric question is unavoidable: does matter — conventionally made of particles — behave like a wave?

Louis de Broglie's 1924 doctoral thesis at the University of Paris said it does. He proposed that a particle with momentum $p$ has an associated wavelength:

$$\lambda = \frac{h}{p}.$$

The same relation that holds for the photon, now turned loose on matter.

The numbers are the point. A 1 kg cricket ball at 1 m/s has $\lambda = 6.6 \times 10^{-34}$ m — twenty orders of magnitude smaller than a proton, and beyond the reach of any conceivable experiment. An electron accelerated through 54 V, by contrast, has a kinetic energy of 54 eV and a de Broglie wavelength of about 0.17 nm — comparable to the spacing of planes in a crystal. So an electron beam aimed at a crystal ought to diffract, exactly as X-rays do.

Clinton Davisson and Lester Germer, at Bell Labs, saw it in 1927. They scattered 54 eV electrons off a nickel crystal and found a sharp diffraction peak right where Bragg's condition put it.

**The calculation.** An electron through $V = 54$ V has kinetic energy $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Its momentum:

$$p = \sqrt{2m_e K} = \sqrt{2(9.11 \times 10^{-31})(8.65 \times 10^{-18})} \approx 3.97 \times 10^{-24} \, \text{kg·m/s}.$$

De Broglie wavelength:

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10} \, \text{m} = 0.167 \, \text{nm}.$$

Nickel's (111) surface plane spacing is $d = 0.215$ nm. The surface diffraction condition $\lambda = d\sin\phi$ gives $\sin\phi = 0.167/0.215 = 0.777$, so $\phi = 51°$. They measured 50°. One degree off.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The single-electron version came later, built up dot by dot by Akira Tonomura's group at Hitachi in 1989. Electrons arrived one at a time, each landing as a single point on the detector. Accumulated over hours, the points assembled themselves into a diffraction pattern. A lone electron, with no other electron anywhere near it to interfere with, produced interference. There is no classical reading of this. The electron "interferes with itself," and Newtonian language simply has no word for it.

![Tonomura buildup sequence ](../images/01-why-quantum-mechanics-fig-04.png)
*Figure 1.4 — Tonomura buildup sequence *

The lesson: matter has wave properties, and they are not about the particle's *size*. The wavelength belongs to the associated amplitude, not to any physical extent. When the electron is detected, it shows up as a point; the wave appears only in the statistical pattern built from many such points.

---

## The fifth confrontation: energy levels are real

In 1914, James Franck and Gustav Hertz accelerated electrons through mercury vapor and measured the current reaching a collector as a function of accelerating voltage. The current rose steadily, then dropped sharply at 4.9 V. It rose again, then dropped at 9.8 V. And again at 14.7 V — regular dips, spaced exactly 4.9 V apart.

The interpretation: an electron with less than 4.9 eV bounces off mercury atoms elastically, loses nothing, and reaches the collector. At 4.9 eV it can hand over that exact amount, kicking a mercury atom from its ground state to its first excited state — and then, drained, it lacks the energy to reach the collector against the retarding field, hence the drop. Add more voltage and the electron recovers enough to get through, until at 9.8 eV it has enough to excite two mercury atoms in succession.

![Franck–Hertz current vs](../images/01-why-quantum-mechanics-fig-05.png)
*Figure 1.5 — Franck–Hertz current vs*

If that reading is right, the excited mercury atoms must decay back to the ground state by emitting photons of energy 4.9 eV. The wavelength:

$$\lambda = \frac{hc}{E} = \frac{1240 \, \text{eV·nm}}{4.9 \, \text{eV}} \approx 253 \, \text{nm}.$$

Franck and Hertz built a spectroscope and saw a sharp emission line at 253.7 nm whenever the accelerating voltage cleared 4.9 V. Two completely independent probes — the electron's stopping voltage and the photon's wavelength — returned the same energy for the same atomic transition. The energy levels are real.

This is the direct evidence for discrete internal energy structure in atoms. Spectroscopy — the Balmer series, the Lyman series — was already on the books, but spectroscopy is indirect: you see the emitted photons and infer the levels backward. Franck–Hertz is direct. You watch the electron lose exactly 4.9 eV in a collision, and then you watch the photon come out at exactly the predicted wavelength.

---

## What the five experiments require

After 1927, any theory hoping to replace classical physics had to swallow five specific, quantitative facts:

1. Energy exchange between matter and the radiation field happens in discrete units of $h\nu$ (Planck, 1900).
2. The electromagnetic field carries energy in indivisible packets of $h\nu$ (Einstein, 1905).
3. Those packets carry momentum $h/\lambda$ (Compton, 1923).
4. Matter has wave properties, with wavelength $h/p$ (de Broglie, 1924; Davisson–Germer, 1927).
5. Atomic systems have discrete internal energy levels (Franck–Hertz, 1914).

| experiment | year | classical prediction | observed result | formula forced |
| --- | --- | --- | --- | --- |
| Blackbody radiation | 1900 | Continuous energy exchange; ultraviolet catastrophe | Spectrum has a finite peak | $E=h\nu$ |
| Photoelectric effect | 1905 | Bright enough light ejects electrons at any frequency | Emission has a threshold frequency | $K_\text{max}=h\nu-\phi$ |
| Compton scattering | 1923 | Light wave transfers energy but has no particle momentum | X-ray wavelength shifts by angle | $\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$ |
| Matter waves | 1924-1927 | Electrons are particles with no diffraction wavelength | Electron beams diffract from crystals | $\lambda=h/p$ |
| Franck-Hertz | 1914 | Collisions transfer arbitrary energies | Mercury atoms absorb discrete 4.9 eV packets | $\Delta E=h\nu$ |

Three structural demands follow. The new theory needs a *probabilistic* account of measurement: you cannot say where a single electron in a diffraction experiment will land, only how the landings distribute in the long run. It needs *wave-equation structure*, to carry interference and de Broglie wavelengths. And it needs *eigenvalue structure*, to carry discrete energy levels.

The chapters ahead build those three structures. The mathematics is the theory of operators on complex vector spaces, plus the wave equation that governs how quantum amplitudes evolve in time. The five experiments above are the constraints; what follows is the theory built to satisfy them.

Before you go on, notice one thing. Planck's constant $h$ sits inside all five relations. The Compton shift, the de Broglie wavelength, the photoelectric threshold, the Planck distribution — every one of them carries $h$, and in every case it is the same $h$, $6.626 \times 10^{-34}$ J·s, pulled out of independent experiments with nothing in common. That is not a coincidence. That is a constant of nature, marking the scale at which classical descriptions give out. If you want to understand *why* quantum mechanics looks the way it does, start there: it is the theory forced into existence by one number and its stubborn appearance in every one of these five confrontations.

---

## Exercises

**Warm-up**

**W1.** Write down the five key formulas from this chapter from memory: the Planck distribution, the photoelectric equation, the Compton shift, the de Broglie relation, and the Franck–Hertz threshold condition. For each, name the one quantity that makes it non-classical — the quantity that goes to zero in the classical limit. *(Tests recall and the classical-limit intuition built throughout the chapter.)*

**W2.** A photon has wavelength 620 nm (red light). Compute its frequency, energy in joules, and energy in eV. Use $E[\text{eV}] \cdot \lambda[\text{nm}] = 1240$ to check your answer. *(Direct application of $E = h\nu$; builds fluency with the 1240 eV·nm shortcut used throughout.)*

**W3.** At what scattering angle $\theta$ does the Compton shift reach its maximum value? What is that maximum shift in picometers? *(Direct substitution into $\Delta\lambda = (h/m_e c)(1-\cos\theta)$; tests whether the student sees that the formula's maximum is a geometric fact.)*

**Application**

**A1.** Copper has work function $\phi = 4.65$ eV. (a) Find the threshold wavelength for photoemission. (b) Light of wavelength 200 nm strikes the surface. Find the maximum kinetic energy of the ejected electrons and the stopping voltage required to halt them. (c) The intensity of the 200 nm beam is doubled. What changes? *(Part (c) is the trap: intensity changes the rate of ejection, not the energy per electron. Tests whether the student has genuinely internalized the one-photon-one-electron picture.)*

**A2.** An electron is accelerated through 150 V. (a) Compute its de Broglie wavelength using the non-relativistic relation $p = \sqrt{2m_e K}$. (b) After computing, check whether the non-relativistic approximation is justified: compare $K$ to $m_e c^2 = 511$ keV. (c) A crystal with interplanar spacing $d = 0.20$ nm is used as a diffraction target. Predict the angle of the first-order diffraction peak. *(Combines §4.4 calculation with a built-in sanity check on the approximation; the approximation check is a habit worth training early.)*

**A3.** In a Franck–Hertz experiment with neon gas, the periodic current dips are observed at 18.7 V, 37.4 V, and 56.1 V. (a) What is the energy of neon's first excited state above the ground state? (b) Predict the wavelength of the photon emitted when the excited neon atom returns to its ground state. In what part of the electromagnetic spectrum does this fall? *(Transfers the mercury analysis to a new element; the wavelength result — visible orange-red — is a satisfying check since neon signs glow that color.)*

**Synthesis**

**S1.** Millikan's photoelectric measurements gave $h = 6.57 \times 10^{-27}$ erg·s. Planck's blackbody fit gave $h = 6.55 \times 10^{-27}$ erg·s. These two experiments involve completely different physical systems — one is about radiation emitted by a hot cavity, the other is about electrons ejected from a metal surface. Write two or three sentences explaining why the agreement of these values is significant, and what it would mean for Einstein's photon hypothesis if the two values had differed by 20%. *(Tests synthesis of §4.1 and §4.2; the counterfactual forces the student to reason about what the constant $h$ actually represents.)*

**S2.** The Tonomura experiment (1989) sent electrons through a double slit one at a time. After 100 electrons, the detector showed random-looking dots. After 70,000 electrons, a clear interference pattern had built up. (a) What does this result rule out as an explanation for diffraction — specifically, what classical mechanism cannot account for it? (b) The de Broglie wavelength of each electron was 0.05 nm. The slit separation was 300 nm. Using the double-slit formula $d\sin\theta = n\lambda$, predict the angle to the first bright fringe. (c) If the electrons were replaced by protons with the same kinetic energy, would the fringe spacing increase, decrease, or stay the same? Justify your answer with a calculation. *(Integrates §4.4 wave-particle reasoning with a quantitative prediction and a comparison that requires understanding what $\lambda = h/p$ actually depends on.)*

**Challenge**

**C1.** In Compton's original experiment, he observed two peaks in the scattered X-ray spectrum at each angle: one at the incident wavelength $\lambda$ (unshifted) and one at $\lambda' = \lambda + \Delta\lambda$ (shifted). The unshifted peak is not predicted by the photon-billiard-ball derivation in §4.3. Propose a physical mechanism that produces the unshifted peak — your explanation should be consistent with the conservation-law framework in §4.3 and should identify what is different about the scattering event that leaves $\lambda$ unchanged. *(Goes beyond the chapter's explicit content; the answer involves scattering off the nucleus rather than a free electron, so the recoiling mass is ~20,000× larger, making $\Delta\lambda$ negligible. Tests whether the student can reason from the formula rather than just apply it.)*

---

## LLM Exercises

**LLM-E1.** Ask a language model to explain the "ultraviolet catastrophe" to you as if you have no background in physics. Then ask it to explain it to you as a physicist. Compare the two explanations: what did it add, what did it simplify, and what did it get wrong or imprecise in each version? Identify one place in each explanation where the model substituted a metaphor for a mechanism.

**LLM-E2.** Paste the Compton scattering derivation from this chapter into a language model and ask it to verify each algebraic step. Where does it agree, where does it flag an error (real or hallucinated), and where does it skip steps without warning? Then ask it to redo the derivation in a different notation (using wavelengths $\lambda, \lambda'$ throughout instead of frequencies). Evaluate whether the result is mathematically equivalent.

**LLM-E3.** Describe the Davisson–Germer experiment to a language model — the 54 V electrons, the nickel crystal, the measured angle of 50° — and ask it to reconstruct the calculation predicting the diffraction angle. Then ask it to explain what the result would mean if the measured angle had been 35° instead of 50°. Evaluate the quality of its physical reasoning, not just its arithmetic.

**LLM-E4.** Ask a language model: "Did Planck quantize light in 1900?" Evaluate the response for precision. The historically and physically correct answer is narrow: he quantized the energy *exchange* between oscillators in the cavity walls and the radiation field, not the field itself. Then ask it to distinguish Planck's 1900 quantization from Einstein's 1905 quantization. Does it maintain the distinction, or does it collapse them?

**LLM-E5.** Give a language model this prompt: "The Franck–Hertz experiment proves the Bohr model." Ask it to evaluate the claim. A strong response should accept what the experiment actually establishes (discrete energy levels in mercury, with the first at 4.9 eV) while distinguishing this from what the Bohr model claims (a specific orbital structure predicting hydrogen's level spacings). Evaluate whether the model draws that line correctly.

---

## References

*Added by fact-check pass 2026-05-14. See `factchecks/01-why-quantum-mechanics-assertions.md` for the verification trail.*

1. Planck, M. "Zur Theorie des Gesetzes der Energieverteilung im Normalspektrum." *Verhandlungen der Deutschen Physikalischen Gesellschaft* 2, 237–245 (1900).
2. Ehrenfest, P. "Welche Züge der Lichtquantenhypothese spielen in der Theorie der Wärmestrahlung eine wesentliche Rolle?" *Annalen der Physik* 36, 91–118 (1911). https://doi.org/10.1002/andp.19113411106
3. Lenard, P. "Über die lichtelektrische Wirkung." *Annalen der Physik* 8, 149–198 (1902). https://doi.org/10.1002/andp.19023130510
4. Einstein, A. "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17, 132–148 (1905).
5. Millikan, R. A. "A Direct Photoelectric Determination of Planck's h." *Physical Review* 7, 355–388 (1916). https://journals.aps.org/pr/abstract/10.1103/PhysRev.7.355
6. Compton, A. H. "A Quantum Theory of the Scattering of X-rays by Light Elements." *Physical Review* 21, 483–502 (1923). https://journals.aps.org/pr/abstract/10.1103/PhysRev.21.483
7. de Broglie, L. *Recherches sur la théorie des quanta*. Ph.D. thesis, Université de Paris (1924); Ann. de Physique 3, 22–128 (1925).
8. Davisson, C. & Germer, L. H. "Diffraction of Electrons by a Crystal of Nickel." *Physical Review* 30, 705–740 (1927). https://link.aps.org/doi/10.1103/PhysRev.30.705
9. Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T. & Ezawa, H. "Demonstration of single-electron buildup of an interference pattern." *American Journal of Physics* 57, 117–120 (1989). https://doi.org/10.1119/1.16104
10. Franck, J. & Hertz, G. "Über Zusammenstöße zwischen Elektronen und den Molekülen des Quecksilberdampfes und die Ionisierungsspannung desselben." *Verhandlungen der Deutschen Physikalischen Gesellschaft* 16, 457–467 (1914).
11. NIST CODATA 2018. "Fundamental Physical Constants." https://physics.nist.gov/cuu/Constants/
