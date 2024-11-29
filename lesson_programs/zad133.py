import random
from math import log10


def is_prime(number: int):
	if number < 2:
		return False
	i = 2
	while i * i <= number:
		if number % i == 0:
			return False
		i += 1
	return True


def z133(number: int):
	if int(log10(number)) + 1 >= 3:
	
	
	else:
		return None


def main():
	n = random.randint(1, 10000)
	print("N:", n)
	print(z133(n))
