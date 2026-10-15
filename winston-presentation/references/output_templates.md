# Output Templates

Boilerplate patterns for each of the three output formats. Read this when you reach Phase 6 (generation) of the workflow. Adapt the templates to the user's content; do not paste them verbatim.

The templates encode Winston's design rules at the artifact level so that the rules are enforced even if the user later edits the deck.

This file is organized as follows:

1. **Delivery mode templates** (the bulk of this file) — for Winston-pure decks where the user will present live
2. **Standalone mode templates** (toward the end) — patterns for decks the user is not there to deliver
3. **Both mode** — guidance on combining the two in a single file

Read this whole file the first time. After that, jump to the section matching the mode chosen in Phase 1.

---

## Delivery mode — Format 1 — `.pptx` (python-pptx)

### Setup

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)   # 16:9
prs.slide_height = Inches(7.5)

# Winston-styled defaults
BG_COLOR = RGBColor(0xFF, 0xFF, 0xFF)         # white
TEXT_COLOR = RGBColor(0x1A, 0x1A, 0x1A)       # near-black
ACCENT_COLOR = RGBColor(0x00, 0x55, 0xA4)     # one accent only
FONT_FAMILY = "Aptos"  # or "Helvetica" or "Calibri"
FONT_SIZE_BODY = Pt(40)
FONT_SIZE_LARGE = Pt(54)
FONT_SIZE_FOOTNOTE = Pt(20)
```

### Promise slide pattern

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank layout — no title placeholder
# Add a single text box, centered, with the promise sentence
tx_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11.33), Inches(2.5))
tf = tx_box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.alignment = PP_ALIGN.LEFT
run = p.add_run()
run.text = "By the end of these 20 minutes, you will know which two of our six product lines drove 80% of Q3 growth — and why one of them is at risk."
run.font.name = FONT_FAMILY
run.font.size = FONT_SIZE_LARGE
run.font.color.rgb = TEXT_COLOR
```

### Body slide pattern

One idea per slide. ≤15 words. No title placeholder. Speaker notes carry the substance.

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])
tx_box = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(11.33), Inches(1.5))
tf = tx_box.text_frame
p = tf.paragraphs[0]
run = p.add_run()
run.text = "Product line A: 47% of growth, 12% of customers."  # 10 words — well within ceiling
run.font.name = FONT_FAMILY
run.font.size = FONT_SIZE_BODY
run.font.color.rgb = TEXT_COLOR

# Speaker notes
notes = slide.notes_slide.notes_text_frame
notes.text = "We just finished talking about the topline number. Now I want to zoom in. Product line A is responsible for forty-seven percent of our Q3 growth, but it's reaching only twelve percent of our customers. So almost half of our growth is concentrated in a tenth of our base. This may sound like a healthy growth story, but the concentration is actually a risk — and that's what I want to walk through next."
```

### Section divider pattern (verbal punctuation)

A single short phrase, generously spaced, marking a section boundary.

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])
tx_box = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(11.33), Inches(1.5))
tf = tx_box.text_frame
p = tf.paragraphs[0]
run = p.add_run()
run.text = "2 of 3:  the risk."   # numbered milestone reinforces verbal punctuation
run.font.name = FONT_FAMILY
run.font.size = FONT_SIZE_LARGE
run.font.color.rgb = ACCENT_COLOR
```

### Contributions slide pattern (the closer)

Specific, concrete, mirrors the promise. Title says "Contributions" — never "Conclusions" or "Thank you."

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Header
header = slide.shapes.add_textbox(Inches(1), Inches(0.5), Inches(11.33), Inches(1))
header.text_frame.paragraphs[0].add_run().text = "Contributions"
header.text_frame.paragraphs[0].runs[0].font.size = Pt(36)
header.text_frame.paragraphs[0].runs[0].font.color.rgb = ACCENT_COLOR
header.text_frame.paragraphs[0].runs[0].font.name = FONT_FAMILY

