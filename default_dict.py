###Using the Python defaultdict Type for Handling Missing Keys

"""
With Python dictionaries, you have at least four available ways to handle missing keys:

Use .setdefault()
Use .get()
Use the key in dict idiom
Use a try and except block
"""

a_dict = {}
a_dict['missing_key']

a_dict.setdefault('missing_key', 'default value')

a_dict['missing_key']

a_dict.setdefault('missing_key', 'another default value')
a_dict

#In the above code, you use .setdefault() to generate a default value for missing_key. 
# Notice that your dictionary, a_dict, now has a new key called missing_key whose value is 
# 'default value'. This key didn’t exist before you called .setdefault(). Finally, if you 
# call .setdefault() on an existing key, then the call won’t have any effect on the dictionary. 
# Your key will hold the original value instead of the new default value.

#On the other hand, if you use .get(), then you can code something like this:
a_dict = {}
a_dict.get('missing_key', 'default value')

a_dict

#Understanding the Python defaultdict Type
#The Python standard library provides collections, which is a module that implements specialized
#  container types. One of those is the Python defaultdict type, which is an alternative to dict 
# that’s specifically designed to help you out with missing keys. defaultdict is a Python type 
# that inherits from dict:

from collections import defaultdict
issubclass(defaultdict, dict)

'''
The above code shows that the Python defaultdict type is a subclass of dict. This means that 
defaultdict inherits most of the behavior of dict. So, you can say that defaultdict is much 
like an ordinary dictionary.

The main difference between defaultdict and dict is that when you try to access or modify a 
key that’s not present in the dictionary, a default value is automatically given to that key. 
In order to provide this functionality, the Python defaultdict type does two things:

It overrides .__missing__().
It adds .default_factory, a writable instance variable that needs to be provided at the time 
of instantiation.
The instance variable .default_factory will hold the first argument passed into 
defaultdict.__init__(). This argument can take a valid Python callable or None. If a callable 
is provided, then it’ll automatically be called by defaultdict whenever you try to access or 
modify the value associated with a missing key.

Note: All the remaining arguments to the class initializer are treated as if they were passed 
to the initializer of regular dict, including the keyword arguments.
'''
#Take a look at how you can create and properly initialize a defaultdict:
# Correct instantiation
def_dict = defaultdict(list)  # Pass list to .default_factory
def_dict['one'] = 1  # Add a key-value pair
def_dict['missing']  # Access a missing key returns an empty list

def_dict['another_missing'].append(4)  # Modify a missing key
def_dict

###Using the Python defaultdict Type

'''
Grouping Items

A typical use of the Python defaultdict type is to set .default_factory to list and then build a 
dictionary that maps keys to lists of values. With this defaultdict, if you try to get access to 
any missing key, then the dictionary runs the following steps:

Call list() to create a new empty list
Insert the empty list into the dictionary using the missing key as key
Return a reference to that list
This allows you to write code like this:
'''

from collections import defaultdict
dd = defaultdict(list)
dd['key'].append(1)
dd

dd['key'].append(2)
dd

dd['key'].append(3)
dd

#EX
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]


from collections import defaultdict

dep_dd = defaultdict(list)
for department, employee in dep:
    dep_dd[department].append(employee)

dep_dd


#To do this with a regular dictionary, you can use dict.setdefault() as follows:

dep_d = dict()
for department, employee in dep:
    dep_d.setdefault(department, []).append(employee)

dep_d


#Grouping Unique Items

#Continue working with the data of departments and employees from the previous section. 
# After some processing, you realize that a few employees have been duplicated in the database 
# by mistake. You need to clean up the data and remove the duplicated employees from your 
# dep_dd dictionary. To do this, you can use a set as the .default_factory and rewrite your code 
# as follows:

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(set)
for department, employee in dep:
    dep_dd[department].add(employee)

dep_dd


#Counting Items
#If you set .default_factory to int, then your defaultdict will be useful for counting the items 
# in a sequence or collection. When you call int() with no arguments, the function returns 0,
#  which is the typical value you’d use to initialize a counter.

#To continue with the example of the company database, suppose you want to build a dictionary 
# that counts the number of employees per department. In this case, you can code something like
#  this:

from collections import defaultdict
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]
dd = defaultdict(int)
for department, _ in dep:
    dd[department] += 1
dd


from collections import defaultdict
s = 'mississippi'
dd = defaultdict(int)
for letter in s:
    dd[letter] += 1

dd

#Easier with a counter
from collections import Counter
counter = Counter('mississippi')
counter

#Accumulating
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]


from collections import defaultdict

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')


dd

sum(dd.values())