# python3
from math import exp, factorial
from string import ascii_letters, digits
import random


def make_key(l):
    letters = ascii_letters + digits
    key = ''
    for _ in range(l):
        key += random.choice(letters)
    return key


def prob_birthday(k, n=365):
    return 1 - factorial(n) / factorial(n - k) / (n**k)


def approx_prob_birthday(k, n=365):
    return 1 - exp(-k**2 / (2 * n))


def number_key(l):
    return 62**l


def prob_key(k, l):
    n = 62**l
    return prob_birthday(k, n)


if __name__ == '__main__':
    random.seed(0)
    print(make_key(4))
    print(make_key(8))
    print(make_key(16))
    print(make_key(32))

    print(prob_birthday(50))
    print(approx_prob_birthday(10000, 62**4))
    print(approx_prob_birthday(10000000, 62**8))
    print(approx_prob_birthday(100000000, 62**10))
    print(approx_prob_birthday(100000000, 62**11))
    print(approx_prob_birthday(1000000000, 62**16))
