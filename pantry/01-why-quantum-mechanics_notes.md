# Research Notes: Unit 01 — Why Quantum Mechanics?

**Source:** TIKTOC.md Unit 1 entry (lines 230–236)
**Notes file:** 01-why-quantum-mechanics_notes.md
**Corresponding chapter:** chapters/01-why-quantum-mechanics.md (not yet written)
**Generated:** 2026-05-13

---

## Unit summary (from TIKTOC.md)

> ### Unit 1: Why Quantum Mechanics?
> - Classical physics and its failures **[BOOK: Ch. 3, 11]**
> - Blackbody radiation **[BOOK: Ch. 3]**
> - Photoelectric effect **[BOOK: Ch. 4]**
> - Compton scattering **[BOOK: Ch. 10]**
> - de Broglie waves and wave-particle duality **[BOOK: Ch. 5, 11]**
> - Franck-Hertz experiment **[BOOK: Ch. 6]**

TIKTOC Part I Verdict: "Best section of the book... Usable as motivational reading before you introduce formalism. No math, so students need a second source for everything quantitative." The companion's job in Unit 1 is therefore narrow: keep the historical narrative the pop-sci book already does well, but add the quantitative machinery the student needs to actually compute results.

---

## A. Conceptual foundations

### 1. The ultraviolet catastrophe and Planck's quantum hypothesis

By the late 1890s the classical theory of blackbody radiation, built on the equipartition of energy across the modes of an electromagnetic cavity, gave the Rayleigh–Jeans law: spectral energy density rising as the square of the frequency without bound. Lord Rayleigh's 1900 calculation and Jeans's 1905 refinement made the disaster explicit. The integral of energy across all frequencies diverged — a finite cavity should radiate infinitely.

Max Planck's response, presented to the German Physical Society on 14 December 1900 (the "birth of quantum theory" date), was a postulate justified only by the fit to experimental data: that the oscillators making up the cavity walls could exchange energy with the radiation field only in discrete packets E = hν. The resulting spectral distribution

ρ(ν,T) = (8πhν³/c³) · 1/(e^(hν/kT) − 1)

cut off the high-frequency divergence because at large hν/kT, the Boltzmann factor exponentially suppressed the high-frequency modes. The constant h, fitted to Lummer and Pringsheim's spectra, took the value Planck reported as 6.55 × 10⁻²⁷ erg·s (modern: 6.62607015 × 10⁻³⁴ J·s, exact by 2019 SI redefinition).

The companion should be explicit about what Planck himself thought he was doing. Planck did not believe radiation was actually quantized in 1900; he treated the quantization as a calculational device for the oscillators in the cavity walls. The radiation field itself, he assumed, remained continuous. Einstein in 1905 took the quantization seriously and applied it to light itself.

**Common misconception:** "Planck quantized light." He did not — he quantized the energy exchange between oscillators and the field. The quantization of the radiation field was Einstein's 1905 move.

**Worked example (Griffiths style):** Show the Wien (high-frequency) and Rayleigh–Jeans (low-frequency) limits of Planck's law and confirm the Stefan–Boltzmann constant σ = 2π⁵k⁴/(15h³c²) emerges from ∫ρ(ν,T)dν. Griffiths covers thermal radiation only briefly (Afterword in some editions); the calculation belongs in this companion chapter.

**Sources:**
- Planck, M. (1901). "Über das Gesetz der Energieverteilung im Normalspectrum." *Annalen der Physik* 4, 553–563. [Available via Wiley/Annalen archives.]
- Kuhn, T. S. (1978). *Black-Body Theory and the Quantum Discontinuity, 1894–1912.* Oxford University Press. [Historical context for "what Planck actually meant."]

### 2. The photoelectric effect and Einstein's light quanta

In 1902 Philipp Lenard reported the experimental fact that demolished the classical wave theory of light's interaction with matter: the kinetic energy of photoelectrons depended on the frequency of the incident light, not its intensity. A bright red light could not eject electrons from a metal whose work function exceeded hν_red, no matter how long you waited or how intense you made the beam. A dim ultraviolet beam ejected electrons instantly.

Einstein's 1905 paper "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt" ("On a Heuristic Point of View Concerning the Production and Transformation of Light") proposed that light itself consisted of localized energy packets of magnitude E = hν. The resulting equation was

K_max = hν − φ

