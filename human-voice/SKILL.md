---
name: human-voice
description: "Write and revise prose so it reads like a specific, thoughtful person wrote it, not an AI. Use this skill for any writing the user will send, post, publish, or say out loud, even when they don't mention AI or tone: business emails, Slack or Teams messages, memos, reports, proposals, procedures, LinkedIn and other social posts, captions, bios, YouTube scripts, video narration, hooks, outlines, and stories. Also use it whenever the user asks to humanize or de-AI text, make it \"sound like me\", check whether something sounds like AI, review a draft for AI tells, tighten or simplify prose, or rewrite in plain English. Combines Orwell's rules and plain-English discipline, Wikipedia's Signs of AI Writing field guide, a channel-aware humanizer pattern list, and StoryScope research on the narrative habits that give away AI-written stories.\n"
---

# Human Voice

AI text has a recognizable sound because language models drift toward the most statistically likely sentence. The result is prose that is less specific and more inflated at the same time: "a pivotal moment that underscores the team's commitment" instead of "we shipped it two weeks early." Readers notice, even when they can't name why.

Two things follow from that, and they shape everything in this skill:

1. **The tells are symptoms, not the disease.** Swapping "delve" for "explore" fixes nothing if the sentence still says nothing. The real problems are vagueness, inflation, over-explaining, and template structure. Fix those and most surface tells disappear on their own.
2. **Structure gives AI away more than vocabulary.** Research on AI fiction (StoryScope, 2026) found that scrubbing word-level artifacts barely changed how detectable a story was. What gave it away was the shape: tidy linear plots, themes spelled out, flat escalation, lessons stated at the end. The same is true of emails and posts. A template is a template no matter which words fill it.

## Step 1: Pick the mode

**Draft.** The user wants something written. Write it in a human voice from the first sentence. Output the piece itself, plus at most one short line if you left placeholders. Do not attach a review, scores, or a list of tells you avoided.

**Revise.** The user gives you text to fix, humanize, or tighten. Return the rewrite first. Then add a short note (three to six lines, plain prose) on the main changes, so they can learn the pattern. Preserve every real claim and the user's meaning. Never add ideas, facts, or anecdotes that weren't there.

**Review.** Only when the user asks you to check, score, audit, or explain whether something sounds like AI. Read `references/review.md` for the scoring rubric and report format.

If it's unclear, treat pasted text as Revise and a description of something to write as Draft.

## Step 2: Identify the channel and read its reference

| Writing | Read |
|---|---|
| Email, Slack, Teams, texts | `references/channels.md` (Email, Chat sections) |
| LinkedIn, X, Threads, Instagram, YouTube community posts, captions, bios | `references/channels.md` (Social section) |
| Memos, reports, proposals, briefs, exec summaries, procedures, technical writing | `references/channels.md` (Business and Procedures sections) |
| YouTube scripts, narration, any storytelling, fiction, anecdotes inside posts | `references/storytelling.md` |
| Any Revise or Review job | `references/patterns.md` (the full catalog of tells and their fixes) |

For short drafts, the core rules below are usually enough on their own. For anything the user will publish, read the channel reference.

**Voice profile.** If `references/voice-profile.md` has been filled in, read it every time and follow it. The user's own voice beats the defaults in this skill, except for the honesty rules (never invent facts, never fake experience).

## Step 3: Apply the core rules

These hold in every channel.

**Say the specific thing.** Use names, numbers, dates, the actual tool, the actual decision, the actual consequence. If you can't picture it happening, rewrite it. If you don't have the specific detail, leave a bracketed placeholder like `[the number from the Q3 review]` rather than inventing one. Never make up statistics, quotes, customers, credentials, or personal stories. A placeholder is honest; a fabricated anecdote is a lie in the user's name.

**Follow Orwell's six rules.** They still work:
1. Don't use a figure of speech you're used to seeing in print ("game-changer", "move the needle", "at the end of the day").
2. Don't use a long word where a short one will do ("use" not "utilize", "help" not "facilitate", "start" not "commence").
3. If you can cut a word, cut it.
4. Use the active voice when the actor matters and is known.
5. Use everyday words over jargon, foreign phrases, or scientific-sounding ones, unless precision demands the technical term and the audience knows it.
6. Break any of these rules before writing something awkward or barbarous.

**Use plain verbs.** "Is", "has", "uses", "said", "wrote". Not "serves as", "stands as", "boasts", "features", "leverages", "authored". AI avoids the plain copula; people don't.

**Say it once.** No opening that previews what you're about to say, no closing that summarizes what you said. End when you're done.

**Trust the reader.** Don't tell them what something "highlights", "underscores", or "reflects". Don't state the moral or the lesson; let the facts carry it. If the point needs explaining, the facts weren't specific enough.

**Commit.** State opinions as opinions without throat-clearing ("I'll be honest", "The truth is"). Hedge only where there is real uncertainty, and then say what's uncertain and why.

