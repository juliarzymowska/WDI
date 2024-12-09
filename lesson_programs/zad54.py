# ja bym to zrobiła inaczej lol


# można używać tablic, zakładamy że a < b
'''
1 / 6 = 0,1 666
bo 1 / 6 = 0 reszta 1
do 1 dopisujemy 0, czyli mamy 10
10 / 6 = 1 i 4r
4r dopisujemy 0, czyli mamy 40
40 / 6 = 6 i 4r
itd..

długość okresu może osiągać co najwyżej b (a/b), czyli w tym wypadku 6 to maksymalny okres
'''

'''def rozwiniecie_dziesietne(a, b): #zajecia
    tab = [0 for _ in range(b+1)] #reszta z dzielenia
    tab1 = [0 for _ in range(b+1)] #liczby

    for i in range(b+1):
        a *= 10
        tab[i] = a%b
        tab1[i] = a//b
        a %= b

        if tab[i] == 0: # brak okresu
            break


a = int(input())
b = int(input())
rozwiniecie_dziesietne(a, b)'''

'''
def rozwinięcie_dziesiętne(a, b): #chatgpt rozwiazanie
    # Obliczamy część całkowitą
    część_całkowita = a // b
    wynik = str(część_całkowita) + "."

    # Obliczamy resztę
    reszta = a % b
    reszty_widziane = {}

    # Pętla do obliczania części ułamkowej
    część_ułamkowa = ""
    pozycja = 0

    while reszta != 0:
        # Sprawdzamy czy reszta się powtarza
        if reszta in reszty_widziane:
            # Powtarzająca się reszta oznacza początek okresu
            indeks_startu = reszty_widziane[reszta]
            część_ułamkowa = (
                    część_ułamkowa[:indeks_startu] + "(" + część_ułamkowa[indeks_startu:] + ")"
            )
            break

        # Zapisujemy pozycję bieżącej reszty
        reszty_widziane[reszta] = pozycja

        # Mnożymy resztę przez 10 i zapisujemy część całkowitą wyniku dzielenia
        reszta *= 10
        cyfra = reszta // b
        część_ułamkowa += str(cyfra)

        # Aktualizujemy resztę
        reszta = reszta % b
        pozycja += 1

    wynik += część_ułamkowa
    return wynik


# Wczytywanie licznika i mianownika
a = int(input("Podaj licznik (liczbę naturalną): "))
b = int(input("Podaj mianownik (liczbę naturalną): "))

# Wypisywanie rozwinięcia dziesiętnego
print("Rozwinięcie dziesiętne ułamka:", rozwinięcie_dziesiętne(a, b))
'''


def fractorial_expansion():
    a = int(input())
    b = int(input())

    czesc_calkowita = str(a // b)
    wynik = czesc_calkowita + "."

    reszta = a % b
    zbior_reszt = [-1 for _ in range(b + 1)]  # maksymalna długość okresu wynosi b
    czesc_ulamkowa = ''
    i = 0  # pozycja w tablicy zbior_reszt

    while reszta != 0:
        if reszta in zbior_reszt:
            j = 0
            while zbior_reszt[j] != reszta:
                j += 1
            # end while

            czesc_ulamkowa = str(
                czesc_ulamkowa[:j] + '(' + czesc_ulamkowa[j:] + ')'
            )
            # print(czesc_ulamkowa[j:], end = '\n')
            break
        # end if

        zbior_reszt[i] = reszta  # zapisujemy reszte do tablicy reszt

        while reszta < b:  # zwiekszamy tak dlugo az reszta bedzie > b
            reszta *= 10
        # end while

        cyfra = reszta // b  # cyfra, ktora dodajemy do czesci ulamkowej
        czesc_ulamkowa += str(cyfra)
        reszta %= b  # wyznaczamy kolejna reszte
        # print(zbior_reszt[i], end = '\n')
        i += 1
    # end while

    wynik += czesc_ulamkowa
    return wynik


print(fractorial_expansion())
