from tkinter import *


def calculate():
    """Calculate the conversion of miles to kilometers. Takes input from Entry 
    widget for miles."""
    kilometer_text = 1.609 * float(miles_input.get())
    lbl_converted_km.config(text=str(round(kilometer_text, 2)))


win = Tk()
win.title("Miles to Kilometers Converter")
win.minsize(width=100, height=100)
win.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=15)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

# Labels
lbl_miles = Label(text="Miles", font=("Arial", 15), padx=10, pady=10)
lbl_miles.grid(column=2, row=0)

lbl_equal = Label(text="is equal to", font=("Arial", 15), padx=10, pady=10)
lbl_equal.grid(column=0, row=1)

lbl_converted_km = Label(text="0", font=("Arial", 15), padx=10, pady=10)
lbl_converted_km.grid(column=1, row=1)

lbl_kilometers = Label(text="Km", font=("Arial", 15), padx=10, pady=10)
lbl_kilometers.grid(column=2, row=1)

# Buttons
btn_calculate = Button(text="Calculate", font=("Arial", 15), command=calculate, 
                       padx=5, pady=5)
btn_calculate.grid(column=1, row=3)




win.mainloop()
