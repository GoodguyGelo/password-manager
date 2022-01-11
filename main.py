from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SEARCH FUNCTION ----------------------------------#
def find_password():
    search_key = website_entry_box.get().lower()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            email = data[search_key]['email']
            password = data[search_key]['password']
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found')
    except KeyError:
        messagebox.showerror(title='Error', message='No details for for the website found.')
    else:
        messagebox.showinfo(title=search_key, message=f'email: {email}\n'
                                                      f'password: {password}')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry_box.get().lower()
    email = email_entry_box.get()
    password = password_entry_box.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message="Don't leave any of the fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)  # read the data_file
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)  # writing the updated data in the data_file
        finally:
            website_entry_box.delete(0, END)
            password_entry_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# the logo canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(118, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels and entries
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry_box = Entry(width=33)
website_entry_box.grid(column=1, row=1, columnspan=1)
website_entry_box.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_entry_box = Entry(width=52)
email_entry_box.grid(column=1, row=2, columnspan=2)
email_entry_box.insert(END, 'angelo.a.naquila@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry_box = Entry(width=33)
password_entry_box.grid(column=1, row=3)

# Buttons

generate_pw_button = Button(text='Generate Password', command=generate_password)
generate_pw_button.grid(column=2, row=3, sticky='w')

add_button = Button(text='Add', width=44, command=save)
add_button.grid(columnspan=2, column=1, row=4)

search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
