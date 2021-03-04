
######### rename files from folder ############

import os
import pathlib

path = 'C:/Users/bruno/Documents/diabetesLearning/foodDatabase/Dataset - Comidas Brasileiras TCC v1/bruno/'
files = os.listdir(path)

offset = 0
for index, file in enumerate(files):
    extension = pathlib.Path(os.path.join(path, file)).suffix
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index + offset), extension])))
        

############# copy files from many subfolders into one folder ########

# import os
# from shutil import copyfile, copy2
# with os.scandir("C:/Users/bruno/Desktop/fotos Database de pratos") as it:
#     for folder in it:
#         with os.scandir(folder.path) as it2:

#             for file in it2:
#                 if file.is_dir():
#                     with os.scandir(file.path) as it3:
#                         for subfile in it3:
#                             if subfile.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#                                 copy2(subfile.path, "C:/Users/bruno/Desktop")
#                 else:
#                     if file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#                         copy2(file.path, "C:/Users/bruno/Desktop")