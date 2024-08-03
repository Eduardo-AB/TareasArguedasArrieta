"""
This module defines a function to print "hello world" to the terminal,
without complying with PEP-8.
"""


def hello_world():
    """Print "hello world" to the terminal."""
    # The opening parenthesis of a function call should
    # go right after the function name
    print ("hello world")

# The funtion definition and the main code should be separated by two blank lines,
# and lines shouldn't be longer than 79 characters
if __name__() == "__main__":
    # Call the function if this file is being executed
    hello_world()
