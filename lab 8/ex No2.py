"""
Написать функцию, принимающую строку s и число n и возвращающую всевозможные перестановки из n символов
в s строке в лексикографическом(!) порядке (использовать itertools.permutations)
"""
import itertools

def get_permutations(s, n):
    for x in itertools.permutations(s, n):
        yield ''.join(x)

print(sorted(get_permutations("cat", 2)))
