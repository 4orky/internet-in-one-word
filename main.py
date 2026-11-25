# The Internet in One Word — make.fun bounty
# u-ronigrv-the-internet-in-one-word-e388f33b
#
# The program writes one word to /output/entry.txt: the single word that
# best describes the whole internet. The judge compares entries two at a
# time, weighing, most important first:
#   1. a single word that describes the whole internet
#   2. funny by itself, no explanation needed
#   3. true about the internet as a whole, not one app, site or mood
#   4. surprising: not the first obvious word anyone reaches for
#   5. lands in one beat: spelled correctly, instantly readable, short
#
# Candidates were hand-drafted against that brief and scored 0-10 on
# criteria 2-5 (criterion 1 is a pass/fail: every candidate is one word).
# Selection is deterministic: highest total wins, ties go to the shorter
# word. The output is byte-identical on every run.

CANDIDATES = [
    # REVISION (second pass, re-reading the judge's brief): criterion 3
    # demands the word say something true about the internet AS A WHOLE.
    # "feral" fails that specificity: a feral cat, a feral child, a feral
    # garden are all feral too — it names wildness in general, not the
    # internet. Its "true" score drops 8 -> 6 (total 34 -> 32), so the
    # winner flips to "enshittification": a word invented specifically
    # about the internet's decay, which beats "feral" on truth (10 vs 6)
    # and surprise (9 vs 8) by more than "feral" wins on brevity
    # (10 vs 6) — exactly the judge's own tiebreak rule ("a later one
    # differs by much more").
    # funny 8, true 6, surprise 8, lands 10 = 32
    ("feral", 8, 6, 8, 10),
    # funny 8, true 10, surprise 9, lands 6 = 33
    # A real word (American Dialect Society 2023 Word of the Year) coined
    # for exactly this: platforms decaying as they squeeze users. Long
    # (16 letters) costs it on "lands in one beat".
    ("enshittification", 8, 10, 9, 6),
    # funny 7, true 8, surprise 7, lands 9 = 31
    ("unhinged", 7, 8, 7, 9),
    # funny 8, true 8, surprise 5, lands 9 = 30
    # Very internet, but the most obvious meme word of the last two years.
    ("brainrot", 8, 8, 5, 9),
    # funny 5, true 6, surprise 8, lands 10 = 29
    ("lore", 5, 6, 8, 10),
    # funny 6, true 5, surprise 6, lands 10 = 27
    ("404", 6, 5, 6, 10),
    # funny 7, true 8, surprise 5, lands 6 = 26
    ("procrastination", 7, 8, 5, 6),
    # funny 4, true 6, surprise 6, lands 10 = 26
    ("loading", 4, 6, 6, 10),
    # funny 5, true 6, surprise 6, lands 7 = 24
    ("echochamber", 5, 6, 6, 7),
    # funny 5, true 7, surprise 4, lands 7 = 23
    ("doomscrolling", 5, 7, 4, 7),
    # funny 4, true 7, surprise 4, lands 8 = 23
    ("distraction", 4, 7, 4, 8),
    # funny 5, true 6, surprise 3, lands 8 = 22
    ("clickbait", 5, 6, 3, 8),
    # funny 5, true 6, surprise 2, lands 9 = 22
    ("memes", 5, 6, 2, 9),
    # funny 5, true 5, surprise 3, lands 9 = 22
    ("trolls", 5, 5, 3, 9),
    # funny 3, true 7, surprise 5, lands 7 = 22
    ("algorithm", 3, 7, 5, 7),
]


def pick(candidates):
    best = None
    for word, funny, true, surprise, lands in candidates:
        assert 1 <= len(word) <= 30, f"candidate over gate: {word!r}"
        assert word.strip(), "candidate is blank"
        assert " " not in word, f"candidate is not one word: {word!r}"
        score = funny + true + surprise + lands
        key = (score, -len(word))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, word)
    return best[1]


def main():
    word = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
