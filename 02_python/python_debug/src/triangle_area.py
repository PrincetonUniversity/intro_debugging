"""There is no bug in this code."""

from .src.MyShapes import RightTriangle


"""
Program to print the area of a triangle
"""
if __name__ == '__main__':
  mytriangle = RightTriangle(2.5, 7.0)
  triag_area = mytriangle.area()
  print("triangle area = ", triag_area)
