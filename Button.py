from tkinter import *
from random import *
window = Tk()

canvas = Canvas(window, bg="white", height=300, width=300)
canvas.pack()

def button_press():
    Colors = ["red", "orange", "yellow", "green", "blue"]
    Color_index = randrange(len(Colors))
    Color_choices = Colors[Color_index]
    canvas.configure(bg=Color_choices)

button = Button(window, text="Push the BUTTON to change color!", command=button_press)
button.pack()
