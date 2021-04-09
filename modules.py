###Python Modules: Overview

'''
There are actually three different ways to define a module in Python:

A module can be written in Python itself.
A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
A built-in module is intrinsically contained in the interpreter, like the itertools module.
'''



#Assuming mod.py is in an appropriate location, which you will learn more about shortly, 
# these objects can be accessed by importing the module as follows:

import mod
print(mod.s)

mod.a

mod.foo(['quux', 'corge', 'grault'])

x = mod.Foo()
x


###The Module Search Path

#Continuing with the above example, let’s take a look at what happens when Python executes the statement:

#import mod
#When the interpreter executes the above import statement, it searches for mod.py in a list of directories 
# assembled from the following sources:

#The directory from which the input script was run or the current directory if the interpreter is being 
# run interactively
#The list of directories contained in the PYTHONPATH environment variable, if it is set. 
# (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
#An installation-dependent list of directories configured at the time Python is installed

import sys
sys.path



path = '/mnt/c/Users/bkise/Documents/repos/real_python'

#sys.path.append(r'C:\Users\john')
sys.path.append(path)
sys.path



import mod

#Once a module has been imported, you can determine the location where it was found with the module’s __file__ attribute:

import mod
mod.__file__


import re
re.__file__


#The import Statement

import mod
mod

#But s and foo remain in the module’s private symbol table and are not meaningful in the local context:
s

foo('quux')


#To be accessed in the local context, names of objects defined in the module must be prefixed by mod:

mod.s

mod.foo('quux')

#from <module_name> import <name(s)>

#Following execution of the above statement, <name(s)> can be referenced in the caller’s environment without the <module_name> prefix:

from mod import s, foo
s

foo('quux')


from mod import Foo
x = Foo()
x


#It is even possible to indiscriminately import everything from a module at one fell swoop:

from <module_name> import *
#This will place the names of all objects from <module_name> into the local symbol table, with the exception of any that begin with the underscore (_) character.

#For example:

from mod import *
s

a

foo

Foo


