import random


def zad118(t: list, w: list, n: int) -> tuple:
    ans = (None, None)

    sum_col = [0 for _ in range(n)]
    sum_row = [0 for _ in range(n)]

    for i in range(n):  # wiersze
        for j in range(n):  # kolumny
            sum_row[i] += t[i][j]
            sum_col[j] += t[i][j]

    index = 0
    for tower in w:  # odejmowanie wież, bo nie szachują one pól, na których się znajdują
        sum_row[tower] -= t[tower][index]
        sum_col[index] -= t[tower][index]
        index += 1

    print(sum_row)
    print(sum_col)

    maxi1 = 0
    maxi2 = 0

    for i in range(n):
        if maxi1 < sum_row[i] + sum_col[i]:
            maxi1 = sum_row[i] + sum_col[i]
            ans = (i, ans[1])
        elif maxi2 < sum_row[i] + sum_col[i] and i != ans[0]:
            maxi2 = sum_row[i] + sum_col[i]
            ans = (ans[0], i)

    return ans


def main():
    n = random.randint(2, 4)  # rozmiar szachownicy
    t = [[random.randint(1, 3) for _ in range(n)] for _ in range(n)]  # szachownica
    w = [random.randint(0, n - 1) for _ in range(n)]  # numery wierszy wież

    for row in t:
        print(row)

    print("towers: ", w)

    print(zad118(t, w, n))


main()
