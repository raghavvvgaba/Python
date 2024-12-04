import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(4)
print("area is " + str(a))
print("circumference is " + str(c))

print("area is ", round(a, 2), "circumference is ", round(c, 2))