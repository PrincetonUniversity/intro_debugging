import pytest
from src.sort import *

def test_snail_sort():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    snail_sort(test_list)
    assert test_list == [1, 2, 3, 4, 6, 7, 8, 9]

def test_divide_sort():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    divide_sort(test_list)
    assert test_list == [1, 2, 3, 4, 6, 7, 8, 9]

def test_sneaky_sort():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    sneaky_sort(test_list)
    assert test_list == [1, 2, 3, 4, 6, 7, 8, 9]