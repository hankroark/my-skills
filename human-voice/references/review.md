# Review Mode

Use this only when the user asks you to check, score, audit, or judge whether text sounds like AI. For plain "fix this" requests, use Revise mode instead (rewrite plus a short note on changes).

## Framing

These are signs, not proof. People write every one of these patterns sometimes, and AI detection tools are unreliable. Never say "this was written by AI." Say what patterns are present and how dense they are: "light, two isolated tells" versus "heavy, puffery and template structure throughout." If the user wrote it themselves, focus on what makes it read as generic, not on accusation.

## Steps

1. **Identify the channel** (email, chat, social, business doc, procedure, script/story) and state it in one line. If unclear, say your guess and invite correction.
2. **Scan for tells** using `patterns.md` plus the channel section of `channels.md` (or `storytelling.md` for scripts and stories). Quote each instance exactly.
3. **Check originality.** Could anyone with a search engine have written this? Is there any firsthand evidence: a story, number, decision, or mistake only the author would know?
4. **Score** on the four dimensions for the channel (below), with one line of justification each.
5. **Name the top three changes** that would help most, in priority order.
6. **Rewrite**, following the Revise rules in SKILL.md (preserve every real claim, add no new facts, placeholders where specifics are missing).

## Scoring (1 to 10)

| Channel | Dimensions (target) |
|---|---|
| Social posts, blogs, articles | AI-likeness (1–3, lower is better), Authenticity (8–10), Reader value (7–10), Credibility: needs real experience to write (7–10) |
| Email | AI-likeness (1–3), Authenticity (8–10), Clarity of purpose and ask (8–10), Tone fit for the relationship (8–10) |
| Chat | AI-likeness (1–2), Naturalness (8–10), Clarity (8–10), Brevity (8–10) |
| Business docs and procedures | AI-likeness (1–3), Clarity (8–10), Specificity: numbers, owners, dates (8–10), Decision-readiness (8–10) |
| Scripts and stories | AI-likeness (1–3), Voice: sounds like this speaker (8–10), Narrative shape: escalation, non-obvious structure, unstated theme (7–10), Ear-readiness (8–10) |

If AI-likeness is low but credibility, clarity, or specificity is also low, say so directly: the text is clean but hollow. Removing tells from empty content doesn't fix it.

## Report format

Keep it tight. Prose for the assessment; a short table for scores; quoted flags grouped by type.

```
**Detected as:** [channel]

[Two or three sentences: what works, what the biggest problem is, and how dense the AI patterns are.]

| Dimension | Score | Why |
|---|---|---|
| ... | x/10 | one line |

**Flags**
[Grouped by type: content, vocabulary, sentence shapes, structure, channel-specific. Each with the exact quote and a one-line fix.]

**Top three changes**
1. ...
2. ...
3. ...

**Rewrite**
[full rewrite]
```

End with one line: the rewrite is a starting point, and the user's own edits on top of it usually make the best version.
