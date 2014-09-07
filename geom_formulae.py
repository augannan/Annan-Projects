__author__ = 'augustine'
#from numbers import Number
from math import *
import math
from numpy import sqrt
from dimension_validate import *


def rectangle_area(length, breadth):

    """
    calculate the area of the rectangle
    :param length: the length
    :param breadth: the breadth
    :return: The area of the rectangle
    >>> rectangle_area (5,4)
    20
    """
    if dim_validate(length,breadth):
        return length*breadth
    elif length is None:
        raise AttributeError("enter value for length")
    elif breadth is None:
        raise AttributeError("enter value for breadth")
    elif type(length) == str:
        raise TypeError("wrong:"+str(length))
    elif type(breadth) == str:
        raise TypeError("wrong:"+str(breadth))
    elif length<0 and breadth > 0:
        raise ValueError("length is less than zero:"+str(length))
    elif breadth <0 and length >0:
        raise ValueError("breadth is less than zero:"+str(breadth))
    else:
        raise ValueError("Both less than Zero "+str(length)+", "+str(breadth))

if __name__ == "__main__":
    samplelength = 6
    samplebreadth = 5
    print("Area of rectangle: ",
          rectangle_area(samplelength, samplebreadth))


def rhombus_area(diagonal_length1, diagonal_length2):

    """
    Calculate area of a rhombus from length of both diagonals
    :param diagonal_length1: the length of diagonal1
    :param diagonal_length2: the length of diagonal2
    :return:the area of rhombus(units^2 of length)
    >>> rhombus_area (6,4)
    12.0
    """
    if dim_validate(diagonal_length1,diagonal_length2):
        return 0.5*diagonal_length1*diagonal_length2
    if diagonal_length1 is None:
        raise AttributeError("enter value for diagonal1")
    if diagonal_length2 is None:
        raise AttributeError("enter value for diagonal2")
    elif type(diagonal_length1) == str:
        raise TypeError("wrong:"+str(diagonal_length1))
    elif type(diagonal_length2) == str:
        raise TypeError("wrong:"+str(diagonal_length2))
    elif diagonal_length1<0 and diagonal_length2 > 0:
        raise ValueError("diagonal1 is less than zero:"+str(diagonal_length1))
    elif diagonal_length2 <0 and diagonal_length1 >0:
        raise ValueError("diagonal2 is less than zero:"+str(diagonal_length2))
    else:
        raise ValueError("Both less than Zero "+str(diagonal_length1)+", "+str(diagonal_length2))

print("Area of a rhombus:", rhombus_area(5, 7))



def rhombus_area_alternative_formulae(base, height):
    """
    Find the area of rhombus
    :param base: length of the base
    :param height: length of the height
    :return:the area of rhombus
    >>> rhombus_area_alternative_formulae(5,7)
    35
    """

    if dim_validate(base, height):
        return  base * height
    elif base is None:
        raise AttributeError("enter value for base")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(base) == str:
        raise TypeError("base value is a string: "+str(base))
    elif type(height) == str:
        raise TypeError("height value is a string:"+str(height))
    elif height < 0 and base >= 0:
        raise ValueError("height is less than 0: "+str(height))
    elif base < 0 and height >= 0:
        raise ValueError("base is less than 0")
    else:
        raise ValueError("your input is not valid, both numbers are negative")

        return base*height
print("Area of a rhombus with alternative formulae is: ", rhombus_area_alternative_formulae(5, 7))


def rhombus_perimeter(side):
    """
    Calculate perimeter of a rhombus from side length.
    :param side: side length
    :return:The perimeter(same units as side length)
    >>> rhombus_perimeter(7)
    28
    """
    if side is None:
        raise AttributeError("The parameter is empty")
    elif dim_validate_number(side):
        return 4 * side
    elif type(side) == str:
        raise TypeError("The length side is a string")
    elif side < 0:
        raise ValueError("The length side is negative" )


print("The perimeter of a rhombus : ", rhombus_perimeter(2))


def hexagon_perimeter(side):
    """
    Calculate the perimeter of a regular polygon of six sides
    :param side: side length
    :return:The perimeter(same units as side length)

    >>> hexagon_perimeter(5)
    30
    """
    if side is None:
        raise AttributeError("The parameter is empty")
    elif dim_validate_number(side):
        return 6 * side
    elif type(side)==str:
        raise TypeError("The length side is a string")
    elif side < 0:
        raise ValueError("The length side is negative" )

print("The perimeter of a hexagon : ", hexagon_perimeter(2))


