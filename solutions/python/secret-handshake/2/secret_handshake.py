CHECK_SHEET = {
    "00001": "wink",
    "00010": "double blink",
    "00100": "close your eyes",
    "01000": "jump",
    "10000": "Reverse",
}


def commands(binary_str):
    moves = [
        CHECK_SHEET[f"{(1 << index):05b}"]
        for index, item in enumerate(reversed(binary_str))
        if item == "1"
    ]
    if 'Reverse' in moves:
        moves.pop()
        moves.reverse()
    return moves