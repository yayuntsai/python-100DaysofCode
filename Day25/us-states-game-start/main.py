import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #add an image as shape
turtle.shape(image)

# If answer state equals the state name in csv
count_correct = 0
correct_state = []

# input popup
#answer_state = screen.textinput(title="Guess State Name", prompt="What's another state name?")
state_data = pd.read_csv("50_states.csv")
all_states = state_data.state.to_list()
non_guess = []

# Check the different with correct ones
def diff(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    print(s1.symmetric_difference(s2))
    return s1.symmetric_difference(s2)

while count_correct <= 50:
    answer_state_ori = screen.textinput(title=f"{count_correct}/50 State Name",
                                        prompt="What's another state name?")
    answer_state = answer_state_ori.title()

    # Exit the game
    if answer_state == 'Exit':
        break
    # If not ended
    if answer_state in all_states:
        index_of_answer = all_states.index(answer_state)
        correct_state.append(answer_state)
        #print(correct_state)
        state_x = state_data.x[index_of_answer]
        state_y = state_data.y[index_of_answer]
        count_correct += 1 # count the correct number in total

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(answer_state)

    non_guess = diff(correct_state, all_states)


# Show unguess states in csv file
dict = {'state': list(non_guess)}
df = pd.DataFrame(dict)
df.to_csv("states_to_learn.csv")