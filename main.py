from email import message
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from PIL import Image,ImageTk
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

low_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
up_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '&', '*']


def generate_password():
    low_text_length = 0
    up_text_length = 0

    # Getting inputs from GUI
    custom_string = custom_entry.get()
    try:
        password_length = int(length_entry.get()) + 1
        number_length = int(number_entry.get())
        character_length = int(character_entry.get())
    except:
        messagebox.showinfo(title="Error", message="Please enter a valid number")
        # This shows error because dumb people will put password length as "POG" and crash the program


    if character_length + number_length + len(custom_string) > password_length:
        messagebox.showinfo(title="Error", message="Password Length Insufficient")
        # This shows Error if Password Length is smaller than the Length of Sum of other Parameters
        if messagebox:
            return()


    if int(length_entry.get()) < 8 or int(length_entry.get()) > 32:
        messagebox.showinfo(title="Error", message="Password length not in range of 8-32 characters")
        return()

    if character_length < 1 or character_length > 6:
        messagebox.showinfo(title="Error", message="Special Character length not in range")
        if messagebox:
            return()

    global text_length
    text_length = password_length - number_length - len(custom_string) - character_length - 1


    try:
        text_state
    except:
        messagebox.showinfo(title="Error", message="Please select an option")
        # This shows error if none of the options are selected


    custom_list = custom_string.split(',') #This converts the custom name into a list

    if len(custom_list) > 1:
        messagebox.showinfo(title="Error", message="Please enter only one custom word")


    # Getting inputs from radio button
    if (text_state == 1):
        low_text_length = text_length
    elif (text_state == 2):
        up_text_length = text_length
    else:
        low_text_length = randint(1, text_length)
        up_text_length = text_length - low_text_length

    # Generating random strings as lists
    password_low_letters = [choice(low_letters) for _ in range(low_text_length)]
    password_up_letters = [choice(up_letters) for _ in range(up_text_length)]
    password_numbers = [choice(numbers) for _ in range(number_length)]
    password_characters = [choice(special_characters) for _ in range(character_length)]

    password_list = password_low_letters + password_up_letters + password_characters + password_numbers + custom_list
    shuffle(password_list)

    global password
    password = "".join(password_list)  # This converts the list to a string
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy():
    pyperclip.copy(password) # This copies the password to your clipboard to paste anywhere

def change_on_hover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))
    # This is to Change colour of Button on Hovering


def radio_used():
    global text_state
    text_state = radio_state.get()  # This gets 1,2,3


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cord = int((screen_width / 2) - (626 / 2))
y_cord = int((screen_height / 2) - (417 / 2))
window.geometry(f"550x500+{x_cord}+{y_cord}")

canvas = Canvas(height=200, width=200)
img = ImageTk.PhotoImage(Image.open("logo.jpg"))
canvas.create_image(117, 110, image=img)
canvas.grid(row=0, column=1)

# Labels
# If any Label has *, that field is compulsory
length_label = Label(text="Password Length (8-32)*:")
length_label.grid(row=1, column=0, sticky=W)
number_label = Label(text="Number of Numbers*:")
number_label.grid(row=2, column=0, sticky=W)
character_label = Label(text="Special Character length (0-6)*:")
character_label.grid(row=3, column=0, sticky=W)
letter_label = Label(text="Case*:")
letter_label.grid(row=4, column=0, sticky=W)
custom_label = Label(text="Custom String:")
custom_label.grid(row=5, column=0, sticky=W)


# Entries
length_entry = Entry()
length_entry.grid(row=1, column=1, columnspan=3)
length_entry.focus()
number_entry = Entry()
number_entry.grid(row=2, column=1, columnspan=3)
character_entry = Entry()
character_entry.grid(row=3, column=1, columnspan=3)
custom_entry = Entry()
custom_entry.grid(row=5, column=1, columnspan=3)
password_entry = Entry()
password_entry.grid(row=6, column=1, columnspan=3)

# Radio Button
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Lower", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Upper", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Mixed", value=3, variable=radio_state, command=radio_used)
radiobutton1.grid(row=4, column=0,columnspan=2)
radiobutton2.grid(row=4, column=1,columnspan=2)
radiobutton3.grid(row=4, column=2,columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=6, column=0, sticky=W)

generate_copy_button = Button(window, text="Copy", command=copy)
generate_copy_button.grid(row=7, column=1, columnspan=2)

change_on_hover(generate_copy_button, "Sky Blue", "White")
change_on_hover(generate_password_button, "Sky Blue", "White")

window.mainloop()