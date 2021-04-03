from tkinter import *
from tkinter import ttk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# DATA ----------------------------------------------------------------------- #
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
random_word = random.choice(to_learn)
print(random_word)


# FUNCTIONS ------------------------------------------------------------------ #
def next_card():
    """Generate random French word with English translation. French word is
    shown first."""
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    new_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=new_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = win.after(3000, func=flip_card)


def flip_card():
    """"""
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# UI SETUP ------------------------------------------------------------------- #
win = Tk()
win.title("Flash Card App")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = win.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
correct_tick = PhotoImage(file="images/right.png")
wrong_cross = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French",
                                font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=random_word["French"],
                               font=("Ariel", 60, "bold"))

# Buttons
unknown_button = ttk.Button(image=wrong_cross, command=next_card)
unknown_button.grid(column=1, row=1)

known_button = ttk.Button(image=correct_tick, command=flip_card)
known_button.grid(column=2, row=1)

win.mainloop()