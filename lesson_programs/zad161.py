import random


def binary(number: int):
    cnt = 0
    while number > 0:
        cnt += (number % 2)
        number //= 2
    return cnt


def zad161(t, p, p1=0, p2=0, p3=0):
    if p == len(t):
        return p1 == p2 == p3

    zad161(t, p + 1, p1 + t[p], p2, p3)
    zad161(t, p + 1, p1, p2 + t[p], p3)
    zad161(t, p + 1, p1, p2, p3 + t[p])


def main():
    t = [random.randint(1, 5) for _ in range(8)]
    ans = []
    for i in range(len(t)):
        ans.append(binary(t[i]))

    print("Liczby wejściowe: ", t)
    print("Zamiana na system 2: ", ans)
    print(zad161(ans, 0))


main()
