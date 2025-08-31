def is_armstrong_number(number):
    """
    An armstrong number is a number that is the sum of its 
    own digits each raised to the power of the number of digits.

    9 = 9 ^ 1 = 9  --> Yes 
    10 = 1^2 + 0 ^2 --> No 
    20 = 2^2 + 0^2 --> No 
    153 = 1^3 + 5^3 + 3^3 = 1+ 125+ 27 = 153 --> Yes
    121 = 1^3+ 2^3+ 1^1 = 1+8+1 = 10 --> No 
    count the number of digits and then extract every digit and then 
    by using pow function we can get the power of that digit and then
    sum it up at the end and compare with the original number to check
    if it is a Narcissistic Number or not.

    (expression for item in iterable if condition)

    """
    # List of numbers

    # digits = [int(num) for num in str(number)]
    # num_power = len(digits)

    # sum_list = [sum_element + pow(int(num), len(str(number))) for num in str(number)]
    print(type(pow(int(num), len(str(number))) for num in str(number)))
    sum_list = sum(pow(int(num), len(str(number))) for num in str(number))
    print(sum_list)
    # for i in digits:
    #     sum = sum + pow(i, num_power)
    return sum_list == number


print(is_armstrong_number(153))
    
    