# Three contributions, generously spaced
contributions = [
    "Identified the two product lines driving 80% of Q3 growth",
    "Quantified the concentration risk in product line A",
    "Recommended a $4M reallocation to product line C in Q4",
]
for i, contrib in enumerate(contributions):
    tx_box = slide.shapes.add_textbox(Inches(1), Inches(2 + i * 1.4), Inches(11.33), Inches(1.2))
    p = tx_box.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = f"{i+1}.  {contrib}"
    run.font.size = FONT_SIZE_BODY
    run.font.name = FONT_FAMILY
    run.font.color.rgb = TEXT_COLOR
```

### Save

```python
import os
out_path = "/mnt/user-data/outputs/winston_deck.pptx"
prs.save(out_path)
```

### Pre-flight checks before saving

Before calling `prs.save()`, walk the deck programmatically and verify:

- No slide has more than 25 words (count words in all text frames)
- No font size is below 28pt
- No slide has a `notes_slide` mentioning "thank you" as the close (if speaker notes were generated)
- The first slide contains the empowerment promise
- The last slide is titled "Contributions"

If any check fails, fix before saving and tell the user what was adjusted.

### Render-and-inspect verification

Pre-flight word-count and font-size checks are necessary but not sufficient. python-pptx will happily place a textbox where it overlaps another textbox; the visual collision only appears when the deck is rendered. Before declaring the deck done:

1. Convert the `.pptx` to PDF using LibreOffice headless: `libreoffice --headless --convert-to pdf <deckname>.pptx`
2. Convert the PDF to PNGs: `pdftoppm -r 80 <deckname>.pdf slide -png`
3. View each rendered slide and check for collisions, runaway wraps, and missing elements
4. Fix any issues, regenerate, and re-render

Skipping this step is the difference between a deck that "should work" and a deck that does work. The build looks clean from the python side even when the rendered output has serious problems.

### Layout fragility — four lessons from real builds

These pitfalls are not in python-pptx documentation but show up reliably in real Winston-style pptx work. Apply these defaults proactively rather than learning them by collision.

**1. Fixed-position layouts break when text wraps unpredictably.** Hardcoding `top=Inches(N)` for sequential items assumes you know how many lines each item will wrap to, which you don't. If contribution 3 wraps to 3 lines instead of the expected 2, it overlaps contribution 4. Two defenses: (a) tighten wording so every item fits the row height you designed for, or (b) use a length-based estimate to bump row spacing for longer items. Sample heuristic: `row_height = 1.0 if len(text) > 110 else 0.75`. This is approximate but reliable enough for executive deck content.

**2. Label-column widths must fit the longest label, not the typical one.** SCQ-style slides (Situation/Complication/Findings/Recommendation) wrap "Recommendation:" to two lines if the column is sized for "Situation:". Default to ~2.4 inches for SCQ label columns; widen further if labels exceed that.

**3. Page numbers and full-width footer elements collide.** A page number in the bottom-right corner overlaps any context line or source citation that spans the full slide width. Either narrow context-line textboxes to ~10.8 inches (leaves a 1.5-inch gutter on the right for the page number) or move the page number high enough that it sits above the context line area. The gutter approach is cleaner.

**4. LibreOffice and PowerPoint render differently.** LibreOffice headless conversion is the right tool for fast iteration during build, but the final deck should also open cleanly in PowerPoint itself. Aptos in particular may fall back to Calibri on machines where Aptos isn't installed; declaring `FONT = "Aptos"` with a known-installed fallback (Calibri or Helvetica) is a reasonable default.

---

## Delivery mode — Format 2 — single-page HTML

### Structure

**Two files, not one.**

- `<deckname>.html` — the deck. Slides only. Clean, projectable, shareable.
- `<deckname>_notes.html` — the companion notes file. One section per slide, mirroring the deck's structure, with the speaker notes (or reader notes in standalone mode) for that slide. Opened in a second browser tab during rehearsal or async reading.

The two files cross-link: the deck has a small "Speaker notes →" link in the corner of each slide pointing to the corresponding section in the notes file; the notes file has a "← Back to slide" link on each section pointing back to the deck.

This split exists because the deck file is a *delivery artifact* — it gets projected at meetings, attached to emails, embedded in tools. Notes baked into the deck make it look unprofessional in those contexts and risk being shown by accident. The notes companion is a *preparation artifact* — it stays on the speaker's laptop, or accompanies the deck in a "deck + notes" zip when both are useful.

If the user explicitly prefers the notes inline (some users want a single self-contained rehearsal file), or wants the notes as Markdown for printing, honor the preference. The default is two HTML files.

### Deck file template (slides only)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[Talk title — say it, don't show it]</title>
<style>
  :root {
    --bg: #ffffff;
    --text: #1a1a1a;
    --accent: #0055a4;
    --font: 'Aptos', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font);
    color: var(--text);
    background: var(--bg);
    line-height: 1.4;
  }
  section.slide {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 6rem;
    border-bottom: 1px solid #eee;
  }
  section.slide .content {
    font-size: 2.5rem;     /* ≈ 40pt equivalent */
    font-weight: 400;
    max-width: 60ch;
  }
  section.slide.large .content {
    font-size: 3.5rem;
  }
  section.slide.divider .content {
    color: var(--accent);
    font-size: 3rem;
  }
  section.contributions ol {
    list-style: none;
    counter-reset: contrib;
  }
  section.contributions li {
    counter-increment: contrib;
    margin: 1.5rem 0;
    padding-left: 3rem;
    position: relative;
    font-size: 2rem;
  }
  section.contributions li::before {
    content: counter(contrib) ".";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: 600;
  }
  /* Notes link in corner of each slide — only visible on hover, subtle */
  a.notes-link {
    position: absolute;
    bottom: 1.5rem;
    right: 2rem;
    font-size: 0.85rem;
    color: #bbb;
    text-decoration: none;
    opacity: 0.5;
    transition: opacity 0.2s;
  }
  a.notes-link:hover { opacity: 1; color: var(--accent); }
  @media (max-width: 768px) {
    section.slide { padding: 2rem; }
    section.slide .content { font-size: 1.8rem; }
    a.notes-link { display: none; } /* hide on mobile presentation */
  }
</style>
</head>
<body>

<!-- Slide 1: Promise -->
<section class="slide large" id="slide-1">
  <div class="content">
    By the end of these 20 minutes, you will know which two of our six product lines drove 80% of Q3 growth — and why one of them is at risk.
  </div>
  <a class="notes-link" href="winston_deck_notes.html#slide-1" target="_blank">Speaker notes →</a>
</section>

<!-- Slide 2: Body slide -->
<section class="slide" id="slide-2">
  <div class="content">
    Product line A: 47% of growth, 12% of customers.
  </div>
  <a class="notes-link" href="winston_deck_notes.html#slide-2" target="_blank">Speaker notes →</a>
</section>

<!-- Slide 3: Section divider (verbal punctuation) -->
<section class="slide divider" id="slide-3">
  <div class="content">
    2 of 3: the risk.
  </div>
</section>

<!-- ...more body slides... -->

<!-- Final slide: Contributions -->
<section class="slide contributions" id="slide-N">
  <div class="content">
    <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 2rem;">Contributions</h2>
    <ol>
      <li>Identified the two product lines driving 80% of Q3 growth</li>
      <li>Quantified the concentration risk in product line A</li>
      <li>Recommended a $4M reallocation to product line C in Q4</li>
    </ol>
  </div>
  <a class="notes-link" href="winston_deck_notes.html#slide-N" target="_blank">Speaker notes →</a>
</section>

</body>
</html>
```

