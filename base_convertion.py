def base_convertion(number : int, base : int):
    if number > 0:
        base_convertion(number // base, base)
        print('0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'[number%base], end = '')

def main():
    n = int(input()) # number
    b = int(input()) # base

    if n == 0:
        print(0)
    else:
        base_convertion(n,b)

main()