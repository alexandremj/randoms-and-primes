import os



def coprimes(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return


# reads 16 bytes from /dev/urandom to use as a seed if none is provided
def get_seed() -> int:
    return int.from_bytes(os.urandom(16), byteorder='little')

def get_seed32() -> int:
    return int.from_bytes(os.urandom(8), byteorder='little')
