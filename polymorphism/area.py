class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radious=r

    def area(self):
        return 3.1415 * self.radious**2

class Square(Shape):
    def __init__(self, l):
        self.length = l 

    def area(self):
        return self.length**2


circle = Circle(45)
print(circle.area())
square = Square(45)
print(square.area())               