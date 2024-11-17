
#hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'] - do systemu 16


def bin(num):
    tab = [0 for i in range(64)]
    i = 0

    while num > 0:
        tab[i] = num%2 #zamiana 2 na p - wtedy taka podstawa jak p
        num //= 2
        i += 1

    i -= 1
    while i >= 0:
        #print(hex[tab[i]],end="")
        print(tab[i],end=" ")
        i -= 1
    print()

n = int(input())
bin(n)