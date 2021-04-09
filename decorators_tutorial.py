### Primer on Python Decorators

'''
Table of Contents

Functions
First-Class Objects
Inner Functions
Returning Functions From Functions
Simple Decorators
Syntactic Sugar!
Reusing Decorators
Decorating Functions With Arguments
Returning Values From Decorated Functions
Who Are You, Really?
A Few Real World Examples
Timing Functions
Debugging Code
Slowing Down Code
Registering Plugins
Is the User Logged In?
Fancy Decorators
Decorating Classes
Nesting Decorators
Decorators With Arguments
Both Please, But Never Mind the Bread
Stateful Decorators
Classes as Decorators
More Real World Examples
Slowing Down Code, Revisited
Creating Singletons
Caching Return Values
Adding Information About Units
Validating JSON
Conclusion
Further Reading
'''


#By definition, a decorator is a function that takes another function and extends the behavior 
# of the latter function without explicitly modifying it.


#Functions
#Before you can understand decorators, you must first understand how functions work. For our 
# purposes, a function returns a value based on the given arguments. Here is a very simple 
# example:

def add_one(number):
    return number + 1

add_one(2)

#In general, functions in Python may also have side effects rather than just turning an input 
# into an output. The print() function is a basic example of this: it returns None while having 
# the side effect of outputting something to the console. However, to understand decorators, it 
# is enough to think about functions as something that turns given arguments into a value


#First-Class Objects
#In Python, functions are first-class objects. This means that functions can be passed around 
# and used as arguments, just like any other object (string, int, float, list, and so on). 
# Consider the following three functions:

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

greet_bob(say_hello)

greet_bob(be_awesome)


#Inner Functions
#It’s possible to define functions inside other functions. Such functions are called inner 
# functions. Here’s an example of a function with two inner functions:

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()
second_child()


#Note that the order in which the inner functions are defined does not matter. Like with any 
# other functions, the printing only happens when the inner functions are executed.

#Furthermore, the inner functions are not defined until the parent function is called. They are 
# locally scoped to parent(): they only exist inside the parent() function as local variables. 
# Try calling first_child(). You should get an error:

#Whenever you call parent(), the inner functions first_child() and second_child() are also called. 
# But because of their local scope, they aren’t available outside of the parent() function.

'''
Returning Functions From Functions
Python also allows you to use functions as return values. The following example returns one of 
the inner functions from the outer parent() function:
'''

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


#Note that you are returning first_child without the parentheses. Recall that this means that you 
# returning a reference to the function first_child. In contrast first_child() with parentheses
#  refers to the result of evaluating the function. This can be seen in the following example:

first = parent(1)
second = parent(2)

first
second


#The somewhat cryptic output simply means that the first variable refers to the local 
# first_child() function inside of parent(), while second points to second_child().

#You can now use first and second as if they are regular functions, even though the functions
#  they point to can’t be accessed directly:

first()
second()

#Finally, note that in the earlier example you executed the inner functions within the parent 
# function, for instance first_child(). However, in this last example, you did not add 
# parentheses to the inner functions—first_child—upon returning. That way, you got a reference 
# to each function that you could call in the future. Make sense?


###Simple Decorators

#Now that you’ve seen that functions are just like any other object in Python, you’re ready 
# to move on and see the magical beast that is the Python decorator. Let’s start with an example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()


#Before moving on, let’s have a look at a second example. Because wrapper() is a regular Python 
# function, the way a decorator modifies a function can change dynamically. So as not to disturb 
# your neighbors, the following example will only run the decorated code during the day:

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
#If you try to call say_whee() after bedtime, nothing will happen:
say_whee()


#Syntactic Sugar!
#The way you decorated say_whee() above is a little clunky. First of all, you end up typing the 
# name say_whee three times. In addition, the decoration gets a bit hidden away below the 
# definition of the function.

#Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes 
# called the “pie” syntax. The following example does the exact same thing as the first decorator 
# example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

#So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how 
# you apply a decorator to a function.


#Reusing Decorators

#Recall that a decorator is just a regular Python function. All the usual tools for easy 
# reusability are available. Let’s move the decorator to its own module that can be used in many other functions.

#Create a file called decorators.py with the following content:

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


#You can now use this new decorator in other files by doing a regular import:

from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

#######
#Change cwd path to current directory
import os
this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
os.chdir(BASE_DIR)
####



#Decorating Functions With Arguments
#Say that you have a function that accepts some arguments. Can you still decorate it? 
# Let’s try:

from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

#Unfortunately, running this code raises an error:
greet("World")

#The problem is that the inner function wrapper_do_twice() does not take any arguments, 
# but name="World" was passed to it. You could fix this by letting wrapper_do_twice() accept 
# one argument, but then it would not work for the say_whee() function you created earlier.

