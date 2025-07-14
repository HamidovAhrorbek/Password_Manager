from tkinter import *

# ---------- PASSWORD GENERATOR ----------#

# ---------- SAVE PASSWORD ----------#

# ---------- UI SETUP ----------#

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=100)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100,112, image=password_img)




window.mainloop()
