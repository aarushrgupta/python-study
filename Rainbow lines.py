from tkinter import *
from random import *
from time import *

window = Tk()
canvas = Canvas(window, bg="white", height=300, width=300)
canvas.pack()

Color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    sleep(0.5)
    canvas.delete("all")

    x = randint(0, 300)
    y = randint(0, 300)
    x2 = randint(0, 300)
    y2 = randint(0, 300)
    x3 = randint(0, 300)

    rand_index = randrange(len(Color_list))
    rand_color = Color_list[rand_index]

    canvas.create_pentagon(x, y, x2, y2, x3, fill=rand_color, width=10)
    window.update()
