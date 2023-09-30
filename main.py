from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a colour: ")

colour = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["Redturtle", "Orangeturtle", "Yellowturtle", "Greenturtle", "Blueturtle", "purpleturtle"]
initial_distance = - 150

for i in range(0, 6):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colour[i])
    initial_distance += 50
    turtles[i].penup()
    turtles[i].goto(x=-240, y=initial_distance)


if user_bet.lower() not in colour:
    print(f" sorry, {user_bet} is not participating in the race.")
else:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("yaay! you won!")
            else:
                print("sorry you lost")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
