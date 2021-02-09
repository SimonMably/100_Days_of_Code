from turtle import Turtle, Screen

# In OOP, classes are blueprints that can be used to construct objects.

# In OOP, we can create multiple objects from the same class or create
# multiple objects from multiple classes in the same program. For example:
timmy = Turtle()
tommy = Turtle()

# timmy and tommy are both objects constructed from the Turtle() class and
# can work independently from each other (we can create as many as we need).
# And because they are two separate objects the can work independently,
# each can be called an 'instance' (or each a separate 'instance'). This
# means that each are an example of a turtle object (from the Turtle() class).
# This also means that each can have their own attributes and can be doing
# different things at the same time. For example:
timmy.shape("turtle")
timmy.color("green")
timmy.forward(40)
tommy.shape("turtle")
tommy.color("purple")
tommy.backward(30)

# The fact that each of these objects can have their own attributes and can
# perform different methods at any one time, in programming, is known as
# having their 'state'. For example, the state of timmy's colour attribute is
# green, while the state of tommy's colour attribute is purple. In this case,
# they have a different state in terms of colour/appearance.
# They can also have different states in terms of doing something. For
# example, one object (or instance), like timmy, can be told to move forwards
# while another object, like tommy, can remain stationary.

screen = Screen()
screen.exitonclick()

