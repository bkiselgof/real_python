###Formatting with print


#The sep= Keyword Argument
#Adding the keyword argument sep=<str> causes objects to be separated by the string <str> 
# instead of the default single space:

print('foo', 42, 'bar')


print('foo', 42, 'bar', sep='/')


print('foo', 42, 'bar', sep='...')


d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print(k, v, sep=' -> ')


#To squish objects together without any space between them, specify sep='':
print('foo', 42, 'bar', sep='')


#The end= Keyword Argument
#The keyword argument end=<str> causes output to be terminated by <str> instead of the default 
# newline:

if True:
    print('foo', end='/')
    print(42, end='/')
    print('bar')


#For example, if you are displaying values in a loop, you might use end= to cause the values to
#  be displayed on one line, rather than on individual lines:

for n in range(10):
    print(n)


for n in range(20):
    print(n, end=(' ' if n < 9 else '\n'))


#The Python String .format() Method
#The Python string .format() method was introduced in version 2.6. It’s similar in many ways to the string modulo operator, but .format() goes well beyond in versatility. The general form of a Python .format() call is shown below:

<template>.format(<positional_argument(s)>, <keyword_argument(s)>)



#The String .format() Method: Arguments
#Let’s start with a quick example to get you acquainted before you dive into more detail on how to 
# use this method in Python to format strings. For review, here’s the first example from the 
# previous tutorial on the string modulo operator:

print('%d %s cost $%.2f' % (6, 'bananas', 1.74))

#Here, you used the string modulo operator in Python to format the string. Now, you can use 
# Python’s string .format() method to obtain the same result, like this:

print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))

#In this example, <template> is the string '{0} {1} cost ${2}'. The replacement fields 
# are {0}, {1}, and {2}, which contain numbers that correspond to the zero-based positional 
# arguments 6, 'bananas', and 1.74. Each positional argument is inserted into the template in 
# place of its corresponding replacement field:

#The next example uses keyword arguments instead of positional parameters to produce the same result:

print('{quantity} {item} cost ${price}'.format(quantity=6, item='bananas', price=1.74))


#Starting with Python 3.1, you can omit the numbers in the replacement fields, in which case the interpreter assumes sequential order. 
# This is referred to as automatic field numbering:
'{}/{}/{}'.format('foo', 'bar', 'baz')

#On the other hand, it’s fine if the arguments outnumber the replacement fields. The excess arguments simply aren’t used:
'{}{}'.format('foo', 'bar', 'baz')

#While you have to specify positional arguments in sequential order, but you can specify keyword arguments in any arbitrary order:

'{0}/{1}/{2}'.format('foo', 'bar', 'baz')

'{0}/{1}/{2}'.format('bar', 'baz', 'foo')


'{x}/{y}/{z}'.format(x='foo', y='bar', z='baz')

'{x}/{y}/{z}'.format(y='bar', z='baz', x='foo')



#You can specify both positional and keyword arguments in one Python .format() call. Just 
# note that, if you do so, then all the positional arguments must appear before any of the keyword arguments:

'{0}{x}{1}'.format('foo', 'bar', x='baz')

'{0}{x}{1}'.format('foo', x='baz', 'bar')

'''
The String .format() Method: Simple Replacement Fields
As you’ve seen, when you call Python’s .format() method, the <template> string contains replacement fields. These indicate where in the template to insert the arguments to the method. A replacement field consists of three components:

{[<name>][!<conversion>][:<format_spec>]}
'''


#<name> indicates which argument from the argument list is inserted into the Python format 
# string in the given location. It’s either a number for a positional argument or a keyword for a 
# keyword argument. In the following example, the <name> components of the replacement fields
#  are 0, 1, and baz, respectively:

x, y, z = 1, 2, 3
'{0}, {1}, {baz}'.format(x, y, baz=z)


#If an argument is a list, then you can use indices with <name> to access the list’s elements:

a = ['foo', 'bar', 'baz']
'{0[0]}, {0[2]}'.format(a)

'{my_list[0]}, {my_list[2]}'.format(my_list=a)

#Similarly, you can use a key reference with <name> if the corresponding argument is a dictionary:

d = {'key1': 'foo', 'key2': 'bar'}
d['key1']

'{0[key1]}'.format(d)

d['key2']

'{my_dict[key2]}'.format(my_dict=d)

'''
You can also reference object attributes from within a replacement field. In the previous 
tutorial in this series, you learned that virtually every item of data in Python is an object. 
Objects may have attributes assigned to them that are accessed using dot notation:

obj.attr
'''

z = 3+5j
type(z)

z.real
z.imag

#The relevance of object attributes in this context is that you can specify them in a 
# Python .format() replacement field:
z
'real = {0.real}, imag = {0.imag}'.format(z)

'''
The <conversion> Component
The <conversion> component is the middle portion of a replacement field:

{[<name>][!<conversion>][:<format_spec>]}

Python can format an object as a string using three different built-in functions:

str()
repr()
ascii()
By default, the Python .format() method uses str(), but in some instances, you may want to force .format() to use one of the other two. You can do this with the <conversion> component of a replacement field. The possible values for <conversion> are shown in the table below:

Value	Meaning
!s	Convert with str()
!r	Convert with repr()
!a	Convert with ascii()
'''

#The following examples force Python to perform string conversion using str(), repr(), 
# and ascii(), respectively:

'{0!s}'.format(42)

'{0!r}'.format(42)

'{0!a}'.format(42)

#same as above. No need for specifying numbers in positional argument
'{!s}'.format(42)

