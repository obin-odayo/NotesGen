import glob
import sys
import os
import subprocess


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
        print("\n\nwAll: Found " + str(len(files)) + " markdown files.")
        for i in files:
            print(str(count) + ". "+ i)
            count+=1
        print("\n\n")
    else:
        print("\n\nwAll: No markdown files found.\n\n")
    
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
            name = name.replace("-", " ")
            file.write(str(count) + ". [" + name + "]" + "(" + i + ")\n")
            count+=1

        print("\n\nindexIt: Done. Check index.md.\n\n")

def webber(fileMD):
    """
    Converts a markdown file to a website.

    Parameters:
    - fileMD (string): file name of markdown file in directory 

    Returns:
    None.
    """
    fileName = fileMD.replace(".md", "")
    fileName = fileName.replace(" ", "")
    command = "pandoc " + fileName + ".md -o " + fileName + ".html"
    os.system(command)

    fileHTML = fileName + ".html"

    with open(fileHTML, "r") as file:
        content = file.read()

    with open(fileHTML, "w") as file:
        # clear file
        file.truncate(0)

        file.write("<!DOCTYPE html>\n")
        file.write("<html lang=\"en\">\n")
        file.write("<head>\n")
        file.write("<meta charset=\"UTF-8\" />\n")
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n")
        file.write('<link rel="stylesheet" href="style.css">')
        file.write("<title>" + fileName + "</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write(content)
        file.write("</body>\n")
        file.write("</html>\n")
    
    print("\n\nWebber: `" + fileName + "` successfully converted to HTML. Check " + fileName + ".html.\n\n")

def styleUp():
    basicStyle = [
    "body {",
    "  font-family: Arial, Helvetica, sans-serif;",
    "  background-color: #121212;",
    "  color: rgb(215, 215, 215);",
    "  margin-left: 15%;",
    "  margin-right: 15%;",
    "}",
    "",
    "body a {",
    "  text-decoration: underline;",
    "  color: rgb(215, 215, 215);",
    "}",
    "",
    "body a:hover {",
    "  text-decoration: none;",
    "}",
    "",
    "body p,",
    "body li {",
    "  font-size: 18px;",
    "}",
    "",
    "body h1 {",
    "  text-align: center;",
    "  font-size: 48px;",
    "}",
    "",
    "body h2 {",
    "  text-align: center;",
    "  font-size: 32px;",
    "}",
    "",
    "body h3 {",
    "  font-size: 32px;",
    "}"
    ]

    with open("style.css", "w") as file:
        for line in basicStyle:
            file.write(line + "\n")

    print("\n\nstyleUp: Created basic style sheet. Check style.css\n\n")

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
        elif "webber : " in cmd:
            cmd = cmd.replace("webber : ", "")
            webber(cmd)
        elif cmd == "webber":
            webber("index.md")
        elif cmd == "styleUp":
            styleUp()
        else:
            print("Error: command, " + cmd + " not found.")