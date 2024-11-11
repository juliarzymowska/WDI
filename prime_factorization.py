def prime_factorization(number : int) -> None:
    i = 2

    while i*i <= number:
        while number % i == 0:
            print(i, end = ' ')
            number //= i
        i += 1

    if number > 1:
        print(number)

def main():
    n = int(input())
    prime_factorization(n)

main()