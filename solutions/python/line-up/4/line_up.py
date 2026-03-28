"""Module providing a function printing python version."""
def line_up(name, number):
    """
    :param name: String
    :param number: number
    :return: String
    {name}, you are the {number}{suffix} customer we serve today. Thank you!"
    """
    suffix_text = find_suffix(number)
    return f"{name}, you are the {number}{suffix_text} customer we serve today. Thank you!"

def find_suffix(number):
    tens_num = number % 100
    if tens_num in [11, 12, 13]:
        suffix = "th"
    else: 
        units_digit = int(str(tens_num)[-1])
        if units_digit == 1:
            suffix = "st"
        elif units_digit == 2:
            suffix = "nd"
        elif units_digit == 3:
            suffix = "rd"
        else: 
            suffix = "th"
    return suffix
