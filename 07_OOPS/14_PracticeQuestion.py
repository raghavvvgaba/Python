class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        a = 3.14 * self.radius**2
        print(a)
    def perimeter(self):
        p = 2 * 3.14 * self.radius
        print(p)
c1 = Circle(21)
c1.area()
c1.perimeter()