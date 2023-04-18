import logging

from utils import get_seed32


"""
    A XorshiftGenerator Generator is based in applying bitwise operations (in this case,
    AND and shifts) to the binary number to change it
"""
class XorshiftGenerator():
    """
    Initializes the XorshiftGenerator Generator

    parameters
        seed: int = the seed to use as the first state of the generator.
            Defaults to 32 bits from /dev/urandom
    """
    def __init__(self, seed: int = get_seed32()) -> None:
        self.seed = seed
        self.state = seed

    """
    Given the current generator state, generates a new random state and sets it
    as the default state

    returns
        x: int = the generated new state
    """
    def _generate_32bit_state(self) -> int:
        logging.debug(f'Start state: {self.state.bit_length()} bits: {hex(self.state)}')
        x = self.state
        x ^= x << 13
        x ^= x >> 17
        x ^= x << 5

        # trimming result to 32-bits
        x = int(str(hex(x))[:10], 16)

        self.state = x
        logging.debug(f'End state: {self.state.bit_length()} bits: {hex(self.state)}')
        return x

    """
    Generates numbers of at most `length` bits

    parameters
        length: int = the max length generated

    yields
        word: int = the word as a hexadecimal number
    """
    def generate(self, length: int) -> int:
        chunks = round(length / 32)
        last_chunk = length % 32
        logging.debug(f'length={length}, chunks={chunks}, last_chunk={last_chunk}')

        if last_chunk:
            trimming = int(last_chunk / 2)
            word = str(hex(self._generate_32bit_state()))[:trimming]
        else:
            word = ''

        for _ in range(chunks):
            x = self._generate_32bit_state()
            word += str(hex(x))[2:]

        yield int(word, 16)
