OHMS_UNIT = {
    "gigaohms": 1000_000_000,
    "megaohms": 1_000_000,
    "kiloohms": 1_000
}

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
    for ohm_key, ohm_value in OHMS_UNIT.items():
        if value >= ohm_value:
            return f"{value / ohm_value:g} {ohm_key} ±{tolerance}"
    return f"{value} ohms ±{tolerance}"


def resistor_label(colors):
    """
    Returns the resistance value in ohms with ±tolerance for a given resistor
    color input. The colors inputs is a list where each index value represents
    signal multiplier, tolerance ex: [sig1, sig2, multiplier, tolerance].
    """
    if len(colors) == 1:
        return f"{COLOR_TO_VALUE.index(colors[0])} ohms"
        
    *sig_colors, multiplier_color, tolerance_color = colors
    
    sig_value = 0
    for col in sig_colors:
        sig_value = sig_value * 10 + COLOR_TO_VALUE.index(col)
    tolerance = TOLERANCE[tolerance_color]
    value = sig_value * 10 ** COLOR_TO_VALUE.index(multiplier_color)
    
    return format_result(value, tolerance)