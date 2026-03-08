def line_up(name, number):
    """
    :param name: String
    :param number: number
    :return: String
    {name}, you are the {number}{postfix} customer we serve today. Thank you!"
    """
    
    tens_num = number % 100
    if tens_num in (11, 12, 13):
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
    units_digit_str = str(tens_num)[-1]
    units_digit = int(units_digit_str)
    if units_digit == 1:
        return f"{name}, you are the {number}st customer we serve today. Thank you!"
    if units_digit == 2:
        return f"{name}, you are the {number}nd customer we serve today. Thank you!"
    if units_digit == 3:
        return f"{name}, you are the {number}rd customer we serve today. Thank you!"
    return f"{name}, you are the {number}th customer we serve today. Thank you!"