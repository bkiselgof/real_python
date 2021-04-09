#Python 3's pathlib Module: Taming the File System

'''
Table of Contents

The Problem With Python File Path Handling
Creating Paths
Reading and Writing Files
Picking Out Components of a Path
Moving and Deleting Files
Examples
Counting Files
Display a Directory Tree
Find the Last Modified File
Create a Unique File Name
Operating System Differences
Paths as Proper Objects
Conclusion
'''



#path.parent
#(pathlib.Path.home() / 'realpython.txt').is_file()


###Creating Paths

#All you really need to know about is the pathlib.Path class. There are a few different ways 
# of creating a path. First of all, there are classmethods like .cwd() (Current Working 
# Directory) and .home() (your user’s home directory):

import pathlib
pathlib.Path.cwd()

# BK: you can print it as a sring intead of a Posix type.
str(pathlib.Path.cwd())

pathlib.Path.home()
pathlib.Path.cwd()

#A path can also be explicitly created from its string representation:
pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt')

#A little tip for dealing with Windows paths: on Windows, the path separator is a backslash, 
# \. However, in many contexts, backslash is also used as an escape character in order to 
# represent non-printable characters. To avoid problems, use raw string literals to represent 
# Windows paths. These are string literals that have an r prepended to them. In raw string 
# literals the \ represents a literal backslash: r'C:\Users'.

#A third way to construct a path is to join the parts of the path using the special 
# operator /. The forward slash operator is used independently of the actual path separator
#  on the platform:

pathlib.Path.home() / 'python' / 'scripts' / 'test.py'

#The / can join several paths or a mix of paths and strings (as above) as long as there is at 
# least one Path object. If you do not like the special / notation, you can do the same thing
#  with the .joinpath() method:

pathlib.Path.home().joinpath('python', 'scripts', 'test.py')

###Reading and Writing Files

#Traditionally, the way to read or write a file in Python has been to use the built-in 
# open() function. This is still true as the open() function can use Path objects directly. 
# The following example finds all headers in a Markdown file and prints them:

path = pathlib.Path.cwd() / 'test.md'
with open(path, mode='r') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]

print('\n'.join(headers))

#An equivalent alternative is to call .open() on the Path object:
with path.open(mode='r') as fid:
    ...

'''
In fact, Path.open() is calling the built-in open() behind the scenes. Which option you use is 
mainly a matter of taste.

For simple reading and writing of files, there are a couple of convenience methods in the 
pathlib library:

.read_text(): open the path in text mode and return the contents as a string.
.read_bytes(): open the path in binary/bytes mode and return the contents as a bytestring.
.write_text(): open the path and write string data to it.
.write_bytes(): open the path in binary/bytes mode and write data to it.
'''

path = pathlib.Path.cwd() / 'test.md'
path.read_text()


path = pathlib.Path.cwd() / 'testing_modules.py'
path.read_text()

#Paths can also be specified as simple file names, in which case they are interpreted relative 
# to the current working directory. The following example is equivalent to the previous one:
pathlib.Path('test.md').read_text()


#The .resolve() method will find the full path. Below, we confirm that the current working 
# directory is used for simple file names:

path = pathlib.Path('test.md')
path.resolve()


path.resolve().parent == pathlib.Path.cwd()

path.parent == pathlib.Path.cwd()

#Note that when paths are compared, it is their representations that are compared. 
# In the example above, path.parent is not equal to pathlib.Path.cwd(), because path.parent
# is represented by '.' while pathlib.Path.cwd() is represented by '/home/gahjelle/realpython/'.

### Picking Out Components of a Path
'''
The different parts of a path are conveniently available as properties. Basic examples include:

.name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories
'''

#Here are these properties in action:

path

path.name

path.stem

path.suffix

path.parent

path.parent.parent

path.anchor

#Note that .parent returns a new Path object, whereas the other properties return strings. This means for instance that .parent can be chained as in the last example or even combined with / to create completely new paths:
path.parent.parent / ('new' + path.suffix)

### Moving and Deleting Files

