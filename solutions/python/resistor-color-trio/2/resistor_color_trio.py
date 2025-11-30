kilo_ohms = 1000
mega_ohms = 1000000
giga_ohms = 1000000000

color_to_value = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    resistor = ""
    last_value = color_to_value.index(colors[2:3][0])
    for color in colors[:2]:
        resistor += str(color_to_value.index(color))
    value = int(resistor) * 10**last_value
    if value >= giga_ohms:
        return f"{value // 1000000000} gigaohms"
    elif value >= mega_ohms:
        return f"{value // 1000000} megaohms"
    elif value >= kilo_ohms:
        return f"{value // 1000} kiloohms"
    return f"{value} ohms"
