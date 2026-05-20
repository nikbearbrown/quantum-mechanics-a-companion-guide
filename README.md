# Quantum Mechanics — A Companion Guide

**Nik Bear Brown** · Bear Brown, LLC · 2026

*The bridge between a rigorous undergraduate quantum-mechanics text (Griffiths) and the popular-science books most students read first. Names the misconceptions the genre installs. Supplies the math the genre omits. Points to where Griffiths gets it right.*

---

## What this book is

Two kinds of book about quantum mechanics sit on shelves: the rigorous undergraduate text (Griffiths, Shankar, Liboff) and the popular-science treatment (*Quantum Physics for Beginners* and its dozens of variants). The first is mathematically solid but builds no intuition. The second builds vivid intuition for objects that don't behave that way. The student who reads only one of these struggles in different specific directions. The student who reads both, without a guide, often spends a semester unlearning the popular-science framings before they can read Griffiths.

This book is the guide. It is a **diagnostic companion**: ten units mapped to the standard semester quantum-mechanics curriculum, each unit doing four jobs — point to where Griffiths derives the topic, audit how popular-science books treat it (✅ adequate, ⚠️ underdeveloped, ❌ omitted, 🚫 actively misleading), supply the math popular-science omits, and correct the misconceptions popular-science installs.

The book's signature pedagogical move is the **balloon-analogy correction** in Unit 5. The popular-science framing of the Heisenberg uncertainty principle as a measurement-disturbance problem (the balloon in a dark room) is Heisenberg's own 1927 microscope argument, which Robertson corrected in 1929. Uncertainty is intrinsic to the state, derivable from operator non-commutativity, before any measurement occurs. The book traces the misconception backward to its source and forward through every place it recurs (Stern-Gerlach in Unit 6, Pauli exclusion in Unit 8, entanglement in Unit 10).

The central concept the book teaches is **diagnostic reading**: before accepting any claim, ask what equation it corresponds to, where the rigorous text derives that equation, and what the equation actually says in plain language. By Unit 10, you should be reading every popular-science quantum book this way. You should be reading Griffiths this way too.

## Who this book is for

An undergraduate physics, chemistry, or engineering student in a first rigorous quantum-mechanics course, who is also reading (or has read, or will read) a popular-science quantum-mechanics book alongside it. Calculus through partial derivatives required. Basic linear algebra helpful — Unit 2 fills the linear-algebra gap most popular-science books leave open.

Not for: a first exposure to QM with no other text in hand; a graduate-level course; readers looking for a book that advances a specific interpretation of QM.

## How to read it

Cover to cover, in order, the first time through. Each unit invokes machinery built in earlier units. Don't skip Unit 2 (Mathematical Foundations) — it is the unit popular-science books skip, and the unit that determines whether the rest makes sense.

For each unit: read the Reading Map first (which Griffiths sections to read in parallel; which popular-science chapters to read for motivation only; which equations the companion adds). Then read the companion unit. Then read the cited Griffiths sections. Then run the exercises. Close with "What would change my mind" and "Still puzzling."

## Table of Contents

**Front matter** — Title · Copyright · Dedication · ~1,300-word Preface

**Introduction** (Chapter 0) — Cold open at the balloon-analogy bridge · central argument · audience · scope in/out · "diagnostic reading" central concept · the balloon analogy as recurring case study · 10-unit map in three groups · how to read · ~800-word AI essai · closing return

### Foundations (Units 1–3)

| # | Title | Companion's job |
|---|-------|-----------------|
| 1 | Why Quantum Mechanics? | Add the math to the five experiments popular-science books narrate well |
| 2 | Mathematical Foundations | Build the linear algebra / Dirac notation popular-science books omit entirely |
| 3 | The Schrödinger Equation | Make the "postulated, not derived" point explicit; supply the Born rule and probability current |

### Workhorse Solvable Systems (Units 4–7)

