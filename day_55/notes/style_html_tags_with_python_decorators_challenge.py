from flask import Flask

# Rendering HTML and CSS with Flask

app = Flask(__name__)


# make_bold() decorator function
def make_bold(function):
    def bold_wrapper():
        return "<b>" + function() + "</b>"
    return bold_wrapper


# make_emphasis() decorator function (emphasis = italic)
def make_emphasis(function):
    def bold_emphasis():
        return "<em>" + function() + "</em>"
    return bold_emphasis


# make_underlined() decorator function
def make_underlined(function):
    def underlined_wrapper():
        return "<u>" + function() + "</u>"
    return underlined_wrapper


@app.route("/")
def hello_world():
    # Rendering more than one HTML element
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif' width=200px>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "==main__":
    app.run(debug=True)
