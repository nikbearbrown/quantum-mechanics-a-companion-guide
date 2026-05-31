# CAJAL SVG Generation Log — Quantum Mechanics: A Companion Guide

**Book:** Quantum Mechanics — A Companion Guide
**Generated:** 2026-05-26
**Author:** Humanitarians AI
**Method:** Stub overwrite. All 49 existing SVG stubs (template placeholders with truncated titles) were replaced with Brutalist CAJAL content driven by the pantry cajal specs. Same filenames retained, same chapter coverage.

## Pipeline

1. SETUP — copied `SCRIPTS/svg-to-png.mjs` and `package.json` from `physics-thermodynamics`; ran `npm install sharp` for 300 DPI raster conversion.
2. SVG generation — read each `*-cajal.md` spec in `pantry/`, read the existing stub (read-then-write safety), wrote the Brutalist replacement.
3. Validation — `xmllint --noout` on the full directory caught one unescaped `<` in 06-the-hydrogen-atom-fig-05; fixed to `&lt;`.
4. Raster — `node SCRIPTS/svg-to-png.mjs` produced 49 PNGs at 300 DPI.

## Inventory

### Ch 01 — Why Quantum Mechanics (5 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | rayleigh-jeans-uv-catastrophe | quantitative | Critical |
| 02 | photoelectric-stopping-potential | quantitative | Critical |
| 03 | compton-scattering-geometry | conceptual | Important |
| 04 | tonomura-buildup | application | Critical |
| 05 | franck-hertz-current-voltage | quantitative | Important |

### Ch 02 — Mathematical Foundations (5 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | double-slit-buildup | application | Critical |
| 02 | complex-plane | conceptual | Critical |
| 03 | interference-intensity | quantitative | Important |
| 04 | sequential-stern-gerlach | application | Critical |
| 05 | hermitian-properties | reference | Important |

### Ch 03 — The Schrödinger Equation (7 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | schrodinger-vs-diffusion | comparison | Important |
| 02 | ground-state-probability-density | quantitative | Important |
| 03 | continuity-equation | conceptual | Critical |
| 04 | phasor-beating | conceptual | Critical |
| 05 | wave-packet-width | quantitative | Important |
| 06 | tdse-anatomy | reference | Important |
| 07 | superposition-snapshots | application | Important |

### Ch 04 — One-Dimensional Problems (6 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | infinite-well-eigenfunctions | conceptual | Critical |
| 02 | correspondence-principle | conceptual | Important |
| 03 | harmonic-oscillator-eigenfunctions | conceptual | Critical |
| 04 | finite-square-well | conceptual | Critical |
| 05 | alpha-decay-tunneling | application | Critical |
| 06 | geiger-nuttall-plot | quantitative | Important |

### Ch 05 — Quantum Formalism (1 fig)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | robertson-proof-structure | conceptual | Important |

*Note:* The cajal spec called for 3 figures (Robertson + three-uncertainties comparison + Schlosshauer survey), but only fig-01 stub exists. The other two could be added later as new files if the chapter density warrants.

### Ch 06 — The Hydrogen Atom (6 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | hydrogen-emission-spectrum | quantitative | Critical |
| 02 | effective-potential | quantitative | Important |
| 03 | 1s-radial-wave-function | quantitative | Critical |
| 04 | 1s-radial-probability | quantitative | Critical |
| 05 | orbital-isosurfaces | conceptual | Critical |
| 06 | hydrogen-energy-levels | reference | Important |

### Ch 07 — Angular Momentum (3 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | angular-momentum-ladder | conceptual | Critical |
| 02 | spherical-harmonics-shapes | conceptual | Critical |
| 03 | singlet-measurement | application | Critical |

*Note:* The cajal spec called for 5 figures (3 author-placed + 2 CAJAL adds for 720° rotation + WCOE neutron interferometer). Only the 3 author-placed stubs exist.

### Ch 08 — Identical Particles (5 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | slater-determinant-anatomy | reference | Important |
| 02 | exchange-correlation | conceptual | Critical |
| 03 | helium-singlet-triplet | quantitative | Critical |
| 04 | madelung-filling | reference | Important |
| 05 | fd-be-mb-distributions | quantitative | Critical |

### Ch 09 — Approximation Methods (4 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | level-repulsion | conceptual | Important |
| 02 | hydrogen-stark-effect | quantitative | Important |
| 03 | variational-helium | quantitative | Important |
| 04 | sinc-squared-delta | quantitative | Important |

*Note:* The cajal spec adds a 5th figure (WKB wave function across turning points). Stub does not exist; could be added as fig-05.

### Ch 10 — Quantum Mechanics in the Modern World (7 figs)

| # | Slug | Type | Priority |
|---|------|------|----------|
| 01 | chsh-bounds | quantitative | Critical |
| 02 | three-level-laser | conceptual | Important |
| 03 | band-diagrams | conceptual | Critical |
| 04 | bell-state-circuit | conceptual | Important |
| 05 | quantum-algorithm-scaling | quantitative | Important |
| 06 | superconductor-tc-timeline | quantitative | Important |
| 07 | stm-tunneling | application | Important |

## Totals

49 figures × (1 SVG + 1 PNG @ 300 DPI) = 98 files.

Chapter-by-chapter: 5 + 5 + 7 + 6 + 1 + 6 + 3 + 5 + 4 + 7 = 49.

## Editorial notes

- All stubs were template placeholders with truncated titles like "Plot of Rayleigh–Jeans vs". User chose "overwrite existing stubs (same slugs)" path; no slug remapping or stub deletion required.
- Five chapters have a cajal-spec figure count higher than the existing stub count (Ch 05: 1 of 3; Ch 07: 3 of 5; Ch 09: 4 of 5). If the missing figures are wanted, they can be added as new `fig-NN` files following the same Brutalist template.
- One xmllint error caught and fixed: `06-the-hydrogen-atom-fig-05.svg` had unescaped `<` in `<text>` content. Standard CAJAL bug; lesson reinforced.
- All figures follow the Brutalist house style: viewBox 700×420 (or 460/480 where vertical space needed), Okabe-Ito palette, EB Garamond titles, Inter labels, JetBrains Mono numerics/equations. Each has aria-labelledby + role="img" + cajal:figure metadata.
