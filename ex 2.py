array = ['math','physic','chemistry','biology']
my_new = open('new.txt','w')
array = map(lambda x: x + '\n',array)
my_new.writelines(array)