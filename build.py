import glob
import sys
import os
import re


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
        print("wAll: Found " + str(len(files)) + " markdown files.")
        for i in files:
            print(str(count) + ". "+ i)
            count+=1
        print("")
    else:
        print("wAll: No markdown files found.")
    
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
        file.write("**By: Zhean Robby L. Ganituen**\n\n")
        file.write("*Email: [mailto:zhean_robby_ganituen@dlsu.edu.ph](mailto:zhean_robby_ganituen@dlsu.edu.ph)*\n\n")
        file.write("Github: [obin-odayo/Notes_CCPROG2](https://github.com/obin-odayo/Notes_CCPROG2)\n\n")
        file.write("## Contents\n\n")
        
        count = 1

        for i in fileList:
            i = i.replace(".md", ".html")
            name = i.replace("docs\\", "")
            i = i.replace("docs\\", "build\\")
            name = name.replace(".md", "")
            name = name.replace("-", " ")
            file.write(str(count) + ". [" + name + "]" + "(" + i + ")\n\n")
            count+=1

        print("indexIt: Done. Check index.md.")

def webber(fileMD, index=0):
    """
    Converts a markdown file to a website.

    Parameters:
    - fileMD (string): file name of markdown file in directory
    - index (int): to check if the working file is the index

    Returns:
    None.
    """

    fileName = fileMD.replace(".md", "")
    fileName = fileName.replace(" ", "")

    if index == 1:
        filePath = "build\\" + fileName
        fileName = "docs\\" + fileName
        fileHTML = filePath + ".html" 
    else:
        filePath = fileName 
        fileHTML = fileName + ".html"
    
    command = "pandoc " + fileName + ".md -o " + filePath + ".html"
    
    print(command)
    os.system(command)
    
    with open(fileHTML, "r") as file:
        content = file.read()

    with open(fileHTML, "w") as file:
        # clear file
        file.truncate(0)

        file.write("<!DOCTYPE html>")
        file.write("<html lang=\"en\">")
        file.write("<head>")
        file.write("<meta charset=\"UTF-8\" />")
        file.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />")
        file.write('<link rel="stylesheet" href="/style.css">')
        file.write("<title>" + fileName + "</title>")
        file.write("</head>")
        file.write("<body>")
        file.write('<a class="button" href="/index.html">Go back</a>')
        file.write(content)
        file.write("</body>")
        file.write("</html>")

    print("Webber: `" + fileName + "` successfully converted to HTML. Check " + fileName + ".html.")

def wiksToLinks(fileName, index=0):
    """
    Converts markdown wikilinks to working HTML links.

    Parameters:
    - fileName (string): file name of markdown file in directory
    - index (int): to check if the working file is the index 

    Returns:
    None.
    """
    fileName = fileName.replace(".md", "")
    fileName = fileName.replace(" ", "")
    
    if index == 1:
        fileName = "build/" + fileName + ".html"
    else: fileName = fileName + ".html"
    
    with open(fileName, "r") as file:
        content = file.read()
    
    wikiLinks = re.findall(r'\[\[(.*?)\]\]', content)

    for link in wikiLinks:
        replace = f'<a href="{link}.html">{link}</a>'
        content = re.sub(r'\[\[' + re.escape(link) + r'\]\]', replace, content)
    
    with open(fileName, 'w') as file:
        file.write(content)

    print("wiksToLinks: successfully transported wikilinks. Check " + fileName + ".html.")

def styleUp():
    """
    Creates default CSS template in the directory.

    Parameters:
    None.

    Returns:
    None.
    """
    basicStyle = [
    "body {",
    "  font-family: Arial, Helvetica, sans-serif;",
    "  background-color: #121212;",
    "  color: #ffffff;",
    "  margin-left: 15%;",
    "  margin-right: 15%;",
    "}",
    "",
    "body code {",
    "  color: #ffd700;",
    "}",
    "",
    "body blockquote {",
    "  background: #090909;",
    "  padding: 10px;",
    "}",
    "",
    "body a {",
    "  text-decoration: underline;",
    "  color: #ffffff;",
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
    "}",
    "",
    ".button {",
    "  bottom: 0%;",
    "  right: 5%;",
    "  position: fixed;",
    "  font-size: 20px;",
    "  text-decoration: none;",
    "  background-color: #454545;",
    "  color: white;",
    "  padding: 0.5%;",
    "}",
    ]

    with open("style.css", "w") as file:
        for line in basicStyle:
            file.write(line + "")

    print("styleUp: Created basic style sheet. Check style.css")    

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
            webber(cmd, 1)
            wiksToLinks(cmd, 1)
        elif cmd == "webber":
            webber("index.md")
            wiksToLinks("index.md")
        elif cmd == "styleUp":
            styleUp()
        elif cmd == "superAll":
            base = showAll()
            for file in base:
                file = file.replace("docs\\", "")
                webber(file, 1)
                wiksToLinks(file, 1)
        else:
            print("Error: command, " + cmd + " not found.")