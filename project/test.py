import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

'''
Executing Tox
The output of Tox is quite straightforward. It creates an environment for each version, installs your dependencies, and then runs the test commands.

There are some additional command line options that are great to remember.

Run only a single environment, such as Python 3.6:

$ tox -e py36
Recreate the virtual environments, in case your dependencies have changed or site-packages is corrupt:

$ tox -r
Run Tox with less verbose output:

$ tox -q
Running Tox with more verbose output:

$ tox -v
'''


# Passive Linting With flake8

# A popular linter that comments on the style of your code in relation to the PEP 8 specification is flake8.

#You can install flake8 using pip:

$ pip install flake8
#You can then run flake8 over a single file, a folder, or a pattern:

$ flake8 test.py
test.py:6:1: E302 expected 2 blank lines, found 1
test.py:23:1: E305 expected 2 blank lines after class or function definition, found 1
test.py:24:20: W292 no newline at end of file


