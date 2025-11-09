def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    aliquot_sum = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")    
    for factor in range(1, number + 1):
        if number != factor and number % factor == 0:
            aliquot_sum += factor
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"
