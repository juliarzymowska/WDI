from math import sqrt


def dlpodciagu(T):
    n = len(T)
    lmax = 0  # długosć najdłuższego podciagu

    for i in range(n):
        czynniki = [0 for _ in range(1000)]  # zerowanie tablicy, w której przechowujemy czynniki pierwsze liczby
        l = 0  # długość obecnego podciągu

        for j in range(i, n):  # szukanie podciągu dla obecnego indeksu tablicy
            b = True  # prawda -> nie ma takiego   dzielnika w tablicy czynniki
            dz = 2  # dzielnik, przez który dzielimy liczbę
            a = T[j]
            while a > 1:
                while a % dz == 0:
                    czynniki[dz] += 1
                    a //= dz
                if czynniki[dz] > 1:
                    b = False
                    break
                dz += 1
            if b:
                l += 1
                lmax = max(l, lmax)
            else:
                break
        # break
        return lmax


print(dlpodciagu([2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]))
# dlpodciagu([2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22])
