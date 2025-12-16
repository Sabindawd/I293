from tkinter import *
from tkinter.messagebox import *
 
def temp_income():
    try:
        income = float(ent_income.get())
        coeff = float(ent_coeff.get())
 
        result = income / coeff
 
        return result
 
    except ValueError:
        showerror("Erreur", "Veuillez entrer uniquement des nombres.")
    except:
        showerror("Erreur", "Réessayer avec un autre nombre")
 
def deduction():
    if ent_ded_young.get() == "0" or ent_ded_discount.get() == "0" or ent_ded_trans.get() == "0" or ent_income.get() == "0" or ent_coeff.get() == "0":
            showerror("ERREUR", f"Les valeurs ne peuvent pas être 0")
            return
    if ent_ded_young.get() and ent_ded_discount.get() and ent_ded_trans.get() and ent_ded_young.get():
            showinfo("Résultat", f"Revenu sans les déduction : {temp_income()}")    
 
 
    if ded_young.get() or ded_trans.get() or ded_discount.get():
        income = temp_income()
        discount = float(ent_ded_discount.get()) / 100
        if ded_young.get():
            income -= float(ent_ded_young.get())
        if ded_trans.get():
            income -= float(ent_ded_trans.get())
        if ded_discount.get():
            income -= income * discount
        showinfo("Résultat", f"Revenu avec les déduction : {income:.2f}")
           
window = Tk()
window.title("Déductions")
window.geometry("300x280")
 
frm_income = Frame(window)
frm_income.pack(fill=X)
 
 
lbl_income = Label(frm_income, text="Revenu annuel brut")
lbl_income.pack(side=LEFT, padx=(10,0))
ent_income = Entry(frm_income, justify='right')
ent_income.pack(side=RIGHT, padx=(0,20))
ent_income.focus()
 
frm_coeff = Frame(window)
frm_coeff.pack(fill=X, pady=(10,0))
 
 
lbl_coeff = Label(frm_coeff, text="Coefficient familial")
lbl_coeff.pack(side=LEFT, padx=(10,0))
ent_coeff = Entry(frm_coeff, width=10, justify='right')
ent_coeff.pack(side=RIGHT, padx=(0,20))
 
frm_young = Frame(window)
frm_young.pack(fill=X)
 
ded_young = BooleanVar()
chk_ded_young = Checkbutton(frm_young, text="Déduction jeune", variable=ded_young)
chk_ded_young.pack(side=LEFT, padx=(50,0))
ent_ded_young = Entry(frm_young, width=10, justify='right')
ent_ded_young.insert(0, "900")
ent_ded_young.pack(side=RIGHT, padx=(0,20))
 
frm_trans = Frame(window)
frm_trans.pack(fill=X)
 
ded_trans = BooleanVar()
chk_ded_trans = Checkbutton(frm_trans, text="Déduction transport", variable=ded_trans)
chk_ded_trans.pack(side=LEFT, padx=(50,0))
ent_ded_trans = Entry(frm_trans, width=10, justify='right')
ent_ded_trans.insert(0, "650")
ent_ded_trans.pack(side=RIGHT, padx=(0,20))
 
frm_discount = Frame(window)
frm_discount.pack(fill=X)
 
ded_discount = BooleanVar()
chk_ded_discount = Checkbutton(frm_discount, text="Rabais fidélité (%)", variable=ded_discount)
chk_ded_discount.pack(side=LEFT, padx=(50,0))
ent_ded_discount = Entry(frm_discount, width=10, justify='right')
ent_ded_discount.insert(0, "4")
ent_ded_discount.pack(side=RIGHT, padx=(0,20))
 
btn_calcul = Button(window, text="Calcul", command=deduction)
btn_calcul.pack(pady=10)
 
 
window.mainloop()