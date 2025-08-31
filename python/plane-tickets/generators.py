"""Functions to automate Conda airlines ticketing system."""
from itertools import cycle, islice

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    # >>> letters = generate_seat_letters(4)
    # >>> next(letters)
    # "A"
    # >>> next(letters)
    "B"
    """
    seats = ["A", "B", "C", "D"]
    for i in range(number):
        yield seats[i % 4]

# letters = generate_seat_letters(6)
# print(next(letters))
# print(next(letters))
# print(next(letters))
# print(next(letters))
# print(next(letters))
# print(next(letters))




def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    # row = 1
    # count = 0
    # while count < number: # this will be one row
    #     if row == 13:
    #         row += 1
    #
    #     # Number of seats per row
    #     seats_per_row = min(4, number - count)
    #     print(seats_per_row)
    #     for seat in generate_seat_letters(seats_per_row):
    #         yield f"{row}{seat}"
    #         count += 1
    #     row +=1

    """
    number is number of seats 
    1 -> 1A
    2 -> 1A, 1B
    3 -> 1A, 1B, 1C
    4 -> 1A, 1B, 1C, 1D
    5 -> 1A, 1B, 1C, 1D, 2A
    """
    number_of_seats = cycle(['A', 'B', 'C', 'D'])
    for i in range(1,number+1):
        row = ((i - 1) // 4) + 1
        if row >=13:
            row+=1
        yield (f"{row}{next(number_of_seats)}")



seat = (list(generate_seats(56)))
print(seat)



def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    number_of_seats = len(passengers)
    seats = generate_seats(number_of_seats)
    # zip creates an iterator that aggregates elements from multiple iterables
    return {passenger: seat for passenger, seat in zip(passengers, seats)}

# print(assign_seats(['Passenger1', 'Passenger2', 'Passenger3', 'Passenger4', 'Passenger5']))

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    test_data = [(["12A", "38B", "69C", "102B"],"KL1022"),
              (["22C", "88B", "33A", "44B"], "DL1002")]
result_data = [['12AKL1022000', '38BKL1022000', '69CKL1022000', '102BKL102200'],
               ['22CDL1002000', '88BDL1002000', '33ADL1002000', '44BDL1002000']]
    """
    empty = []
    for seat in seat_numbers:
        empty.append(seat+flight_id)
    padded_list = []
    for element in empty:
        padding_needed = 12 - len(element)
        if padding_needed > 0:
            element += "0"*padding_needed
        padded_list.append(element)
    yield padded_list[0]

code = (generate_codes(["12A", "38B", "69C", "102B"],"KL1022"))
print(next(code))