### Companion notes file template

The notes file is a standalone HTML document, styled as a quiet readable column rather than as full-viewport slides. Each section corresponds to a slide in the deck and includes a back-link.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Speaker Notes — [Talk title]</title>
<style>
  :root {
    --bg: #fafafa;
    --text: #1a1a1a;
    --accent: #0055a4;
    --muted: #666;
    --rule: #e0e0e0;
    --font: 'Aptos', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: var(--font);
    color: var(--text);
    background: var(--bg);
    line-height: 1.6;
    padding: 3rem 2rem;
  }
  main {
    max-width: 70ch;
    margin: 0 auto;
  }
  header.doc-header {
    margin-bottom: 3rem;
    padding-bottom: 1.5rem;
    border-bottom: 2px solid var(--rule);
  }
  header.doc-header h1 {
    font-size: 1.75rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }
  header.doc-header p {
    color: var(--muted);
    font-size: 1rem;
  }
  section.note-block {
    margin-bottom: 2.5rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--rule);
  }
  section.note-block h2 {
    font-size: 1.25rem;
    color: var(--accent);
    margin-bottom: 0.5rem;
  }
  section.note-block .slide-content {
    font-style: italic;
    color: var(--muted);
    margin-bottom: 1rem;
    padding: 0.75rem 1rem;
    background: #fff;
    border-left: 3px solid var(--rule);
    font-size: 0.95rem;
  }
  section.note-block .notes-body p {
    margin-bottom: 0.75rem;
    font-size: 1rem;
  }
  a.back-link {
    display: inline-block;
    margin-top: 1rem;
    font-size: 0.85rem;
    color: var(--muted);
    text-decoration: none;
  }
  a.back-link:hover { color: var(--accent); }
