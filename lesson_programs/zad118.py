import random

def ex118(t: list, w: list, n : int) -> tuple:
  for i in range(n):
    for j in range(n):
  :w

  return ()

def main():
  '''
  n = int(input()) #rozmiar szachownicy
  t = [[int(input()) for _ in range(n)] for _ in range(n)] #szachownica
  w = [int(input()) for _ in range(n)] #numery wierszy wież
  '''

  n = random.randint(2, 10)
  t = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]
  w = [random.randint(1, 20) for _ in range(n)]

  print(ex118(t, w, n))

main()