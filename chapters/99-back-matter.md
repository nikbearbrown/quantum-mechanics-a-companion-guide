---

## Acknowledgments

The students of computational physics, AI-for-engineering, and the cross-listed quantum-mechanics-for-data-scientists offerings at Northeastern who served as the diagnostic test population for this book over more than a decade. Particular thanks to the ones who arrived in my office with a popular-science quantum book in one hand and Griffiths in the other and asked, in some form, "which one of these is lying?" That question is the book.

Thanks to the colleagues across physics, chemistry, and engineering who read the unit drafts and pushed back where the math was thin or where the diagnostic claims were too strong. Where this companion gets the audit right, it owes them. Where it gets it wrong, the responsibility is mine.

The Griffiths text — *Introduction to Quantum Mechanics*, by David J. Griffiths and Darrell F. Schroeter — is the rigorous backbone this companion is built to support. I have used Griffiths in my teaching for more than a decade and continue to recommend it to every student of undergraduate quantum mechanics.

The popular-science quantum books that this companion audits exist on a wide quality spectrum. The standard recycled misconceptions named in this book recur across the genre regardless of authorship. The audit framework presented in TIKTOC.md and applied across the units is what generalizes; the specific exemplar audited is one of many that could have been chosen.

---

## About the Author

**Nik Bear Brown** is an Associate Teaching Professor at Northeastern University's College of Engineering, where he teaches data science, AI, computational physics, visualization, and graduate courses on AI-augmented learning. His Ph.D. is in computer science from UCLA, with major field in computational and systems biology and minor fields in artificial intelligence and statistics. He holds a master's in Information Design and Data Visualization and an MBA from Northeastern, and a B.A. in biochemistry and molecular biology from UC Santa Cruz. He was an NSF IGERT Bioinformatics Fellow and did a part-time postdoc in deep learning at Harvard Medical School while teaching at Northeastern; before academia he was a molecular biologist at DNAX Research Institute and Cetus Corporation.

His cross-domain teaching background is what makes this companion possible. He is not a working quantum theorist; he is the cross-domain instructor who has watched over a decade of physics, chemistry, and engineering undergraduates try to read the two genres of quantum-mechanics book — the rigorous undergraduate text and the popular-science treatment — and bounce off the gap between them. The companion is the diagnostic document he wished existed when he was teaching them.

