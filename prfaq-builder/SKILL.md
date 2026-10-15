---
name: prfaq-builder
description: Coach the user through writing an Amazon-style Working Backwards PR/FAQ (Press Release + Frequently Asked Questions) — the document teams write *before* building, to pressure-test a product idea by starting from the customer and working backwards. Use this skill whenever the user wants to write, draft, structure, review, or improve a PR/FAQ, press release for an unbuilt product, "working backwards" document, internal press release, one-pager for a new product or feature idea, or wants to validate/pitch a new product concept. Trigger even if the user doesn't say "PR/FAQ" by name — phrases like "write the press release before we build it", "work backwards from the customer", "I have a product idea I want to pressure-test", "help me think through this new feature idea", or "draft a launch announcement for something we haven't built yet" all indicate this skill. Also use it to critique or score an existing PR/FAQ draft. The skill assumes the user is new to the method and teaches the thinking as it goes.
---

# PR/FAQ Builder (Working Backwards)

## What this skill is for

The PR/FAQ is Amazon's tool for vetting a new product or feature **before building it**. You write a one-page mock press release announcing the finished product to customers, plus a set of FAQs that work backwards from that vision to the hard problems you'll have to solve. The press release is a *forcing function*: it keeps you focused on the customer and the value, not on your current capabilities, your P&L, or your competitors.

Your job with this skill is two things at once:

1. **Produce a real, well-structured PR/FAQ** in Markdown that the user can take into a review.
2. **Teach the method as you go.** Assume the user has never written one. They should come away understanding *why* each part exists and what good looks like — not just with a filled-in template. This learning goal is as important as the document. Don't lecture; teach in small, just-in-time doses tied to the section you're working on.

## Core principles to keep front of mind

These are the ideas the whole method rests on. Surface them naturally when they're relevant rather than dumping them all up front.

- **Customer-backwards, not skills-forward.** Start from what the customer needs and work back to what you'd have to build. Most people instinctively start from "what can we build with what we have today" — the PR/FAQ exists to break that habit. If the idea doesn't require solving at least one genuinely hard problem, it's probably not differentiated enough.
- **Truth-seeking, not selling.** The document is not a pitch to "win" approval. It's a tool to find out whether the idea is actually good. The best PR/FAQs spend real effort on what could make the product fail. Reward honesty over polish.
- **A funnel, not a tunnel.** It should be cheap to write one and cheap to kill one. A first draft takes a few hours, not days. Many ideas should die at this stage — that's the point. Iterating on a press release is far cheaper than iterating on a product.
- **Better / faster / cheaper.** A worthwhile idea beats the customer's current alternative on at least one of these, meaningfully. "There's always a current solution" — even if it's a spreadsheet or doing nothing. Name it.
- **Real numbers matter.** The market is worth pursuing only if enough customers have the problem *and* are willing to pay to solve it (TAM = number of customers × willingness to pay). Vague hand-waving here is the most common failure.

## The workflow

Work through this collaboratively and conversationally. Do **not** silently generate a finished document on the first turn — that "ta-da" approach defeats the learning goal and produces shallow drafts. Interview, draft section by section, and explain as you go. That said, match the user's energy: if they clearly want to move fast, batch the questions; if they're exploring, slow down.

### Step 0 — Orient (brief)

If the user is new to this (the default assumption), give a 3-4 sentence orientation in your own words: what a PR/FAQ is, that you'll write the press release *as if the product already launched*, and that the goal is to pressure-test the idea, not to sell it. Then start the interview. Keep this short — teaching happens throughout, not in a wall of text up front.

If the user already has a draft and wants a review, skip to **Reviewing a draft** below.

### Step 1 — Interview for the press release

Read `references/template.md` for the exact section structure and `references/teaching-notes.md` for the per-section "why" and the questions that draw out good answers. `references/example.md` is a short worked PR/FAQ showing the shape and voice of a good draft — consult it when you need a concrete model. Walk through the press release sections **in order**, because each depends on the one before:

1. **Customer** — who *specifically* is this for? Push back hard on "everyone." Great products serve a sharply defined segment.
2. **Problem** — from the customer's point of view, in their words. What do they do today, and why does it fall short?
3. **Solution** — what the product is and how it directly solves *that* problem. Watch for solutions that drift away from the stated problem (a very common mistake).
4. **Differentiation** — better/faster/cheaper than the current alternative, and how.
5. **Headline, sub-headline, summary, quotes, call to action** — these get easier once 1-4 are solid.

Ask about one or two sections at a time, reflect back what you heard, then draft that piece. Where the user is vague, name the gap and explain why it matters (tie it to a principle above), then help them fill it. It's fine — encouraged — to flag assumptions and mark them as things to validate later rather than pretending you have facts you don't.

### Step 2 — Draft the press release

Assemble the press release per `references/template.md`. Keep it to roughly one page. Plain language, no corporate jargon, written *to the customer*. Use a realistic, meaningful launch date (a date you'd actually aim for), not a placeholder. The customer quote and spokesperson quote should sound like real things a real person would say.

### Step 3 — Build the FAQ

This is where the hard thinking lives. The press release defines the destination; the FAQ is the map and the list of dragons. Use the full question set in `references/faq-rubric.md`, which has two parts:

- **External FAQs** — what press and customers will ask: price, how it works, availability, support, etc.
- **Internal FAQs** — what your own leaders and teammates will ask: TAM and the math behind it, competition, the hard technical/legal/operational problems, unit economics, upfront investment, dependencies, "what has to be true for this to succeed," and "top three reasons this will fail."

Don't just dump the questions. For each one, either help the user answer it or, if they can't yet, record it explicitly as an **open question to resolve** — surfacing unknowns is a feature, not a failure. The "top reasons this will fail" and "what has to be true" questions are the most valuable; spend real effort there and resist the urge to make the idea look bulletproof.

### Step 4 — Self-review against the rubric

Before delivering, check the draft against the reviewer's evaluation criteria in `references/faq-rubric.md` (the "Reviewer's lens" and "Common mistakes" sections). Tell the user honestly where the draft is strong and where it's still thin. Frame weak spots as the natural next iteration, not failures — first drafts are *supposed* to have holes.

### Step 5 — Deliver and point to next steps

Write the final document to a Markdown file and present it. Briefly remind the user how this is meant to be used: circulated and read silently at the start of a review meeting, then debated; revised across multiple drafts; and ultimately driving a clear go / no-go decision. Offer to iterate on weak sections or to produce a Word version if they want one for circulation.

## Output format

Deliver a single Markdown file using the structure in `references/template.md`. Default filename: `PRFAQ-<short-product-name>.md`. Keep the press release to ~1 page; let the FAQ run as long as the thinking requires. Clearly separate **Press Release**, **External FAQ**, and **Internal FAQ**, and include an **Open Questions / To Validate** section so unknowns are visible rather than buried.

## Reviewing a draft (when the user already has one)

If the user brings an existing PR/FAQ, switch to coach-reviewer mode:

1. Read it, then read `references/faq-rubric.md`.
2. Score it against the reviewer's seven questions and flag any of the common mistakes (`references/teaching-notes.md` and the rubric both cover these).
3. Give specific, kind, actionable feedback — point to the exact section, explain the underlying principle, and suggest a concrete fix. Lead with what's working.
4. Offer to rewrite the weak sections with them.

## A note on tone while coaching

The people using this are learning. Be encouraging and concrete. When you push back — and you should, especially on a vague customer or a problem with no real market — explain the reasoning so they internalize it for next time. The aim is that after one or two PR/FAQs with you, they could write a decent one on their own.