def circle_area(radius):
    """
    Calculate the area of a circle
    :param radius: the radius
    :return:The area of circle(units^2 of radius)
    >>> circle_area(7)
    153.93804002589985
    """
    if dim_validate_number(radius):
        return pi*radius*radius
    if radius is None:
        raise AttributeError("enter value for radius")
    elif type(radius) == str:
        raise TypeError("wrong:"+str(radius))
    elif radius <0:
        raise ValueError("radius is less than zero:"+str(radius))
    else:
        raise ValueError("your input is not correct:"+str(radius))

print("The area of the circle: ", circle_area(4))


def rectangular_prism_volume(length, breadth, height):
    """
    Calculate the volume of a rectangular prism
    :param length:length side of the prism
    :param breadth:breadth side of the prism
    :param height:height side of the prism
    :return:The volume of a rectangular prism(units^3 of a side)
     >>> rectangular_prism_volume(2, 3, 4)
     24
    """

    if dim_validate_3arg(length, breadth, height):
        return height* length * breadth
    elif length is None and breadth is None and height is None:
        raise AttributeError("Enter values for all parameters")
    elif length is None and breadth is None:
        raise AttributeError("Enter value for length and breadth")
    elif length is None and height is None:
        raise AttributeError("Enter values for length and width")
    elif breadth is None and height is None:
        raise AttributeError("Enter values for breadth and height")
    elif length is None:
        raise AttributeError("enter value for side length")
    elif breadth is None:
        raise AttributeError("enter value for breadth")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(length) == str:
        raise TypeError("short parallel side value is a string: "+str(length))
    elif type(breadth) == str:
        raise TypeError("longer parallel side value is a string:"+str(breadth))
    elif type(height) == str:
        raise TypeError("height is a string:"+str(height))
    elif breadth < 0 and length >= 0 and height > 0:
        raise ValueError("longer parallel side value is less than 0: "+str(breadth))
    elif length < 0 and breadth >= 0 and height > 0:
        raise ValueError("shorter parallel side value is less than 0")
    elif height < 0 and length >= 0 and breadth > 0:
        raise ValueError("height is less than 0")
    else:
        raise ValueError("your inputs are not valid")

print("Volume of a rectangular prism is: ", rectangular_prism_volume(2, 3, 4))


def equilateral_triangle_area(base, height):
    """
    evaluate the area of an equilateral triangle given the dimensions
    :param base: base of the triangle
    :param height:  perpendicular height of the triangle
    :return:the area of the triangle
    >>> equilateral_triangle_area(4,sqrt(12))
    6.9282032302755088
    """
    if dim_validate(base, height):
        return 0.5 * base * height
    elif base is None and height is None:
        raise AttributeError("Enter value for both parameters")
    elif base is None:
        raise AttributeError("enter value for base")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(base) == str and type(height) == str:
        raise TypeError("Parameters enter are strings"+str(base),+str(height))
    elif type(base) == str:
        raise TypeError("base value is a string: "+str(base))
    elif type(height) == str:
        raise TypeError("height value is a string:"+str(height))
    elif height < 0 and base < 0:
        raise ValueError("The base and the height are both less than 0 ")
    elif height < 0 and base >= 0:
        raise ValueError("height is less than 0: "+str(height))
    elif base < 0 and height >= 0:
        raise ValueError("base is less than 0")
    else:
        raise ValueError("your input is not valid, both numbers are negative")
print("Area of an equilateral triangle is: ", equilateral_triangle_area(2, 6))


def equilateral_triangle_area_alternative_formulae(side):
    """
    calculate the area of an equilateral triangle given one side
    :param side: a side of the equilateral triangle
    :return:the area of the equilateral triangle
    >>> equilateral_triangle_area_alternative_formulae(5)
    10.825317547305481
    """
    if side is None:
        raise AttributeError("The parameter is empty")
    if dim_validate_number(side):
        return (math.sqrt(3.0)/4.0)*side*side
    elif side is None:
        raise AttributeError("enter a value for side length")
    elif type(side) == str:
        raise TypeError("side length cannot be a string")
    elif side < 0:
        raise ValueError("side length cannot b negative")
    else:
        raise ValueError("your input is invalid")
print("Area of equilateral triangle for an alternative formulae: ",
        equilateral_triangle_area_alternative_formulae(5))


def cylinder_volume(radius, height):
    """
    calculate the volume of a cylinder (in unit cube)
    :param radius: radius of the base of the cylinder
    :param height: height of the cylinder
    :return:the volume of the cylinder
    >>> cylinder_volume(7,10)
    1539.3804002589986
    """
    if dim_validate(radius, height):
        return pi * radius**2 * height
    elif radius is None:
        raise AttributeError("enter value for the radius")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(radius) == str:
        raise TypeError("radius is a string: "+str(radius))
    elif type(height) == str:
        raise TypeError("height value is a string:"+str(height))
    elif height < 0 and radius > 0:
        raise ValueError("height is less than 0: "+str(height))
    elif radius < 0 and height > 0:
        raise ValueError("radius is less than 0")
    else:
        raise ValueError("your input is not valid")

