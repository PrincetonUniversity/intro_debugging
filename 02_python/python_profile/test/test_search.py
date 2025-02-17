import pytest
from src.search import *

def test_simple_search():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    assert simple_search(test_list, 7) is True
    assert simple_search(test_list, 99) is False

def test_sort_search():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    assert sort_search(test_list, 7) is True
    assert sort_search(test_list, 99) is False

def test_better_search():
    test_list = [9, 8, 6, 7, 4, 3, 2, 1 ]
    assert better_search(test_list, 1) is True
    assert better_search(test_list, 99) is False ## Expected to fail. Fix!
