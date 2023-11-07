#!/usr/bin/python3
""" Import statment """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This initialize a new square.
        Args:
            size (int): This is the size of the new square.
        """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
