__author__ = 'augustine'

import turtle


def draw_trapezium(horizontalside1, slantedside1, horizontalside2, slantedside2):
    turtle.penup()
    turtle.backward(horizontalside1/2)
    turtle.pendown()

    turtle.forward(horizontalside1)
    turtle.left(120)
    turtle.forward(slantedside1)
    turtle.left(60)
    turtle.forward(horizontalside2)
    turtle.left(90)
    turtle.forward(slantedside2)
    turtle.done()
if __name__ == "__main__":
    draw_trapezium(378,250,250,220)
#Hexagon

side = 85

i =0;
while i < 6:
    turtle.forward(side)
    turtle.left(60)
    i = i + 1

turtle.done()

#Equilateral triangle

side = 120

i = 0 ;
while i < 3:
    turtle.forward(side)
    turtle.left(120)
    i = i + 1

turtle.done()

#Rectangle

side1 = 220
side2 = 120

turtle.forward(220)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(220)
turtle.left(90)
turtle.forward(120)
turtle.done()


#Rhombus

side = 150
turtle.forward(side)
turtle.left(135)
turtle.forward(side)
turtle.left(45)
turtle.forward(side)
turtle.left(135)
turtle.forward(side)
turtle.left(45)
turtle.done()

#Circle

radius = 130
turtle.circle(radius)
turtle.done()

#Parallelogram

side1 = 300
side2 = 200
turtle.forward(300)
turtle.left(135)
turtle.forward(200)
turtle.left(45)
turtle.forward(300)
turtle.left(135)
turtle.forward(200)
turtle.left(45)
turtle.done()


#Kite

def draw_kite(diagonal1,diagonal2):
    turtle.left(150)
    turtle.forward(diagonal1)
    turtle.left(40)
    turtle.forward(diagonal2)
    turtle.left(130)
    turtle.forward(diagonal2)
    turtle.left(40)
    turtle.forward(diagonal1)
    turtle.done()
if __name__ == "__main__":
    draw_kite(229, 140)