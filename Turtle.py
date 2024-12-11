"""
This file named 'turtle.py' is an example of using turtle graphics in Python.
"""

import turtle, sys
from turtle import *
#Importing the Turtle Graphics module
from turtle import *

#Turtle is another gaming programming tool that can be used as other graphical purposes.
#Turtle for this file is used to make the game snake.

#Window Screen W+H
WIDTH = 800
HEIGHT = 500
DELAY = 20 #milliseconds

#Constant window similar to Playground script
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.title("Bababooey")
screen.tracer(0) #Turns off automatic animation


#Below will draw a red box going forward 4 times and right 4 times.
color("Red")
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

#Now creating Script for snake below
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")

my_turtle.forward(100)

#sets animation
move_turtle()

#Done functions similarly to print and must be put at the end of each script
#done()
turtle.done()