import os
import shutil

path = "C:\\Users\\surya\\OneDrive\\Desktop"  
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  

    target_folder = os.path.join(path, extension)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    shutil.move(os.path.join(path, file), os.path.join(target_folder, file))

