import random


def is_prime(number: int):
    if number < 2:
        return False
    i = 2

    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    return True


def divide_recursive(s: str, parts: list):
    if not s:
        return is_prime(len(parts))

    for i in range(len(s) - 1, -1, -1):
        if is_prime(int(s[i:])):
            if divide_recursive(s[:i], parts + [int(s[i:])]):
                return True

    return False


def main():
    n = random.randint(1, 100000)
    # n = 2255
    print(n, divide_recursive(str(n), []))


main()
