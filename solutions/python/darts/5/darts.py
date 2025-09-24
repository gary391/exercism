INNER_RADIUS_SQUARED = 1  # 1²
MIDDLE_RADIUS_SQUARED = 25 # 5²
OUTER_RADIUS_SQUARED = 100  # 10²

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
    except TypeError:
        raise TypeError(f"x and y must be numeric, got {type(x).__name__} and {type(y).__name__}")
    if distance_squared <= INNER_RADIUS_SQUARED:
        return 10 
    if distance_squared <= MIDDLE_RADIUS_SQUARED:
        return 5
    if distance_squared <= OUTER_RADIUS_SQUARED:
        return 1
    return 0
