from flask import Flask

app = Flask(__name__)


# If user accesses homepage, because of the forward slash in Decorator
@app.route("/")
def hello_world():
    return "Hello, World!"


# if user accesses the 'bye' page, because of the '/bye' in the Decorator
@app.route("/bye")
def say_bye():
    return "Bye, World"


if __name__ == "__main__":
    app.run()
