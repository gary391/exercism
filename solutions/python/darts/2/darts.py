
def score(x, y):
    """
    https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
    (x - center_x)² + (y - center_y)² < radius²

    Please note that points that satisfy the above equation with < replaced by == are considered the points on the circle,     and the points that satisfy the above equation with < replaced by > are considered the outside the circle.
    
    Equation of the circle who's center is at 0,0 
    \(x^{2}+y^{2}=r^{2}\)
    
    """
    if ((x**2 + y**2 ) <= 1):
        return 10 
    if (((x**2 + y**2 ) > 1) and ((x**2 + y**2 ) <= 25)) :
        return 5
    if (((x**2 + y**2 ) > 25) and ((x**2 + y**2 ) <= 100)):
        return 1
    if  ((x**2 + y**2 ) > 100):
        return 0
