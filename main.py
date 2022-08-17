import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)

screen.title("Name the States")
correct_list = []
correct_count = 0
while correct_count < 50:
    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        fail_list = []
        for state in state_list:
            if state not in correct_list:
                fail_list.append(state)
        new_data = pandas.DataFrame(fail_list)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        if answer_state not in correct_list:
            correct_list.append(answer_state)
            correct_count += 1
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        correct_state = data[data.state == answer_state]
        state_name.goto(int(correct_state.x), int(correct_state.y))
        state_name.write(answer_state)

if len(correct_list) == 50:
    print("You've answer all the states in the U.S.")




