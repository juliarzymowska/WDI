import random


def zad138(t: list, ans=[], ans_pos=[], pos=0):
    if sum(ans) == sum(ans_pos) and len(ans) > 0:
        return ans, ans_pos
    if pos == len(t):
        return None
    return zad138(t, ans + [t[pos]], ans_pos + [pos], pos + 1) or zad138(t, ans, ans_pos, pos + 1)


def main():
    n = random.randint(2, 10)
    t = [random.randint(1, 5) for _ in range(n)]

    print(t)
    print(zad138(t))


main()
