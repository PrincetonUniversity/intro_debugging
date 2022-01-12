"""There is no bug in this code."""
import random
from time import time
import pandas as pd
import math


def create_rand_list(size, min, max):
    rand_list = []
    for x in range(size):
        rand_list.append(random.randint(min, max))
    return rand_list


def simple_search(search_list, query_list):
    found_ctr = 0
    for i in query_list:
        for k in search_list:
            if i == k:
                found_ctr = found_ctr + 1
                break
    return found_ctr


def sort_search(search_list, query_list):
    found_ctr = 0
    search_list.sort()
    for i in query_list:
        for k in search_list:
            if i == k:
                found_ctr = found_ctr + 1
                break
    return found_ctr


def better_search(search_list, query_list):
    found_ctr = 0
    search_list.sort()
    for i in query_list:
        found = False
        first = 0
        last = len(search_list)
        while not found and first <= last:
            mid = int((first + last) / 2)
            if i == search_list[mid]:
                found_ctr = found_ctr + 1
                found = True
            else:
                if i < search_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
    return found_ctr


if __name__ == '__main__':
    start = time()
    search_list = create_rand_list(10000, 0, 10000)
    query_list = create_rand_list(1000, 0, 10000)
    end = time()
    print(f'Data generation took {round(end - start, 4)} seconds.')

    start = time()
    found_count = better_search(search_list, query_list)
    print("Found {} elements.".format(found_count))
    end = time()
    print(f'Simple search took {round(end - start, 4)} seconds.')
