def gcd(num1 : int, num2 : int) -> int:
    temp = None

    while num2 > 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    #end while

    return num1
def main():
    a = int(input())
    b = int(input())

    print(gcd(a, b))
    print(a*b/gcd(a,b)) #nww
main()