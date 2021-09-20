flag = True
while flag:
    file_name = input('enter file : ')
    try:
        with open(file_name,'r') as file:
            for line in file:
                print(line.strip())
        flag = False
    except FileNotFoundError:
        print('Bad file path, try again')