def fun(year):
    minimum = year + 1
    para = (0, 0)

    for i in range(1, year//2 + 1):
        for j in range(i+1, year//2 + 1):
            if fib(i, j, year):
               if minimum > i + j:
                   minimum = i + j
                   para = (i, j)
    return para
def fib(a, b, year):
    while b < year:
        a, b = b, a+b
    return b == year

print(fun(2021))