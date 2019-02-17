import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as mergeFile:
            lines = mergeFile.readlines()

        with open(sys.argv[1], 'w') as mergeFile:
            for line in range(len(lines)):
                if lines[line].count(",") == 2:
                    mergeFile.write(lines[line].replace(",", " ", 1))
                else:
                    mergeFile.write(lines[line])
        print("Done")
    else:
        print("\u001b[31mWrong number of arguments given\u001b[0m")
        print("Usage: python3 TwoColumns.py .../merge.csv")
