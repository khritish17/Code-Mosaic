import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()


canvas = tk.Canvas(root, width=1000, height=800)
canvas.grid(columnspan=3)

# logo
logo = PhotoImage(file="logo.png")
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)
root.mainloop()