# **0x00 shell basics** 

The learning objectives for this project were:

## **General** 
	• What does RTFM mean?
	• What is a Shebang
	• What is the Shell
	• What is the shell
	• What is the difference between a terminal and a shell
	• What is the shell prompt
	• How to use the history (the basics)

## **Navigation** 
	• What do the commands or built-ins cd, pwd, ls do
	• How to navigate the filesystem
	• What are the . and .. directories
	• What is the working directory, how to print it and how to change it
	• What is the root directory
	• What is the home directory, and how to go there
	• What is the difference between the root directory and the home directory of the user root
	• What are the characteristics of hidden files and how to list them
	• What does the command cd - do

## **Looking Around**
	• What do the commands ls, less, file do
	• How do you use options and arguments with commands
	• Understand the ls long format and how to display it
	• What does the ln command do
	• What do you find in the most common/important directories
	• What is a symbolic link
	• What is a hard link
	• What is the difference between a hard link and a symbolic link

## **Manipulating Files**
	• What do the commands cp, mv, rm, mkdir do
	• What are wildcards and how do they work
	• How to use wildcards

## **Working with Commands** 
	• What do type, which, help, man commands do
	• What are the different kinds of commands
	• What is an alias
	• When do you use the command help instead of man

## **Reading Man Pages**
	• How to read a man page
	• What are man page sections
	• What are the section numbers for User commands, System calls and Library functions
	• Keyboard Shortcuts for Bash
	• Common shortcuts for Bash

## **LTS**
	• What does LTS mean?

### **For this project we had to write the following scripts:**
	• 0-current_working_directory - prints the absolute path name of the current working directory.
	• 1-listit - displays the contents list of your current directory.
	• 2-bring_me_home - changes the working directory to the user’s home directory.
	• 3-listfiles - displays current directory contents in a long format.
	• 4-listmorefiles - displays current directory contents, including hidden files (starting with .). Use the long format.
	• 5-listfilesdigitonly - displays current directory contents:
		- Long format.
		- With user and group IDs displayed numerically.
		- And hidden files (starting with .)
	• 6-firstdirectory - creates a directory named my_first_directory in the /tmp/ directory.
	• 7-movethatfile - moves the file betty from /tmp/ to /tmp/my_first_directory.
	• 8-firstdelete - deletes the file betty. The file betty is in /tmp/my_first_directory
	• 9-firstdirdeletion - deletes the directory my_first_directory that is in the /tmp directory.
	• 10-back - changes the working directory to the previous one.
	• 11-lists - ists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
	• 12-file_type - prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
	• 13-symbolic_link - creates a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
	• 14-copy_html - copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
	We could consider that all HTML files have the extension .html
	• 100-lets_move - moves all files beginning with an uppercase letter to the directory /tmp/u. We could assume that the directory /tmp/u will exist when we will run your script
	• 101-clean_emacs - deletes all files in the current working directory that end with the character ~.
	• 102-tree - creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory. 
	We were only allowed to use two spaces (and lines) in the script, not more.
	• 103-commas - lists all the files and directories of the current directory, separated by commas (,):
		- Directory names should end with a slash (/).
		- Files and directories starting with a dot (.) should be listed.
		- The listing should be alpha ordered, except for the directories (.) and (..) which should be listed at the very beginning.
		- Only digits and letters are used to sort; Digits should come first.
		- You can assume that all the files we will test with will have at least one letter or one digit.
		- The listing should end with a new line.
	• school.mgc - Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.

