import string
import os

class TextLoader:
    def __init__(self, address):
        self.path = address
        list_files  =  os.listdir(self.path)
        self.files = [address + '/' + list_files[k] for k,file in enumerate(list_files)]
        self.file = open(self.files[3], encoding='utf-8')

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

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.file)
        print(*self.__getitem__(3))
        self.file = file

if __name__ == "__main__":
    address = 'D:\PycharmProjects\dino pygame\lap trinh huong doi tuong\lab 9\sample'
    a = TextLoader(address)
    print(len(a))
    print(*a[3])