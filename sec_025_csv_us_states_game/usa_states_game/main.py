import pandas as pd
import turtle
from pointer import Pointer

# screen setup
screen = turtle.Screen()
screen.title("U.S. States Games")
image_path = r"sec_025_csv_us_states_game\usa_states_game\blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)


data = pd.read_csv(r"sec_025_csv_us_states_game\usa_states_game\50_states.csv")
all_states = data.state.to_list()


# setup pointer 
pointer = Pointer()

all_guessed_states = []


while len(all_guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(all_guessed_states)}/50 Guess the State", prompt="What's another state").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in all_guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"sec_025_csv_us_states_game\usa_states_game\states_to_learn.txt")
        break
    
    if not data[data.state == answer_state].empty and answer_state not in all_guessed_states:
        guessed_state = data.loc[data.state == answer_state]
        x_coordinate = int(guessed_state.x.item())
        y_coordinate = int(guessed_state.y.item())
        pointer.new_state(state=answer_state, x_pos=x_coordinate, y_pos=y_coordinate)
        all_guessed_states.append(answer_state)


