def isEven(number):
    return number % 2 == 0


def forEven(number):
    return number // 2

def forOdd(number):
    return (number * number) +1


def steps(number):
    """
    Collatz Conjecture
    Can every number find its way to 1?

    The rules were deceptively simple. Pick any positive integer.

    If it's even, divide it by 2.
    If it's odd, multiply it by 3 and add 1.

    For number 12
    12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1

    #TODO
    - Given a positive integer, return the number of steps it takes
      to reach 1 according to the rules of the Collatz Conjecture.
    - Raise an expection (ValueError)
        - If the given value is zero or a negative integer
          raise ValueError("Only positive integers are allowed")

    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # def isEvenOdd(number):
    #     return number % 2 == 0


    # Keep a counter to know the steps.
    # Check the number is even or odd

    # If the number is even divide the number by 2

    # If the number is even again divide the number by 2
    # If the number is odd, multiply the number by 3 and add 1
    def helper(num, count):
        if num == 1:
            return count
        count += 1
        if num % 2 == 0:
            num = num // 2
            if num == 1:
                return count
            else:
                return helper(num, count)
        else:
            if num == 1:
                return count
            num = (num * 3) + 1
            return helper(num, count)

    return helper(number, 0)





print(steps(1))