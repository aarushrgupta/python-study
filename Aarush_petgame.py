from tkinter import *
from tkinter.ttk import *
from tkinter.simpledialog import *
from time import *
from random import *


# initialization
root = Tk()
root.geometry("300x650+500+50")

calm_ing = PhotoImage(file="calm.png")
happy_ing = PhotoImage(file="happy.png")
grumpy_ing = PhotoImage(file="grumpy.png")
sad_ing = PhotoImage(file="sad.png")
annoyed_ing = PhotoImage(file="annoyed.png")

pet_ing = PhotoImage(file="pet.png")
play_ing = PhotoImage(file="play.png")
feed_ing = PhotoImage(file="feed.png")

pauseicon = PhotoImage(file="pauseicon.png")

play_level = 50
feed_level = 50
pet_level = 50

#set up UI
calm_ing = PhotoImage(file="calm.png")
display_lbl = Lable(root, image=calm_img)
display_lbl.pack(pady=10)