**Vary rhythm the way speech does.** Mix sentence lengths because the thought calls for it, not on a schedule. A wall of medium sentences is an AI tell. So is a drumbeat of short punchy fragments.

**Punctuation and formatting.** No em dashes by default; use a comma, period, colon, or parentheses instead. (Claude in particular overuses them, more than professional human writers.) Use only the formatting the channel naturally has: no bold sprinkled through emails, no headers in a message, no bullets where one sentence would do, no emoji as bullet points, straight quotes rather than curly ones in plain text.

**Match the register to the relationship.** Write to a colleague the way you'd talk to that colleague. Write for an audience you respect as smart and busy.

## Step 4: Kill the common tells

This is the short list. The full catalog with fixes is in `references/patterns.md`.

**Words.** delve, tapestry, testament, pivotal, crucial, vital, underscore, highlight (as a verb), showcase, foster, cultivate, enhance, elevate, empower, unlock, unleash, leverage, harness, navigate, streamline, robust, seamless, holistic, dynamic, vibrant, intricate, nuanced, multifaceted, comprehensive, landscape, realm, journey, synergy, game-changer, align with, resonate with, boasts, valuable insights, additionally (opening a sentence), moreover, furthermore. One or two can be coincidence. Several together is the tell. Don't swap in a synonym; rewrite the sentence around the concrete fact.

**Sentence shapes.**
- Negative parallelism: "It's not X, it's Y." / "Not just X, but Y." / "Y rather than X." State Y.
- Reflexive triples: three adjectives, three phrases, three parallel clauses. Use the number of items that actually exist.
- The "-ing" tail: a sentence ending in ", highlighting the importance of..." or ", ensuring that...". Cut it or make it its own claim.
- Vague attribution: "experts say", "many believe", "industry reports suggest". Name the source or own the claim.
- Vague association: "is associated with", "in connection with". Say what the relationship is.
- Self-posed question: "The result? Chaos." / "Why does this matter? Because..." Just say it.
- Setup lines: "Here's the thing:", "Here's what most people miss:", "The answer is simple:". Delete them and start with the substance.

**Structure.**
- Intro, three points, conclusion that restates the intro.
- Every paragraph the same length.
- Opening with a generic claim ("In today's fast-paced world...") instead of something specific.
- Closing with a summary, a moral, an upbeat look ahead ("Despite these challenges, the future looks bright"), or a mic-drop one-liner.
- "**Label:** explanation" bullet lists standing in for an argument.

**Chatbot residue.** "Certainly!", "Great question", "I hope this helps", "Let me know if you'd like...", "Here's a breakdown", "Below is...". These belong to a chat with an assistant, never in something the user sends.

## Step 5: Don't overcorrect

Over-scrubbed text has its own sound. Watch for these:

- **Synonym swapping.** Replacing flagged words while keeping the same empty sentence. Rewrite the thought instead.
- **Choppy minimalism.** Every sentence short and declarative. Real writing has some long sentences that carry a chain of reasoning.
- **Fake folksiness.** Sprinkling in "Look,", "Honestly,", "Here's the deal", "kinda", or deliberate typos to seem casual. That's a costume, and readers see it.
- **Banning legitimate tools.** A list of three is fine when there are three things. Passive voice is fine when the actor is unknown or unimportant. A contrast is fine when someone actually holds the wrong view and you're answering them. A heading is fine in a long report. The test is whether the device does work or just decorates.
- **Flattening the user's voice.** If they write long, wry sentences, keep them long and wry. Fix the AI texture, not their personality.

## Step 6: Final pass before output

Run this silently. Don't report it unless asked.

1. Could someone else have written this exact piece without the user's knowledge or experience? If yes, find where the specifics should go or leave placeholders.
2. Does the first sentence say something concrete?
3. Does the last sentence add something, or just restate?
4. Read it as if aloud. Anywhere you'd stumble or sound like a press release?
5. Any word from the Step 4 list? Any em dash?
6. Any sentence that explains the significance of the previous one? Cut it.
7. Is the formatting what this channel actually uses?
8. Is every fact real or clearly marked as a placeholder?

For pieces over about 300 words, you can also run `python scripts/tell_scan.py <file>` to catch mechanical tells (flagged vocabulary, em dashes, repeated sentence openers, uniform sentence length). It's a backstop for the things that are easy to miss, not a substitute for reading the piece.

## Sources

This skill merges: George Orwell's "Politics and the English Language" (1946) and ASD-STE100 Simplified Technical English; Wikipedia's "Signs of AI writing" field guide (WikiProject AI Cleanup); a channel-aware humanizer pattern list for blogs, LinkedIn, email, and Slack; and Russell et al., "StoryScope: Investigating idiosyncrasies in AI fiction" (arXiv 2604.03136, 2026).
