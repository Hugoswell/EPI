from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    current_pos = len(A)-1
    while current_pos >= 0:
        if A[current_pos] == 9:
            A[current_pos] = 0
        else:
            A[current_pos] += 1
            break
        current_pos -= 1
    if current_pos == -1:
        A.insert(0,1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
