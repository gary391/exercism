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
    distance_squared = x**2 + y**2
    INNER_RADIUS_SQUARED = 1
    MIDDLE_RADIUS_SQUARED = 25
    OUTER_RADIUS_SQUARED = 100
    # Type checking reference - https://realpython.com/what-does-isinstance-do-in-python/
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if distance_squared <= INNER_RADIUS_SQUARED:
            return 10 
        if distance_squared <= MIDDLE_RADIUS_SQUARED:
            return 5
        if distance_squared <= OUTER_RADIUS_SQUARED:
            return 1
        else:
            return 0
    else:
        print(f"{x}, {y} are not numeric, please enter numeric values.")
