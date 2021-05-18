######################### Creating A Starting Loop ###############################

# Importing
from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter
from tkinter import messagebox

# Title of the program
root = Tk()
root.title("Weeb Comics Store")
root.configure(bg='black')

############################## Making A Define Function #######################

# Create a variable to store the comic balance
Super_Dude = 8
Lizard_Man = 12
Water_Woman = 3

# Create a function that will update the balance.
def update_balance():
  global Super_Dude, Lizard_Man, Water_Woman
  comics = chosen_comics.get()

  if comics == "Super Dude":
      Super_Dude += int(amount.get())
      message_text.set("")
  elif comics == "Lizard Man":
      Lizard_Man += int(amount.get())
      message_text.set("")
  elif comics == "Water Woman":
      Water_Woman += int(amount.get())
      message_text.set("")
  else:
      pass
  
  total_balance = Super_Dude + Lizard_Man + Water_Woman
  balance_string = "Super Dude: {}\nLizard Man: {}\nWater Woman: {}\nTotal In Stock: {}".format(Super_Dude, Lizard_Man, Water_Woman, total_balance)
  Comic_details.set(balance_string)
  amount.set("")

def buy_comic():
  global Super_Dude, Lizard_Man, Water_Woman
  comics = account_box.get()

  if comics == "Super Dude":
      if Super_Dude > 0:
        Super_Dude -= 1
        message_text.set("Super Dude\n has been\n Succesfully sold.")
      else:
        popupmsg("Super Dude is\n Out of stock!")
  elif comics == "Lizard Man":
      if Lizard_Man > 0:
        Lizard_Man -= 1
        message_text.set("Lizard Man\n has been\n Succesfully sold.")
      else:
        popupmsg("Lizard Man is\n Out of stock!")
  elif comics == "Water Woman":
      if Water_Woman > 0:
        Water_Woman -= 1
        message_text.set("Water Woman\n has been\n Succesfully sold.")
      else:
        popupmsg("Water Woman is\n Out of stock!")
  else:
      pass
  total_balance = Super_Dude + Lizard_Man + Water_Woman
  balance_string = "Super Dude: {}\nLizard Man: {}\nWater Woman: {}\nTotal In Stock: {}".format(Super_Dude, Lizard_Man, Water_Woman, total_balance)
  Comic_details.set(balance_string)

def existing_number_validate(char):
    if char.isdigit():
        return True
    else:
        return False

def popupmsg(msg):
  messagebox.showerror('Out Of Stock!', msg)

######################## IMAGE ############################

# Create the PhotoImage and label to hold it
comic_image = PhotoImage(file="/Students/samuel.hermoso/Desktop/Phyton term 3/unnamed2.png")
comicimage_label = ttk.Label(root, image=comic_image)
comicimage_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

####################### FRAMES ##############################

# Create the top frame
top_frame = ttk.LabelFrame(root, text="STOCK LEVELS")
top_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create the middle frame
middle_frame = ttk.LabelFrame(root, text="SELLING SECTION")
middle_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root, text="RESTOCK SECTION")
bottom_frame.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW")

####################### LABELS #############################

# Create the Names of the Books
Comic_details = StringVar()
Comic_details.set("Super Dude: 8 \nLizard Man: 12\nWater Woman: 3\nTotal In Stock: 23")
details_label = ttk.Label(top_frame, textvariable=Comic_details, justify=CENTER)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and set the message text variable
message_text = StringVar()
message_text.set("")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, justify=CENTER)
message_label.grid(row=2, column=2, padx=10, pady=10)

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:", justify=CENTER)
amount_label.grid(row=5, column=0, padx=10, pady=3)

######################## COMBOBOX #########################

# Set up a variable and option list for the account Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(middle_frame, textvariable=chosen_account, state="readonly", justify=CENTER)
account_box['values'] = account_names
account_box.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

# Set up a variable and option list for the account Combobox
comics_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_comics = StringVar()
chosen_comics.set(account_names[0])

# Create a Combobox to select the account
restock_box = ttk.Combobox(bottom_frame, textvariable=chosen_comics, state="readonly", justify=CENTER)
restock_box['values'] = account_names
restock_box.grid(row=2, column=1, padx=10, sticky="WE")

############################ BUTTONS #########################

# Create a sell button
buy_button = ttk.Button(middle_frame, text="Buy", command=buy_comic)
buy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create a restock button
restock_button = ttk.Button(bottom_frame, text="ReStock", command=update_balance)
restock_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

########################## ENTRY #############################

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry_command = bottom_frame.register(existing_number_validate)
amount_entry = ttk.Entry(bottom_frame, textvariable=amount, justify=CENTER, validate='all', validatecommand=(amount_entry_command, '%S'))
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

############################ Run the Mainloop ########################
root.mainloop()
