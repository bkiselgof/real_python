

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

for key in a_dict:
    print(key, '->', a_dict[key])

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
d_items  # Here d_items is a view of items

for item in a_dict.items():
    print(item)

for key, value in a_dict.items():
    print(key, '->', value)


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
keys

for key in a_dict.keys():
    print(key)

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
values

for value in a_dict.values():
    print(value)


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

'pet' in a_dict.keys()
'apple' in a_dict.values()
'onion' in a_dict.values()

#Modifying Values and Keys

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)  # Apply a 10% discount

prices


#On the other hand, the keys can be added or removed from a dictionary by converting the 
# view returned by .keys() into a list object:
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):  # Use a list instead of a view
    if key == 'orange':
        del prices[key]  # Delete a key from prices

prices


#Turning Keys Into Values and Vice Versa
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

new_dict

#Filtering Items

a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}  # Create a new empty dictionary
for key, value in a_dict.items():
    # If value satisfies the condition, then store it in new_dict
    if value <= 2:
        new_dict[key] = value

new_dict

#Doing Some Calculations

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value  # Accumulate the values in total_income

total_income


#Using Comprehensions

objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
a_dict



#Turning Keys Into Values and Vice Versa: Revisited
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
new_dict

#Filtering Items: Revisited
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
new_dict

#Doing Some Calculations: Revisited
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum([value for value in incomes.values()])
total_income

#A generator expression is more memory efficient.
total_income = sum(value for value in incomes.values())
total_income

#Finally, there is a simpler way to solve this problem by just using incomes.values() directly as an argument to sum():
total_income = sum(incomes.values())
total_income

#Removing Specific Items

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
non_citric

#Sorting a Dictionary
# Python 3.6, and beyond
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
sorted_income


#Iterating in Sorted Order

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
    print(key, '->', incomes[key])

#Sorted by Values

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
def by_value(item):
    return item[1]

for k, v in sorted(incomes.items(), key=by_value):
    print(k, '->', v)


#Easier way but without keys.
for value in sorted(incomes.values()):
    print(value)

#Reversed
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes, reverse=True):
    print(key, '->', incomes[key])


#Iterating Destructively With .popitem()
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break



#Using Some of Python’s Built-In Functions

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices.items()))
new_prices

list(map(discount, prices.items()))


prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(has_low_price, prices.keys()))
low_price

#Using collections.ChainMap
#collections is a useful module from the Python Standard Library that provides specialized 
# container data types. One of these data types is ChainMap, which is a dictionary-like class for 
# creating a single view of multiple mappings (like dictionaries). With ChainMap, you can group 
# multiple dictionaries together to create a single, updateable view.

#Now, suppose you have two (or more) dictionaries, and you need to iterate through them together 
# as one. To achieve this, you can create a ChainMap object and initialize it with your 
# dictionaries:

from collections import ChainMap

fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}

chained_dict = ChainMap(fruit_prices, vegetable_prices)
chained_dict  # A ChainMap object

for key in chained_dict:
    print(key, '->', chained_dict[key])


#ChainMap objects also implement .keys(), values(), and .items() as a standard dictionary does, 
# so you can use these methods to iterate through the dictionary-like object generated by ChainMap, just like you would do with a regular dictionary:

for key, value in chained_dict.items():
    print(key, '->', value)



#Cyclic Iteration With cycle()

from itertools import cycle
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 3  # Define how many times you need to iterate through prices
total_items = times * len(prices)
for item in cycle(prices.items()):
    if not total_items:
        break
    total_items -= 1
    print(item)

#Chained Iteration With chain()
#itertools also provides chain(*iterables), which gets some iterables as arguments and makes an 
# iterator that yields elements from the first iterable until it’s exhausted, then iterates over 
# the next iterable and so on, until all of them are exhausted.

#This allows you to iterate through multiple dictionaries in a chain, like to what you did with 
# collections.ChainMap:

from itertools import chain
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}
for item in chain(fruit_prices.items(), vegetable_prices.items()):
    print(item)


#Using the Dictionary Unpacking Operator (**)

#Python 3.5 brings a new and interesting feature. PEP 448 - Additional Unpacking Generalizations 
# can make your life easier when it comes to iterating through multiple dictionaries in Python. 
# Let’s see how this works with a short example.

#Suppose you have two (or more) dictionaries, and you need to iterate through them together, 
# without using collections.ChainMap or itertools.chain(), as you’ve seen in the previous 
# sections. In this case, you can use the dictionary unpacking operator (**) to merge the 
# two dictionaries into a new one and then iterate through it:

fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
# How to use the unpacking operator **
{**vegetable_prices, **fruit_prices}

# You can use this feature to iterate through multiple dictionaries
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)

[(k, '->', v) for k, v in {**vegetable_prices, **fruit_prices}.items()]


#The dictionary unpacking operator (**) is really an awesome feature in Python. It allows you 
# to merge multiple dictionaries into a new one, as you did in the example with vegetable_prices
#  and fruit_prices. Once you’ve merged the dictionaries with the unpacking operator, you can 
# iterate through the new dictionary as usual.

#It’s important to note that if the dictionaries you’re trying to merge have repeated or common
#  keys, then the values of the right-most dictionary will prevail:

vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': .25}

{**vegetable_prices, **fruit_prices}I 