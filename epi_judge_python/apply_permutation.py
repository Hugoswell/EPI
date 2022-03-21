from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    B = [-1] * len(A)
    print(B)
    for i in range(len(A)):
        B[perm[i]] = A[i]
    A = B.copy()
    print(A)


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('apply_permutation.py',
    #                                    'apply_permutation.tsv',
    #                                    apply_permutation_wrapper))
    apply_permutation([2,0,1,4,3], ['a','b','c','d','f'])
