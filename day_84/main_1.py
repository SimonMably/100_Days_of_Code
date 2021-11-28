import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning
from PIL import ImageTk, Image


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configure root window
        self.title("Watermark")
        self.geometry("1000x700")

        # Label
        # FIX THIS: Image not showing.
        image = Image.open("tree.jpg")
        test = ImageTk.PhotoImage(image=image)

        self.label = ttk.Label(borderwidth="10px", image=test)
        self.label.pack(expand=True)

        # Button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        """A pop up message box"""
        showinfo(title='Information', message='Hello, Tkinter!')

    def browse_images(self):
        """"""
        pass

    def view_image(self):
        """"""
        pass

    def add_watermark(self):
        """"""
        pass

    def save_watermarked_image(self):
        """"""
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
