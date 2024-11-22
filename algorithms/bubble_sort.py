def bubble_sort(t : list) -> list:
    n = len(t)

    for i in range(n):
        for j in range (1, n-i):
            if t[j] < t[j-1]: #sorting in ascending order
                t[j], t[j-1] = t[j-1], t[j]
        #end for
    #end for

    return t

def main():
    print(bubble_sort([10, 2, 13, 7, 9, 12, 3, 19]))

main()