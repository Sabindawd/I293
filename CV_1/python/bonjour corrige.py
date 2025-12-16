# Author : Frédérique Andolfatto
# Hello program
# 04.11.2025

from tkinter import *

def say_hello() :
    global lbl_say_hello, ent_firstname
    # two ways to write the message in the label
    # lbl_say_hello.config(text="Bonjour, " + ent_firstname.get()) or
    lbl_say_hello.config(text=f"Bonjour, {ent_firstname.get()}")

window = Tk()
window.title("Bonjour qui?")
window.geometry("400x200")
lbl_firstname = Label(window, text="Votre prénom :")
lbl_firstname.pack(anchor=W, pady=10, padx=5)

ent_firstname = Entry()
ent_firstname.pack(anchor=W, fill=X, pady=10, padx=5)

btn_say_hello = Button(window, text="Dire bonjour", command=say_hello)
btn_say_hello.pack(anchor=W, pady=10, padx=5)

lbl_say_hello = Label(window)
lbl_say_hello.pack(anchor=W, pady=10, padx=5)

window.mainloop()