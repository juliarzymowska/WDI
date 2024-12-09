def moja():
    return None


def zajecia(dane: list):
    wiersz = [False for _ in range(100)]
    kolumna = [False for _ in range(100)]
    p1 = [False for _ in range(199)]  # przekatna1 (od lewej do prawej np)
    p2 = [False for _ in range(199)]  # przekatna2

    for hetman in dane:
        x, y = hetman

        if wiersz[x] or kolumna[y]:
            return True

        wiersz[x] = True
        kolumna[y] = True

        if p1[x + y] or p2[x - y]:  # x-y<0 to python bierze indeks tablicy od konca, np. -1 to ostatni indeks
            return True
        p1[x + y] = True
        p2[x - y] = True

    return False
