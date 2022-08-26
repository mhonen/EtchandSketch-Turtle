#################################################################################
#
# Program: Etch and Sketch
#
# version: 1.0
#
# Description: A copy of the childhood toy etch and sketch using a turtle! LOL
#
##################################################################################


from turtle import Turtle, Screen

# Create Turtle and Screen objects
t = Turtle()
s = Screen()

t.shape("turtle")
t.color("green")
t.pencolor("black")

# Functions for the movement of the turtle.
def move_forwards():
  t.forward(10)

def move_backwards():
  t.backward(10)
  
def move_clockwise():
  t.right(10)
  
def move_counter_clockwise():
  t.left(10)
  
def clear_screen():
  t.clear()
  t.penup()
  t.home()
  t.pendown()
  
# Event Listeners using keys w, s, a, and d
s.listen()

s.onkey(move_forwards, 'w')
s.onkey(move_backwards, 's')
s.onkey(move_clockwise, 'a')
s.onkey(move_counter_clockwise,'d')
s.onkey(clear_screen, 'c')

# Exit screen
s.exitonclick()