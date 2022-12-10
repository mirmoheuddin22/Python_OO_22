class Rectangle:
  #def __init__(self, p_a, b):
  def __init__(self, p_a=5, b=10):
    self.a = p_a
    self.b = b

  def set_params(self, a, par_b):
    self.a = a
    self.b = par_b

  def calc_surface(self):
    return self.a * self.b

#r = Rectangle(b=6)
#r = Rectangle(p_a=4, b=8)
#r = Rectangle(8, 6)
#r  = Rectangle()
r = Rectangle(b=5)
r.a = 9
#r.set_params(4, 5)
print(r.calc_surface())
#print(r)