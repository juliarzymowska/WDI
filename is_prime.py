def is_prime(number : int) -> int:
    if number <= 2:
        return True
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
    #end while

    return True

def main():
    a = int(input())
    print(is_prime(a))

main()