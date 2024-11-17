def cosinus(x, n):
    ans = 1
    fac = 1
    x2n = 1

    for i in range(1, n + 1):
        x2n *= (-1) * (x ** 2)
        fac *= ((2 * i) * (2 * i - 1))
        ans += x2n / fac

    print(ans)


x = int(input())
n = int(input())
cosinus(x, n)