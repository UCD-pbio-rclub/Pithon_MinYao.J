# Problem 1
# On the python website, find a builtin module. Describe and show examples of some of the useful functions in the module and how they might be utilized by us.

# 9.2. math — Mathematical functions
# It provides access to the mathematical functions defined by the C standard.

import math

#9.2.7. Constants

math.pi
print('math.pi',math.pi)

math.pi / 180.0
print('math.pi / 180.0',math.pi / 180.0)

#9.2.2. Power and logarithmic functions

math.sqrt(10)
print('math.sqrt(10)',math.sqrt(10))

math.log2(10)
print('math.log2(10)',math.log2(10))

#9.2.3. Trigonometric functions

math.cos(137.5)
print('math.cos(137.5)',math.cos(137.5))

math.sin(137.5)
print('math.sin(137.5)',math.sin(137.5))

#24.1. turtle — Turtle graphics

# Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966.

import turtle

turtle.color("black", "red")
turtle.begin_fill()
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.end_fill()

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1: #abs(a) absolute value of a #Return the turtle’s current location (x,y)
        break
end_fill()
done()