where φ is the work function of the metal — the minimum energy to liberate an electron from the surface. This is the equation for which Einstein won the 1921 Nobel Prize. (Note: the Nobel was specifically for the photoelectric law, not for relativity — a deliberately conservative choice by the Nobel committee.)

Robert Millikan, who set out between 1912 and 1916 to disprove Einstein's photon hypothesis, instead measured the slope of K_max vs. ν and got exactly h, agreeing with Planck's blackbody value. Millikan reported this result in *Physical Review* in 1916 with the famous concession that the experiment supported "Einstein's equation" despite his belief that the photon idea was "untenable."

**Common misconception:** "The photoelectric effect proves light is particles." More precisely: it shows that the energy in a light beam is delivered to bound electrons in indivisible packets of size hν, and the rate of ejection (not the energy) scales with intensity. Light is neither classical particle nor classical wave — both pictures are projections of something the classical vocabulary does not have a word for. Unit 1 should set this up; Unit 2 (state vectors) and Unit 3 (Schrödinger equation) deliver the actual replacement.

**Worked example:** Sodium has φ ≈ 2.28 eV. Compute the threshold wavelength (λ_0 = hc/φ ≈ 544 nm — green light). Then for incident 400 nm light compute K_max ≈ 0.82 eV. This calculation appears in Griffiths Ch. 1 problem set [verify exact problem number — typically Problem 1.x in the introductory historical section].

**Sources:**
- Einstein, A. (1905). "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17, 132–148. English translation in Stachel, J. ed. (1998). *Einstein's Miraculous Year.* Princeton University Press.
- Millikan, R. A. (1916). "A Direct Photoelectric Determination of Planck's 'h'." *Physical Review* 7(3), 355–388.

### 3. Compton scattering and the kinematics of the photon

Arthur Holly Compton's 1923 paper in *Physical Review* settled the question of whether the photon carried momentum. Photons scattered off loosely bound electrons in graphite shifted their wavelength by an amount that depended only on the scattering angle:

Δλ = λ' − λ = (h/m_e c)(1 − cos θ)

The Compton wavelength of the electron h/m_e c = 2.426 × 10⁻¹² m sets the scale. The derivation is pure relativistic kinematics applied to a photon with four-momentum (hν/c, hν/c·n̂) and an electron initially at rest — conservation of energy and three-momentum gives the result in roughly half a page. This is the cleanest place in Unit 1 to *do the math* — the derivation is elementary, the prediction is precise, and the experimental confirmation is unambiguous.

The classical Thomson scattering picture predicts no wavelength shift, because in the classical picture the electron oscillates at the incident frequency and re-radiates at the same frequency. Compton's result was the moment the photon picture became unavoidable.

**Common misconception:** "The Klein–Nishina formula gives the Compton shift." It does not — Klein–Nishina (1929) gives the *differential cross section* for photon-electron scattering including quantum-electrodynamic spin effects. The wavelength-shift formula is purely kinematic and was derived by Compton in 1923 (and independently by Debye the same year). The pop-sci book names Klein–Nishina without distinguishing this; the companion should.

**Worked example:** Photon of wavelength 0.0711 nm (Mo Kα line, the wavelength Compton actually used) scattered at θ = 90° picks up Δλ = h/m_e c · 1 = 2.43 pm. Final wavelength 0.0735 nm. Classical Thomson prediction: 0.0711 nm. The shift is real and measurable.

**Sources:**
- Compton, A. H. (1923). "A Quantum Theory of the Scattering of X-rays by Light Elements." *Physical Review* 21(5), 483–502.
- Griffiths, *Introduction to Quantum Mechanics* — historical context appears in Ch. 1 introduction; the kinematic derivation is more typically found in Griffiths's *Introduction to Elementary Particles* (Ch. 7) [verify chapter for current edition].

### 4. The de Broglie hypothesis and matter waves

Louis de Broglie's 1924 doctoral thesis at the University of Paris proposed the symmetric extension of Einstein's relation: if light with energy E = hν carries momentum p = E/c = h/λ, then a material particle with momentum p should also have a wavelength

λ = h/p

The argument was a relativistic-symmetry move: Einstein had given waves a particle nature, so de Broglie was giving particles a wave nature. The numerical consequence is striking. A 1 kg cricket ball moving at 1 m/s has a de Broglie wavelength of 6.6 × 10⁻³⁴ m — twenty orders of magnitude below a proton radius, undetectable. An electron at 1 eV has wavelength ~1.2 nm — on the order of atomic spacings, and therefore diffractable by a crystal lattice.

