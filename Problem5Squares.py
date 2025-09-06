# Muhammad Haroon Nasir
# 05/09/25
# Problem 5: Using a draw square function, the program draws 5 squares with the smallest one in the center, and the rest around it.

import turtle


def drawSquare(t, sz):
    # Turtle t draws a square with side size sz
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
alex.speed(5)

# Start with the smallest square in the center
size = 10

for x in range(5):
    # Move to the bottom-left corner of the current square
    # Each square is 10 units larger, so we need to move 5 units left and down
    if x > 0:
        alex.penup()
        alex.backward(5)  # Move left
        alex.right(90)
        alex.forward(5)  # Move down
        alex.left(90)
        alex.pendown()
    
    drawSquare(alex, size)
    size += 10

wn.exitonclick()