# Chapter 1 — Why Quantum Mechanics?

## TL;DR

- The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.
- The chapter moves through The first confrontation: infinite energy in a box, The second confrontation: a threshold that shouldn't exist, The third confrontation: the wrong color comes back, The fourth confrontation: the electron as a wave, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.*

---

By 1900, many of the world's leading physicists believed their subject was nearly complete. Newton had supplied mechanics, Maxwell had supplied electrodynamics, Boltzmann had supplied statistical mechanics, and Clausius had supplied thermodynamics. The fundamental laws seemed settled, and the work that remained looked like a matter of refining measurements to a few more decimal places.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

Those decimal places, as we will see, opened onto an entirely different universe.

The difficulty was not a matter of interpretation or philosophy. It was numerical. Classical physics, built on those four pillars, made definite and testable predictions about how matter and light should behave. When experimenters pushed into new regimes — very short wavelengths, very faint beams, very precise spectroscopy — the predictions did more than miss by a little. Where experiments found finite peaks, the theory predicted infinities. Where experiments found sharp cutoffs, the theory predicted smooth, continuous behavior. And the theory had no vocabulary at all for results that were sharp, reproducible, and completely unlike anything it had anticipated.

Five experiments, carried out over roughly a quarter of a century, are what forced the change. In this chapter we will walk through each one and look closely at the mathematics it required. We treat these not as historical anecdotes but as a sequence of confrontations between an elegant theory and a universe that refused to cooperate.

---

## The first confrontation: infinite energy in a box

We begin with a simple setup: a hollow metal box whose walls are held at a fixed temperature. The walls glow, emitting electromagnetic radiation, and that radiation bounces around inside until it reaches thermal equilibrium with the walls. The question we want to answer is how the energy is distributed among the different frequencies.

Classical statistical mechanics gives a clean answer. Each electromagnetic mode in the cavity receives, on average, an energy $k_B T$ from the equipartition theorem, and there are infinitely many modes because the frequency can be arbitrarily high. If we count the modes in a frequency interval $[\nu, \nu + d\nu]$, we find $8\pi\nu^2/c^3$ of them per unit volume. Multiplying by $k_B T$ gives:

$$\rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T.$$

![Plot of Rayleigh–Jeans vs](../images/01-why-quantum-mechanics-fig-01.png)
*Figure 1.1 — Plot of Rayleigh–Jeans vs*

Notice that this expression grows without bound as the frequency increases. The total energy, $\int_0^\infty \rho_{\text{RJ}} \, d\nu$, diverges. Taken literally, a box at room temperature would hold infinite energy in its short-wavelength modes. Paul Ehrenfest later named this failure the "ultraviolet catastrophe."

Meanwhile, experimentalists at the Physikalisch-Technische Reichsanstalt in Berlin — Otto Lummer and Ernst Pringsheim — were measuring blackbody spectra with remarkable precision through the late 1890s. What they saw was a finite peak at a characteristic frequency, followed by an exponential drop at higher frequencies. Nature showed no catastrophe at all. There was simply a curve, and that curve needed an explanation.

Max Planck presented his fit on 14 December 1900. The Planck distribution is:

$$\rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}.$$

He fitted the constant $h$ to the data, obtaining $6.55 \times 10^{-27}$ erg·s, which is within 1% of today's value $h = 6.626 \times 10^{-34}$ J·s.

Let us follow how he arrived at this. Suppose the oscillators in the cavity walls — the atoms absorbing and re-emitting radiation — cannot trade energy continuously with the field. Suppose instead they can exchange energy only in discrete chunks of size $h\nu$, that is, in whole multiples of an energy quantum. Then the average thermal energy of an oscillator at frequency $\nu$ is no longer $k_B T$ (the equipartition result) but rather:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}}.$$

To evaluate this, let $x = e^{-h\nu/k_B T}$. The numerator becomes $h\nu \sum n x^n = h\nu \cdot x/(1-x)^2$, and the denominator becomes $\sum x^n = 1/(1-x)$. Dividing one by the other gives:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_B T} - 1}.$$

