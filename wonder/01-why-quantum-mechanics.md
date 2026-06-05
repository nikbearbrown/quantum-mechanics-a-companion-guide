# Chapter 1 — Why Quantum Mechanics?

## TL;DR

- This is the theory a stubborn universe forced on us by breaking every prediction classical physics dared to make.
- We walk through the first confrontation (infinite energy in a box), the second (a threshold that has no business existing), the third (light comes back the wrong color), the fourth (the electron behaving like a wave), and the rest.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The Theory a Universe Built by Breaking Every Prediction Classical Physics Made.*

---

Here is a thing I find genuinely funny, and a little wonderful. By the year 1900, the smartest physicists alive were quietly convinced the show was basically over. Newton had handed them mechanics. Maxwell had handed them electrodynamics. Boltzmann had statistical mechanics, Clausius had thermodynamics. The big laws were in the bank. What was left, they figured, was tidying up — measuring the known constants to one more decimal place.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

And then the decimal places opened up and a whole new universe climbed out.

Now, the trouble was not some vague philosophical worry. It was sharp and it was numerical. Classical physics — those four great pillars working together — made specific, checkable predictions about how light and matter ought to behave. And as the experimenters pushed into the strange corners — very short wavelengths, very faint beams, very fine spectroscopy — the predictions did not fail by a polite little margin. They handed back *infinities* where nature handed back tidy finite peaks. They predicted smooth, gradual behavior where nature gave a hard, clean cutoff. The theory had no words at all for results that were reproducible, sharp, and utterly unlike anything it expected.

Five experiments, stretched across about a quarter of a century, did the damage. I want to walk you through each one and show you the mathematics it forced into existence — not as a history lesson, but as a series of stand-offs between a beautiful theory and a universe that simply refused to cooperate.

---

## The first confrontation: infinite energy in a box

Let's start with something you could almost build in your kitchen: a hollow metal box, walls held at some fixed temperature. The walls glow. They throw off electromagnetic radiation, and that radiation rattles around inside, settling into thermal equilibrium with the walls. Here is the question. How does the energy split itself up among all the different frequencies?

Classical statistical mechanics gives a beautifully clean answer — and that is exactly what should make you nervous. Every electromagnetic mode in the cavity gets, on average, an energy of $k_B T$, by the equipartition theorem. And there are infinitely many modes, because you can always cook up one of higher frequency. Count them in a little frequency window $[\nu, \nu + d\nu]$. There are $8\pi\nu^2/c^3$ of them per unit volume. Multiply by $k_B T$:

$$\rho_{\text{RJ}}(\nu, T) = \frac{8\pi \nu^2}{c^3} k_B T.$$

![Plot of Rayleigh–Jeans vs](../images/01-why-quantum-mechanics-fig-01.png)
*Figure 1.1 — Plot of Rayleigh–Jeans vs*

Now look at what that says. It climbs without limit as the frequency goes up. The total energy, $\int_0^\infty \rho_{\text{RJ}} \, d\nu$, blows up to infinity. A box sitting at room temperature should, by this reasoning, hold an infinite amount of energy in its short-wavelength modes. Open the oven door and the universe ends. Paul Ehrenfest later gave this disaster a name worthy of it: the "ultraviolet catastrophe."

Meanwhile, over in Berlin, the experimenters at the Physikalisch-Technische Reichsanstalt — Otto Lummer and Ernst Pringsheim — were measuring real blackbody spectra through the late 1890s, and measuring them with extraordinary care. And what did nature actually do? It gave a finite peak at some characteristic frequency, then dropped off exponentially toward the high frequencies. No catastrophe. No infinity. Just a shape — a specific, stubborn shape — that nobody could explain.

Max Planck stood up with his fit on 14 December 1900. The Planck distribution is:

$$\rho(\nu, T) = \frac{8\pi h \nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_B T} - 1}.$$

The constant $h$ he fitted to the data: $6.55 \times 10^{-27}$ erg·s, within 1% of today's value $h = 6.626 \times 10^{-34}$ J·s.

Now watch how he pulled it off, because it is one of the slyest moves in the history of physics. Suppose the little oscillators in the cavity walls — the atoms doing the absorbing and re-emitting — cannot trade energy with the field in a smooth, continuous trickle. Suppose instead they can only hand it over in discrete chunks of size $h\nu$, in whole-number multiples of a quantum of energy. Then the average thermal energy of an oscillator at frequency $\nu$ is no longer the equipartition value $k_B T$. It is:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} n h\nu \, e^{-n h\nu/k_B T}}{\sum_{n=0}^{\infty} e^{-n h\nu/k_B T}}.$$

