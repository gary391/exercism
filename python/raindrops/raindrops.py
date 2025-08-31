def convert(number):
    # rain_sound = ""
    # if number % 3 == 0:
    #     rain_sound += "Pling"
    # if number % 5 == 0:
    #     rain_sound += "Plang"
    # if number % 7 == 0:
    #     rain_sound += "Plong"
    # # elif number % 3 !=0 and number % 5 != 0 and number % 7 != 0 and number != 0:
    # #     rain_sound = str(number)
    # # return rain_sound
    # # Using ternary operator
    # # value_if_true if condition else value_if_false
    # return rain_sound if rain_sound else str(number)

    rain_sound_dict = {3: "Pling", 5: "Plang", 7: "Plong"}
    # Get the values for the dictionary, and the corresponding sounds
    rain_sound = []
    for item, value in rain_sound_dict.items():
        # print(f"{item}: {value}")
        if number % item == 0:
            rain_sound.append(value)


    return "".join(rain_sound) if rain_sound else str(number)

print(convert(63))