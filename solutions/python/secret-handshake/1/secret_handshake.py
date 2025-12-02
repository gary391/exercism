CHECK_SHEET = {
    "00001": "wink",
    "00010": "double blink",
    "00100": "close your eyes",
    "01000": "jump",
    "10000": "Reverse",
}


def commands(binary_str):
    moves = []
    reverse = False
    for index, item in enumerate(reversed(binary_str)):
        if item == "1":
            # bit shifting and b (binary), 5 (at least 5 characters wide) and 0" → pad with leading zeros if shorter) 
            print(format(1 << index, "05b"))
            if CHECK_SHEET[format(1 << index, "05b")] == "Reverse":
                reverse = True
                continue
            moves.append(CHECK_SHEET[format(1 << index, "05b")])
    if reverse:
        moves = moves[::-1]
    return moves