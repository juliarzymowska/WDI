def find_partitions(n, max_part=None):
    """
    Znajduje wszystkie możliwe podziały liczby n na sumę składników.

    :param n: Liczba naturalna do podziału.
    :param max_part: Maksymalna wartość składnika w bieżącym kroku (dla porządku nierosnącego).
    :return: Lista list, gdzie każda podlista to jeden podział.
    """
    if n == 0:
        return [[]]  # Pusty podział dla liczby 0.
    if max_part is None:
        max_part = n
    
    partitions = []
    for i in range(min(max_part, n), 0, -1):  # Iterujemy od największego możliwego składnika.
        for sub_partition in find_partitions(n - i, i):  # Rekurencja z pomniejszoną liczbą i mniejszym max_part.
            partitions.append([i] + sub_partition)
    return partitions


def print_partitions(n):
    """
    Wypisuje wszystkie podziały liczby n w postaci sum składników.

    :param n: Liczba naturalna.
    """
    partitions = find_partitions(n)
    for partition in partitions:
        print(" + ".join(map(str, partition)))


# Przykład użycia
n = 6
print_partitions(n)