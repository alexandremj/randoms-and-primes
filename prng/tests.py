from linear_congruential_generator import LinearCongruentialGenerator
from xorshift import XorshiftGenerator

import logging
import time

TEST_SUITE_LENGTH = 10000
TESTED_LENGTHS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]



def test_generate_lcg():
    times = {}
    for length in TESTED_LENGTHS:
        start_time = time.process_time()
        generator = LinearCongruentialGenerator(length=length)
        for _ in range(TEST_SUITE_LENGTH):
            n = next(generator.generate())
            # print(f'{n.bit_length()} (expected {length}) bits: {hex(n)}')

        end_time = round(time.process_time() - start_time, 6)
        average_end_time = end_time / TEST_SUITE_LENGTH
        times.update({length: average_end_time})
    return times


def test_generate_xorshift():
    generator = XorshiftGenerator()
    times = {}
    for length in TESTED_LENGTHS:
        start_time = time.process_time()
        for _ in range(TEST_SUITE_LENGTH):
            n = next(generator.generate(length=length))
            # print(f'{n.bit_length()} (expected {length}) bits: {hex(n)}')

        end_time = round(time.process_time() - start_time, 6)
        average_end_time = end_time / TEST_SUITE_LENGTH
        times.update({length: average_end_time})
    return times


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    lcg_times = test_generate_lcg()
    xorshift_times = test_generate_xorshift()
    logging.info(f'lcg_times: {lcg_times}')
    logging.info(f'xorshift_times: {xorshift_times}')
    import pdb; pdb.set_trace()
