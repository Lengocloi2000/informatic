"""
Написать функцию, принимающую 2 списка и возвращающую декартово произведение (использовать itertools.product)
"""
import itertools
def get_cartesian_product(a, b):
    for x, y in itertools.product(a, b):
        yield (x,y)

print(list(get_cartesian_product([1, 2], [3,4])))
