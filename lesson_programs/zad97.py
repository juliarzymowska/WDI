def zad97(t: list) -> list:
    n = len(t)
    ans = []  # list to store the answer
    it = [0] * n  # indicator for each column
    min_i = None  # index of the smallest element in the current iteration

    while len(ans) < n * n:
        min_val = float('inf')

        for i in range(n):
            if it[i] < n and t[i][it[i]] < min_val:
                min_val = t[i][it[i]]
                min_i = i

        if min_val not in ans:
            ans.append(min_val)
        else:
            ans.append(0)

        it[min_i] += 1

    return ans


def move_left(t: list) -> list:
    n = len(t)

    for i in range(n):
        if t[i] == 0:
            for j in range(i + 1, n):
                if t[j] != 0:
                    t[i] = t[j]
                    t[j] = 0
                    break

    return t


def main():
    t = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [3, 4, 5, 6],
        [2, 3, 7, 9]
    ]
    print(move_left((zad97(t))))


main()