He is the author of the *with LLMs* textbook series, the architect of the **Brutalist** system for AI-assisted creative production ([brutalist.art](https://www.brutalist.art/)), and the founder of [Humanitarians AI](https://www.humanitarians.ai/) (a 501(c)(3) supporting OPT and H-1B fellows in production-scale AI work). His larger framework, **[Irreducibly Human](https://irreducibly.xyz)**, addresses the cognitive capacities the AI era most urgently requires humans to develop. He writes at [nikbearbrown.com](https://www.nikbearbrown.com) and [skepticism.ai](https://www.skepticism.ai). Reach him at [bear@bearbrown.co](mailto:bear@bearbrown.co).

Pronouns: they/them. Fun fact: once ran away with the circus, worked as a photojournalist, and did sumo wrestling.

---

## Notes

### Unit 1 — Why Quantum Mechanics?
1. Planck 1901, "Über das Gesetz der Energieverteilung im Normalspektrum," *Annalen der Physik* 4, 553. The original quantization hypothesis.
2. Einstein 1905, "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt," *Annalen der Physik* 17, 132. The photoelectric paper; Nobel Prize 1921.
3. Compton 1923, "A Quantum Theory of the Scattering of X-rays by Light Elements," *Physical Review* 21, 483.
4. de Broglie 1924, thesis, University of Paris. Davisson & Germer 1927, "Diffraction of Electrons by a Crystal of Nickel," *Physical Review* 30, 705.
5. Franck & Hertz 1914, "Über Zusammenstöße zwischen Elektronen und den Molekülen des Quecksilberdampfes und die Ionisierungsspannung desselben," *Verhandlungen der Deutschen Physikalischen Gesellschaft* 16, 457.

### Unit 2 — Mathematical Foundations
1. Dirac 1939, "A New Notation for Quantum Mechanics," *Mathematical Proceedings of the Cambridge Philosophical Society* 35, 416. The origin of bra-ket notation.
2. Reed & Simon, *Methods of Modern Mathematical Physics, Vol. 1: Functional Analysis*. The rigorous functional-analysis backbone behind Hilbert space.
3. Shankar, *Principles of Quantum Mechanics*, 2nd ed., Chapter 1. The cleanest undergraduate mathematical-foundations chapter in print.

### Unit 3 — The Schrödinger Equation
1. Schrödinger 1926, four-paper series, *Annalen der Physik* 79–81. The original derivation of the equation.
2. Born 1926, "Zur Quantenmechanik der Stoßvorgänge," *Zeitschrift für Physik* 37, 863. The probabilistic interpretation.
3. Griffiths §1.2 makes the "postulated, not derived" point explicit; cite his framing.

### Unit 4 — One-Dimensional Problems
1. Griffiths §2.2 (box), §2.3 (oscillator, both methods), §2.6 (finite well), Ch. 9 (WKB).
2. Gamow 1928, "Zur Quantentheorie des Atomkernes," *Zeitschrift für Physik* 51, 204. Alpha decay via tunneling.
3. Binnig & Rohrer 1982, "Scanning Tunneling Microscopy," *Physical Review Letters* 49, 57. Nobel 1986.

### Unit 5 — Quantum Formalism
1. **Heisenberg 1927**, "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik," *Zeitschrift für Physik* 43, 172. The original *epistemic* (microscope) uncertainty argument — the source of the balloon-analogy misconception.
2. **Robertson 1929**, "The Uncertainty Principle," *Physical Review* 34, 163. The corrected general inequality, derived from Cauchy-Schwarz, intrinsic to the state.
3. Schrödinger 1930, *Berliner Berichte*. The further-refined covariance form.
4. Bell 1990, "Against 'Measurement,'" *Physics World* 3, 33. The canonical critique of the measurement-problem evasions.
5. Schlosshauer 2007, *Decoherence and the Quantum-to-Classical Transition*. Springer. The reference book on decoherence.
6. Schlosshauer, Kofler & Zeilinger 2013, "A Snapshot of Foundational Attitudes Toward Quantum Mechanics," *Studies in History and Philosophy of Modern Physics* 44, 222. The survey documenting the absence of consensus on interpretation.
7. Frauchiger & Renner 2018, "Quantum Theory Cannot Consistently Describe the Use of Itself," *Nature Communications* 9, 3711.

### Unit 6 — The Hydrogen Atom
1. Bohr 1913, "On the Constitution of Atoms and Molecules," *Philosophical Magazine* 26, 1.
2. Pauli 1926, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik," *Zeitschrift für Physik* 36, 336. The algebraic solution via the SO(4) symmetry.
3. Schrödinger 1926 (Unit 3 references). The wave-mechanical solution.
4. Stern & Gerlach 1922, *Zeitschrift für Physik* 9, 349. Quantization of spin angular momentum.
5. Dirac 1928, "The Quantum Theory of the Electron," *Proceedings of the Royal Society A* 117, 610. Spin from relativistic QM.
6. Pauli 1925, "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren," *Zeitschrift für Physik* 31, 765. The exclusion principle.

### Unit 7 — Angular Momentum
1. Pauli 1927, *Zeitschrift für Physik* 43, 601. Pauli matrices.
2. Werner et al. 1975, *Physical Review Letters* 35; Rauch et al. 1975, *Physics Letters A* 54. Neutron interferometry confirming the $4\pi$ rotational symmetry of spin-1/2.
3. Berry 1984, "Quantal Phase Factors Accompanying Adiabatic Changes," *Proceedings of the Royal Society A* 392, 45. The Berry / geometric phase.
4. Bohm 1951, *Quantum Theory*, §22. The cleaner spin-1/2 reformulation of EPR.

### Unit 8 — Identical Particles
1. **Pauli 1940**, "The Connection Between Spin and Statistics," *Physical Review* 58, 716. The spin-statistics theorem.
2. Slater 1929, *Physical Review* 34, 1293. The Slater determinant.
3. Anderson et al. 1995, *Science* 269, 198. The first observed Bose-Einstein condensate.
4. Davis et al. 1995, *Physical Review Letters* 75, 3969. Sodium BEC.
5. Chandrasekhar 1931, *Astrophysical Journal* 74, 81. White dwarf mass limit from electron degeneracy pressure.

### Unit 9 — Approximation Methods
1. Dirac 1927, "The Quantum Theory of the Emission and Absorption of Radiation," *Proceedings of the Royal Society A* 114, 243. The actual origin of what is now called Fermi's golden rule.
2. Fermi 1950, *Nuclear Physics: A Course Given by Enrico Fermi at the University of Chicago*. The coinage of "golden rule."
3. Einstein 1917, "Zur Quantentheorie der Strahlung," *Physikalische Zeitschrift* 18, 121. A and B coefficients.
4. Hylleraas 1929, *Zeitschrift für Physik* 54, 347. Variational calculation of the helium ground state.
5. Wentzel 1926 (*Z. Phys.* 38); Kramers 1926 (*Z. Phys.* 39); Brillouin 1926 (*C. R. Acad. Sci.*). Independent WKB derivations.
6. Dyson 1952, *Physical Review* 85, 631. The asymptotic nature of perturbation series.

### Unit 10 — Quantum Mechanics in the Modern World
1. EPR 1935, *Physical Review* 47, 777. The original paradox.
2. Bell 1964, "On the Einstein Podolsky Rosen Paradox," *Physics Physique Fizika* 1, 195. The inequality.
3. Aspect, Dalibard & Roger 1982, *Physical Review Letters* 49, 1804. The classic experimental violation.
4. Hensen et al. 2015, *Nature* 526, 682; Giustina et al. 2015, *Physical Review Letters* 115, 250401; Shalm et al. 2015, *Physical Review Letters* 115, 250402. The 2015 loophole-free Bell tests.
5. Nobel Prize in Physics 2022 — Aspect, Clauser, Zeilinger.
6. Bardeen, Cooper & Schrieffer 1957, *Physical Review* 108, 1175. BCS theory of superconductivity.
7. Bednorz & Müller 1986, *Zeitschrift für Physik B* 64, 189. High-temperature superconductivity.
8. Shor 1994, "Algorithms for Quantum Computation," *Proceedings of the 35th Annual Symposium on Foundations of Computer Science*. Quantum factoring.
9. NIST 2024, FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA). Post-quantum cryptography standards.

---

## References

Anderson, M. H., et al. "Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor." *Science* 269 (1995): 198–201.

Aspect, Alain, Jean Dalibard, and Gérard Roger. "Experimental Test of Bell's Inequalities Using Time-Varying Analyzers." *Physical Review Letters* 49 (1982): 1804–1807.

Bardeen, J., L. N. Cooper, and J. R. Schrieffer. "Theory of Superconductivity." *Physical Review* 108 (1957): 1175–1204.

Bell, John S. "On the Einstein Podolsky Rosen Paradox." *Physics Physique Fizika* 1 (1964): 195–200.

Bell, John S. "Against 'Measurement.'" *Physics World* 3, no. 8 (1990): 33–40.

Bender, Carl M., and Steven A. Orszag. *Advanced Mathematical Methods for Scientists and Engineers I: Asymptotic Methods and Perturbation Theory*. Springer, 1978.

Berry, M. V. "Quantal Phase Factors Accompanying Adiabatic Changes." *Proceedings of the Royal Society A* 392 (1984): 45–57.

Binnig, Gerd, and Heinrich Rohrer. "Scanning Tunneling Microscopy." *Physical Review Letters* 49 (1982): 57–61.

Bohm, David. *Quantum Theory*. Prentice-Hall, 1951.

Bohr, Niels. "On the Constitution of Atoms and Molecules." *Philosophical Magazine* 26 (1913): 1–25.

Born, Max. "Zur Quantenmechanik der Stoßvorgänge." *Zeitschrift für Physik* 37 (1926): 863–867.

Chandrasekhar, Subrahmanyan. "The Maximum Mass of Ideal White Dwarfs." *Astrophysical Journal* 74 (1931): 81–82.

Cohen-Tannoudji, Claude, Bernard Diu, and Franck Laloë. *Quantum Mechanics*. Wiley, 1977.

Compton, Arthur H. "A Quantum Theory of the Scattering of X-rays by Light Elements." *Physical Review* 21 (1923): 483–502.

Davis, K. B., et al. "Bose-Einstein Condensation in a Gas of Sodium Atoms." *Physical Review Letters* 75 (1995): 3969–3973.

Davisson, C., and L. H. Germer. "Diffraction of Electrons by a Crystal of Nickel." *Physical Review* 30 (1927): 705–740.

de Broglie, Louis. "Recherches sur la théorie des quanta." Ph.D. thesis, University of Paris, 1924.

Dirac, P. A. M. "The Quantum Theory of the Emission and Absorption of Radiation." *Proceedings of the Royal Society A* 114 (1927): 243–265.

Dirac, P. A. M. "The Quantum Theory of the Electron." *Proceedings of the Royal Society A* 117 (1928): 610–624.

Dirac, P. A. M. "A New Notation for Quantum Mechanics." *Mathematical Proceedings of the Cambridge Philosophical Society* 35 (1939): 416–418.

Dyson, F. J. "Divergence of Perturbation Theory in Quantum Electrodynamics." *Physical Review* 85 (1952): 631–632.

Einstein, Albert. "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt." *Annalen der Physik* 17 (1905): 132–148.

Einstein, Albert. "Zur Quantentheorie der Strahlung." *Physikalische Zeitschrift* 18 (1917): 121–128.

Einstein, Albert, Boris Podolsky, and Nathan Rosen. "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" *Physical Review* 47 (1935): 777–780.

Fermi, Enrico. *Nuclear Physics: A Course Given by Enrico Fermi at the University of Chicago*. University of Chicago Press, 1950.

Franck, James, and Gustav Hertz. "Über Zusammenstöße zwischen Elektronen und den Molekülen des Quecksilberdampfes und die Ionisierungsspannung desselben." *Verhandlungen der Deutschen Physikalischen Gesellschaft* 16 (1914): 457–467.

Frauchiger, D., and R. Renner. "Quantum Theory Cannot Consistently Describe the Use of Itself." *Nature Communications* 9 (2018): 3711.

Gamow, George. "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik* 51 (1928): 204–212.

Giustina, Marissa, et al. "Significant-Loophole-Free Test of Bell's Theorem with Entangled Photons." *Physical Review Letters* 115 (2015): 250401.

Griffiths, David J., and Darrell F. Schroeter. *Introduction to Quantum Mechanics*. 3rd ed. Cambridge University Press, 2018.

Heisenberg, Werner. "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik." *Zeitschrift für Physik* 43 (1927): 172–198.

Hensen, B., et al. "Loophole-Free Bell Inequality Violation Using Electron Spins Separated by 1.3 Kilometres." *Nature* 526 (2015): 682–686.

Hylleraas, Egil A. "Neue Berechnung der Energie des Heliums im Grundzustande, sowie des tiefsten Terms von Ortho-Helium." *Zeitschrift für Physik* 54 (1929): 347–366.

Liboff, Richard L. *Introductory Quantum Mechanics*. 4th ed. Addison-Wesley, 2003.

Pauli, Wolfgang. "Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren." *Zeitschrift für Physik* 31 (1925): 765–783.

Pauli, Wolfgang. "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik." *Zeitschrift für Physik* 36 (1926): 336–363.

Pauli, Wolfgang. *Zeitschrift für Physik* 43 (1927): 601. [Pauli matrices.]

Pauli, Wolfgang. "The Connection Between Spin and Statistics." *Physical Review* 58 (1940): 716–722.

Planck, Max. "Über das Gesetz der Energieverteilung im Normalspektrum." *Annalen der Physik* 4 (1901): 553–563.

Reed, Michael, and Barry Simon. *Methods of Modern Mathematical Physics, Vol. 1: Functional Analysis*. Academic Press, 1980.

Robertson, H. P. "The Uncertainty Principle." *Physical Review* 34 (1929): 163–164.

Schlosshauer, Maximilian. *Decoherence and the Quantum-to-Classical Transition*. Springer, 2007.

Schlosshauer, Maximilian, Johannes Kofler, and Anton Zeilinger. "A Snapshot of Foundational Attitudes Toward Quantum Mechanics." *Studies in History and Philosophy of Modern Physics* 44 (2013): 222–230.

Schrödinger, Erwin. "Quantisierung als Eigenwertproblem (Erste Mitteilung)." *Annalen der Physik* 79 (1926): 361–376. [And the three subsequent papers in the same year.]

Shalm, Lynden K., et al. "Strong Loophole-Free Test of Local Realism." *Physical Review Letters* 115 (2015): 250402.

Shankar, R. *Principles of Quantum Mechanics*. 2nd ed. Plenum Press, 1994.

Shor, Peter W. "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *Proceedings of the 35th Annual Symposium on Foundations of Computer Science* (1994): 124–134.

Slater, John C. "The Theory of Complex Spectra." *Physical Review* 34 (1929): 1293–1322.

Stern, Otto, and Walther Gerlach. "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld." *Zeitschrift für Physik* 9 (1922): 349–352.

---

## On the Absence of an Index

This is a Kindle and online book. It does not include a printed index. Three reasons.

First, e-reader search makes printed indexes obsolete for this format — every term in the book is one keystroke away. Second, this book is integrated with **Medhavy** ([medhavy.com](https://www.medhavy.com/)) — मेधावी, from the Sanskrit for *intelligent* — an AI-powered intelligent textbook platform that indexes the book semantically rather than alphabetically. Search Medhavy for a misconception and it will surface the unit that corrects it. Third, the companion's structure — ten units, each opening with a Reading Map — already functions as an index. If you need to find where the book treats the balloon analogy, you open Unit 5. If you need to find where it treats Pauli exclusion, you open Unit 8. The Reading Map at the head of each unit cross-references both Griffiths and the audited popular-science exemplar.

Come learn something with us.

---

## Glossary

**Born rule.** $P(x, t) = |\psi(x, t)|^2$. The probability density of finding the particle at position $x$. Postulated, not derived. Cited in popular-science books constantly; cited correctly in Griffiths §1.3.

**Bra-ket notation.** Dirac's notation: $|\psi\rangle$ is a ket (state vector); $\langle\phi|$ is the dual; $\langle\phi|\psi\rangle$ is the inner product. Unit 2 supplies the math popular-science books omit.

**CHSH inequality.** Clauser-Horne-Shimony-Holt 1969. The form of Bell's inequality used in modern Bell tests. $|S| \leq 2$ classically; $|S| \leq 2\sqrt{2}$ quantum-mechanically (Tsirelson bound). Unit 10.

**Cauchy-Schwarz inequality.** $|\langle f, g\rangle|^2 \leq \langle f, f\rangle\langle g, g\rangle$. The inequality from which Robertson 1929 derived the rigorous form of the uncertainty principle. Unit 5.

**Coherent state.** A superposition of harmonic-oscillator eigenstates that maintains a Gaussian shape and oscillates classically. The eigenstate of the lowering operator. Unit 4.

**Decoherence.** The process by which quantum coherences are suppressed via entanglement with environmental degrees of freedom. Explains the quantum-to-classical transition without resolving the measurement problem. Unit 5 + Unit 10.

**Eigenvalue / eigenstate.** $\hat{O}|\psi\rangle = \lambda|\psi\rangle$. Measurements yield eigenvalues; the system is projected into the corresponding eigenstate. Unit 2.

**Entanglement.** A state of two or more subsystems that cannot be written as a product of individual states. Generates non-classical correlations that violate Bell inequalities. *Not* faster-than-light communication. Unit 10.

**Fermi's golden rule.** $W_{i\to f} = (2\pi/\hbar) |\langle f|\hat{H}'|i\rangle|^2 \rho(E_f)$. Misnamed — derived by Dirac in 1927. Unit 9.

**Hamiltonian.** $\hat{H}$. The operator whose eigenvalues are the system's allowed energies. Generates time evolution via $i\hbar \partial_t |\psi\rangle = \hat{H}|\psi\rangle$. Unit 3.

**Hermitian operator.** $\hat{O}^\dagger = \hat{O}$. For *complex* matrices, this means the conjugate transpose equals the matrix, NOT just the transpose. Real eigenvalues. Observables correspond to Hermitian operators. Unit 2.

**Pauli matrices.** $\sigma_x, \sigma_y, \sigma_z$. The 2×2 Hermitian generators of SU(2). Spin-1/2 operators are $S_i = (\hbar/2)\sigma_i$. Unit 7.

**Pauli exclusion principle.** No two electrons in an atom share all four quantum numbers $(n, \ell, m_\ell, m_s)$. In Unit 8 this is shown to be a *consequence* of antisymmetry under exchange, not a separate postulate.

**Robertson uncertainty.** $\sigma_A \sigma_B \geq (1/2) |\langle [\hat{A}, \hat{B}]\rangle|$. Robertson 1929. Intrinsic to the state. Derived from Cauchy-Schwarz. NOT a measurement-disturbance phenomenon. The corrected form of the principle Heisenberg first proposed informally in 1927. Unit 5.

**Schrödinger equation.** $i\hbar \partial_t |\psi\rangle = \hat{H}|\psi\rangle$ (time-dependent); $\hat{H}|\psi\rangle = E|\psi\rangle$ (time-independent). Postulated, not derived. Unit 3.

**Singlet state.** $|0,0\rangle = (|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)/\sqrt{2}$. The maximally entangled state of two spin-1/2 particles. The canonical EPR state. Unit 7 (constructed); Unit 10 (used in Bell tests).

**Slater determinant.** $\psi = (1/\sqrt{N!}) \det[\phi_i(x_j)]$. Automatically antisymmetric. Vanishes if any two electrons share a state — Pauli exclusion built in. Unit 8.

**Spherical harmonics.** $Y_{\ell m}(\theta, \phi)$. Eigenfunctions of $\hat{L}^2$ and $\hat{L}_z$. The angular part of central-potential wave functions. Unit 6.

**Spin.** Intrinsic angular momentum. Not classical rotation (the classical picture gives equator speeds > c). Derivable from relativistic QM (Dirac 1928). Unit 6, Unit 7.

**Stern-Gerlach experiment.** Stern & Gerlach 1922. Silver atoms passing through an inhomogeneous magnetic field split into two beams, revealing the quantization of spin angular momentum. Unit 6.

**Stationary state.** An energy eigenstate. $|\psi|^2$ is time-independent; the wave function evolves only by a global phase $e^{-iEt/\hbar}$. Common misconception: "stationary states don't change in time" — they do change by a time-dependent phase that matters for superpositions.

**Wave function.** $\psi(x, t)$. Complex-valued probability amplitude. Not the particle. Not the energy distribution. Not the orbit. Unit 1, Unit 3.

**WKB approximation.** Wentzel-Kramers-Brillouin 1926. Semi-classical approximation in $\hbar$. Foundation of the tunneling formula and Bohr-Sommerfeld quantization. Unit 4.

---

## Errata

Reported errors and corrections are maintained at [nikbearbrown.com/qm-companion-errata](https://www.nikbearbrown.com) (link active after publication).

To report an error: [bear@bearbrown.co](mailto:bear@bearbrown.co).

⚡ Fun fact: I once ran away with the circus, was a photojournalist, and did sumo wrestling.
