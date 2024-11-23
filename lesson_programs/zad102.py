import random


def same_digits(number: int) -> list:
	tab = []
	
	while number > 0:
		tab.append(number % 10)
		number //= 10
	
	return tab


def zad102(t: list) -> int:
	ans = 0
	n = len(t)
	digits = [[0 for _ in range(n)] for _ in range(n)]
	
	for i in range(n):
		for j in range(n):
			digits[i][j] = same_digits(t[i][j])
	
	for i in range(n):
		for j in range(n):
			if i + 1 < n and j + 1 < n:
				if digits[i][j] == digits[i + 1][j + 1]:
					ans += 1
			if i + 1 < n and j - 1 >= 0:
				if digits[i][j] == digits[i + 1][j - 1]:
					ans += 1
			if i - 1 >= 0 and j + 1 < n:
				if digits[i][j] == digits[i - 1][j + 1]:
					ans += 1
			if i - 1 >= 0 and j - 1 >= 0:
				if digits[i][j] == digits[i - 1][j - 1]:
					ans += 1
	
	return ans


def main():
	n = random.randint(2, 10)
	t = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
	
	for row in t:
		print(row)
	
	print(zad102(t))
	
main()