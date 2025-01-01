import random

vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def ascii_sum(word: str) -> int:
	ans = 0
	for i in range(len(word)):
		ans += ord(word[i])  # changes to int from str
	return ans


def vowels_sum(word: str) -> int:
	global vowels
	
	ans = 0
	for i in range(len(word)):
		if word[i] in vowels:
			ans += 1
	return ans


def words(size: int) -> str:
	w = ""
	for i in range(size):
		w += chr(random.randint(97, 122))  # only lower case letters
	return w


def zad149(s: str, ans: str, vowels_s1: int, ascii_s1: int):
	if vowels_s1 == ascii_s1 == 0:
		return ans
	
	for i in range(len(s)):
		if ord(s[i]) <= ascii_s1:
			if s[i] in vowels and vowels_s1 > 0:  # if s[i] is a vowel and there are still vowels to be used
				temp = zad149(s[i + 1:], ans + s[i], vowels_s1 - 1, ascii_s1 - ord(s[i]))
				if temp != "":  # if ans is not empty
					return temp
			elif s[i] not in vowels:  # if s[i] is not a vowel
				temp = zad149(s[i + 1:], ans + s[i], vowels_s1, ascii_s1 - ord(s[i]))
				if temp != "":  # if ans is not empty
					return temp
	
	return False


def main():
	n1 = random.randint(5, 15)  # size of s1
	n2 = random.randint(5, 15)  # size of s2
	s1 = words(n1)
	s2 = words(n2)
	
	ascii_ = ascii_sum(s1)  # sum of ascii in s1
	vowels_ = vowels_sum(s1)  # number of vowels in s1
	
	print(f"S1: {s1}, S2: {s2}, sum of ascii code S1: {ascii_}, sum of vowels in S1: {vowels_}")
	print(zad149(s2, "", vowels_, ascii_))


main()
