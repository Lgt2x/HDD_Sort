import glob
import sys

if __name__ == "__main__":
    folder = sys.argv[1]

    children = glob.glob(folder+"/*list_*.csv")
    allMovies = []
    for movieList in children:
        with open(movieList, "r") as textList:
            allMovies += textList.readlines()

    allMovies.sort()

    with open(folder + "/merge.csv", "w+") as mergeFile:
        for movie in allMovies:
            mergeFile.write(movie)
