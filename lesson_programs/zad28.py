from math import sqrt


def rozklad(n: int):
    for i in range(int(sqrt(n)), 0, -1):
        if n % i == 0:
            return i, n // i


x = int(input())
print(rozklad(x))
