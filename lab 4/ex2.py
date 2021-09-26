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