#The solution is to use *args and **kwargs in the inner wrapper function. Then it will accept an 
# arbitrary number of positional and keyword arguments. Rewrite decorators.py as follows:

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

#The wrapper_do_twice() inner function now accepts any number of arguments and passes them on to 
# the function it decorates. Now both your say_whee() and greet() examples works:

say_whee()
greet("World")


#Returning Values From Decorated Functions
#What happens to the return value of decorated functions? Well, that’s up to the decorator to 
# decide. Let’s say you decorate a simple function as follows:

from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

#Try to use it:
hi_adam = return_greeting("Adam")
print(hi_adam)

#Oops, your decorator ate the return value from the function.
#Because the do_twice_wrapper() doesn’t explicitly return a value, the call 
# return_greeting("Adam") ended up returning None.

#To fix this, you need to make sure the wrapper function returns the return value of the 
# decorated function. Change your decorators.py file:
return_greeting("Adam")

#Who Are You, Really?

#A great convenience when working with Python, especially in the interactive shell, is its 
# owerful introspection ability. Introspection is the ability of an object to know about its 
# own attributes at runtime. For instance, a function knows its own name and documentation:

print

print.__name__

help(print)

#The introspection works for functions you define yourself as well:
say_whee
say_whee.__name__
help(say_whee)

#However, after being decorated, say_whee() has gotten very confused about its identity. It now 
# reports being the wrapper_do_twice() inner function inside the do_twice() decorator. Although
#  technically true, this is not very useful information.

#To fix this, decorators should use the @functools.wraps decorator, which will preserve 
# information about the original function. Update decorators.py again:


#from importlib import reload  
#reload(decorators)
from decorators import do_twice

#You do not need to change anything about the decorated say_whee() function:

say_whee
say_whee.__name__
help(say_whee)

#A Few Real World Examples

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


#Timing Functions
#Let’s start by creating a @timer decorator. It will measure the time a function takes to 
# execute and print the duration to the console. Here’s the code:

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)
waste_some_time(999)

#Debugging Code
#The following @debug decorator will print the arguments a function is called with as well as 
# its return value every time the function is called:

import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


#Let’s see how the decorator works in practice by applying it to a simple function with one 
# position and one keyword argument:

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("Benjamin")
make_greeting("Richard", age=112)
make_greeting(name="Dorrisile", age=116)

#The following example calculates an approximation to the mathematical constant e:

import math
from decorators import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

#This example also shows how you can apply a decorator to a function that has already been 
# defined. The approximation of e is based on the following series expansion:

#When calling the approximate_e() function, you can see the @debug decorator at work:
approximate_e(3)

approximate_e(5)
approximate_e(20)

#In this example, you get a decent approximation to the true value e = 2.718281828, adding 
# only 5 terms.

#Registering Plugins
#Decorators don’t have to wrap the function they’re decorating. They can also simply register 
# that a function exists and return it unwrapped. This can be used, for instance, to create a 
# light-weight plug-in architecture:

import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

PLUGINS
randomly_greet("Alice")

#The main benefit of this simple plugin architecture is that you do not need to maintain a 
# list of which plugins exist. That list is created when the plugins register themselves. 
# This makes it trivial to add a new plugin: just define the function and decorate it with 
# @register.

#If you are familiar with globals() in Python, you might see some similarities to how the 
# plugin architecture works. globals() gives access to all global variables in the current 
# scope, including your plugins:

globals()

#Using the @register decorator, you can create your own curated list of interesting variables, 
# effectively hand-picking some functions from globals().

#Fancy Decorators
'''
In the second part of this tutorial, we’ll explore more advanced features, including how to use 
the following:

Decorators on classes
Several decorators on one function
Decorators with arguments
Decorators that can optionally take arguments
Stateful decorators
Classes as decorators
'''

#Decorating Classes
#There are two different ways you can use decorators on classes. The first one is very close to 
# what you have already done with functions: you can decorate the methods of a class. This was 
# one of the motivations for introducing decorators back in the day.

#Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod,
# @property. The @classmethod and @staticmethod decorators are used to define methods inside a 
# class namespace that are not connected to a particular instance of that class. The @property 
# decorator is used to customize getters and setters for class attributes. Expand the box below 
# for an example using these decorators.

########################################################################################################################
### Example using built-in decorators

#The following definition of a Circle class uses the @classmethod, @staticmethod, and @property 
# decorators:

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

