def zad134(waga, p1=[], p2=[], p3=[], pos=0) -> bool:

  if sum(p1) == sum(p2) == sum(p3) and pos == len(waga)-1:
    return True

  if pos >= len(waga):
    return False

  return zad134(waga, p1+[waga[pos]], p2, p3, pos+1) or zad134(waga, p1, p2+[waga[pos]], p3, pos+1) or zad134(waga, p1, p2, p3+[waga[pos]], pos+1)


print(zad134(waga=[1,2,3,4,5,6,7,8,9]))