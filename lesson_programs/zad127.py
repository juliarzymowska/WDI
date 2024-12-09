def multi(s: str) -> int:
    n = len(s)
    ok = True

    for c in range(n // 2 + 1):  # sprawdzamy do połowy stringa, bo pattern nie może być dłuższy niż połowa
        if n % c == 0:  # sprawdzamy czy możemy wziąć taki fragment (dla str o size 15 nie może być fragment równy 4)
            ok = True
            for i in range(c):  # przechodzimy przez kolejne litery naszego fragmentu
                for j in range(c, n,
                               c):  # przechodzimy przez kolejne litery naszego fragmentu porównując je do kolejnych przedziałów
                    if s[i] != s[i + j]:  # jeśli fałsz
                        ok = False
                        break
                if not ok:  # fragment się nie zgadza, przerywamy dla naszego fragmentu
                    break
            # end for
            if ok:  # jeśli cały fragment przeszedł to zwracamy długość napisu
                return n
    return 0


def main():
    maxi = 0
    n = int(input())
    t = [str(input()) for _ in range(n)]

    for i in range(n):
        maxi = max(maxi, multi(str(input())))

    print(maxi)


main()
