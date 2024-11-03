from math import sqrt

def sieve(n : int):
    primes = [True for _ in range(n+1)] # ustawioamy wszystkie liczby jako pierwsze
    primes[0] = primes[1] = False # 0 i 1 to nie są liczby pierwsze
    ans = 0
    for i in range (2, int( sqrt(n) ) + 1, 1):
        if primes[i] != 0:
            for j in range(i*i, n+1, i):
                primes[j] = False
            #end for
        #end if
    #end for

    return primes

def main():
    #T = int(input())
    print(sieve(100))

main()