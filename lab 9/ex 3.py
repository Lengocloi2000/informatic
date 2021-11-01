'''
Скачайте архив, и разархивируйте его в отдельную папку в вашей рабочей папке.
Вам необходимо создать класс TextLoader,
который принимает в инициализаторе адрес папки.
 Метод __len__ должен возвращать количество текстов в папке. метод __getitem__ загружает текст,
 приводит его к нижнему регистру и убирает знаки препинания, при итерировании возвращаются нормализованные тексты, аналогично методу __getitem__.
'''

import zipfile
import pathlib
import re
import requests
import io
import os

class TextLoader:
    def __init__(self, address):
        r = requests.get(address)
        with r, zipfile.ZipFile(io.BytesIO(r.content)) as zip_file:
            zip_file.extractall('file')
        self.path = pathlib.Path('sample')
        list_files  =  [name for name in list(self.path.glob('**/*.txt')) if name.is_file()]
        self.files = list_files
        self.iterable = iter(self.files)

    def __len__(self):
        return len(self.files)

    def __next__(self):
        text = next(self.iterable)
        with text.open('r') as f:
            r = f.read()
        with text.open('w') as f:
            norm = self.norma_text(r)
            f.write(norm)

    def __iter__(self):
        return self

    def norma_text(self,t):
         t = re.sub(r'[,.:;?!]','', t)
         t = t.lower()

if __name__ == "__main__":
    address = 'https://github.com/Lengocloi2000/informatic/blob/main/sample.zip'
    a = TextLoader(address)
    print(len(a))
    for i in range(len(a)):
        try:
            b = next(a)
            print(b.read()[:20])
            print("----------")
        except StopIteration:
            print("End.")