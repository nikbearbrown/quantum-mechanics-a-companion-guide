# Chapter 1 — Why Quantum Mechanics?

## TL;DR

- The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.
- The chapter moves through The first confrontation: infinite energy in a box, The second confrontation: a threshold that shouldn't exist, The third confrontation: the wrong color comes back, The fourth confrontation: the electron as a wave, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.*

---

Consider the mood of physics as the nineteenth century closed. Its leading figures had reason to feel that the edifice was nearly complete. Newton had given them mechanics; Maxwell had unified electricity, magnetism, and light into a single set of equations; Boltzmann had reduced heat to the statistics of moving molecules; Clausius had codified thermodynamics. The architecture stood. What remained, many supposed, was maintenance — measuring the known constants to one more decimal place.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

Those extra decimal places opened onto a different universe.

The crisis, when it came, was not a matter of interpretation or taste. It was a matter of numbers. The four pillars of classical physics, taken together, made sharp predictions about how light and matter ought to behave. As long as experiments stayed in familiar territory the predictions held. But when the experimentalists pressed into the extremes — the shortest wavelengths, the faintest beams, the most exacting spectroscopy — the theory did not merely err by a margin. It returned infinities where the laboratory returned tidy finite peaks. It promised smooth, gradual behavior where the laboratory delivered abrupt thresholds. And it had no vocabulary whatsoever for results that were crisp, repeatable, and unlike anything in the classical canon.

The damage was done by a handful of experiments strung across roughly a quarter century. I want to take them one at a time and show, in each case, the equation the universe forced into existence — not as a museum tour through history, but as a running argument between an elegant theory and a world that refused to cooperate.

---

## The first confrontation: infinite energy in a box

Begin with the plainest of objects: a hollow metal box, its walls held at a single fixed temperature. The walls glow. They pour out electromagnetic radiation, which ricochets inside until it settles into thermal equilibrium with the walls themselves. The question physicists asked was modest. Across all the available frequencies, how is the trapped energy shared out?

Classical statistical mechanics answered without hesitation. Each electromagnetic mode the cavity can support — and there are endlessly many, since nothing forbids a mode of arbitrarily high frequency — collects, on average, the energy $k_B T$ that the equipartition theorem assigns it. Count how many modes fall in a frequency slice $[\nu, \nu + d\nu]$. There are $8\pi\nu^2/c^3$ of them per unit volume. Multiply by $k_B T$:

$$\rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T.$$

![Plot of Rayleigh–Jeans vs](../images/01-why-quantum-mechanics-fig-01.png)
*Figure 1.1 — Plot of Rayleigh–Jeans vs*

Read that formula and watch it climb. As the frequency rises it grows without limit, and the total energy, $\int_0^\infty \rho_{\text{RJ}} \, d\nu$, diverges outright. Taken seriously, the result says a box sitting at room temperature should hold an infinite store of energy in its short-wavelength modes. Paul Ehrenfest would later fix a name to the absurdity: the "ultraviolet catastrophe."

Out in the laboratory there was no catastrophe — only a curve waiting for an explanation. At the Physikalisch-Technische Reichsanstalt in Berlin, Otto Lummer and Ernst Pringsheim spent the late 1890s measuring blackbody spectra to a precision that left little room for doubt. What they found rose to a finite peak at a characteristic frequency and then fell away exponentially toward the high frequencies. Nature drew a shape, and the shape demanded a theory.

Max Planck supplied one, presenting his fit on 14 December 1900. The Planck distribution is:

$$\rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}.$$

The constant $h$ he fitted to the data: $6.55 \times 10^{-27}$ erg·s, within 1% of today's value $h = 6.626 \times 10^{-34}$ J·s.

Here is the move that bought him the curve. Imagine the oscillators in the cavity walls — the atoms absorbing and re-emitting radiation — barred from trading energy with the field in a continuous stream. Suppose instead that they can only hand over or take in energy in discrete lumps of size $h\nu$, in whole multiples of a single quantum. Then the average thermal energy of an oscillator at frequency $\nu$ is no longer the equipartition value $k_B T$ but:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}}.$$

Let $x = e^{-h\nu/k_B T}$. The numerator is $h\nu \sum n x^n = h\nu \cdot x/(1-x)^2$; the denominator is $\sum x^n = 1/(1-x)$. Dividing:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_B T} - 1}.$$

