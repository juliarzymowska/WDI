from math import sqrt

def sito_eratostenesa(n): #chyba nie działa ??
    tab = [0 for _ in range(n + 1)]

    for i in range(2, int(math.sqrt(n+1))):
        if tab[i] == 0:
            for j in range(i*i, n+1, i):
                tab[j] = 1


    for i in range(1, n+1):
        if tab[i] == 0:
            print(i)

def tablica(n): #dobre
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False

    for i in range(2, int( sqrt(n) ) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    for i in range(2, n):
        if primes[i]:
            print(i, end=' ')

N = int(input())
#sito_eratostenesa(N)
tablica(N)