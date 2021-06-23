from flask import Flask

# Rendering HTML and CSS with Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    # Rendering more than one HTML element
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif' width=200px>" \
           ""


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "==main__":
    app.run(debug=True)

















