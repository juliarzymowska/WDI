from math import sqrt, log10

def is_prime(number : int) -> int:
    if number < 2:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    #end while

    return True

def different_digits(number : int) -> bool:
    check = [False for _ in range(10)]

    while number > 0:
        if check[number%10]:
            return False
        #end if
        check[number%10] = True
        number //= 10
    #end while

    return True

def number_cut(number : int, M : int, N : int, l : int) -> int:
    number %= 10**(l-M)
    number //= 10**N

    return number

def new_number(number : int):
    l = int( log10(number) ) + 1
    ans = 0

    for M in range(l):
        for N in range(l-M):
            new = number_cut(number, M, N, l)
            #print(new)
            if is_prime(new) and different_digits(new):
                ans = max(ans, new)

    return ans

def main():
    a = 1202742516
    print(new_number(a))
    #new_number(a)

main()