Davisson and Germer's 1927 experiment at Bell Labs, scattering electrons off a nickel crystal, confirmed the prediction quantitatively. The diffraction pattern matched what you would expect from a wave of wavelength h/p. George Paget Thomson's independent experiment at Aberdeen the same year confirmed it with thin foils. (Father J. J. Thomson got the Nobel in 1906 for showing the electron was a particle; son G. P. Thomson shared the 1937 Nobel for showing the electron was a wave. The universe has a sense of humor.)

**Common misconception:** "de Broglie wavelength is the size of the particle." It is not — it is the wavelength of the probability amplitude associated with motion at momentum p. The particle, when detected, registers as a point. The wavelength describes the interference behavior of the *amplitude* whose squared modulus gives the detection probability.

**Worked example:** Compute the de Broglie wavelength of an electron accelerated through 54 V (Davisson–Germer): K = 54 eV, p = √(2mK), λ = h/p ≈ 0.167 nm. Compare to the nickel (111) plane spacing 0.215 nm. Bragg condition gives a peak at θ ≈ 50° — the angle Davisson and Germer measured.

**Sources:**
- de Broglie, L. (1924). *Recherches sur la théorie des quanta.* Doctoral thesis, University of Paris. English translation by A. F. Kracklauer (2004) available via the de Broglie Foundation [verify URL stability].
- Davisson, C. and Germer, L. H. (1927). "Diffraction of Electrons by a Crystal of Nickel." *Physical Review* 30(6), 705–740.
- Griffiths Ch. 1 (introductory historical material).

### 5. Franck–Hertz: atomic energy levels are discrete

James Franck and Gustav Hertz reported in 1914 (*Verhandlungen der Deutschen Physikalischen Gesellschaft* 16, 457–467) that electrons passing through mercury vapor lost energy in discrete chunks of 4.9 eV. The current-vs-voltage curve showed periodic dips at multiples of 4.9 V. Below this threshold, collisions were elastic; above it, the electron could excite the mercury atom and lose exactly the excitation energy. This was the direct experimental confirmation that atomic energy levels are quantized — independent of and complementary to the spectroscopic evidence from Balmer, Lyman, and Paschen series in hydrogen.

The 4.9 eV value corresponds to the 6¹S₀ → 6³P₁ transition in mercury, and the 253.7 nm UV emission Franck and Hertz observed when the threshold was exceeded matches hc/E = 1240 eV·nm / 4.9 eV = 253 nm.

**Common misconception:** "Franck–Hertz proves Bohr's model." It proves energy-level quantization, which the Bohr model predicts as one consequence. The full Bohr model (specific level structure of hydrogen) is over-fitted; Franck–Hertz is more general and survives the move to full quantum mechanics.

**Worked example:** From the 4.9 V threshold, predict the wavelength of the emitted photon. Compare to the measured 253.7 nm. The agreement is the experimental signature that the electron's lost energy is going into a *single* atomic transition.

**Sources:**
- Franck, J. and Hertz, G. (1914). "Über Zusammenstöße zwischen Elektronen und Molekülen des Quecksilberdampfes und die Ionisierungsspannung desselben." *Verhandlungen der Deutschen Physikalischen Gesellschaft* 16, 457–467. Nobel Prize 1925.

---

## B. Domain examples and cases

### Case 1 — The 1900 Lummer–Pringsheim blackbody measurements

Otto Lummer and Ernst Pringsheim's 1899–1900 measurements at the Physikalisch-Technische Reichsanstalt in Berlin gave Planck the experimental data that no classical theory could fit. The deviation from the Wien law at long wavelengths, especially the radiance at 6 μm and high temperature, is what forced the new functional form. Without these measurements Planck had no reason to abandon classical thermodynamics. Worth naming: the quantum revolution started in a German metrology lab measuring radiator filaments for the lighting industry.

### Case 2 — Millikan's reluctant confirmation (1916)

Millikan called Einstein's hypothesis "untenable" in print, then spent four years trying to disprove it with the most careful photoelectric measurements yet performed. The slope of his stopping-potential-vs-frequency plot gave h = 6.57 × 10⁻²⁷ erg·s, agreeing with Planck's blackbody h to 0.5%. He still rejected the photon interpretation. The historiography lesson — that an experimentalist can do unimpeachable work *for* a theory he disbelieves — is worth a paragraph in the chapter.

