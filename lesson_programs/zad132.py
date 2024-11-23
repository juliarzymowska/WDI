def newton(n: int, k: int) -> int:
	if k == 0 or k == n:
		return 1
	if k < 0 or k > n:
		return 0
	
	return newton(n - 1, k - 1) + newton(n - 1, k)


def main():
	print(newton(int(input()), int(input())))


main()
