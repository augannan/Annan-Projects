__author__ = 'augustine'
from numbers import Number
from math import *


def rectangle_area(length, breadth):

    """
    calculate the area of the rectangle
    :param length: the length
    :param breadth: the breadth
    :return: The area of the rectangle
    >>> rectangle_area (5,4)
    20
    """
    return length * breadth


def rhombus_area(diagonal_length1, diagonal_length2):

    """
    Calculate area of a rhombus from length of both diagonals
    :param diagonal_length1: the length of diagonal1
    :param diagonal_length2: the length of diagonal2
    :return:the area of rhombus(units^2 of length)
    >>> rhombus_area (6,4)
    12
    """
    return 0.5 * diagonal_length1 * diagonal_length2


def rhombus_area_alternative_formulae(base, height):
    """
    Find the area of rhombus
    :param base: length of the base
    :param height: length of the height
    :return:the area of rhombus
    >>> rhombus_area_alternative_formulae(5,7)
    35
    """
    return base*height


def rhombus_perimeter(side):
    """
    Calculate perimeter of a rhombus from side length.
    :param side: side length
    :return:The perimeter(same units as side length)
    >>>rhombus_perimeter(7)
    28
    """
    return 4 * side


def hexagon_perimeter(side):
    """
    Calculate the perimeter of a regular polygon of six sides
    :param side: side length
    :return:The perimeter(same units as side length)
    >>>hexagon_perimeter(5)
    30
    """
    return 6 * side


def circle_area(radius):
    """
    Calculate the area of a circle
    :param radius: the radius
    :return:The area of circle(units^2 of radius)
    >>> circle_area(7)
    154
    """
    return pi*radius*radius


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
    volume = length * breadth * height
    return volume


def equilateral_triangle_area(base, height):
    """
    evaluate the area of an equilateral triangle given the dimensions
    :param base: base of the triangle
    :param height:  perpendicular height of the triangle
    :return:the area of the triangle
    >>>equilateral_triangle_area(4,math.sqrt(12))
    6.928203230275509
    """
    return 0.5*base*height


def equilateral_triangle_area_alternative_formulae(side):
    """
    calculate the area of an equilateral triangle given one side
    :param side: a side of the equilateral triangle
    :return:the area of the equilateral triangle
    >>>equilateral_triangle_area_alternative_formulae(5)
    10.825317547305481
    """
    area = (math.sqrt(3.0)/4.0)*side*side
    return area


def cylinder_volume(radius, height):
    """
    calculate the volume of a cylinder (in unit cube)
    :param radius: radius of the base of the cylinder
    :param height: height of the cylinder
    :return:the volume of the cylinder
    >>> cylinder_volume(7,10)
    1539.3804002589986
    """
    return pi*radius*radius*height


def parallelogram_area(base, height):
    """
    calculate the area of a parallelogram given the base and height
    :param base: base length of the parallelogram
    :param height: perpendicular height of the parallelogram
    :return: the area of the parallelogram
    >>>parallelogram_area(5,12)
    60
    """
    return base*height


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
    return 0.5*(parallel1+parallel2)*height


def kite_area(diagonal1, diagonal2) -> Number:
    """
    Calculate the area of a kite
    :param diagonal1: the length of diagonal1
    :param diagonal2: the length of diagonal2
    :return:the area of a kite(units^2 of a length)
    >>> kite_area(10,20)
    100
    """
    return 0.5*diagonal1*diagonal2


def cube_volume(side):
    """
    'cube volume' calculates the volume of a cube (in cubic units).
    :param side:a side of the cube
    :return:volume of the cube(units^3 of side)
    >>>cube_volume(5)
    125
    """
    return side**3
