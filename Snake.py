"""
Author: Allen Navas

Using the Turtle module. The code below it is a simple snake game to extend the usage of the Turtle module.
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
DELAY = 200 #milliseconds

offsets = {
    "up":(0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

#Constant window similar to Playground script
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0) #Turns off automatic animation.

#Event Handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

#Now creating Script for <object> below
boogey = turtle.Turtle()
boogey.shape("circle")
boogey.color("blue")
boogey.penup()

def game_loop():
    boogey.clearstamps() # Removes snake made by stamps
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

#Below sets the collision and makes sure the game will reset or end if the snake hits itself or the wall
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.by()
    else:
         snake.append(new_head) # Places new head on snake
         snake.pop(0) # Removes first or last segment of the list in snake.

         for segment in snake: # Drawing the snake
           boogey.goto(segment[0], segment[1])
           boogey.stamp()
           screen.update() # Refreshes screen

    #Rinse and repeat
    turtle.ontimer(game_loop, DELAY) #This will make the snake move.

#Moving object, snake created below
snake = [[0,0], [20,0], [40,0], [60,0]]
snake_direction = "up"

#Drawing the snake
for segment in snake:
    boogey.goto(segment[0], segment[1])
    boogey.stamp()

# Calls function for snake to move below
game_loop()

#Done functions similarly to print and must be put at the end of each script. Finishes Script!
#done()
turtle.done()
