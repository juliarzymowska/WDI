import math


def prime(n: int):
    if n < 2:
        return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


n = int(input())
print(prime(n))
