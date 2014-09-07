__author__ = 'augustine'

#from math import *
from numbers import Number


def dim_validate_number(dim):
    """
    Test if dim is a Number .

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False

    """
    return isinstance(dim, Number) and dim >=0


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


def dim_validate(arg1, arg2):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5 5)
    True

    >>> dim_validate(-6,3)
    False

    >>> dim_validate("a string", "a string")
    False
    """
    return isinstance(arg1, Number) and isinstance(arg2, Number) and arg1 >= 0 and arg2 >=0


def dim_validate_3arg(arg1, arg2, arg3):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate_3arg(5, 5, 3)
    True

    >>> dim_validate(-6,3, 4)
    False

    >>> dim_validate("a string", "a string" "a string")
    False
    """
    return isinstance(arg1, Number) and isinstance(arg2, Number) and \
           isinstance(arg3,Number) and arg1 > 0 and arg2 > 0 and arg3 > 0

