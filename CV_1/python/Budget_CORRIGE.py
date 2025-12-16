from tkinter import *


def calculate_budget():
    print("dans calcul budget")
    try:
        price = float(ent_price.get())
        money_available = float(ent_money_available.get())
        discount = float(ent_discount.get())
        discount_inter = price * discount / 100
        final_price = price - discount_inter
        money_remains = money_available - final_price
        if price < 0 or money_available < 0:
            raise ValueError("Les valeurs ne peuvent pas être négatives.")
        else:
            if money_available >= price:
                lbl_result.config(text=f"Vous avez suffisamment d'argent pour acheter l'article. \n Le prix final après réduction est de {final_price:.2f} CHF. \n Il vous restera {money_remains:.2f} CHF.")
            else:
                lbl_result.config(text=f"Vous n'avez pas suffisamment d'argent pour acheter l'article.")
    except:
        lbl_result.config(text="Veuillez entrer des valeurs numériques valides.")



# Close the main window
def close_window():
    root.quit()


# Fenêtre principale
root = Tk()
root.title("Calculateur de budget")
root.geometry("400x300")

# Entry fields
Label(root, text="CALCULATEUR DE BUDGET").pack(pady=20, padx=5)

# Prix
frm_price = Frame(root)
frm_price.pack(fill=X, padx=5, pady=5)
lbl_price = Label(frm_price, text="Prix de l'article (CHF) :")
lbl_price.pack(side=LEFT)
ent_price = Entry(frm_price)
ent_price.pack(side=RIGHT)
ent_price.focus()

# Argent disponible
frm_money_available = Frame(root)
frm_money_available.pack(fill=X, padx=5, pady=5)
lbl_money_available = Label(frm_money_available, text="Argent disponible (CHF) :")
lbl_money_available.pack(side=LEFT)
ent_money_available = Entry(frm_money_available)
ent_money_available.pack(side=RIGHT)

# Réduction
frm_discount =Frame(root)
frm_discount.pack(fill=X, padx=5, pady=5)
lbl_discount = Label(frm_discount, text="Réduction (%) :")
lbl_discount.pack(side=LEFT)
ent_discount = Entry(frm_discount)
ent_discount.pack(side=RIGHT)

# Bouton

frm_buttons = Frame(root, pady=10)
frm_buttons.pack()


btn_calculate = Button(frm_buttons, text="Calculer", command=calculate_budget)
btn_calculate.pack(side=LEFT, padx=5, pady=5)

Button(frm_buttons, text="Quitter", command=close_window).pack(padx=5, pady=5)


# Résultat
lbl_result = Label(root, text="", font=("Arial", 10))
lbl_result.pack()

root.mainloop()
 