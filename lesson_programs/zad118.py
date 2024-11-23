import random


def zad118(t: list, w: list, n : int) -> tuple:
	ans = ()
	sum_column = [0] * n
	
	for i in range(n): #kolumny
		for j in range(n): #wiersze
			sum_column[i] += t[j][i]
	
	mini1 = float('inf')
	mini2 = float('inf')
	
	for i in range(n): # kolumny
		sum_column[i] -= w[i]
	
	return ans


def main():
	n = random.randint(2, 10)  # rozmiar szachownicy
	t = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]  # szachownica
	w = [random.randint(1, 20) for _ in range(n)]  # numery wierszy wież


main()