Trace the two limits and the whole story falls out. When the frequency is low, $h\nu \ll k_B T$, and $e^{h\nu/k_B T} - 1 \approx h\nu/k_B T$, so $\langle E \rangle \to k_B T$ — the old equipartition answer reappears, exactly where it always worked. When the frequency is high, $h\nu \gg k_B T$, and $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$ — crushed exponentially. The catastrophe simply evaporates. Multiply this average by the unchanged classical mode-counting density $8\pi\nu^2/c^3$, and Planck's distribution stands before you.

One subtlety has to be honored before we move on, because the history is regularly mangled here. Planck did not quantize light. What he quantized was the energy *exchange* between the cavity walls and the radiation field. In his 1900 picture the radiation remained a continuous electromagnetic wave; the discrete packets resided in the walls, never in the field itself. It was Einstein, five years on, who would dare to put the packets into the field.

---

## The second confrontation: a threshold that shouldn't exist

Shine light on a clean metal surface and electrons fly off. That much was old news. What Philipp Lenard reported in 1902 was the detail no one had bargained for: the kinetic energy of the escaping electrons tracked the *frequency* of the light, not its *intensity*. A blazing red beam, dumping enormous power onto every square centimeter, could fail to dislodge a single electron from certain metals. A feeble ultraviolet beam pried them loose at once.

Classical wave theory insists that intensity should be what counts. A brighter wave pours in more energy each second, so an electron clinging to the metal ought to be able to soak up enough, given patience, to break free. The patience never pays off. The threshold is a clean edge. Three classical expectations fail at once: the wrong variable governs the result (frequency, not intensity), the threshold is a sharp cutoff rather than a gentle ramp, and the kinetic energy above threshold scales linearly with frequency rather than with intensity.

Einstein's 1905 paper proposed the cure that nobody wanted: light itself arrives in indivisible packets of energy — photons — each carrying $E = h\nu$. An electron bound to the metal by an energy $\phi$ (the work function, a fixed property of the metal) swallows one photon. If $h\nu > \phi$, the electron escapes with kinetic energy:

$$K_{\max} = h\nu - \phi.$$

Below the threshold frequency $\nu_0 = \phi/h$, no electrons emerge no matter how fierce the beam. Above it, intensity sets only how many electrons leave each second; frequency sets how much energy each one carries away.

![Stopping potential V_s vs](../images/01-why-quantum-mechanics-fig-02.png)
*Figure 1.2 — Stopping potential V_s vs*

Robert Millikan set out, over four years from 1912 to 1916, to demolish this idea. He measured the stopping potential $V_s$ — the retarding voltage that just arrests the most energetic electrons, so that $eV_s = K_{\max}$ — against frequency. Einstein's equation makes the slope of that line exactly $h/e$. Millikan's careful work returned $h = 6.57 \times 10^{-27}$ erg·s — within half a percent of the value Planck had wrung from blackbody radiation, an entirely separate experiment. He published the confirmation while still insisting that the hypothesis behind it was, in his judgment, untenable.

**A worked example.** Sodium has work function $\phi \approx 2.36$ eV (NIST clean-surface value; see references). The threshold wavelength is:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240 \, \text{eV·nm}}{2.36 \, \text{eV}} \approx 525 \, \text{nm}.$$

That's green light. Illuminate with $\lambda = 400$ nm (violet). Photon energy $h\nu = 1240/400 = 3.10$ eV. The most energetic photoelectron leaves with:

$$K_{\max} = 3.10 \, \text{eV} - 2.36 \, \text{eV} = 0.74 \, \text{eV}.$$

A retarding voltage of 0.74 V stops it exactly.

The moral is compact: one photon, one electron. Energy comes in indivisible portions; the threshold is sharp because a portion either suffices or it does not; and intensity governs the rate of emission, never the energy carried by each electron.

---

## The third confrontation: the wrong color comes back

In 1923, Arthur Holly Compton, working at Washington University, fired X-rays at graphite and measured how the wavelength of the scattered radiation depended on the angle of scatter. Classical theory — Thomson scattering — said the electron should oscillate at the incoming frequency and re-radiate at that *same* frequency. No shift in wavelength was permitted; only a redistribution of the radiation across angles.

