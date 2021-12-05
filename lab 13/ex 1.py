"""Задача 1"""
'''объект : class'''
import pickle
class Greeter:
    def __init__(self, name , old):
        self.name = name
        self.old = old

p_file = open('class.pickle','wb')
pickle.dump(Greeter("Le Loi" , 21 ),p_file,pickle.HIGHEST_PROTOCOL)
p_file.close()
p_in = open('class.pickle','rb')
h = pickle.load(p_in)
print(h.__dict__)

'''объект : открытый файл'''
import pickle

example_dict = {1:'4',2:'2',3:'a'}
pickle_out = open('dict.pickle','wb')
pickle.dump(example_dict,pickle_out,pickle.HIGHEST_PROTOCOL)
pickle_out.close()

pickle_in = open('dict.pickle','rb')
example_dict_new = pickle.load(pickle_in)
print(example_dict_new)

'''встроенные функции'''
pr = abs(-15)

with open('func.pickle', 'wb') as f:
    pickle.dump(pr, f, pickle.HIGHEST_PROTOCOL)
with open('func.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)

'''итераторы'''

iter = range(7)
with open('iter.pickle', 'wb') as f:
    pickle.dump(iter, f, pickle.HIGHEST_PROTOCOL)
with open('iter.pickle', 'rb') as f:
    data = pickle.load(f)
for i in data:
    print(i)

