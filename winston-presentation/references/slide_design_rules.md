# Slide Design Rules — Delivery Mode

This file expands the design rules for **delivery mode** — decks where the user will be in the room presenting. For standalone-mode rules (decks the user is not there to deliver), read `standalone_mode.md` instead.

The headline rule for delivery mode is unchanged from Winston: **the slide is a condiment, not the meal**. The speaker is the meal. Every design choice traces back to that.

Read this when you reach Phase 4 (slide design) of the workflow and the mode is delivery (or you are working on Part 1 of a Both-mode deck).

---

## The headline rules

| Rule | Default | Hard limit |
|------|---------|-----------|
| Words per slide | ≤15 | 25 |
| Font size, body text | 40pt | 36pt floor |
| Font size, any text | 36pt | 28pt floor (only for footnotes/sources) |
| Slide titles | Omitted | Optional only for navigable technical decks |
| Logos | None on body slides | Master slide only, if at all |
| Background patterns | None | None |
| Bullets | Sparingly | Only when items are genuinely parallel |
| Images | Simple, relevant | No clipart, no stock-photo people pointing at things |

---

## The 10 Winston crimes

When designing or reviewing slides, run the deck through this checklist. Each crime has a specific fix. Document any deliberate violations and explain why.

### 1. Too many slides

**Symptom**: more than ~1 slide per 1–2 minutes of speaking time.

**Fix**: cut. The signal that you have too many slides is that you find yourself flipping through them. If you have 60 slides for a 20-minute talk, you do not have a 20-minute talk; you have 60 4-second slides.

### 2. Too many words per slide

**Symptom**: more than 25 words on a slide, or any slide where the audience needs to *read*, not glance.

**Fix**: strip words until what's left is a handle, not a transcript. Winston's airport diagnostic — "you have too many, and they have too many words" — was always true even without seeing the slides.

### 3. Font size too small

**Symptom**: anything below 36pt for body content. Often a downstream symptom of crime #2 — the words don't fit, so the font shrinks.

**Fix**: enlarge first, *then* see if the words still fit. They won't. Cut words until they do.

### 4. Reading slides aloud

**Symptom**: the speaker's words match the slide's words.

**Fix**: write speaker notes that *say what the slide doesn't*. The slide is the handle; the speaker provides the substance. If the slide says "Q3 growth concentrated in two product lines," the speaker says *which* two and *why*.

### 5. Laser pointer

**Symptom**: any reliance on a laser pointer to direct attention.

**Fix**: put a labeled arrow on the slide itself. Refer to it verbally: "look at point 1." This keeps the speaker facing the audience and removes the dancing-red-dot distraction. For an HTML or pptx output, this means *literally drawing the arrow into the slide* during generation.

### 6. Speaker far from slides

**Symptom**: the room layout forces the audience into a tennis-match between the speaker on stage left and the slide on stage right.

**Fix**: this is a presentation-day issue, not a slide-design issue, but flag it in speaker notes if the venue is known. ("Stand close to the screen — do not present from the lectern.")

### 7. No white space / no air

**Symptom**: print the deck out and lay it on a table. If it looks "heavy," it is.

**Fix**: split heavy slides into two or three. Increase margins. Remove decorative elements. White space is not wasted — it is what makes the remaining content visible.

### 8. Background clutter and logos

**Symptom**: every slide carries the company logo, the talk title, the page number, the date, and a decorative ribbon.

**Fix**: relegate all of this to the master slide if it must exist at all, or remove it. A logo on every slide adds nothing; it just trains the audience to ignore the corner of the screen.

### 9. Collaborators slide at the end

**Symptom**: a final slide listing co-authors, advisors, or team members.

**Fix**: move it to the front. Putting collaborators at the end implies the speaker's work depended on others; putting them at the front says "I worked with these people, and now here's what we did." Same content, different framing.

### 10. "Thank you" or "Questions?" as final slide

**Symptom**: the deck ends on a thank-you, a questions prompt, a URL, or a logo.

**Fix**: replace with a **Contributions** slide listing the specific, concrete things the speaker added. The contributions slide stays up during Q&A — it is the most-viewed slide of the entire deck. Spend it well.

---

## On the hapax legomenon

A *hapax legomenon* is a word that appears exactly once in a body of text. Winston borrows the term for a slide you can use exactly once per talk: a deliberately overwhelming, impossible-to-read slide whose entire job is to make the audience *feel* the complexity of something. Winston's example was a slide showing the governance structure of Afghanistan.

Rules:

- **One per talk.** Maximum. Two of these is one too many.
- **The point is the complexity.** The audience does not need to read it. The audience needs to *recoil* from it.
- **Pair it with a verbal punchline.** "You don't need to read this — you couldn't if you tried. That's the point."
- **Skip it if you don't have one.** This is not a required slide. Forcing one cheapens the technique.

---

## On images

| Use | Avoid |
|-----|-------|
| Photographs of the actual subject | Clipart |
| Diagrams the speaker drew or commissioned | Stock photos of business people in meetings |
| Charts with ≤2 series and clear labels | Charts with 6 series and a tiny legend |
| A single hero image dominating the slide | Multiple small images cluttering a slide |
| Images with deliberate white space around them | Images bleeding to the slide edges by default |

If a chart has more than two series, ask whether you can split it. If a photo is decorative rather than load-bearing, cut it.

---

## On color

Pragmatic defaults:

- **Background**: white or very light grey
- **Body text**: black or near-black
- **One accent color** for emphasis (a single hue — not a rainbow)
- **High contrast** — projected screens wash out contrast, so what looks fine on a laptop may be unreadable on a screen

Avoid:

- White text on dark backgrounds — projects as grey-on-grey
- More than one accent color
- Color-coded systems where the audience has to memorize what each color means

---

## On the slide-as-condiment principle

Every design choice traces back to this: **the slide is a condiment, not the meal**. The speaker is the meal. If a design element competes with the speaker for the audience's attention, it loses. This is the test for any decorative flourish, any animated transition, any logo in the corner: does it help the speaker, or compete with the speaker? If it competes, cut it.
