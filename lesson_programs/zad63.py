def liczba_e():  # wersja dla (a)społecznych
    e = 1
    n = 1
    w = 1  # nastepny wyraz ciagu

    while w > 0:
        e += w
        n += 1
        w /= n
    return e


# liczba_e()

def Liczba_e(n):  # zajecia 'zaawansowana wersjs'
    e = [0 for _ in range(n)]  # o 1 za mało, bo to łatwiejsza wersja
    w = [0 for _ in range(n)]

    e[0] = 1
    w[0] = 1
    n = 1
    b = True

    while b:
        b = False
        p = 0
        for i in range(n - 1, -1, -1):
            s = e[i] + w[i] + p
            p = s // 10
            e[i] = s % 10

        n += 1

        r = 0
        for i in range(0, n - 1):  # dodawanie pod kreską
            r = r * 10 + w[i]
            w[i] = r // n
            r %= n
            if w[i] > 0:
                b = True

    return e
