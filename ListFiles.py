import os
import glob
import sys


def unfold(folder, name, textfile, count):
    children = glob.glob(folder + "/*")
    for child in children:
        if os.path.isdir(child):
            count = unfold(child, name, textfile, count)
        else:
            file = os.path.splitext(os.path.basename(child))
            if file[1] in [".avi", ".mkv", ".mp4"]:
                count += 1
                textfile.write(file[0] + ", " + name + "\n")
    return count


if __name__ == "__main__":
    try:
        scriptPath, hddPath, destPath, hddName = sys.argv
    except ValueError:
        print("\u001b[31mWrong number of arguments given\u001b[0m")
        print("Usage: python3 [Path to script] [Path to hard drive] [Destination of the list] [Name given to the list]")
    else:
        print("Computing...")
        with open(destPath + "/" + "list_" + hddName + ".csv", "w+") as movieList:
            counter = unfold(hddPath, hddName, movieList, 0)

        print("Done")
        print("\u001b[1m" + str(counter) + " entries added to " + str(hddName) + ".csv\u001b[0m")
