__author__ = 'augustine'

from geom_formulae import *
from nose.tools import *


#RECTANGLE
def test_rectangle_area_commutative():
    assert rectangle_area(1,2) == rectangle_area(2,1)

@raises(TypeError)
def test_rectangle_area():
    rectangle_area("a string", 1)

@raises(ValueError)
def test_rectangle_area():
    rectangle_area(1, -1)

@raises(AttributeError)
def test_rectangle_area():
    rectangle_area(None,1)

#RHOMBUS AREA
def test_rhombus_area_commutative():
    assert rhombus_area_alternative_formulae(1,2) == rhombus_area_alternative_formulae (2,1)

@raises(TypeError)
def test_rhombus_area():
    rhombus_area_alternative_formulae("string", 5)

@raises(ValueError)
def test_rhombus_area():
    rhombus_area_alternative_formulae(2,-3)

@raises(AttributeError)
def test_rhombus_area():
    rhombus_area_alternative_formulae(2, None)

#RHOMBUS AREA

def test_rhombus_area_commutative2():
    assert rhombus_area(2,4) == rhombus_area(4,2)

@raises (TypeError)
def test_rhombus_area():
    rhombus_area("a string", 4)

@ raises (ValueError)
def test_rhombus_area():
    rhombus_area(-5, 4)

@raises (AttributeError)
def test_rhombus_area():
    rhombus_area(None, 4)

#RHOMBUS PERIMETER
@raises(TypeError)
def test_rhombus_perimeter():
    rhombus_perimeter("string")

@raises(ValueError)
def test_rhombus_perimeter():
    rhombus_perimeter(-3)

@raises(AttributeError)
def test_rhombus_perimeter():
    rhombus_perimeter(None)


#VOLUME OF RECTANGULAR PRISM
@raises(TypeError)
def test_rectangular_prism_volume():
    rectangular_prism_volume("string", 5, 6) and rectangular_prism_volume("string", "string", 6)

@raises(ValueError)
def test_rectangular_prism_volume():
    rectangular_prism_volume(1, 2, -3) and rectangular_prism_volume(-2, -1, 2) and rectangular_prism_volume(2, 1, -2)\

@raises(AttributeError)
def test_rectangular_prism_volume():
    rectangular_prism_volume(None, 2, 3) and rectangular_prism_volume(None, None, 3)



#AREA OF EQUILATERAL TRIANGLE
def test_triangle_area_commutative():
    assert equilateral_triangle_area(6, 7) == equilateral_triangle_area(7, 6)

@raises (TypeError)
def test_triangle_area():
    equilateral_triangle_area("a string", 8)

@ raises (ValueError)
def test_triangle_area():
    equilateral_triangle_area(-4, 3)

@raises (AttributeError)
def test_triangle_area():
    equilateral_triangle_area(4, None)

#PERIMETER OF HEXAGON
@raises(TypeError)
def test_hexagon_perimeter():
    hexagon_perimeter("string")

@raises(ValueError)
def test_hexagon_perimeter():
    hexagon_perimeter(1)

@raises(AttributeError)
def test_hexagon_perimeter():
    hexagon_perimeter(None,)


#AREA OF A CIRCLE
raises (TypeError)
def test_circle_area():
    circle_area("a string")

@ raises (ValueError)
def test_circle_area():
    circle_area(-4)

@raises (AttributeError)
def test_circle_area():
    circle_area(None)

#VOLUME OF A CYLINDER
@ raises (TypeError)
def test_cylinder_volume():
    cylinder_volume("a string", 6)

@ raises (ValueError)
def test_cylinder_volume():
    cylinder_volume(-8, 9)

@ raises (AttributeError)
def test_cylinder_volume():
    cylinder_volume(None, 4)


#AREA OF A KITE
def test_kite_area_commutative():
    assert kite_area(4,5) == kite_area(5,4)

@ raises (TypeError)
def test_kite_area():
    kite_area(4, "a string")

@ raises (ValueError)
def test_kite_area():
    kite_area(4,-6)

@ raises (AttributeError)
def test_kite_area():
    kite_area(None, 4)


#VOLUME OF A CUBE
@raises (TypeError)
def test_cube_volume():
    cube_volume("a string")

@raises (ValueError)
def test_cube_volume():
    cube_volume(-2)

@raises (AttributeError)
def test_cube_volume():
    cube_volume(None)
