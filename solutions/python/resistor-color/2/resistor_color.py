
def color_code(color):
    all_colors = colors()
    for index, value in enumerate(all_colors):
        if value == color:
            return index


def colors():
    return ["black", "brown", "red","orange", "yellow", "green", "blue", "violet", "grey", "white"]

