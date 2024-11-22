'''
program algorytmem zachłannym:
- kładziemy najcięższy odważnik tak, aby nie przeważył szalki
- odważniki tylko na 1nej szalce

Pyt: czy da się odważyć dany ciężar??? (n - ciężar)
nie działa dla [1,3,5,10,16,24], bo wszystkie poprzednie indeksy muszą być < od kolejnego.
działałoby dla: [1,3,5,10,20,40] (1+3 < 5, 1+3+5 < 10, 1+3+5+10 < 20, 1+3+5+10+20 < 40)
'''
def odwazniki_zachlanne(t, n) -> bool: #t - tablica odważników, n - ciężar

  for i in range(len(t)-1, -1, -1):
    if n >= t[i]:
      n-=t[i]
      if n == 0:
        return True

  return False

'''
program rekurencyjny:
odpowiada na pytanie: czy da się odważyć 26g zaczynając od odważnika 0
'''

def odwazniki_rekurencyjnie(t, n, p=0) -> bool: #tablica, ciężar, pozycja

  if n == 0:
    return True
  if n < 0 or p >= len(t):
    return False

  return odwazniki_rekurencyjnie(t, n - t[p], p+1) or odwazniki_rekurencyjnie(t, n, p+1) # rekurencja z nawrotem

def main():
  t = [1, 3, 5, 10, 16, 24, 40]
  n = 26
  print(odwazniki_zachlanne(t, n))
  print(odwazniki_rekurencyjnie(t, n))

main()