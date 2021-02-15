import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) #add an image as shape
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

#input popup
answer_state = screen.textinput(title="Guess State Name", prompt="What's another state name?")
turtle.mainloop()