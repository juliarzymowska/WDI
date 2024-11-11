LL = [[3, 5, 7], [2, 4, 8]]
Ans = [x**2 for L in LL for x in L]

print(Ans)

osoby = [('ola', 18), ('ania', 4), ('kasia', 21)]

pelnoletnie = [x for (x,y) in osoby if y >= 18]
print(pelnoletnie)


K = [x**2 for x in range(100) if (x**2)%10 == 6]
print(K[1:6])