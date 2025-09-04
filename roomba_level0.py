# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
x = 1
for loop in range(4):
    forward(160)
    right(270 * x)
    forward(40)
    right(270 * x)
   
    if x == 1:
        x = -1
    else:
        x = 1
forward(160)
right(270 * x)
forward(40)
right(270 * x)
 
# End your code here
###
 
window.exitonclick()