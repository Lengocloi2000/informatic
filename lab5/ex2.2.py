class Mother:
    __name = ''
    __old = ''
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_name(self):
        return self.__name

    def get_old(self):
        return self.__old

    def __str__(self):
        return 'This is {} \nShe is {} years old'.format(self.__name,self.__old)

class Daughter(Mother):
    __job = ''
    def __init__(self, name, old, job ):
        super().__init__(name,old)
        self.__job = job

    def get_job(self):
        return self.__job

    def __str__(self):
        return 'This is {}\nShe is {} years old \nShe is {}'.format(self.get_name(),self.get_old(),self.get_job())

Mom = Mother('Татьяна' , 30)
daug = Daughter('Катя', 10, 'student')

print(Mom)
print('\n~~~~~~~~~~~~~~~~~~~\n')
print(daug)