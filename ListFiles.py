import os

pathInit = input()

def Deplie(folder):
    print(folder+":")

    result = os.popen('ls ' + Escape(folder)).read()[:-1].split("\n")
    if not result[0]: return
    
    for file in result:
        if (IsFolder(Escape(folder+"/"+file))):
            Deplie(folder+"/"+file)
        else:
            print(file,end=" ")
            size = int(os.popen("stat -f%z "+Escape(folder+"/"+file)).read()[:-1])
            sizeMo = round(size/10**6,1)
            print(str(str(sizeMo)+" Mo"))

    print()
        

def IsFolder(path):
    return (os.system("cd "+path) == 0)

def Escape(path):
    
    newPath = path.replace(" ","\\ ")
    newPath = newPath.replace("(","\\(")
    newPath = newPath.replace(")","\\)")
    
    return newPath

Deplie(pathInit)
