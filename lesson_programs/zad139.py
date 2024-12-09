import random


def zad139(number: int):
    # print(number)
    if number % 2 == 0:
        return zad139(number // 2)
    if number % 3 == 0:
        return zad139(number // 3)
    if number % 5 == 0:
        return zad139(number // 5)

    if number == 1:
        return True
    return False


def main():
    n = random.randint(1, 100)
    # print(17, zad139(17))
    for i in range(1, n + 1):
        if zad139(i):
            print(i, sep=" ")


main()
