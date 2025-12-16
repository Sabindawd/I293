# I319-bonjour.py
# Author: Balog Alexandru
# Date: 4.11.2025

from tkinter import *

def say_subject() :
    print("Bonjour,", ent_subject.get())
    lbl_subject1.config(text=f"Bonjour, {ent_subject.get()}")

window = Tk()
window.title("Bonjour qui? : ")
window.geometry("200x200")

lbl_subject = Label(window, text="Votre prénom : ")
lbl_subject.pack(anchor=W, padx=5, pady=5)

ent_subject = Entry(window)
ent_subject.pack(anchor=W, padx=5, pady=5)

btn_validate = Button(window, text="Dire bonjour : ", command = say_subject)
btn_validate.pack(anchor=W, padx=10, pady=10)

lbl_subject1 = Label(window)
lbl_subject1.pack(anchor=W, padx=15, pady=15)

window.mainloop()



