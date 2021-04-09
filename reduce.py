

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

my_add(5, 5)

from functools import reduce
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)

"""
The Optional Argument: initializer
The third argument to Python’s reduce(), called initializer, is optional. If you supply a value to initializer, then reduce() will feed it to the first call of function as its first argument.

This means that the first call to function will use the value of initializer and the first item of iterable to perform its first partial computation. After this, reduce() continues working with the subsequent items of iterable.

Here’s an example in which you use my_add() with initializer set to 100:
"""
from functools import reduce
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers, 100)

#If you’re planning to use reduce() to process iterables that may potentially be empty, 
# then it’s good practice to provide a value to initializer. Python’s reduce() will use this value 
# as its default return value when iterable is empty. If you don’t provide an initializer value, 
# then reduce() will raise a TypeError. Take a look at the following example:

from functools import reduce
# Using an initializer value
reduce(my_add, [], 0)  # Use 0 as return value
# Using no initializer value
reduce(my_add, [])  # Raise a TypeError with an empty iterable


from functools import reduce
numbers = [1, 2, 3, 4]
reduce(lambda a, b: a + b, numbers)

from operator import add
from functools import reduce
add(1, 2)
numbers = [1, 2, 3, 4]
reduce(add, numbers)


from functools import reduce
numbers = [1, 2, 3, 4]
reduce(lambda a, b: a * b, numbers)

from operator import mul
from functools import reduce

mul(2, 2)

numbers = [1, 2, 3, 4]
reduce(mul, numbers)

from math import prod
numbers = [1, 2, 3, 4]
prod(numbers)


#Finding the Minimum and Maximum Value

numbers = [3, 5, 2, 4, 7, 1]

# Minimum
min_value, *rest = numbers
for num in rest:
    if num < min_value:
        min_value = num

min_value


# Maximum
max_value, *rest = numbers
for num in rest:
    if num > max_value:
        max_value = num

max_value

#######
numbers = [3, 5, 2, 4, 7, 1]

min_value, *rest = numbers
min_value

rest

####
max_value, *rest = numbers
max_value

rest


from functools import reduce

# Minimum
def my_min_func(a, b):
    return a if a < b else b


# Maximum
def my_max_func(a, b):
    return a if a > b else b


numbers = [3, 5, 2, 4, 7, 1]

reduce(my_min_func, numbers)

reduce(my_max_func, numbers)


#You can also use a lambda function to solve the minimum and maximum problem. Take a look at the following examples:
from functools import reduce
numbers = [3, 5, 2, 4, 7, 1]
# Minimum
reduce(lambda a, b: a if a < b else b, numbers)
# Maximum
reduce(lambda a, b: a if a > b else b, numbers)


def check_all_true(iterable):
    for item in iterable:
        if not item:
            return False
    return True


check_all_true([1, 1, 1, 1, 1])
check_all_true([1, 1, 1, 1, 0])
check_all_true([])

from functools import reduce
reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0])
reduce(lambda a, b: bool(a and b), [1, 1, 1, 2, 1])
reduce(lambda a, b: bool(a and b), [], True)

#Fortunately, Python provides the right tool for solving the all-true problem in a Pythonic, 
# readable, and efficient way: the built-in function all().
#You can use all(iterable) to check if all of the items in iterable are true. Here’s how all() 
# works:

all([1, 1, 1, 1, 1])

all([1, 1, 1, 0, 1])

all([])

#Comparing reduce() and accumulate()

from itertools import accumulate
from operator import add
from functools import reduce

numbers = [1, 2, 3, 4]

list(accumulate(numbers))

reduce(add, numbers)


from itertools import accumulate
from operator import mul
from functools import reduce

numbers = [1, 2, 3, 4]

list(accumulate(numbers, mul))

reduce(mul, numbers)


#To better understand the importance of readability, imagine that you’re starting to learn Python 
# and you’re trying to solve an exercise about calculating the sum of all the even numbers in an 
# iterable.

from functools import reduce

def sum_even(it):
    return reduce(lambda x, y: x + y if not y % 2 else x, it, 0)


sum_even([1, 2, 3, 4])


def sum_even(iterable):
    return sum(num for num in iterable if not num % 2)


sum_even([1, 2, 3, 4])
