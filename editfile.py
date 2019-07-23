import glob, os
import shutil

currentPath = "D:/tes/New Website 2019 Images"
def moveFile(path):
    for file in os.listdir(path):
        if os.path.isdir(path + '/' + file):  
            moveFile(path + '/' + file)
        elif os.path.isfile(path + '/' + file):
            pathFileMove = file.replace('(','').replace(')','').replace(' ','-')
            shutil.move(path + '/' + file,currentPath + '/' + pathFileMove)
moveFile("D:/tes/New Website 2019 Images")