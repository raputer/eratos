import math


def getPrime(number: int):
    limit = int(math.sqrt(number))
    prime = [2]
    odd = [i + 1 for i in range(2, number, 2)]

    if all([number > 1, isinstance(number, int)]):
        while limit >= odd[0]:
            prime.append(odd[0])
            odd = [j for j in odd if j % odd[0] != 0]
        return prime + odd
    return 0


def isPrime(number: int):
    if number in getPrime(number):
        return True
    return False
