import numpy as np
import math

class TwoVec:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.arr=np.array([self.x, self.y])
    def mag(self):
        return math.sqrt(sum(pow(element, 2) for element in self.arr))
    def rot(self):
        return math.atan(self.y/self.x)
    def dotp(self, o):
        return np.dot(self.arr, o.arr)
    def crossp(self, o):
        return np.cross(self.arr, o.arr)
    def dis(self, o):
        return math.dist(self.arr, o.arr)

class ThreeVec(TwoVec):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z
        self.arr=np.array([self.x, self.y, self.z])

    def mag(self):
        return math.sqrt(sum(pow(element, 2) for element in self.arr))
    # def rot(self):
    #     return math.atan(self.y/self.x)
    def dotp(self, o):
        return np.dot(self.arr, o.arr)
    def crossp(self, o):
        return np.cross(self.arr, o.arr)
    def dis(self, o):
        return math.dist(self.arr, o.arr)
    

v1 = ThreeVec(3,4,5)
v2 = ThreeVec(1,2,3)
# print(v1.mag())
# print(v1.rot())
print(v1.crossp(v2))
# print(v1.dotp(v2))
# print(v1.crossp(v2))
        