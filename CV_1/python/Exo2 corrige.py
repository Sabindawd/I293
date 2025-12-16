# Function : score management
# author : Frédérique Andolfatto
# Date : 18.11.2024
# Version : 1.0

from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("Score")
window.geometry("300x280")


nb_sets_local = 0
nb_points_local = 0
nb_sets_guest = 0
nb_points_guest = 0

nb_sets = 0
nb_points = 0


# Check values and format in entries fields
def check_entry():
    global nb_sets, nb_points
    if ent_set_nb.get() == "":
        raise Exception("le nombre de sets ne peut pas être vide")

    if ent_points_nb.get() == "":
        raise Exception("le nombre de points ne peut pas être vide")

    nb_sets = int(ent_set_nb.get())
    if nb_sets < 0:
        raise Exception("Le nombre de sets ne peut pas être négatif")

    nb_points = int(ent_points_nb.get())
    if nb_points < 0:
        raise Exception("Le nombre de points ne peut pas être négatif")


# enable buttons
def enable_buttons():
    btn_guest_minus.config(state="normal")
    btn_guest_plus.config(state="normal")
    btn_local_plus.config(state="normal")
    btn_local_minus.config(state="normal")


# reset points values
def reset_nb_points():
    global nb_points_local, nb_points_guest
    nb_points_local = 0
    nb_points_guest = 0


# display points values
def display_nb_points():
    lbl_points_local.configure(text="Points : " + str(nb_points_local))
    lbl_points_guest.configure(text="Points : " + str(nb_points_guest))


# increase of 1 the number of points for the local part
def increase_points_local():
    global nb_points_local, nb_sets_local, nb_points_guest, nb_points, nb_sets, window
    try:
        check_entry()
        nb_points_local = nb_points_local + 1
        if (nb_points_local % nb_points) == 0:
            nb_sets_local = nb_sets_local + 1
            lbl_set_local.configure(text="Sets : " + str(nb_sets_local))
            reset_nb_points()
        display_nb_points()
        if nb_sets_local >= nb_sets:
            showinfo(title="game over", message="Bravo, l'équipe locale a gagné!")
            window.quit()
    except ValueError:
        showinfo(title="Données incorrectes", message="Les nombres de points doivent être entiers")
    except Exception as e:
        showinfo(title="Données incorrectes", message=str(e))


# decrease of 1 the number of points for the local part
def decrease_points_local():
    global nb_points_local
    try:
        check_entry()
        if nb_points_local == 0:
            showinfo("Erreur", f"Impossible de diminuer le nombre de points, il est déjà à 0")
        else:
            nb_points_local = nb_points_local - 1
            lbl_points_local.configure(text="Points : " + str(nb_points_local))
    except ValueError:
        showinfo(title="Données incorrectes", message="Les nombres de points doivent être entiers")
    except Exception as e:
        showinfo(title="Données incorrectes", message=str(e))


# increase of 1 the number of points for the guest part
def increase_points_guest():
    global nb_points_guest, nb_sets_guest, nb_points_local, nb_points, nb_sets, window
    try:
        check_entry()
        nb_points_guest = nb_points_guest + 1
        if (nb_points_guest % nb_points) == 0:
            nb_sets_guest = nb_sets_guest + 1
            lbl_set_guest.configure(text="Sets : " + str(nb_sets_guest))
            reset_nb_points()
        display_nb_points()
        if nb_sets_guest >= nb_sets:
            showinfo(title="game over", message="Bravo, l'équipe 'invité' a gagné!")
            window.quit()
    except ValueError:
        showinfo(title="Données incorrectes", message="Les nombres de points doivent être entiers")
    except Exception as e:
        showinfo(title="Données incorrectes", message=str(e))


# decrease of 1 the number of points for the guest part
def decrease_points_guest():
    global nb_points_guest
    try:
        check_entry()
        if nb_points_guest == 0:
            showinfo("Erreur", f"Impossible de diminuer le nombre de points, il est déjà à 0")
        else:
            nb_points_guest = nb_points_guest - 1
            lbl_points_guest.configure(text="Points : " + str(nb_points_guest))
    except ValueError:
        showinfo(title="Données incorrectes", message="Les nombres de points doivent être entiers")
    except Exception as e:
        showinfo(title="Données incorrectes", message=str(e))


# enable buttons if entry fields are not empty, called when the set nb field is released
def leave_sets_nb(event):
    if ent_set_nb.get() != "" and ent_points_nb.get() != "":
        enable_buttons()


# enable buttons if entry fields are not empty, called when the points nb field is released
def leave_points_nb(event):
    if ent_set_nb.get() != "" and ent_points_nb.get() != "":
        enable_buttons()


# UI - widgets - Frames - Label - Entry - Buttons
frm_nb_set = Frame(window)
frm_nb_set.pack(fill=X)

lbl_set_nb = Label(frm_nb_set, text="Nombre de sets : ")
lbl_set_nb.pack(padx=10, pady=10, side=LEFT)

ent_set_nb = Entry(frm_nb_set)
ent_set_nb.name = "nb sets"
ent_set_nb.pack(side=RIGHT, padx=10, pady=10)
ent_set_nb.bind('<KeyRelease>', leave_sets_nb)
ent_set_nb.focus()

frm_nb_points = Frame(window)
frm_nb_points.pack(fill=X)

lbl_points_nb = Label(frm_nb_points, text="Nombre de points : ")
lbl_points_nb.pack(padx=10, pady=10, side=LEFT)

ent_points_nb = Entry(frm_nb_points)
ent_points_nb.name = "nb points"
ent_points_nb.pack(side=RIGHT, padx=10, pady=10)

ent_points_nb.bind('<KeyRelease>', leave_points_nb)

# interesting : https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method
frm_local = Frame(window)
frm_local.pack(side=LEFT, expand=1, fill=X)

lbl_local = Label(frm_local, text="Local : ")
lbl_local.pack(padx=10, pady=10)

lbl_set_local = Label(frm_local, text="Sets : 0")
lbl_set_local.pack(padx=10, pady=10)

lbl_points_local = Label(frm_local, text="Points : 0")
lbl_points_local.pack(padx=10, pady=10)


btn_local_plus = Button(frm_local, text="+", fg="red", command=increase_points_local, state=DISABLED)
btn_local_plus.pack(side=LEFT, anchor=E, expand=1, padx=(5, 0), pady=10)
btn_local_minus = Button(frm_local, text="-", fg="green", command=decrease_points_local, state=DISABLED)
btn_local_minus.pack(side=LEFT, anchor=W, expand=1, padx=(5, 0), pady=10)

frm_guest = Frame(window)
frm_guest.pack(side=LEFT, expand=1, fill=X)

lbl_guest = Label(frm_guest, text="Invité : ")
lbl_guest.pack(padx=10, pady=10)

lbl_set_guest = Label(frm_guest, text="Sets : 0")
lbl_set_guest.pack(padx=10, pady=10)

lbl_points_guest = Label(frm_guest, text="Points : 0")
lbl_points_guest.pack(padx=10, pady=10)

btn_guest_plus = Button(frm_guest, text="+", fg="red", command=increase_points_guest, state=DISABLED)
btn_guest_plus.pack(side=LEFT, expand=1, anchor=E, padx=(5, 0), pady=10)
btn_guest_minus = Button(frm_guest, text="-", fg="green", command=decrease_points_guest, state=DISABLED)
btn_guest_minus.pack(side=LEFT, expand=1, anchor=W, padx=(5, 0), pady=10)


window.mainloop()
