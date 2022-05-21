from test_framework import generic_test

# EPI O(n)T solution
# def parity(x: int) -> int:
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result

# EPI 0(n)T solution better average and best case
# def parity(x: int) -> int:
#     count = 0
#     while x:
#         count ^= 1
#         x &= x - 1
#     return count

# My Solution O(n)T
# def parity(i : int) -> int:
#     count = 0
#     while i:
#         count += i & 1
#         i >>= 1
#     return count % 2 == 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
 