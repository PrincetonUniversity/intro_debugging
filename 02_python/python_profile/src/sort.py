"""There is no bug in this code."""
import random
from time import time
import pandas as pd
import sys

def create_rand_list(size, min, max):
    rand_list = []
    for x in range(size):
        rand_list.append(random.randint(min, max))
    return rand_list

@profile
def snail_sort(sort_list):
    for i in range(len(sort_list)):
        for j in range(len(sort_list) - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list

def divide_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        L = sort_list[:mid]
        R = sort_list[mid:]
        divide_sort(L)
        divide_sort(R)
        l_idx = 0
        r_idx = 0
        i = 0
        while l_idx < len(L) and r_idx < len(R):
            if L[l_idx] < R[r_idx]:
                sort_list[i] = L[l_idx]
                l_idx = l_idx + 1
            else:
                sort_list[i] = R[r_idx]
                r_idx = r_idx + 1
            i = i + 1
        while l_idx < len(L):
            sort_list[i] = L[l_idx]
            l_idx = l_idx + 1
            i = i + 1
        while r_idx < len(R):
            sort_list[i] = R[r_idx]
            r_idx = r_idx + 1
            i = i + 1
    return sort_list

def sneaky_sort(sort_list):
    max_val = int(max(sort_list))
    min_val = int(min(sort_list))
    key_range = max_val - min_val + 1
    count_list = [0] * key_range
    output_list = [0] * len(sort_list)

    for i in range(0, len(sort_list)):
        count_list[sort_list[i] - min_val] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]

    for i in range(len(sort_list) - 1, -1, -1):
        output_list[count_list[sort_list[i] - min_val] - 1] = sort_list[i]
        count_list[sort_list[i] - min_val] -= 1

    for i in range(0, len(sort_list)):
        sort_list[i] = output_list[i]

    return sort_list


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please specify a sort type (snail_sort, divide_sort, sneaky_sort).")
        exit(1)

    sort_type = sys.argv[1]
    problem_size = 2
    df_exe = pd.DataFrame(columns=['size', 'time'])
    for x in range(24):
        sort_list = create_rand_list(problem_size, 0, 10000)
        start = time()
        if sort_type == 'sneaky_sort':
            sneaky_sort(sort_list)
        elif sort_type == 'snail_sort':
            snail_sort(sort_list)
        elif sort_type == 'divide_sort':
            divide_sort(sort_list)
        else:
            print("Invalid sort type specified. Defaulting to sneaky_sort.")
            sneaky_sort(sort_list)
        end = time()
        print(f'Sort took {round(end - start, 4)} seconds for {problem_size} numbers.')
        df_exe = df_exe.append(pd.Series([problem_size, round(end - start, 4)], index=df_exe.columns),
                               ignore_index=True)
        problem_size = problem_size * 2
    df_exe.to_csv(sort_type + '_growth.csv', index=False)
