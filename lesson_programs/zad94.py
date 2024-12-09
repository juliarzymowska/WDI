def ex94(n: int, t: list) -> bool:
    ok = True

    for i in range(n):
        ok = True
        for j in range(n):
            if not even_digit(t[i][j]):
                ok = False
                break

    return ok


def even_digit(number: int):
    while number > 0:
        if (number % 10) % 2 == 0:
            return True
        number //= 10
    return False


def main():
    n = int(input())
    tab = [[int(input()) for _ in range(n)] for _ in range(n)]
    print(ex94(n, tab))


main()
