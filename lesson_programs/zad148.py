def hetman(t: list, x=0, p1=[], p2=[], k=[]):
    if x == 8:
        print(t)
        exit()

    for i in range(8):
        if check(x, i, p1, p2, k):
            t[x] = i
            k[i] = True
            p1[x + 1] = True
            p2[x - i] = True
            hetman(t, x + 1, p1, p2, k)  # jeśli dla wszystkich kombinacji return
            k[i] = p1[x + i] = p2[x - i] = False


def check(x, y, p1, p2, k):
    return p1[x + y] == False and k[y] == False and p2[x - y] == False
