#!/usr/bin/python3


""""
print square
"""

def print_square(size):
    """
    Checking for any exceptions
    """

    if isinstance(size, int) is False:
        raise TypeError('size must be integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for item in range(0, size):
        print('#' * size)
