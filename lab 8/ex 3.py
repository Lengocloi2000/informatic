"""
Реализуйте аналог функций zip, map, enumerate. ***
"""
## map
def add(x):
    return x+2

lst = [1,2,3,4,5,6]

def analis_map(function, iterable):
    for i in iterable:
        yield function(i)

for x in analis_map(add,lst):
    print(x)

## zip
number = [1,2,3,4]
str_number = ['one','two','three']
ord_number = ['first','second','third']

def analis_zip(*iterable):
    sentinal = object
    iterators = [iter(it) for it in iterable]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for  it in (iterators):
            value = next(it,sentinal)
            if value is sentinal:
                return
            values.append(value)
        yield tuple(values)
for x in analis_zip(number,str_number,ord_number):
    print(x)

## enumerate

ord_number = ['first','second','third','four','five']

def analis_enumerate(iterable,start = 1):
    n = start
    for i in iterable:
        yield n , i
        n += 1

for x in analis_enumerate(ord_number):
    print(*x)