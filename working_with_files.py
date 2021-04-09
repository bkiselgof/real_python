"""
Table of Contents

Python’s “with open(…) as …” Pattern
Getting a Directory Listing
Directory Listing in Legacy Python Versions
Directory Listing in Modern Python Versions
Listing All Files in a Directory
Listing Subdirectories
Getting File Attributes
Making Directories
Creating a Single Directory
Creating Multiple Directories
Filename Pattern Matching
Using String Methods
Simple Filename Pattern Matching Using fnmatch
More Advanced Pattern Matching
Filename Pattern Matching Using glob
Traversing Directories and Processing Files
Making Temporary Files and Directories
Deleting Files and Directories
Deleting Files in Python
Deleting Directories
Deleting Entire Directory Trees
Copying, Moving, and Renaming Files and Directories
Copying Files in Python
Copying Directories
Moving Files and Directories
Renaming Files and Directories
Archiving
Reading ZIP Files
Extracting ZIP Archives
Extracting Data From Password Protected Archives
Creating New ZIP Archives
Opening TAR Archives
Extracting Files From a TAR Archive
Creating New TAR Archives
Working With Compressed Archives
An Easier Way of Creating Archives
Reading Multiple Files
Conclusion
"""



with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)


with open('data.txt', 'r') as f:
    data = f.read()

print(data)

#Directory Listing in Legacy Python Versions
#In versions of Python prior to Python 3, os.listdir() is the method to use to get a 
# directory listing:

dir1 = '/mnt/c/Users/bkise/Documents/repos/real_python'

import os
entries = os.listdir(dir1)
entries

import os
entries = os.scandir(dir1)
entries


#The ScandirIterator points to all the entries in the current directory. You can loop over the contents of the iterator and print out the filenames:
import os
with os.scandir(dir1) as entries:
    for entry in entries:
        print(entry.name)


import os
# List all files in a directory using scandir()
basepath = dir1
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)


#Here’s how to list files in a directory using pathlib.Path():

from pathlib import Path

basepath = Path(dir1)
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)


#Here’s how to list files in a directory using pathlib.Path():

from pathlib import Path

basepath = Path(dir1)
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)


#Listing All Files in a Directory

dir2 = '/mnt/c/Users/bkise/Documents/repos'

import os

# List all files in a directory using os.listdir
basepath = dir2
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)



#An easier way to list files in a directory is to use os.scandir() or pathlib.Path():

import os

# List all files in a directory using scandir()
lbasepath = dir2
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)


#Another way
from pathlib import Path

basepath = Path(dir2)
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)


from pathlib import Path

# List all files in directory using pathlib and using generators!
basepath = Path(dir2)
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)


#Listing Subdirectories

#To list subdirectories instead of files, use one of the methods below. Here’s how to use 
# os.listdir() and os.path():

import os

# List all subdirectories using os.listdir
basepath = dir2
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)


#Here’s how to use os.scandir():

import os

# List all subdirectories using scandir()
basepath = dir2
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)


#Here’s how to use pathlib.Path():

from pathlib import Path

# List all subdirectory using pathlib
basepath = Path(dir2)
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)


#Getting File Attributes

'''
Python makes retrieving file attributes such as file size and modified times easy. This is done 
through os.stat(), os.scandir(), or pathlib.Path().

os.scandir() and pathlib.Path() retrieve a directory listing with file attributes combined. 
This can be potentially more efficient than using os.listdir() to list files and then getting
 file attribute information for each file.

The examples below show how to get the time the files in my_directory/ were last modified. 
The output is in seconds:
'''

import os
with os.scandir(dir2) as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)



#To convert the values returned by st_mtime for display purposes, you could write a helper 
# f unction to convert the seconds into a datetime object:

from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files(d):
    dir_entries = scandir(d)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

get_files(dir2)


