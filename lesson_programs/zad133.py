import random

ans = []


def is_prime(number: int):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def zad133(number: str):
    global ans
    # print(number)

    if len(number) > 1 and is_prime(int(number)) and number not in ans:
        print(number)
        ans.append(number)

    for i in range(len(number)):
        zad133(number[:i] + number[i + 1:])


def main():
    n = random.randint(1, 100000)
    # n = 1511
    print("N:", n)
    zad133(str(n))


main()
