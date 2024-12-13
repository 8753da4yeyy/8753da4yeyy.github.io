"""
Author: Allen Navas
Creation: 08/2024
Purpose: This program will be using the pygame module. It will be used to display images on the screen and also change the icon of the program.
Which will be monkey faces.
"""
import pygame, sys #This will import the pygame module and the sys module
from pygame.locals import* #Means we are importing fucntions in Pygame

#Calls a function "in it" and initializes the pygame
pygame.init()
clock = pygame.time.Clock()

#Window Setup
display_window = pygame.display.set_mode((1080,720)) #Creates a display window and set the width and height.It is a user defined variable
pygame.display.set_caption("Turtle and Monkey's") #Sets the caption of the display window

#Imaging setup for display
monkey_img = pygame.image.load("G:/Github Repositories/8753da4yeyy.github.io/Pygame/Fmoke.jpg").convert() #This will obtain an image from the python project file IF it has been saved in it
Smile = pygame.image.load("G:/Github Repositories/8753da4yeyy.github.io/Pygame/Smile_Moke.jpg").convert()
Abu = pygame.image.load("G:/Github Repositories/8753da4yeyy.github.io/Pygame/BUBU.jpg").convert()
pygame.display.set_icon(Smile) #This will change the icon of the program to the image you have selected

# Palette swap the image of the flying monkey
def palette_swap(surf, old_c, new_c):
    img_copy = pygame.Surface(surf.get_size())
    img_copy.fill(new_c)
    surf.set_colorkey(old_c)
    img_copy.blit(surf, (0, 0))
    return img_copy


# These of sets will be used to move the turtle in the direction of the arrow key pressed
offsets = {
    "up":(0,20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}

# the functions below will be used to move the turtle in the direction of the arrow key pressed
def go_up():
    global turtle_direction
    if turtle_direction != "down":
        turtle_direction = "up"

def go_right():
    global turtle_direction
    if turtle_direction != "left":
        turtle_direction = "right"

def go_down():
    global turtle_direction
    if turtle_direction != "up":
        turtle_direction = "down"

def go_left():
    global turtle_direction
    if turtle_direction != "right":
        turtle_direction = "left"

# Initialize turtle direction
turtle_direction = "up"

#The condition will remain true to have the loop continually display the window
while True: #This will be the main loop of the program
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            pygame.quit() #Helps forcfully quit the game
            sys.exit() #Helps close the application
    display_window.fill((255, 255, 255)) #This will set the background color of the screen

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        go_up()
    if keys[pygame.K_DOWN]:
        go_down()
    if keys[pygame.K_LEFT]:
        go_left()
    if keys[pygame.K_RIGHT]:
        go_right()
    display_window.blit(monkey_img, (0, 0)) #This will make the background as the image you selected. Refer back to line 13 for image assigning
    pygame.draw.rect(display_window,(85, 72, 50), pygame.Rect(30, 40, 100, 100))  # This creates a Rect object based on the X, Y, W, H, valuee. It will also give it color based on the values next to the surface
    display_window.blit(Abu, (250,250))#This will display the image on screen different from the background image. The numbers represent the positioning of said image on screen.
    pygame.display.flip() #Any changes in the game will update displayed in the window in a particular part. "Pygame.display.update()" updates the screen in general
