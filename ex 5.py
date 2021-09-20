arr = ['math', 'physic', 'chemistry', 'biology']
def write_array(arr , file_name):
    my_new = open('new.txt', 'w')
    arr = map(lambda x: x + '\n', arr)
    my_new.writelines(arr)

flag = True
while flag:
    new_file = input('enter file to write lines: ')
    try:
        write_array(list_of_lines, new_file)
        flag = False
        print('success')
    except FileNotFoundError:
        print('Directory does not exist, try again')
