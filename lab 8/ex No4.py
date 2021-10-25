"""
Функция должна принимать строку s и число k и возвращать все возможные комбинации из символов в строке s с длинами = k с
 повторениями (использовать itertools.combinations_with_replacement)
"""
import itertools

def get_combinations_with_r(s, n):
    for x in itertools.combinations_with_replacement(s, n):
        yield ''.join(sorted(x))

print(sorted(get_combinations_with_r("cat", 2)))