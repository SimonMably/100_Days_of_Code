from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import json


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
    new_data = {
        website.title(): {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields",
                            message="One or more entry fields are empty. "
                                    "Fill them in before clicking the Add "
                                    "button.")
    else:
        try:
            with open("login_details.json", "r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("login_details.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("login_details.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------- SEARCH PASSWORD ------------------------------ #
def find_password():
    """IF user presses 'Search """
    website = website_entry.get().title()
    try:
        with open("login_details.json", "r") as f:
            data = json.load(f)
            if website not in data:
                raise KeyError
    except KeyError:
        messagebox.showerror(title="Error!",
                             message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        messagebox.showinfo(title="Password Found",
                            message=f"Website: {website}\n"
                                    f"Email: {data[website]['email']}\n"
                                    f"Password: {data[website]['password']}")
    finally:
        website_entry.delete(0, END)
        website_entry.focus()


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
website_entry = ttk.Entry()
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

# Search button
search_button = ttk.Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="ew")

# email/username label and entry
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = ttk.Entry()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

email_username_entry.insert(0, "email@mail.com")

# password label and entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = ttk.Entry()
password_entry.grid(column=1, row=3, sticky="ew")

# generate password button
generate_password_button = ttk.Button(text="Generate Password",
                                      command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew")

# add button
add_button = ttk.Button(text="Add", command=save_login_details)
add_button.grid(column=1, row=4, sticky="ew")

window.mainloop()
