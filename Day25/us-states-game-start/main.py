import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #add an image as shape
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# input popup
answer_state = screen.textinput(title="Guess State Name", prompt="What's another state name?")
state_data = pd.read_csv("50_states.csv")
all_states = state_data.state.to_list()
print(all_states)
#print(state_data[state_data['state'] == answer_state].x)

#turtle.setpos(state_x, state_y)

# If answer state equals the state name in csv
count_correct = 0
for i in all_states:
    if i == answer_state:
        index_of_answer = all_states.index(i)
        state_x = state_data.x[index_of_answer]
        state_y = state_data.y[index_of_answer]
        #state_y = state_data[state_data['state'] == answer_state].y
        count_correct += 1 # count the correct number in total
        print(state_x, state_y)

turtle.mainloop()