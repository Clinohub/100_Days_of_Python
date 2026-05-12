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
    answer_state = answer.strip().lower()

    if answer_state == "exit" or answer_state == 'logout':
        break

    for state in us_states["state"].values:
        if state.lower() == answer_state:
            if state in guess_states:
                break

            guess_states.append(state)

            state_row = us_states[us_states["state"] == state]

            state_coordinate = (state_row["x"].item(), state_row.y.item())

            game_write.goto(state_coordinate[0], state_coordinate[1])
            game_write.write(f"{state}", False, "center", ("Helvetica", 7, "normal"))

states_to_learn = {
    "missed_states":[]
}
for us_state in us_states.state.values:
    if us_state not in guess_states:
        states_to_learn["missed_states"].append(us_state)

# if empty/(true = not False(False value=None, 0, "", [], {}))
if not states_to_learn["missed_states"]:
    with open("./states_to_learn.csv", 'w') as  empty:
        empty.write("Congratulations! On U.S. States Mastery.\n")
else:
    df = pandas.DataFrame(states_to_learn)
    df.to_csv("./states_to_learn.csv", index=False)

print(states_to_learn)