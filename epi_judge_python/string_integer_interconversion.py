from calendar import c
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools, string

# My solution
def int_to_string(n: int) -> str:
    negative, n = n < 0, abs(n)
    res = []
    if n == 0:
        return "0"
    while n:
        last_char = chr(ord('0') + n % 10)
        res.append(last_char)
        n //= 10
    if negative:
        res.append('-')
    return ''.join(reversed(res))

# EPI solution
def string_to_int(s: str) -> int:
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda sum, c: sum * 10 + string.digits.index(c),
        s[s[0] in '+-':], 0)

# My solution
def string_to_int(s: str)-> int:
    sign = -1 if s[0] == '-' else 1
    s = s[1:] if s[0] in '+-' else s
    res = 0
    for c in s:
        res *= 10
        res += ord(c) - ord('0')
    return sign * res

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
    # print(int_to_string(-123))