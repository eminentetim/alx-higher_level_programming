#!/usr/bin/python3

class MyList(list):
    """
    This class is a subclass of the built_in list class
    """

    def print_sorted(self):
        """
        This prints a sorted list in an ascending order.
        """

        print(sorted(self))
