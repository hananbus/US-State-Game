import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Arial", 8, "normal")

screen = Screen()
screen.title("U.S States Game")
us_image = "blank_states_img.gif"
screen.addshape(us_image)
tim = Turtle(us_image)
t = Turtle()
t.hideturtle()
t.penup()

score = 0

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while len(states) > 0:
    user_answer = screen.textinput(f"{score}/50 state's correct", "What's another state's name? ").title()

    if user_answer == "Exit":
        states = pandas.DataFrame(states)
        states.to_csv("missed_states.csv")
        break

    if user_answer in states:
        state_info = data[data.state == user_answer]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(user_answer, font=FONT)
        states.remove(user_answer)
        score += 1
        print(len(states))

