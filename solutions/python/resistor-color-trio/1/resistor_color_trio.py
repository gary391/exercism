def label(colors):

    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    kilo_ohms = 1000
    mega_ohms = 1000000
    giga_ohms = 1000000000
    last_digits = color_map[colors[2:3][0]]
    resistor = ""
    for color in colors[:2]:
        if color in color_map:
            resistor += str(color_map[color])
    value = int(resistor) * 10**last_digits
    if value >= giga_ohms:
        return f"{value // 1000000000} gigaohms"
    elif value >= mega_ohms:
        return f"{value // 1000000} megaohms"
    elif value >= kilo_ohms:
        return f"{value // 1000} kiloohms"
    return f"{value} ohms"