
#Defining Main Functions in Python

'''
Table of Contents

A Basic Python main()
Execution Modes in Python
Executing From the Command Line
Importing Into a Module or the Interactive Interpreter
Best Practices for Python Main Functions
Put Most Code Into a Function or Class
Use if __name__ == "__main__" to Control the Execution of Your Code
Create a Function Called main() to Contain the Code You Want to Run
Call Other Functions From main()
Summary of Python Main Function Best Practices
Conclusion
'''


###A Basic Python main()
#In some Python scripts, you may see a function definition and a conditional statement that looks 
# like the example below:

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()



##Execution Modes in Python

#There are two primary ways that you can instruct the Python interpreter to execute or use code:

#You can execute the Python file as a script using the command line.
#You can import the code from one Python file into another file or into the interactive interpreter.
#You can read a lot more about these approaches in How to Run Your Python Scripts. 
# No matter which way of running your code you’re using, Python defines a special variable 
# called __name__ that contains a string whose value depends on how the code is being used.


#Executing From the Command Line

print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))

#In this example, you can see that __name__ has the value '__main__', where the quote 
# symbols (') tell you that the value has the string type.

#Importing Into a Module or the Interactive Interpreter
import execution_methods

#This is my file to test Python's execution methods.
#The variable __name__ tells me which context this file is running in.
#The value of __name__ is: 'execution_methods'

#In this code output, you can see that the Python interpreter executes the three calls to print(). 
# The first two lines of output are exactly the same as when you executed the file as a script on 
# the command line because there are no variables in either of the first two lines. However, 
# there is a difference in the output from the third print().

#When the Python interpreter imports code, the value of __name__ is set to be the same as the 
# name of the module that is being imported. You can see this in the third line of output 
# above. __name__ has the value 'execution_methods', which is the name of the .py file that 
# Python is importing from.

#Note that if you import the module again without quitting Python, there will be no output.

###Best Practices for Python Main Functions

'''
You will learn about four best practices to make sure that your code can serve a dual purpose:

Put most code into a function or class.
Use __name__ to control execution of your code.
Create a function called main() to contain the code you want to run.
Call other functions from main().
'''

###Put Most Code Into a Function or Class
'''
Remember that the Python interpreter executes all the code in a module when it imports the module. 
Sometimes the code you write will have side effects that you want the user to control, such as:

Running a computation that takes a long time
Writing to a file on the disk
Printing information that would clutter the user’s terminal
In these cases, you want the user to control triggering the execution of this code, rather than 
letting the Python interpreter execute the code when it imports your module.

Therefore, the best practice is to include most code inside a function or a class. This is 
because when the Python interpreter encounters the def or class keywords, it only stores those 
definitions for later use and doesn’t actually execute them until you tell it to.
'''

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data


#Now, what will happen when you execute this file as a script on the command line?

#The Python interpreter will execute the from time import sleep and print() lines that are outside
#  the function definition, then it will create the definition of the function called 
# process_data(). Then, the script will exit without doing anything further, because the script 
# does not have any code that executes process_data().

#The code block below shows the result of running this file as a script:

python3 best_practices.py

#Import the Best Practices File in Another Module or the Interactive Interpreter

#When you import this file in an interactive session (or another module), the Python interpreter 
# will perform exactly the same steps as when it executes file as a script.
#Once the Python interpreter imports the file, you can use any variables, classes, or functions 
# defined in the module you’ve imported. To demonstrate this, we will use the interactive Python 
# interpreter. Start the interactive interpreter and then type import best_practices:

import best_practices

'''
Use if __name__ == "__main__" to Control the Execution of Your Code
What if you want process_data() to execute when you run the script from the command line but not 
when the Python interpreter imports the file?

You can use the if __name__ == "__main__" idiom to determine the execution context and 
conditionally run process_data() only when __name__ is equal to "__main__". Add the code 
below to the bottom of your best_practices.py file:
'''

#Now you should check what happens when you import the best_practices.py file from the interactive
#  interpreter (or another module). The example below demonstrates this situation:

import best_practices

#Notice that you get the same behavior as before you added the conditional statement to the 
# end of the file! This is because the __name__ variable had the value "best_practices", 
# so Python did not execute the code inside the block, including process_data(), because 
# the conditional statement evaluated to False.

###Create a Function Called main() to Contain the Code You Want to Run
'''
Although Python does not assign any significance to a function named main(), the best practice is to 
name the entry point function main() anyways. That way, any other programmers who read your script
 immediately know that this function is the starting point of the code that accomplishes the primary
  of the script.

In addition, main() should contain any code that you want to run when the Python interpreter 
executes the file. This is better than putting the code directly into the conditional block 
because a user can reuse main()if they import your module.
'''

#Change the best_practices.py file so that it looks like the code below:

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__":
    main()

#In this example, you added the definition of main() that includes the code that was previously 
# inside the conditional block. Then, you changed the conditional block so that it executes main().
#  If you run this code as a script or import it, you will get the same output as in the previous
#  section.

###Call Other Functions From main()
'''
Another common practice in Python is to have main() execute other functions, rather than including 
the task-accomplishing code in main(). This is especially useful when you can compose your overall
 task from several smaller sub-tasks that can execute independently.

For example, you may have a script that does the following:

Reads a data file from a source that could be a database, a file on the disk, or a web API
Processes the data
Writes the processed data to another location
If you implement each of these sub-tasks in separate functions, then it is easy for a you
 (or another user) to re-use a few of the steps and ignore the ones you don’t want. Then 
 you can create a default workflow in main(), and you can have the best of both worlds.
'''

Modify your best_practices.py file so that it looks like the code below:

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()

#In the output from this execution, you can see that the Python interpreter executed main(), 
# which executed read_data_from_web(), process_data(), and write_data_to_database(). However, 
# you can also import the best_practices.py file and re-use process_data() for a different 
# input data source, as shown below:

import best_practices as bp

data = "Data from a file"
modified_data = bp.process_data(data)

bp.write_data_to_database(modified_data)
bp.write_data_to_database(modified_data)
