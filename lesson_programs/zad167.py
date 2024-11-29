samogloski = 'aeiouy'


def index(word) -> tuple:  # indeksy samoglosek
	pos1 = -1
	pos2 = -1
	
	for i in range(len(word)):
		if word[i] in samogloski:
			if pos1 == -1:
				pos1 = i
			else:
				pos2 = i
	
	return pos1, pos2


def zad167(word):
	pos = index(word)
	
	if pos[1] == -1:
		return 1
	
	suma = 0
	
	for k in range(pos[0], pos[1] + 1):
		suma += zad167(word[k+1:])
	
	return suma

def main():
	word = input()
	print(zad167(word))
	
main()