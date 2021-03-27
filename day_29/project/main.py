from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip


# -------------------------- PASSWORD GENERATOR ------------------------------ #
def generate_password():
    """"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    '''# Course Solution:
    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers
    '''

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # Copies password into clipboard
    pyperclip.copy(password)


# ----------------------------- SAVE PASSWORD -------------------------------- #
def save_login_details():
    """Retrieves text from entry fields, formats text into a string and
    appends to a text file: 'login_details.txt'. Also deletes text from
    website_entry and password_entry and gives user confirmation of saved
    details."""
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=f"Login details for {website}",
                                   message="These are the entered details: \n"
                                           f"Email: {email_username}\n"
                                           f"Password: {password}\n"
                                           "Is this ok?")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields",
                            message="One or more entry fields are empty. "
                                    "Fill them in before clicking the Add "
                                    "button.")
    else:
        if is_ok:
            with open("login_details.txt", "a") as f:
                f.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------------- UI SETUP ---------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_img = PhotoImage(file="logo.png")
window.iconphoto(False, logo_img)

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# website entry
website_entry = ttk.Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# email/username label and entry
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = ttk.Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "email@mail.com")

# password label and entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = ttk.Entry(width=22)
password_entry.grid(column=1, row=3)

# generate password button
generate_password_button = ttk.Button(text="Generate Password",
                                      command=generate_password)
generate_password_button.grid(column=2, row=3)

# add button
add_button = ttk.Button(text="Add", width=40, command=save_login_details)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
