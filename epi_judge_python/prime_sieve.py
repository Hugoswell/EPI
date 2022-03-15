from typing import List

from test_framework import generic_test
import math


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    def is_prime(n: int) -> bool:
        nb_divisors = 0
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                nb_divisors += 1            
        return nb_divisors == 0
    
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
