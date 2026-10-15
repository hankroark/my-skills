---
name: "slide-craft"
description: "Plan or audit the content and structure of a presentation (storyboards, action titles, SCQA, BLUF, ORDER, SBAR, decision memo, status, change announcement); not for rendering .pptx."
---

# Slide-craft

Slide-craft is the **thinking layer** for presentations. It decides *what each
slide says and proves* and *what order the argument runs in* — before anyone
opens PowerPoint. It is deliberately separate from the **visual layer** (a
PPTX-creation skill), which decides *how slides look*.

It has two modes:

- **PLAN** — turn a topic, document, or notes into a reviewable **storyboard**
  (a Markdown deck plan the user edits and iterates), then hand that storyboard
  to a PPTX skill to build the deck.
- **AUDIT** — review an existing deck (a `.pptx`, exported text, or a described
  deck) against slide-craft principles and return prioritized, specific findings
  (and, optionally, a corrected storyboard).

Reference sections at the end of this file (consult as needed):
- **Reference A — Methodology**: the principles, with examples and the
  decision rules the skill applies in both modes.
- **Reference B — Executive Frameworks**: situation-specific executive spines
  (BLUF, ORDER, SBAR, decision memo, What / So What / Now What, change
  announcement), with a selector, slide maps, and failure modes.
- **Reference C — Storyboard Schema & Handoff Contract**: the exact Markdown
  format of the storyboard, and the **handoff contract** a PPTX skill consumes.
- **Reference D — Audit Rubric & Report Format**: the scoring rubric and report
  format for AUDIT mode.

---

## Core principles (applied in BOTH modes)

These come from Minto/McKinsey, Duarte, and Reynolds. Full detail + examples in
Reference A. The five the skill enforces:

1. **Audience-first.** Start from who is in the room, the decision they must
   make, and the one question they need answered. Everything serves that.
2. **Lead with the answer (BLUF; Minto Pyramid + SCQA by default).** The
   bottom line goes on the first slide. For a recommendation, open with
   Situation → Complication → Question → Answer, then the grouped supporting
   arguments. For bad news, escalation, decisions, status, or change
   announcements, use the matching spine in Reference B instead of SCQA.
3. **Action titles as a storyline.** Every slide title is a full-sentence
   *takeaway*, not a topic label. Reading the titles top-to-bottom must convey
   the whole argument. Write the titles FIRST.
4. **One idea per slide.** If a slide needs an "and," it is probably two slides.
5. **Signal over noise.** Every element on a slide proves the title; visuals
   amplify the point rather than repeat it. Cut the rest.

A sixth, cross-cutting test: the **"so what?"** — every slide must answer why the
audience should care, and the answer must be specific, not a restatement of data.

---

## Mode 1 — PLAN

Goal: produce a storyboard the user can review and edit, then feed to a PPTX skill.

### Step 1 — Gather inputs (ask if missing)

