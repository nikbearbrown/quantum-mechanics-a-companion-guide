# Simulation Ideas — quantum-mechanics-a-companion-guide

Medhavy-register "Claude Code + Manim" workflow reels. The physics is the excuse;
the lesson is the prompt→read→run→check→change loop.

---

## Sim-01 — Photoelectric Threshold (3-sim reel)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: K_max = hν − φ; threshold at ν₀ = φ/h
- Concrete numbers: Na work function φ = 2.28 eV; photons at 700 nm (1.77 eV, blocked), 546 nm (2.27 eV, blocked), 300 nm (4.13 eV, K = 1.85 eV ejected)
- Visual artifact: three photon arrows (red, green, UV) hitting a sodium surface; red/green produce ✗, UV launches an electron arrow scaled as √K
- Two testable predictions: P1: 546 nm (E = 2.27 eV < φ) → zero electrons even at maximum intensity; P2: 300 nm (E = 4.13 eV) → K = 1.85 eV, electron speed ∝ √1.85
- Sim slug: medhavy-companion-photoelectric
- Note: CROSS-REFERENCE — this concept is built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B01–B04). Do not rebuild; link to that reel.

---

## Sim-02 — Compton Scattering (cross-reference)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Physical rule: Δλ = (h/m_e c)(1 − cos θ), λ_C = 2.426 pm
- Note: CROSS-REFERENCE — built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B05–B08). Do not rebuild.

---

## Sim-03 — UV Catastrophe (cross-reference)
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Physical rule: Planck ρ(ν) = 8πhν³/c³ · 1/(e^(hν/kT)−1) vs Rayleigh-Jeans ρ_RJ = 8πν²kT/c³
- Note: CROSS-REFERENCE — built in quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims (B09–B12). Do not rebuild.

---

## Sim-04 — Particle in a Box: Zero-Point Energy and n² Spectrum
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n = n²π²ℏ²/(2mL²); ground state at n=1, never zero
- Concrete numbers: L = 1 nm, electron: E₁ ≈ 0.376 eV, E₂ ≈ 1.504 eV, E₃ ≈ 3.384 eV; ratios 1:4:9
- Visual artifact: energy ladder with sine-wave eigenfunctions drawn at each rung; squeezing L visibly raises E₁
- Two testable predictions: P1: E₂/E₁ = 4.000 exactly; P2: halving L quadruples E₁ (E₁ ∝ 1/L²)
- Sim slug: medhavy-companion-pib
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/medhavy-companion-pib/medhavy-companion-pib-review.mp4`
- Note: CROSS-REFERENCE — vox-pib-zero-point is an explainer in this same book. The simulation workflow reel (showing Claude Code building the scene) is new and distinct; build it.

---

## Sim-05 — Quantum Tunneling: Exponential Barrier Dependence
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: T ≈ e^(−2κd), κ = √(2m(V₀−E))/ℏ; for φ≈4 eV, κ ≈ 1 Å⁻¹ → factor of 7 per Å
- Concrete numbers: V₀ = 1 eV, E = 0.5 eV, d varies 0.5–2 nm; T changes by e^(2×1.02×d) per Å step
- Visual artifact: wave decaying through barrier; log(T) vs d plot showing linear slope = −2κ
- Two testable predictions: P1: at d = 0 transmission T = 1 (no barrier); P2: each 1 Å increase multiplies T by e^(−2κ) ≈ 1/7.4 for typical metals
- Sim slug: medhavy-companion-tunneling
- Status: BUILT
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/medhavy-companion-tunneling/medhavy-companion-tunneling-review.mp4`
