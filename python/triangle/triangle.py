# def isTriangle(a, b, c):
#     """
#     sorted(a,b,c)
#     """
#     sides = sorted([a,b,c])
#     # if a > 0 and b > 0 and c > 0:
#     #     if (a + b >= c) and (b + c >= a) and ( a + c >= b):
#     #         return True
#     # return False
#     return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])



def isTriangle(a, b, c):
    sides = sorted([a,b,c])
    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])
# print(isTriangle(5, 9, 2))
def equilateral(sides):
    a,b,c = sides
    if set([a,b,c]) != {0}:
        return len(set(sides)) == 1




# print(equilateral([0, 0, 0]))
def isosceles(sides):
    pass


def scalene(sides):
    return len(set(sides)) == 3

print(scalene([7, 3, 2]))
