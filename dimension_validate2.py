__author__ = 'augustine'
from numbers import Number
from numpy import *


def dim_validate(* args, **kwargs):
    result= True
    for arg in args:
        result = result and (isinstance(kwargs(key),Number)) and kwargs(key)>=0
    return result


def dim_validate1(dim1,dim2):
    return isinstance(dim1,dim2)and isinstance(dim2,Number) and dim2>dim1


def dim_validate2(dim1,dim2):
    return isinstance(dim1,Number) and isinstance(dim2,Number) and dim2>dim1


def dim_validate3(*args):
    result = True


def dim_validate(dim):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(dim, Number) and dim >= 0


def dim_sign(dim):
    """
    Tests the sign of the dimension.
    :param dim: dimension to be tested
    :return: True if the sing is positive and False if it is negative
    >>> dim_sign(5)
    True
    >>> dim_sign(-5)
    False
    """
    return dim >= 0


def dim_type(dim):
    """
    Tests if the type of the dimension is a number
    :param dim:the dimension to be tested
    :return:True if the dimension is a number and false if it is anything else
    >>> dim_type(1)
    True
    """
    return isinstance(dim, Number)


def dim_complete1(dim):
    """
    Tests if the argument was entered
    :param dim: the argument
    :return:True if the argument is not None and False otherwise.
    >>> dim_complete(1)
    True
    """
    if dim is not None:
        return True

def dim_complete2(dim):
    """
    Tests if parameter is an even number
    :param dim: the argument
    :return:True if divisible by 2
    >>> dim_complete2(5)
    False
    >>> dim_complete2(4)
    True
    """
    return dim % 2 == 0


def dim_validate4(dim):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate4(5)
    True

    >>> dim_validate4(5)
    True

    >>> ("a string")
    False
    """
    return isinstance(dim, Number)