Let $x = e^{-h\nu/k_B T}$. The numerator is $h\nu \sum n x^n = h\nu \cdot x/(1-x)^2$; the denominator is $\sum x^n = 1/(1-x)$. Dividing:

$$\langle E \rangle = \frac{h\nu}{e^{h\nu/k_B T} - 1}.$$

And now look at what this little expression does at the two ends. At low frequencies, where $h\nu \ll k_B T$, we have $e^{h\nu/k_B T} - 1 \approx h\nu/k_B T$, so $\langle E \rangle \to k_B T$ — equipartition comes marching right back, exactly where the old theory worked. At high frequencies, $h\nu \gg k_B T$, and $\langle E \rangle \to h\nu \, e^{-h\nu/k_B T}$ — crushed down exponentially. The catastrophe is simply gone. Multiply by the mode-counting density $8\pi\nu^2/c^3$ (that part is the old classical counting, unchanged) and out drops Planck's distribution.

One thing I want you to get straight before we move on, because almost everybody gets it slightly wrong. Planck did *not* quantize light. He quantized the energy *exchange* between the cavity walls and the radiation field. In his 1900 picture, the radiation itself is still a perfectly ordinary continuous electromagnetic wave. The discrete packets lived in the walls, not in the field. It took Einstein, five years later, to put the packets into the field itself. Hold onto that distinction — it is going to matter.

---

## The second confrontation: a threshold that shouldn't exist

Shine some light on a clean metal surface. Electrons pop off. That much was old news. But in 1902 Philipp Lenard reported the part that should not happen at all: the kinetic energy of the ejected electrons depended on the *frequency* of the light, not on its *intensity*. A blindingly bright red beam — pouring power onto the surface — could knock loose no electrons whatsoever from certain metals. A feeble little ultraviolet beam knocked them loose instantly.

Stop and feel how strange that is. Classical wave theory says intensity is what should count. A brighter wave delivers more energy per second. An electron clinging to the metal ought to be able to soak up enough energy to escape, if you just wait long enough. But the wait never pays off. The threshold is sharp as a knife. The classical picture fails three ways at once: wrong variable (frequency, not intensity), wrong threshold behavior (a clean cutoff, not a gradual ramp), wrong scaling (kinetic energy rising with frequency above the threshold, not with intensity).

Einstein's 1905 paper made the audacious proposal: light itself arrives in indivisible packets — photons — each carrying energy $E = h\nu$. An electron bound to the metal with binding energy $\phi$ (the work function, a property of the metal) swallows exactly one photon. If $h\nu > \phi$, the electron escapes with kinetic energy:

$$K_{\max} = h\nu - \phi.$$

Below the threshold frequency $\nu_0 = \phi/h$, no electrons come out, no matter how bright you make the light. Above it, intensity controls *how many* electrons come out per second; frequency controls *how much energy* each one carries. One photon, one electron. The packet either has enough to spring the electron loose, or it doesn't.

![Stopping potential V_s vs](../images/01-why-quantum-mechanics-fig-02.png)
*Figure 1.2 — Stopping potential V_s vs*

Here is my favorite part. Robert Millikan spent four years — 1912 to 1916 — trying to *disprove* this. He measured the stopping potential $V_s$ — the retarding voltage that just barely halts the most energetic electrons, so $eV_s = K_{\max}$ — as a function of frequency. By Einstein's equation, the slope of that line is $h/e$. Millikan measured $h = 6.57 \times 10^{-27}$ erg·s. That is within 0.5% of Planck's blackbody value, pulled from a completely different experiment. And he published it grumbling — conceding that the photoelectric equation worked perfectly while insisting that the photon hypothesis underneath it was "untenable." The man hated the answer and confirmed it to half a percent anyway. That is science being honest in spite of itself.

**A worked example.** Sodium has work function $\phi \approx 2.36$ eV (NIST clean-surface value; see references). The threshold wavelength is:

$$\lambda_0 = \frac{hc}{\phi} = \frac{1240 \, \text{eV·nm}}{2.36 \, \text{eV}} \approx 525 \, \text{nm}.$$

That's green light. Illuminate with $\lambda = 400$ nm (violet). Photon energy $h\nu = 1240/400 = 3.10$ eV. The most energetic photoelectron leaves with:

$$K_{\max} = 3.10 \, \text{eV} - 2.36 \, \text{eV} = 0.74 \, \text{eV}.$$