Before storyboarding, you need the following. **If the user has not provided
them, ask** (use a single grouped set of questions, don't interrogate):

- **Audience** — who, and their seniority / familiarity with the topic.
- **Situation** -- what job is this deck doing? A recommendation, bad news,
  an escalation, a decision request, a status update, or a change
  announcement? This picks the framework (see the selector in Reference B).
  Infer it from the request when it's obvious, and say which framework you
  picked.
- **Decision or action** — what should the audience do, decide, or believe after?
- **The one core message** — if they remember one sentence, what is it?
- **Source material** — a document, data, notes, or just the topic.
- **Constraints** — rough length (slide count), time limit, leave-behind vs.
  presented live, any required sections.

If the user gave a document or notes, read them first and propose answers to the
above, then confirm — don't ask what you can infer.

### Step 2 — Build the argument (don't write slides yet)

1. **Pick the spine.** Recommendation → SCQA (below). Any other situation in
   the Reference B selector → that framework's steps.
   Either way, apply BLUF: decide what the first slide's title says before
   anything else.
2. Write the spine in prose. For SCQA: Situation, Complication, Question,
   Answer, where the Answer is your core message / recommendation. For a
   framework: one or two sentences per step (e.g. ORDER's Objective, Result,
   Diagnosis, Explain, Resolution).
3. Under the Answer (or under each framework step), list the **supporting
   arguments**: 3–5 for SCQA, whatever each step needs for a framework. Each
   will become a section or a slide.
4. Under each argument, note the **evidence** that proves it (data, example,
   comparison). Evidence that proves nothing in the pyramid gets cut.
5. Check the spine against the framework's failure modes in Reference B (e.g.
   ORDER's Result buried after context, a decision memo without "do nothing").

Keep this argument sketch — it becomes the storyboard's header block.

### Step 3 — Write action titles first

Draft the **full-sentence takeaway title** for every slide, in order, and read
them top-to-bottom as a standalone narrative. Fix any title that is a topic
label or that breaks the logical flow. Only proceed when the titles alone tell
the story. See Reference A for the title patterns and a
topic-label → action-title rewrite table.

### Step 4 — Flesh out each slide in the storyboard

For each slide, fill the storyboard row (see Reference C): action title, the
single idea, the **suggested visual component** (stat callout, comparison, step
flow, timeline, chart, quote, etc.), the **evidence/content** that proves the
title, and an optional **speaker note / so-what**. Enforce one idea per slide
here — split any slide carrying two.

### Step 5 — Write the storyboard file and offer review

Write the storyboard to a Markdown file (e.g.
`<deck-name>-storyboard.md`) in the user's folder and present it for review.
Invite edits and iterate. The storyboard — not a finished deck — is the review
gate (the "ghost deck"): fixing the story here is cheap; fixing it after
production is not.

### Step 6 — Hand off to a PPTX skill

When the user approves the storyboard, hand it to a PPTX-creation skill
as the deck plan. The storyboard schema is designed to
map directly onto that skill's slide-by-slide plan — one storyboard row per
slide, with the suggested visual component naming the layout/component to use.
See the **handoff contract** in Reference C.

---

## Mode 2 — AUDIT

Goal: review an existing deck and return prioritized, specific, actionable findings.

### Step 1 — Get the deck's content

- **`.pptx` file:** extract the text/structure. If a PPTX skill or `markitdown`
  is available, use it: `python -m markitdown deck.pptx`. Capture per-slide
  titles, body text **and speaker notes** in order. The notes often hold the
  strongest content.
- **Also render the slides to images and look at them.** Text extraction
  misses image-only slides, placeholder markers ("?"), strikethrough, and
  the actual visual. On macOS with LibreOffice:
  `soffice --headless --convert-to pdf deck.pptx && pdftoppm -r 80 -png deck.pdf slide`
  then view each PNG. Work on a copy in a temp folder and delete it afterward.
- **Exported text / described deck:** use what the user provides; ask for the
  slide titles in order at minimum (the titles carry most of the diagnosis).

### Step 2 — Score against the rubric

Apply Reference D. Evaluate, at the deck level:

- **Title storyline** — do the titles, read alone, tell the whole argument?
- **Lead-with-the-answer** — is the recommendation up front (SCQA), or buried?
- **Numbers reconcile** -- does each metric match across slides and notes,
  and do the parts sum to the totals?
- **Framework fit** -- what situation is this deck in, and does its structure
  match the spine in Reference B? Bad news after three slides of context, or a
  decision request with no options slide, fails here.
- **Pyramid integrity** — do supporting points group logically under the message?

…and per slide:

- **Action title** — takeaway sentence vs. topic label?
- **One idea** — single idea, or overloaded?
- **Body proves title** — does everything support the headline?
- **Signal-to-noise** — dense text, redundant visuals, or clutter?
- **So-what** — is the point specific and worth caring about?
- **Nothing buried in notes / finished** -- is key content only in the
  speaker notes? Are placeholders left on the slide?

### Step 3 — Report findings (prioritized)

Produce the audit report defined in Reference D:
an overall read + scores, the **top issues ranked by impact**, and a per-slide
table with a verdict and a concrete fix (including a rewritten action title where
the title is weak). Lead with the highest-leverage fixes; don't just list every
nit.

### Step 4 — Offer a corrected storyboard

Offer to produce a fixed **storyboard** (PLAN-mode output) reflecting the
recommended structure, which the user can then rebuild from via a PPTX skill.
This turns the audit into an actionable plan rather than just a critique.

---

## What this skill does NOT do

- It does not render, style, or save `.pptx` files — that's the PPTX skill's job.
- It does not choose brand colors, fonts, or templates.
- It does not invent data or evidence. If a supporting point lacks evidence, it
  flags the gap rather than fabricating a number.
- It does not write PR/FAQs. For a Working Backwards press release, use the
  `prfaq-builder` skill.
- It does not cover engineering postmortems. ORDER (Reference B) is the
  leadership-facing version of a failure review.

When the deck needs to be built, hand the approved storyboard to the appropriate
PPTX-creation skill.

---
---

# Reference A — Methodology

The principles the skill applies, with examples and decision rules. Grounded in
Barbara Minto's Pyramid Principle (McKinsey), Nancy Duarte's storyboarding, and
Garr Reynolds' Presentation Zen (signal-to-noise, cognitive load).

## A1. Audience-first

Decide three things before anything else:

- **Who** is the audience, and how senior / familiar with the topic are they?
- **What decision or action** should the deck drive? (Approve a budget? Change a
  plan? Understand a risk?)
- **What one question** do they most need answered?

Everything in the deck serves that decision. A board wants the recommendation and
the risk; a working team wants the mechanism and the next steps. Same content,
different emphasis. If you can't name the decision, you're not ready to storyboard.

## A2. Lead with the answer — Minto Pyramid + SCQA

**Think bottom-up, communicate top-down.** You discover the answer by working
through findings; you *present* it by stating the answer first, then support.

### SCQA (the opening frame)

- **Situation** — context the audience already agrees with. Neutral, familiar.
- **Complication** — what changed / the problem / why act now. Creates tension.
- **Question** — the question the complication forces (often implicit).
- **Answer** — your recommendation / core message. This is the deck's thesis.

> Example
> - S: We run 11 regional warehouses serving all our customers.
> - C: Utilization is 40% and the annual operating cost has grown to $15M.
> - Q: How do we cut cost without slowing delivery?
> - A: Consolidate into 4 regional hubs — cutting operating cost 50% while
>   raising utilization to 80%.

### The pyramid

Put the **Answer at the top**. Beneath it, **3–5 supporting arguments** that
together make the answer true (the "key line"). Beneath each argument, the
**evidence**. Every level answers the "why?" or "how?" of the level above.

```
                 Answer / core message
        ┌────────────────┼────────────────┐
   Argument 1        Argument 2        Argument 3
   (evidence)        (evidence)        (evidence)
```

Rule: if a piece of evidence doesn't prove an argument, and an argument doesn't
prove the answer, cut it. The pyramid is a filter, not just an outline.

## A3. Action titles as a storyline

The single highest-leverage habit. **Write titles first**, before building slides.

- A title is a **full-sentence takeaway**, not a topic label.
- Reading **all the titles in order** must convey the whole argument — the
  "flip test": a busy exec reads only the titles and gets the case.
- The slide body's only job is to **prove the title**.

### Topic label → action title

| Topic label (weak) | Action title (strong) |
|--------------------|------------------------|
| Warehouse Consolidation | Consolidating to 4 hubs cuts operating cost 50% |
| Q2 Results | Q2 beat plan on every milestone metric |
| Background | Rising operating cost, not demand, is driving the budget gap |
| Competitive Landscape | Two rivals now undercut us on delivery speed |
| Recommendation | Approve the 3-phase consolidation to start in Q3 |
| Risks | The only material risk — delays during the move — is covered by a 2-hub overlap |
| Next Steps | Three decisions today unblock a Q3 pilot |

### Title patterns that work

- **Claim + metric:** "Automation cut cycle time 60%."
- **Comparison:** "Regional hubs beat local warehouses on cost *and* speed."
- **Cause:** "Operating cost, not demand, drives the gap."
- **Imperative (for decisions):** "Approve the Q3 pilot."

Avoid: one-word/topic titles, vague titles ("Overview", "Details"), and titles
that just name the chart ("Revenue by quarter").

## A4. One idea per slide

Each slide carries exactly one idea. Tests:

- If the title needs an **"and"** joining two claims, split the slide.
- If the body has two unrelated visuals, split the slide.
- If you can't write a single-sentence takeaway title, the slide has >1 idea.

Splitting is cheap and almost always improves clarity. A 12-slide deck of single
ideas beats a 6-slide deck of double ideas.

## A5. Signal over noise (Presentation Zen / cognitive load)

The audience has limited working memory (~3–5 items). Spend it on the message,
not on decoding the slide.

- **Visuals amplify, never duplicate.** Don't put the same point in a sentence
  AND a chart AND a bullet. Pick the form that proves it fastest.
- **Cut every non-essential element.** Logos-on-every-slide, decorative clip
  art, full-sentence bullets read aloud — all noise.
- **Prefer one strong visual** (a stat callout, one clean chart, a comparison)
  over a wall of text.
- **Whitespace is not wasted space** — it directs attention.

For a presented (live) deck, the slide supports the speaker; for a leave-behind
(read alone), the slide carries a bit more, but the action title still does the
heavy lifting.

## A6. The "so what?" test (cross-cutting)

For every slide, ask "so what?" The answer must be **specific and consequential**,
not a restatement of the data.

- Weak: "Costs went up." (so what?)
- Strong: "Operating cost grew $5M in 12 months — enough to fund the consolidation."

If a slide's so-what is generic or missing, the slide is filler. Cut it or sharpen it.

## Quick reference — the order of operations

1. Audience + decision + one core message + situation (picks the framework).
2. Spine: SCQA + pyramid by default, or the situation's framework from
   Reference B. BLUF either way.
3. Action titles for every slide; read them top-to-bottom (flip test).
4. One idea per slide; split as needed.
5. For each slide: pick the visual that proves the title; cut noise.
6. So-what check on every slide.
7. Write the storyboard; review; hand to a PPTX skill.

---
---

# Reference B — Executive Frameworks

SCQA plus the Minto pyramid (Reference A) is the default spine. It fits
recommendations. It fits poorly when the deck delivers a miss, escalates a
problem, reports status, or announces a change. This section maps those
situations to a spine built for them.

## How to use this section

1. **Name the situation** in PLAN Step 1 (see the selector below).
2. **Use that framework's steps as the deck's key line** in place of SCQA. Each
   step becomes a slide or a section.
3. **Keep every other principle.** BLUF, action titles, one idea per slide,
   signal over noise, and the so-what test all still apply. The pyramid still
   applies *under* each step: every claim needs its evidence.
4. **If no situation fits, use SCQA.** Don't force a framework.

### Selector

| Situation | Framework | Typical length |
|-----------|-----------|----------------|
| Any deck, any situation | **BLUF** (overlay rule, always on) | n/a |
| A recommendation or proposal | **SCQA + pyramid** (default, Reference A) | 5–12 slides |
| A missed goal, slip, overrun, or failure | **ORDER** | 1 or 5–6 slides |
| A problem you need leadership to act on now | **SBAR** | 1–4 slides |
| A choice leadership must make | **Decision memo** | 4–7 slides |
| A recurring or periodic update | **What / So What / Now What** | 1–3 slides per workstream |
| A reorg, new process, or operating-model rollout | **Change announcement** | 5–8 slides |

Situations can stack. A slip that needs a leadership decision is ORDER with a
decision memo for Resolution. Pick the framework for the *primary* job of the
deck, and nest the other inside one step.

## BLUF -- Bottom Line Up Front

**Source:** US military writing practice.

**Rule, not an arc.** The conclusion, decision, or ask appears in the first
sentence the audience reads. On a deck, that means the action title of slide 1
(or the executive summary slide) states the bottom line. Everything after
supports it.

**Applies to every framework below.** Each has a note on where its bottom line
goes.

**Test:** if the exec stopped after the first slide, would they know the answer
and what you need from them? If not, the deck fails BLUF.

**Failure mode:** a "context" or "background" slide before the bottom line.
Context earns its place only after the audience knows why they need it.

## ORDER -- delivering bad news

**Use when:** a goal was missed, a date slipped, a budget overran, or something
failed, and leadership needs to hear it from you first.

**Source:** found online; origin unverified. Don't attribute it to anyone in
deliverables.

| Step | What it says | Action-title pattern |
|------|--------------|----------------------|
| **Objective** | The original goal, commitment, or target | "We committed to <X> by <date>" |
| **Result** | What actually happened, stated plainly with the number | "We delivered <Y>, <gap> short of target" |
| **Diagnosis** | The cause or causes. Root cause, not symptoms | "<Cause>, not <assumed cause>, drove the miss" |
| **Explain** | What the cause affected: scope, cost, schedule, people, customers | "The slip moves <dependency> to <date> and costs <$>" |
| **Resolution** | What's being done, by whom, the recovery date, and the ask | "<Action> recovers <X> by <date>; we need <ask>" |

**BLUF placement:** Objective and Result share slide 1, or the executive summary
states them in one line: "We committed to X; we delivered Y; here's the fix."
The miss must be visible on the first slide.

**One-slide version:** five rows, one per step, title = Result + Resolution.

**Failure modes:**
- Result arrives on slide 3 or later, after the context.
- Diagnosis lists symptoms ("the vendor was late") without the cause ("we had no
  second source").
- Explain is skipped, so leadership can't size the impact.
- Resolution has actions but no recovery date, owner, or ask.
- Blame aimed at people instead of the system. Diagnose causes, not culprits.

## SBAR -- escalation

**Use when:** a problem needs a leader's action, decision, or air cover now, and
the audience has minutes, not an hour. Tighter than ORDER: ORDER explains a past
miss; SBAR gets help with a live problem.

**Source:** commonly credited to US Navy submarine communications, adapted by
Kaiser Permanente for clinical handoffs.

| Step | What it says | Action-title pattern |
|------|--------------|----------------------|
| **Situation** | What is happening right now, in one sentence | "<Thing> is at risk of <outcome> by <date>" |
| **Background** | Only the context needed to understand the situation | "This started when <event>" |
| **Assessment** | Your read: the cause, the severity, what happens if nothing changes | "Without action, <consequence>" |
| **Recommendation** | What you want done, and by whom | "Approve <X> / call <person> / decide <Y> by <date>" |

**BLUF placement:** on a one-slide SBAR, the title is the Recommendation. On a
multi-slide SBAR, slide 1 title combines Situation and Recommendation.

**Failure modes:**
- Background grows into a history lesson. Cap it at what the Assessment needs.
- Assessment is missing, so the leader has to diagnose it themselves.
- Recommendation is vague ("need support") instead of a specific ask.

## Decision memo -- asking for a choice

**Use when:** leadership must pick between real options: approve or reject,
fund A or B, accept a risk or pay to mitigate it.

**Source:** general executive practice; no single origin.

| Step | What it says | Action-title pattern |
|------|--------------|----------------------|
| **Decision needed** | The exact question, and when it must be decided | "Decide <X> by <date> to hold <milestone>" |
| **Options** | Two or three real options, always including "do nothing" | "Three options; only B holds the date" |
| **Recommendation** | Your pick and the deciding reason | "Choose B: <deciding reason>" |
| **Risks** | What could go wrong with the recommendation, and mitigations | "B's main risk, <X>, is mitigated by <Y>" |
| **Ask** | What you need from this audience, today | "Approve B and <resource> today" |

**BLUF placement:** slide 1 title states the decision and your recommendation:
"Choose B to hold the Q3 date." The options slide comes second, as proof.

**Visual:** the options slide is usually a `comparison` or a table with the same
criteria across every option (cost, time, risk, what it gives up).

**Failure modes:**
- Straw-man options that exist only to make the recommendation look good.
- "Do nothing" omitted, so the cost of inaction is never shown.
- Options compared on different criteria.
- No deadline, so the decision drifts.

## What / So What / Now What -- status update

**Use when:** a recurring update: monthly program review, quarterly business
review, weekly status. It forces the "so what" that status decks usually skip.

**Source:** Borton's reflective model (1970), later popularized by Rolfe,
Freshwater, and Jasper (2001).

| Step | What it says | Action-title pattern |
|------|--------------|----------------------|
| **What** | What happened since last time: facts, metrics, milestones, and the delta | "<Workstream> hit <milestone>; <metric> moved <delta>" |
| **So What** | Why it matters: what it proves, what it puts at risk, trend vs. plan | "That puts <goal> on track / at risk by <date>" |
| **Now What** | Next actions, owners, and any asks | "Next: <action>; we need <ask>" |

**BLUF placement:** lead with the overall status (on track / at risk / off
track) in slide 1's title, then run the three steps per workstream.

**Pairs with RAG status:** if the program uses red/amber/green, the So What
justifies the color, and any amber or red workstream needs a Now What with a
path back to green.

**Failure modes:**
- All What, no So What: a list of activities with no meaning attached.
- Repeating the whole story every period instead of the delta.
- Every workstream green until the month it turns red. If So What never says
  "at risk," it isn't doing its job.

## Change announcement -- reorg, new process, operating model

**Use when:** telling people something about how they work is changing:
reorganizations, new roles, new processes, operating-model rollouts, tool
retirements.

**Source:** common change-communication pattern; origin unknown.

| Step | What it says | Action-title pattern |
|------|--------------|----------------------|
| **Why** | The problem the change solves, in concrete terms | "<Problem> costs us <X>; the current model can't fix it" |
| **What's changing** | The change itself, specifically | "Starting <date>, <role/process> becomes <new state>" |
| **What's not changing** | What stays the same | "Your <manager/team/tools> stay the same" |
| **What it means for you** | The impact, by audience segment if they differ | "For <group>, this means <specific change>" |
| **What's next** | Timeline, where to ask questions, how feedback works | "<Milestones> through <date>; questions go to <channel>" |

**BLUF placement:** slide 1 title states the change and the date in one
sentence. Don't open with a long Why: people can't hear the rationale until they
know what's happening to them.

**The step most decks drop:** What's not changing. Uncertainty fills every gap,
and naming what stays the same lowers anxiety more than anything else in the
deck.

**Failure modes:**
- Why is abstract ("to drive alignment") instead of a concrete problem.
- What it means for you is missing or generic, so every person in the room has
  to work it out alone.
- No feedback path, so the announcement reads as final when it may not be.
- Characterizations of the old model that land on the people who ran it. Aim
  the case at the system.

---
---

# Reference C — Storyboard Schema & Handoff Contract

The storyboard is the deliverable of PLAN mode and the input a PPTX-creation
skill consumes. It is plain Markdown so the user can read, edit, and version it.

## File

Name it `<deck-name>-storyboard.md` and save it in the user's working folder.
It has two parts: a **header block** (the argument) and a **slide list**.

## Header block

```markdown
# <Deck title> — Storyboard

**Audience:** <who, seniority, familiarity>
**Decision/action:** <what they should do or believe after>
**Core message (one sentence):** <the single thing to remember>
**Format:** <live presentation | leave-behind> · ~<N> slides · <time limit if any>
**Framework:** <SCQA (default) | ORDER | SBAR | Decision memo | What/So What/Now What | Change announcement>
**Bottom line (BLUF):** <what slide 1's title says>

## Argument (SCQA)
- **Situation:** <agreed context>
- **Complication:** <what changed / why now>
- **Question:** <the question that raises>
- **Answer:** <the recommendation = core message>

> If the framework isn't SCQA, replace this section with the framework's steps,
> one line each, e.g. `## Argument (ORDER)` with Objective, Result, Diagnosis,
> Explain, Resolution. See Reference B.

## Supporting arguments (pyramid)
1. <argument 1> — proof: <evidence>
2. <argument 2> — proof: <evidence>
3. <argument 3> — proof: <evidence>
```

## Slide list

One block per slide, in order. **One idea per slide.**

```markdown
### Slide <n> — <role: cover | agenda | section | content | recommendation | closing>
- **Action title:** <full-sentence takeaway — appears as the slide title>
- **One idea:** <the single point this slide makes>
- **Visual component:** <stat-callout | metric-dashboard | comparison | step-flow |
  timeline | chart:<type> | quote | icon-list | card-grid | image | text>
- **Content/evidence:** <the specific data, items, or copy that proves the title>
- **So-what / notes:** <why it matters; optional speaker note>
```

### Minimal example

```markdown
### Slide 3 — content
- **Action title:** Operating cost grew $5M in 12 months — enough to fund the consolidation
- **One idea:** Cost growth, not demand, is the budget problem
- **Visual component:** chart:column (operating cost by quarter, 4 quarters)
- **Content/evidence:** $10M a year ago → $15M today; demand flat over same period
- **So-what / notes:** Sets up the consolidation as self-funding; lead-in to Slide 4
```

## Field rules

- **Action title** — required; must be a takeaway sentence (see Reference A).
- **One idea** — required; if you can't state it in one sentence, split the slide.
- **Visual component** — use the vocabulary above so a PPTX skill can map it to a
  layout/component. `chart:<type>` where type ∈ {column, bar, line, pie, area}.
- **Content/evidence** — be concrete (real numbers, real list items). If evidence
  is missing, write `EVIDENCE NEEDED: <what>` rather than inventing data.
- **So-what / notes** — optional but recommended; also used as the speaker note.

## Handoff contract (how a PPTX skill consumes this)

A PPTX-creation skill treats the storyboard as its
slide-by-slide build plan:

1. **One storyboard slide block → one slide.** Order is preserved.
2. **Action title → the slide's title text.**
3. **Visual component → the layout/component choice.** Map the vocabulary:
   - `stat-callout`, `metric-dashboard` → stat/KPI card layout
   - `comparison` → two-column / side-by-side layout
   - `step-flow`, `timeline` → process layout
   - `chart:<type>` → native chart of that type
   - `quote` → quote block; `icon-list`/`card-grid` → list/grid; `image` → image+caption
   - `text` → title + minimal supporting text (use sparingly)
4. **Content/evidence → the body content** the slide must render.
5. **So-what / notes → speaker notes** (and a sanity check that the slide earns
   its place).
6. **Header block → deck-level setup:** core message can seed the cover subtitle;
   the bottom line and the argument (SCQA or framework steps) can seed an
   executive-summary slide if the format calls for one.

The PPTX skill owns all visual decisions (brand, color, fonts, exact layout). The
storyboard never specifies styling — only structure, message, and evidence.

> Tip: keep the storyboard's visual-component names aligned with the target PPTX
> skill's component menu when you know which skill will build the deck.

---
---

# Reference D — Audit Rubric & Report Format

How AUDIT mode scores an existing deck and reports findings. Be specific and
prioritized: lead with the few fixes that most improve the deck, not every nit.

## What to evaluate

### Deck-level (the highest-leverage checks)

| Check | Pass looks like | Fail looks like |
|-------|-----------------|-----------------|
| **Title storyline (flip test)** | Reading titles top-to-bottom conveys the full argument | Titles are topic labels; the thread is missing |
| **Lead with the answer** | Recommendation/core message appears early (SCQA) | The "ask" is buried near the end |
| **Numbers reconcile** | The same metric matches across slides and speaker notes, and parts sum to their totals | One figure shown three ways (slide, callout, notes); bars that don't add up to the stated total; counts that double-count (the same service in two environments) without saying so |
| **Framework fit** | Structure matches the deck's situation (Reference B): bad news leads with the result, a decision request shows options including "do nothing", a change announcement says what's not changing | A miss revealed after the context; a decision with no options; a status update with no "so what" |
| **Pyramid integrity** | Supporting sections group logically under one message | Sections are a list of topics with no spine |
| **Length vs. purpose** | Slide count fits the decision and time | Bloated with filler, or too thin to support the ask |

### Slide-level

| Check | Pass | Fail |
|-------|------|------|
| **Action title** | Full-sentence takeaway | Topic label ("Overview", "Q2 Results") |
| **One idea** | Single point | Two+ ideas / title needs an "and" |
| **Body proves title** | Every element supports the headline | Body unrelated to or broader than the title |
| **Signal-to-noise** | One clear visual; minimal text | Wall of text; redundant chart+bullets+sentence |
| **So-what** | Specific, consequential | Generic restatement of data, or none |
| **Nothing buried in notes** | Speaker notes support the slide; the key facts are on the slide | The strongest content (the answer, the backlog, the improvement list, the ask) appears only in speaker notes, or notes are copied from another slide |
| **Finished** | No placeholders | "?", "TBD", strikethrough, or empty markers left on the slide |

## Scoring

Give each deck-level check and each slide a simple verdict:

- ✅ **Strong** — meets the principle.
- ⚠️ **Needs work** — partially; fixable with a tweak.
- ❌ **Weak** — fails; needs rework.

Optionally roll up to a 1–5 deck score, but the verdicts + specific fixes matter
more than a number. Never give a score without naming the reasons.

## Report format

```markdown
# Audit — <deck name> (<N> slides)

## Overall
<2–4 sentences: does the deck lead with the answer? Do the titles tell the story?
What is the single biggest opportunity?>

**Deck-level scores**
- Title storyline: <✅/⚠️/❌> — <why>
- Lead with the answer: <✅/⚠️/❌> — <why>
- Numbers reconcile: <✅/⚠️/❌> — <mismatches, listed in a "Data to reconcile" section>
- Framework fit: <✅/⚠️/❌> — <situation, framework it should follow, where it departs>
- Pyramid integrity: <✅/⚠️/❌> — <why>
- Length vs. purpose: <✅/⚠️/❌> — <why>

## Top issues (ranked by impact)
1. <highest-leverage fix, with the concrete change>
2. <next>
3. <next>

## Per-slide findings
| # | Current title | Verdict | Issue | Suggested fix (incl. rewritten title) |
|---|---------------|---------|-------|----------------------------------------|
| 1 | <title> | ⚠️ | topic label | "<rewritten action title>" |
| 2 | <title> | ✅ | — | — |
| … | | | | |

## Recommended structure (optional)
<If the spine is wrong, sketch the corrected SCQA + section order.>
```

## Rules for a good audit

- **Prioritize.** The "Top issues" section is the point. Three high-impact fixes
  beat thirty trivial ones.
- **Be concrete.** For every weak title, supply a rewritten action title. For
  "too dense", say what to cut.
- **Diagnose the spine first.** A deck with great-looking slides but no argument
  needs restructuring, not title tweaks — say so.
- **Don't fabricate.** If you can't see a slide's data (e.g. an image-only
  chart), note the limitation rather than guessing.
- **Offer the next step.** End by offering a corrected **storyboard** (PLAN mode)
  the user can rebuild from.