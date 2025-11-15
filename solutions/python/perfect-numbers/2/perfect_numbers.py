import math
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    aliquot_sum = set()
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    limit = int(math.sqrt(number))
    for factor in range(1, limit + 1):
        if number % factor == 0:
            aliquot_sum.add(factor)        
            aliquot_sum.add(number // factor)
    if number in aliquot_sum:
        aliquot_sum.remove(number)
    if sum(aliquot_sum) == number:
        return "perfect"
    elif sum(aliquot_sum) > number:
        return "abundant"
    return "deficient"