We can check the two limits. At low frequencies, where $h\nu \ll k_B T$, we have $e^{h\nu/k_B T} - 1 \approx h\nu/k_B T$, so $\langle E \rangle \to k_B T$ and equipartition is recovered. At high frequencies, where $h\nu \gg k_B T$, we have $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$, which is exponentially suppressed. The catastrophe disappears. Multiplying by the mode-counting density $8\pi\nu^2/c^3$, which is classical and unchanged, returns Planck's distribution.

One point is worth getting straight before we move on. Planck did not quantize light. What he quantized was the energy *exchange* between the cavity walls and the radiation field. In his 1900 picture, the radiation itself was still a continuous electromagnetic wave; the discrete packets lived in the walls, not in the field. It was Einstein's paper five years later that placed the packets in the field itself.

---

## The second confrontation: a threshold that shouldn't exist

Shine light on a clean metal surface and electrons come off. That much was already known. What Philipp Lenard reported in 1902 was the surprising part: the kinetic energy of the ejected electrons depended on the *frequency* of the light rather than on its *intensity*. A very bright red beam, delivering enormous power per unit area, produced no electrons at all from some metals, while a dim ultraviolet beam produced electrons immediately.

Classical wave theory insists that intensity should be what matters. A brighter wave delivers more energy per unit time, so an electron bound to the surface ought to be able to accumulate enough energy to escape if it just waits long enough. But the wait never pays off. The threshold is sharp. The classical picture fails in three ways at once: it identifies the wrong variable (frequency, not intensity), it predicts the wrong threshold behavior (a gradual onset rather than a sharp cutoff), and it predicts the wrong scaling (energy that grows with intensity rather than linearly with frequency above threshold).

Einstein's 1905 paper proposed that light itself arrives in indivisible energy packets — photons — each carrying energy $E = h\nu$. An electron bound to the metal with binding energy $\phi$ (the work function, a property of the metal) absorbs a single photon. If $h\nu > \phi$, the electron escapes with kinetic energy:

$$K_{\max} = h\nu - \phi.$$

Below the threshold frequency $\nu_0 = \phi/h$, no electrons appear no matter how intense the light. Above it, intensity sets how many electrons leave per second, while frequency sets how much energy each one carries.

![Stopping potential V_s vs](../images/01-why-quantum-mechanics-fig-02.png)
*Figure 1.2 — Stopping potential V_s vs*

Robert Millikan spent four years, from 1912 to 1916, trying to disprove this. He measured the stopping potential $V_s$ — the retarding voltage that just halts the most energetic electrons, so that $eV_s = K_{\max}$ — as a function of frequency. By Einstein's equation, the slope of that relationship should be $h/e$. Millikan found $h = 6.57 \times 10^{-27}$ erg·s, within 0.5% of Planck's blackbody value from an entirely different experiment. He published the result while conceding that the photoelectric equation worked even though he remained convinced the hypothesis behind it was "untenable."

**A worked example.** Sodium has work function $\phi \approx 2.36$ eV (NIST clean-surface value; see references). The threshold wavelength is:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240 \, \text{eV·nm}}{2.36 \, \text{eV}} \approx 525 \, \text{nm}.$$

This corresponds to green light. Now illuminate the surface with $\lambda = 400$ nm (violet). The photon energy is $h\nu = 1240/400 = 3.10$ eV, and the most energetic photoelectron leaves with:

$$K_{\max} = 3.10 \, \text{eV} - 2.36 \, \text{eV} = 0.74 \, \text{eV}.$$

A retarding voltage of 0.74 V stops it exactly.

The lesson is one photon, one electron. Energy arrives in indivisible packets; the threshold is sharp because a single packet either has enough energy or it does not; and intensity governs the rate of emission, not the energy carried by each electron.

---

## The third confrontation: the wrong color comes back

In 1923, Arthur Holly Compton, working at Washington University, scattered X-rays off graphite and measured the wavelength of the scattered radiation as a function of angle. The classical prediction, known as Thomson scattering, says the electron oscillates at the driving frequency and re-radiates at that *same* frequency. There should be no wavelength shift, only a redistribution of the radiation in angle.

What Compton found was a shift. The scattered X-rays emerged with longer wavelengths than the incident X-rays, by an amount that depended only on the scattering angle $\theta$:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The combination $h/m_e c = 2.426 \times 10^{-12}$ m is called the Compton wavelength of the electron. The shifts are tiny — on the order of picometers — but they are unmistakable and perfectly reproducible.

