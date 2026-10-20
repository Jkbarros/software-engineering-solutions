# linux shell

**Source:** [`linux shell.docx`](../archive/canvas-submissions/linux%20shell.docx)  
**Course:** COSC 381 - Software Engineering Solutions (EMU)  
**Author:** Julio Barros

Julio Barros

Linux Shell

1.

/home

/etc

2.

The path for ~ will be /home/johnwick.

3.

4.

- According to the screenshot, the current working directory is "folder1"
- To delete the folder1, first, get out of "folder1" ( cd ../)
- Delete the folder using:
- rm -r folder1

5.

6.

>> is being used to add to a file and > is being used to overwrite ("clobber") a file.

Whenever users run ps aux > file, the conclusion of the command is recorded to document, and if a document named file actually exists, its data are overwritten.

When you have to use ps aux >> file, the outcome of ps aux is recorded to file; although, whereas if document named file previously exists, the file will now have both the contents of the previous file and the contents of ps aux, that will be added after the older contents.

if you type something in a terminal:

ps aux > log

It will save the output of ps aux to a file called log.

subsequently, if you placed

ps aux >> log

The very next outcome will then be added to the bottom of the first. If you only use one >, the prior file will be overwritten.
