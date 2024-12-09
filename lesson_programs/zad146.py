import random


def zad146_lesson(number, ans="", start=1):  # probably not working (?)
    if number == 0 and not str(number) in ans:
        print(ans)
        exit()

    for i in range(start, number):
        zad146_lesson(number - i, ans + str(i), i)


def podziały(n, wynik="", ostatnia=1):  # daga
    # print(f"N: {n}, wynik: {wynik}, ostatnia: {ostatnia}")

    if n == 0 or wynik[:-1] == "+":
        print(wynik[:-1], '\n\n')
        return

    for x in range(ostatnia, n + 1):
        # print("Petla: ", n, n - x, wynik + f"{x}" + "+", x, sep=',')
        podziały(n - x, wynik + f"{x}" + "+", x)


def main():
    n = random.randint(2, 10)
    print(n)
    # print(podziały(n))
    zad146_lesson(n)


main()
