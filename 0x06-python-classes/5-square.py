#!/usr/bin/python3


class Square:
    """ Reprenting a square"""

    def __init__(self, size=0):
        """
        Initialize a new square.
        args:
        size (int): is the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returning the size of the square """
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square with a # charater."""
        for i in range(0, self.__size):
            [print("#", end="") for k in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
