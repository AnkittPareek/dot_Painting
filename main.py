import random
import turtle
from random import *

import colorgram
import turtle as t
t.colormode(255)

tim = turtle.Turtle()
screen = turtle.Screen()

colors = colorgram.extract('image.jpg', 30)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

tim.shape("turtle")
tim.penup()
tim.back(230)
tim.setheading(270)
tim.forward(200)
tim.setheading(0)
tim.speed("fastest")
i = 15


def dotted_line():
    for _ in range(i):
        tim.dot(12, (choice(rgb_color)))
        tim.forward(30)


def re_position():
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(15*30)
    tim.setheading(0)


for _ in range(i):
    dotted_line()
    re_position()


screen.exitonclick()
