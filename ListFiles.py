import os
import glob

pathInit = input()

def Unfold(folder):
    children = glob.glob(folder+"/*")
    for child in children:
        if os.path.isdir(child):
            Unfold(child)
        else:
            file = os.path.splitext(os.path.basename(child))
            if file[1] in [".avi",".mkv",".mp4"]:
                print(file[0])
    

Unfold(pathInit)
