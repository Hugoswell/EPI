from typing import List

from test_framework import generic_test

def apply_permutation(P: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        while P[i] != i:
            A[i], A[P[i]] = A[P[i]], A[i]
            P[P[i]], P[i] = P[i], P[P[i]]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
