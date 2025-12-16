# Pizza.py
# Author: Balog Alexandru
# Date: 09.12.2025

from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("Pizza")
window.geometry("350x300")


# Table
frm_table = Frame(window)
frm_table.pack(fill=X, padx=5, pady=5)
lbl_table = Label(frm_table, text="Table")
lbl_table.pack(side=LEFT,padx=5)
ent_table = Entry(frm_table,width=5)
ent_table.pack(side=LEFT)


# Pizza Size
frm_size = LabelFrame(window, text="Pâte")
frm_size.pack(side=LEFT,padx=(20,0), pady=(0,70))


# Pizza Size Radio Buttons
normaux = StringVar(value=NONE)
chk_extra_fine = Radiobutton(frm_size, text="Extra fine", variable=normaux, value="Extra fine")
chk_extra_fine.pack(anchor=W,padx=5)
chk_fine = Radiobutton(frm_size, text="Fine", variable=normaux, value="Fine")
chk_fine.pack(anchor=W,padx=5)
chk_normal = Radiobutton(frm_size, text="Normal", variable=normaux, value="Normal")
chk_normal.pack(anchor=W,padx=5)
chk_epaisse = Radiobutton(frm_size, text="Epaisse", variable=normaux, value="Epaisse")
chk_epaisse.pack(anchor=W,padx=5)


# Pizza Toppings
frm_toppings = Frame(window)
frm_toppings.pack(side=RIGHT,padx=(0,20), pady=(0,70))


# Pizza Toppings Checkbuttons
Anchois = BooleanVar()
chk_Anchois = Checkbutton(frm_toppings, text="Anchois", variable=Anchois)
chk_Anchois.pack(anchor=W,padx=5)
Capres = BooleanVar()
chk_Capres = Checkbutton(frm_toppings, text="Câpres", variable=Capres)
chk_Capres.pack(anchor=W,padx=5)
Jambon = BooleanVar()
chk_Jambon = Checkbutton(frm_toppings, text="Jambon", variable=Jambon)
chk_Jambon.pack(anchor=W,padx=5)
Crevettes = BooleanVar()
chk_Crevettes = Checkbutton(frm_toppings, text="Crevettes", variable=Crevettes)
chk_Crevettes.pack(anchor=W,padx=5)


# Commande Button
def order_pizza():
    table_number = ent_table.get()
    size = ""
    if normaux.get() == "Extra fine":
        size = "Extra fine"
    elif normaux.get() == "Fine":
        size = "Fine"
    elif normaux.get() == "Normal":
        size = "Normal"
    elif normaux.get() == "Epaisse":
        size = "Epaisse"
    toppings = []
    if Anchois.get():
        toppings.append("Anchois")
    if Capres.get():
        toppings.append("Câpres")
    if Jambon.get():
        toppings.append("Jambon")
    if Crevettes.get():
        toppings.append("Crevettes")
    toppings_str = ", ".join(toppings) if toppings else "Aucun"
    order_summary = f"Table: {table_number}\nPâte: {size}\nGarnitures: {toppings_str}"
    showinfo("Résumé de la commande", order_summary)


frm_commande = Frame(window)
frm_commande.pack(fill=X,side=BOTTOM)
btn_commande = Button(frm_commande, text="Commander", command=order_pizza)
btn_commande.pack(pady=10,side=RIGHT)


window.mainloop()