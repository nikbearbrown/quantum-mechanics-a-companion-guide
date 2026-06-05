# Chapter 1 — Why Quantum Mechanics?

## TL;DR

- This chapter delivers the five experiments that classical physics could not explain and the five formulas they forced.
- It covers the ultraviolet catastrophe and the Planck distribution, the photoelectric threshold, the Compton shift, matter waves, and the Franck–Hertz energy levels.
- It states each classical prediction, the observed result, the formula required, and the role of Planck's constant $h$ as the common scale.

*The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.*

---

By 1900, classical physics was regarded as essentially complete. Newtonian mechanics, Maxwell's electrodynamics, Boltzmann's statistical mechanics, and Clausius's thermodynamics together covered the known phenomena. The expectation was refinement, not revision.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The refinement turned out to require a new physics.

The failure was quantitative, not philosophical. The four classical pillars made specific, testable predictions about matter and light. In new experimental regimes — very short wavelengths, very weak beams, high-precision spectroscopy — those predictions failed by large margins. They returned infinities where experiments gave finite peaks, continuous threshold behavior where experiments gave sharp cutoffs, and no account at all of results that were sharp, reproducible, and unanticipated.

Five experiments over roughly twenty-five years forced the change. Each is treated below as a constraint on any successor theory, together with the formula it required.

---

## The first confrontation: infinite energy in a box

A hollow metal box with walls at fixed temperature emits electromagnetic radiation, which reaches thermal equilibrium with the walls. The quantity of interest is how the energy is distributed across frequencies.

Classical statistical mechanics gives a definite answer. By equipartition, each electromagnetic mode in the cavity carries average energy $k_B T$, and there are infinitely many modes because frequency is unbounded. The mode count per unit volume in $[\nu, \nu + d\nu]$ is $8\pi\nu^2/c^3$. Multiplying by $k_B T$:

$$\rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T.$$

![Plot of Rayleigh–Jeans vs](../images/01-why-quantum-mechanics-fig-01.png)
*Figure 1.1 — Plot of Rayleigh–Jeans vs*

This rises without bound with frequency, so the total energy $\int_0^\infty \rho_{\text{RJ}} \, d\nu$ diverges. The result is infinite energy in the short-wavelength modes — the "ultraviolet catastrophe," a term due to Paul Ehrenfest.

Measurements at the Physikalisch-Technische Reichsanstalt in Berlin by Otto Lummer and Ernst Pringsheim through the late 1890s showed a finite peak at a characteristic frequency followed by an exponential fall-off. The spectrum had a definite shape requiring explanation.

Max Planck presented his fit on 14 December 1900. The Planck distribution is:

$$\rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}.$$

He fit the constant $h$ to the data: $6.55 \times 10^{-27}$ erg·s, within 1% of the modern value $h = 6.626 \times 10^{-34}$ J·s.

The derivation rests on one assumption: the wall oscillators that absorb and re-emit radiation exchange energy with the field only in discrete units of $h\nu$, not continuously. The average thermal energy of an oscillator at frequency $\nu$ is then not $k_B T$ but:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}}.$$

Set $x = e^{-h\nu/k_B T}$. The numerator is $h\nu \sum n x^n = h\nu \cdot x/(1-x)^2$; the denominator is $\sum x^n = 1/(1-x)$. Dividing:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_B T} - 1}.$$

In the low-frequency limit $h\nu \ll k_B T$, $e^{h\nu/k_B T} - 1 \approx h\nu/k_B T$, so $\langle E \rangle \to k_B T$ and equipartition is recovered. In the high-frequency limit $h\nu \gg k_B T$, $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$, which is exponentially suppressed. The divergence is removed. Multiplying by the unchanged mode density $8\pi\nu^2/c^3$ gives the Planck distribution.

One distinction to keep straight: Planck quantized the energy *exchange* between cavity walls and field, not light itself. In his 1900 picture the radiation remained a continuous electromagnetic wave; the discrete packets resided in the walls. Quantizing the field came five years later, with Einstein.

---

## The second confrontation: a threshold that shouldn't exist

Light on a clean metal surface ejects electrons. The non-classical part, reported by Philipp Lenard in 1902, is that the kinetic energy of the ejected electrons depends on the *frequency* of the light, not its *intensity*. A bright red beam produces no electrons from certain metals; a dim ultraviolet beam produces them immediately.

Classical wave theory predicts the opposite: intensity should govern the energy delivered, and a bound electron should eventually accumulate enough to escape regardless of frequency. It does not. The threshold is sharp. The classical picture fails on three counts at once: wrong controlling variable (frequency, not intensity), wrong threshold behavior (sharp cutoff, not gradual), and wrong scaling (kinetic energy linear in frequency above threshold, not in intensity).

