from tkinter import *
from tkinter import ttk
from functools import partial

# Create a variable to store the comic balance
Super_Dude = 8
Lizard_Man = 12
Water_Woman = 3

# Create a function that will update the balance.
def update_balance():
  global Super_Dude, Lizard_Man, Water_Woman
  comics = chosen_comics.get()

  if comics == "Super Dude":
      Super_Dude += amount.get()
    else:
        Super_Dude -= amount.get()

    elif account == "Lizard Man":
      Lizard_Man += amount.get()
    else:
      Lizard_Man -= amount.get()
      
    elif account == "Water Woman":
      Water_Woman += amount.get()
    else:
      Water_Woman -= amount.get()
  
  total_balance = Super_Dude + Lizard_Man + Water_Woman
  balance_string = "Super Dude: {}\nLizard Man: {}\nWater Woman: {}\nTotal Comic Sold: {}".format(Super_Dude, Lizard_Man, Water_Woman, total_balance)
  Comic_details.set(balance_string)
  amount.set("")

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
Comic_details = StringVar()
Comic_details.set("Super Dude: 8 \nLizard Man: 12\nWater Woman: 3\nTotal Comic Sold: 0")
details_label = ttk.Label(top_frame, textvariable=Comic_details, justify="center")
details_label.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

# Create a label for the account combobox
account_label = ttk.Label(top_frame, text="Stock Levels")
account_label.grid(row=1, column=2, padx=10, pady=3)

# Set up a variable and option list for the account Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(top_frame, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=2, column=1, padx=10, sticky="WE")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

#Title of the second frame
Restock_text = StringVar()
Restock_text.set("RESTOCK SECTION")
Restock_label = ttk.Label(bottom_frame, textvariable=Restock_text, wraplength="300", justify="center")
Restock_label.grid(row=0, column=1, padx=10, pady=10)

# Set up a variable and option list for the account Combobox
comics_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_comics = StringVar()
chosen_comics.set(account_names[0])

# Create a Combobox to select the account
restock_box = ttk.Combobox(bottom_frame, textvariable=chosen_comics, state="readonly")
restock_box['values'] = account_names
restock_box.grid(row=2, column=1, padx=10, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=update_balance)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the mainloop
root.mainloop()
