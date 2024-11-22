'''
drzewo trinarne
w wersji hard możemy kłaść odważniki na obie szalki, a nie tylko na jedną
'''
def odwazniki_rekurencyjnie_obie_szalki(t, n, p=0):
  if n == 0:
    return True
  if p == len(t):
    return False
  return odwazniki_rekurencyjnie_obie_szalki(t, n - t[p], p+1) or odwazniki_rekurencyjnie_obie_szalki(t, n, p+1) or odwazniki_rekurencyjnie_obie_szalki(t, n+t[p], p+1)
def waga(t, n, p=0, r=[]): #funkcja zwracająca jakie odważniki mają leżeć na której szalce, r - result to tablica, która przetrzymuje jakie odważniki wzięliśmy
  #print('*', end='')

  if n == 0:
    print(r)
    return
  if p >= len(t):
    return

  waga(t, n-t[p], p+1, r+[t[p]])
  waga(t, n, p+1, r)
  waga(t, n+t[p], p+1, r+[-t[p]])
  #r+[t[p]] - dodawanie listy, bo .append() dodaje jakby na "stałe", a tak to w przypadku nawrotu nie ma problemu

def main():
  t = [1, 3, 5, 10, 16, 24]
  n = 26

  #print(odwazniki_rekurencyjnie_obie_szalki(t, n))
  print(waga(t, 23))
  #print(waga([1, 3, 9, 27], 23))
  #print(waga([1,3,9,27,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 23))
main()