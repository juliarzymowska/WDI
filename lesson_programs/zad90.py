def new_number(number, mask):
    counter = 0
    k = 0  # new number

    while number > 0:
        if mask % 2 == 1:
            k += (number % 10) * (10 ** counter)
            counter += 1

        mask //= 2
        number //= 10

    return k


def zad90(number):
    l = len(str(number))
    ans = 0

    for mask in range(1, 2 ** l):
        new = new_number(number, mask)
        # print(new, end = '\n')
        if new % 7 == 0:
            ans += 1

    return ans


def main():
    a = int(input())
    print(zad90(a))
    # zad90(a)


main()
