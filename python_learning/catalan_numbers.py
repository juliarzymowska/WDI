def catalan(n : int):
    if n == 0:
        return 1
    else:
        return catalan(n-1)*(4*(n-1)+2)/((n-1)+2)

j = 0
even = 0

while True:
    print(j, catalan(j))

    if catalan(j) % 2 == 0:
        even += 1

    j += 1
    
    if catalan(j) > 1000000:
        break

print(f"Liczby parzyste: {even} i nieparzyste: {j - even}")