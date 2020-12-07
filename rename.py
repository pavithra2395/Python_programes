import os
os.getcwd()
collection = "C:/darth_vader"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:/darth_vader/" + filename, "C:/darth_vader/" + str(i) + ".jpg")