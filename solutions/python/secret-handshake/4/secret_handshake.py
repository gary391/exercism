ACTIONS = ["wink", "double blink", "close your eyes", "jump", "reverse"]

def commands(binary_str):
    value = int(binary_str, 2)
    print(value)
    moves = [ACTIONS[index] for index, action in enumerate(ACTIONS) if value & (1 << index)]
    if value & (1 << 4):
    # if 'reverse' in moves:
        moves = moves[-2::-1]
    return moves
print(commands("11111"))