__author__ = 'augustine'

#from math import *
from numbers import Number


def dim_validate_number(dim):
    """
    Test if dim is a Number .

    >>> dim_validate(5)
    True

    >>> dim_validate("a")
    False

    >>> dim_validate("a string")
    False

    """
    return isinstance(dim, Number)


def dim_validate_positive(dim):
    """
    Test if a dim is positive
    :param dim: dimension
    :return: True or false

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False
    """
    return dim >=0


def dim_validate_argument(dim1, dim2):
    """
    Test for the presence of all arguments
    :param dim1:
    :param dim2:
    :return:

    >>> dim_validate(5)
    False

    >>> dim_validate(5, 6)
    True

    >>> dim_validate(5, "string")
    False

    >>> dim_validate("string", 6)
    False
    """
    if dim1 is not None and dim2 is not None:
        return True

def dim_validate(arg1, arg2):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(4 4)
    True

    >>> dim_validate(-4,2)
    False

    >>> dim_validate("a string", "a string")
    False
    """
    return isinstance(arg1, Number) and isinstance(arg2, Number) and arg1 >= 0 and arg2 >=0


def dim_validate_3arg(arg1, arg2, arg3):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate_3arg(4, 4, 2)
    True

    >>> dim_validate(-4,2, 3)
    False

    >>> dim_validate("a string", "a string" "a string")
    False
    """
    return isinstance(arg1, Number) and isinstance(arg2, Number) and \
           isinstance(arg3,Number) and arg1 > 0 and arg2 > 0 and arg3 > 0