| # | Title | Companion's signature move |
|---|-------|-----------------|
| 4 | One-Dimensional Problems | Two solution methods for the harmonic oscillator; WKB tunneling with the Gamow factor |
| 5 | Quantum Formalism | **The balloon-analogy correction** (Heisenberg 1927 epistemic → Robertson 1929 intrinsic); the five postulates; honest about contested interpretations |
| 6 | The Hydrogen Atom | The $r_{mp}$ vs. $\langle r \rangle$ contrast as the antidote to the orbit-as-path misconception; classical-spin-disproof calculation |
| 7 | Angular Momentum | Ladder-operator derivation of the eigenvalue spectrum; explicit construction of the singlet state as the bridge forward to Bell's theorem |

### Beyond the Solvable (Units 8–10)

| # | Title | Companion's signature move |
|---|-------|-----------------|
| 8 | Identical Particles | Pauli exclusion as a *consequence* of antisymmetry, not a separate postulate; the helium singlet-triplet splitting derived |
| 9 | Approximation Methods | The Dirac 1927 / Fermi 1950 historical correction on the "golden rule"; the variational helium calculation; the WKB Gamow factor |
| 10 | Quantum Mechanics in the Modern World | CHSH inequality derivation (both LHV bound and QM violation at optimal angles); Bell tests, Nobel 2022; aging-risk flag on hardware specifics |

**Back matter** — Acknowledgments · About the Author · per-unit Notes · References (~50 entries) · On the Absence of an Index · Glossary (~20 terms) · Errata

## About the Author

**Nik Bear Brown** is an Associate Teaching Professor at Northeastern University's College of Engineering, where he teaches data science, AI, computational physics, visualization, and graduate courses on AI-augmented learning. PhD in computer science from UCLA with major field in computational and systems biology. He has been teaching variants of computational physics, AI-for-engineering, and cross-domain quantum mechanics at Northeastern for over a decade, and watched dozens of undergraduates try to read the rigorous text and the popular-science book in parallel and bounce off the gap between them. The companion is the document that gap demanded. He writes at [nikbearbrown.com](https://www.nikbearbrown.com) and [skepticism.ai](https://www.skepticism.ai). Reach him at [bear@bearbrown.co](mailto:bear@bearbrown.co).

## Companions

**Pair this book with a rigorous primary text.** Griffiths *Introduction to Quantum Mechanics* (3rd ed., Cambridge, 2018) is the canonical pairing; every unit's Reading Map cites specific Griffiths sections. Shankar *Principles of Quantum Mechanics* (2nd ed.) and Liboff *Introductory Quantum Mechanics* (4th ed.) also work.

**Pair this book with a popular-science quantum book.** The companion is built around an audit of one anonymous *Quantum Physics for Beginners* (2021), but the audit framework generalizes — any popular-science quantum book will install the same set of recycled misconceptions at the same places, and the companion's diagnostic tags (✅ ⚠️ ❌ 🚫) apply across the genre.

**Medhavy integration:** [medhavy.com](https://www.medhavy.com/) — मेधावी, from the Sanskrit for *intelligent*. An AI-powered intelligent textbook platform that indexes this book semantically. Search a misconception and Medhavy surfaces the unit that corrects it.

## A note about AI

The book contains an explicit AI essai in the Introduction. The short version: use Claude (or ChatGPT, or Gemini) to verify derivations step by step, to generate counter-examples for your own intuitions, and to audit popular-science passages against the rigorous formulation. Do not use AI to "explain quantum mechanics simply" — the training data contains so many balloon analogies that the model will reach for one, installing the same misconceptions the popular-science books install. The AI is the assistant, not the teacher. Griffiths is the teacher.

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law. See [LICENSE.md](./LICENSE.md) for full terms.

ISBN: [INSERT ISBN]
First edition: 2026.

## Contact

Permissions · Errata · Adoption · Course integration: [bear@bearbrown.co](mailto:bear@bearbrown.co)

---

## Signature Simulations

<!-- TODO: populate from chapter content -->

---

*Read both books. Trust neither. Diagnose every claim. This is the companion that makes that possible.*
