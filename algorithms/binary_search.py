def binary_search(t : list, number : int) -> int:
    n = len(t)
    r = n - 1 #index of last element of t
    l = 0 #index of first element of t

    while l <= r:
        m = (l + r) // 2 #middle index of t

        if number == t[m]:
            return m #we found that t[m] == number
        elif number > t[m]:
            l = m + 1
        else:
            p = m - 1
    #end while

    return -1 # didnt found the number
def main():
    #l = []
    #l = input()
    print(binary_search([1, 2, 5, 7, 9, 12, 14, 19], 14))

main()