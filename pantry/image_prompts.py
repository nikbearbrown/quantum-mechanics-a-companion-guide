"""
Image prompts collected from CAJAL pantry files for the
quantum-mechanics-a-companion-guide book.

Each element is a self-contained prompt suitable for image generation.
Style baseline across all prompts: flat vector, white background,
Okabe-Ito colorblind-safe palette (no red-green combinations),
no text labels in image (typography applied post-generation),
no human figures, no shadows, no gradient fills, no 3D perspective.
"""

image_prompts = [
    # ---------- Chapter 1: Why Quantum Mechanics ----------

    # Fig 1.1 — Rayleigh-Jeans vs Planck
    "Single-column scientific figure, flat vector, white background. "
    "Spectral energy density (y-axis) vs frequency (x-axis), no numerical labels. "
    "Two curves on same axes from origin: Rayleigh-Jeans prediction in vermillion #D55E00 1pt solid, "
    "rising as nu-squared without bound and exiting top of panel with a small truncation arrow; "
    "Planck distribution in blue #0072B2 1pt solid, rising to a finite peak then falling exponentially "
    "to near-zero at the right edge. Vertical black 0.5pt dashed reference line at the Planck peak. "
    "Y-axis at exactly zero. No legend, no title, no text, no log scaling.",

    # Fig 1.2 — Photoelectric stopping potential vs frequency
    "Single-column scientific figure, flat vector, white background. "
    "Stopping potential (y-axis) vs frequency (x-axis), no numerical labels. "
    "Single blue #0072B2 1pt straight line with positive slope. Dashed segment to the left of the "
    "threshold frequency (no-emission region), solid segment to the right (emission region). "
    "Small orange #E69F00 filled circle at the x-intercept marking the threshold frequency. "
    "Below the dashed segment, a vermillion #D55E00 0.5pt dashed bracket spans the no-emission region. "
    "Black 1pt axes. No text labels, no equations, no work-function annotations.",

    # Fig 1.3 — Compton scattering geometry
    "Single-column scientific figure, flat vector, white background. "
    "Single scattering event at panel center-left. Black filled dot at the scattering vertex "
    "(initially-at-rest electron). Incident photon as a blue #0072B2 1pt arrow entering horizontally "
    "from the left to the vertex. Two outgoing arrows from the vertex: scattered photon in sky blue "
    "#56B4E9 1pt departing upward-rightward at angle theta above horizontal; recoiling electron in "
    "vermillion #D55E00 1pt departing downward-rightward at angle phi below horizontal. Small black "
    "0.5pt arc-of-angle indicators at the vertex marking theta and phi. No wavelength, momentum, or "
    "energy labels. No detectors, no graphite block, no Cartesian axes, no nucleus.",

    # Fig 1.4 — Tonomura buildup
    "Single-column scientific figure, flat vector, white background. Four equal-size rectangular "
    "detector panels in a horizontal row, each with black 1pt outline, separated by thin black 0.5pt "
    "vertical rules. Inside each panel, small blue #0072B2 filled dots positioned within an underlying "
    "vertical-stripe interference envelope. Panel 1: about 30 dots scattered apparently randomly. "
    "Panel 2: about 300 dots beginning to cluster into vertical stripes. Panel 3: about 1500 dots "
    "with clear vertical bright bands. Panel 4: about 5000 dots forming 5-7 sharp vertical fringes. "
    "Bright-fringe positions identical across panels; only sampling density increases. No labels, "
    "no source apparatus, no axis annotations, no scale bar.",

    # Fig 1.5 — Franck-Hertz current vs voltage
    "Single-column scientific figure, flat vector, white background. "
    "Collector current (y-axis) vs accelerating voltage (x-axis), no numerical labels. "
    "Single blue #0072B2 1pt curve with rising envelope but three sharp dips at regularly-spaced "
    "voltage positions (4.9, 9.8, 14.7 V), each followed by partial recovery. Three small orange "
    "#E69F00 filled upward-pointing triangle markers below the x-axis at the three dip positions. "
    "Y-axis at zero. No text, no equations, no apparatus, no atom diagrams, no multi-gas family.",

    # ---------- Chapter 2: Mathematical Foundations ----------

    # Fig 2.1 — Double-slit single-electron buildup
    "Single-column scientific figure, flat vector, white background. Two-region layout separated by "
    "a thin black 0.5pt vertical rule. Left region (apparatus): black filled dot electron source on far "
    "left with sky blue #56B4E9 1pt rightward arrow; vertical black 1pt barrier with two horizontal gaps "
    "(slits) at center; black 0.5pt vertical detector screen on right; sky blue 0.5pt fan-out arcs from "
    "each slit reaching the detector. Right region (buildup): three small inset panels stacked vertically "
    "showing detector hits accumulating with blue #0072B2 filled dots — sparse ~10 dots, clustering ~100, "
    "sharp vertical fringes ~1000. No wavelength or angle labels, no source-type designation.",

    # Fig 2.2 — The complex plane
    "Single-column scientific figure, flat vector, white background. Cartesian plane with horizontal "
    "real axis and vertical imaginary axis, both black 1pt with arrowheads at positive ends, origin at "
    "panel center. Blue #0072B2 filled small circle marking point z in the upper-right quadrant. Blue "
    "1pt solid line from origin to z. Black 0.5pt dashed vertical projection from z down to the real "
    "axis, and dashed horizontal projection from z to the imaginary axis. Black 0.5pt arc near origin "
    "indicating angle theta between positive real axis and the line to z. Vermillion #D55E00 filled "
    "circle for the complex conjugate z* in the lower-right quadrant (mirror across real axis), with "
    "a vermillion 0.5pt dashed line from origin to z*. No numerical labels, no equations, no unit circle.",

    # Fig 2.3 — Interference intensity pattern
    "Single-column scientific figure, flat vector, white background. "
    "Intensity (y-axis) vs angle (x-axis, symmetric around zero), no numerical labels. "
    "Single blue #0072B2 1pt curve in cosine-squared shape, oscillating between 0 and 2, with five to "
    "seven visible maxima across the panel width. Above the maxima, small orange #E69F00 filled "
    "downward-pointing triangles marking the bright-band positions. Black 0.5pt vertical tick marks "
    "at the zero positions (dark bands). Y-axis at zero, runs to about 2.2. Black 1pt axes. "
    "No equations, no wavelength labels, no Bragg annotations, no envelope from single-slit diffraction.",

    # Fig 2.4 — Stern-Gerlach sequential measurements
    "Double-column wide scientific figure, flat vector, white background. Strict horizontal left-to-right "
    "apparatus sequence: black filled rectangle oven source; sky blue #56B4E9 1pt beam arrow rightward; "
    "first blue #0072B2 1pt outlined box (sigma-z magnet) splitting beam into upper and lower paths; "
    "vermillion #D55E00 filled rectangle blocking the lower path; surviving upper path enters second "
    "blue outlined box (sigma-x magnet) splitting into upper and lower; one sigma-x output enters third "
    "blue outlined box (sigma-z magnet) which splits again into two outputs — the punchline that the "
    "original spin information is gone. All beams sky blue 1pt straight lines. No spin labels, no "
    "pole-piece geometry, no curved trajectories, no historical photographs.",

    # ---------- Chapter 3: The Schrödinger Equation ----------

    # Fig 3.1 — Schrödinger vs diffusion wave packet
    "Single-column scientific figure, flat vector, white background. Two side-by-side panels separated "
    "by a thin black 0.5pt vertical rule. Both panels: probability density (y-axis) vs position (x-axis), "
    "same axis ranges. Left panel (Schrödinger evolution): three blue #0072B2 1pt Gaussian curves at "
    "three times — sharp initial Gaussian at t=0, moderately wider at t1, much wider but still Gaussian "
    "at t2. Right panel (diffusion equation): three vermillion #D55E00 1pt curves at the same three "
    "times — same Gaussian at t=0, smoothed and lower amplitude at t1, nearly flat at t2. Y-axis at "
    "zero in both panels. No labels, no equations, no panel headers.",

    # Fig 3.2 — Ground-state probability density in infinite square well
    "Single-column scientific figure, flat vector, white background. Single blue #0072B2 1pt sine-squared "
    "curve over the interval [0, L]: starts at 0 at x=0, rises smoothly to maximum at x=L/2, falls "
    "smoothly back to 0 at x=L. The leftmost quarter [0, L/4] is filled with translucent orange #E69F00 "
    "at 25% opacity (highlighting the region whose probability is computed as approximately 0.091). "
    "Vertical black 0.5pt dashed reference lines at x=0, x=L/4, x=L/2, x=L. Short vertical black 1pt "
    "well-wall segments at x=0 and x=L. Y-axis at zero. No numerical labels, no equations, no second "
    "eigenstate, no animation cues.",

    # Fig 3.3 — Continuity equation / probability current across a region
    "Single-column scientific figure, flat vector, white background. Horizontal 1D axis. Rectangular "
    "region [a, b] filled with sky blue #56B4E9 at 25% opacity. Thin black 1pt vertical lines at x=a "
    "and x=b marking the boundaries. Inside the region, three small blue #0072B2 filled dots representing "
    "sample probability-density values. At x=a, a bluish green #009E73 1pt rightward arrow indicating "
    "incoming current j(a). At x=b, a vermillion #D55E00 1pt rightward arrow indicating outgoing current "
    "j(b). Above the shaded region, a black 1pt downward arrow indicating the rate of change of total "
    "probability inside. No equations, no labels, no specific density function curve.",

    # Fig 3.4 — Phasor beating: one stationary state vs two
    "Single-column scientific figure, flat vector, white background. Two side-by-side panels separated "
    "by a thin black 0.5pt vertical rule. Left panel (one phasor): upper sub-panel shows an Argand "
    "diagram with a single blue #0072B2 filled arrow from origin to a point on the unit circle, with a "
    "small black 0.5pt curved arrow indicating counterclockwise rotation; lower sub-panel shows a flat "
    "horizontal sky blue #56B4E9 1pt line representing |psi|^2 constant in time. Right panel (two "
    "phasors): upper sub-panel shows two arrows from origin (blue #0072B2 and orange #E69F00) rotating "
    "at different rates, plus a reddish purple #CC79A7 sum arrow; lower sub-panel shows a reddish purple "
    "1pt sinusoidal curve representing |psi|^2 oscillating in time at the Bohr frequency. No frequency "
    "labels, no equations, no spectral lines.",

    # Fig 3.5 — Gaussian wave packet width vs time
    "Single-column scientific figure, flat vector, white background. "
    "Position-space width sigma(t) (y-axis) vs time t (x-axis), no numerical labels. "
    "Single blue #0072B2 1pt curve starting at sigma_0 on the y-axis, initially flat (parabolic minimum "
    "at t=0), then transitioning smoothly to linear growth at late times. Vermillion #D55E00 1pt dashed "
    "asymptote tangent to the late-time linear regime and extrapolated back through the y-axis. Small "
    "orange #E69F00 filled circle marker at t=0 indicating the minimum-width point. Y-axis at zero. "
    "Black 1pt axes. No equations, no characteristic-time annotation, no particle labels.",

    # ---------- Chapter 4: One-Dimensional Problems ----------

    # Fig 4.1 — Infinite square well: first four eigenfunctions
    "Single-column scientific figure, flat vector, white background. Four equal-height panels stacked "
    "vertically, all sharing the x-axis range [0, L]. Each panel shows the interval bounded by short "
    "black 1pt vertical wall segments at x=0 and x=L. In each panel, a blue #0072B2 1pt curve representing "
    "psi_n(x): panel 1 (n=1) a single half-sine arch entirely above the baseline; panel 2 (n=2) one full "
    "sine cycle with one interior node; panel 3 (n=3) one-and-a-half sine periods with two interior nodes; "
    "panel 4 (n=4) two full sine periods with three interior nodes. Light gray dashed horizontal baseline "
    "in each panel. Black 0.5pt dashed vertical lines at each interior node. Symmetric y-axis range. "
    "No labels, no quantum-number annotations, no |psi|^2 overlay, no energy-level diagram.",

    # Fig 4.2 — Probability density and correspondence principle
    "Single-column scientific figure, flat vector, white background. Three equal-height panels stacked "
    "vertically, all sharing x-axis range [0, L] and bounded by vertical black 1pt wall segments. "
    "Each panel shows |psi_n|^2 vs x. Top panel (n=1): blue #0072B2 1pt single-peaked sine-squared curve. "
    "Middle panel (n=2): sky blue #56B4E9 1pt curve with two peaks separated by a zero at x=L/2. Bottom "
    "panel (n=10): orange #E69F00 1pt curve with ten rapidly oscillating peaks. In the bottom panel only, "
    "a horizontal black 0.5pt dashed reference line at the classical-uniform value 1/L spanning the panel. "
    "Y-axis at zero in all panels. No n-labels, no equations, no psi_n overlay.",

    # Fig 4.3 — Harmonic oscillator eigenfunctions
    "Single-column scientific figure, flat vector, white background. Cartesian axes with horizontal "
    "position x centered on origin and vertical axis showing energy/wave-function. Black 1pt parabolic "
    "potential curve V(x) = (1/2)m omega^2 x^2 centered at origin. Four horizontal black 0.5pt "
    "energy-level lines at heights E_n = hbar omega (n + 1/2) for n=0,1,2,3, each line truncated at the "
    "classical turning points where V(x) crosses E_n. Sitting on each energy-level line, a blue #0072B2 "
    "1pt curve representing psi_n(x), drawn with its baseline at E_n: n=0 a single Gaussian bump, n=1 "
    "antisymmetric with one node, n=2 symmetric with two nodes, n=3 antisymmetric with three nodes. "
    "No labels, no equations, no |psi|^2 overlay, no zero-point arrows, no turning-point markers.",

    # Fig 4.4 — Finite square well: tails into forbidden region
    "Single-column scientific figure, flat vector, white background. Cartesian axes. Black 1pt piecewise "
    "potential V(x): horizontal at V=0 for x < -a, dropping vertically at x=-a to V=-V_0, horizontal "
    "well-bottom from -a to +a at depth -V_0, rising vertically at x=+a back to V=0, horizontal at V=0 "
    "for x > +a. Horizontal black 0.5pt energy-level line at some E with -V_0 < E < 0 spanning the panel "
    "width. Single blue #0072B2 1pt wave function curve drawn with its baseline on the energy level: "
    "oscillating cosine-like inside the well [-a, +a], decaying exponentially outside both walls. The "
    "exterior tails clearly extend visible distances into the classically forbidden V=0 region before "
    "fading toward zero. No labels, no k or kappa annotations, no equations, no infinite-well comparison.",

    # Fig 4.5 — Nuclear potential well: alpha-decay geometry
    "Single-column scientific figure, flat vector, white background. Radial axis r horizontal from origin "
    "rightward; potential V(r) vertical. Black 1pt potential curve: deep attractive square well from r=0 "
    "to r=R at value -V_nuc, then jumping vertically up at r=R to the Coulomb-barrier peak, then decaying "
    "as 1/r to the right and approaching zero at large r. Horizontal black 0.5pt energy-level line at "
    "positive E below the Coulomb peak, spanning the panel width. The tunneling region (between r=R and "
    "the outer turning point r_2 where V(r_2)=E) filled with vermillion #D55E00 at 15% opacity. Blue "
    "#0072B2 1pt wave function drawn with baseline on the energy level: oscillating inside the well, "
    "decaying exponentially through the shaded barrier region, oscillating outward beyond r_2. "
    "No labels, no Z values, no helium-ball alpha-particle icons, no daughter nucleus.",

    # Fig 4.6 — Geiger-Nuttall plot
    "Single-column scientific figure, flat vector, white background. "
    "Log10(half-life in seconds) on y-axis spanning approximately -6 to +25; 1/sqrt(E) (with E in MeV) "
    "on x-axis. About ten blue #0072B2 filled small circle data points distributed along an approximately "
    "straight line across the 24-order range — representing alpha-emitting nuclei from short-half-life "
    "(e.g., Po-212) at the lower-left to long-half-life (e.g., U-238, Th-232) at the upper-right. Blue "
    "#0072B2 1pt straight fitted line through the points. Black 1pt axes, no numerical labels, no "
    "nuclide labels, no error bars, no fit equation, no historical photographs.",

    # ---------- Chapter 5: Quantum Formalism ----------

    # Fig 5.1 — Robertson proof structure flowchart
    "Single-column scientific figure, flat vector, white background. Vertical top-down process flowchart "
    "with five sequential nodes drawn as light-gray rounded rectangles, connected by black 1pt arrows. "
    "Node labels (short verbal phrases, no equations): (1) 'Define shifted operators (zero-mean)'; "
    "(2) 'Build two Hilbert-space vectors |f>, |g>'; (3) 'Cauchy-Schwarz inequality'; (4) 'Discard real "
    "part; keep imaginary part'; (5) 'Commutator appears' — this final node filled with accent orange "
    "#E69F00 since it is the punchline. To the right of node 4, a muted blue side-annotation reading "
    "'Keep real part: Schrodinger's 1930 strengthening'. No mathematical equations rendered inside "
    "boxes; the figure shows the logical chain, not the algebra.",

    # Fig 5.2 — Three uncertainties: Heisenberg vs Robertson vs Ozawa
    "Single-column scientific figure, flat vector, white background. Three equal-size panels side by "
    "side, each with a single inequality printed in matched typography below the panel. "
    "Panel A (blue #0072B2, Heisenberg 1927 measurement disturbance): schematic gamma-ray microscope — "
    "incoming photon arrow, electron at scattering point, scattered photon arrow with brackets labeling "
    "delta-x (resolution) and delta-p (transferred momentum); caption 'measurement disturbance'. "
    "Panel B (vermillion #D55E00, Robertson 1929 state preparation): a Hilbert-space-style icon showing "
    "a state vector |psi> with two perpendicular 'width' brackets sigma_A and sigma_B on two non-commuting "
    "axes, with no apparatus shown; caption 'state preparation'. "
    "Panel C (bluish green #009E73, Ozawa 2003): system state icon with intrinsic widths, separate "
    "apparatus icon labeled noise epsilon, and a disturbance arrow eta returning to the system; "
    "caption 'measurement-disturbance, corrected'. Consistent stroke weight across panels.",

    # Fig 5.3 — Schlosshauer-Kofler-Zeilinger 2013 survey
    "Single-column scientific figure, flat vector, white background. Horizontal bar chart with categorical "
    "y-axis (interpretation name) and quantitative x-axis (percentage of respondents, starting at zero). "
    "Five to six bars sorted in descending order: Copenhagen (~42%), Information-based / QBism-adjacent "
    "(~24%), Many-Worlds (~18%), Bohmian (~smaller), Objective collapse (~smaller), Other/Undecided "
    "(~smaller). All bars in single neutral Okabe-Ito sky blue #56B4E9 so no interpretation is visually "
    "privileged. Subtitle (typography to be applied after): 'n = 33, specialist foundations conference "
    "(Schlosshauer, Kofler, Zeilinger 2013)'. No 3D effects, no pie chart, no error bars, no commentary "
    "about which interpretation is correct.",

    # ---------- Chapter 6: The Hydrogen Atom ----------

    # Fig 6.1 — Hydrogen emission spectrum (visible)
    "Single-column scientific figure, flat vector, white background. Horizontal spectrum strip "
    "approximately 400-700 nm. Background showing a perceptually-accurate continuous visible-spectrum "
    "color gradient from violet at 400 to deep red at 700 nm. Superimposed: four sharp vertical bars "
    "in matched colors at 656 nm (H-alpha red), 486 nm (H-beta cyan), 434 nm (H-gamma violet), 410 nm "
    "(H-delta deep violet). Each line labeled with its Balmer-series identifier and transition "
    "(e.g., n=3 to 2). No Lyman or Paschen lines (visible range only). No transition diagram in this figure.",

    # Fig 6.2 — Effective potential for hydrogen radial problem
    "Single-column scientific figure, flat vector, white background. Line plot of effective potential "
    "V_eff (vertical, eV, range about -30 to +10) vs radial distance r (horizontal, in units of Bohr "
    "radius a_0, range 0 to 5). Two curves: l=0 in blue #0072B2 (pure Coulomb, attractive everywhere, "
    "diverging to negative infinity as r approaches 0); l=1 in vermillion #D55E00 (Coulomb plus "
    "centrifugal barrier, with a minimum at finite r, rising to positive infinity as r approaches 0). "
    "Horizontal dashed reference line at E_1 = -13.6 eV. Short annotation arrow pointing to the "
    "centrifugal-barrier rise of the l=1 curve. Legend in top-right. No l>=2 curves, no wavefunctions, "
    "no equations.",

    # Fig 6.3 — 2-panel: radial wavefunction R_10 + radial probability density P(r)
    "Single-column scientific figure, flat vector, white background. Two side-by-side panels with shared "
    "x-axis (r in units of Bohr radius a_0, range 0 to 5). "
    "Panel A: R_10(r) = (2/a_0^(3/2)) e^(-r/a_0) as a single sky blue #56B4E9 1pt monotonically decreasing "
    "curve. "
    "Panel B: P(r) = (4/a_0^3) r^2 e^(-2r/a_0) as a sky blue 1pt curve, peaked at r = a_0 and falling on "
    "both sides. Panel B annotations: vertical vermillion #D55E00 line at r = a_0 labeled 'most probable: "
    "a_0'; vertical vermillion line at r = 3a_0/2 labeled 'average: 3a_0/2'; a light gray shaded tail "
    "to the right of the peak showing the asymmetry that pulls the mean above the mode. "
    "No 2s or 3s curves, no probability cloud rendering.",

    # Fig 6.4 — Orbital isosurfaces 1s, 2s, 2p_z, 3d_{z^2}
    "Single-column scientific figure, flat vector, white background. 2-by-2 grid of 3D isosurface "
    "renderings of hydrogen orbitals at the 90%-probability surface, all drawn at a common scale within "
    "shared bounding boxes so size comparisons are meaningful. Top row: 1s (spherical), 2s (spherical "
    "with internal radial node visible). Bottom row: 2p_z (dumbbell along z-axis), 3d_{z^2} (dumbbell "
    "with equatorial torus). Each panel labeled with quantum numbers (n, l, m) and spectroscopic name. "
    "Positive-amplitude lobes rendered in light bluish-gray, negative-amplitude lobes in light orange "
    "(for orbitals with sign changes). Semi-transparent surfaces, soft lighting, no background gradient. "
    "No electron-dot spray, no 4f orbitals, no other 3d variants.",

    # Fig 6.5 — Stern-Gerlach apparatus (spin focus)
    "Single-column scientific figure, flat vector, white background. Schematic apparatus side-view with "
    "horizontal left-to-right flow: oven source emitting a beam of neutral silver atoms; collimating "
    "slit; inhomogeneous magnet drawn as two pole pieces labeled N and S with a wedge-shaped gap to "
    "indicate the field-gradient direction (gradient indicator in orange #E69F00); detector screen on "
    "right showing two discrete spots in vermillion #D55E00. Beam path traced through the apparatus. "
    "Apparatus geometry in neutral gray. Inset callout magnifying the two spots. "
    "No 'expected classical smear' overlay. No spin-up/spin-down vector arrows on individual atoms "
    "(the chapter argues against the spinning-ball picture). No orbital-angular-momentum framing.",

    # Fig 6.6 — Hydrogen energy levels with SO(4) degeneracy
    "Single-column scientific figure, flat vector, white background. Energy-level diagram with vertical "
    "energy axis in eV. Horizontal bars at E_n = -13.6/n^2 eV for n = 1, 2, 3, 4. Each level subdivided "
    "horizontally into l-sublevels drawn at exactly the same vertical height: n=1 (1s); n=2 (2s, 2p); "
    "n=3 (3s, 3p, 3d); n=4 (4s, 4p, 4d, 4f). Color-coded by n in Okabe-Ito (n=1 blue #0072B2, n=2 "
    "vermillion #D55E00, n=3 bluish green #009E73, n=4 orange #E69F00). Spectroscopic labels (s, p, d, f) "
    "below each bar. Degeneracy counts (1, 4, 9, 16) annotated. Dashed horizontal at E=0 marking "
    "ionization threshold. No Lamb shift, no fine structure, no spin splitting, no transition arrows.",

    # ---------- Chapter 7: Angular Momentum ----------

    # Fig 7.1 — Angular-momentum ladder diagram
    "Single-column scientific figure, flat vector, white background. Three vertically-arranged ladder "
    "columns side by side at common vertical scale: l=0 (single rung at m=0), l=1 (three rungs at "
    "m=-1, 0, +1), l=2 (five rungs at m=-2, -1, 0, +1, +2). Rungs as short horizontal blue #0072B2 bars. "
    "Curved arrows on the right side of each ladder: vermillion #D55E00 raising arrows (L+) connecting "
    "adjacent rungs upward; sky blue #56B4E9 lowering arrows (L-) connecting adjacent rungs downward. "
    "Top rung of each ladder annotated 'L+ |l, l> = 0'; bottom rung annotated 'L- |l, -l> = 0'. "
    "m-value labels on the right side. l labels at the top of each column. "
    "No spin ladders mixed in, no spherical harmonic plots, no half-integer ladders.",

    # Fig 7.2 — Angular shapes of |Y_lm|^2
    "Single-column scientific figure, flat vector, white background. 2-by-2 grid of polar/spherical "
    "renderings of |Y_lm(theta, phi)|^2 on the unit sphere. Panel A: Y_{0,0} (uniform sphere). "
    "Panel B: Y_{1,0} (dumbbell aligned along z-axis). Panel C: Y_{1,+1} (donut/torus shape around "
    "z-axis, going as sin^2 theta). Panel D: Y_{1,-1} (donut shape, visually indistinguishable from "
    "C in |Y|^2). Each panel renders a 3D surface with z-axis drawn explicitly. Magnitude encoded as "
    "a sequential sky blue #56B4E9 to dark blue #0072B2 gradient. Neutral background. Caption clarifies "
    "this is the angular part only (in contrast to the full radial-times-angular orbital isosurfaces). "
    "No Re(Y) or Im(Y) plots — probability density only.",

    # Fig 7.3 — Two-particle singlet measurement schematic
    "Single-column scientific figure, flat vector, white background. Left-right symmetric layout. "
    "Center: source labeled |0, 0> emitting an entangled pair, with the singlet ket "
    "(|up down> - |down up>)/sqrt(2) printed below. Two neutral-gray particle arrows depart from the "
    "source toward the left and right edges of the panel. At each end, a Stern-Gerlach-style detector "
    "drawn with an orientation arrow (vermillion #D55E00 on the left, bluish green #009E73 on the "
    "right). At each detector, two output spots labeled +hbar/2 and -hbar/2. Inset annotation: "
    "'aligned axes: always opposite; angle theta: cos^2(theta/2) opposite-outcome probability.' "
    "No hidden-variable trajectory depictions, no Bell-inequality plot, no spooky-action editorializing.",

    # Fig 7.4 — Spinor 720-degree rotation under SU(2)
    "Single-column scientific figure, flat vector, white background. Two side-by-side comparison panels "
    "of equal size, each laying out a circular rotation path with vector positions at 0, 90, 180, 270, "
    "and 360 degrees. "
    "Panel A (classical vector under SO(3)): vector drawn as a blue #0072B2 arrow at each of the four "
    "positions, with the arrow at 360 degrees identical to the starting arrow. Caption: 'SO(3): "
    "360 degrees returns to identity'. "
    "Panel B (spin-1/2 spinor under SU(2)): same circular path layout, but the spinor arrow's color "
    "shifts cyclically across a perceptually sequential Okabe-Ito gradient (blue at 0 degrees, through "
    "bluish-green and orange to vermillion at 360 degrees, then back through orange and bluish-green "
    "to blue at 720 degrees), with phase encoded as color. Caption: 'SU(2): 360 deg gives -|psi>; "
    "720 deg returns to identity'. No Mobius-strip imagery, no SU(2) matrix algebra in the figure.",

    # Fig 7.5 — WCOE 1975 neutron interferometer
    "Single-column scientific figure, flat vector, white background. Apparatus schematic with "
    "left-to-right flow: neutron source on left; crystal beam splitter creating two paths (upper and "
    "lower) drawn as neutral gray lines; magnetic-field coil on one path (rendered in orange #E69F00) "
    "labeled 'B-field: rotates neutron spin by 2 pi'; recombination at a second crystal; detector on "
    "right. Inset graph: two superposed sinusoidal interference patterns on shared axes — solid blue "
    "#0072B2 curve (no rotation) and dashed vermillion #D55E00 curve (with 2 pi rotation, displaced "
    "by pi from the solid curve). Inset annotation: 'fringes shift by pi when one beam is rotated by "
    "2 pi'. Apparatus in neutral gray, magnetic-field component highlighted in orange. "
    "No QM formula derivation in the figure, no follow-up experiments.",

    # ---------- Chapter 8: Identical Particles ----------

    # Fig 8.1 — Exchange correlation: distinguishable vs fermion vs boson joint density
    "Single-column scientific figure, flat vector, white background. Three side-by-side 2D heatmap "
    "panels with identical axes (x_1 horizontal, x_2 vertical, both in units of well length L) and a "
    "single shared sequential colormap (sky blue #56B4E9 to dark blue #0072B2) so densities are "
    "quantitatively comparable. Dashed diagonal line x_1 = x_2 drawn across each panel. "
    "Panel A: distinguishable particles, |psi_1(x_1) psi_2(x_2)|^2, a relatively uniform product-density "
    "distribution. "
    "Panel B: fermions (antisymmetric spatial), with a clear 'exchange hole' — vanishing density along "
    "the x_1 = x_2 diagonal. "
    "Panel C: bosons (symmetric spatial), with enhanced density along the diagonal. "
    "Single shared colorbar. No diverging colormaps (density is non-negative). No 'exchange force' "
    "annotations.",

    # Fig 8.2 — Helium parahelium vs orthohelium energy levels
    "Single-column scientific figure, flat vector, white background. Energy-level diagram with vertical "
    "energy axis in eV. Three columns showing the perturbation cascade: column 1, single neutral-gray "
    "level at unperturbed E_0 (the 1s 2s configuration); column 2, single level displaced up by the "
    "direct Coulomb integral J; column 3, splitting into two levels — parahelium at E_0 + J + K labeled "
    "S=0 (singlet) in bluish green #009E73, orthohelium at E_0 + J - K labeled S=1 (triplet) in "
    "vermillion #D55E00. Right side of the figure shows experimental values from NIST: orthohelium at "
    "-59.2 eV, parahelium at -58.4 eV, splitting 0.8 eV annotated as '2K'. Energy gap annotations "
    "between levels. No other helium configurations, no transition arrows, no spin arrows on levels.",

    # Fig 8.3 — Madelung diagonal-filling diagram
    "Single-column scientific figure, flat vector, white background. 2D grid layout with rows indexed "
    "by principal quantum number n (1 through 6 or 7) and columns indexed by orbital angular momentum "
    "l (s, p, d, f). Each cell labeled with the orbital name (e.g., '1s', '2p', '3d'). Diagonal arrows "
    "in orange #E69F00 overlaid on the grid, tracing the Madelung filling order from top-right to "
    "bottom-left in successive diagonal sweeps: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, "
    "5d, 6p, 7s. Cell labels in black on white. Cells beyond practical filling faded or omitted. "
    "No exception labels (Cr, Cu) in the figure itself — those go in the caption. No electrons-as-dots.",

    # Fig 8.4 — Fermi-Dirac vs Bose-Einstein vs Maxwell-Boltzmann
    "Single-column scientific figure, flat vector, white background. Line plot with three curves on "
    "shared axes: x-axis = (E - mu)/k_B T, range about -4 to +4; y-axis = mean occupation <n>, range "
    "0 to about 3. Vertical reference line at x = 0 (E = mu). Three curves: Fermi-Dirac 1/(exp(x)+1) "
    "in vermillion #D55E00, asymptoting to max occupation 1 at low energies; Bose-Einstein 1/(exp(x)-1) "
    "in bluish green #009E73, diverging as x approaches 0 from the positive side; Maxwell-Boltzmann "
    "exp(-x) in neutral gray, the classical asymptote that both quantum cases approach at high "
    "(E - mu)/k_B T. Annotations: 'FD: max occupation 1 (Pauli)'; 'BE: diverges as E approaches mu "
    "(condensation)'; 'MB: classical high-T limit'. No specific temperatures, no Fermi energy or BEC "
    "critical temperature labels.",

    # ---------- Chapter 9: Approximation Methods ----------

    # Fig 9.1 — Level repulsion / avoided crossing under perturbation
    "Single-column scientific figure, flat vector, white background. Line plot of energy E (vertical) "
    "vs perturbation strength lambda (horizontal). Two dashed gray reference lines depicting unperturbed "
    "levels that would cross at some lambda_c. Two solid curves depicting actual eigenvalues that bend "
    "away from each other near lambda_c, never crossing: upper curve in vermillion #D55E00, lower curve "
    "in blue #0072B2. Vertical line at lambda_c with annotation showing the gap labeled '2 |<a|H'|b>|'. "
    "Two orange #E69F00 arrows annotating 'level repulsion' — upper arrow pointing up at the upper "
    "level, lower arrow pointing down at the lower level. "
    "No more than 2 levels. No physical-system labels. No eigenstate-composition arrows.",

    # Fig 9.2 — Hydrogen n=2 linear Stark splitting
    "Single-column scientific figure, flat vector, white background. Energy-level diagram with two "
    "labeled columns: 'electric field E = 0' on left and 'E not equal to 0' on right. Left column: "
    "single horizontal level labeled 'n=2 (4-fold degenerate)' in neutral gray. Right column: three "
    "levels — top at +3 e E a_0 in vermillion #D55E00 labeled (|2s> - |2p_z>)/sqrt(2); middle at 0 with "
    "degeneracy 2 in blue #0072B2 labeled '|2p_x>, |2p_y>'; bottom at -3 e E a_0 in bluish green #009E73 "
    "labeled (|2s> + |2p_z>)/sqrt(2). Diagonal connecting lines in matched colors from the single "
    "left-column level to the three right-column levels showing which states evolved into which. "
    "No second-order corrections (this is the linear Stark effect). No n=1 or n=3 levels.",

    # Fig 9.3 — Variational helium <H>(Z*) vs Z*
    "Single-column scientific figure, flat vector, white background. Line plot of expectation value "
    "<H>(Z*) (vertical, in eV, range about -80 to -60) vs trial parameter Z* (horizontal, range 1.0 "
    "to 2.5). Single blue #0072B2 1pt parabolic-shaped curve for <H>(Z*) = (Z*)^2 - 4 Z* + (5/8) Z*. "
    "Vermillion #D55E00 filled circle marker at the minimum at Z* = 27/16 (approximately 1.69) with "
    "horizontal and vertical reference lines down to the axes. Annotation: 'E_var = -2.848 Hartree, "
    "approximately -77.5 eV'. Dashed bluish green #009E73 horizontal reference line at the experimental "
    "value -79.0 eV showing the 1.5 eV variational gap. Optional annotation at Z* = 2 (bare nuclear "
    "charge) showing where the naive unscreened calculation would lie above the minimum. "
    "No kinetic-only or Coulomb-only component curves.",

    # Fig 9.4 — Sinc-squared convergence to delta function
    "Single-column scientific figure, flat vector, white background. Line plot of sin^2(Omega t / 2) "
    "divided by Omega^2 (vertical) vs Omega (horizontal, centered on Omega = 0, range about -5/t_1 to "
    "+5/t_1). Three overlaid curves at three increasing values of t (small t_1, medium t_2 = 2 t_1, "
    "large t_3 = 4 t_1): sky blue #56B4E9 for small t (broad and short); bluish green #009E73 for "
    "medium t (narrower and taller); vermillion #D55E00 for large t (narrowest and tallest). Each peak "
    "centered at Omega = 0 with peak height proportional to t^2 and width proportional to 1/t. Area "
    "under each curve approximately constant. Annotations: 'peak height proportional to t^2'; 'peak "
    "width proportional to 1/t'; 'area proportional to t, approaches delta function'. Legend "
    "distinguishing the three t-values.",

    # Fig 9.5 — WKB wave function across a turning point
    "Single-column scientific figure, flat vector, white background. Two stacked panels with shared "
    "x-axis. "
    "Top panel: potential V(x) drawn in dark gray as a smooth bound-state well (parabolic or asymmetric "
    "shape). Horizontal dashed orange #E69F00 line at the bound-state energy E. Classical turning "
    "points x_a and x_b marked where V(x_a) = V(x_b) = E. "
    "Bottom panel: WKB wave function psi(x). For x < x_a (classically forbidden), exponential decay in "
    "light blue #56B4E9. For x_a < x < x_b (classically allowed), oscillation in blue #0072B2 with local "
    "wavelength lambda(x) = h / sqrt(2 m (E - V(x))) — wavelength visibly compresses where V is low and "
    "stretches where V approaches E. For x > x_b (classically forbidden), exponential decay again. "
    "Vermillion #D55E00 brackets at x_a and x_b annotated 'Airy function matching'. "
    "No explicit Airy function shape rendered; no separate amplitude curve overlay.",

    # ---------- Chapter 10: Quantum Mechanics in the Modern World ----------

    # Fig 10.1 — CHSH / Tsirelson / Popescu-Rohrlich bounds
    "Single-column scientific figure, flat vector, white background. Horizontal number line / bar "
    "diagram with |S| value on the x-axis, range 0 to 4. Three colored bands across the axis: 0 to 2 "
    "in sky blue #56B4E9 labeled 'local hidden variables (LHV)'; 2 to 2 sqrt(2) (approximately 2.828) "
    "in vermillion #D55E00 labeled 'quantum mechanics (singlet, optimal axes)'; 2 sqrt(2) to 4 in "
    "light gray labeled 'no-signaling but non-quantum (Popescu-Rohrlich)'. Vertical marker lines with "
    "labels above the axis: '2 (CHSH bound)', '2 sqrt(2) approximately 2.828 (Tsirelson bound)', "
    "'4 (algebraic max)'. Single experimental marker at |S| = 2.697 with annotation 'Aspect 1982'. "
    "No multiple-experiment markers, no editorializing about interpretations.",

    # Fig 10.2 — Three-level laser energy diagram
    "Single-column scientific figure, flat vector, white background. Energy-level diagram with vertical "
    "energy axis and three horizontal levels: ground state (level 1, drawn as a thick bar to indicate "
    "heavy population), broadband pump level (level 3, drawn as a wider band), metastable upper laser "
    "level (level 2, narrow). Three arrow types between levels: orange #E69F00 broadband upward "
    "absorption arrow from 1 to 3 (pump); gray arrow from 3 to 2 labeled 'fast non-radiative decay' "
    "(heat); vermillion #D55E00 downward arrow from 2 to 1 (stimulated emission, coherent). Population "
    "labels N_1, N_2, N_3 on the right side. Inversion annotation 'N_2 > N_1' near the upper laser "
    "level. Optional inset showing the four-level scheme as the modern variant. "
    "No Einstein A and B coefficients as labels. No cavity mirrors. No ruby-specific transitions.",

    # Fig 10.3 — Three-panel band diagrams: conductor / insulator / semiconductor
    "Single-column scientific figure, flat vector, white background. Three side-by-side panels with "
    "shared energy axis ranges so band gaps are quantitatively comparable. "
    "Panel A (metal/conductor): valence and conduction bands overlap, or valence band partially filled. "
    "Filled band in dark blue #0072B2, empty band in sky blue #56B4E9. Fermi level (dashed vermillion "
    "#D55E00) inside a band. "
    "Panel B (insulator): wide gap (about 5 eV) between filled valence band (dark blue) and empty "
    "conduction band (sky blue). Fermi level in middle of gap. "
    "Panel C (semiconductor): narrow gap (about 1 eV) with annotations 'Si: 1.12 eV, GaAs: 1.43 eV'. "
    "Same structure as insulator. "
    "Small reference bracket showing k_B T at 300 K (about 0.025 eV) for scale. "
    "No E vs k dispersion. No doping figures.",

    # Fig 10.4 — Bell state generation quantum circuit
    "Single-column scientific figure, flat vector, white background. Standard quantum-circuit diagram. "
    "Two horizontal wires (top wire = qubit 1, bottom wire = qubit 2), both starting in |0> annotated "
    "on the left edge. Hadamard gate as a sky blue #56B4E9 boxed 'H' on the top wire. CNOT gate "
    "immediately after the Hadamard: filled black dot on the top wire (control), open circle with "
    "plus inside on the bottom wire (target), connected by a vertical line. Annotations: intermediate "
    "state '(|00> + |10>) / sqrt(2)' between gates; final state '(|00> + |11>) / sqrt(2)' highlighted "
    "in vermillion #D55E00 on the right of the circuit. Standard left-to-right time flow. "
    "No measurement gates. No Bloch sphere overlays. No other Bell states.",

    # Fig 10.5 — Algorithm runtime scaling: Shor vs Grover vs classical
    "Single-column scientific figure, flat vector, white background. Two log-log subplots side by side. "
    "Factoring subplot: classical GNFS runtime as a vermillion #D55E00 curve rising sub-exponentially "
    "(exp of n^(1/3) (log n)^(2/3)); Shor's algorithm O(n^3) as a much shallower bluish green #009E73 "
    "curve. Annotation arrow showing the gap widens dramatically with input size n. "
    "Search subplot: classical brute-force O(N) as a vermillion straight line on log-log; Grover O(sqrt(N)) "
    "as a bluish green line with half the slope. Annotation arrow showing the parallel constant-factor "
    "gap on log scale. "
    "Legend distinguishes classical vs quantum curves. Labels 'exponential speedup' for Shor and "
    "'quadratic speedup' for Grover. "
    "No specific hardware estimates. No other algorithms (HHL, simulation).",

    # Fig 10.6 — Superconductor T_c records 1911-present
    "Single-column scientific figure, flat vector, white background. Scatter plot with year on the "
    "x-axis (1911 to present) and T_c in Kelvin on the y-axis (log scale spanning about 1 K to 300 K). "
    "Plotted points for major records: Hg 1911 (4.2 K), Nb 1930 (~9 K), Nb_3 Ge 1973 (~23 K) — all "
    "blue circles (conventional superconductors); LBCO 1986 (~35 K), YBCO 1987 (~93 K), HgBaCaCuO 1993 "
    "(~133 K) — vermillion #D55E00 squares (cuprates); H_3 S under pressure 2015 (~203 K), LaH_10 "
    "under pressure 2019 (~250 K) — orange #E69F00 triangles (pressure-stabilized hydrides). Horizontal "
    "dashed reference line at 77 K labeled 'liquid nitrogen boiling point'. Legend distinguishes the "
    "three superconductor categories. "
    "No unconfirmed claims (LK-99 etc.). No extrapolation to future records.",

    # Fig 10.7 — STM cross-section with exponential current
    "Single-column scientific figure, flat vector, white background. Two-region layout. "
    "Main schematic (left, atomic-scale cross-section): STM tip drawn at apex narrowing to one or a few "
    "neutral-gray atoms; vacuum gap labeled 'd ~ a few Angstroms'; conducting surface below with "
    "several atoms visible. Vermillion #D55E00 vertical tunneling-current arrow between the closest "
    "tip atom and the closest surface atom. "
    "Inset graph (right): I vs d showing the exponential dependence I proportional to exp(-2 kappa d) "
    "with kappa about 1 inverse Angstrom in bluish green #009E73; axes labeled. "
    "Annotation: 'd changes by 1 Angstrom, I changes by factor of 7'. "
    "No full STM apparatus (piezo scanners, vibration isolation, electronics). No actual surface "
    "topographic image. No human figures.",
]


if __name__ == "__main__":
    print(f"Collected {len(image_prompts)} image prompts from the QM book CAJAL pantry.")
    for i, p in enumerate(image_prompts, 1):
        print(f"\n--- Prompt {i} ---\n{p}")
