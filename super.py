

#super() in Single Inheritance

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width



class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


square = Square(4)
square.area()

rectangle = Rectangle(2,4)
rectangle.area()


#By using inheritance, you can reduce the amount of code you write while simultaneously reflecting 
# the real-world relationship between rectangles and squares:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square(4)
square.area()


###What Can super() Do for You?
#So what can super() do for you in single inheritance?

#Like in other object-oriented languages, it allows you to call methods of the superclass in your 
# subclass. The primary use case of this is to extend the functionality of the inherited method.

#In the example below, you will create a class Cube that inherits from Square and extends the 
# functionality of .area() (inherited from the Rectangle class through Square) to calculate the
#  surface area and volume of a Cube instance:

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


#Now that you’ve built the classes, let’s look at the surface area and volume of a cube with a 
# side length of 3:

cube = Cube(3)
cube.surface_area()

cube.volume()

###A super() Deep Dive

#Before heading into multiple inheritance, let’s take a quick detour into the mechanics of super().

#While the examples above (and below) call super() without any parameters, super() can also take
#  two parameters: the first is the subclass, and the second parameter is an object that is an 
# instance of that subclass.

#First, let’s see two examples showing what manipulating the first variable can do, using the classes 
# already shown:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

#In Python 3, the super(Square, self) call is equivalent to the parameterless super() call. 
# The first parameter refers to the subclass Square, while the second parameter refers to a 
# Square object which, in this case, is self. You can call super() with other classes as well:

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

#In this example, you are setting Square as the subclass argument to super(), instead of Cube. 
# This causes super() to start searching for a matching method (in this case, .area()) at one 
# level above Square in the instance hierarchy, in this case Rectangle.

#In this specific example, the behavior doesn’t change. But imagine that Square also implemented 
# an .area() function that you wanted to make sure Cube did not use. Calling super() in this way 
# allows you to do that.


###super() in Multiple Inheritance

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

#The problem, though, is that both superclasses (Triangle and Square) define a .area(). Take a 
# second and think about what might happen when you call .area() on RightPyramid, and then try 
# calling it like below:

pyramid = RightPyramid(2, 4)
pyramid.area()

#Method Resolution Order
#The method resolution order (or MRO) tells Python how to search for inherited methods. This comes 
# in handy when you’re using super() because the MRO tells you exactly where Python will look for a
#  method you’re calling with super() and in what order.

#Every class has an .__mro__ attribute that allows us to inspect the order, so let’s do that:
RightPyramid.__mro__

#Luckily, you have some control over how the MRO is constructed. Just by changing the signature of 
# the RightPyramid class, you can search in the order you want, and the methods will resolve 
# correctly:

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

pyramid = RightPyramid(2, 4)
RightPyramid.__mro__


pyramid.area()
