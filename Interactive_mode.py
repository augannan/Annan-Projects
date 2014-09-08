__author__ = 'augustine'
from Shapes_to_objects import *

my_dictionary = {'1':'Rectangle', '2': 'Circle', '3': 'Equilateral Triangle', '4': 'Rhombus', '5':
    'Parallelogram', '6': 'Hexagon', '7':'Trapezium', '8':'Cylinder', '9': 'Cone',
                 '10':'Rectangular Prism'}
print("********************************************************************************")
print(                   'WELCOME TO THE INTERACTIVE MODE ')
print("********************************************************************************")
print('GEOMETRIC PROPERTIES OF THE FOLLOWING SHAPES AND SOLIDS CAN BE KNOWN HERE'
      "\n****************************************************************************"
      '\nRectangle \nTrapezium \nCircle \nParallelogram\nEquilateral Triangle\nRhombus'
      '\nCylinder \nHexagon \nCone \nRectangular Prism')
print("***************************************************************************************")
print("You cant stop this programme,so beware. Nobody told you to use it.")
print("*****************************************************************************************")


def start():
    figure = input("Enter the name of the geometric figure you want to know its properties ? OR type 'quit' to stop:::")
    while figure != 'quit':
        if figure in my_dictionary.get('1'):
            try:
                length = float(input("Enter the length? OR type 'quit' to enter another shape/solid:::"))
                width = float(input("Enter the width? OR 'type 'quit' to enter another shape/solid:::"))
                rectangle = Rectangle(length, width)
                print(rectangle)
                rectangle.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()
        elif figure in my_dictionary.get('2'):
            try:
                radius = float(input("Enter the radius of the circle? OR "
                                     "'type 'quit' to enter another shape/solid:::"))
                circle = Circle(radius)
                print(circle)
                circle.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()
        elif figure in my_dictionary.get('3'):
            try:
                base = float(input("Enter the base? OR 'type 'quit' to enter another shape/solid:::"))
                triangle = Equilateral_triangle(base)
                print(triangle)
                triangle.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('4'):
            try:
                base = float(input("Enter the base of the rhombus? OR 'type 'quit' to "
                                   "enter another shape/solid:::"))
                height = float(input("Enter the height of the "
                                     "rhombus? OR 'type 'quit' to enter another shape/solid:::"))
                rhombus = Rhombus(base,height)
                print(rhombus)
                rhombus.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('5'):
            try:
                base = float(input("Enter the base of the parallelogram? OR 'type"
                                   " 'quit' to enter another shape/solid:::"))
                height = float(input("Enter the height of the parallelogram? OR"
                                     "'type 'quit' to enter another shape/solid:::"))
                parallelogram = Parallelogram(base,height)
                print(parallelogram)
                parallelogram.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('6'):
            try:
                side_length = float(input("Enter the side length of the hexagon? OR 'type 'quit' "
                                          "to enter another shape/solid:::"))
                hexagon = Hexagon(side_length)
                print(hexagon)
                hexagon.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()
        elif figure in my_dictionary.get('7'):
            try:
                side_length = float(input("Enter the side length of the hexagon? OR 'type 'quit' "
                                          "to enter another shape/solid:::"))
                hexagon = Hexagon(side_length)
                print(hexagon)
                hexagon.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('8'):
            try:
                slant_leg1 = float(input("Enter the length of the left leg? OR "
                                         "type 'quit' to enter another shape/solid:::"))
                slant_leg2 = float(input("Enter the length of the right leg? "
                                         "OR type 'quit' to enter another shape/solid:::"))
                lower_base = float(input("Enter the length of the lower base?  OR "
                                         "'type 'quit' to enter another shape/solid:::"))
                upper_base = float(input("Enter the length of the upper base? "
                                         "OR type 'quit' to enter another shape/solid:::"))
                height = float(input("Enter the height of the Trapezium ? "
                                     "OR type 'quit' to enter another shape/solid:::"))

                trapezium = Trapezium(slant_leg1,slant_leg2,lower_base,upper_base,height)
                print(trapezium)
                trapezium.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('8'):
            try:
                radius = float(input("Enter the radius of the cylinder? OR "
                                     "type 'quit' to enter another shape/solid:::"))
                height = float(input("Enter the height of the shape? OR type 'quit' to enter another shape/solid:::"))
                cylinder = Cylinder(radius,height)
                print(cylinder)
                cylinder.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('9'):
            try:
                radius = float(input("Enter radius of the Cone? OR type 'quit' to enter another shape/solid:::"))
                height = float(input("Enter the height of the shape? OR type 'quit' to enter another shape/solid:::"))

                cone = Cone(radius,height)
                print(cone)
                cone.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure in my_dictionary.get('10'):
            try:
                length = float(input("Enter the length of the prism? OR type 'quit' to enter another shape/solid"))
                height = float(input("Enter the height of the prism? OR type 'quit' to enter another shape/solid"))
                width = float(input("Enter the width of the prism? OR type 'quit' to enter another shape/solid"))
                prism = Rectangular_Prism(length,height,width)
                print(prism)
                prism.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        else:
            print("************************************************************************************************")
            print(" Please enter only figures in the list.Enter them as they appear on the screen{CASE SENSITIVE} " )
            print("**************************************************************************************************")
            print('The available figures are \nRectangle, \nTrapezium, \nCircle, \nParallelogram,'
              '\nEquilateral Triangle,\nRhombus\nCylinder, \nHexagon, \nCone, \nRectangular Prism')
            print("**************************************************************************************************")
            print("**************************************************************************************************")
            return start()



start()


