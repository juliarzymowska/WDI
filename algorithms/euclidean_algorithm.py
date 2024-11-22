def gcd(num1 : int, num2 : int) -> int:
    temp = None #pom

    while num2 > 0:
        temp = num2 # pom = b
        num2 = num1 % num2 # b = a%b
        num1 = temp # a = pom
    #end while

    return num1
def main():
    a = int(input())
    b = int(input())

    print(gcd(a, b))
    print(a*b/gcd(a,b)) #nww
main()