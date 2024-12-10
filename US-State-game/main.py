import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S.States game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
guess_made=0

while(len(guessed_states)<50 ):
    answer_state=screen.textinput(f"{guess_made}/50 States","What's the another state's name? ").title()
    if answer_state=="Exit":
        missing_state=[ state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")        
        break;
    if answer_state in all_states:
        guess_made+=1
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())
