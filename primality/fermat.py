import logging
import random



"""
    Implements the Fermat primality test. Given a possible prime `n` and `k`
    rounds of testing, the test returns True if, after `k` random numbers
    tested (`a`), none fails the congruency:

    a ** (n - 1) is congruent to 1 mod n

    Notably, the test fails with Carmichael numbers, the first of which is 561

    (Usually definitions use p instead of n)
"""
class FermatPrimality():
    def __init__(self) -> None:
        pass


    """
        Calculates the greatest common dividers of integers a and b by the
        Euclidean Theorem

        parameters
            a: int = first number to be tested
            b: int = second number to be tested

        returns
            a: int = the greatest common divider between a and b
    """
    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a


    """
        Generates a suitable `a` for primality testing, that is, an `a` in the
        range `[2, n-2]` that is coprime to `n`

        parameters:
            n: int = prime number to be tested

        returns:
            a: int = a suitable number to test `n`'s primality
    """
    def _generate_a(self, n: int) -> int:
        a = n

        while self._gcd(a, n) != 1:
            a = random.randrange(2, n - 2)

        return a


    """
        Tests the primality of `n` in `k` rounds

        parameters:
            n: int = assumed prime to be tested
            k: int = rounds of testing

        returns:
            True if the Fermat Primality Test believes the number is a prime,
            False otherwise
    """
    def is_prime(self, n: int, k: int) -> bool:
        if n < 6:
            raise Exception(f'UntestableIntegerException: {n}')

        for _ in range(k):
            a = self._generate_a(n)

            logging.debug(f'a={a}, n={n}, module={a ** (n - 1) % n}')
            if (a ** (n - 1) % n) != 1:
                return False

        return True