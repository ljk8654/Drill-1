import turtle

turtle.shape('turtle')

def turtle_move_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
def turtle_move_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def turtle_move_down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
def turtle_move_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
   

turtle.onkey(turtle_move_up, 'Up')
turtle.onkey(turtle_move_down, 'Down')
turtle.onkey(turtle_move_left, 'Left')
turtle.onkey(turtle_move_right, 'Right')
turtle.listen()
