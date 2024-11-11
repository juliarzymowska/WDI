import math

def quadratic_formula(a, b, c):
    delta = float(b**2 - 4*a*c)
    #if delta < 0:
        #print("Brak rozwiązań")
        #return None, None
    #elif delta == 0:
        #x1 = float(-b/2*a)
        #print(f"Jedno rozwiązanie: {x1}")
        #return x1, None
    #else:
    if delta >= 0:
        x1 = float(-b-math.sqrt(delta)/2*a)
        x2 = float(-b+math.sqrt(delta)/2*a)
        #print(f"Dwa rozwiązania: {x1} i {x2}")
        return x1, x2
    return None, None

a=int(input())
b=int(input())
c=int(input())
#quadratic_formula(a,b,c)

x1, x2 = quadratic_formula(a,b,c)

print(x1, x2)