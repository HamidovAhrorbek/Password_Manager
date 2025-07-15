from tkinter import *
from tkinter import messagebox
import random
import string

# ---------- PASSWORD GENERATOR ----------#
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!#$%&()*+"

    password_chars = (
        random.choices(letters, k=8) +
        random.choices(digits, k=2) +
        random.choices(symbols, k=2)
    )
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------- SAVE PASSWORD ----------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                          f"Email: {email}\nPassword: {password}\nSave?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------- UI SETUP ----------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
try:
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except:
    pass  # Prevent crash if logo image is missing
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "xxxx@mail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
