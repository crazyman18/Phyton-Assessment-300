######################### Creating A Starting Loop ###############################

# Importing
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter
from tkinter import messagebox
import tkinter.font as font

# Title of the program
root = Tk()
root.geometry("400x700")
root.title("Weeb Comics Store")
root.configure(bg='black')

############################# Class Coding #################################
# Initialize list
comicsbalance_list = []
account_names = []

message_text_list = ""
message_text_total = 0

Comic_details = StringVar()

# Create the Account class
class Comics:
  """WEEB Comics Store"""
  def __init__(self, name, stock, sold):
    self.name = name
    self.stock = int(stock)
    self.sold = int(sold)
    comicsbalance_list.append(self)
    account_names.append(self.name)

    global message_text_list
    message_text_list += (self.name + "-" + str(self.stock) + "\n")
    global message_text_total
    message_text_total += self.sold

# Create a function to read data from the file
def get_data():
  comics_balance = open("comicsbalance.txt","r")
  line_list = comics_balance.readlines()
  for line in line_list:
    comicsbalance_data = line.strip().split(",")
    Comics(*comicsbalance_data)
  comics_balance.close()
  Comic_details.set(message_text_list + "----------\nTotal Comics Sold:{}".format(message_text_total))

def update_thestock():
  comics_balance = open("comicsbalance.txt","w")
  for comic in comicsbalance_list:
    comics_balance.write("{},{},{}\n".format(comic.name,comic.stock,comic.sold))
  comics_balance.close()

get_data()
############################## Making A Define Function #######################

# Create a variable to store the comic balance
def sell_comic():
  global message_text_total, message_text_list
  for comic in comicsbalance_list:
    if account_box.get() == comic.name:
      comicvar = comic
      break
  if 1 <= comicvar.stock:
    comicvar.stock -=1
    message_text_total += 1
    message_text.set("{} Comic\n has been sold\n Succesfully".format(comic.name))
    message_text_list = ""
    for comic in comicsbalance_list:
      message_text_list += (comic.name + " - " + str(comic.stock) + "\n")
    Comic_details.set(message_text_list + "----------\nTotal Comics Sold:{}".format(message_text_total))
    update_thestock()
    return True
  else:
    popupmsg("Out of stock!")
    return False
  
  
# Create a function that will update the balance.
def restock_comic():
  comic = chosen_comics.get()
  for comic in comicsbalance_list:
    if chosen_comics.get() == comic.name:
      comic.stock += int(amount.get())
      message_text.set("{} * {} Comic\n has been restocked\n Succesfully".format(int(amount.get()), comic.name))
  message_text_list = ""
  for comic in comicsbalance_list:
      message_text_list += (comic.name + " - " + str(comic.stock) + "\n")
  Comic_details.set(message_text_list + "----------\nTotal Comics Sold:{}".format(message_text_total))
  update_thestock()
  amount_entry.delete(0, END)
  restock_button.config(state='disabled')

# Entry Error
def existing_number_validate(char):
    if char.isdigit():
        return True
    else:
        return False

# Popup message
def popupmsg(msg):
  messagebox.showerror('Out Of Stock!', msg)

def button_on(event):
  if amount_entry.get() == "":
    restock_button.config(state='disabled')
  else:
    for char in amount_entry.get():
      if char.isdigit():
        restock_button.config(state='normal')
        break
      else:
        restock_button.config(state='disabled')
        break
      
######################## IMAGE ############################

# Create the PhotoImage and label to hold it
comic_image = PhotoImage(file="/Students/samuel.hermoso/Desktop/Phyton term 3/unnamed2.png")
comicimage_label = ttk.Label(root, image=comic_image)
comicimage_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

####################### FRAMES ##############################

# Create the top frame
top_frame = LabelFrame(root, text="STOCK LEVELS")
top_frame.config(font=("Arial", 8, 'normal', 'italic'))
top_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create the middle frame
middle_frame = LabelFrame(root, text="SELLING SECTION")
middle_frame.config(font=("Arial", 8, 'normal', 'italic'))
middle_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

# Create the bottom frame
bottom_frame = LabelFrame(root, text="RESTOCK SECTION")
bottom_frame.config(font=("Arial", 8, 'normal', 'italic'))
bottom_frame.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW")

####################### LABELS #############################

# Create the Names of the Books
details_label = ttk.Label(top_frame, textvariable=Comic_details, justify=CENTER, font=("Times New Roman", 12, 'normal', 'roman'))
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and set the message text variable
message_text = StringVar()
message_text.set("")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, justify=CENTER, font=("Times New Roman", 12, 'normal', 'roman'))
message_label.grid(row=2, column=2, padx=10, pady=10)

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:", justify=CENTER, font=("Times New Roman", 12, 'normal', 'roman'))
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Copyright Display
copy_right = Label(root, text="© Samuel Hermoso", fg="#0046d5")
copy_right.config(font = ("Candara", 10), justify=LEFT)
copy_right.grid(row=4, column=0)


######################## COMBOBOX #########################

# Set up a variable and option list for the account Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(middle_frame, textvariable=chosen_account, state="readonly", justify=CENTER, font=("Verdana", 10, 'bold', 'roman'))
account_box['values'] = account_names
account_box.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

# Set up a variable and option list for the account Combobox
comics_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_comics = StringVar()
chosen_comics.set(account_names[0])

# Create a Combobox to select the account
restock_box = ttk.Combobox(bottom_frame, textvariable=chosen_comics, state="readonly", justify=CENTER, font=("Verdana", 10, 'bold', 'roman'))
restock_box['values'] = account_names
restock_box.grid(row=2, column=1, padx=10, sticky="WE")

############################ BUTTONS #########################

ButtonFont = font.Font=("Impact", 12, 'normal', 'roman')

# Create a sell button
buy_button = Button(middle_frame, text="Buy", command=sell_comic)
buy_button['font'] = ButtonFont
buy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create a restock button
restock_button = Button(bottom_frame, text="ReStock", command=restock_comic, state='disabled')
restock_button['font'] = ButtonFont
restock_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

########################## ENTRY #############################

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry_command = bottom_frame.register(existing_number_validate)
amount_entry = ttk.Entry(bottom_frame, textvariable=amount, justify=CENTER, validate='all', validatecommand=(amount_entry_command, '%S'))
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")
amount_entry.bind("<KeyRelease>", button_on)
#amount_entry.bind("<BackSpace>", button_on)


############################ Run the Mainloop ########################
root.mainloop()
