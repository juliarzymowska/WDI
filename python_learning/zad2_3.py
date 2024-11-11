def zad2(a : int, b : int):
    '''a = sorted(a)
    b = sorted(b)

    if a == b:
        return True
    else: return False'''
    if len(a) != len(b):
        return False
    
    numbers_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numbers_b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while a > 0:
        numbers_a[a%10] += 1
        a //= 10

    while b > 0:
        numbers_b[b%10] += 1
        b //= 10

    if numbers_a == numbers_b:
        return True
    else:
        return False

a = int(input())
b = int(input())

print(zad2(a, b))