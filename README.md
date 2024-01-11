# NotesGen

* Notes Generator with static templating and wikilinks.
* Only using Markdown, HTML, CSS, Python, and Pandoc.
* Created on January 11, 2023.

## Requirements

* [Python](https://www.python.org/)
* [Pandoc](https://pandoc.org/)

> Add both to PATH.

## How To

**Prepare directory:** Create the folder where the notes are going to be stored. The tree of your directory should look something like:

```txt
root
├───build
└───docs
    └───src
```

**Clone `build.py`**. Clone the file in the root of the directory.

```txt
root
├───build
└───docs
    └───src
└───build.py <-
```

**Create your style file.** Open a command line interface where the directory is located and run the python script. Enter the `styleUp` command to create base style file.

1. `C:\path\to\your\dir>build.py`
2. `.> styleUp`

**Start writing**. Start writing your notes in markdown, remember to use wikilinks to use as references and improve note taking.

**Make an index file**. Create an index file at the root of your directory. Use the `wAll` command to check if all your notes are detected, if so then run the `indexIt` then the `webber` command to make the index file.

1. `C:\path\to\your\dir>build.py`
2. `.> wAll`
3. `.> wAll : indexIt`
4. `.> webber`

```txt
root
├───build
└───docs
    └───src
└───build.py
└───index.md <-
└───index.html <-
```

**Build your notes database**. Once done writing open the command line and execute the building commands.

### Building all notes

To build all notes simply execute the `superAll` command in the command line.

1. `C:\path\to\your\dir>build.py`
2. `.> superAll`

This would create all the HTML files for you immediately.

### Building notes one-by-one

To build notes one-by-one simply execute the following commands in the command line.

1. `C:\path\to\your\dir>build.py`
2. `.> webber : _name_of_file.md`

This will only create the HTML file of the selected file.
