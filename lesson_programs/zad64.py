def zajecia():
    tab = [0 for _ in range(10)]

    while True:
        x = int(input())

        if x == 0:
            break
        if x > tab[0]:
            i = 0
            while i < 9 and tab[i] < x:
                tab[i] = tab[i + 1]
                i += 1
            if tab[9] < x:
                tab[9] = x
            else:
                tab[i - 1] = x

    print(tab[0])


'''
def moja(): # źle, bo tylko dla cyfr, a tu chodzi o liczby naturalne
    Tab = [0 for _ in range(10)]

    while True:
        a = int(input())

        if a == 0:
            break

        Tab[a] += 1

    suma = 0
    for i in range(9, -1, -1):
        suma += Tab[i]

        if suma == 10:
            print(i)
            break
'''


# zajecia()

def moja_poprawiona():
    tab = [-1 for _ in range(
        10)]  # wypełniamy tablice -1, bo to nie jest liczba naturalna, więc wtedy wiemy czy wstawiliśmy już na tym indeksie jakąś liczbę
    # print(tab, end='\n')

    while True:
        a = int(input())

        if a == 0:
            break

        for i in range(10):
            if tab[i] < a:
                if tab[i] != -1:
                    for j in range(9, i, -1):
                        tab[j] = tab[j - 1]
                tab[i] = a
                break

        # print(f"{tab}", end='\n')

    return tab[
        9]  # zwracamy ostatni indeks tablicy, bo sortujemy rosnąco, zatem 10 co do wielkości wartość jest na ostatnim indeksie tablicy


print(moja_poprawiona())
# moja_poprawiona()