A retarding voltage of 0.74 V stops it exactly.

The lesson is simple and stubborn: one photon, one electron. Energy arrives in indivisible packets, the threshold is sharp because a packet either has enough or it doesn't, and intensity controls the rate, not the energy each electron walks away with.

---

## The third confrontation: the wrong color comes back

In 1923, Arthur Holly Compton at Washington University fired X-rays at graphite and measured the wavelength of the scattered radiation as a function of angle. The classical prediction here — Thomson scattering — is clear: the electron jiggles at the frequency of the incoming wave and re-radiates at that *same* frequency. No shift in wavelength. Just light spread out into different angles, the same color it went in.

Compton found a shift. The scattered X-rays came back *longer* in wavelength than the ones that went in, and by an amount that depended on nothing but the angle $\theta$:

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta).$$

The combination $h/m_e c = 2.426 \times 10^{-12}$ m is called the Compton wavelength of the electron. The shifts are tiny — picometers — but they are unmistakable and they repeat perfectly every time.

Now here is the thing I love about this one: the derivation is the cleanest piece of mathematics in the whole chapter, and it needs no quantum mechanics at all beyond one bold assumption. Just treat the photon as a relativistic particle with energy $E_\gamma = h\nu$ and momentum $p_\gamma = h/\lambda$. The electron starts at rest. Write down conservation of energy and conservation of momentum (two components), then chase out the electron's recoil angle.

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

Half a page of algebra. That's the whole thing. No quantum mechanics beyond the one move of treating the photon as a relativistic particle with $E = h\nu$ and $p = h/\lambda$ — billiard balls, basically, but one of the balls is light.

**In Compton's original experiment** he used molybdenum Kα X-rays at $\lambda = 0.0711$ nm. At $\theta = 90°$, $\cos\theta = 0$, so $\Delta\lambda = h/m_e c = 2.43$ pm. He measured 2.23 pm. The agreement was the moment the photon picture became unavoidable.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

The lesson: the photon carries momentum $h/\lambda$. Watch the relay race. Planck had quantized the energy exchange. Einstein had quantized the field. Compton now quantized the momentum, and with that the photon stood fully assembled as a relativistic particle.

---

## The fourth confrontation: the electron as a wave

If light — which everybody *knew* was a wave — turned out to act like a particle, then the obvious mirror-image question grabs you by the collar: does matter, which everybody *knew* was made of particles, turn out to act like a wave?

Louis de Broglie's 1924 doctoral thesis at the University of Paris said: yes. He proposed that a particle with momentum $p$ has a wavelength riding along with it:

$$\lambda = \frac{h}{p}.$$

The very same relation as for the photon — only now you point it at matter.

And the numbers are wonderfully instructive, because they tell you instantly why nobody had ever noticed. A 1 kg cricket ball at 1 m/s has $\lambda = 6.6 \times 10^{-34}$ m — twenty orders of magnitude smaller than a proton. No experiment that could ever be built will detect that. The ball is a particle, full stop, and the wave is buried so deep below the noise of the world that it might as well not exist. But take an electron accelerated through 54 V: it has a kinetic energy of 54 eV and a de Broglie wavelength of roughly 0.17 nm — about the spacing between the planes of atoms in a crystal lattice. And *that* changes everything. Aim an electron beam at a crystal and it should diffract, exactly the way X-rays do.

Clinton Davisson and Lester Germer at Bell Labs caught it in 1927. They scattered 54 eV electrons off a nickel crystal and saw a sharp diffraction peak sitting right at the angle Bragg's condition predicts.

**The calculation.** An electron through $V = 54$ V has kinetic energy $K = 54$ eV $= 8.65 \times 10^{-18}$ J. Its momentum:

$$p = \sqrt{2m_e K} = \sqrt{2(9.11 \times 10^{-31})(8.65 \times 10^{-18})} \approx 3.97 \times 10^{-24} \, \text{kg·m/s}.$$

De Broglie wavelength:

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{3.97 \times 10^{-24}} \approx 1.67 \times 10^{-10} \, \text{m} = 0.167 \, \text{nm}.$$

Nickel's (111) surface plane spacing is $d = 0.215$ nm. The surface diffraction condition gives $\lambda = d\sin\phi$, so $\sin\phi = 0.167/0.215 = 0.777$, $\phi = 51°$. They measured 50°. Agreement to within one degree.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/01-why-quantum-mechanics-assertions.md -->

