from math import log10

def zad101(T):
    l = len(T) # to samo co len(T[0]) - liczba kolumn, bo macierz jest kwadratowa
    # len(T) - liczba wierszy

    wiersze = [False for _ in range(l)]
    kolumny = [False for _ in range(l)]

    for i in range(l):
        for j in range(l):
            if T[i][j] == 0:
                wiersze[i] = True
                kolumny[j] = True
                break

    for i in range(l):
        if wiersze[i] == False or kolumny[i] == False:
            return False
    return True

def main():
    T = []
    print(zad101(T))

main()
