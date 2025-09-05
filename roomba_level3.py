# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(0)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here
forward (40)
right (90)
forward (120)
left (90)
x = -1
for loop in range(6):
    forward(320)
    left(270 * x)
    forward(40)
    left(270 * x)
   
    if x == 1:
        x = -1
    else:
        x = 1
forward(320)
right(180)
forward(40)
right(90)
forward (40)
left(90)
forward(120)
right(90)
forward(40)
backward(400)
forward(40)
right(90)
forward(120)
backward(240)
left(90)
forward(320)
right(90) 
forward(120)
right(90)
forward(160)
left(90)
forward(200)
# End your code here
###
 
window.exitonclick()