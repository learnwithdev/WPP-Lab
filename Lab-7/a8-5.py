from abc import abstractmethod
class Shape:
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r=r
    def perimeter(self):
        return 2*3.14*self.r
    def area(self):
        return 3.14*self.r**2
class Rect(Shape):
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
c= Circle(3)
r=Rect(3,4)

print(f"Circumference of Circle: {c.perimeter()} units")
print(f"Area of Circle: {c.area()} units")

print(f"Area of Rectangle: {r.area()} units")
print(f"Perimeter of Rectangle: {r.perimeter()} units")
