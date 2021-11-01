'''
Скачайте архив, и разархивируйте его в отдельную папку в вашей рабочей папке.
Вам необходимо создать класс TextLoader,
который принимает в инициализаторе адрес папки.
 Метод __len__ должен возвращать количество текстов в папке. метод __getitem__ загружает текст,
 приводит его к нижнему регистру и убирает знаки препинания, при итерировании возвращаются нормализованные тексты, аналогично методу __getitem__.
'''

import string
import os

class TextLoader:
    def __init__(self, address):
        self.path = address
        list_files  =  os.listdir(self.path)
        self.files = [address + '/' + list_files[k] for k,file in enumerate(list_files)]

    def __len__(self):
        return len(self.files)

    def __getitem__(self, x):
        arr = []
        file = open(self.files[x], "r", encoding='utf-8')
        for line in file:
            line = line.lower()
            arr.append(line.translate(str.maketrans('', '', string.punctuation)))
        file.close()
        return arr

if __name__ == "__main__":
    address = 'D:\PycharmProjects\dino pygame\lap trinh huong doi tuong\lab 9\sample'
    a = TextLoader(address)
    print(len(a))
    print(*a[3])
