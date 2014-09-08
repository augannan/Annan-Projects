__author__ = 'augustine'
import turtle
import math
from math import *


def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


class Shape(object):
    shapes_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)


class Hexagon(Shape):

    Hexagons_created = 0
    def __init__(self, side_length:(int,float)):
        super(Hexagon, self).__init__(side_length=side_length)
        self.Hexagons_created += 1
        self.side_length = side_length
        self.area = self.side_length**2 * math.sqrt(12)/3
        self.perimeter = self.side_length*6

    def __str__(self):
        return super(Hexagon, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Hexagon):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        i =0;
        side_length=85
        while i < 6:
            turtle.forward(side_length)
            turtle.left(60)
            i = i + 1

        turtle.done()

if __name__ == "__main__":
    sq = Hexagon(50)
    print(sq)
    sq.draw()
"""
    try:
        sq2 = Hexagon("a string")
    except TypeError as err:
        print(err.args[0], sq.Hexagons_created, sq.Hexagons_created)
"""


class Circle(Shape):

    Circles_created = 0
    def __init__(self, radius:(int,float)):
        super(Circle, self).__init__(radius=radius)
        self.Circles_created += 1
        self.radius = radius
        self.area = self.radius**2 * pi
        self.perimeter = self.radius*2*pi

    def __str__(self):
        return super(Circle, self).__str__()+\
               "; side length: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        radius = 130
        turtle.circle(radius)
        turtle.done()



if __name__ == "__main__":
    sq = Circle(50)
    print(sq)
    sq.draw()
"""
    try:
        sq2 = Circle("a string")
    except TypeError as err:
        print(err.args[0], sq.Circles_created, sq.Circles_created)
"""


class Equilateral_triangle(Shape):

    Equilateral_triangles_created = 0
    def __init__(self, side_length:(int,float)):
        super(Equilateral_triangle, self).__init__(side_length=side_length)
        self.Equilateral_triangles_created += 1
        self.side_length = side_length
        self.area = self.side_length**2 * math.sqrt(3)/4
        self.perimeter = self.side_length*4

    def __str__(self):
        return super(Equilateral_triangle, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Equilateral_triangle):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        side = 120

        i = 0 ;
        while i < 3:
            turtle.forward(side)
            turtle.left(120)
            i = i + 1

        turtle.done()

if __name__ == "__main__":
    sq = Equilateral_triangle(50)
    print(sq)
    sq.draw()

"""
    try:
        sq2 = Equilateral_triangle("a string")
    except TypeError as err:
        print(err.args[0], sq.Equilateral_triangles_created, sq.Equilateral_triangles_created)
"""


class Rectangle(Shape):

    rectangles_created = 0
    def __init__(self, side_length:(int,float), breadth:(int,float)):
        super(Rectangle, self).__init__(side_length=side_length, breadth=breadth)
        self.rectangles_created += 1
        self.side_length = side_length
        self.breadth = breadth
        self.area = self.side_length* self.breadth
        self.perimeter = self.side_length*2 + self.breadth * 2

    def __str__(self):
        return super(Rectangle, self).__str__() +"; side length: "+str(self.side_length)+"; breadth: "+str(self.breadth)

    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.side_length - other.side_length or self.breadth - other.breadth

    def draw(self):
        side_length = 220
        breadth = 120

        turtle.forward(220)
        turtle.left(90)
        turtle.forward(120)
        turtle.left(90)
        turtle.forward(220)
        turtle.left(90)
        turtle.forward(120)
        turtle.done()

if __name__ == "__main__":
    rectangle = Rectangle(220, 120)
    print(rectangle)
    rectangle.draw()


class Rhombus(object):
    rhombus_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)


class Rhombus(Shape):
    """a class representation of rectangle"""
    rhombus_created = 0
    def __init__(self, base:(int,float), height:(int,float)):
        super(Rhombus, self).__init__(base=base, height=height)
        self.rhombus_created += 1
        self.base = base
        self.height = height
        self.area = self.base*self.height
        self.perimeter = 4*self.base

    def __str__(self):
        return super(Rhombus, self).__str__()+"; base "+str(self.base)+", height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Rhombus):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(2):
            turtle.forward(200)
            turtle.left(60)
            turtle.forward(200)
            turtle.left(120)
        turtle.done()


if __name__ == "__main__":
    rhombus = Rhombus(12, 3)
    print(rhombus)
    rhombus.draw()


