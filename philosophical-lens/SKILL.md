---
name: philosophical-lens
description: Apply a philosopher's reasoning framework (Socrates, Aristotle, Descartes, Kant, Hume, Hegel, Plato) to analyze a problem or question the user, picking the lens that fits the task.
---

# Philosophical Lens

Adapted from Harb et al., "The Ballad of LLM Agents: Philosophical Reasoning for Chemistry" (Argonne National Laboratory, 2026) and the system prompts at github.com/HassanHarb92/Sci_reasoning_LLMs. In that study, a structured philosophical reasoning framework improved accuracy on hard chemistry problems, but no single framework won everywhere. The right lens depended on the kind of problem and on the model. This skill applies the same design to non-scientific work: business and strategy decisions, technology and governance questions, and creative practice.

Treat the transfer as a working hypothesis. The study measured numeric chemistry answers. Here the payoff is clearer framing, exposed assumptions, honest uncertainty, and better decisions.

## When to use

- The user says "use a philosophical lens", "think about this like a philosopher", "run Kant on this", "Hume this", "Socratic questions", or names any lens below.
- The user asks Claude to question them, interrogate their thinking, or help them find what they actually think.
- The user explicitly invokes /philosophical-lens.

Do not apply it uninvited to ordinary requests.

## Two modes

### Work mode
Triggered by "use a lens to work this", "analyze this through X", or material plus a request for analysis. Claude does the reasoning and delivers the output structure below.

### Question mode
Triggered by "ask me questions", "interrogate this", "help me figure out what I think". Also the default when the substance lives mainly in the user's head (the intent behind a creative project, a stance going into a negotiation, a half-formed strategy).

Rules for question mode:
- Open with one line naming the lens and why, then the first question.
- Ask one sharp question per turn by default. Ask up to three only when they are tightly linked and the topic is analytical.
- Build each next question from the user's answer: test the answer against a case or consequence (elenchus), check it against earlier answers for contradiction, narrow vague terms.
- Do not answer for the user and do not lecture between questions. At most one sentence reflecting back what the answer established.
- Switch lenses when answers reveal a different demand (for example, a definitional question turns out to be an evidence question). Say so in one line.
- About every five exchanges, or when the user asks where things stand, give a short "Established / Still open" summary.
- Finish with the synthesis section from the output structure when the user asks, or when the core question has a clear answer.

If the mode is ambiguous, use work mode when the user supplied material, question mode when the user supplied only a topic.

## Choosing the lens

Follow the study's selection flow:

1. **Start Socratic when the problem itself is unclear.** If the user cannot yet state the question crisply, or key terms are doing too much work, use Socratic moves first to expose the problem's structure.
2. **Identify the dominant demand and pick a lead lens** from the table.
3. **Add at most one supporting lens** when the problem has a second clear demand. Two lenses is the usual ceiling; three only for large, multi-part problems.
4. **Depth check after the analysis.** Ask: did this surface something the user did not already have? Does the conclusion rest on an unexamined premise? If the answer is shallow, loop back: apply Socratic questioning to the weakest premise, or switch lenses.

| Dominant demand | Lead lens | Common pairing |
|---|---|---|
| Problem is fuzzy; terms are vague; confident claim never tested | Socrates | any |
| Big messy plan, roadmap, migration, consolidation, sequencing, cost or sizing model, troubleshooting | Descartes | Hume |
| Governance, policy, standards, guardrails, decision rights, principles, ethics, evaluation criteria | Kant | Hume |
| Is this working? Vendor claims, pilot results, metrics, adoption data, postmortems, causal claims | Hume | Kant or Descartes |
| What is this thing really? Taxonomy, positioning, purpose, the right balance between extremes | Aristotle | Plato or Kant |
| Two legitimate goods in conflict; stakeholder disagreement; central vs federated; speed vs control | Hegel | Kant |
| Vision, north star, principles, artistic intent, what a body of work is about | Plato | Descartes or Hume to bring it back to earth |

Honor an explicit lens choice from the user. If the chosen lens looks poorly suited, still use it and note in one line which lens might add something.

Hegel and Plato were the weakest lenses in the study, which measured precise numeric answers. In this skill, use them for tension and vision, never as the lead lens for a problem that needs a precise answer (a cost model, a capacity estimate, a schedule).

## Output structure (work mode)

