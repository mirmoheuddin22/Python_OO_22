from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    @abstractmethod
    def calc_surface(self):
        pass

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    @abstractmethod
    def calc_surface(self):
        return 55
        #pass

    def get_a(self):
        return self._a

class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b
    #def calc_surface(self):
    #    return self._a*self.b

    def swap_sides(self):
        a = self._a
# @@ -38,24 +39,31
    # @@ def __init__(self, a):
#         #self._a = a

    def calc_surface(self):
        print(super().calc_surface())
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


#s = Shape(14, 4)
#print(s)

class Triangle(Shape):
    def calc_surface(self):
        pass

# It's not possible to create an instance of an abstract class Shape
#s = Shape(67, 76)
#print(s)

r = Rectangle(5, 6)
print(r)
#r._a = 600
#print(r.calc_surface())
print(r.calc_surface())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
t = Triangle(4, 6)
print(t)

c = Circle(6)
print(c.calc_surface())
print(c)