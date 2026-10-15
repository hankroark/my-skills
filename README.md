# my-skills

Skills I use with Claude for writing, presentations, and thinking through problems. Each folder is one skill: a `SKILL.md` file with instructions, plus optional reference files and scripts that the skill loads when it needs them.

## The skills

| Skill | What it does |
|---|---|
| [human-voice](human-voice/) | Writes and revises emails, chat messages, posts, documents, and video scripts so they read like a specific person wrote them, not an AI. Includes a catalog of common AI tells, channel-specific guidance, a fill-in voice profile, and a small Python script that scans a draft for mechanical tells. |
| [philosophical-lens](philosophical-lens/) | Analyzes a problem through one or two philosophers' reasoning methods (Socrates, Aristotle, Descartes, Kant, Hume, Hegel, Plato), picked to fit the problem. Can do the analysis itself or question you until you work out what you think. |
| [mckinsey-problem-solving](mckinsey-problem-solving/) | Turns a messy business problem into a structured brief: executive summary, situation/complication/question, a MECE issue tree, three recommendations, and an implementation plan with risks. |
| [prfaq-builder](prfaq-builder/) | Coaches you through an Amazon-style Working Backwards PR/FAQ (a press release and FAQ written before anything is built), teaching the method as it goes. Can also review an existing draft. |
| [slide-craft](slide-craft/) | Plans the content and structure of a deck before anyone builds slides: action titles, one idea per slide, and the right framework for the situation (SCQA, BLUF, ORDER for bad news, SBAR for escalations, decision memos, status updates, change announcements). Produces a Markdown storyboard for a slide-building skill to render. Also audits existing decks. |
| [winston-presentation](winston-presentation/) | Builds decks using Patrick Winston's "How to Speak" framework (empowerment promise, vision, proof, contributions, no "thank you" slide). Supports decks you present live, decks that must stand on their own, or both. Outputs PowerPoint, HTML, or a Markdown outline. |

slide-craft handles what a deck says, and winston-presentation handles a speaker-first style of deck. Neither one sets brand colors, fonts, or templates; pair them with whatever slide-building skill you use for that.

## Installing

- **Claude Code:** copy a skill's folder into `~/.claude/skills/` (for all projects) or into `.claude/skills/` inside a project.
- **Claude apps:** zip a skill's folder and upload it in the Skills section of Claude's settings.

## Sources and credits

These skills build on other people's work:

- **human-voice:** George Orwell, "Politics and the English Language" (1946); ASD-STE100 Simplified Technical English; Wikipedia's "Signs of AI writing" guide (WikiProject AI Cleanup); Russell et al., "StoryScope: Investigating idiosyncrasies in AI fiction" (2026).
- **philosophical-lens:** adapted from Harb et al., "The Ballad of LLM Agents: Philosophical Reasoning for Chemistry" (Argonne National Laboratory, 2026) and the prompts at [github.com/HassanHarb92/Sci_reasoning_LLMs](https://github.com/HassanHarb92/Sci_reasoning_LLMs).
- **mckinsey-problem-solving** and **slide-craft:** Barbara Minto's Pyramid Principle and SCQA; slide-craft also draws on Nancy Duarte and Garr Reynolds. The executive frameworks in slide-craft name their own sources where known.
- **prfaq-builder:** Amazon's Working Backwards PR/FAQ method.
- **winston-presentation:** Patrick Winston's MIT lecture "How to Speak."

None of these skills is affiliated with or endorsed by the people or organizations named above. All examples in the skills (companies, products, people, and numbers) are made up.
