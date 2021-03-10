import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
# Adding 'blank_states_img.gif' file as a shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states = pd.read_csv("50_states.csv")
state_names = us_states["state"].to_list()

correct_guesses = []
score = 0

# X coordinate list
x_list = us_states["x"].to_list()

# Y coordinates list
y_list = us_states["y"].to_list()

is_user_guessing = True
while is_user_guessing:
    # Pop-up text input
    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"{score}/50 correct.")

    guess_state = us_states[us_states.state == answer_state.title()]
    state_x = guess_state.x
    state_y = guess_state.y

    if answer_state == "exit" or answer_state == "Exit":
        is_user_guessing = False
        # States that are not guessed to be saved to a csv file
        missing_states = []
        for state in state_names:
            if state not in correct_guesses:
                missing_states.append(state)
                missing_state_data = pd.DataFrame(missing_states)
                missing_state_data.to_csv("states_to_learn.csv")
    elif answer_state.title() in correct_guesses:
        # Pass if guess has already been guessed
        pass
    elif answer_state.title() in state_names:
        correct_guesses.append(answer_state.title())
        score += 1

        # Writes name of US state at correct screen x, y coordinates
        state_text = turtle.Turtle()
        state_text.color("black")
        state_text.penup()
        state_text.hideturtle()
        state_text.goto(state_x.item(), state_y.item())
        state_text.write(answer_state.title())

# Alternative method for turtle.exitonclick(). Method will keep turtle window
# open, even after it has been clicked.
turtle.mainloop()
