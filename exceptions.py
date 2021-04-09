'''
Table of Contents

Exceptions versus Syntax Errors
Raising an Exception
The AssertionError Exception
The try and except Block: Handling Exceptions
The else Clause
Cleaning Up After Using finally
Summing Up
'''

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#The AssertionError Exception

import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

#he try and except Block: Handling Exceptions

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except:
    pass


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')



try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')


#To catch this type of exception and print it to screen, you could use the following code:

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


###
try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')


#The else Clause
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')


#You can also try to run code inside the else clause and catch possible exceptions there as well:

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

#Cleaning Up After Using finally
# 
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')


