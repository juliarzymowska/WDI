import random


# ans = 0


def czy_zlozona(number):
    return True


def zad159(A, B, number):
    # global ans
    # nonlocal ans

    if A == 0 and B == 0:
        if not czy_zlozona(number):
            # ans += 1
            return 1
        return 0
    else:
        # p1 = p2 = 0
        x = 0
        if A > 0:
            # p1 = zad159(A - 1, B, number * 2 + 1)
            x += zad159(A - 1, B, number * 2 + 1)
        if B > 0:
            # p2 = zad159(A, B - 1, number * 2)
            x += zad159(A, B - 1, number * 2)

    return x


# return ans
# return p1 + p2

def main():
    ans = 0
    A = random.randint(1, 5)
    B = random.randint(1, 5)
    zad159(A - 1, B, 1)
    # print(ans)
    return ans


main()