Einstein's 1905 paper proposed that light arrives in indivisible packets — photons — each of energy $E = h\nu$. An electron bound by work function $\phi$ absorbs one photon. If $h\nu > \phi$, it escapes with kinetic energy:

$$K_{\max} = h\nu - \phi.$$

Below the threshold frequency $\nu_0 = \phi/h$, no electrons emerge at any intensity. Above it, intensity sets the emission rate; frequency sets the energy per electron.

![Stopping potential V_s vs](../images/01-why-quantum-mechanics-fig-02.png)
*Figure 1.2 — Stopping potential V_s vs*

Robert Millikan spent 1912–1916 attempting to disprove the relation. He measured the stopping potential $V_s$ — the retarding voltage that halts the most energetic electrons, so $eV_s = K_{\max}$ — versus frequency. The slope is $h/e$. Millikan obtained $h = 6.57 \times 10^{-27}$ erg·s, within 0.5% of Planck's blackbody value from an unrelated experiment. He published the result while maintaining that the underlying hypothesis was "untenable."

**Worked example — photoelectric threshold and stopping voltage for sodium.**

**Given.** Sodium work function $\phi \approx 2.36$ eV (NIST clean-surface value; see references). Incident wavelength $\lambda = 400$ nm (violet). Use $E[\text{eV}] \cdot \lambda[\text{nm}] = 1240$.

**Find.** The threshold wavelength $\lambda_0$, the photon energy, and the maximum photoelectron kinetic energy.

**Solution.** Threshold wavelength:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240 \, \text{eV·nm}}{2.36 \, \text{eV}} \approx 525 \, \text{nm}.$$

Photon energy at 400 nm: $h\nu = 1240/400 = 3.10$ eV. Maximum kinetic energy:

$$K_{\max} = 3.10 \, \text{eV} - 2.36 \, \text{eV} = 0.74 \, \text{eV}.$$

**Check.** $\lambda_0 \approx 525$ nm is green light; the 400 nm beam is below this threshold wavelength and therefore ejects electrons, consistent with $K_{\max} > 0$. A retarding voltage of 0.74 V stops the most energetic electron exactly.

The operative rule: one photon, one electron. Energy arrives in indivisible packets, the threshold is sharp because a packet either suffices or does not, and intensity sets rate rather than energy per electron.

---

## The third confrontation: the wrong color comes back

In 1923, Arthur Holly Compton at Washington University scattered X-rays off graphite and measured the scattered wavelength versus angle. The classical prediction — Thomson scattering — has the electron oscillate at the driving frequency and re-radiate at the *same* frequency, giving no wavelength shift, only an angular redistribution.

Compton measured a shift. The scattered X-rays were longer in wavelength than the incident X-rays by an amount depending only on the angle $\theta$:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The constant $h/m_e c = 2.426 \times 10^{-12}$ m is the Compton wavelength of the electron. The shifts are picometer-scale, small but reproducible.

The derivation treats the photon as a relativistic particle of energy $E_\gamma = h\nu$ and momentum $p_\gamma = h/\lambda$, with the electron initially at rest. Write conservation of energy and momentum and eliminate the electron's recoil angle.

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

Set equal, expand $(h\nu - h\nu')^2$ on the left, cancel common terms, and divide by $2(h\nu)(h\nu')$:

