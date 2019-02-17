import sys
import glob

if __name__ == "__main__":
    try:
        folder = sys.argv[1]
    except ValueError:
        print("\u001b[31mWrong number of arguments given\u001b[0m")
        print("Usage: python3 Merge.py [Path to directory]")
    else:
        children = glob.glob(folder + "/*list_*.csv")
        allMovies = []
        print("Collecting...")
        for movieList in children:
            with open(movieList, "r") as textList:
                allMovies += textList.readlines()
        print("Sorting...")
        allMovies.sort()

        print("Writing the output...")
        with open(folder + "/merge.csv", "w+") as mergeFile:
            for movie in allMovies:
                mergeFile.write(movie)

        print("\u001b[1mSuccessfully merged", len(allMovies), "elements.\u001b[0m")
