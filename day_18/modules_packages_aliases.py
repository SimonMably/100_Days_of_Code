# import turtle  # Standard/simple importing of a module
#
# # When doing a standard/simple import of a module, we can call upon all
# # of that modules variable, functions/methods and classes in a specific way:
# tim = turtle.Turtle()

###############################################################################
# from turtle import Turtle, Screen  # Importing specific things from a module.
#
# # We can also import specific variable, functions/methods and classes from a
# # module. It would make calling upon them more convenient as we won't have to
# # type the name of the module and a '.' before whatever we imported. For
# # example:
# tim = Turtle()
# # NOT tim = turtle.Turtle()
#
# # Also, we can import multiple things from the same module in the same import
# # statement.

###############################################################################
# from turtle import *  # Imports everything from module.
#
# # This method of importing modules has it pros and cons.
# # A pro is that we can we can use just the name of the variable,
# # function/method or class (like above)
#
# # tim = Turtle()
# forward(100)
#
# # One example of a con is that, if we use a modules function (like turtles
# # forward() (as seen above)), it may be confusing to us or other programmers
# # who look at our code, especially if we import and utilise other modules the
# # same way, as we may end up not know what came from were.

###############################################################################

# It would be best to avoid the last method as it wil be more confusing than
# it's worth.
# We should instead the second use method if we're using the same things from
# a module more than 3 times in the same file for example. And if we're using
# these same things from a module only once or twice in the same file, then we
# can use the first method of importing.
# We should use either the first or second methods of importing as to cause
# less confusion for ourselves and for other people who read our code.

###############################################################################

# # Aliasing Modules
# # Module name can be long and rather tedious to type out everytime we need to
# # call upon a module. When we type out the import statement, we can give a
# # module an alias (another name) that is much smaller than its actual name.
# # This alias name will represent the entire module and will be regarded by
# # the program as the same name as the actual module name.
# # For example:
# import turtle as t
#
# tim = t.Turtle()

###############################################################################

# Installing Modules

# Some modules, like turtle, random and tkinter, are built-in and packaged with
# Python (Known as the Python standard library) and can be imported and used
# straight out of the box.
# All other Python modules that exist are third-party modules that have to be
# downloaded and installed first. This can be done via an IDE (like Pycharm)
# or via a Terminal program (like the Command Prompt on a Windows OS)


screen = Screen()
screen.exitonclick()
