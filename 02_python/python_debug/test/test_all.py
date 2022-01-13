import pytest
from src.MyShapes import *

def test_triangle_area():
    shape_obj = RightTriangle(2.5, 7.0)
    area_value = shape_obj.area()
    assert area_value == 8.75

def test_trapezoid_area():
    shape_obj = Trapezoid(2.5, 5.0, 7.0)
    area_value = shape_obj.area()
    assert area_value == 26.25

def test_ellipse_area():
    shape_obj = Ellipse(5.0, 7.0)
    area_value = shape_obj.area()
    assert round(area_value,4) == 27.4889

def test_cylinder_area():
    shape_obj = Cylinder(2.5, 7.0)
    area_value = shape_obj.surf_area()
    assert round(area_value,4) == 149.2257

def test_cone_area():
    shape_obj = RightCircularCone(2.5, 7.0)
    area_value = shape_obj.surf_area()
    assert round(area_value,4) == 78.0139

def test_pyramid_area():
    shape_obj = RectangularPyramid(3.0, 5.0, 7.0)
    area_value = shape_obj.surf_area()
    assert area_value == 73.0937

def test_cylinder_volume():
    shape_obj = Cylinder(2.5, 7.0)
    vol_value = shape_obj.volume()
    assert round(vol_value,4) == 137.44

def test_cone_volume():
    shape_obj = RightCircularCone(2.5, 7.0)
    vol_value = shape_obj.volume()
    assert round(vol_value,4) == 45.8149

def test_pyramid_volume():
    shape_obj = RectangularPyramid(3.0, 5.0, 7.0)
    vol_value = shape_obj.volume()
    assert vol_value == 35.0000

