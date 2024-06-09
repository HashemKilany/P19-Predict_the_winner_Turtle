import random
from turtle import Screen, Turtle

screen = Screen()
screen.listen()

screen.setup(width=500, height=400)
user_guess = screen.textinput(title="make a guess!", prompt="which turtle will win the race: pick a color:")
print(user_guess)
colors: list[str] = ['red', 'blue', 'yellow', 'pink', 'green', 'brown']
race_0n = False
all_turtles = []
x = -230
y = -90
for i in range(6):
    new_tur = Turtle(shape="turtle")
    new_tur.penup()
    new_tur.setpos(x, y)
    new_tur.color(colors[i])
    y += 30
    all_turtles.append(new_tur)
if user_guess:
    race_0n = True

while race_0n:
    for tur in all_turtles:
        if tur.xcor() > 230:
            race_0n = False
            winning_color = tur.pencolor()
            if user_guess == winning_color:
                print(f"the winner is {winning_color} you win")
            else:
                print(f"the winner is {winning_color} you lose")
        tur.forward(random.randint(0, 10))

screen.exitonclick()
