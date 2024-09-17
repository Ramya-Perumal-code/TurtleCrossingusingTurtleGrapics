from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
race_on = False

for n in range(0, 6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[n])
    t.goto(x=-230, y=-100+n*30)
    turtle_list.append(t)

if user_bet:
    race_on = True

while race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