1. **Lens.** Which lens or lenses, and why, in one or two lines.
2. **Reframed question.** Rewrite the user's question in the lens's terms, making explicit what must be defined, decomposed, evidenced, constrained, or reconciled.
3. **Three questions that matter.** The three questions the lens says carry the most weight. For each, give Claude's working answer and label it as Given or Assumed, so the user can see which ones to check.
4. **Analysis.** Ordered steps using the lens's moves. Label claims where it matters:
   - **Given**: stated by the user or in the material.
   - **Assumed**: a premise Claude supplied.
   - **Inferred**: a conclusion drawn from the above.
   - **Value judgment**: where an "ought" or a preference enters.
5. **Synthesis.** The conclusion in plain language, a stated confidence level, what evidence or event would change the conclusion, and one concrete next step.

Scale to the request. A quick ask gets: lens line, reframe, three to five analysis bullets, two-line synthesis. Do not pad.

## Style rules

- Plain language first. Put the philosophical term in parentheses at most. Every principle used must change the analysis; if it does not, leave it out. Name-dropping is decoration.
- Name the specific thing being analyzed ("the tool consolidation", "the cost guardrail policy", "the third image in the series") instead of vague pronouns like "it" or "they".
- Do not roleplay the philosopher or use an archaic voice. The lens is a method, not a costume.
- Disagree with the user when the lens shows a weak premise. Say where the reasoning breaks.
- Match the user's expertise. Skip fundamentals the user clearly already knows.

## The lenses

### Socrates: dialectical inquiry
Use when the problem is unclear, a claim is confident but untested, or a question-mode session is starting.

Moves:
- **Definition:** "What exactly do we mean by X here?" ("adoption", "governed", "done", "a finished piece")
- **Cross-examination (elenchus):** take a claim and find a case or consequence that contradicts it.
- **Assumption surfacing:** "What has to be true for this to hold?"
- **Hypothesis elimination:** list candidate explanations and rule them out with what is known.
- **Counterfactual:** "If we did nothing, what would actually happen?"
- **Analogy:** compare to a known case, then find exactly where the analogy breaks.
- **Drawing it out (maieutics):** the user's own knowledge is the source; questions extract it.
- **Generalize and test:** from examples to a rule, then test the rule on a new case.

### Aristotle: categories, causes, the mean
Use to pin down what something is, why it exists, and the right balance.

Moves:
- **Genus and difference:** what class does X belong to, and what distinguishes X from others in that class? ("Is this a product, a service, or a mandate?")
- **Category check:** is X a thing, a quantity, a quality, or a relation? Catch category errors, such as treating customer experience as a feature to ship rather than a relation between customers and the product.
- **Four causes:** material (what it is made of: people, budget, tools; light, subject, medium), formal (its structure: architecture, org design; composition), efficient (what actually produces change: a funding decision, an incentive, a specific edit), final (the purpose it serves: the business outcome; the intent of the work).
- **Potential and actual:** what is latent, and what condition turns it real?
- **Essence and accident:** which features define identity, and which can change without changing what the thing is?
- **Reputable opinion (endoxa):** start from industry consensus or expert views, test it, keep what survives.
- **The mean:** the right point between two failure extremes (governance too loose vs too heavy; an edit too flat vs overcooked), defined by concrete criteria.

### Descartes: doubt, decompose, rebuild
Use for plans, roadmaps, migrations, consolidations, cost and sizing models, and troubleshooting.

Moves:
- **Methodic doubt:** which parts rest only on authority or habit? Which stand on evidence?
- **Term hygiene:** separate the different meanings of a loaded word ("cost", "platform", "quality") and label each.
- **Decompose:** break the problem into the smallest parts that can each be understood.
- **Simple to complex:** order the parts so each builds on what is already solid.
- **Foundations:** name the few core principles that the rest of the rules should follow from; flag rules that conflict with them.
- **Deductive chain:** premises, steps, conclusion, laid out so the weakest link is visible.
- **Model it:** a table, matrix, simple equation, or diagram that makes relations explicit.
- **Review:** enumerate every step and check for omissions and hidden assumptions.

### Kant: conditions, constraints, frameworks
Use for governance, policy, standards, guardrails, decision rights, principles, and evaluation frameworks.

Moves:
- **Conditions of possibility:** what must already be in place for this to work, or to be measurable at all? (For a chargeback model to be fair, what must be true of cost attribution?)
- **Defining rules vs guiding ideals (constitutive vs regulative):** which rules make the thing what it is, and which only guide behavior? A common governance failure is enforcing an aspiration as a hard control, or treating a hard control as optional guidance.
- **Universalizability:** could this rule hold if every team and every case applied it? Find exceptions that would destroy the rule if generalized.
- **Ends, not merely means:** does the policy treat a team or person only as a means to someone else's metric?
- **Objectivity as invariance:** what holds across stakeholder perspectives (security, finance, users, leadership)? That invariant core is the defensible part.
- **Framework awareness:** a framework (a management method, an industry standard, a regulatory regime) shapes what is visible. Compare frameworks by shared criteria, not preference.
- **Limits of a claim:** can this metric or evidence actually answer this question?
- **Constraint satisfaction:** which constraints eliminated which options, and what violation would force a revision?

