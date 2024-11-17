def dlugosc_najdluzszego_ciagu_geometrycznego(T):
    n = len(T)
    if n < 3:
        return 0

    max_dlugosc = 0
    dlugosc_biezaca = 2  # minimalna długość ciągu geometrycznego to 2
    poprzedni_iloraz = (T[1][0] * T[0][1] / T[1][1] * T[0][0])

    for i in range(1, n - 1):
        obecny_iloraz = (T[i + 1][0] * T[i][1] / T[i + 1][1] * T[i][0])

        if obecny_iloraz == poprzedni_iloraz:
            dlugosc_biezaca += 1
        else:
            if dlugosc_biezaca > max_dlugosc:
                max_dlugosc = dlugosc_biezaca
            dlugosc_biezaca = 2
            poprzedni_iloraz = obecny_iloraz

    if dlugosc_biezaca > max_dlugosc:
        max_dlugosc = dlugosc_biezaca

    return max_dlugosc if max_dlugosc > 2 else 0