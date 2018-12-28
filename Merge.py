import os
import glob

folderInit = input("Path to folder containing lists: ")
mergeFile = open(folderInit+"/merge_HDDs.txt","w+")

children = glob.glob("/Users/Louis/Desktop/HDD_Sort/*list_*.txt")

for movieList in children:
    with open(movieList,"r") as textList:
        mergeFile.write(textList.read())

mergeFile.close()