if not destination.exists():
    source.replace(destination)

#However, this does leave the door open for a possible race condition. Another process may 
# add a file at the destination path between the execution of the if statement and 
# the .replace() method. If that is a concern, a safer way is to open the destination path
#  for exclusive creation and explicitly copy the source data:

with destination.open(mode='xb') as fid:
    fid.write(source.read_bytes())

#The code above will raise a FileExistsError if destination already exists. Technically, 
# this copies a file. To perform a move, simply delete source after the copy is done (see below). 
# Make sure no exception was raised though.

#When you are renaming files, useful methods might be .with_name() and .with_suffix(). They 
# both return the original path but with the name or the suffix replaced, respectively.

#For instance:

path

path.with_suffix('.py')

path.replace(path.with_suffix('.py'))

#Directories and files can be deleted using .rmdir() and .unlink() respectively. (Again, be 
# careful!)

### Examples

#Counting Files
#There are a few different ways to list many files. The simplest is the .iterdir() method, 
# which iterates over all files in the given directory. The following example combines .iterdir()
#  with the collections.Counter class to count how many files there are of each filetype in 
# the current directory:

import collections
collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())

#BK: To double check above
os.listdir()

#More flexible file listings can be created with the methods .glob() and .rglob() 
# (recursive glob). For instance, pathlib.Path.cwd().glob('*.txt') returns all files with 
# a .txt suffix in the current directory. The following only counts filetypes starting with p:

import collections
collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('*.p*'))

#Display a Directory Tree
#The next example defines a function, tree(), that will print a visual tree representing the
#  file hierarchy, rooted at a given directory. Here, we want to list subdirectories as well, 
# so we use the .rglob() method:

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

#Note that we need to know how far away from the root directory a file is located. To do this, 
# we first use .relative_to() to represent a path relative to the root directory. Then, we count
#  the number of directories (using the .parts property) in the representation. When run, this 
# function creates a visual tree like the following:

tree(pathlib.Path.cwd())

#Find the Last Modified File

#The .iterdir(), .glob(), and .rglob() methods are great fits for generator expressions and list 
#comprehensions. To find the file in a directory that was last modified, you can use the
#  .stat() method to get information about the underlying files. For instance, .stat().st_mtime 
# gives the time of last modification of a file:

from datetime import datetime

#time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
time, file_path = max((f.stat().st_mtime, f) for f in pathlib.Path.cwd().iterdir())
print(datetime.fromtimestamp(time), file_path)

#You can even get the contents of the file that was last modified with a similar expression:

#max((f.stat().st_mtime, f) for f in directory.iterdir())[1].read_text()
max((f.stat().st_mtime, f) for f in pathlib.Path.cwd().iterdir())[1].read_text()

#Create a Unique File Name

#The last example will show how to construct a unique numbered file name based on a template. 
# First, specify a pattern for the file name, with room for a counter. Then, check the 
# existence of the file path created by joining a directory and the file name (with a value 
# for the counter). If it already exists, increase the counter and try again:

def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path

path = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')
#If the directory already contains the files test001.txt and test002.txt, the above code will 
# set path to test003.txt.


### Operating System Differences

pathlib.WindowsPath('test.md')

#There might be times when you need a representation of a path without access to the underlying 
# file system (in which case it could also make sense to represent a Windows path on a 
# non-Windows system or vice versa). This can be done with PurePath objects. These objects 
# support the operations discussed in the section on Path Components but not the methods that 
# access the file system:

path = pathlib.PureWindowsPath(r'C:\Users\gahjelle\realpython\file.txt')
path.name

path.parent

path.exists()

#You can directly instantiate PureWindowsPath or PurePosixPath on all systems. Instantiating 
# PurePath will return one of these objects depending on the operating system you are using.

### Paths as Proper Object

#Independently of the operating system you are using, paths are represented in Posix style, 
# with the forward slash as the path separator. On Windows, you will see something like this:

pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt')

#Still, when a path is converted to a string, it will use the native form, for instance with 
# backslashes on Windows:
str(pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt'))
