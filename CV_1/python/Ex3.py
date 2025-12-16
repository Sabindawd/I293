# .py
# Author: Balog Alexandru
# Date: 2.12.2025

import tkinter as tk
from tkinter import messagebox
 
def calcul_revenu_imposable():
    try:
        revenu_brut = float(entry_revenu.get())
        coeff_familial = float(entry_coeff.get())
 
        
        rabais = float(entry_rabais.get()) if var_rabais.get() else 0
        rabais_montant = revenu_brut * (rabais / 100)
 
        
        ded1 = int(entry_ded1.get()) if var_ded1.get() else 0
        ded2 = int(entry_ded2.get()) if var_ded2.get() else 0
 
        revenu_imposable = (revenu_brut / coeff_familial) - ded1 - ded2 - rabais_montant
 
        label_revenu.config(text=f"Revenu imposable: fr. {revenu_imposable:,.2f}".replace(",", "'"))
 
    except:
        messagebox.showerror("Erreur", "Veuillez remplir correctement tous les champs numériques.")
 
 
root = tk.Tk()
root.title("Déductions")
 
tk.Label(root, text="Revenu annuel brut").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_revenu = tk.Entry(root)
entry_revenu.grid(row=0, column=1, padx=5)
entry_revenu.insert(0, "145000")
 
tk.Label(root, text="Coefficient familial").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_coeff = tk.Entry(root)
entry_coeff.grid(row=1, column=1, padx=5)
entry_coeff.insert(0, "2.5")
 
frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2, pady=10)
    
var_ded1 = tk.BooleanVar()
check1 = tk.Checkbutton(frame, text="Déduction jeune", variable=var_ded1,
                        command=lambda: entry_ded1.config(state="normal" if var_ded1.get() else "disabled"))
check1.grid(row=0, column=0, sticky="w")
 
entry_ded1 = tk.Entry(frame, width=10)
entry_ded1.grid(row=0, column=1, padx=10)
entry_ded1.insert(0, "900")
entry_ded1.config(state="disabled")
 
var_ded2 = tk.BooleanVar(value=True)
check2 = tk.Checkbutton(frame, text="Déduction transport", variable=var_ded2,
                        command=lambda: entry_ded2.config(state="normal" if var_ded2.get() else "disabled"))
check2.grid(row=1, column=0, sticky="w")
 
entry_ded2 = tk.Entry(frame, width=10)
entry_ded2.grid(row=1, column=1, padx=10)
entry_ded2.insert(0, "650")
 
var_rabais = tk.BooleanVar(value=True)
check3 = tk.Checkbutton(frame, text="Rabais fidélité (%)", variable=var_rabais,
                        command=lambda: entry_rabais.config(state="normal" if var_rabais.get() else "disabled"))
check3.grid(row=2, column=0, sticky="w")
 
entry_rabais = tk.Entry(frame, width=10)
entry_rabais.grid(row=2, column=1, padx=10)
entry_rabais.insert(0, "4")
 
btn = tk.Button(root, text="Calcul", command=calcul_revenu_imposable)
btn.grid(row=3, column=0, columnspan=2, pady=10)
 
label_revenu = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_revenu.grid(row=4, column=0, columnspan=2, pady=20)
 
root.mainloop()