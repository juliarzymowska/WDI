def newton_sqrt(n, epsilon):
    a = float(1)
    b = float(n)

    while abs(b - a) >= epsilon:
        a = (a + b) / 2
        b = n / a

    return (a + b) / 2

t = input()

for i in range(int(t)):
    a = int(input())
    e = int(input())
    print(newton_sqrt(a, e), end='\n')