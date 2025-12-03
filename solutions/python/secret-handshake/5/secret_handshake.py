ACTIONS = ["wink", "double blink", "close your eyes", "jump", "reverse"]


def commands(binary_str):
    value = int(binary_str, 2)
    moves = [action for index, action in enumerate(ACTIONS) if value & (1 << index)]
    if value & (1 << 4):
        moves = moves[-2::-1]
    return moves