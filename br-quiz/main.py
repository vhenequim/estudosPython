import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil States Game")
image = "brazil-map-r.gif"
screen.addshape(image)
turtle.shape(image)

br_states_dict = {
    "state" : [],
    "x" : [],
    "y" : [],
}

# Code to get the coords from the map
# noinspection SpellCheckingInspection
# def get_mouse_click_coor(x, y):
#     state_selected = screen.textinput(title="State", prompt="Write").title()
#     if state_selected == "Fim":
#         new_data = pandas.DataFrame(br_states_dict)
#         new_data.to_csv("brazil-states.csv")
#         quit()
#     print(state_selected, x, y)
#     br_states_dict["state"].append(state_selected)
#     br_states_dict["x"].append(x)
#     br_states_dict["y"].append(y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# print(br_states_dict)
# turtle.mainloop()

data = pandas.read_csv("brazil-states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 27:
    awnser_state = screen.textinput(title=f"{len(guessed_states)}/27 States",
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
    if awnser_state in all_states and awnser_state not in guessed_states:
        guessed_states.append(awnser_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == awnser_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

turtle.mainloop()
