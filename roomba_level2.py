# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)
x = 1
###
# Start your code here
for loop in range(20):
    forward(560)
    right(270 * x)
    forward(40)
    right(270 * x)
   
    if x == 1:
        x = -1
    else:
        x = 1
 
 
# End your code here
###
 
window.exitonclick()