### Python Descriptors: An Introduction

'''
Table of Contents

What Are Python Descriptors?
How Descriptors Work in Python’s Internals
Python Descriptors in Properties
Python Descriptors in Methods and Functions
How Attributes Are Accessed With the Lookup Chain
How to Use Python Descriptors Properly
Why Use Python Descriptors?
Lazy Properties
D.R.Y. Code
Conclusion
'''


# descriptors.py
class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

'''
As a descriptor, it has binding behavior when it’s accessed using dot notation. In this case, the 
descriptor logs a message on the console every time it’s accessed to get or set a value:

When it’s accessed to .__get__() the value, it always returns the value 42.
When it’s accessed to .__set__() a specific value, it raises an AttributeError exception, which is 
the recommended way to implement read-only descriptors.
'''

###How Descriptors Work in Python’s Internals

#Python Descriptors in Properties
#If you want to get the same result as the previous example without explicitly using a Python 
# descriptor, then the most straightforward approach is to use a property. The following example 
# uses a property that logs a message to the console when it’s accessed:

# property_decorator.py
class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

#The example above makes use of decorators to define a property, but as you may know, decorators 
# are just syntactic sugar. The example before, in fact, can be written as follows:

# property_function.py
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

'''
Now you can see that the property has been created by using property(). The signature of this 
function is as follows:

property(fget=None, fset=None, fdel=None, doc=None) -> object
property() returns a property object that implements the descriptor protocol. It uses the parameters
 fget, fset and fdel for the actual implementation of the three methods of the protocol.
'''

###How Attributes Are Accessed With the Lookup Chain

#To understand a little more about Python descriptors and Python internals, you need to 
# understand what happens in Python when an attribute is accessed. In Python, every object has a 
# built-in __dict__ attribute. This is a dictionary that contains all the attributes defined in
# the object itself. To see this in action, consider the following example:

class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

#This code creates a new object and prints the contents of the __dict__ attribute for both the 
# object and the class. Now, run the script and analyze the output to see the __dict__ attributes 
# set:

my_car = Car("red")
print(my_car.__dict__)
print(type(my_car).__dict__)


#The __dict__ attributes are set as expected. Note that, in Python, everything is an object. 
# A class is actually an object as well, so it will also have a __dict__ attribute that contains all the attributes and methods of the class.

#So, what’s going on under the hood when you access an attribute in Python? Let’s make some tests with a modified version of the former example. 
# Consider this code:

# lookup.py
class Vehicle(object):
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")

print(my_car.color)
print(my_car.number_of_weels)
print(my_car.can_fly)

#Here, when you access the attribute color of the instance my_car, you’re actually accessing a 
# single value of the __dict__ attribute of the object my_car. When you access the attribute 
# number_of_wheels of the object my_car, you’re really accessing a single value of 
# the __dict__ attribute of the class Car. Finally, when you access the can_fly attribute, 
# you’re actually accessing it by using the __dict__ attribute of the Vehicle class.


#This means that it’s possible to rewrite the above example like this:

# lookup2.py
class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")

print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_weels'])
print(type(my_car).__base__.__dict__['can_fly'])


print(type(my_car).__dict__['number_of_weels'])

'''
So, what happens when you access the attribute of an object with dot notation? How does the 
interpreter know what you really need? Well, here’s where a concept called the lookup chain comes 
in:

First, you’ll get the result returned from the __get__ method of the data descriptor named after 
the attribute you’re looking for.

If that fails, then you’ll get the value of your object’s __dict__ for the key named after the 
attribute you’re looking for.

If that fails, then you’ll get the result returned from the __get__ method of the non-data 
descriptor named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object type’s __dict__ for the key named 
after the attribute you’re looking for.

If that fails, then you’ll get the value of your object parent type’s __dict__ for the key 
named after the attribute you’re looking for.

If that fails, then the previous step is repeated for all the parent’s types in the method 
resolution order of your object.

If everything else has failed, then you’ll get an AttributeError exception.
'''

###How to Use Python Descriptors Properly

#If you want to use Python descriptors in your code, then you just need to implement the descriptor
# protocol. The most important methods of this protocol are .__get__() and .__set__(), which 
# have the following signature:

__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None

'''
When you implement the protocol, keep these things in mind:

self is the instance of the descriptor you’re writing.
obj is the instance of the object your descriptor is attached to.
type is the type of the object the descriptor is attached to.
In .__set__(), you don’t have the type variable, because you can only call .__set__() on the object. 
In contrast, you can call .__get__() on both the object and the class.
'''
# Another important thing to know is that Python descriptors are instantiated just once per class. 
# That means that every single instance of a class containing a descriptor shares that descriptor 
# instance. This is something that you might not expect and can lead to a classic pitfall, 
# like this:

