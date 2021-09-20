import os
import zipfile

file_zip = open('file2.txt','w')
# zip = zipfile.ZipFile('file.zip')
# zip.extractall()
arr = []
for folder, subfolders, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            arr.append(folder)
            break

arr.sort()
file_zip.write('\n'.join(arr))

file_zip.close()

flag = True
while flag:
    new_file = input('enter file to write lines: ')
    try:
        ans = open(new_file,'w')
        for line in new_file:
            ans.write(line)
            ans.write('\n')
        ans.close()
        flag = False
        print('success')
    except FileNotFoundError:
        print('Directory does not exist, try again')
