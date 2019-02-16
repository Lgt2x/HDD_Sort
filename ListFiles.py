import os
import glob
import sys


def unfold(folder, name, textfile):
    children = glob.glob(folder + "/*")
    for child in children:
        if os.path.isdir(child):
            unfold(child, name, textfile)
        else:
            file = os.path.splitext(os.path.basename(child))
            if file[1] in [".avi", ".mkv", ".mp4"]:
                textfile.write(file[0] + ", " + name + "\n")


if __name__ == "__main__":
    try:
        scriptPath, hddPath, hddName = sys.argv
    except ValueError:
        print("Wrong number of arguments given (requires 2)")
    else:
        with open(hddPath + "/" + "list_" + hddName + ".csv", "w+") as movieList:
            unfold(hddPath, hddName, movieList)
