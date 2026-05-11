# US States Games ! File Handling
# Working with CSVs and Pandas
# 100 Days of Code ! Day 25

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_write = turtle.Turtle()
game_write.hideturtle()
game_write.penup()

us_states = pandas.read_csv("50_states .csv")

guess_states = []
while len(guess_states) < 50:
    answer =  screen.textinput(
        title=f"{len(guess_states)}/50 Correct States",
        prompt="What's another state's name?"
    )
    answer_state = answer.strip()

    for state in us_states["state"].values:
        if state.lower() == answer_state.lower():
            if state in guess_states:
                break

            guess_states.append(state)

            state_row = us_states[us_states["state"] == state]

            state_coordinate = (state_row["x"].item(), state_row.y.item())

            game_write.goto(state_coordinate[0], state_coordinate[1])
            game_write.write(f"{state}", False, "center", ("Helvetica", 7, "normal"))

screen.exitonclick()