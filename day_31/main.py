from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# DATA ----------------------------------------------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    # print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# FUNCTIONS ------------------------------------------------------------------ #
def is_known():
    """If user presses the known/tick button, the currently shown word is
    removed from pool of words to learn."""
    to_learn.remove(current_card)

    learn_data = pd.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def next_card():
    """Generate random French word with English translation. French word is
    shown first for a short period of time."""
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card, image=card_front)

    # Flips to English translation after 5 seconds
    flip_timer = win.after(5000, func=flip_card)


def flip_card():
    """Flips to English side of card."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(flash_card, image=card_back)


# UI SETUP ------------------------------------------------------------------- #
win = Tk()
win.title("Flash Card App")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
correct_tick = PhotoImage(file="images/right.png")
wrong_cross = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0,
                bg=BACKGROUND_COLOR)
flash_card = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="",
                                font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="",
                               font=("Ariel", 60, "bold"))

flip_timer = win.after(5000, func=flip_card)

# Buttons
unknown_button = Button(image=wrong_cross, command=next_card)
unknown_button.grid(column=1, row=1)

known_button = Button(image=correct_tick, command=is_known)
known_button.grid(column=2, row=1)

next_card()

win.mainloop()
