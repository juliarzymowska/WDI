def ex93(n : int, t : list) -> bool:
    cnt = 0

    for i in range(n):
        for j in range(n):
            if odd_digits(t[i][j]):
                cnt += 1
                break

    return cnt == n

def odd_digits(number : int):
    ok = True

    while number > 0:
        if (number%10) % 2 != 0:
            ok = False
            return ok
        number //= 10

    return ok

def main():
    ex93(int(input()))

main()