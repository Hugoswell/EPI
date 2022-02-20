from pickle import FALSE
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    low, str_int = 0, str(x)
    high = len(str_int) - 1
    while low < high:
        if str_int[low] != str_int[high]:
            return False
        low += 1
        high -= 1
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
