KILO_OHMS = 1000
MEGA_OHMS = 1000000
GIGA_OHMS = 1000000000
TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}

COLOR_TO_VALUE = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def resistor_label(colors):
    resistor = ""

    if len(colors) == 5:
        tolerance = TOLERANCE[colors[-1]]
        multi_value = COLOR_TO_VALUE.index(colors[3:4][0])
        for color in colors[:3]:
            resistor += str(COLOR_TO_VALUE.index(color))
        value = int(resistor) * 10**multi_value
        if value >= GIGA_OHMS:
            return f"{value / 1000_000_000:g} gigaohms  ±{tolerance}"
        elif value >= MEGA_OHMS:
            return f"{value / 1_000_000:g} megaohms ±{tolerance}"
        elif value >= KILO_OHMS:
            return f"{value / 1_000:g} kiloohms ±{tolerance}"
        return f"{value} ohms ±{tolerance}"
    elif len(colors) == 4:
        tolerance = TOLERANCE[colors[-1]]
        multi_value = COLOR_TO_VALUE.index(colors[2:3][0])
        for color in colors[:2]:
            resistor += str(COLOR_TO_VALUE.index(color))
        value = int(resistor) * 10**multi_value
        if value >= GIGA_OHMS:
            return f"{value / 1000_000_000:g} gigaohms  ±{tolerance}"
        elif value >= MEGA_OHMS:
            return f"{value / 1_000_000:g} megaohms ±{tolerance}"
        elif value >= KILO_OHMS:
            return f"{value / 1_000:g} kiloohms ±{tolerance}"
        return f"{value} ohms ±{tolerance}"
    return f"{COLOR_TO_VALUE.index(colors[0])} ohms"



