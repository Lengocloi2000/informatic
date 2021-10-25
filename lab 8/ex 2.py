"""
Напишите генератор, выводящий первые n чисел Фибоначчи.
"""
def fibo(n):
    count = 1
    fib_1,fib_2 = 0,1
    while count<=n:
        yield fib_1
        fib_1 , fib_2 = fib_2, fib_1+fib_2
        count+=1

for x in fibo(11):
    print(x)















