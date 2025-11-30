def color_code(color):

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
    print(color_map[color])
    if type(color) == list:
        for cc in color:
            if cc in color_map:
                return color_map[cc]
    return color_map[color]


def colors():
    return ["black", "brown", "red","orange", "yellow", "green", "blue", "violet", "grey", "white"]

