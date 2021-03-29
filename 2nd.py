from tkinter import *
from tkinter import ttk

#Title of the program
root = Tk()
root.title("Weeb Comics Store")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Weeb Comics Store")
top_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")
