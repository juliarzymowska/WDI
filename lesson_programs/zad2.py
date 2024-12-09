def fib():
    a = 1  # pierwszy wyraz ciągu
    b = 1  # drugi wyraz ciągu

    print(a, b, sep="\n")

    while True:
        a, b = b, a + b
        if b > 1000000:
            break
        print(b)


fib()