The derivation is the cleanest piece of mathematics in this chapter. We treat the photon as a relativistic particle with energy $E_\gamma = h\nu$ and momentum $p_\gamma = h/\lambda$, and we take the electron to be initially at rest. We write down conservation of energy and conservation of momentum (in two components), then eliminate the electron's recoil angle.

![Compton scattering geometry ](../images/01-why-quantum-mechanics-fig-03.png)
*Figure 1.3 — Compton scattering geometry *

*Conservation of energy:*
$$h\nu + m_e c^2 = h\nu' + E_e.$$

*Conservation of momentum:*
$$\frac{h\nu}{c} = \frac{h\nu'}{c}\cos\theta + p_e \cos\phi, \qquad 0 = \frac{h\nu'}{c}\sin\theta - p_e \sin\phi.$$

We solve for $p_e \cos\phi$ and $p_e \sin\phi$, then square and add to eliminate $\phi$:

$$p_e^2 c^2 = (h\nu)^2 - 2(h\nu)(h\nu')\cos\theta + (h\nu')^2.$$

From energy conservation, $E_e = h(\nu - \nu') + m_e c^2$, and the relativistic relation $E_e^2 = p_e^2 c^2 + (m_e c^2)^2$ gives:

$$p_e^2 c^2 = h^2(\nu - \nu')^2 + 2m_e c^2 h(\nu - \nu').$$

Setting the two expressions equal, expanding $(h\nu - h\nu')^2$ on the left, canceling common terms, and dividing by $2(h\nu)(h\nu')$, we get:

$$\frac{m_e c^2(\nu - \nu')}{\nu\nu'} = 1 - \cos\theta.$$

Since $(\nu - \nu')/(\nu\nu') = (\lambda' - \lambda)/c$, this becomes:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

That is about half a page of algebra, using no quantum mechanics beyond treating the photon as a relativistic particle with $E = h\nu$ and $p = h/\lambda$.

**In Compton's original experiment** he used molybdenum Kα X-rays at $\lambda = 0.0711$ nm. At $\theta = 90°$, where $\cos\theta = 0$, the predicted shift is $\Delta\lambda = h/m_e c = 2.43$ pm. He measured 2.23 pm. That agreement was the moment the photon picture became impossible to avoid.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The lesson is that the photon carries momentum $h/\lambda$. Planck had quantized energy exchange, Einstein had quantized the field, and Compton quantized the momentum, completing the picture of the photon as a relativistic particle.

---

## The fourth confrontation: the electron as a wave

If light, which we conventionally think of as a wave, can behave like a particle, then a symmetric question naturally arises: does matter, which we conventionally think of as made of particles, behave like a wave?

Louis de Broglie's 1924 doctoral thesis at the University of Paris answered yes. He proposed that a particle with momentum $p$ has an associated wavelength:

$$\lambda = \frac{h}{p}.$$

This is the same relation that holds for the photon, now carried over to matter.

The numbers are instructive. A 1 kg cricket ball moving at 1 m/s has $\lambda = 6.6 \times 10^{-34}$ m, which is twenty orders of magnitude smaller than a proton. No experiment anywhere could detect such a wavelength. An electron accelerated through 54 V, by contrast, has a kinetic energy of 54 eV and a de Broglie wavelength of roughly 0.17 nm, comparable to the spacing between planes in a crystal lattice. An electron beam aimed at a crystal should therefore diffract, just as X-rays do.

Clinton Davisson and Lester Germer at Bell Labs observed exactly this in 1927. They scattered 54 eV electrons off a nickel crystal and saw a sharp diffraction peak at the angle predicted by Bragg's condition.

**The calculation.** An electron accelerated through $V = 54$ V has kinetic energy $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Its momentum is:

$$p = \sqrt{2m_e K} = \sqrt{2(9.11 \times 10^{-31})(8.65 \times 10^{-18})} \approx 3.97 \times 10^{-24} \, \text{kg·m/s}.$$

The de Broglie wavelength is then:

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10} \, \text{m} = 0.167 \, \text{nm}.$$

Nickel's (111) surface plane spacing is $d = 0.215$ nm. The surface diffraction condition gives $\lambda = d\sin\phi$, so $\sin\phi = 0.167/0.215 = 0.777$ and $\phi = 51°$. They measured 50°, an agreement to within a single degree.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The single-electron version of this experiment was carried out as a continuous buildup by Akira Tonomura's group at Hitachi in 1989. Electrons arrived one at a time, each registering as a single point on the detector. Over the course of hours, those points assembled themselves into a diffraction pattern. A single electron, with no other electrons present to interact with, produced interference. There is no classical way to read this. The electron "interferes with itself" in a way that has no counterpart in Newtonian language.

![Tonomura buildup sequence ](../images/01-why-quantum-mechanics-fig-04.png)
*Figure 1.4 — Tonomura buildup sequence *

The lesson is that matter has wave properties, and those properties are not about the particle's *size*. The wavelength is a property of the associated amplitude, not a physical extent. When the electron is detected, it appears as a single point; the wave reveals itself only in the statistical pattern built up from many detections.

---

## The fifth confrontation: energy levels are real

In 1914, James Franck and Gustav Hertz accelerated electrons through mercury vapor and measured the current reaching a collector as a function of the accelerating voltage. The current rose steadily, then dropped sharply at 4.9 V. It rose again, then dropped at 9.8 V. And again at 14.7 V. The dips were regular, spaced exactly 4.9 V apart.

Here is the interpretation. An electron with kinetic energy below 4.9 eV bounces off mercury atoms elastically, loses no energy, and reaches the collector. At 4.9 eV the electron can hand over that exact amount to a mercury atom, exciting it from its ground state to its first excited state. Having given up its energy, the electron can no longer make it to the collector against the retarding field, which is why the current drops. With more voltage, the electron regains enough energy to reach the collector, until at 9.8 eV it can excite two mercury atoms one after the other.

![Franck–Hertz current vs](../images/01-why-quantum-mechanics-fig-05.png)
*Figure 1.5 — Franck–Hertz current vs*

If this interpretation is correct, the excited mercury atoms should fall back to their ground state by emitting photons, and those photons should carry energy 4.9 eV. The corresponding wavelength is:

$$\lambda = \frac{hc}{E} = \frac{1240 \, \text{eV·nm}}{4.9 \, \text{eV}} \approx 253 \, \text{nm}.$$

Franck and Hertz built a spectroscope and observed a sharp emission line at 253.7 nm whenever the accelerating voltage exceeded 4.9 V. Two completely independent probes — the electron stopping voltage and the photon wavelength — gave the same energy for the same atomic transition. The energy levels are real.

This is the direct evidence for discrete internal energy structure in atoms. Spectroscopy, including the Balmer and Lyman series, was already known, but spectroscopy is indirect: we observe emitted photons and infer the levels backward. Franck–Hertz is direct. We watch the electron lose exactly 4.9 eV in a collision, and then we watch the photon emerge at exactly the predicted wavelength.

---

## What the five experiments require

After 1927, any theory hoping to replace classical physics had to account for five specific, quantitative facts:

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

Three structural requirements follow from these facts. The new theory needs a *probabilistic* account of measurement, because we cannot predict where a single electron in a diffraction experiment will land; we can predict only the long-run distribution. It needs *wave-equation structure* in order to handle interference and de Broglie wavelengths. And it needs *eigenvalue structure* in order to handle discrete energy levels.

The next chapters build those structures. The mathematics we will need is the theory of operators on complex vector spaces, together with the wave equation that governs how quantum amplitudes evolve in time. The five experiments above are the constraints, and what follows is the theory built to meet them.

Before going on, it is worth pausing on one detail. Planck's constant $h$ appears in all five relations. The Compton shift, the de Broglie wavelength, the photoelectric threshold, the Planck distribution — every one of them contains $h$, and in every case it is the same $h$, $6.626 \times 10^{-34}$ J·s, extracted from independent experiments with completely different setups. This is not a coincidence. It is a constant of nature, fixing the scale at which classical descriptions break down. If we want to understand *why* quantum mechanics looks the way it does, this is where we begin: it is the theory forced upon us by the existence of this single number and its appearance in every one of these five confrontations.

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
