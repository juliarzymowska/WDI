def is_prime(a: int):
    if a < 2:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True


def check_mask(mask, number):
    counter = 0

    while mask > 0:
        if mask % 2 == 1:
            counter += 1
        mask //= 2

    return counter == len(str(number))


def new_number(a: int, b: int, mask):
    n = 0  # new number
    counter = 0
    length = len(str(a) + str(b))

    while counter != length:
        if mask % 2 == 0:
            n += (a % 10) * (10 ** counter)
            a //= 10
        else:
            n += (b % 10) * (10 ** counter)
            b //= 10

        mask //= 2
        counter += 1
    return n


def main():
    p = input()
    q = input()

    length = len(str(p) + str(q))

    ans = 0
    r = None  # new number from p and q

    for mask in range(1, 2 ** length):
        if check_mask(mask, p):
            r = new_number(int(p), int(q), mask)
            if is_prime(r):
                # print(r, end = ' ')
                ans += 1
    return ans


print(main())
