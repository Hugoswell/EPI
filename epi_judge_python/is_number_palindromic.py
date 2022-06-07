from pickle import FALSE
from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))