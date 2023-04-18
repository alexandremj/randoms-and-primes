from typing import Union
import logging
import time

from sympy import isprime # testing the generated primes

from primality.fermat import FermatPrimality
from primality.miller_rabin import MillerRabinPrimality
from prng.linear_congruential_generator import LinearCongruentialGenerator
from prng.xorshift import XorshiftGenerator

TEST_SUITE_LENGTH = 1
TESTED_LENGTHS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

K = 4

def generate(generator: Union[LinearCongruentialGenerator, XorshiftGenerator],
             length: int) -> int:
    if isinstance(generator, LinearCongruentialGenerator):
        p = next(generator.generate())
    else:
        p = next(generator.generate(length))
    return p


def generate_prime(generator: Union[LinearCongruentialGenerator, XorshiftGenerator],
                   tester: Union[FermatPrimality, MillerRabinPrimality],
                   length: int) -> int:
    p = generate(generator, length)
    logging.debug(p)

    while not tester.is_prime(p, K):
        logging.debug(p)
        p = generate(generator, length)

    return p


if __name__ == '__main__':
    import pdb; pdb.set_trace()
    logging.basicConfig(level=logging.DEBUG)

    fermat = FermatPrimality()
    miller_rabin = MillerRabinPrimality()

    xorshift = XorshiftGenerator()

    lcg_fermat_average_times = {}
    lcg_miller_rabin_average_times = {}
    xorshift_fermat_average_times = {}
    xorshift_miller_rabin_average_times = {}

    #for length in TESTED_LENGTHS:
    #    lcg = LinearCongruentialGenerator(length)
    #    start_time = time.process_time()
    #    for _ in range(TEST_SUITE_LENGTH):
    #        p = generate_prime(lcg, fermat, length)
    #        if not isprime(p):
    #            logging.info(f'Fermat lists {p} as prime but sympy doesn\'t')
    #
    #    end_time = (time.process_time() - start_time) / TEST_SUITE_LENGTH
    #    lcg_fermat_average_times.update({length: end_time})


    #for length in TESTED_LENGTHS:
    #    start_time = time.process_time()
    #    for _ in range(TEST_SUITE_LENGTH):
    #        p = generate_prime(xorshift, fermat, length)
    #        if not isprime(p):
    #            logging.info(f'Fermat lists {p} as prime but sympy doesn\'t')
    #
    #    end_time = (time.process_time() - start_time) / TEST_SUITE_LENGTH
    #    xorshift_fermat_average_times.update({length: end_time})

    for length in TESTED_LENGTHS:
        lcg = LinearCongruentialGenerator(length)
        start_time = time.process_time()

        for _ in range(TEST_SUITE_LENGTH):
            p = generate_prime(lcg, miller_rabin, length)
            if not isprime(p):
                logging.info(f'Miller-Rabin lists {p} as prime but sympy doesn\'t')

        end_time = (time.process_time() - start_time) / TEST_SUITE_LENGTH
        lcg_miller_rabin_average_times.update({length: end_time})


    for length in TESTED_LENGTHS:
        start_time = time.process_time()

        for _ in range(TEST_SUITE_LENGTH):
            p = generate_prime(xorshift, miller_rabin, length)
            if not isprime(p):
                logging.info(f'Miller-Rabin lists {p} as prime but sympy doesn\'t')

        end_time = (time.process_time() - start_time) / TEST_SUITE_LENGTH
        xorshift_miller_rabin_average_times.update({length: end_time})


    logging.info(f'lcg_fermat_average_times = {lcg_fermat_average_times}')
    logging.info(f'lcg_miller_rabin_average_times = {lcg_miller_rabin_average_times}')
    logging.info(f'xorshift_fermat_average_times = {xorshift_fermat_average_times}')
    logging.info(f'xorshift_miller_rabin_average_times = {xorshift_miller_rabin_average_times}')

    import pdb; pdb.set_trace()
