

#Iterating With for Loops in Python
#A for loop in Python uses collection-based iteration. This means that Python assigns the next item from an iterable to the loop variable on every iteration, like in this example:

values = ["a", "b", "c"]

for value in values:
    print(value)

#Another way
index = 0

for value in values:
    print(index, value)
    index += 1


#Another common way to approach this problem is to use range() combined with len() to create an index automatically. This way, you don’t need to remember to update the index:
for index in range(len(values)):
    value = values[index]
    print(index, value)

#Using Python’s enumerate()
#You can use enumerate() in a loop in almost the same way that you use the original iterable object. Instead of putting the iterable directly after in in the for loop, you put it inside the parentheses of enumerate(). You also have to change the loop variable a little bit, as shown in this example:

for count, value in enumerate(values):
    print(count, value)

#When you use enumerate(), the function gives you back two loop variables:

#The count of the current iteration
#The value of the item at the current iteration

[(i,j) for i, j in enumerate(values)]

{i:j for i, j in enumerate(values)}

#########################
#Argument unpacking example
def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')


f(1, 2, 3)

t = ('foo', 'bar', 'baz')
type(t)

f(*t)
#####################

#To start the count at 1
for count, value in enumerate(values, start=1):
    print(count, value)


#Practicing With Python enumerate()

#Conditional Statements to Skip Items
#Using conditional statements to process items can be a very powerful technique. Sometimes you 
# might need to perform an action on only the very first iteration of a loop, as in this example:

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)



#You can also combine mathematical operations with conditions for the count or index. For 
# instance, you might need to return items from an iterable, but only if they have an even index. 
# You can do this by using enumerate():

def even_items(iterable):
    """Return items from ``iterable`` when their index is even."""
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values

seq = list(range(1, 11))
print(seq)

even_items(seq)

even_items(range(1,10))

def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

even_items(seq)

[i for i in range(10) if not i%2]
[i for i in range(1,11) if not i%2]

alphabet = "abcdefghijklmnopqrstuvwxyz"
even_items(alphabet)

#same output as above
list(alphabet[1::2])


#Understanding Python enumerate()

#One way to write a function meeting these specifications is given in the Python documentation:

def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


seasons = ["Spring", "Summer", "Fall", "Winter"]

my_enumerate(seasons)

list(my_enumerate(seasons))
list(my_enumerate(seasons, start=1))

#Unpacking Arguments With enumerate()

values = ["a", "b"]
enum_instance = enumerate(values)
enum_instance

next(enum_instance)

next(enum_instance)

next(enum_instance)


first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]

for one, two, three in zip(first, second, third):
    print(one, two, three)

#You can combine zip() and enumerate() by using nested argument unpacking:

for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three)


#There are other ways to emulate the behavior of enumerate() combined with zip(). 
# One method uses itertools.count(), which returns consecutive integers by default, starting at 
# zero. You can change the previous example to use itertools.count():

import itertools
for count, one, two, three in zip(itertools.count(), first, second, third):
    print(count, one, two, three)