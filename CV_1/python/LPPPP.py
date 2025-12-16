import tkinter as tk

root = tk.Tk()
root.title("My First Listbox")

# Box (container)
box = tk.Frame(root, borderwidth=2, relief="solid")
box.pack(padx=20, pady=20)

# Listbox
listbox = tk.Listbox(box, width=20, height=5)
listbox.pack()

# Add items
listbox.insert(tk.END, "Apple")
listbox.insert(tk.END, "Banana")
listbox.insert(tk.END, "Orange")

root.mainloop()
