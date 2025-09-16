INNER_RADIUS_SQUARED = 1
MIDDLE_RADIUS_SQUARED = 25
OUTER_RADIUS_SQUARED = 100

# SCORING_ZONES = [
    # (0.25, 25),   # bullseye: radius² and points
#     (1, 10),      # inner
#     (25, 5),      # middle
#     (100, 1),     # outer
# ]


def score(x, y):
    """
    (num, num) -> int
    
    Returns the points awarded based on the distance from center 
    where the dart lands on the circular target board.
    
    - Inner circle (radius 1): 10 points
    - Middle circle (radius 5): 5 points  
    - Outer circle (radius 10): 1 point
    - Outside target: 0 points    
    """
    try: 
        distance_squared = x**2 + y**2
        if distance_squared <= INNER_RADIUS_SQUARED:
            return 10 
        if distance_squared <= MIDDLE_RADIUS_SQUARED:
            return 5
        if distance_squared <= OUTER_RADIUS_SQUARED:
            return 1
        return 0
    except TypeError:
        print(f"{x}, {y} are not numeric, please enter numeric values.")
        return None

    # try:
    #     distance_squared = x**2 + y**2
    #     for pair in SCORING_ZONES:
    #         if distance_squared <= pair[0]:
    #             return pair[1]
    #     return 0
    # except TypeError:
    #     print(f"{x}, {y} are not numeric, please enter numeric values.")
    #     return None