Now for the version that really ought to keep you up at night. Akira Tonomura's group at Hitachi did it in 1989 as a slow buildup, one electron at a time. Each electron arrived alone, registering as a single point on the detector — bang, a dot, just like a particle. But let the dots pile up over hours, and they arrange themselves into a diffraction pattern. A single electron, with no other electron anywhere near it to interfere with, produces interference. Sit with that. There is no classical way to read it. The electron "interferes with itself," and there is no Newtonian sentence you can write down that means anything like that.

![Tonomura buildup sequence ](../images/01-why-quantum-mechanics-fig-04.png)
*Figure 1.4 — Tonomura buildup sequence *

The lesson: matter has wave properties, and — this is the subtle part — those properties are not about the particle's *size*. The wavelength belongs to the associated amplitude, not to some physical extent of the electron. When you actually catch the electron, it shows up as a point. The wave only ever announces itself in the statistical pattern built from a great many of those points.

---

## The fifth confrontation: energy levels are real

In 1914, James Franck and Gustav Hertz pushed electrons through mercury vapor and measured the current reaching a collector as they cranked up the accelerating voltage. The current rose steadily — then dropped sharply at 4.9 V. It rose again, dropped again at 9.8 V. And again at 14.7 V. Regular dips, spaced exactly 4.9 V apart, like a metronome.

Here is what's going on. An electron with kinetic energy below 4.9 eV just bounces off the mercury atoms elastically, losing no energy, and sails on to the collector. But at 4.9 eV, the electron can hand over that exact amount to a mercury atom, kicking it from its ground state up to its first excited state. Having given away its energy, the electron can no longer fight its way to the collector against the retarding field — and there's your drop. Crank the voltage higher and the electron picks up enough energy again to reach the collector, right up until it has 9.8 eV and can excite *two* mercury atoms in a row.

![Franck–Hertz current vs](../images/01-why-quantum-mechanics-fig-05.png)
*Figure 1.5 — Franck–Hertz current vs*

Now, if that story is right, here is a prediction with teeth. The excited mercury atoms have to fall back down to the ground state, and when they do they should spit out photons carrying exactly 4.9 eV. The wavelength:

$$\lambda = \frac{hc}{E} = \frac{1240 \, \text{eV·nm}}{4.9 \, \text{eV}} \approx 253 \, \text{nm}.$$

So Franck and Hertz built a spectroscope and looked. And there it was — a sharp emission line at 253.7 nm, appearing exactly whenever the accelerating voltage climbed past 4.9 V. Two completely independent probes — the stopping voltage of an electron and the wavelength of a photon — pointed at the very same energy for the very same atomic transition. The energy levels are real.

This is the *direct* evidence for discrete internal energy structure inside atoms, and it is worth appreciating how direct. Spectroscopy — the Balmer series, the Lyman series — was already on the books, but spectroscopy is an inference: you see the emitted photons and you reason backward to the levels. Franck–Hertz cuts out the middleman. You watch the electron lose exactly 4.9 eV in a collision, and then you watch the photon come out at exactly the predicted wavelength. You are looking at the energy levels almost with your own eyes.

---

## What the five experiments require

After 1927, any theory hoping to replace classical physics had five specific, quantitative facts it had to swallow whole:

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

Three structural demands fall straight out of these. The new theory needs a *probabilistic* account of measurement: you simply cannot say where a single electron in a diffraction experiment will land; you can only say where the crowd of them will pile up over the long run. It needs *wave-equation structure*: something that can handle interference and de Broglie wavelengths. And it needs *eigenvalue structure*: something that can produce discrete energy levels rather than a continuous smear.

The next chapters build exactly those structures. The mathematics you'll need is the theory of operators acting on complex vector spaces, plus the wave equation that says how quantum amplitudes march forward in time. The five experiments above are the constraints — the iron facts the theory has to honor. What follows is the theory built to meet them.

But before you turn the page, notice one thing — and I think it is the most beautiful clue in the whole story. Planck's constant $h$ shows up in *all five* relations. The Compton shift, the de Broglie wavelength, the photoelectric threshold, the Planck distribution — every one of them has $h$ sitting inside it. And in every case it is the *same* $h$, $6.626 \times 10^{-34}$ J·s, pulled out of independent experiments with completely different apparatus, different metals, different gases, different decades. That is not a coincidence. You don't get a coincidence five times to the same six digits. That is a constant of nature, marking the exact scale at which classical descriptions give up the ghost. When you want to understand *why* quantum mechanics looks the way it does, start there: it is the theory forced into being by this one number and its insistence on appearing in every single one of these five confrontations.

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
