'''
Table of Contents

Namespaces in Python
The Built-In Namespace
The Global Namespace
The Local and Enclosing Namespaces
Variable Scope
Python Namespace Dictionaries
The globals() function
The locals() function
Modify Variables Out of Scope
The global Declaration
The nonlocal Declaration
Best Practices
Conclusion
'''

###The Built-In Namespace

#The built-in namespace contains the names of all of Python’s built-in objects. 
# These are available at all times when Python is running. You can list the objects in the 
# built-in namespace with the following command:

dir(__builtins__)

###The Global Namespace

#The global namespace contains any names defined at the level of the main program. Python 
# creates the global namespace when the main program body starts, and it remains in 
# existence until the interpreter terminates.

###The Local and Enclosing Namespaces

#Functions don’t exist independently from one another only at the level of the main program.
# You can also define one function inside another:

def f():
    print('Start f()')

    def g():
        print('Start g()')
        print('End g()')
        return

    g()

    print('End f()')
    return


f()

#In this example, function g() is defined within the body of f(). Here’s what’s happening in
#  this code:
'''
Lines 1 to 12 define f(), the enclosing function.
Lines 4 to 7 define g(), the enclosed function.
On line 15, the main program calls f().
On line 9, f() calls g().
'''


'''
Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.
Enclosing: If x isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.
Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
Built-in: If it can’t find x anywhere else, then the interpreter tries the built-in scope.
'''


#Example 3: Triple Definition

#Next is a situation in which x is defined here, there, and everywhere. One definition is 
# outside f(), another one is inside f() but outside g(), and a third is inside g():

x = 'global'

def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x)

    g()

f()

#Now the print() statement on line 8 has to distinguish between three different 
# possibilities:

#Line 1 defines x in the global scope.
#Line 4 defines x again in the enclosing scope.
#Line 7 defines x a third time in the scope that’s local to g().
#Here, the LEGB rule dictates that g() sees its own locally defined value of x first. 
# So the print() statement displays 'local'.

#The globals() function
#The built-in function globals() returns a reference to the current global namespace dictionary. You can use it to access the objects in the global namespace. Here’s an example of what it looks like when the main program starts:

type(globals())


globals()

#Now watch what happens when you define a variable in the global scope:
x = 'foo'
globals()

#After the assignment statement x = 'foo', a new item appears in the global namespace 
# dictionary. The dictionary key is the object’s name, x, and the dictionary value is the 
# object’s value, 'foo'.

#You would typically access this object in the usual way, by referring to its symbolic 
# name, x. But you can also access it indirectly through the global namespace dictionary:

x

globals()['x']

x is globals()['x']

#You can create and modify entries in the global namespace using the globals() function as well:

globals()['y'] = 100

globals()

y

globals()['y'] = 3.14159
y


#The locals() function
#Python also provides a corresponding built-in function called locals(). It’s similar to 
# globals() but accesses objects in the local namespace instead:

def f(x, y):
    s = 'foo'
    print(locals())


f(10, 0.5)

###Modify Variables Out of Scope

#A similar situation exists when a function tries to modify a variable outside its local scope. A function can’t modify an immutable object outside its local scope at all:

x = 20
def f():
    x = 40
    print(x)


f()

x
'''
When f() executes the assignment x = 40 on line 3, it creates a new local reference to an integer object whose value is 40. At that point, f() loses the reference to the object named x in the global namespace. So the assignment statement doesn’t affect the global object.

Note that when f() executes print(x) on line 4, it displays 40, the value of its own local x. But after f() terminates, x in the global scope is still 20.
'''

#A function can modify an object of mutable type that’s outside its local scope if it 
# modifies the object in place:

my_list = ['foo', 'bar', 'baz']
def f():
    my_list[1] = 'quux'

f()
my_list

#In this case, my_list is a list, and lists are mutable. f() can make changes inside my_list 
# even though it’s outside the local scope.

#But if f() tries to reassign my_list entirely, then it will create a new local object and 
# won’t modify the global my_list:

my_list = ['foo', 'bar', 'baz']
def f():
    my_list = ['qux', 'quux']

f()
my_list

#The global Declaration
#What if you really do need to modify a value in the global scope from within f()? This is 
# possible in Python using the global declaration:

x = 20
def f():
    global x
    x = 40
    print(x)


f()

x


#As you’ve already seen, globals() returns a reference to the global namespace dictionary. 
# If you wanted to, instead of using a global statement, you could accomplish the same thing 
# using globals():

x = 20
def f():
    globals()['x'] = 40
    print(x)


f()

x

#If the name specified in the global declaration doesn’t exist in the global scope when the function starts, then a combination of the global statement and an assignment will create it:

y

def g():
    global y
    y = 20


g()
y

#You can also specify several comma-separated names in a single global declaration:
x, y, z = 10, 20, 30

def f():
    global x, y, z

#Here, x, y, and z are all declared to refer to objects in the global scope by the single global statement on line 4.

#To modify x in the enclosing scope from inside g(), you need the analogous keyword nonlocal. 
# Names specified after the nonlocal keyword refer to variables in the nearest enclosing scope:

def f():
    x = 20

    def g():
        nonlocal x
        x = 40

    g()
    print(x)


f()
