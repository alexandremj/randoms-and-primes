import logging

from fermat import FermatPrimality
from miller_rabin import MillerRabinPrimality
from sympy import isprime # used for comparing results



logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

PRIME_START = 7
PRIME_LIMIT = 1000
candidates = [i for i in range(PRIME_START, PRIME_LIMIT)]
# tester = MillerRabinPrimality()
tester = FermatPrimality()
primes = []

for i in range(PRIME_START, PRIME_LIMIT):
    if tester.is_prime(i, 4):
        primes.append(i)

sympy_primes = [i for i in range(PRIME_START, PRIME_LIMIT) if isprime(i)]


print('False positives: ')
print(sorted(list(set(primes) - set(sympy_primes))))
print('Undetected primes:')
print(sorted(list(set(sympy_primes) - set(primes))))