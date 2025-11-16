def is_valid(isbn):
    # replace "-" in the string
    if "-" in isbn:
        isbn = isbn.replace("-", "")
    # Check if the length of the isbn is less then 10 exit
    if (len(isbn) != 10):
        return False
    if isbn[:-1].isdigit() and (isbn[-1] == "X" or isbn[-1].isdigit()):
        sum = 0
        for index, element in enumerate(isbn):
            if element == "X":
                element = 10
            sum = sum + (int(element) * (10-index))
        return sum % 11 == 0
    return False