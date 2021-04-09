### Python import: Advanced Techniques and Tips

'''
Basic Python import
Modules
Packages
Absolute and Relative Imports
Python’s Import Path
Example: Structure Your Imports
Create and Install a Local Package
Namespace Packages
Imports Style Guide
Resource Imports
Introducing importlib.resources
Example: Use Data Files
Example: Add Icons to Tkinter GUIs
Dynamic Imports
Using importlib
Example: Factory Method With Namespace Packages
Example: A Package of Plugins
The Python Import System
Import Internals
Example: Singletons as Modules
Reloading Modules
Finders and Loaders
Example: Automatically Install From PyPI
Example: Import Data Files
Import Tips and Tricks
Handle Packages Across Python Versions
Handle Missing Packages: Use an Alternative
Handle Missing Packages: Use a Mock Instead
Import Scripts as Modules
Run Python Scripts From ZIP Files
Handle Cyclical Imports
Profile Imports
Conclusion
'''


import math
math.pi


import math
dir()

dir(math)


#Using dir() without any argument shows what’s in the global namespace. To see the contents of the 
# math namespace, you use dir(math).

#You’ve already seen the most straightforward use of import. However, there are other ways to use 
# it that allow you to import specific parts of a module and to rename the module as you import it.

#The following code imports only the pi variable from the math module:

from math import pi
pi


math.pi
#Note that this places pi in the global namespace and not within a math namespace.

#You can also rename modules and attributes as they’re imported:

import math as m
m.pi


from math import pi as PI
PI


###Packages
'''
You can use a package to further organize your modules. The Python.org glossary defines package as 
follows:

A Python module which can contain submodules or recursively, subpackages. Technically, a package is
 a Python module with an __path__ attribute. (Source)

Note that a package is still a module. As a user, you usually don’t need to worry about whether 
you’re importing a module or a package.

In practice, a package typically corresponds to a file directory containing Python files and other
 directories. To create a Python package yourself, you create a directory and a file
 named __init__.py inside it. The __init__.py file contains the contents of the package when 
 it’s treated as a module. It can be left empty.

Note: Directories without an __init__.py file are still treated as packages by Python. However, 
these won’t be regular packages, but something called namespace packages. You’ll learn more 
about them later.
'''

#In general, submodules and subpackages aren’t imported when you import a package. However, you 
# can use __init__.py to include any or all submodules and subpackages if you want. To show a 
# few examples of this behavior, you’ll create a package for saying Hello world in a few different 
# languages. The package will consist of the following directories and files:

world/
│
├── africa/
│   ├── __init__.py
│   └── zimbabwe.py
│
├── europe/
│   ├── __init__.py
│   ├── greece.py
│   ├── norway.py
│   └── spain.py
│
└── __init__.py

#Absolute and Relative Imports

#Recall the source code of world/__init__.py in the earlier example:

from . import africa
#You’ve already seen from...import statements such as from math import pi, but what does the dot (.) 
# in from . import africa mean?

#The dot refers to the current package, and the statement is an example of a relative import. You 
# can read it as “From the current package, import the subpackage africa.”


#There’s an equivalent absolute import statement in which you explicitly name the current package:
from world import africa

#Relative imports must be in the form from...import, and the location you’re importing from must 
# start with a dot.

#The PEP 8 style guide recommends using absolute imports in general. However, relative imports 
# are an alternative for organizing package hierarchies.


#Similarly, Python’s global namespace is also a dictionary. You can access it through globals().
globals()

###Python’s Import Path
'''
You can inspect Python’s import path by printing sys.path. Broadly speaking, this list will contain 
three different kinds of locations:

The directory of the current script (or the current directory if there’s no script, such as when 
Python is running interactively)
The contents of the PYTHONPATH environment variable
Other, installation-dependent directories
'''
sys.path






