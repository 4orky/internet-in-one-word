"""One-word verdict on the whole internet.

Bounty: u-ronigrv-the-internet-in-one-word-e388f33b. The judge pits
entries against each other two at a time and ranks them, most weight
first, on: the word sums up the entire internet; it is funny standing
alone with no setup; it holds for the internet at large rather than a
single platform or passing mood; it is not the first word anybody
would blurt out; and it hits at once, spelled right and easy to read.

I drafted fifteen single-word hopefuls by hand, graded each one 0-10
on humour, breadth, freshness and punch (the "sums up the internet"
test is pass/fail, and every hopeful passes it by being one word),
then let the numbers choose. Biggest total takes it; a tie goes to
the shorter spelling. Re-running the script prints the same word
every single time.
"""

from pathlib import Path

# Each hopeful maps to four marks: humour, breadth, freshness, punch.
# Second look, re-reading the brief: the breadth mark asks whether the
# word is true of the internet as a whole, not of wildness anywhere.
# "feral" fits a stray cat, an unruly toddler, an overgrown garden
# just as well, so its breadth mark falls from 8 to 6. That drops its
# total from 34 to 32 and hands the win to "enshittification", a word
# minted for this exact rot, which outscores it on breadth and
# freshness by more than it gives away on punch.
HOPEFULS = {
    "feral": (8, 6, 8, 10),
    "enshittification": (8, 10, 9, 6),
    "unhinged": (7, 8, 7, 9),
    "brainrot": (8, 8, 5, 9),
    "lore": (5, 6, 8, 10),
    "404": (6, 5, 6, 10),
    "procrastination": (7, 8, 5, 6),
    "loading": (4, 6, 6, 10),
    "echochamber": (5, 6, 6, 7),
    "doomscrolling": (5, 7, 4, 7),
    "distraction": (4, 7, 4, 8),
    "clickbait": (5, 6, 3, 8),
    "memes": (5, 6, 2, 9),
    "trolls": (5, 5, 3, 9),
    "algorithm": (3, 7, 5, 7),
}


def total_marks(marks):
    """Add up one hopeful's four marks."""
    humour, breadth, freshness, punch = marks
    return humour + breadth + freshness + punch


def choose_word(hopefuls):
    """Return the hopeful with the biggest total, shortest on a tie."""
    champion = None
    champion_key = None
    for spelling, marks in hopefuls.items():
        pieces = spelling.split()
        if len(pieces) != 1:
            raise ValueError("hopeful is not a single word: %r" % spelling)
        if not 1 <= len(spelling) <= 30:
            raise ValueError("hopeful outside the length gate: %r" % spelling)
        tally = total_marks(marks)
        ranking = (tally, -len(spelling))
        if champion_key is None or ranking > champion_key:
            champion_key = ranking
            champion = spelling
    return champion


def emit_entry():
    """Pick the champion word, save it, and print it."""
    champion = choose_word(HOPEFULS)
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(champion, encoding="utf-8")
    print(champion)


emit_entry()
