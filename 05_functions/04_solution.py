import math
def circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference
a, c = circle(4)

print("Area:", round(a,2), "Circumference:", round(c,2))
     