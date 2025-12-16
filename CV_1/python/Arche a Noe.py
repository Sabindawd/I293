import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Arche de Noé")
root.geometry("360x300")


#LEFT BOX 
left_box = tk.Frame(root)
left_box.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(left_box, text="Encore à terre").pack()
animal_listbox = tk.Listbox(left_box, width=15, height=20)
animal_listbox.pack()


animals = [
    "Araignée", "Chat", "Cheval", "Chien", "Cobra",
    "Coccinelle", "Kangourou", "Perroquet", "Rat", "Ver de terre"
]

for animal in animals:
    animal_listbox.insert(tk.END, animal)


#SORT LISTBOX
def sort_left_listbox():
    items = list(animal_listbox.get(0, tk.END))
    items.sort()
    animal_listbox.delete(0, tk.END)
    for item in items:
        animal_listbox.insert(tk.END, item)

sort_left_listbox()


#MIDDLE BOX
middle_box = tk.Frame(root)
middle_box.pack(side=tk.LEFT, padx=20, pady=20)


# RIGHT BOX 
right_box = tk.Frame(root)
right_box.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(right_box, text="A bord").pack()
arche_listbox = tk.Listbox(right_box, width=15, height=20)
arche_listbox.pack()


#BUTTON ADD
button_frm = tk.Frame(root)
button_frm.pack(side=tk.RIGHT, padx=20, pady=20)

def add_animal():
    selected = animal_listbox.curselection()
    if selected:
        index = selected[0]
        animal = animal_listbox.get(index)
        arche_listbox.insert(tk.END, animal)
        animal_listbox.delete(index)
    else:
        messagebox.showwarning(
            "Aucun animal sélectionné",
            "Veuillez sélectionner un animal à ajouter."
        )

add_button = tk.Button(middle_box, text="==>", command=add_animal)
add_button.pack()


#BUTTON REMOVE
def remove_animal():
    selected = arche_listbox.curselection()
    if selected:
        index = selected[0]
        animal = arche_listbox.get(index)
        animal_listbox.insert(tk.END, animal)
        sort_left_listbox()  # Sort left list after adding back
        arche_listbox.delete(index)
    else:
        messagebox.showwarning(
            "Aucun animal sélectionné",
            "Veuillez sélectionner un animal à retirer."
        )

remove_button = tk.Button(middle_box, text="<==", command=remove_animal)
remove_button.pack()


root.mainloop()
