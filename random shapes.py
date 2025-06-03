from tkinter import *
from random import *
from time import *

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


Color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    sleep(0.5)
    canvas.delete("all")

    x = randint(0, 300)
    y = randint(0, 300)
    x2 = randint(0, 300)
    y2 = randint(0, 300)

    rand_index = randrange(len(Color_list))
    rand_color = Color_list[rand_index]

    canvas.create_line(x, y, x2, y2, fill=rand_color, width=10)
    window.update()

