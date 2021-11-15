import threading
import matplotlib.pyplot as plt
import time

# task 3
a = 0
def scalar_product(x):
    global a
    a = a + x

def run_threads(n,v):
    threads = [threading.Thread(target= scalar_product, args = (v[i],)) for i in range(n)]
    for thread in threads:
        thread.start()

v1 = [150519992020,301220002020,181019992020,221119942020,112119992020]
v2 = [150519992020,301220002020,181019992020,221119942020,112119992020,224353255454]
v3 = [150519992020,301220002020,181019992020,221119942020,112119992020,224353255454, 224353255454]
v4 = [150519992020,301220002020,181019992020,221119942020,112119992020,224353255454, 224353255454,181019992020]
v5 = [150519992020,301220002020,181019992020,221119942020,112119992020,224353255454,221119942020,112119992020,224353255454]
v= [v1,v2,v3,v4,v5]
print(v[0])
list_time = []
for i in range(len(v)):
    n = len(v[i])
    start_time = time.time()
    run_threads(n, v[i])
    run_time = time.time() - start_time
    print('Finished.\nScalar product is: {}.\nRuntime is: {}.'.format(a, run_time))

#task4
def scalar(h):
    a = 0
    for i in range(len(h)):
        a += h[i]
    return a
h1 = [150519992020,301220002020]
h2 = [150519992020,301220002020,181019992020]
h3 = [150519992020,301220002020,181019992020,221119942020]
h=[h1,h2,h3]
x_data = [2,3,4,5,6,7,8,9] # Number of threads
list_time = []
for i in range(3):
    start_time1 = time.time()
    scalar(h[i])
    run_time1 = time.time() - start_time1
    list_time.append(run_time1)
for i in range(len(v)):
    n = len(v[i])
    start_time = time.time()
    run_threads(n, v[i])
    run_time = time.time() - start_time
    list_time.append(run_time)

print(list_time)
plt.plot(x_data, list_time)
plt.grid()
plt.ylabel('Время выполнения, [с]')
plt.xlabel('Число потоков')
plt.show()