</style>
</head>
<body>
<main>

<header class="doc-header">
  <h1>Speaker Notes — [Talk title]</h1>
  <p>Companion to <a href="winston_deck.html">winston_deck.html</a>. Open side-by-side with the deck for rehearsal, or read on its own as a written version of the talk.</p>
</header>

<section class="note-block" id="slide-1">
  <h2>Slide 1 — Promise</h2>
  <div class="slide-content">"By the end of these 20 minutes, you will know which two of our six product lines drove 80% of Q3 growth — and why one of them is at risk."</div>
  <div class="notes-body">
    <p>Open with the promise verbatim. Pause after "at risk" — let the room sit with it for a beat. This is the empowerment promise; everything in the next twenty minutes earns its way back to this sentence.</p>
  </div>
  <a class="back-link" href="winston_deck.html#slide-1">← Back to slide</a>
</section>

<section class="note-block" id="slide-2">
  <h2>Slide 2 — Concentration</h2>
  <div class="slide-content">"Product line A: 47% of growth, 12% of customers."</div>
  <div class="notes-body">
    <p>Here's the concentration. Forty-seven percent of growth in a product reaching twelve percent of our customers. This may sound like a healthy growth story — but the concentration itself is the risk, and that's what I want to unpack next.</p>
  </div>
  <a class="back-link" href="winston_deck.html#slide-2">← Back to slide</a>
</section>

<!-- ...one section per slide... -->
<!-- Note: section divider slides (verbal punctuation only) typically don't need notes, but include a brief one if the speaker wants a verbal cue. -->

<section class="note-block" id="slide-N">
  <h2>Slide N — Contributions</h2>
  <div class="slide-content">"Contributions: 1. Identified the two product lines... 2. Quantified the concentration risk... 3. Recommended a $4M reallocation..."</div>
  <div class="notes-body">
    <p>Redeem the promise explicitly: "I told you at the start you'd leave knowing which two product lines drove our growth and why one was at risk. Here it is." Then salute, do not thank: "It's been a pleasure presenting to this group." Take questions with this slide still up.</p>
  </div>
  <a class="back-link" href="winston_deck.html#slide-N">← Back to slide</a>
</section>

</main>
</body>
</html>
```

### Save

Write the deck to `/mnt/user-data/outputs/winston_deck.html` and the notes to `/mnt/user-data/outputs/winston_deck_notes.html`. Present both files. In Both mode, the single notes companion covers slides from both the delivery part and the standalone appendix — separated by a divider in the notes file mirroring the divider in the deck.

---

## Delivery mode — Format 3 — content/structure only (Markdown)

### Template

```markdown
# [Talk Title — for reference only, not displayed on slide 1]

**Empowerment promise**: [one sentence — the promise the deck must redeem on the contributions slide]

**Audience**: [who is in the room]
**Duration**: [minutes]
**Format intent**: hand to [styling skill name] for visual treatment

---

## Slide 1 — Promise

**On-slide content** (≤15 words):
> [The empowerment promise sentence]

**Speaker notes**:
> [3–6 sentences. Open with the promise verbatim. Pause. Set up the journey.]

---

## Slide 2 — Collaborators (only if applicable; place at front, never at end)

**On-slide content**:
> Worked with: [names]

**Speaker notes**:
> [Brief acknowledgment, then move on. Do not dwell.]

---

## Slide 3 — Vision

