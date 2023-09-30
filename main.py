# Etech-A-Sketch App

from turtle import Turtle, Screen

ammu = Turtle()
screen = Screen()
screen.listen()


def moving_forward():
    """to move forward"""
    ammu.forward(10)


def moving_backward():
    """to move backward"""
    ammu.backward(10)


def turn_left():
    """to turn left side by 10 degree"""
    new_heading = ammu.heading() + 10
    ammu.setheading(new_heading)


def turn_right():
    """to turn right side by 10 degree"""
    new_heading = ammu.heading() - 10
    ammu.setheading(new_heading)


def clear_screen():
    """it will clear the drawing and goes back to the starting point"""
    ammu.clear()
    ammu.penup()
    ammu.home()
    ammu.pendown()


# from the below code the drawing will take place
screen.onkey(fun=moving_forward, key="w")
screen.onkey(fun=moving_backward, key="s")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

screen.exitonclick()
