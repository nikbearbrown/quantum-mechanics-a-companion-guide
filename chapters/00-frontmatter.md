# Quantum Mechanics — A Companion Guide

**Nik Bear Brown**

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in
any form or by any means without the prior written permission of the publisher,
except in the case of brief quotations in critical reviews and certain other
noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

First edition: 2026

For permissions inquiries: bear@bearbrown.co

---

## Dedication

*For the student who finished a pop-science book on quantum mechanics, picked up Griffiths the next semester, and discovered that the two books were apparently describing different universes. They are not. This is the bridge.*

---

## Preface

Two kinds of book about quantum mechanics sit on bookstore shelves, and they do not speak to each other.

The first is the rigorous undergraduate text — Griffiths, Liboff, Shankar, Cohen-Tannoudji. Equations on the page. Worked examples. Problem sets. A student who works through Griffiths cover to cover can solve the hydrogen atom by hand, derive the Robertson uncertainty relation from Cauchy-Schwarz, and explain why $L_x$ and $L_y$ cannot be measured simultaneously to arbitrary precision. The mathematics is solid. The physics is precise. The book is exactly what a working physicist needs and exactly what a curious general reader cannot read.

The second is the popular-science book on quantum mechanics. The shelves are full of them. Some are good. Many are not. The ones that aren't share a specific failure mode: they teach the student a beautiful, vivid, and *wrong* mental picture. The most common is the balloon analogy for the uncertainty principle — "to find a balloon in the dark, you must bump into it, changing its position." This image is exactly the kind of thing a popular-science writer reaches for. It is also exactly the misconception Heisenberg himself proposed in 1927 and that Robertson corrected in 1929. The balloon analogy teaches the wrong physics: uncertainty as measurement disturbance, when uncertainty is in fact a property of the quantum state, derivable from operator non-commutativity, *before any measurement occurs*.

A student who reads only Griffiths struggles to develop intuition for objects that have no classical analogue. A student who reads only a pop-science book develops vivid intuition for objects that don't behave the way they imagine. The two failure modes are different. The bridge between them is what this book is.

I wrote this book because I have been teaching computational physics and AI-for-engineering at Northeastern for over a decade, and over that time I have watched undergraduates fail in both directions. The ones who read pop-sci first arrived in my course confident that they understood quantum mechanics; when I asked them why uncertainty was intrinsic to the state rather than caused by measurement, they could not answer, because their book had taught them the wrong story. The ones who read Griffiths first arrived in my course able to grind through the math but unable to tell me what an orbital actually is — they had been told to compute $\langle r\rangle$ and the most probable $r$ but had never confronted the fact that these are *different numbers about the same distribution*. The first group needed corrections. The second group needed intuition. Both groups needed the same thing: a careful reading guide that points to the right primary text for each question, names the misconceptions that the standard pop-science treatments install, and provides the math the pop-science treatments omit.

This book is that reading guide.

Why now: because the pop-science quantum mechanics market is larger than it has ever been and shows no signs of stopping. Every six months, another book appears with a title like *Quantum Physics for Beginners* or *The Strange World of Quantum Reality* or *Quantum Mechanics in Five Easy Steps*. Some are clear. Most are not. The genre's standard moves — the balloon analogy, the "observer creates reality" framing, the conflation of entanglement with faster-than-light signaling — are recycled from book to book, each iteration drifting slightly farther from what the equations actually say. The student walking into their first university quantum-mechanics course has often already read three of these books and has installed a mental model that the professor must spend half the semester carefully dismantling. A diagnostic companion that names the recycled misconceptions explicitly and points to where Griffiths corrects them is not a luxury anymore. It is what the situation requires.

Why me: because I have run the diagnostic for over a decade across courses in computational physics, computational biology, and AI-for-engineering, and watched the same misconceptions recur in the same places. I am not the working theoretical physicist who will write the next generation of QM textbooks. I am the cross-domain instructor who has watched many quantum-mechanics-curious students try to read the standard pop-science books, then try to read Griffiths, and bounce off the gap between the two. This book is the document I wished existed when I was teaching them.

This book does **not** teach you quantum mechanics from zero. It is a companion. Use it with Griffiths (or Shankar, or Liboff). It does not replace the primary text. It does not solve all the problems in Griffiths for you. It does not derive every result; it points to where the result is derived properly and adds the explanation the pop-science treatment skipped.

This book does **not** review every pop-science quantum book on the market. It is built around an audit of one specific exemplar — an anonymously authored *Quantum Physics for Beginners* (2021) that is widely sold and that represents the genre faithfully. The audit table in the TIKTOC.md document (which precedes this book) rates that exemplar topic by topic and identifies what to use and what to avoid. The conclusions generalize: every pop-science quantum book makes essentially the same set of moves at the same places, with the same set of accompanying errors.

This book does **not** advance an interpretation of quantum mechanics. The interpretation question (Copenhagen / Many-Worlds / Bohmian / QBism / spontaneous collapse) is genuinely contested. The formalism is not. This book teaches the formalism honestly and names the interpretive question as open. Unit 5 contains the most careful treatment of where the contested ground actually is and is honest about not picking sides.

— Nik Bear Brown
Boston, 2026
