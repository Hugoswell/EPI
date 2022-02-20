from test_framework import generic_test


def reverse(x: int) -> int:
    res, x_remaining = 0, abs(x)
    while x_remaining:
        res = 10 * res + x_remaining % 10
        x_remaining //= 10
    return -res if x < 0 else res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))