def square_of_sum(number):
    def fun(number):
        for i in range(number+1):
            yield i

    total = 0
    for n in fun(number):
        total += n
    return total * total


def sum_of_squares(count: int) -> int:
    total = 0 
    n  = (item*item for item in range(count + 1))
    for i in n: 
        total = total + i
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
