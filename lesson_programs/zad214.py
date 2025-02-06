import random


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def insert(root, value): # wstawianie elementu do drzewa!@
	if root is None:
		return Node(value)
	if value < root.value:
		root.left = insert(root.left, value)
	else:
		root.right = insert(root.right, value)
	return root


def tree_print(root):
	if root is None:
		return
	tree_print(root.left)
	print(root.value, end=" ")
	tree_print(root.right)


def tree_exists(root, x):
	if root is None:
		return False
	if root.value == x:
		return True
	
	return tree_exists(root.left, x) or tree_exists(root.right, x)


def tree_height(root, cnt=0):  # liczba poziomów w drzewie
	if root is None:
		return 0
	
	if root.right is not None:
		tree_height(root.right, cnt + 1)
	
	return cnt


def tree_size(root, cnt=0):  # liczba węzłów w drzewie
	if root is None:
		return 0


def main():
	n = random.randint(1, 50)
	print(f"Rozmiar drzewa: {n}")
	root = None
	
	for _ in range(n):
		value = random.randint(1, 100)
		root = insert(root, value)
	
	print("Elementy drzewa w kolejności in-order:")
	tree_print(root)
	print("\n", tree_exists(root, 3))


if __name__ == "__main__":
	main()
