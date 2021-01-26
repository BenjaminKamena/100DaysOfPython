import turtle
import pandas

screen = turtle.Screen()
screen.title("U.s. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
quessed_states = []

while len(quessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    if answer_state == "Exist":
        missing_status = []
        for state in all_states:
            if state not in quessed_states:
                missing_status.append(state)
            new_data = pandas.DataFrame(missing_status)
            new_data.to_csv("learn.csv")
        break
    if answer_state in all_states:
        quessed_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(state_data.state.item())



def get_mouse_click_coor(x, y):
   print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
