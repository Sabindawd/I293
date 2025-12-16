# I319-fenetre_bleu_rouge.py
# Author: Balog Alexandru
# Date: 4.11.2025

from tkinter import *
from tkinter import messagebox

move_count = 0
color_count = 0

def blue():
    global color_count
    color_count += 1
    window.config(bg="blue")
    frm_top.config(bg="blue")
    frm_bottom.config(bg="blue")
    frm_middle.config(bg="blue")
    frm_middle1.config(bg="blue")

def red():
    global color_count
    color_count += 1
    window.config(bg="red")
    frm_top.config(bg="red")
    frm_bottom.config(bg="red")
    frm_middle.config(bg="red")
    frm_middle1.config(bg="red")

def hautgauche():
    global move_count
    move_count += 1
    window.geometry("+0+0")

def hautdroite():
    global move_count
    move_count += 1
    screen_width = window.winfo_screenwidth()
    window_width = window.winfo_width()
    x = screen_width - window_width
    window.geometry(f"+{x}+0")

def basgauche():
    global move_count
    move_count += 1
    screen_height = window.winfo_screenheight()
    window_height = window.winfo_height()
    y = screen_height - window_height
    window.geometry(f"+0+{y}")

def basdroite():
    global move_count
    move_count += 1
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = screen_width - window_width
    y = screen_height - window_height
    window.geometry(f"+{x}+{y}")

def show_stats():
    messagebox.showinfo("Statistiques",
                        f"Fenêtre déplacée : {move_count} fois\n"
                        f"Couleur changée : {color_count} fois")

window = Tk()
window.title("Fenêtre : ")
window.geometry("300x300+100+100")

frm_top = Frame(window)
frm_top.pack(fill=X)

btn_top_left = Button(frm_top, text="Haut/Gauche", command=hautgauche)
btn_top_left.pack(side=LEFT, padx=5, pady=5)

btn_top_right = Button(frm_top, text="Haut/Droite", command=hautdroite)
btn_top_right.pack(side=RIGHT, padx=5, pady=5)

frm_bottom = Frame(window)
frm_bottom.pack(fill=X, side=BOTTOM)

btn_bottom_left = Button(frm_bottom, text="Bas/Gauche", command=basgauche)
btn_bottom_left.pack(side=LEFT, padx=5, pady=5)

btn_bottom_right = Button(frm_bottom, text="Bas/Droite", command=basdroite)
btn_bottom_right.pack(side=RIGHT, padx=5, pady=5)

frm_middle = Frame(window)
frm_middle.pack(fill=X)

btn_blue = Button(frm_middle, text="Bleu", command=blue)
btn_blue.pack(pady=(20, 5))

btn_red = Button(frm_middle, text="Rouge", command=red)
btn_red.pack()

frm_middle1 = Frame(window)
frm_middle1.pack(fill=X, side=BOTTOM)

btn_stats = Button(frm_middle1, text="Stats", command=show_stats)
btn_stats.pack(pady=(1, 0))

btn_quit = Button(frm_middle1, text="Quitter", command=window.destroy)
btn_quit.pack(pady=(35, 35))

window.mainloop()
