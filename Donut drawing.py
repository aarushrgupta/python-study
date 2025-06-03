from tkinter import *
window = Tk()
canvas = Canvas(window, bg="lemon chiffon", height=300, width=300)
canvas.pack()

canvas.create_oval(50, 50, 250, 250, fill="burlywood")
canvas.create_oval(125, 125, 175, 175, fill="lemon chiffon")
