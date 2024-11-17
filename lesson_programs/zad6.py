def newton_sqrt(epsilon : float, n : float):
    a = float(1) # pierwszy bok kwadratu
    b = float(n) # drugi bok kwadratu

    while abs(a-b) >= epsilon:
        a = (a + b) / 2
        b = n / a

    return (a + b) / 2

n = int(input())
epsilon = float(input())
print(newton_sqrt(epsilon, n))