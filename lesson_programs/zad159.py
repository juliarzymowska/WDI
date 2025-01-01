import random

cnt = 0


def is_prime(number: int):
    if number < 2:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    return True


def test(number: int, a: int, b: int, i: int):  # i - index of ans
    global cnt
    if a == b == 0 and not is_prime(number):
        cnt += 1

    if a > 0:
        test(number + 2 ** i, a - 1, b, i - 1)
    if b > 0:
        test(number, a, b - 1, i - 1)


def main():
    a = random.randint(1, 3)  # number of 1
    b = random.randint(1, 3)  # number of 0

    print(f"a: {a}, b: {b}")
    test(2 ** (a + b - 1), a - 1, b, a + b - 2)  # a-1, because the oldest bit has to be == 1, so ans == 2**(a+b-1)
    print(cnt)


main()
