# Function : creation of an user interface with tkinter : moves and colors of a window
# author : Frédérique Andolfatto
# Date : 18.11.2024
# Version : 1.0

from tkinter import *
from tkinter.messagebox import *

window = Tk()
window.title("FenetreBleuRouge")

window_width = 270
window_height = 330

# width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# for statistics
nb_clicks_move = 0
nb_clicks_color_changed = 0

# set the window in the center of the screen
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))


def move_high_left():
    global nb_clicks_move
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, 0, 0))
    nb_clicks_move += 1


# https://stackoverflow.com/questions/71007339/how-to-make-a-tkinter-window-align-to-the-right
# x and y specify the desired location of window on the screen, in pixels. If x is preceded by +, it specifies the number of pixels between the left edge of the screen and the left edge of window's border;
# if preceded by - then x specifies the number of pixels between the right edge of the screen and the right edge of window's border.
# If y is preceded by + then it specifies the number of pixels between the top of the screen and the top of window's border;
# if y is preceded by - then it specifies the number of pixels between the bottom of window's border and the bottom of the screen.
def move_high_right():
    global nb_clicks_move
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, screen_width-window_width, 0))
    # other solution according to comments above
    # window.geometry("-0+0")
    nb_clicks_move += 1


def set_blue_bg():
    global window, nb_clicks_color_changed
    window.configure(bg="blue")
    frm_top.configure(bg="blue")
    frm_center.configure(bg="blue")
    frm_bottom.configure(bg="blue")
    nb_clicks_color_changed += 1


def set_red_bg():
    global window, nb_clicks_color_changed
    window.configure(bg="red")
    frm_top.configure(bg="red")
    frm_center.configure(bg="red")
    frm_bottom.configure(bg="red")
    nb_clicks_color_changed += 1


def move_low_left():
    print("hl")
    global nb_clicks_move
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, 0, screen_height-window_height-70))
    # other solution according to comments above
    # window.geometry("+0-0")
    nb_clicks_move += 1


def move_low_right():
    print("hl")
    global nb_clicks_move
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, screen_width-window_width,
                                         screen_height-window_height-70))
    # other solution according to comments above
    # window.geometry("-0-0")
    nb_clicks_move += 1


def give_stats():
    showinfo("Statistiques", f"{nb_clicks_color_changed} changement(s) de couleur, {nb_clicks_move} déplacement(s)")


def quit_app():
    window.quit()


# Frame for buttons at the top
frm_top = Frame(window)
frm_top.pack(side=TOP, fill=X)

# Button on the left
btn_top_left = Button(frm_top, text="Haut Gauche", command=move_high_left)
btn_top_left.pack(side=LEFT)

# Button on the right
btn_top_right = Button(frm_top, text="Haut Droite", command=move_high_right)
btn_top_right.pack(side=RIGHT)

# Frame for buttons in the middle
frm_center = Frame(window)
frm_center.pack(side=TOP)

btn_blue = Button(frm_center, text="Bleu", command=set_blue_bg)
btn_blue.pack(padx=10, pady=(30, 5))

btn_red = Button(frm_center, text="Rouge", command=set_red_bg)
btn_red.pack(padx=10, pady=(5, 20))

btn_stats = Button(frm_center, text="Stats", command=give_stats)
btn_stats.pack(padx=10, pady=(30, 10))

btn_quit = Button(frm_center, text="Quitter", command=quit_app)
btn_quit.pack(padx=10, pady=(30, 30))

# Frame for buttons below
frm_bottom = Frame(window)
frm_bottom.pack(fill=X)

# Button on the left
btn_bottom_left = Button(frm_bottom, text="Bas Gauche", command=move_low_left)
btn_bottom_left.pack(side=LEFT)

# Button on the right
btn_bottom_right = Button(frm_bottom, text="Bas Droite", command=move_low_right)
btn_bottom_right.pack(side=RIGHT)

window.mainloop()
