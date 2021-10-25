"""
В функцию передается список списков. Нужно вернуть максимум, который достигает выражение $(a_1^2 + a_2^2 + ... + a_n^2) % m $. Где ai --- максимальный элемент из i-ого списка
(использовать функцию из itertools)
"""
import itertools
def maximize(lists, m):
    new_list =[]
    new =[]
    for x in itertools.starmap(max,lists):
        new_list.append(x**2)
    for i in itertools.accumulate(new_list):
        new.append(i)
    return max(new)%m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))

