import time


# A decorator function is a wrapper function that gives another function some functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()  # Runs function twice (function() refers to a function that has the '@decorator_name' above the
        function()  # function definition and is called. In this case, say_hello()
    return wrapper_function


@delay_decorator  # (otherwise known as Syntactic Sugar)
def say_hello():
    time.sleep(2)
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()

# Works the same way as using a Decorator without actually using a Decorators @ syntax
decorated_function = delay_decorator(say_greeting)
decorated_function()










