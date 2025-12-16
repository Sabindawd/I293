
from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("Sélection de sujets")
window.geometry("400x380")

# Variables
tech_var = StringVar(value='Aucun sujet sélectionné')
science_var = StringVar(value='Aucun sujet sélectionné')
art_var = StringVar(value='Aucun sujet sélectionné')
sport_var = StringVar(value='Aucun sujet sélectionné')

def on_button_toggle():
    msg = (
        "Sélection actuelle :\n"
        f"Technologie : {tech_var.get()}\n"
        f"Science : {science_var.get()}\n"
        f"Art : {art_var.get()}\n"
        f"Sport : {sport_var.get()}"
    )
    showinfo("Sélection actuelle", msg)

# Checkbuttons
Checkbutton(window, text='Technologie',
            variable=tech_var,
            onvalue='sélectionné',
            offvalue='Aucun sujet sélectionné').pack(padx=30)

Checkbutton(window, text='Science',
            variable=science_var,
            onvalue='sélectionné',
            offvalue='Aucun sujet sélectionné').pack(padx=30)

Checkbutton(window, text='Art',
            variable=art_var,
            onvalue='sélectionné',
            offvalue='Aucun sujet sélectionné').pack(padx=30)

Checkbutton(window, text='Sport',
            variable=sport_var,
            onvalue='sélectionné',
            offvalue='Aucun sujet sélectionné').pack(padx=30)

Button(window, text="Afficher sélection",
       command=on_button_toggle,
       width=30).pack(pady=10)


window.mainloop()
