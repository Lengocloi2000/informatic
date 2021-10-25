"""
Вам дана функция на языке python:
def print_map(function, iterable):
    for i in iterable:
        print(function(i))
Требуется переписать данную функцию не используя цикл for.
"""

def function(x):
    return x ** 2

def print_map(function, iterable):
    iter_obj = iter(iterable)
    while True:
        try:
            print(function(next(iter_obj)))
        except StopIteration:
            break


print_map(function, [1, 2, 3, 4])
