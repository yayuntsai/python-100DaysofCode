import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #add an image as shape
turtle.shape(image)

# If answer state equals the state name in csv
count_correct = 0
not_guess = 50


# input popup
#answer_state = screen.textinput(title="Guess State Name", prompt="What's another state name?")
state_data = pd.read_csv("50_states.csv")
all_states = state_data.state.to_list()
#print(all_states)
#print(state_data[state_data['state'] == answer_state].x)


while count_correct <= 50:
    answer_state_ori = screen.textinput(title=f"{count_correct}/50 State Name", prompt="What's another state name?")
    answer_state = answer_state_ori.title()

    if answer_state in all_states:
        index_of_answer = all_states.index(answer_state)
        state_x = state_data.x[index_of_answer]
        state_y = state_data.y[index_of_answer]
        count_correct += 1 # count the correct number in total
        not_guess -= 1


        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(answer_state)

turtle.mainloop()