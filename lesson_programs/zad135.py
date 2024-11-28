import random

mini = float('inf')


def wersja1(t, w, k, s):  # ruch króla, t - szachownica, w - wiersz, k - kolumna, s - koszt drogi
	global mini
	
	if w == 7:
		mini = min(mini, s + t[w][k])
		return
	
	wersja1(t, w + 1, k, s + t[w + 1][k])
	if k + 1 < len(t):
		wersja1(t, w + 1, k + 1, s + t[w + 1][k + 1])
	if k - 1 >= 0:
		wersja1(t, w + 1, k - 1, s + t[w + 1][k - 1])


def wersja2(t, w, k):
	if k < 0 or k == 8:
		return float('inf')
	
	if w == 7:
		return t[7][k]
	
	return min(wersja2(t, w + 1, k), wersja2(t, w + 1, k + 1), wersja2(t, w + 1, k - 1)) + t[w][k]


def main():
	t = [[random.randint(1, 5) for _ in range(8)] for _ in range(8)]
	
	print(wersja1(t, 0, 0, t[0][0]))
	print(wersja2(t, 0, 0))


main()
