def leap_year(year):
    """"
    1. Every year that is evenly divided by 4
    2. Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly
       divisible by 400
    """

    # If a number is multiple of 100

    if year % 100 == 0:
        if year % 400==0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False

print(leap_year(2000))