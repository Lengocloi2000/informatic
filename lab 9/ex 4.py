'''
От некоторого устройства в режиме реального времени приходят данные. Необходимо написать сопрограмму,
которая вычисляет среднее, дисперсию, а также количество элементов в переданном наборе данных с устройства.
Результаты работы сопрограмма должна выдавать при отправке соответствующих сигналов.
'''

import numpy as np
class PrintAverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

class PrintAmountOfElements(Exception):
    pass

def My_coroutine():
    print("Starting coroutine")
    A = []
    try:
        while True:
            try:
                x = yield
                A.append(x)
                aver = np.mean(A) # Returns the average of the array elements
                disp = np.var(A)
                n = len(A)

            except PrintAverage:
                yield aver
            except PrintDispersion:
                yield disp
            except PrintAmountOfElements:
                yield n
    finally:
        print("Stop coroutine")

coroutine = My_coroutine()
next(coroutine)
for i in range(12):
    coroutine.send(i)
    if i%2 == 0:
        print("Average:", coroutine.throw(PrintAverage))
        next(coroutine)
    if i%3 == 0:
        print("Dispersion:", coroutine.throw(PrintDispersion))
        next(coroutine)
    if i%4 == 0:
        print('Amount Of Elements:', coroutine.throw(PrintAmountOfElements))

print()
print(coroutine.throw(PrintAverage))
next(coroutine)

print(coroutine.throw(PrintDispersion))
next(coroutine)
print(coroutine.throw(PrintAmountOfElements))
next(coroutine)

coroutine.close()