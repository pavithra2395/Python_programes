import os
import shutil

input = "C:\\Users\\User\\Desktop\\puppies\\"

output = "C:\\Users\\User\\Desktop\\py\\"

result = os.walk(input)

for i in result:
    root = i[0]
    # folder = i[1]
    files = i[2]
    for file in files:
        if file.endswith('.py'):
            shutil.copyfile(root+'\\'+file, output+'\\'+file)