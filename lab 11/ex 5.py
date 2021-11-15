'''Запустите код. Попробуйте объяснить, почему LIST - пуст.'''
'''т.к у каждого процесса есть изолированное от других процессов состояние.
значение в списке LIST превращается [] после каждого процесса 
чтобы в списке появляется 'item' мы должны использовать межпроцессный обмен, либо очереди Queue, либо каналы данных (pipe)
например ниже
'''
from multiprocessing import Process, Queue

def worker(LIST):
    LIST.put('item')

LIST = Queue()
if __name__ == "__main__":
    processes = [
        Process(target=worker, args= (LIST,))
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST.get())