$$\frac{m_e c^2(\nu - \nu')}{\nu\nu'} = 1 - \cos\theta.$$

Since $(\nu - \nu')/(\nu\nu') = (\lambda' - \lambda)/c$:

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The full derivation is about half a page and uses no quantum mechanics beyond the photon relations $E = h\nu$ and $p = h/\lambda$.

**Worked example — Compton shift at 90°.**

**Given.** Compton's incident molybdenum Kα X-rays at $\lambda = 0.0711$ nm, scattering angle $\theta = 90°$.

**Find.** The wavelength shift $\Delta\lambda$.

**Solution.** At $\theta = 90°$, $\cos\theta = 0$, so $\Delta\lambda = h/m_e c = 2.43$ pm.

**Check.** Compton measured 2.23 pm at this angle, in agreement with the prediction. This result established the photon picture.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The operative rule: the photon carries momentum $h/\lambda$. Planck quantized energy exchange, Einstein quantized the field, and Compton established the photon's momentum, completing the photon as a relativistic particle.

---

## The fourth confrontation: the electron as a wave

If light behaves like a particle, the symmetric question is whether matter behaves like a wave.

Louis de Broglie's 1924 doctoral thesis at the University of Paris proposed that a particle of momentum $p$ has an associated wavelength:

$$\lambda = \frac{h}{p}.$$

This is the photon relation applied to matter.

The numerical scale determines where the effect is observable. A 1 kg cricket ball at 1 m/s has $\lambda = 6.6 \times 10^{-34}$ m — twenty orders of magnitude below a proton's size, undetectable. An electron accelerated through 54 V has kinetic energy 54 eV and de Broglie wavelength near 0.17 nm, comparable to crystal lattice plane spacings. An electron beam on a crystal should therefore diffract, as X-rays do.

Clinton Davisson and Lester Germer at Bell Labs observed this in 1927, scattering 54 eV electrons off a nickel crystal and finding a sharp diffraction peak at the angle Bragg's condition predicts.

**Worked example — Davisson–Germer diffraction angle.**

**Given.** An electron accelerated through $V = 54$ V, so $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Nickel (111) surface plane spacing $d = 0.215$ nm. Surface diffraction condition $\lambda = d\sin\phi$.

**Find.** The electron's de Broglie wavelength and the predicted first-order diffraction angle.

**Solution.** Momentum:

$$p = \sqrt{2m_e K} = \sqrt{2(9.11 \times 10^{-31})(8.65 \times 10^{-18})} \approx 3.97 \times 10^{-24} \, \text{kg·m/s}.$$

De Broglie wavelength:

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10} \, \text{m} = 0.167 \, \text{nm}.$$

Diffraction angle: $\sin\phi = 0.167/0.215 = 0.777$, so $\phi = 51°$.

**Check.** Davisson and Germer measured 50°, agreeing with the prediction to within one degree.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The single-electron version was carried out by Akira Tonomura's group at Hitachi in 1989. Electrons arrived one at a time, each registering as a point. Accumulated over hours, the points formed a diffraction pattern. A single electron, with no other electrons present, produced interference. There is no classical account of this; the electron interferes with itself.

![Tonomura buildup sequence ](../images/01-why-quantum-mechanics-fig-04.png)
*Figure 1.4 — Tonomura buildup sequence *

The operative rule: matter has wave properties, and the wavelength is a property of the associated amplitude, not of the particle's physical extent. A detected electron appears as a point. The wave appears only in the statistical pattern built from many detections.

---

## The fifth confrontation: energy levels are real

In 1914, James Franck and Gustav Hertz accelerated electrons through mercury vapor and measured the collector current versus accelerating voltage. The current rose, then dropped sharply at 4.9 V, rose again and dropped at 9.8 V, and again at 14.7 V — regular dips spaced exactly 4.9 V apart.

The interpretation: below 4.9 eV the electron scatters elastically off mercury atoms, loses no energy, and reaches the collector. At 4.9 eV it can transfer exactly that energy to a mercury atom, exciting it from the ground state to the first excited state; the electron then lacks the energy to reach the collector against the retarding field, producing the drop. Additional voltage restores its energy until, at 9.8 eV, it can excite two atoms in succession.

![Franck–Hertz current vs](../images/01-why-quantum-mechanics-fig-05.png)
*Figure 1.5 — Franck–Hertz current vs*

If correct, the excited mercury atoms should decay by emitting photons of energy 4.9 eV. The wavelength:

$$\lambda = \frac{hc}{E} = \frac{1240 \, \text{eV·nm}}{4.9 \, \text{eV}} \approx 253 \, \text{nm}.$$

Franck and Hertz observed a sharp emission line at 253.7 nm whenever the accelerating voltage exceeded 4.9 V. Two independent probes — electron stopping voltage and photon wavelength — gave the same energy for the same atomic transition. The energy levels are real.

This is the direct evidence for discrete internal energy structure in atoms. Spectroscopy — the Balmer and Lyman series — was already known but is indirect: emitted photons are measured and the levels inferred. Franck–Hertz is direct: the electron is observed losing exactly 4.9 eV in a collision, and the photon is observed at exactly the predicted wavelength.

---

## What the five experiments require

After 1927, any replacement for classical physics had to accommodate five quantitative facts:

1. Energy exchange between matter and the radiation field occurs in discrete units of $h\nu$ (Planck, 1900).
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

Three structural requirements follow. The theory needs a *probabilistic* account of measurement: the landing point of a single electron in a diffraction experiment is not predictable, only its long-run distribution. It needs *wave-equation structure* to handle interference and de Broglie wavelengths. And it needs *eigenvalue structure* to handle discrete energy levels.

The next chapters build these structures. The required mathematics is the theory of operators on complex vector spaces and the wave equation governing the time evolution of quantum amplitudes. The five experiments are the constraints; the following theory is built to meet them.

Note that Planck's constant $h$ appears in all five relations — the Compton shift, the de Broglie wavelength, the photoelectric threshold, the Planck distribution — and in every case it is the same $h$, $6.626 \times 10^{-34}$ J·s, extracted from independent experiments with different setups. This is a constant of nature setting the scale at which classical descriptions fail. It is the right starting point for understanding why quantum mechanics has the form it does: the theory is forced by the existence of this number and its appearance in each of these five confrontations.

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
