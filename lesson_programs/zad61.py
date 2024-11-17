def fun(a, b):
    tab = [0 for i in range(10)]

    while a > 0:
        tab[a % 10] += 1
        a //= 2

    while b > 0:
       tab[b % 10] -= 1
       b //= 2

    for i in range(10):
        if tab[i] != 0:
            return False
    return True


A = int(input())
B = int(input())

print(fun(A,B))