
###Map functions

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = map(int, str_nums)
int_nums

#have to use list to get the memembers of map function
list(int_nums)

#map does not change the original function
str_nums


numbers = [-2, -1, 0, 1, 2]

abs_values = list(map(abs, numbers))
abs_values


list(map(float, numbers))

words = ["Welcome", "to", "Real", "Python"]
list(map(len, words))

#Using with lambda
numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers)
list(squared)

#Processing Multiple Input Iterables With map()

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

list(map(pow, first_it, second_it))

#pow() takes two arguments, x and y, and returns x to the power of y. In the first iteration, 
# x will be 1, y will be 4, and the result will be 1. In the second iteration, x will be 2, 
# y will be 5, and the result will be 32, and so on. The final iterable is only as long as the 
# shortest iterable, which is first_it in this case.

list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))


list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))


#Using the Methods of str

string_it = ["processing", "strings", "with", "map"]

list(map(str.capitalize, string_it))

list(map(str.upper, string_it))

list(map(str.lower, string_it))

with_spaces = ["processing ", "  strings", "with   ", " map   "]

list(map(str.strip, with_spaces))

#Note: If you need to supply arguments rather than rely on the default value, then you can use a lambda function.
#Here’s an example that uses str.strip() to remove dots rather than the default whitespace:

with_dots = ["processing..", "...strings", "with....", "..map.."]

list(map(lambda s: s.strip("."), with_dots))

#Removing Punctuation

import re

def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

remove_punctuation("...Python!")


text = """Some people, when confronted with a problem, think
"I know, I'll use regular expressions."
Now they have two problems. Jamie Zawinski"""

words = text.split()
words

list(map(remove_punctuation, words))

###
#Implementing a Caesar Cipher Algorithm
#Julius Caesar, the Roman statesman, used to protect the messages he sent to his generals 
# by encrypting them using a cipher. A Caesar cipher shifts each letter by a number of letters. 
# For example, if you shift the letter a by three, then you get the letter d, and so on.


def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

#ord() takes a Unicode character and returns an integer that represents the Unicode code point of the input character. For example, ord("a") returns 97, and ord("b") returns 98:
ord("a")
ord("b")

"".join(map(rotate_chr, "My secret message goes here."))

#Using Math Operations

def powers(x):
    return x ** 2, x ** 3


numbers = [1, 2, 3, 4]

list(map(powers, numbers))

#BK: same as above
list(map(lambda x: (x**2, x**3), numbers))

import math
numbers = [1, 2, 3, 4, 5, 6, 7]
list(map(math.factorial, numbers))



def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9

celsius_temps = [100, 40, 80]
# Convert to Fahrenheit
list(map(to_fahrenheit, celsius_temps))


fahr_temps = [212, 104, 176]
# Convert to Celsius
list(map(to_celsius, fahr_temps))


# Convert to floating-point
list(map(float, ["12.3", "3.3", "-15.2"]))

# Convert to integer
list(map(int, ["12", "3", "-15"]))

def to_float(number):
    try:
        return float(number.replace(",", "."))
    except ValueError:
        return float("nan")


list(map(to_float, ["12.3", "3,3", "-15.2", "One"]))


#map() and filter()
import math
def is_positive(num):
    return num >= 0

def sanitized_sqrt(numbers):
    cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
    return list(cleaned_iter)


sanitized_sqrt([25, 9, 81, -16, 0])


#map() and reduce()

#Here’s an example that combines map() and reduce() to calculate the total size of all the files that live in your home directory cumulatively:

import functools
import operator
import os
import os.path

files = os.listdir(os.path.expanduser("~"))

functools.reduce(operator.add, map(os.path.getsize, files))

#Processing Tuple-Based Iterables With starmap()

from itertools import starmap

list(starmap(pow, [(2, 7), (4, 3)]))
#In the first example, you use pow() to calculate the power of the first value raised to the 
# second value in each tuple. The tuples will be in the form (base, exponent).
2**7
4**3

list(map(pow, (2, 7), (4, 3)))
2**4
7**3

#Coding With Pythonic Style: Replacing map()

# Transformation function
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5, 6]

# Using map()
list(map(square, numbers))


# Using a list comprehension
[square(x) for x in numbers]

gen_exp = (square(x) for x in numbers)
list(gen_exp)