# Effective Python Testing With Pytest

'''
Table of Contents

How to Install pytest
What Makes pytest So Useful?
Less Boilerplate
State and Dependency Management
Test Filtering
Test Parametrization
Plugin-Based Architecture
Fixtures: Managing State and Dependencies
When to Create Fixtures
When to Avoid Fixtures
Fixtures at Scale
Marks: Categorizing Tests
Parametrization: Combining Tests
Durations Reports: Fighting Slow Tests
Useful pytest Plugins
pytest-randomly
pytest-cov
pytest-django
pytest-bdd
Conclusion
'''

'''Less Boilerplate
Most functional tests follow the Arrange-Act-Assert model:

Arrange, or set up, the conditions for the test
Act by calling some function or method
Assert that some end condition is true
'''

#Imagine you’d like to write a test suite just to make sure unittest is working properly in your project. You might want to write one test that always passes and one that always fails:

# test_with_unittest.py

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

#You can then run those tests from the command line using the discover option of unittest:
python -m unittest discover

#As expected, one test passed and one failed. You’ve proven that unittest is working, but look at what you had to do:

#Import the TestCase class from unittest
#Create TryTesting, a subclass of TestCase
#Write a method in TryTesting for each test
#Use one of the self.assert* methods from unittest.TestCase to make assertions

#That’s a significant amount of code to write, and because it’s the minimum you need for 
# any test, you’d end up writing the same code over and over. pytest simplifies this 
# workflow by allowing you to use Python’s assert keyword directly:

# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False

#That’s it. You don’t have to deal with any imports or classes. Because you can use the 
# assert keyword, you don’t need to learn or remember all the different self.assert* 
# methods in unittest, either. If you can write an expression that you expect to evaluate
#  to True, then pytest will test it for you. You can run it using the pytest command:

#Here are a few more quick assertion examples:

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }


#Test Filtering
#As your test suite grows, you may find that you want to run just a few tests on a feature and save the full suite for later. pytest provides a few ways of doing this:

#Name-based filtering: You can limit pytest to running only those tests whose fully 
# qualified names match a particular expression. You can do this with the -k parameter.

#Directory scoping: By default, pytest will run only those tests that are in or under the
#  current directory.

#Test categorization: pytest can include or exclude tests from particular categories that
# you define. You can do this with the -m parameter.


### Fixtures: Managing State and Dependencies

#pytest fixtures are a way of providing data, test doubles, or state setup to your tests. 
# Fixtures are functions that can return a wide range of values. Each test that depends 
# on a fixture must explicitly accept that fixture as an argument.


@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",])

def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)