__author__ = 'augustine'
from numbers import Number

import turtle
import math
from math import *
def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


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
    """a class representation of square"""
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
    """a class representation of rectangle"""
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