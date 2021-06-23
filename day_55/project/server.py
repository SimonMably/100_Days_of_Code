from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

colours = ["#d40bb5", "#cf2929", "#272dc4", "#1e9c22", "#22a9ab", ]


def style_h1_with_colour(function):
    def wrapper(*args, **kwargs):
        generated_colour = colours[random.randint(1, 5)]
        return f"<h1 style='color:{generated_colour}'>{function(**kwargs)}</h1>"
    return wrapper


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1><br>" \
           "<img src='https://media.giphy.com/media/ZNegC7wFpuQT7nurZ0/giphy.gif'>"


@app.route("/<int:number>")
@style_h1_with_colour
def guess_number(number):
    if random_number > number:
        return "Too low, try again!<br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number == random_number:
        return "Correct<br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif random_number < number and number < 10:
        return "Too high, try again!<br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number < 0 or number > 9:
        return "Make a guess between 0 and 9 only!<br>" \
               "<img src='https://media.giphy.com/media/fItgT774J3nWw/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