### Hume: evidence, causation, honest uncertainty
Use for vendor claims, pilot results, metrics, adoption data, postmortems, and any "X caused Y" or "this will work" claim.

Moves:
- **Trace to observation:** what was actually seen or measured? Strip anything not tied to an observation.
- **Definition vs fact:** separate what is true by definition or arithmetic from what is true about the world.
- **Pattern, not necessity:** a causal claim is a repeated pattern plus background assumptions. Name both.
- **Rival causes:** third variables, reversed causation, selection effects, timing coincidences.
- **Induction check:** it worked before; what is different this time?
- **Degrees of belief:** proportion confidence to evidence and state it.
- **Is vs ought:** moving from data ("teams use X") to a norm ("we should standardize on X") requires a stated value premise.
- **Act anyway (mitigated skepticism):** decide at the confidence the evidence warrants, and name what would trigger a revisit.

### Hegel: tension and synthesis
Use when two legitimate goods conflict. Not for precise answers.

Moves:
- **Strongest versions:** state each position (thesis, antithesis) at its most defensible.
- **What each protects:** identify the legitimate interest under each position.
- **Synthesis that lifts (sublation):** a resolution that keeps the legitimate core of both and moves to a new level. Not a split-the-difference compromise.
- **Development over time:** today's synthesis becomes tomorrow's position; anticipate the next tension.
- **Mutual dependence:** show how each side's position depends on the other's existence.

### Plato: ideal form and vision
Use for vision, principles, mission, and artistic intent. Pair with Descartes or Hume to return to the concrete.

Moves:
- **Ascend to the form:** describe the ideal version, abstracted from today's constraints.
- **Measure the gap:** compare actual to ideal; separate essential gaps from incidental ones.
- **Shadows on the wall:** what proxy is being mistaken for the real thing (ticket counts for outcomes, engagement for quality)?
- **The good it serves:** name the value the ideal is oriented toward.
- **Dialogue:** follow-up questions that refine the form.

## Domain pairings

### Technology, product, and governance
- Tool or platform consolidation: Descartes to decompose, Hegel for standardization vs team autonomy.
- Retiring a tool people depend on: Hegel for what each side protects, Kant to test whether the decision and the process each hold up.
- New governance policy or guardrail: Kant for universalizability and defining vs guiding rules, Hume for whether the policy will change behavior.
- Tool or vendor evaluation: Hume for the evidence behind claims, Kant for the conditions the tool needs to succeed, or Aristotle for what category of thing is being bought.
- Product vision or strategy narrative: Plato for the north star, Aristotle for the final cause.
- Communicating to a leader from a different background: Socratic definitions first, Aristotle to categorize the ask in that leader's terms.

### General business
- Negotiation or disagreement prep: Hegel, then Socratic questions to test the synthesis.
- Business case: Descartes for structure, Hume for the evidence.
- Org design: Aristotle's four causes.

### Creative work (photography, art, writing, design)
- Critique of a piece: Hume (what is actually on the page or in the frame vs what the creator knows about it), Aristotle's four causes.
- Series or project intent: Plato with Socratic questions; question mode works well.
- A piece that is not working: Descartes, isolating one element or adjustment at a time.
- Tension within a piece or body of work: Hegel.

## Examples

**"Use a philosophical lens on whether to add an LLM gateway to our AI cost governance tooling."**
Lead Kant, support Hume. Kant: what conditions must exist for cost controls to be enforceable (identity, routing all model traffic through one gateway)? Which proposed controls are defining rules vs guiding ideals? Hume: what evidence supports the claimed savings, and what rival explanations could account for a pilot's results?

**"Ask me questions like a philosopher about my photo series."**
Question mode, Socrates aiming at Plato's ideal form. First turn: "Lens: Socratic, working toward what the series is about. First question: when you look at the three strongest images in the series, what do those three share that the weaker images lack?"

**"Descartes this: skin tones look off in this edit."**
Decompose into capture (white balance, light source), global adjustments, local adjustments, and output profile. Test one variable at a time in that order, and name the step whose reversal removes the problem.
