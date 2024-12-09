import random


def is_prime(number: int):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def binary_to_decimal(t: str) -> int:
    return int(t, 2)


def zad137(t: str, ans: list):
    # print(t)

    if is_prime(binary_to_decimal(t)) and len(ans) > 0:
        return True

    for i in range(len(t) - 1, -1, -1):
        if is_prime(binary_to_decimal(t[i:])):
            return zad137(t[:i], ans + [t[i:]])

    return False


def main():
    n = random.randint(10, 1000)
    t = bin(n)[2:]
    print(t, zad137(str(t), []))


main()
