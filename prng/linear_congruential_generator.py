from utils import get_seed



# c++11's minstd_rand parameters
# DEFAULT_A = 48271
# DEFAULT_C = 0
# DEFAULT_M = 2**31 - 1

# MMIX as implemented by Donald Knuth
DEFAULT_A = 6364136223846793005
DEFAULT_C = 1442695040888963407
DEFAULT_M = 2 ** 64



"""
A Linear Congruential Generator is based in the recurrence relation:
    X_{n+1} = (a * X_n + c) mod m

With X_0 = seed, a is called the multiplier, c the increment and m the module
for the recurrence relation
"""
class LinearCongruentialGenerator():
    """
    Initializes the Linear Congruential Generator

    parameters
        seed: int = the seed to use as X_0 for the generator.
                    Defaults to 16 bytes from /dev/urandom
        a: int = the multiplier for the recurrence relation.
                    Defaults to DEFAULT_A
        c: int = the increment for the recurrence relation.
                    Defaults to DEFAULT_C
        m: int = the module for the recurrente relation.
                    Defaults to DEFAULT_M
        length: int = overrides m to allow setting the desired length.
                    Defaults to 32
    """
    def __init__(self, seed: int = get_seed(), a: int = DEFAULT_A,
                 c: int = DEFAULT_C, m: int = DEFAULT_M, length: int = 32):
        self.seed = seed
        self.a = a
        self.c = c
        self.length = length

        if length == DEFAULT_M:
            self.m = m
        else:
            self.m = 2 ** length - 1

        self.xn = self.seed


    """
    Generates a new random number and updates current last generated number
    for this instance of the Linear Congruential Generator

    yields:
        number: int = the generated number
    """
    def generate(self) -> int:
        number = (self.a * self.xn + self.c) % self.m
        self.xn = number
        yield number
