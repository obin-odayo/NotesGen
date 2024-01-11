import glob
import sys

def showAll():
    files = glob.glob("*.md")
    files.remove("_index.md")
    count = 1

    if files:
        print("%d markdown files found: ", len(files))
        for i in files:
            print(str(count) + ". [["+ i +"]]")
            count+=1
    else:
        print("\nNo markdown files found.\n")
    
    return files

def index(fileList):
    with open('_index.md', 'w') as file:
        file.write("# CCPROG2 Notes\n\n")
        file.write("**By: Zhean Robby L. Ganituen**\n")
        file.write("*Email: [obin.odayo@gmail.com](mailto:obin.odayo@gmail.com)*\n\n")
        file.write("## Contents\n\n")
        
        count = 1

        for i in fileList:
            file.write(str(count) + ". [["+ i +"]]\n")
            count+=1

        print("\nindexIt: Done. Check _index.md.\n")

if __name__ == "__main__":    
    while True:
        cmd = input(".> ")

        if cmd == "wAll":
            showAll()
            print("")
        elif cmd == "wAll : indexIt":
            fileList = showAll()
            index(fileList)
        elif cmd == "ext":
            sys.exit()
