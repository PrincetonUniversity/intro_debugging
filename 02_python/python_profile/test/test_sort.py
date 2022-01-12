import pytest
from src.sort import *

def test_triangle_area():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    sneaky_sort(test_list)
    assert test_list == [1, 2, 3, 4, 6, 7, 8, 9]