__author__ = 'augustine'
from math import *
from dimension_validate2 import *
#from numpy import *
from pylab import *


def secant_method(func, first_guess, second_guess, err):
    """
    Computes the roots of a given function given two intelligent guesses,
    close to the root
    :param func: The function .
    :param first_guess: The fist intelligent guess
    :param second_guess: The second intelligent guess
    :param err: The error(Tolerance)
    :return: root, the root of the function
    >>> (secant_method(math.sin, pi/2, 3*pi/2, 1e-6, 6))
    3.141593
    """

    if dim_complete1(func) and dim_complete1(first_guess) and dim_complete1(second_guess) and dim_complete1(err):
        if dim_type(first_guess) and dim_type(second_guess) and dim_type(err)and callable(func):
            if dim_sign(err):
                x0, x1 = first_guess, second_guess
                while fabs(func(x1)) > err and func(x0) != func(x1):
                    x2 = (x0*func(x1) - x1*func(x0))/(func(x1) - func(x0))
                    x0 = x1
                    x1 = x2
                root = x1
                return root
            else:
                raise ValueError(" Enter positive numbers: "+str(err))
        raise TypeError("One or more arguments is(are) not number(s)! Enter a Number")
    raise AttributeError(" Enter all parameters, ")

if __name__ == "__main__":
    print ("***************************************************************************************")
    print ("1a. Secant_method with limits 0.1, 2.0 :" ,secant_method(lambda x:cos(x)+sin(x), pi/2, 3*pi/2, 1e-6))
    print ("1b. Secant_method with limits -2.0, 2.0: " ,secant_method(lambda x:cos(x)+sin(x), -pi/2, pi/2, 1e-6))
    print ("1c. Secant_method with limits -2.0, 2.0: " ,secant_method(lambda x:x**3,5, 6, 1e-9))

