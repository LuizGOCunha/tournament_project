from tkinter import *
from random import randint

from model.fighter import Fighter

# creates the master class through Tk
root = Tk()
root.geometry('800x600')

def dice_roll():
    dice_roll = randint(1,20)
    label.config(text=dice_roll)

def create_fighter():
    name = name_entry.get()
    weight = float(weight_entry.get())
    age = int(age_entry.get())
    sex = sex_entry.get()
    belt = int(belt_entry.get())
    fighter = Fighter(name, weight, belt, age, sex)
    fighter_label = Label(root, text=f"{fighter.__str__()}")
    fighter_label.pack()

def randomize_fighter():
    name = f"Fighter{randint(0,1000)}"
    weight = float(randint(40,100))
    belt = randint(0,4)
    age = randint(15,50)
    sex_options = ("M", "F")
    sex = sex_options[randint(0,1)]
    fighter = Fighter(name, weight, belt, age, sex)
    label.config(text=f"{fighter.__str__()}")

def remove_form():
    for items in form_items:
        items.destroy()

def create_form():
    # Forms
    global name_entry, weight_entry, age_entry, sex_entry, belt_entry   
    global name_label, weight_label, age_label, sex_label, belt_label   
    name_label = Label(root, text="Fighter Name:")
    name_entry = Entry(root)
    weight_label = Label(root, text="Weight:")
    weight_entry = Entry(root)
    age_label = Label(root, text="Age:")
    age_entry = Entry(root)
    sex_label = Label(root, text="Sex:")
    sex_entry = Entry(root)
    belt_label = Label(root, text="Belt")
    belt_entry = Entry(root)
    name_label.pack()
    name_entry.pack()
    weight_label.pack()
    weight_entry.pack()
    age_label.pack()
    age_entry.pack()
    sex_label.pack()
    sex_entry.pack()
    belt_label.pack()
    belt_entry.pack()
    # Creating buttons
    button = Button(root, text="Submit", command=create_fighter)
    button.pack()
    button2 = Button(root, text="Random", command=randomize_fighter)
    button2.pack()
    done_button = Button(root, text="Done", command=remove_form)
    done_button.pack()
    global form_items
    form_items = (
    name_entry, name_label, weight_entry, weight_label, age_entry, age_label, 
    sex_entry, sex_label, belt_entry, belt_label, button, button2, done_button
    )



create_form()

global label
label = Label(root, text="" )
label.pack()

root.mainloop()