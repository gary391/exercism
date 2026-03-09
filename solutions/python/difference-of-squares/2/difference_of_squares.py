def square_of_sum(number):
    def fun(number):
        for i in range(number+1):
            yield i

    sum = 0
    for n in fun(number):
        sum += n
    return sum * sum


def sum_of_squares(number):
    def fun(number):
        for i in range(number+1):
            yield i
    sum = 0
    for n in fun(number):
        sum += n*n
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
