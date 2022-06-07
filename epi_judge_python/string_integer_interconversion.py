from calendar import c
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools, string

def int_to_string(i: int) -> str:

def string_to_int(s: str) -> int:


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))