### Case 3 — Tonomura's single-electron double slit (1989)

Akira Tonomura's group at Hitachi published a video in *American Journal of Physics* (1989) showing single electrons arriving one at a time on a detector, each registering as a point, and accumulating over hours into a perfect two-slit interference pattern. This is the single most pedagogically clean demonstration that the wave-particle duality of de Broglie is real and not an artifact of large-N. Each electron detected as a particle; the pattern of detections distributed as a wave.

### Failure case — Classical predictions for photoemission

The classical wave picture predicts (a) a delay time before photoemission while the electron accumulates enough energy from a weak beam — measurable in seconds to minutes for sufficiently dim sources, (b) intensity-dependent kinetic energies, (c) emission at any frequency given enough intensity. Experiment: (a) emission is prompt to within 10⁻⁹ s even at the weakest detectable intensities, (b) kinetic energy is intensity-independent, (c) emission is frequency-threshold gated. All three classical predictions fail. This is the textbook example of a theory being killed by three independent quantitative disagreements with the same experiment.

---

## C. Connections and dependencies

**Prerequisites:** Classical electromagnetism at the level of Griffiths *Introduction to Electrodynamics* Ch. 9 (electromagnetic waves) — students should know that classical light is a transverse EM wave with energy density (ε₀/2)|E|² + (1/2μ₀)|B|². Basic special relativity for the Compton derivation (four-momentum). Maxwell–Boltzmann statistics for the equipartition argument.

**Unlocks:** The motivation for Unit 2 (we need new mathematics — complex vector spaces — because classical wave or particle math cannot describe what we just saw). The motivation for Unit 3 (we need a wave equation for matter waves — the Schrödinger equation). The motivation for Unit 6 (hydrogen spectrum quantization is *predicted* by Schrödinger, only postulated by Bohr).

**Adjacent unit connections:**
- Unit 2 (math foundations): Why do we need complex amplitudes? Because the interference patterns in the double-slit experiment require both phase and amplitude — and probabilities (which must be real and non-negative) come from |ψ|², not ψ itself.
- Unit 3 (Schrödinger equation): The de Broglie relation λ = h/p plus Einstein's E = hν determines the dispersion relation; the SE is the simplest linear wave equation consistent with both.
- Unit 5 (formalism): Heisenberg uncertainty has a direct heuristic argument from de Broglie — narrow wave packet in position requires wide spread in wavenumber, hence in momentum.

---

## D. Current state of the field

**Settled:** All five experimental results (blackbody, photoelectric, Compton, electron diffraction, Franck–Hertz) are textbook physics, reproduced thousands of times, no contemporary controversy. Planck's constant is now defined (since 20 May 2019) to be exactly 6.62607015 × 10⁻³⁴ J·s by international agreement, making it a defining constant of the SI rather than a measured one.

**Contested:** The *interpretive* significance of these results is settled at the operational level but not at the ontological level. "What is a photon?" is still genuinely contested. Lamb (1995, *Applied Physics B* 60, 77–84, "Anti-photon") argued the term should be retired. Most working physicists use the photon picture as a calculational shorthand for quantum electrodynamic mode excitations and leave the ontology for another day. For Unit 1 the companion should describe the photon operationally — "a quantum of the electromagnetic field with energy hν and momentum hν/c" — and flag that the deeper question waits for the formalism in Units 2 and 3.

**Key references:**
- Jammer, M. (1966). *The Conceptual Development of Quantum Mechanics.* McGraw-Hill. [The standard historical reference.]
- Pais, A. (1982). *'Subtle is the Lord...': The Science and the Life of Albert Einstein.* Oxford University Press. [Chapter 19 on the photon hypothesis.]
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed. (2018) — historical introduction in Ch. 1.

**Recent developments (last 3 years):** Photon-number-resolving detectors (superconducting transition-edge sensors) have made it routine to count individual photons in laboratory experiments. Quantum-eraser variants of Compton scattering continue to test the consistency of QED at high precision. None of this changes the Unit 1 narrative; it deepens it.

---

## E. Teaching considerations

**Where undergraduates stick:**

1. **"What is a photon, really?"** This question is unanswerable at the Unit 1 level and the student needs to be told that — explicitly, not by deflection. "We are going to spend Units 2 and 3 building the mathematical machinery that lets us answer this question precisely. For now, take 'photon' as 'whatever the discrete energy exchange in these experiments is.'"