**On-slide content** (≤15 words):
> [Problem statement + what's new in the approach]

**Speaker notes**:
> [Situate the work — time, space, field. Why this problem? Why now? What's new about the approach?]

---

## Slide 4 — Proof of done-something

**On-slide content**:
> [Concrete steps taken — not vague accomplishments]

**Speaker notes**:
> [The concrete work. By the end of this slide, the audience must believe the speaker has done something real. This is the second half of the 5-minute rule.]

---

## Slide 5 — [first body idea]

**On-slide content** (≤15 words):
> [The handle, not the substance]

**Speaker notes**:
> [The substance. First cycle pass: brief framing. Use a fence here if the idea is near-miss territory.]

---

## Slide 6 — [section divider, optional]

**On-slide content**:
> 2 of 3: [section label]

**Speaker notes**:
> "We just finished talking about [X]. Now we turn to [Y]." (Verbal punctuation — give the foggy 20% a place to rejoin.)

---

## [...continue for body slides...]

Each body slide:
- ≤15 words on-slide
- Speaker notes carry the substance
- Cycle the central idea at least three times across the body
- Use rhetorical questions sparingly (one or two for the whole talk, with 7-second pauses)
- Build a fence around any concept that could be confused with a neighbor

---

## Slide N — Contributions (the closer; **never** "Conclusions" or "Thank you")

**On-slide content**:
> **Contributions**
> 1. [Specific contribution mirroring the promise]
> 2. [Specific contribution]
> 3. [Specific contribution]

**Speaker notes**:
> Redeem the promise explicitly: "I told you at the start that you'd leave knowing [X]. Here is [X]."
> Salute the audience — do not thank them: "It's been a pleasure presenting to this group."
> Take questions with this slide still up.

---

## Optional — Winston's Star annotations

If the user wanted memorability:
- **Symbol**: [the visual handle — what's drawn on slide N or wherever]
- **Slogan**: [one-sentence handle the audience repeats afterward]
- **Surprise**: [the counterintuitive moment — which slide carries it]
- **Salient idea**: [the one idea that sticks out — which slide carries it]
- **Story**: [the narrative thread woven through the body slides]

---

## Self-check

Before declaring the outline complete, verify:

- [ ] The promise on slide 1 and the contributions on slide N mirror each other
- [ ] Vision and proof are both established within the first ~25% of slides
- [ ] Each body idea is cycled at least three times
- [ ] Verbal punctuation marks every section boundary in speaker notes
- [ ] No slide ends the deck with "Conclusions", "Questions?", "Thank you", or a URL
- [ ] No on-slide content exceeds 25 words
- [ ] Collaborators (if any) are at the front, not the end
```

### Save

Write to `/mnt/user-data/outputs/winston_deck.md` and present.

---

## Choosing between formats

| User says | Format |
|-----------|--------|
| "Make me slides" / "Build a PowerPoint" / "I need a deck" | `.pptx` |
| "Build me a webpage version" / "Something I can share as a link" / "One scrolling page" | HTML |
| "Just give me the structure" / "Outline" / "I'll style it myself" / "For our company template" | Markdown |

If unclear, ask. Don't guess between formats — the user's distribution channel matters more than convenience.

---

## Standalone mode templates

Standalone mode reuses the same three formats but with relaxed design rules and a different slide skeleton. The key differences from delivery-mode templates:

- More words per slide (~75–100 target, 150 ceiling)
- Slide titles required on body slides
- Page numbers required
- Charts get full legends, axis labels, source citations
- A 1–2 sentence context line under each major idea
- Executive summary slide at the front
- Glossary slide allowed when jargon is present
- Q&A / contact slide allowed at the end (after Contributions, never replacing it)
- The "speaker notes" pane becomes "reader notes" — annotations, anticipated Q&A, cross-references

Read `standalone_mode.md` for the full rules. The templates below show the shape; the rules document is authoritative on content.

### Standalone mode — Format 1 — `.pptx` (python-pptx)

The setup block at the top of this file still applies. Override these constants:

```python
# Standalone-mode overrides
FONT_SIZE_BODY = Pt(24)         # was 40 in delivery
FONT_SIZE_HEADLINE = Pt(32)     # the headline statement on each body slide
FONT_SIZE_FOOTNOTE = Pt(18)     # was 20
WORD_CEILING = 150              # was 25
```

Use a layout with a title placeholder (e.g. `prs.slide_layouts[1]` for "Title and Content") rather than the blank layout used in delivery mode.

#### Executive summary slide pattern

```python
slide = prs.slides.add_slide(prs.slide_layouts[1])  # has title placeholder
slide.shapes.title.text = "Executive Summary"

# SCQ + Recommendation, structured
content = slide.placeholders[1].text_frame
content.text = "Situation: Q3 revenue grew 12%, our strongest quarter in two years."
content.add_paragraph().text = ""
p = content.add_paragraph()
p.text = "Complication: 80% of that growth came from two of six product lines, and product line A — half of all growth — is showing concentration risk."
content.add_paragraph().text = ""
p = content.add_paragraph()
p.text = "Findings:"
for finding in [
    "Product line A: 47% of growth, 12% of customers (high concentration)",
    "Product line C: outperforming projections by 23%, underinvested",
    "Product line F: declining 8% YoY, no clear path to recovery",
]:
    p = content.add_paragraph()
    p.text = f"• {finding}"
content.add_paragraph().text = ""
p = content.add_paragraph()
p.text = "Recommendation: Reallocate $4M from product line F to product line C in Q4; commission a customer concentration study for product line A."
```

#### Body slide pattern (4-part anatomy)

```python
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "Concentration Risk in Product Line A"

# Headline statement (larger, top of body area)
headline_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(12.33), Inches(0.8))
p = headline_box.text_frame.paragraphs[0]
run = p.add_run()
run.text = "47% of Q3 growth came from a product reaching only 12% of our customers."
run.font.size = FONT_SIZE_HEADLINE
run.font.color.rgb = ACCENT_COLOR
run.font.bold = True

# Body content (~50–75 words)
body_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.33), Inches(3.5))
tf = body_box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.add_run().text = "Product line A drove $4.2M of the $9M Q3 revenue increase. However, our analysis shows this revenue is concentrated among 47 enterprise accounts — primarily in three industry verticals. The top 10 of those accounts represent 60% of product line A revenue. If any single account churns, we lose 8% of total Q3 growth."
for run in p.runs:
    run.font.size = FONT_SIZE_BODY

