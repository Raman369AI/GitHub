
from logging_config import get_logger

logger = get_logger(__name__)

def count_primes(n):
    sieve = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: sieve[x*2::x] = [False] * len(sieve[x*2::x])
    return sum(sieve) - 2 # subtract 2 because we don'<｜begin▁of▁sentence｜> count '0' and '1' as prime numbers.

print("The number of primes between 1 and 10000 is: ",count_primes(10000))