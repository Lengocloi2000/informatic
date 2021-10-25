"""
Реализовать функцию get_combinations. Должна принимать строку s и число k и возвращать все возможные комбинации
из символов в строке s с длинами <= k (использовать itertools.combinations)
"""
import itertools

def get_combinations(s, k):
    my_list = []
    for n in range(1, k + 1):
        new_list = []
        for x in itertools.combinations(s, n):
            new_list.append(''.join(sorted(x)))
        my_list.extend(sorted(new_list))
    print(my_list)

get_combinations("cat", 2)