Compton found a shift. The scattered X-rays emerged longer in wavelength than the incident ones, by an amount that depended on nothing but the angle $\theta$:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The combination $h/m_e c = 2.426 \times 10^{-12}$ m is called the Compton wavelength of the electron. The shifts run to mere picometers — small, but sharp, and perfectly reproducible.

The derivation is the tidiest piece of mathematics in the chapter. Treat the photon as a relativistic particle carrying energy $E_\gamma = h\nu$ and momentum $p_\gamma = h/\lambda$. Take the electron to be at rest before the collision. Write conservation of energy and of momentum (in two components), then eliminate the electron's recoil angle.

![Compton scattering geometry ](../images/01-why-quantum-mechanics-fig-03.png)
*Figure 1.3 — Compton scattering geometry *

*Conservation of energy:*
$$h\nu + m_e c^2 = h\nu' + E_e.$$

*Conservation of momentum:*
$$\frac{h\nu}{c} = \frac{h\nu'}{c}\cos\theta + p_e \cos\phi, \qquad 0 = \frac{h\nu'}{c}\sin\theta - p_e \sin\phi.$$

Solve for $p_e \cos\phi$ and $p_e \sin\phi$, square and add to eliminate $\phi$:

$$p_e^2 c^2 = (h\nu)^2 - 2(h\nu)(h\nu')\cos\theta + (h\nu')^2.$$

