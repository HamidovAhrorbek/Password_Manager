from tkinter import *

# ---------- PASSWORD GENERATOR ----------#

# ---------- SAVE PASSWORD ----------#

# ---------- UI SETUP ----------#

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=password_img)
canvas.pack()

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, columnspan=20)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, columnspan=20)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, columnspan=15)

generate_password = Button(text="Generate Password", highlightthickness=0)
generate_password.grid(column=2,row=4)

add = Button(text="Add", highlightthickness=0)
add.grid(column=1,row=4)


window.mainloop()
