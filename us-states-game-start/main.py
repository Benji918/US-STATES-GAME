from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('U.S States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle = Turtle(shape=img)

display = Turtle()
display.hideturtle()
display.penup()

data = pd.read_csv('50_states.csv')
states = data.state.to_list()

game_continue = True
count = 0
guessed_states = []

while game_continue:
    user_anwser = screen.textinput(title=f'{count}/50 States correct', prompt="Name the other states!").title()
    # Use a for loop to get each state
    if user_anwser == 'Exit':
        # states to learn.csv
        learning_states = [state for state in states if state not in guessed_states]
        convert = pd.DataFrame(learning_states)
        # Save it as a csv file
        convert.to_csv('learning_states.csv')
        break
    for state in states:
        # Check if the user_anwser is among the 50 states
        if user_anwser == state:
            # Get the x & y coordinates of the selected state
            state_name = data[data.state == user_anwser]
            display.goto(x=int(state_name.x), y=int(state_name.y))
            # Write that individual state on the map
            display.write(arg=f'{user_anwser}', align='center', font=('Courier', 9, 'normal'))
            # increase the number of answered states
            count += 1
            guessed_states.append(user_anwser)
        #  Check if the user guessed all the states correctly
        if count == len(states):
            display.goto(0, 0)
            display.write(arg='You guessed all the states correctly!', align='center', font=('Courier', 12, 'bold'))
            # End the game
            game_continue = False


        