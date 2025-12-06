PIECES = [
    ("the house that Jack built", None),
    ("the malt", "that lay in"),
    ("the rat", "that ate"),
    ("the cat", "that killed"),
    ("the dog", "that worried"),
    ("the cow with the crumpled horn", "that tossed"),
    ("the maiden all forlorn", "that milked"),
    ("the man all tattered and torn", "that kissed"),
    ("the priest all shaven and shorn", "that married"),
    ("the rooster that crowed in the morn", "that woke"),
    ("the farmer sowing his corn", "that kept"),
    ("the horse and the hound and the horn", "that belonged to"),
]


def build_verse(n):
    idx = n - 1
    initial_line = [f"This is {PIECES[idx][0]}"]
    middle_line = [
        f" {PIECES[i][1]} {PIECES[i-1][0]}"
        for i in range(idx, 0, -1)
    ]
    return "".join(initial_line + middle_line) + "."


def recite(start_verse, end_verse):
    return [build_verse(v) for v in range(start_verse, end_verse+1)]
    
