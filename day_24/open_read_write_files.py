
# Using python to open, write, amend, modify and read files, all without
# having to us the mouse. We can do all of this with the in-built method
# 'open()'.

# The open() method can take a number of inputs/parameters, most of which have
# default values (these are optional inputs). These inputs/parameters include:
# open(file, mode=str, buffering=-1, encoding=None, errors=None, newline=None,
#      closefd=True, opener=None)
'''
# Example opening a file:
file = open("my_file.txt")
'''
# For the above file, nothing will happen on its own, but Python will open
# the defined file to have it ready for use. 
'''
# Reading the file and print to screen
contents = file.read()
print(contents)

# Closing the file
file.close()

# When Python opens a file, it uses up resources of whatever computer we are
# using. We also don't know when Python will close the file on its own to
# free up those resources, so we can use the close() method to manually close
# the file after it has been used.

# Another way to open a file and use it, is to open a file with the 'with'
# keyword. This will do the same as above, except we don't have to use the
# close() method as the with keyword will do that for us. Also, whatever word
# we use after the 'as' keyword acts as a variable name, so we can use
# whatever name we want (usually, when a file is being opened with the 'with'
# keyword, the variable name is something along the lines of 'file' or 'f'.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# One advantage of opening files with the above method is that it
# automatically closes the file after it uses the file. It's an advantage
# because if we use the first method of opening files instead, we may forget
# to manually close the file.

# Writing to a file:

# The below code will return an error because; 1. the open() method opens a
# file (in the manner below) in read only mode by default, 2. we're trying to
# write text to a file. Text cannot be written to a file when the file is
# open in read only file.

with open("my_file.txt") as file:
    file.write("New text")
'''

# When we want to write to a file, we will want to set the open() method to
# "w" for write mode (the 'mode=' isn't necessary, but can be used with a
# positional argument):
'''
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# We can't seem to read from an open file in write mode
with open("my_file.txt") as file:
    content = file.read()
    print(content)
'''

# Writing to a file in write mode will override whatever is already in the
# file (whatever is in the file will be removed and replaced by whatever we
# are currently writing to the file.
'''
# When opening a file in write mode, if the file doesn't actually exist,
# Python will create the file:
with open("my_other_file.txt", mode="w") as file:
    file.write("Created a new file.")

with open("my_other_file.txt") as file:
    content = file.read()
    print(content)
'''
# This new file will be created in the same directory as the Python file that
# create it.


# Appending to a file
'''
# If we want to add to a file, we can open a file in 'append' mode (the
# 'mode="a"' means append mode:
with open("my_file.txt", mode="a") as file:
    file.write("\nI enjoy playing video games.")
'''
'''
# Relative and Absolute File Paths
# Files don't just have a name. They also have a path (or way to get to
# them). Files are kept within certain places on computers and we need to give
# computers directions to access these files

# With computers, there are files and there are folders. Files can live
# within folders and we can navigate through 7 folders deep (for example) to
# get to particular file.

# Everything starts at the root folder. On a Windows computer, the root
# folder is usually the 'C drive'. The root folder on a Windows computer is
# represented by an uppercase C and a colon prefixing a forward slash (C:/)
# On a Mac computer, the root folder is known as the 'Macintosh HD'. The root
# folder on a Mac is represented by a single forward slash (/).

# An examples of a path:

/ Root
¦
¦¬ / Work
    ¦
    ¦¬ report.doc       (Mac path = /Work/report.doc)
    ¦                   (Windows path = C://Work/report.doc)
    ¦¬ / Project
        ¦
        ¦¬ talk.ppt     (Mac path = /Work/Project/talk.ppt)
                        (Windows path = C:/Work/Project/talk.ppt)
'''
# Absolute File Path
# We can access a particular file like the above example. For example,
# the path for the file 'talk.ppt' is: C:/Work/Project/talk.ppt' (on windows).
# This sort of path is known as an Absolute File Path.


# Relative File Path
# If we are already inside a particular folder (also known as 'Working
# Directory' or 'Directory', a folder that we are, at the time, working from),
# we can access a file from that folder while being in the folder.
# We can access a file from a folder while inside that folder by using a
# Relative File Path.

# Example of a Relative File Path (if inside the Project folder from above):
# ./talk.ppt

# The './' at the beginning tells the computer to look inside whatever folder
# we are currently in for the the file (in this case for the example) we are
# looking for.
# If we were inside of the 'Work' folder instead of the 'Project' folder,
# the Relative File Path to access the same file would be:
# ./Project/talk.ppt

# If we wanted to go one ste up in the directory tree:
# If we wanted to access the 'report.doc' (inside the 'Work' folder) file while
# we were inside the 'Project' folder (also inside the 'Work' folder),
# we could access 'report.doc' from the 'Project' folder by using the
# Relative File Path: '../report.doc'.
# The two dots at the beginning represent stepping out of the current
# directory (folder) and into the parent folder to access the file that we
# want. The two dots essentially represent stepping up the file path hierarchy.

# Remember:
# ./file.txt or just file.txt - to access file inside the same directory/folder
# ./subfolder/file.txt - to access file in subfolder while inside parent folder
# ../file.txt - to access file in parent folder while inside subfolder

# Challenge
# 1. Opening file from same directory
with open("my_file.txt") as file:
    contents = file.read()
    print()
    print(contents)

# 2. Opening file using Absolute File Path:
with open("C:/Users/Simon/Desktop/my_other_file.txt") \
        as f:
    content = f.read()
    print()
    print(content)

# 3. Opening a file using Relative File Path:
with open("../../another_file.txt") as my_file:
    cont = my_file.read()
    print()
    print(cont)
# Going two steps back through the directory, like in challenge 3, we have to
# use '../' for every step back.

# The difference between the Absolute and Relative File Paths;
#   - Absolute File Path: always relative to the root directory of a computer.
#   - Relative File Path: relative to the current working directory (the
#                         folder that we are currently working in). It depends
#                         where we are and where we are trying to get to.





