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

def main():
    a = int(input())
    print(is_prime(a))

main()