def z135(t, w, k, s): #ruch króla, t - szachownica, w - wiersz, k - kolumna, s - koszt drogi
  global mini

  if w == 7:
    mini = min(mini, s+t[w][k])
    return

  z135(t, w+1, k, s+t[w+1][k])
  if k+1 < len(t):
    z135(t, w+1, k+1, s+t[w+1][k+1])
  if k-1 >= 0:
    z135(t, w+1, k-1, s+t[w+1][k-1])

def main():
  # do dokończenia na wdi

main()