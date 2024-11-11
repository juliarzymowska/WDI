'''
Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczym 2 liczb o najmniejszej różnicy. Np. 30 = 5 * 6, 120 = 10 * 12
'''

import math

def zad6(a : float):
    for i in range (int(math.sqrt(a)), 0, -1):
        if a % i == 0:
            return i, a//i

a = int(input())
print(zad6(a))