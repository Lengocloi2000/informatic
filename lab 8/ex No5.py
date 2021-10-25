"""
Написать функцию, которая подсчитывает количество подряд идующих символов в строке
 (использовать itertools.groupby)
"""
import itertools

def compress_string(s):
    for x,y in itertools.groupby(s):
        yield (len(list(y)),int(x))

print(list(compress_string('1222311')))