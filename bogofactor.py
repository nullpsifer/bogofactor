from math import factorial
from random import SystemRandom


def is_prime(n):
    return (factorial(n - 1) + 1) % n == 0


def bogofactor(n):
    if is_prime(n):
        return [n]
    else:
        while True:
            cryptogen = SystemRandom()
            divisor = cryptogen.randrange(2, n)
            if n % divisor == 0:
                return bogofactor(divisor) + bogofactor(int(n / divisor))
