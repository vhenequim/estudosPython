import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Code to get the coords from the map
# # noinspection SpellCheckingInspection
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    awnser_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another state name?").title()
    print(awnser_state)
    if awnser_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if awnser_state in all_states:
        guessed_states.append(awnser_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == awnser_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

turtle.mainloop()
