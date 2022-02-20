from test_framework import generic_test


def reverse_bits(x: int) -> int:
    result = 0
    list = []
    for i in range(64):
        temp = x >> i
        list.append(temp & 1)
    for j in range(64):
        result <<= 1
        result |= list[j]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
