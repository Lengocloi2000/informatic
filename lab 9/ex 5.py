'''
Представьте, что у вас настроено взаимодействие с сервером, от которого приходят пакеты, содержащие сообщения от различных клиентов.
Обработка каждого из клиентов должна идти в отдельном потоке.

Реализуйте:

Корутина connect_user принимает данные авторизации от пользователя, открывает файл с названием .txt и создает на его основе корутину цrite_to_file
Корутина write_to_file(f_obj) записывает переданное планировщиком задач сообщение пользователя,
которые записываются в файловый объект, переданный в качестве аргумента при генерации.
Также принимает и обрабатывает сигнал об окончании соединения и выходит из сопрограммы.
Планировщик задач, распределяющий задачи по сопроцессам на каждого пользователя.
'''

class Terminate(Exception):
    pass

class Connect(Exception):
    pass

def connect_user(user):
    with open('user.txt','w') as f:
        yield from write_to_file(f)

def write_to_file(f_obj):
    while True:
        try:
            x = yield
            print(f"Inner: {x}")
            f_obj.writelines(x)
        except Terminate:
            print('Finished')
            break
    f_obj.close()

def Task_Manager():
    print("Task Manager started")
    u = []
    while True:
        try:
            x = yield
            print(f"Outer: {x}")
            u.append(x)
        except Connect:
            yield from connect_user(u)

try:
    coroutine = Task_Manager()
    next(coroutine)
    coroutine.send('LeLoi')
    coroutine.send('Kaka')
    coroutine.throw(Connect)
    coroutine.send('exercise')
    coroutine.send('news')
    coroutine.throw(Terminate)
except:
    pass
