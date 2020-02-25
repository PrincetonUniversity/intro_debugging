class RightTriangle(object):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return 0.5 * self.base * self.height

class Rectangle(object):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return self.base * self.height
