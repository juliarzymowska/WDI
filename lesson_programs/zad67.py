from math import sqrt


def rozklad_liczby(a: int):
    dzielnik = 2
    czynniki = [False for _ in range(int(sqrt(a)) + 1)]

    while dzielnik * dzielnik <= a:
        if a % dzielnik == 0:
            czynniki[dzielnik] = True
        # end if
        while a % dzielnik == 0:
            a //= dzielnik
        # end while
        dzielnik += 1
    # end while

    return czynniki


def skok(T):
    n = len(T)
    ans = [False for _ in range(len(T))]
    ans[0] = True  # prawda dla indeksu 0

    tab = rozklad_liczby(T[0])

    for j in range(len(tab)):  # przypadek dla T[0]
        if j <= n:
            ans[j] = True  # wpisujemy, gdzie możemy wejść zaczynając od indeksu 0

    for i in range(1, n):
        if ans[i]:  # jeśli możemy wejść z indeksu 0/i
            tab = rozklad_liczby(T[i])

            for j in range(len(tab)):  # przeszukujemy tablicę czynników
                if tab[j] and i + j < n:
                    ans[i + j] = True

    if ans[n - 1]:
        return True
    return False


def main():
    print(skok([4, 9, 10, 3, 5, 12, 2, 11, 12, 15212512]))


main()