class Trapezium(Shape):
    """a class representation of rectangle"""
    trapezium_created = 0
    def __init__(self, slant_leg1:(int,float), slant_leg2:(int,float), upper_base:(int,float), lower_base:(int,float), height:(int,float)):
        super(Trapezium, self).__init__(slant_leg1=slant_leg1, slant_leg2=slant_leg2, upper_base=upper_base, lower_base=lower_base, height=height)
        self.trapezium_created += 1
        self.slant_leg1 = slant_leg1
        self.slant_leg2 = slant_leg2
        self.upper_base = upper_base
        self.lower_base = lower_base
        self.height = height
        self.area = 0.5*(self.lower_base+self.upper_base)*self.height
        self.perimeter = self.slant_leg1+self.lower_base+self.upper_base+self.slant_leg2

    def __str__(self):
        return super(Trapezium, self).__str__()+"; slant_leg1 "+str(self.slant_leg1)+"," \
                " slant_leg2: "+str(self.slant_leg2)+", upper_base: "+str(self.upper_base)+", " \
                                    "lower_base: "+str(self.lower_base)+", height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Trapezium):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):

            turtle.forward(100)
            turtle.left(120)
            turtle.forward(60)
            turtle.left(60)
            turtle.forward(40)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(60)
            turtle.done()


if __name__ == "__main__":
    trapezium = Trapezium(3,5,2,4,8)
    print(trapezium)
    trapezium.draw()



class Parallelogram(Shape):
    """a class representation of square"""
    parallelogram_created = 0
    def __init__(self, base:(int,float), height:(int,float)):
        super(Parallelogram, self).__init__(base=base, height=height)
        self.parallelogram_created += 1
        self.base = base
        self.height = height
        self.area = self.base* self.height
        self.perimeter = self.base*2 + self.height * 2

    def __str__(self):
        return super(Parallelogram, self).__str__() +"; base: "+str(self.base)+"; height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Parallelogram):
            raise TypeError
        else:
            return self.base - other.base or self.height - other.height

    def draw(self):
        base = 220
        height = 120
        turtle.forward(300)
        turtle.left(135)
        turtle.forward(200)
        turtle.left(45)
        turtle.forward(300)
        turtle.left(135)
        turtle.forward(200)
        turtle.left(45)
        turtle.done()

if __name__ == "__main__":
    Pa = Parallelogram(220, 120)
    print(Pa)
    Pa.draw()


class Solids(object):
    solids_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.solids_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; surface area : "+str(self.surface_area)+\
               "; Volume: "+str(self.volume)


class Cylinder(Solids):
    """a class representation of square"""
    cylinder_created = 0


    def __init__(self, radius:(int,float), height:(int,float)):
        super(Cylinder, self).__init__(radius=radius, height=height)
        self.cylinder_created += 1
        self.radius = radius
        self.height = height
        self.surface_area =  self.radius*2*pi * self.height
        self.volume = self.radius**2 * pi * self.height

    def __str__(self):
        return super(Cylinder, self).__str__() +"; radius: "+str(self.radius)+"; height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Cylinder):
            raise TypeError
        else:
            return self.radius - other.radius or self.height - other.height



if __name__ == "__main__":
    cy = Cylinder(220, 120)
    print(cy)


class Cone(Solids):

    cone_created = 0


    def __init__(self, radius:(int,float), height:(int,float)):
        super(Cone, self).__init__(radius=radius, height=height)
        self.cone_created += 1
        self.radius = radius
        self.height = height
        self.surface_area =  self.radius*pi * (self.radius + math.sqrt(self.height**2+self.radius**2))
        self.volume = self.radius**2 * pi * self.height/3

    def __str__(self):
        return super(Cone, self).__str__() +"; radius: "+str(self.radius)+"; height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Cone):
            raise TypeError
        else:
            return self.radius - other.radius or self.height - other.height



if __name__ == "__main__":
    con = Cone(10, 20)
    print(con)



class Rectangular_Prism(Solids):

    rectangular_prism_created = 0
    def __init__(self, length:(int,float), breadth:(int,float), height:(int,float)):
        super(Rectangular_Prism, self).__init__(length=length, breadth=breadth, height=height)
        self.solids_created += 1
        self.length = length
        self.breadth = breadth
        self.height = height
        self.volume = self.length*self.breadth*self.height
        self.surface_area = 2*((self.length*self.breadth) + (self.breadth*self.height) + (self.length*self.height))

    def __str__(self):
        return super(Rectangular_Prism, self).__str__()+"; length "+str(self.length)+"," \
                                        " breadth: "+str(self.breadth)+", height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Solids):
            raise TypeError
        else:
            return self.side_length - other.side_length

if __name__ == "__main__":
    rectangular_prism = Rectangular_Prism(5,3,4)
    print(rectangular_prism)