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

