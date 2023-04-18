from typing import Tuple
import logging
import random



'''
Implements the Miller-Rabin Primality Test as described in
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
'''
class MillerRabinPrimality():
    def __init__(self):
        pass

    '''
    Factors a number into its even and odd parts, returning the count of even
    potencies and the remaining odd part

    params:
        n: int = the number to be factored
    returns:
        two_count: int = the amount of 2s that appear in the factorization
        remainder: int = the odd part of the factorization
    '''
    def _factor(self, n: int) -> Tuple[int, int]:
        if n < 2:
            raise Exception(f'UntestableIntegerException: {n}')

        logging.debug(f'Factoring {n}')
        two_count = 0
        remainder = n
        while remainder % 2 == 0:
            remainder = remainder / 2
            two_count += 1

        remainder = int(remainder)

        logging.debug(f'Factoring {n} results in 2 ** {two_count} + {remainder}')
        return two_count, remainder

    '''
    Checks if a given number (n) is prime using the Miller-Rabin method with
    k = number of testing rounds

    params:
        n: int = the number to be tested
        k: int = the number of rounds of testing. Improves confidence
                (roughly 4 ** -k)
    returns:
        True if the Miller-Rabin test belives n is a prime number, False
        otherwise

    '''
    def is_prime(self, n: int, k: int) -> bool:
        if n < 4:
            logging.debug(f'{n} is too small, returning False')
            return False

        if n % 2 == 0:
            logging.debug(f'{n} is even, returning False')
            return False

        s, d = self._factor(n - 1)

        for _ in range(k):
            a = random.randrange(2, n - 2)
            x = (a ** d) % n
            logging.debug(f's={s}, d={d}, a={a}, x={x}, n={n}')

            for _ in range(s):
                y = x ** 2 % n
                if y == 1 and x != 1 and x != n - 1:
                    logging.debug(f'{n} failed with above params')
                    return False

                x = y

            if y != 1:
                return False

        logging.debug(f'{n} is believed to be prime')
        return True
