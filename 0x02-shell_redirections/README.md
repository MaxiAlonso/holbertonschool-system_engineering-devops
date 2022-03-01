# **0x02 shell redirections**

The learning objectives for this project were:

## **Shell, I/O Redirection**
	• What do the commands head, tail, find, wc, sort, uniq, grep, tr do
	• How to redirect standard output to a file
	• How to get standard input from a file instead of the keyboard
	• How to send the output from one program to the input of another program
	• How to combine commands and filters with redirections

## **Special Characters**
	• What are special characters
	• Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

## **Other Man Pages**
	• How to display a line of text
	• How to concatenate files and print on the standard output
	• How to reverse a string
	• How to remove sections from each line of files
	• What is the /etc/passwd file and what is its format
	• What is the /etc/shadow file and what is its format

### For this project we had to write the following scripts:
	• 0-hello_world - prints “Hello, World”, followed by a new line to the standard output.
	• 1-confused_smiley - displays a confused smiley "(Ôo)'.
	• 2-hellofile - displays the content of the /etc/passwd file.
	• 3-twofiles - displays the content of /etc/passwd and /etc/hosts
	• 4-lastlines - displays the last 10 lines of /etc/passwd
	• 5-firstlines - displays the first 10 lines of /etc/passwd
	• 6-third_line - displays the third line of the file iacta.
	The file iacta will be in the working directory, we were not allowed to use sed.
	• 7-file - creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
	• 8-cwd_state - writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
	• 9-duplicate_last_line - duplicates the last line of the file iacta. The file iacta will be in the working directory.
	• 10-no_more_js - deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
	• 11-directories - counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted.
	• 12-newest_files - displays the 10 newest files in the current directory.
	Requirements:
		- One file per line.
		- Sorted from the newest to the oldest.
	• 13-unique - takes a list of words as input and prints only words that appear exactly once.
		- Input format: One line, one word.
		- Output format: One line, one word.
		- Words should be sorted.
	• 14-findthatword – displays lines containing the pattern “root” from the file /etc/passwd
	• 15-countthatword - displays the number of lines that contain the pattern “bin” in the file /etc/passwd.
	• 16-whatsnext – displays lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
	• 17-hidethisword - displays all the lines in the file /etc/passwd that do not contain the pattern “bin”.
	• 18-letteronly - display all lines of the file /etc/ssh/sshd_config starting with a letter.
	• 19-AZ - replaces all characters A and c from input to Z and e respectively.
	• 20-hiago - removes all letters c and C from input.
	• 21-reverse - revers its input. 
	• 22-users_and_homes - displays all users and their home directories, sorted by users. Based on the the /etc/passwd file.
	• 100-empty_casks - finds all empty files and directories in the current directory and all sub-directories.
		- Only the names of the files and directories should be displayed (not the entire path).
		- Hidden files should be listed
		- One file name per line
		- The listing should end with a new line
	We were not allowed to use basename, grep, egrep, fgrep or rgrep.
	• 101-gifs - lists all the files with a .gif extension in the current directory and all its sub-directories.
		- Hidden files should be listed.
		- Only regular files (not directories) should be listed.
		- The names of the files should be displayed without their extensions.
		- The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay
		- One file name per line.
		- The listing should end with a new line.
	We were not allowed to use basename, grep, egrep, fgrep or rgrep.
	• 102-acrostic - An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. 
	Create a script that decodes acrostics that use the first letter of each line.
		- The ‘decoded’ message has to end with a new line
	We were not allowed to use grep, egrep, fgrep or rgrep.
	• 103-the_biggest_fan - Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
		- Order by number of requests, most active host or IP at the top
		- We were not allowed to use grep, egrep, fgrep or rgrep.

