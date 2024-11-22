from math import log10

def base_convertion_1(number : int, base : int):
    ans = ''
    cnt = 0
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    while number > 0:
        ans += hex[number%base]
        number //= base

    b = ''
    for i in range(len(ans)):
        b += ans[len(ans) - i - 1]

    return b

def base_convertion_string(number : int, base : int):
    if number > 0:
        base_convertion_string(number // base, base)
        print('0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'[number%base], end = '')

def base_convertion_list(number : int, base : int):
    l = int( log10(number) ) + 1
    t = [-1 for _ in range(l)]
    cnt = 0
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


    while number > 0:
        t[cnt] = number%base
        cnt += 1
        number //= base

    cnt -= 1

    while cnt>=0:
        print(hex[t[cnt]], end = '')
        cnt -= 1

def main():
    n = int(input()) # number
    b = int(input()) # base

    if n == 0:
        print(0)
    else:
        base_convertion_string(n,b)
        print('\n')
        print(base_convertion_1(n, b))
        base_convertion_list(n, b)

main()