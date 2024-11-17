def fun(n : int):
    equivalent = n
    reverse = 0

    while equivalent > 0:
        reverse = reverse * 10 + equivalent % 10 # zamiast 10 piszemy 2 dla systemu dwójkowego i tyle
        equivalent //= 10

    if reverse == n:
        print("palindrom")
    else:
        print("nie palindrom")

x = int(input())
fun(x)