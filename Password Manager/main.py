from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# you can use this function to generate a password if you wish but I have used the 2nd one.
# def generate_password():
#     letters = string.ascii_letters
#     digits = string.digits
#     special_chars = string.punctuation
#     all_chars = letters + digits + special_chars
#     password_length = 12  # You can adjust the password length as needed
#     password = ''.join(random.choice(all_chars) for _ in range(password_length))
#     password_entry.delete(0, END)
#     password_entry.insert(0, password)

def generate_password():
    password_entry.delete(0, END)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = emil_entry.get()
    password = password_entry.get()

    if website and email and password:
        confirm=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if confirm:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                clear_ui()
                pyperclip.copy(password)
                messagebox.showinfo(title="Password saved", message="Password saved successfully")
        else:
            clear_ui()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

def clear_ui():
    website_entry.delete(0, END)
    emil_entry.delete(0, END)
    emil_entry.insert(0, "aryan@gmail.com") # You can change the default email here
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# Labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

emil_entry=Entry(width=35)
emil_entry.grid(row=2,column=1,columnspan=2)
emil_entry.insert(0,"aryan@gmail.com") # You can change the default email here

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,columnspan=1)

# Buttons
generate_password_button=Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2,padx=5)
add_button=Button(text="Add",width=36, command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()