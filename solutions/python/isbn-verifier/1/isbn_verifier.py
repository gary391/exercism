def is_valid(isbn):
    count = 10
    sum = 0
    # replace "-" in the string
    if "-" in isbn:
        isbn = isbn.replace("-", "")
    # Check if the length of the isbn is less then 10 exit
    if (len(isbn) != 10):
        return False
    if isbn[:-1].isdigit() and (isbn[-1] == "X" or isbn[-1].isdigit()):
        for element in isbn:
            if element == "X":
                element = 10
            else:
                element = int(element)
            sum = sum + element * count
            count = count - 1
        if sum % 11 == 0:
            return True
    return False
