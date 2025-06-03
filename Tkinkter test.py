from tkinter import *
window = Tk()
canvas = Canvas(window, bg="white", height=300, width=300)
canvas.pack()

canvas.create_square(50, 50, 250, 250, fill="blue")