print("Volume of cylinder : ", cylinder_volume(3, 5))


def parallelogram_area(base, height):
    """
    calculate the area of a parallelogram given the base and height
    :param base: base length of the parallelogram
    :param height: perpendicular height of the parallelogram
    :return: the area of the parallelogram
    >>> parallelogram_area(5,12)
    60
    """
    if dim_validate(base, height):
        return base * height
    elif base is None:
        raise AttributeError("enter value for base")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(base) == str:
        raise TypeError("base value is a string: "+str(base))
    elif type(height) == str:
        raise TypeError("height value is a string:"+str(height))
    elif base < 0 and height > 0:
        raise ValueError("base is less than 0: "+str(base))
    elif height < 0 and base >= 0:
        raise ValueError("height is less than 0")
    else:
        raise ValueError("your input is not valid")

    return base * height
print("Area of a parallelogram:",parallelogram_area( 3, 6))


def trapezium_area(parallel1, parallel2, height) -> Number:
    """
    Calculate the area of a trapezium
    :param parallel1: the parallel1 side
    :param parallel2: the parallel2 side
    :param height: the height
    :return:area of a trapezium(units^2 of a side length)
    >>> trapezium_area(4,5,7)
    31.5
    """
    if dim_validate_3arg(parallel1, parallel2, height):
        return height/2.0 * (parallel1 + parallel2)
    elif parallel1 is None:
        raise AttributeError("enter value for shorter parallel side")
    elif parallel2 is None:
        raise AttributeError("enter value for longer parallel side")
    elif height is None:
        raise AttributeError("enter value for height")
    elif type(parallel1) == str:
        raise TypeError("short parallel side value is a string: "+str(parallel1))
    elif type(parallel2) == str:
        raise TypeError("longer parallel side value is a string:"+str(parallel2))
    elif type(height) == str:
        raise TypeError("height is a string:"+str(height))
    elif parallel2 < 0 and parallel1 > 0 and height > 0:
        raise ValueError("longer parallel side value is less than 0: "+str(parallel2))
    elif parallel1 < 0 and parallel2 >= 0 and height > 0:
        raise ValueError("shorter parallel side value is less than 0")
    elif height < 0 and parallel1 >= 0 and parallel2 > 0:
        raise ValueError("height is less than 0")
    else:
        raise ValueError("your inputs are not valid")

print("Area of a trapezium is: ",trapezium_area(2, 3, 7))


def kite_area(diagonal1, diagonal2) -> Number:
    """
    Calculate the area of a kite
    :param diagonal1: the length of diagonal1
    :param diagonal2: the length of diagonal2
    :return:the area of a kite(units^2 of a length)
    >>> kite_area(10,20)
    100.0
    """
    if dim_validate(diagonal1,diagonal2):
        return 0.5*diagonal1*diagonal2
    if diagonal1 is None:
        raise AttributeError("enter value for diagonal1")
    if diagonal2 is None:
        raise AttributeError("enter value for diagonal2")
    elif type(diagonal1) == str:
        raise TypeError("wrong:"+str(diagonal1))
    elif type(diagonal2) == str:
        raise TypeError("wrong:"+str(diagonal2))
    elif diagonal1<0 and diagonal2 > 0:
        raise ValueError("diagonal1 is less than zero:"+str(diagonal1))
    elif diagonal2 <0 and diagonal1 >0:
        raise ValueError("diagonal2 is less than zero:"+str(diagonal2))
    else:
        raise ValueError("Both less than Zero "+str(diagonal1)+", "+str(diagonal2))

print("Area of kite: ", kite_area(3, 4))


def cube_volume(side):
    """
    'cube volume' calculates the volume of a cube (in cubic units).
    :param side:a side of the cube
    :return:volume of the cube(units^3 of side)
    >>> cube_volume(5)
    125
    """
    if side is None:
        raise AttributeError("The parameter is empty")
    if dim_validate_number(side):
        return side**3
    elif side is None:
        raise AttributeError("enter a value for side length")
    elif type(side) == str:
        raise TypeError("side length cannot be a string")
    elif side < 0:
        raise ValueError("side length cannot be negative")
    else:
        raise ValueError("your input is invalid")
print("Volume of a cube: ", cube_volume(6))
