"""Find bugs is the functions."""
import math

class RightTriangle(object):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def area(self):
    return self.base * self.height

class Trapezoid(object):
  def __init__(self, par_side_1, par_side_2, height):
    self.par_side_1 = par_side_1
    self.par_side_2 = par_side_2
    self.height = height
  def area(self):
    sum_par_side = self.par_side_1 + self.par_side_1
    return 0.5 * sum_par_side * self.height

class Ellipse(object):
  def __init__(self, minor_axis, major_axis):
    self.minor_axis = minor_axis
    self.major_axis = major_axis
  def area(self):
    return math.pi * (self.major_axis/2.0) * (self.minor_axis/2.0)

class Cylinder(object):
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  def surf_area(self):
    base_area =  (2 * math.pi * self.radius * self.radius)
    body_area = (2 * math.pi * self.radius * self.height)
    return  body_area + base_area
  def volume(self):
    return math.pi * self.radius * self.height

class RightCircularCone(object):
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  def surf_area(self):
    base_area =  (math.pi * self.radius * self.radius)
    body_area = math.pi * self.radius * math.sqrt((self.radius * self.radius) + (self.height * self.height))
    return  body_area + base_area
  def volume(self):
    return  0.3333333 * 3.14 * self.radius * self.radius * self.height

class RectangularPyramid(object):
  def __init__(self, len_base, width_base, height):
    self.len_base = len_base
    self.width_base = width_base
    self.height = height
  def surf_area(self):
    base_area =  (self.len_base * self.width_base)
    body_area_1 = self.width_base * math.sqrt((self.len_base/2.0 * self.len_base/2.0) + (self.height * self.height))
    body_area_2 = self.len_base * math.sqrt((self.width_base/2.0 * self.width_base/2.0) + (self.height * self.height))
    return  body_area_1 + body_area_2 + base_area
  def volume(self):
    return  0.3333333 * self.len_base * self.width_base * self.height

