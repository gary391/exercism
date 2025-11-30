RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def value(colors):
    resistor = ""
    for color in colors[:2]:
        resistor += str(RESISTOR_COLORS.index(color))
    return int(resistor)
