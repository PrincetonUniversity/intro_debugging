"""There is no bug in this code."""
import random
from time import time
from sort import *
import sys


def create_rand_list(size, min, max):
    rand_list = []
    for x in range(size):
        rand_list.append(random.randint(min, max))
    return rand_list


def simple_search(search_list, query):
    for k in search_list:
        if query == k:
            return True
    return False

def sort_search(search_list, query):
    sorted_list = snail_sort(search_list)
    return simple_search(sorted_list, query)

def better_search(search_list, query):
    sorted_list = snail_sort(search_list)
    first = 0
    last = len(sorted_list)
    while first <= last:
        mid = int((first + last) / 2)
        if query == sorted_list[mid]:
            return True
        else:
            if query < sorted_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

def list_searching(search_list, query_list, search_func):
    found_ctr = 0
    search_list.sort()
    for i in query_list:
        if search_func(search_list, i):
            found_ctr = found_ctr + 1
    return found_ctr

"""
Program to search a list of numbers in another list of numbers
"""
if __name__ == '__main__':
    start = time()
    if len(sys.argv) < 2:
        print("Please specify a search type (simple_search, sort_search, better_search).")
        exit(1)
    search_type = sys.argv[1]
    search_list = create_rand_list(1000, 0, 10000)
    query_list = create_rand_list(100, 0, 1000)
    end = time()
    print(f'Data generation took {round(end - start, 4)} seconds.')
    start = time()
    found_count = 0
    if search_type == 'simple_search':
        found_count = list_searching(search_list, query_list, simple_search)
    elif search_type == 'sort_search':
        found_count = list_searching(search_list, query_list, sort_search)
    elif search_type == 'better_search':
        found_count = list_searching(search_list, query_list, better_search)
    else:
        print("Not a valid search type. Defaulting to simple_search.")
        found_count = list_searching(search_list, query_list, simple_search)
    print("Found {} elements.".format(found_count))
    end = time()
    print(f'Search took {round(end - start, 4)} seconds.')
