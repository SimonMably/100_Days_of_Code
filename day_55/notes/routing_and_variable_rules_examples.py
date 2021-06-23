from flask import Flask

app = Flask(__name__)

# These @app.route() Decorators bind their accompanying functions to the URL
# Routing: This Decorator and function refers to a websites homepage
@app.route("/")
def hello_world():
    return 'Hello, World!'


#  Routing: This Decorator and function refers to a websites 'bye' webpage (eg. WebsiteName.com/bye)
@app.route("bye")
def bye():
    return "Bye!"


# Variable Rules: <name> in Decorator refers to a variable called 'name' which will be used as an argument in 'greet()'
# function. Example: WebsiteName.com/simon. In this case, 'simon' is used as a variable (any name can be used).

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
