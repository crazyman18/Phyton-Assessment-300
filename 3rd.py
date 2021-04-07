from tkinter import *
from tkinter import ttk
from functools import partial

#Title of the program
root = Tk()
root.title("Weeb Comics Store")

# Create the PhotoImage and label to hold it
comic_image = PhotoImage(file="/Students/samuel.hermoso/Desktop/Phyton term 3/unnamed2.png")
comicimage_label = ttk.Label(root, image=comic_image)
comicimage_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Weeb Comics Store")
top_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("WEEB COMIC SELECTION")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength="300", justify="center")
message_label.grid(row=0, column=1, padx=10, pady=10)

# Create the Names of the Books
account_details = StringVar()
account_details.set("Super Dude: 8 \nLizard Man: 12\nWater Woman: 3")
details_label = ttk.Label(top_frame, textvariable=account_details, justify="center")
details_label.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

# Create a label for the account combobox
account_label = ttk.Label(top_frame, text="Account: ")
account_label.grid(row=1, column=1, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(top_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=2, column=1, padx=10, pady=3, sticky="WE")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

# Run the mainloop
root.mainloop()