From energy conservation, $E_e = h(\nu - \nu') + m_e c^2$, and the relativistic relation $E_e^2 = p_e^2 c^2 + (m_e c^2)^2$ gives:

$$p_e^2 c^2 = h^2(\nu - \nu')^2 + 2m_e c^2 h(\nu - \nu').$$

Set equal and expand $(h\nu - h\nu')^2$ on the left, cancel common terms, divide by $2(h\nu)(h\nu')$:

$$\frac{m_e c^2(\nu - \nu')}{\nu\nu'} = 1 - \cos\theta.$$

Since $(\nu - \nu')/(\nu\nu') = (\lambda' - \lambda)/c$:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

Half a page of algebra, and no quantum mechanics beyond the single assumption that the photon is a relativistic particle with $E = h\nu$ and $p = h/\lambda$.

**In Compton's original experiment** he used molybdenum Kα X-rays at $\lambda = 0.0711$ nm. At $\theta = 90°$, $\cos\theta = 0$, so $\Delta\lambda = h/m_e c = 2.43$ pm. He measured 2.23 pm. The agreement was the moment the photon picture became unavoidable.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The moral builds on the last two: the photon carries momentum $h/\lambda$. Planck had quantized energy exchange; Einstein had quantized the field; now Compton quantized the momentum, finishing the photon as a fully relativistic particle.

---

## The fourth confrontation: the electron as a wave

If light, the textbook wave, could be caught behaving as a particle, the mirror-image question almost asks itself: can matter, the textbook collection of particles, be caught behaving as a wave?

Louis de Broglie's 1924 doctoral thesis at the University of Paris answered yes. He proposed that a particle carrying momentum $p$ has a wavelength riding along with it:

$$\lambda = \frac{h}{p}.$$

The very same relation that held for the photon, now turned loose on matter.

Run the numbers and you see at once why nobody had stumbled on this before. A 1 kg cricket ball moving at 1 m/s carries $\lambda = 6.6 \times 10^{-34}$ m — twenty orders of magnitude below the size of a proton, beyond the reach of any conceivable instrument. An electron accelerated through 54 V is a different matter entirely: kinetic energy 54 eV, de Broglie wavelength about 0.17 nm, right in the range of the spacing between crystal planes. So an electron beam fired at a crystal ought to diffract, exactly as X-rays do.

Clinton Davisson and Lester Germer, at Bell Labs, caught it in 1927. They bounced 54 eV electrons off a nickel crystal and watched a sharp diffraction peak appear at precisely the angle Bragg's condition demands.

**The calculation.** An electron through $V = 54$ V has kinetic energy $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Its momentum:

$$p = \sqrt{2m_e K} = \sqrt{2(9.11 \times 10^{-31})(8.65 \times 10^{-18})} \approx 3.97 \times 10^{-24} \, \text{kg·m/s}.$$

De Broglie wavelength:

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10} \, \text{m} = 0.167 \, \text{nm}.$$

Nickel's (111) surface plane spacing is $d = 0.215$ nm. The surface diffraction condition gives $\lambda = d\sin\phi$, so $\sin\phi = 0.167/0.215 = 0.777$, $\phi = 51°$. They measured 50°. Agreement to within one degree.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The starkest version of the result waited until 1989, when Akira Tonomura's group at Hitachi recorded the pattern building up one electron at a time. The electrons arrived singly, each leaving a single point on the detector. Left to accumulate over hours, those points assembled themselves into a diffraction pattern. A lone electron, with no companions present to push against, produced interference. No Newtonian sentence can describe this. The electron "interferes with itself," and the phrase has no counterpart in the older language.

![Tonomura buildup sequence ](../images/01-why-quantum-mechanics-fig-04.png)
*Figure 1.4 — Tonomura buildup sequence *

The moral is easy to misstate, so state it carefully: matter has wave properties, and those properties say nothing about the particle's *size*. The wavelength belongs to the associated amplitude, not to any physical extent. When the electron is detected it shows up as a point. The wave reveals itself only in the statistical pattern that emerges from many detections.

---

## The fifth confrontation: energy levels are real

In 1914, James Franck and Gustav Hertz drove electrons through mercury vapor and measured the current arriving at a collector as they raised the accelerating voltage. The current climbed steadily, then plunged at 4.9 V. It climbed once more, then plunged again at 9.8 V. And again at 14.7 V. Regular dips, spaced exactly 4.9 V apart.

The reading of the data is clean. An electron carrying less than 4.9 eV bounces off the mercury atoms elastically, surrendering no energy, and sails on to the collector. At 4.9 eV it can deliver that precise amount to a mercury atom, lifting the atom from its ground state into its first excited state. Stripped of its energy, the electron can no longer fight its way to the collector against the retarding field — and the current drops. Crank the voltage higher and the electron recovers enough energy to reach the collector again, until at 9.8 eV it can excite two mercury atoms one after the other.

![Franck–Hertz current vs](../images/01-why-quantum-mechanics-fig-05.png)
*Figure 1.5 — Franck–Hertz current vs*

If that reading is correct, the excited mercury atoms must fall back to their ground state by emitting photons, and those photons should each carry 4.9 eV. The wavelength:

$$\lambda = \frac{hc}{E} = \frac{1240 \, \text{eV·nm}}{4.9 \, \text{eV}} \approx 253 \, \text{nm}.$$

Franck and Hertz built a spectroscope and saw exactly that — a sharp emission line at 253.7 nm appearing whenever the accelerating voltage climbed past 4.9 V. Two wholly independent probes — the stopping voltage of an electron and the wavelength of a photon — converged on a single energy for a single atomic transition. The levels are not a bookkeeping fiction. They are real.

This is the most direct evidence we have for discrete internal energy structure in atoms. Spectroscopy had long shown such structure — the Balmer series, the Lyman series — but spectroscopy works by inference: you catch the emitted photons and reason backward to the levels. Franck–Hertz is direct. You watch the electron lose exactly 4.9 eV in a single collision, and then you watch the photon depart at exactly the wavelength that loss predicts.

---

## What the five experiments require

By 1927 the constraints were in place. Any theory hoping to supplant classical physics had to swallow five specific, quantitative facts:

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

Three structural demands grow out of these facts. The successor theory needs a *probabilistic* account of measurement: in a diffraction experiment you cannot say where any single electron will land — only how the landings distribute over the long run. It needs *wave-equation structure*, to carry interference and the de Broglie wavelength. And it needs *eigenvalue structure*, to carry discrete energy levels.

The chapters ahead build exactly these structures. The mathematics they require is the theory of operators acting on complex vector spaces, together with the wave equation that governs how quantum amplitudes change in time. The five experiments above set the constraints. What follows is the theory raised to meet them.

Before you turn the page, pause on one thing. Planck's constant $h$ stands in all five relations. The Compton shift, the de Broglie wavelength, the photoelectric threshold, the Planck distribution — every one of them carries $h$, and in every one it is the same $h$, $6.626 \times 10^{-34}$ J·s, pulled out of experiments with nothing in common but the answer. That recurrence is no accident. It is a constant of nature, fixing the scale at which classical descriptions give way. If you want to understand *why* quantum mechanics has the shape it has, begin there: it is the theory compelled into being by this single number and its insistence on appearing in each of these five confrontations.

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
