from tkinter import *
from time import *
window = Tk()
canvas = Canvas(window, bg="dark blue", height=300, width=300)
canvas.pack()

canvas.create_oval(0, 0, 300, 300, fill="tan", width=0)
canvas.create_oval(0, 0, 100, 100, fill="tan", width=0)
canvas.create_oval(300, 0, 200, 100, fill="tan", width=0)
canvas.create_oval(200, 150, 250, 200, fill="green", width=0)

#This is when the eye will wink
eye = canvas.create_oval(50, 150, 100, 200, fill="green", width=0)
canvas.create_line(60, 155, 100, 170, fill="green")
canvas.create_line(60, 190, 100, 170, fill="green")
canvas.create_line(150, 260, 150, 300, fill="green")
canvas.create_polygon(120, 200, 180, 200, 150, 260, fill="green")

def wink(event):
    canvas.itemconfig(eye, state="hidden")
    window.update()
    sleep(0.3)
    canvas.itemconfig(eye, state="normal")

window.bind("<KeyPress-space>", wink)


