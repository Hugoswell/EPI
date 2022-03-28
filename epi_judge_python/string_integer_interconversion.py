from test_framework import generic_test
from test_framework.test_failure import TestFailure

def int_to_string(x: int) -> str:
    sign = '' if x >= 0 else '-'
    number = abs(x)
    result = ''
    while number:
        current_digit = number % 10
        result += str(current_digit)
        number //= 10
    result += sign
    return result[::-1]


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    return 0


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