import math
from unittest import result
from test_framework import generic_test
import string

# My solution
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def from_b1_to_decimal(numb1: str):
        result, numb1 = 0, numb1.lower()
        for i in range(len(numb1)):
            exponential = len(numb1) - i - 1
            result += string.hexdigits.index(numb1[i]) * (b1 ** exponential)
        return result

    def from_decimal_to_b2(numb10: int, b2: int) -> str:
        result = []
        while numb10:
            result.append(string.hexdigits[numb10 % b2].upper())
            numb10 //= b2
        return ''.join(reversed(result)) or '0'
    
    negative = num_as_string[0] == '-'
    if negative:
        num_as_string = num_as_string[1:]
    
    base10 = from_b1_to_decimal(num_as_string)
    return '-' + from_decimal_to_b2(base10, b2) if negative else from_decimal_to_b2(base10, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
