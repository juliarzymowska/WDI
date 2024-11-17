'''
Tablica jest wypełniona liczbami naturalnymi, które nie powtarzają się, należy znaleźć:

TAKIE 3 LICZBY, KTÓRE:
1) MAJĄ NWD == 1 (są względnie pierwsze)
2) przerwa między 1 a 2 a 3 powinna być nie większa niż 1
'''

def nwd(a, b):
    pom = None

    while b > 0:
        pom = b
        b = a%b
        a = pom
    #end while

    return a

def trojki(T):
    n = len(T)
    ans = 0

    for i in range(n-1):
        for j in range(i+1, i+3):
            if j < n and nwd(T[i], T[j]) == 1:
                for k in range(j+1, j+3):
                    if k < n and nwd(T[j], T[k]) == 1 and nwd(T[i], T[k]) == 1:
                        ans += 1

    return ans

def main():
    print(trojki([2, 4, 6, 7, 8, 10, 12]))  # 0 trójek
    print(trojki([2, 3, 4, 6, 7, 8, 10]))  # 1 trójka (3,4,7)
    print(trojki([2, 4, 3, 6, 5]))  # 2 trójki (2,3,5),(4,3,5)
    print(trojki([2, 3, 4, 5, 6, 8, 7]))  # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
    #trojki([2, 3, 4, 5, 6, 8, 7])
main()