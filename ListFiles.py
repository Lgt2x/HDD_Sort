import os
import glob

pathInit = input("Path to HDD: ")
dest = input("Dossier destination de la liste: ")
listFile = open(dest+"/"+"list_"+os.path.basename(pathInit)+".txt","w+")

def Unfold(folder, listFile):
    children = glob.glob(folder+"/*")
    for child in children:
        if os.path.isdir(child):
            Unfold(child, listFile)
        else:
            file = os.path.splitext(os.path.basename(child))
            if file[1] in [".avi",".mkv",".mp4"]:
                listFile.write(file[0]+"\n")
    

Unfold(pathInit, listFile)

listFile.close()
