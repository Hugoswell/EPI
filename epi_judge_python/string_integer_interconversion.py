from calendar import c
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools, string

def int_to_string(x: int) -> str:
    negative = False
    if x < 0:
        x, negative = -x, True
    res = []
    while True:
        res.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    return ('-' if negative else '') + ''.join(reversed(res))


def string_to_int(s: str) -> int:
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda sum, c: sum * 10 + string.digits.index(c),
        s[s[0] in '+-':], 0)


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