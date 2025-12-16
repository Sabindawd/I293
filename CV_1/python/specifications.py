from tkinter import *
from tkinter import messagebox

match_over = False

def add_point(lbl, lbl_sets, side_name):
    global match_over
    if match_over:
        return  
    
    try:
        points_to_win = int(ent_points.get())
        sets_to_win = int(ent_sets.get())
    except ValueError:
        messagebox.showerror("Error", "Entrez des nombres valides pour les points et les sets.")
        return
    
    current = int(lbl['text'])
    lbl.config(text=str(current + 1))
    
    if int(lbl['text']) >= points_to_win:
        sets = int(lbl_sets['text'])
        lbl_sets.config(text=str(sets + 1))
        lbl.config(text="0")
        
        if sets + 1 >= sets_to_win:
            match_over = True
            messagebox.showinfo("Match finit", f"{side_name} gagnez!")

def delete_point(lbl):
    if match_over:
        return  
    current = int(lbl['text'])
    if current > 0:
        lbl.config(text=str(current - 1))

window = Tk()
window.title("Score")
window.geometry("400x400")
window.configure()

frm_points = Frame(window)
frm_points.pack()

lbl_points = Label(frm_points, text="Nombre de points:")
lbl_points.pack(side=LEFT)

ent_points = Entry(frm_points, bg="white")
ent_points.pack()
ent_points.insert(0, "")  

frm_sets = Frame(window)
frm_sets.pack()

lbl_sets = Label(frm_sets, text="Nombre de sets:")
lbl_sets.pack(side=LEFT, pady=15)

ent_sets = Entry(frm_sets, bg="white")
ent_sets.pack(pady=15)
ent_sets.insert(0, "")  

# LOCAL
frm_local = Frame(window)
frm_local.pack(side=LEFT, padx=25)

frm_local_labels = Frame(frm_local)
frm_local_labels.pack()

lbl_local_title = Label(frm_local_labels, text="Local:")
lbl_local_title.pack(pady=15)

lbl_local_sets_title = Label(frm_local_labels, text="Sets: ")
lbl_local_sets_title.pack(pady=15)

lbl_local_sets = Label(frm_local_labels, text="0")
lbl_local_sets.pack()

lbl_local_points_title = Label(frm_local_labels, text="Points: ")
lbl_local_points_title.pack(pady=15)

lbl_local_points = Label(frm_local_labels, text="0")
lbl_local_points.pack()

# BUTTONS LOCAL
btn_local_plus = Button(frm_local, text="+", fg="green", 
                        command=lambda: add_point(lbl_local_points, lbl_local_sets, "Local"))
btn_local_plus.pack(side=LEFT, pady=15)

btn_local_minus = Button(frm_local, text="-", fg="red", 
                         command=lambda: delete_point(lbl_local_points))
btn_local_minus.pack(side=RIGHT)

# INVITE
frm_invite = Frame(window)
frm_invite.pack(side=RIGHT, padx=25)

frm_invite_labels = Frame(frm_invite)
frm_invite_labels.pack()

lbl_invite_title = Label(frm_invite_labels, text="Invite:")
lbl_invite_title.pack(pady=15)

lbl_invite_sets_title = Label(frm_invite_labels, text="Sets:")
lbl_invite_sets_title.pack(pady=15)

lbl_invite_sets = Label(frm_invite_labels, text="0")
lbl_invite_sets.pack()

lbl_invite_points_title = Label(frm_invite_labels, text="Points:")
lbl_invite_points_title.pack()

lbl_invite_points = Label(frm_invite_labels, text="0")
lbl_invite_points.pack(pady=15)

# BUTTONS INVITE
btn_invite_plus = Button(frm_invite, text="+", fg="green", 
                         command=lambda: add_point(lbl_invite_points, lbl_invite_sets, "Invite"))
btn_invite_plus.pack(side=LEFT)

btn_invite_minus = Button(frm_invite, text="-", fg="red", 
                          command=lambda: delete_point(lbl_invite_points))
btn_invite_minus.pack(side=RIGHT)

window.mainloop()