'''
The <format_spec> Component
The <format_spec> component is the last portion of a replacement field:

{[<name>][!<conversion>][:<format_spec>]}

<format_spec> represents the guts of the Python .format() method’s functionality. It contains information that exerts fine control over how values are formatted prior to being inserted into the template string. The general form is this:

:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]

The ten subcomponents of <format_spec> are specified in the order shown. They control formatting as described in the table below:

Subcomponent	Effect
:	Separates the <format_spec> from the rest of the replacement field
<fill>	Specifies how to pad values that don’t occupy the entire field width
<align>	Specifies how to justify values that don’t occupy the entire field width
<sign>	Controls whether a leading sign is included for numeric values
#	Selects an alternate output form for certain presentation types
0	Causes values to be padded on the left with zeros instead of ASCII space characters
<width>	Specifies the minimum width of the output
<group>	Specifies a grouping character for numeric output
.<prec>	Specifies the number of digits after the decimal point for floating-point presentation types, and the maximum output width for string presentations types
<type>	Specifies the presentation type, which is the type of conversion performed on the corresponding argument
'''

'''
The <type> Subcomponent
Let’s start with <type>, which is the final portion of <format_spec>. The <type> subcomponent specifies the presentation type, which is the type of conversion that’s performed on the corresponding value to produce the output. The possible values are shown below:

Value	Presentation Type
b	Binary integer
c	Single character
d	Decimal integer
e or E	Exponential
f or F	Floating point
g or G	Floating point or Exponential
o	Octal integer
s	String
x or X	Hexadecimal integer
%	Percentage
'''

#These are like the conversion types used with the string modulo operator, and in many cases, 
# they function the same. The following examples demonstrate the similarity:

'%d' % 42

'{:d}'.format(42)

'{0!r}'.format(42.5535)

'%f' % 2.1

'{:f}'.format(2.1)


'%s' % 'foobar'

'{:s}'.format('foobar')


'%x' % 31

'{:x}'.format(31)

#The first presentation type you’ll see is b, which designates binary integer conversion:

'{:b}'.format(257)

#For both the string modulo operator and Python’s .format() method, the g conversion type 
# chooses either floating-point or exponential output, depending on the magnitude of the exponent and the value specified for <prec>:

'{:g}'.format(3.14159)

'{:g}'.format(-123456789.8765)

#G is identical to g except for when the output is exponential, in which case the 'E' will be in
#  uppercase:

'{:G}'.format(-123456789.8765)

'''
The <fill> and <align> Subcomponents
<fill> and <align> control how formatted output is padded and positioned within the specified field width. These subcomponents only have meaning when the formatted field value doesn’t occupy the entire field width, which can only happen if a minimum field width is specified with <width>. If <width> isn’t specified, then <fill> and <align> are effectively ignored. You’ll cover <width> later on in this tutorial.

Here are the possible values for the <align> subcomponent:

<
>
^
=
'''

#A value using the less than sign (<) indicates that the output is left-justified:
'{0:<8s}'.format('foo')

'{0:<8d}'.format(123)

#A value using the greater than sign (>) indicates that the output should be right-justified:
'{0:>8s}'.format('foo')

'{0:>8d}'.format(123)

#A value using a caret (^) indicates that the output should be centered in the output field:
'{0:^8s}'.format('foo')

'{0:^8d}'.format(123)

#<fill> specifies how to fill in extra space when the formatted value doesn’t completely fill the 
# output width. It can be any character except for curly braces ({}). (If you really feel compelled
#  to pad a field with curly braces, then you’ll just have to find another way!)

#Some examples of the use of <fill> are shown below:

'{0:->8s}'.format('foo')

'{0:#<8d}'.format(123)

'{0:*^8s}'.format('foo')







#################################################################################################
### F - Strings

#The magic of f-strings is that you can embed Python expressions directly inside them. Any portion 
# of an f-string that’s enclosed in curly braces ({}) is treated as an expression. The expression is
#  evaluated and converted to string representation, and the result is interpolated into the 
# original string in that location:

s = 'bar'
print(f'foo.{s}.baz')

#The interpreter treats the remainder of the f-string—anything not inside curly braces—just as 
# it would an ordinary string. For example, escape sequences are processed as expected:
s = 'bar'
print(f'foo\n{s}\nbaz')


quantity = 6
item = 'bananas'
price = 1.74
print(f'{quantity} {item} cost ${price}')

#This is equivalent to the following:

quantity = 6
item = 'bananas'
price = 1.74
print('{0} {1} cost ${2}'.format(quantity, item, price))



#Expressions embedded in f-strings can be almost arbitrarily complex. The examples below show 
# some of the possibilities:

#Variables:
quantity, item, price = 6, 'bananas', 1.74
f'{quantity} {item} cost ${price}'

#Arithmetic expressions:
quantity, item, price = 6, 'bananas', 1.74
print(f'Price per item is ${price/quantity}')


x = 6
print(f'{x} cubed is {x**3}')

#Objects of composite types:
a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}

print(f'a = {a} | d = {d}')

#Indexing, slicing, and key references:
a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}

print(f'First item in list a = {a[0]}')


print(f'Last two items in list a = {a[-2:]}')


print(f'List a reversed = {a[::-1]}')


print(f"Dict value for key 'bar' is {d['bar']}")

#Function and method calls:
a = ['foo', 'bar', 'baz', 'qux', 'quux']
print(f'List a has {len(a)} items')


s = 'foobar'
f'--- {s.upper()} ---'


d = {'foo': 1, 'bar': 2}
print(f"Dict value for key 'bar' is {d.get('bar')}")

#Conditional expressions:
x = 3
y = 7
print(f'The larger of {x} and {y} is {x if x > y else y}')


age = 13
f'I am {"a minor" if age < 18 else "an adult"}.'

#Object attributes:
z = 3+5j
z

print(f'real = {z.real}, imag = {z.imag}')