2. **Confusion between Planck's quantization and Einstein's.** Many students leave Unit 1 thinking Planck quantized light. Correcting this in passing matters because Unit 5 will revisit the historical sequence and the student needs the chronology right.

3. **de Broglie wavelength of macroscopic objects.** Students often want to know why we don't see interference for a baseball. The answer — that h is small enough that macroscopic wavelengths are sub-nuclear — is quantitative and reassuring once they run the number.

**Analogies that work:**
- Photon as "indivisible coin in the energy transaction" — clean, doesn't overpromise.
- de Broglie wave as "the wave whose interference tells you where particles will land, not the particle itself" — gets the student to Born rule (Unit 3) without saying the words.

**Analogies that mislead:**
- "Light is sometimes a wave and sometimes a particle." Pop-sci framing that suggests light *switches modes*. It doesn't — it has properties that classical particle/wave language cannot simultaneously accommodate. Replace with "light is quantum and the wave/particle vocabulary is a classical limit on each side."
- The "wavicle" coinage. Cute, useless. Cut.

**Exercises (Bloom's level):**
- **Knowledge:** State Planck's law, the photoelectric equation, the Compton formula, the de Broglie relation. (L1)
- **Application:** Compute threshold wavelengths for given work functions; predict diffraction peaks for given electron energies. (L3)
- **Analysis:** Given a hypothetical experiment, identify which classical prediction it violates and which quantum prediction it confirms. (L4)
- **Evaluation:** Read a paragraph of Millikan (1916) describing his expectations; analyze the gap between data and his interpretive commitment. (L5)
- **Synthesis:** Construct the chain from de Broglie relation → Bragg condition → Davisson–Germer measurement to predict their result before reading the experimental section. (L6)

---

## F. Library files relevant to this unit

- **Griffiths, *Introduction to Quantum Mechanics*** — Ch. 1 (introduction) covers the historical motivation. Pull problems from Ch. 1 problem set for the worked examples. (`822531304-David-J-Griffiths-Introduction-to-Quantum-Mechanics-Prentice-Hall-1994.txt` in pantry — this is the 1st edition; cite Ch. 1 sections and adjust for current edition.)
- **Liboff, *Introductory Quantum Mechanics*** — covers blackbody and photoelectric in early chapters with more historical detail than Griffiths. (`436681929-Introductory-Quantum-Mechanics-by-Richard-L-Liboff-pdf.txt`.)
- **Pop-sci references** (Quantum Physics for Beginners 2021 — 4 .txt files in pantry, and Strange World of Quantum Physics 2022): Ch. 3 (blackbody), Ch. 4 (photoelectric), Ch. 5 (de Broglie), Ch. 6 (Franck-Hertz), Ch. 10 (Compton), Ch. 11 (duality) — TIKTOC marks these as ✅ or ⚠️ but accurate; assign as motivational reading.
- **`_lib_QM-Into-the-Light-Beginners.md`** — pop-sci reference notes; useful for student-facing analogies.
- **`_lib_Significant-Figures-Stewart.md`** — Stewart's biographical sketches of Planck and Einstein could supply human-interest material if the chapter's hook needs it.

---

## G. Gaps and flags

- **FLAG:** Griffiths chapter numbering shifts between editions (1st, 2nd, 3rd). The pantry text is the 1st edition. The chapter author should cross-check section numbers against whichever edition is being adopted for the course.
- **FLAG:** The 1989 Tonomura paper citation is *American Journal of Physics* 57(2), 117–120, "Demonstration of single-electron buildup of an interference pattern" — [verify exact pagination from AJP archive before publishing].
- **GAP:** The Lummer–Pringsheim primary data are in turn-of-century *Verhandlungen* papers that are hard to retrieve. For pedagogical purposes Kuhn (1978) or Jammer (1966) is the standard secondary source.
- **GAP:** Translation quality of de Broglie's thesis varies — the Kracklauer 2004 translation is the most commonly cited but the de Broglie Foundation hosting may not be permanent. [verify URL stability before final draft.]
- **FLAG:** The pop-sci book's Klein–Nishina mention (TIKTOC Ch. 10) should be corrected — the formula it names is not the wavelength shift but the cross section. Companion chapter should make this distinction explicit in a sidebar or footnote.