'''
In this class:

.cylinder_volume() is a regular method.
.radius is a mutable property: it can be set to a different value. However, by defining a setter 
method, we can do some error testing to make sure it’s not set to a nonsensical negative number. 
Properties are accessed as attributes without parentheses.
.area is an immutable property: properties without .setter() methods can’t be changed. Even 
though it is defined as a method, it can be retrieved as an attribute without parentheses.
.unit_circle() is a class method. It’s not bound to one particular instance of Circle. Class 
methods are often used as factory methods that can create specific instances of the class.
.pi() is a static method. It’s not really dependent on the Circle class, except that it is part
 of its namespace. Static methods can be called on either an instance or the class.
'''

#The Circle class can for example be used as follows:

c = Circle(5)
c.radius

c.area

c.radius = 2
c.area
#set the radius from 5 to 2 above and now it's 2!
c.radius

c.area = 100
#This fails. There is no setter for area. Only a getter

c.cylinder_volume(height=4)

c.radius = -1

c = Circle.unit_circle()
c.radius

c.pi()
Circle.pi()

#######################################################################################################################

#Let’s define a class where we decorate some of its methods using the @debug and @timer 
# decorators from earlier:

from decorators import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

#Using this class, you can see the effect of the decorators:

tw = TimeWaster(1000)
tw.waste_time(999)

#The other way to use decorators on classes is to decorate the whole class. This is, for 
# example, done in the new dataclasses module in Python 3.7:

from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str

#The meaning of the syntax is similar to the function decorators. In the example above, 
# you could have done the decoration by writing PlayingCard = dataclass(PlayingCard).

#A common use of class decorators is to be a simpler alternative to some use-cases of metaclasses.
# th cases, you are changing the definition of a class dynamically.

#Writing a class decorator is very similar to writing a function decorator. The only difference
# is that the decorator will receive a class and not a function as an argument. In fact, all the 
# decorators you saw above will work as class decorators. When you are using them on a class 
# instead of a function, their effect might not be what you want. In the following example, 
# the @timer decorator is applied to a class:

from decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

#Decorating a class does not decorate its methods. Recall that @timer is just shorthand for 
# TimeWaster = timer(TimeWaster).

#Here, @timer only measures the time it takes to instantiate the class:

tw = TimeWaster(1000)

tw.waste_time(999)

#Nesting Decorators
#You can apply several decorators to a function by stacking them on top of each other:

from decorators import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

#Think about this as the decorators being executed in the order they are listed. In other 
# words, @debug calls @do_twice, which calls greet(), or debug(do_twice(greet())):

greet("Eva")

#Observe the difference if we change the order of @debug and @do_twice:

from decorators import debug, do_twice

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")

#In this case, @do_twice will be applied to @debug as well:

greet("Eva")

#Decorators With Arguments
#Sometimes, it’s useful to pass arguments to your decorators. For instance, @do_twice could be 
# extended to a @repeat(num_times) decorator. The number of times to execute the decorated 
# function could then be given as an argument.

#This would allow you to do something like this:

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
 
greet("World")

######

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


#Stateful Decorators
#Sometimes, it’s useful to have a decorator that can keep track of state. As a simple example, 
# we will create a decorator that counts the number of times a function is called.

#Note: In the beginning of this guide, we talked about pure functions returning a value based on 
# given arguments. Stateful decorators are quite the opposite, where the return value will depend 
#  current state, as well as the given arguments.

#In the next section, you will see how to use classes to keep state. But in simple cases, you 
# can also get away with using function attributes:

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

#The state—the number of calls to the function—is stored in the function attribute .num_calls 
# on the wrapper function. Here is the effect of using it:

say_whee()

say_whee()

say_whee.num_calls

#Classes as Decorators
#The typical way to maintain state is by using classes. In this section, you’ll see how to 
# rewrite the @count_calls example from the previous section using a class as a decorator.

#Recall that the decorator syntax @my_decorator is just an easier way of saying 
# func = my_decorator(func). Therefore, if my_decorator is a class, it needs to take func as an
#  argument in its .__init__() method. Furthermore, the class instance needs to be callable so
#  that it can stand in for the decorated function.

#For a class instance to be callable, you implement the special .__call__() method:

class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

#The .__call__() method is executed each time you try to call an instance of the class:
counter = Counter()

counter()

counter()

counter.count


#Therefore, a typical implementation of a decorator class needs to implement .__init__() and .__call__():

import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")

#The .__init__() method must store a reference to the function and can do any other necessary 
# initialization. The .__call__() method will be called instead of the decorated function. 
# It does essentially the same thing as the wrapper() function in our earlier examples. Note 
# that you need to use the functools.update_wrapper() function instead of @functools.wraps.

#This @CountCalls decorator works the same as the one in the previous section:

say_whee()

say_whee()

say_whee.num_calls