# Context/background line (smaller, at bottom)
context_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.3), Inches(12.33), Inches(0.5))
p = context_box.text_frame.paragraphs[0]
run = p.add_run()
run.text = "Context: customer concentration is measured as the % of revenue from the top 10 accounts. Industry benchmark for healthy SaaS is <30%."
run.font.size = FONT_SIZE_FOOTNOTE
run.font.italic = True

# Page number (bottom right)
# Set up via slide master, or add a textbox on each slide
```

#### Pre-flight checks for standalone

Before saving, verify:

- Every body slide has a title
- Every body slide has a headline statement and a context line
- Page numbers appear on all slides except the title slide
- The deck contains, in order: title, executive summary, vision, proof, body slides, [optional glossary], contributions, [optional Q&A]
- Charts have legend, axis labels, and source citation
- Word count per slide is ≤150

After saving, perform the same render-and-inspect verification described in the delivery-mode pptx section. Standalone slides are denser than delivery slides and more vulnerable to the four layout fragilities — particularly label-column widths and page-number collisions, both of which appear naturally in standalone but rarely in delivery.

### Standalone mode — Format 2 — single-page HTML

Use the delivery-mode HTML template as the base and override these CSS values:

```css
:root {
  /* ...same color and font vars... */
}

section.slide {
  min-height: auto;          /* was 100vh in delivery */
  padding: 3rem 5rem;        /* tighter than delivery */
}

section.slide h2.title {
  font-size: 1.75rem;        /* slide titles are now required */
  color: var(--accent);
  margin-bottom: 1rem;
}

section.slide .headline {
  font-size: 1.5rem;          /* the headline statement */
  font-weight: 600;
  margin-bottom: 1.5rem;
}

section.slide .body {
  font-size: 1.1rem;          /* was 2.5rem in delivery */
  line-height: 1.6;
  max-width: 70ch;
}

section.slide .context {
  font-size: 0.9rem;
  font-style: italic;
  color: #666;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

footer.page-number {
  position: absolute;
  bottom: 1rem;
  right: 1.5rem;
  font-size: 0.85rem;
  color: #999;
}
```

Body slide pattern in HTML:

```html
<section class="slide standalone" id="slide-5">
  <h2 class="title">Concentration Risk in Product Line A</h2>
  <p class="headline">47% of Q3 growth came from a product reaching only 12% of our customers.</p>
  <div class="body">
    <p>Product line A drove $4.2M of the $9M Q3 revenue increase. However, our analysis shows this revenue is concentrated among 47 enterprise accounts...</p>
  </div>
  <div class="context">
    Context: customer concentration is measured as the % of revenue from the top 10 accounts. Industry benchmark for healthy SaaS is &lt;30%.
  </div>
  <a class="notes-link" href="winston_deck_notes.html#slide-5" target="_blank">Reader notes →</a>
  <footer class="page-number">5</footer>
</section>
```

The reader notes for this slide live in the companion notes file under the matching `id="slide-5"` anchor. The same `notes-link` styling used in delivery mode applies here — subtle in the corner, opens the notes file in a new tab.

### Standalone mode — Format 3 — content/structure only (Markdown)

Use the delivery-mode Markdown template as the base and override the body slide block:

```markdown
## Slide 5 — Concentration Risk in Product Line A

**Slide title**: Concentration Risk in Product Line A

**Headline statement** (larger font on slide):
> 47% of Q3 growth came from a product reaching only 12% of our customers.

**Body** (~50–75 words):
> Product line A drove $4.2M of the $9M Q3 revenue increase. However, our analysis shows this revenue is concentrated among 47 enterprise accounts — primarily in three industry verticals. The top 10 of those accounts represent 60% of product line A revenue. If any single account churns, we lose 8% of total Q3 growth.

**Context**:
> *Customer concentration is measured as the % of revenue from the top 10 accounts. Industry benchmark for healthy SaaS is <30%.*

**Source**: Internal customer analytics, Q3 2025 close.

**Reader notes**:
> This slide identifies the central risk that drives the rest of the deck. A natural question here is: how does this compare to the previous quarter? See slide 7 for the trend data.
```

The full standalone Markdown outline includes title, exec summary, vision, proof, body slides, optional glossary, contributions, optional Q&A — in that order.

#### Standalone self-check

Before declaring the standalone outline complete, verify:

- [ ] The deck has a title slide with author, date, version
- [ ] The executive summary appears on slide 2 and includes situation, complication, findings, recommendation
- [ ] Every body slide has a title, a headline statement, body content, and a context line
- [ ] Page numbers are referenced
- [ ] Charts (if any) get full legends, axis labels, and source citations
- [ ] The Contributions slide is the rhetorical close (not "Conclusions" or "Thank you")
- [ ] An optional Q&A / contact slide, if used, follows Contributions — it does not replace it
- [ ] Reader notes add value rather than narrating the slide

---

## Both mode

In Both mode, produce one file with two parts:

**Part 1** — slides 1 through N+1 — the full delivery-mode deck (promise, collaborators, vision, proof, body, contributions). Apply delivery-mode design rules.

**Divider slide** — between the parts. Title: "Standalone Appendix" or "For Async Distribution". Brief explanation: "What follows is a standalone version of this content for readers who weren't in the live presentation."

**Part 2** — the slides after the divider — the standalone-mode deck (title-slide-equivalent for the appendix, executive summary, vision, proof, body slides with the 4-part anatomy, optional glossary, contributions, optional Q&A). Apply standalone-mode design rules.

The two parts will look visibly different. That's correct — it signals to a viewer that the appendix is a different artifact, designed for a different reader. Don't try to harmonize the visual style; the difference is the feature.

In `.pptx`, this is achieved by changing the slide layout for Part 2 (use the title-and-content layout for body slides instead of the blank layout). In HTML, by adding a class to the appendix sections that triggers the standalone CSS overrides. In Markdown, by an explicit `## Part 1 — Delivery` and `## Part 2 — Standalone Appendix` split.

The Contributions slide from Part 1 is the natural Q&A moment in the live presentation; Part 2 begins after questions wrap, when the speaker says some version of "I'll leave you with a written version of this for your reference."

---
