

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
vowels

sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]

consonants

#BK - easier way.
[i for i in sentence if i not in 'aeiou']

#You can place the conditional at the end of the statement for simple filtering, but what if you 
# want to change a member value instead of filtering it out? In this case, it’s useful to place 
# the conditional near the beginning of the expression:
#new_list = [expression (if conditional) for member in iterable]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
prices

#set comprehension
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
unique_vowels

#Dictionary comprehension
squares = {i: i * i for i in range(10)}
squares

#Using the Walrus Operator
#It allows you to run an expression while simultaneously assigning the output value to a 
# variable.

import random
def get_weather_data():
    return random.randrange(90, 110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
hot_temps


cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
temps


matrix = [[i for i in range(5)] for _ in range(6)]
matrix
#The outer list comprehension [... for _ in range(6)] creates six rows, while the inner list 
# comprehension [i for i in range(5)] fills each of these rows with values.

matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]

flat = [num for row in matrix for num in row]
flat

#Easier to undersntand with a loop
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)

flat


#Generators for large calculations
sum(i * i for i in range(1000000000))

#map() also operates lazily, meaning memory won’t be an issue if you choose to use it in this 
# case:
sum(map(lambda i: i*i, range(1000000000)))