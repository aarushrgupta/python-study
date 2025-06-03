from tkinter import *

window = Tk()
canvas = Canvas(window, bg="red", height=300, width=300)
canvas.pack()

canvas.create_line(0,0,300,300, fill="yellow",width = 10)
canvas.create_line(300,0,0,300, fill="yellow",width = 10)
