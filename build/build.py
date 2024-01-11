import glob
import sys
import os


def showAll():
    """
    Shows all the markdown files in the docs directory.
    Returns the list of files.

    Parameters:
    - none

    Returns:
    Array: The list of all markdown files in the docs directory.
    """
    docPath = os.path.join("docs", "*.md")

    files = glob.glob(docPath)
    count = 1

    if files:
        print("%d markdown files found: ", len(files))
        for i in files:
            print(str(count) + ". "+ i)
            count+=1
    else:
        print("\nNo markdown files found.\n")
    
    return files

def index(fileList):
    """
    Creates or rewrites the index file in the directory with the updates list of files.

    Parameters:
    - fileList (list): list of files in the directory 

    Returns:
    None.
    """
    with open('index.md', 'w') as file:
        file.write("# CCPROG2 Notes\n\n")
        file.write("**By: Zhean Robby L. Ganituen**\n")
        file.write("*Email: [mailto:zhean_robby_ganituen@dlsu.edu.ph](mailto:zhean_robby_ganituen@dlsu.edu.ph)*\n\n")
        file.write("Github: [obin-odayo/Notes_CCPROG2](https://github.com/obin-odayo/Notes_CCPROG2)\n\n")
        file.write("## Contents\n\n")
        
        count = 1

        for i in fileList:
            name = i.replace("docs\\", "")
            name = name.replace(".md", "")
            name = name.replace(" ", "-")
            file.write(str(count) + ". [" + name + "]" + "(" + i + ")\n")
            count+=1

        print("\nindexIt: Done. Check index.md.\n")

if __name__ == "__main__":    
    while True:
        cmd = input(".> ")

        if cmd == "wAll":
            showAll()
        elif cmd == "wAll : indexIt":
            fileList = showAll()
            index(fileList)
        elif cmd == "ext":
            sys.exit()
