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


def format_result(value, tolerance):
    if value >= GIGA_OHMS:
        return f"{value / 1000_000_000:g} gigaohms  ±{tolerance}"
    elif value >= MEGA_OHMS:
        return f"{value / 1_000_000:g} megaohms ±{tolerance}"
    elif value >= KILO_OHMS:
        return f"{value / 1_000:g} kiloohms ±{tolerance}"
    return f"{value} ohms ±{tolerance}"


def resistor_label(colors):
    if len(colors) == 1:
        return f"{COLOR_TO_VALUE.index(colors[0])} ohms"
    sig_band_count = len(colors) - 2 # 3 or 2 depending on number of colors 4,5
    sig_colors = colors[:sig_band_count]
    multiplier_color = COLOR_TO_VALUE.index(colors[sig_band_count])
    tolerance = TOLERANCE[colors[-1]]
    digits = [str(COLOR_TO_VALUE.index(c)) for c in sig_colors]
    resistor = "".join(digits)
    value = int(resistor) * 10**int(multiplier_color)
    return format_result(value, tolerance)