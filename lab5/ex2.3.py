class Animal:
    __name = ''
    __old = ''

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_old(self, old):
        self.__old = old

    def get_old(self):
        return self.__old

    def __str__(self):
        return self.get_str()


class  Zebra(Animal):
    __kind = ''

    def __init__(self, name, old, kind ):
        super().__init__(name,old)
        self.__kind = kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    def get_str(self):
        return ' '.join(['Name :',self.get_name(),'\n',
                         'old : ',self.get_old(),'\n',
                         'kind : ',self.get_kind(),'\n'])


class Dolphin(Animal):
    __kind = ''
    __place = ''

    def __init__(self, name, old, kind , place):
        super().__init__(name, old)
        self.__kind = kind
        self.__place = place

    def set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    def set_place(self,place):
        self.__place = place

    def get_place(self):
        return self.__place

    def get_str(self):
        return ' '.join(['Name :', self.get_name(), '\n',
                         'old : ', self.get_old(), '\n',
                         'kind : ', self.get_kind(), '\n',
                         'place: ', self.get_place()])

dolphin = Dolphin('Dolphin','10','fish','underwater')
zebra = Zebra('Zebra', '7' , 'horse')

print(dolphin)
print('\n~~~~~~~~~~~~~\n')
print(zebra)



