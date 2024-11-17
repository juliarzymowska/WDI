def zad55():
    a = int(input())
    b = int(input())

    tab_a = [0 for _ in range(16)]
    tab_b = [0 for _ in range(16)]

    for i in range(2, 17):
        pom_a = a
        pom_b = b

        while pom_a > 0: #konwersja do tablicy liczby a
            tab_a[pom_a%i] += 1
            pom_a //= i

        while pom_b > 0: # konwersja do tablicy liczby b
            tab_b[pom_b%i] +=1
            pom_b //=i

        print(i, "  ", tab_a, tab_b, sep=' ', end='\n')

        ok = True #zakladamy ze istnieje
        podstawa = i

        for j in range(16):
            if tab_b[j] > 0 and tab_a[j] > 0:
                ok = False # nie istnieje
            tab_a[j] = tab_b[j] = 0 #resetowanie tablic

        if ok:
            return ok, podstawa
    return ok

print(zad55())