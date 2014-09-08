__author__ = 'augustine'


import csv
from Shapes_to_objects import *
file = open("shapes_solids.csv", 'r')
shape_dict = {'Circle': 2, 'Rhombus': 3, 'Parallelogram': 3, 'Hexagon': 2, 'Cone': 3, 'Cylinder': 3,
              'Rectangular_Prism': 4,'Trapezium': 6, 'Equilateral_triangle': 2, 'Rectangle': 3}

with open("shapes_solids.csv", 'r') as csvfile:
    shapes = csv.reader(csvfile, delimiter=' ')
    for row in shapes:
        print(row)
        if len(row) == 0:
            print("EMPTY ROW")
        else:
            try:
                check_len = shape_dict[row[0]] == len(row)
            except KeyError as err:
                    print("I don't get it!!!!!", err.args[0], ";  not in my dictionary")
            if  check_len is True:
                if row[0] == 'Circle':
                    try:
                        cir = Circle(float(row[1]))
                        print(cir)
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Rhombus':
                    try:
                        rhombus = Rhombus(float(row[1]),float(row[2]))
                        print(rhombus)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Parallelogram':
                    try:
                        para = Parallelogram(float(row[1]), float(row[2]))
                        print(para)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Hexagon':
                    try:
                        hexagon = Hexagon (float(row[1]))
                        print(hexagon)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Rectangular Prism':
                    try:
                        prism = Rectangular_Prism(float(row[1]), float(row[2]), float(row[3]))
                        print(prism)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Trapezium':
                    try:
                        trapezium = Trapezium(float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]))
                        print(trapezium)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Cone':
                    try:
                        co = Cone(float(row[1]), float(row[2]))
                        print(co)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Equilateral_triangle':
                    try:
                        triangle = Equilateral_triangle(float(row[1]))
                        print(triangle)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Cylinder':
                    try:
                        cy = Cylinder(float(row[1]), float(row[2]))
                        print(cy)

                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'Rectangle':
                    try:
                        rect = Rectangle(float(row[1]), float(row[2]))
                        print (rect)

                    except ValueError as err:
                        print(err.args[0])
            else:
                print(" Check and Enter all parameters for the geometric figure")