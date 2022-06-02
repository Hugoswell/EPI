from typing import List

from test_framework import generic_test
import math

# My solution O(nloglog(n))T, O(n)S
def generate_primes(n: int) -> List[int]:
    result, primes = [], [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
            result.append(i)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
