from unittest.mock import numerics


def fibonacci_list(number : int) -> list:
    fib = [0 for _ in range(number+1)]
    fib[0] = fib[1] = 1 # 0 and 1 equals 1

    for i in range(2, number+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib
def fibonacci_no_list(number : int) -> None:
    a = 1 #index 0 of fib
    b = 1 #index 1 of fib
    c = None

    if number == 0:
        print(a)
    elif number >= 1:
        print(a, b, sep = '\n')

    for i in range(2, number+1):
        c = a + b
        a = b
        b = c
        print(c)

    print('\n')

def fibonacci_recursion(number : int):
    if number < 2:
        return 1
    else:
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)

def main():
    n = int(input())

    print("Fibonacci list:", fibonacci_list(n), end = '\n\n')

    print("Fibonacci no list:")
    fibonacci_no_list(n)

    print("Fibonacci recursion:", fibonacci_recursion(n), end = '\n')

main()