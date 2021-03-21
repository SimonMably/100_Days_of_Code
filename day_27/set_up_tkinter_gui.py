import tkinter

window = tkinter.Tk()
# Text in string appears at top of GUI window.
window.title("My First Gui Program")
# Sets minimum size for GUI window. Size of window can be adjusted manually
# (resize bigger/smaller), but cannot be made smaller than set minimum size.
window.minsize(width=500, height=300)

# Create components and place onto window:
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# pack() method places (or packs) items at the top center of GUI window. Item
# will not show on the GUI window until it is placed ont the window with pack()
# or other placing method.
my_label.pack(expand=True)  # Packs item at center of window
# Can also use other arguments (other than 'expand'). eg. (side="bottom"
# Documentation for the pack() method:
# https://docs.python.org/3/library/tkinter.html#the-packer







# Keeps the tkinter GUI window open. Needs to be at the end of the file.
window.mainloop()
