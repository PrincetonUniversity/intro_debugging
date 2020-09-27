import pytest
from src.MyShapes import RightTriangle

def test_triangle_area():
    mytriangle = RightTriangle(2.5, 7.0)
    triag_area = mytriangle.area()
    assert triag_area == 8.75