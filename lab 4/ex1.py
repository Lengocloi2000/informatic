# Напишите консольную программу, которой на вход подается единственное число N (без имени или с именем -n),
# а программа печатает значение Nго числа Фибоначчи
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n')

    return parser

def fibo(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    print (fibo(int(namespace.n)))