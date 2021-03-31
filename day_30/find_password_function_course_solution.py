
def find_password():
    website = website_entry.get()
    try:
        with open("login_details.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for "
                                                       f"{website} exists.")

# Only use Exception Handling when we don't have an easy alternative.
# Why use Exception Handling when if-elif-else statements can catch stuff
# easily.
