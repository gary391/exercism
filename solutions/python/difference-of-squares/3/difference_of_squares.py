def square_of_sum(number):
    def fun(number):
        for i in range(number+1):
            yield i

    sum = 0
    for n in fun(number):
        sum += n
    return sum * sum


def sum_of_squares(count: int) -> int:
    sum = 0 
    n  = (i*i for i in range(count + 1))
    for item in n: 
        sum = sum + item
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
