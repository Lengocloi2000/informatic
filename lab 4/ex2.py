'''Напишите функцию, которая получает на вход список чисел и выдает ответ сколько в данном списке четных чисел.
 Напишите декоратор, который меняет поведение функции следующим образом: если четных чисел нет, 
 то пишет "Нет(" а если их больше 10, то пишет "Очень много"
'''

def decorator_even_number(func):
    def wrapper(*args,**kwargs):
        val = func(*args,**kwargs)
        if val == 0 :
            return 'Нет'
        elif val > 10:
            return 'очень много'
        else:
            return val
    return wrapper

@decorator_even_number
def count_even_number(A):
    count = 0
    for x in A:
        if x % 2 == 0:
            count += 1
    return count

A = list(map(int,input().split()))
print(count_even_number(A))





