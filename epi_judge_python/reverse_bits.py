from test_framework import generic_test

def reverse_bits(x: int) -> int:
    result = 0
    for i in range(64):
        shifted = x >> i
        result <<= 1
        result |= shifted & 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
