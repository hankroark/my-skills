#!/usr/bin/env python3
"""Scan text for mechanical AI-writing tells.

Usage:
    python tell_scan.py draft.txt
    cat draft.txt | python tell_scan.py -

Catches the easy-to-miss surface patterns: flagged vocabulary, stock phrases,
em dashes, repeated sentence openers, uniform sentence and paragraph length,
and chatbot residue. It cannot judge vagueness, structure, or whether the
content is specific, so always read the piece yourself as well.
"""
import re
import statistics
import sys

WORDS = [
    "delve", "delves", "delving", "tapestry", "testament", "pivotal", "crucial",
    "vital", "intricate", "intricacies", "interplay", "meticulous", "meticulously",
    "underscore", "underscores", "underscored", "underscoring", "highlighting",
    "showcase", "showcases", "showcasing", "foster", "fosters", "fostering",
    "cultivate", "cultivating", "garner", "garnered", "bolster", "bolstered",
    "enhance", "enhances", "enhancing", "elevate", "elevates", "elevating",
    "empower", "empowers", "empowering", "enduring", "vibrant", "realm",
    "multifaceted", "nuanced", "comprehensive", "holistic", "robust", "seamless",
    "seamlessly", "dynamic", "transformative", "synergy", "harness", "harnessing",
    "unlock", "unlocks", "unlocking", "unleash", "leverage", "leverages",
    "leveraging", "streamline", "streamlines", "streamlining", "utilize",
    "utilizes", "utilizing", "facilitate", "facilitates", "facilitating",
    "boasts", "game-changer", "game-changing", "cutting-edge", "world-class",
    "best-in-class", "groundbreaking", "renowned", "nestled", "additionally",
    "moreover", "furthermore", "notably", "essentially", "certainly",
]

PHRASES = [
    "in today's", "ever-evolving", "when it comes to", "at the end of the day",
    "it's important to note", "it is important to note", "it's worth noting",
    "it goes without saying", "here's the thing", "here's the kicker",
    "here's what most people", "here's why", "here's a breakdown", "below is",
    "the truth is", "i'll be honest", "and honestly?", "let that sink in",
    "read that again", "a testament to", "plays a crucial role",
    "plays a pivotal role", "plays a key role", "serves as", "stands as",
    "align with", "aligns with", "resonate with", "resonates with",
    "valuable insights", "actionable insights", "move the needle",
    "low-hanging fruit", "best practices", "thought leader", "deep dive",
    "circle back", "touch base", "reach out", "i hope this email finds you",
    "i hope this finds you", "please don't hesitate", "i look forward to hearing",
    "i wanted to reach out", "just wanted to", "per our", "as per my",
    "at your earliest convenience", "in conclusion", "in summary",
    "despite these challenges", "the future looks bright", "excited for what's next",
    "not only", "it's not about", "it isn't about", "rather than",
    "in this video", "welcome back to the channel", "dive deep", "dive into",
    "let's dive", "certainly!", "great question", "i hope this helps",
    "let me know if you", "would you like me to", "feel free to",
]

RESIDUE = re.compile(r"\[(your|insert|company|name|date)[^\]]*\]", re.I)


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if len(p.strip().split()) >= 2]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    low = text.lower()
    findings = []

    em = text.count("\u2014")
    if em:
        findings.append(f"Em dashes: {em}. Replace with comma, period, colon, or parentheses.")

    hits = {}
    for w in WORDS:
        n = len(re.findall(rf"\b{re.escape(w)}\b", low))
        if n:
            hits[w] = n
    if hits:
        listed = ", ".join(f"{k} x{v}" if v > 1 else k for k, v in sorted(hits.items()))
        findings.append(f"Flagged vocabulary ({sum(hits.values())}): {listed}")

    ph = [p for p in PHRASES if p in low]
    if ph:
        findings.append("Stock phrases: " + "; ".join(f'"{p}"' for p in ph))

    sents = sentences(text)
    firsts = [re.sub(r"[^a-z']", "", s.split()[0].lower()) for s in sents]
    runs = []
    for i in range(1, len(firsts)):
        if firsts[i] and firsts[i] == firsts[i - 1]:
            runs.append(f'"{firsts[i]}" (sentences {i} and {i + 1})')
    if runs:
        findings.append("Back-to-back sentences with the same first word: " + ", ".join(runs[:8]))

    if len(sents) >= 6:
        lens = [len(s.split()) for s in sents]
        mean = statistics.mean(lens)
        sd = statistics.pstdev(lens)
        cv = sd / mean if mean else 0
        note = f"Sentences: {len(sents)}, mean {mean:.1f} words, spread (CV) {cv:.2f}."
        if cv < 0.35:
            note += " Low variation; the rhythm may feel uniform."
        findings.append(note)
        long_ones = [i + 1 for i, n in enumerate(lens) if n > 30]
        if long_ones:
            findings.append(f"Sentences over 30 words: {long_ones}. Check they read easily.")

    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    if len(paras) >= 4:
        plens = [len(p.split()) for p in paras]
        pm = statistics.mean(plens)
        pcv = statistics.pstdev(plens) / pm if pm else 0
        if pcv < 0.25:
            findings.append(f"Paragraphs are very uniform in length (CV {pcv:.2f}).")
        one_liners = sum(1 for p in paras if len(sentences(p)) <= 1)
        if one_liners / len(paras) > 0.7 and len(paras) >= 6:
            findings.append("Most paragraphs are a single line (LinkedIn ghostwriter format).")

    exclaims = text.count("!")
    if exclaims >= 3:
        findings.append(f"Exclamation points: {exclaims}.")

    bold = len(re.findall(r"\*\*[^*]+\*\*", text))
    if bold >= 3:
        findings.append(f"Bold spans: {bold}. Check the channel actually uses bold.")
    if re.search(r"^\s*[-*]\s+\*\*[^*]+:\*\*", text, re.M):
        findings.append('"**Label:** description" bullet list detected.')
    if "\u2192" in text:
        findings.append("Arrow characters found; consider writing the sequence as a sentence.")
    curly = sum(text.count(c) for c in "\u201c\u201d\u2018\u2019")
    if curly:
        findings.append(f"Curly quotes/apostrophes: {curly} (fine in documents, odd in plain text).")
    res = RESIDUE.findall(text)
    if res:
        findings.append("Template placeholders present; confirm they're intentional.")

    words = len(text.split())
    print(f"Scanned {words} words.")
    if not findings:
        print("No mechanical tells found. Still read it for vagueness and structure.")
    for f in findings:
        print("- " + f)


if __name__ == "__main__":
    main()
