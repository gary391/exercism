KILO_OHMS = 1000
MEGA_OHMS = 1000000
GIGA_OHMS = 1000000000


COLOR_TO_VALUE = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def label(colors):
    resistor = ""
    last_value = COLOR_TO_VALUE.index(colors[2:3][0])
    for color in colors[:2]:
        resistor += str(COLOR_TO_VALUE.index(color))
    value = int(resistor) * 10**last_value
    if value >= GIGA_OHMS:
        return f"{value // 1000000000} gigaohms"
    elif value >= MEGA_OHMS:
        return f"{value // 1000000} megaohms"
    elif value >= KILO_OHMS:
        return f"{value // 1000} kiloohms"
    return f"{value} ohms"
