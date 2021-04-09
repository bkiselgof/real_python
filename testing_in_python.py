# Getting Started With Testing in Python

'''
Table of Contents

Testing Your Code
Automated vs. Manual Testing
Unit Tests vs. Integration Tests
Choosing a Test Runner
Writing Your First Test
Where to Write the Test
How to Structure a Simple Test
How to Write Assertions
Side Effects
Executing Your First Test
Executing Test Runners
Understanding Test Output
Running Your Tests From PyCharm
Running Your Tests From Visual Studio Code
Testing for Web Frameworks Like Django and Flask
Why They’re Different From Other Applications
How to Use the Django Test Runner
How to Use unittest and Flask
More Advanced Testing Scenarios
Handling Expected Failures
Isolating Behaviors in Your Application
Writing Integration Tests
Testing Data-Driven Applications
Testing in Multiple Environments
Installing Tox
Configuring Tox for Your Dependencies
Executing Tox
Automating the Execution of Your Tests
What’s Next
Introducing Linters Into Your Application
Keeping Your Test Code Clean
Testing for Performance Degradation Between Changes
Testing for Security Flaws in Your Application
Conclusion
'''


assert sum([1, 2, 3]) == 6, "Should be 6"

#This will not output anything on the REPL because the values are correct.

#If the result from sum() is incorrect, this will fail with an AssertionError and 
# the message "Should be 6". Try an assertion statement again with the wrong values 
# to see an AssertionError:

assert sum([1, 1, 1]) == 6, "Should be 6"

'''
unittest
unittest has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.

unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

unittest requires that:

You put your tests into classes as methods
You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
To convert the earlier example to a unittest test case, you would have to:

Import unittest from the standard library
Create a class called TestSum that inherits from the TestCase class
Convert the test functions into methods by adding self as the first argument
Change the assertions to use the self.assertEqual() method on the TestCase class
Change the command-line entry point to call unittest.main()
'''

#Follow those steps by creating a new file test_sum_unittest.py with the following code:

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()


#nose
#You may find that over time, as you write hundreds or even thousands of tests for your 
# application, it becomes increasingly hard to understand and use the output from 
# unittest.

#nose is compatible with any tests written using the unittest framework and can be used 
# as a drop-in replacement for the unittest test runner. The development of nose as an 
# open-source application fell behind, and a fork called nose2 was created. If you’re 
# starting from scratch, it is recommended that you use nose2 instead of nose.

#To get started with nose2, install nose2 from PyPI and execute it on the command line. 
# nose2 will try to discover all test scripts named test*.py and test cases inheriting 
# from unittest.TestCase in your current directory:

python -m nose2

'''
Note: What if your application is a single script?

You can import any attributes of the script, such as classes, functions, and variables 
by using the built-in __import__() function. Instead of from my_sum import sum, you 
can write the following:

target = __import__("my_sum.py")
sum = target.sum
The benefit of using __import__() is that you don’t have to turn your project folder 
into a package, and you can specify the file name. This is also useful if your filename
 collides with any standard library packages. For example, math.py would collide with 
 the math module.
'''

'''
Executing Test Runners
The Python application that executes your test code, checks the assertions, and gives you test results in your console is called the test runner.

At the bottom of test.py, you added this small snippet of code:

if __name__ == '__main__':
    unittest.main()
This is a command line entry point. It means that if you execute the script alone by running python test.py at the command line, it will call unittest.main(). This executes the test runner by discovering all classes in this file that inherit from unittest.TestCase.

This is one of many ways to execute the unittest test runner. When you have a single test file named test.py, calling python test.py is a great way to get started.

Another way is using the unittest command line. Try this:

$ python -m unittest test
This will execute the same test module (called test) via the command line.

You can provide additional options to change the output. One of those is -v for verbose. Try that next:
'''

'''
python -m unittest -v test

Instead of providing the name of a module containing tests, you can request an auto-discovery using the following:

$ python -m unittest discover
This will search the current directory for any files named test*.py and attempt to test them.

Once you have multiple test files, as long as you follow the test*.py naming pattern, you can provide the name of the directory instead by using the -s flag and the name of the directory:

$ python -m unittest discover -s tests
unittest will run all tests in a single test plan and give you the results.

Lastly, if your source code is not in the directory root and contained in a subdirectory, for example in a folder called src/, you can tell unittest where to execute the tests so that it can import the modules correctly with the -t flag:

$ python -m unittest discover -s tests -t src
unittest will change to the src/ directory, scan for all test*.py files inside the the tests directory, and execute them.
'''

#Understanding Test Output
#That was a very simple example where everything passes, so now you’re going to try a 
# failing test and interpret the output.

#sum() should be able to accept other lists of numeric types, like fractions.

#At the top of the test.py file, add an import statement to import the Fraction type 
# from the fractions module in the standard library:

'''
In the output, you’ll see the following information:

The first line shows the execution results of all the tests, one failed (F) and one passed (.).

The FAIL entry shows some details about the failed test:

The test method name (test_list_fraction)
The test module (test) and the test case (TestSum)
A traceback to the failing line
The details of the assertion with the expected result (1) and the actual result (Fraction(9, 10))
Remember, you can add extra information to the test output by adding the -v flag to the python -m unittest command.
'''

# Testing in Multiple Environments
'''
Configuring Tox for Your Dependencies
Tox is configured via a configuration file in your project directory. The Tox configuration file contains the following:

The command to run in order to execute tests
Any additional packages required before executing
The target Python versions to test against
Instead of having to learn the Tox configuration syntax, you can get a head start by running the quickstart application:

$ tox-quickstart
'''
