# def square(number):
#     """
#
#     :param number: number of squares
#     :return: number of grains in the square.
#     """
#     if number < 1 or number > 64:
#         raise ValueError("square must be between 1 and 64")
#     return 2 ** (number - 1)


def square(number):
    """

    :param number: number of squares
    :return: number of grains in the square.
    """
    # if number < 1 or number > 64:
    #     raise ValueError("square must be between 1 and 64")
    # return 2 ** (number - 1)

    """
    1 << 2
    0000 0001 << 2 ---> 0000 0100 = 4 
    1 << 3 
    0000 0001 << 3 ---> 0000 1000 = 8
    
    2^0 + 2^1 + 2^2 ---+2^63
    a = 2^0 = 1 - First term 
    r = common ratio, which is 2 in our case 
    n = 64 
    sum of n terms in GP =  a (1-r^n)/(1-r)
    1(1-2^64)/(-1)
    2^64 -1 
    (1<<64) -1
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)


def total():
  return (1 << 64) - 1


def square_old(number):
    """

    :param number: number of squares
    :return: number of grains in the square.

    1 << 2
    0000 0001 << 2 ---> 0000 0100 = 4
    1 << 3
    0000 0001 << 3 ---> 0000 1000 = 8
    1, 2 4 8
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    return 1 << number - 1

print(square_old(3))