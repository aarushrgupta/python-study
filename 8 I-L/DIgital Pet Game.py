from tkinter import *
from tkinter.ttk import *
from tkinter.simpledialog import *
from time import *
from random import *


# Initialization
root = Tk()
root.geometry("300x650+500+50")

calm_img = PhotoImage(file='calm.png')
happy_img = PhotoImage(file='happy.png')
grumpy_img = PhotoImage(file='grumpy.png')
sad_img = PhotoImage(file='sad.png')
annoyed_img = PhotoImage(file='annoyed.png')

pet_img = PhotoImage(file='pet.png')
play_img = PhotoImage(file='play.png')
feed_img = PhotoImage(file='feed.png')

pauseicon = PhotoImage(file='pauseicon.png')

play_level = 50
feed_level = 50
pet_level = 50

#Functions
def check_play(lower, upper):
    if play_level >= lower and play_level <= upper:
        return True
    else:
        return False
def check_feed(lower, upper):
    if feed_level >= lower and feed_level <= upper:
        return True
    else:
        return False
def check_pet(lower, upper):
    if pet_level >= lower and pet_level <= upper:
        return True
    else:
        return False

def update_display():
    if time() < annoyed_done:
        display_lbl.configure(image=annoyed_img)
    elif check_play(33, 66) and check_feed(33, 66) and check_feed(33, 75):
        display_lbl.configure(image=calm_img)
    elif check_play(50, 75) and check_feed(50, 75) and check_feed(50, 75):
        display_lbl.configure(image=happy_img)
    elif check_play(25, 100) and check_feed(25, 100) and check_feed(25, 100):
        display_lbl.configure(image=grumpy_img)
    else:
        display_lbl.configure(image=sad_img)

def update_ui():
    Play_bar['value'] = play_level
    Feed_bar['value'] = feed_level
    Pet_bar['value'] = pet_level
    update_display()

def play():
    global play_level
    check_click()
    play_level += 5
    if play_level > 100:
        play_level = 100
    update_ui()
    
def feed():
    global feed_level
    check_click()
    feed_level += 5
    if feed_level > 100:
        feed_level = 100
    update_ui()
    
def pet():
    global pet_level
    check_click()
    pet_level += 5
    if pet_level > 100:
        pet_level = 100
    update_ui()

def update_levels():
    global play_level, feed_level, pet_level
    which = randint(1, 3)
    if which == 1 and play_level >= 5:
        play_level -= 5
    if which == 2 and play_level >= 5:
        feed_level -= 5
    if which == 3 and pet_level >= 5:
        pet_level -= 5

next_update = 0
def schedule_update():
    global next_update
    delay = randint(2, 3)
    next_update = time() + delay

playing = True
def frame():
    root.after(100, frame)
    if playing == True:
        if time() >= next_update:
            update_levels()
            schedule_update()
        update_ui()

last_click = 0
annoyed_done = 0
def check_click():
    global last_click, annoyed_done
    cur = time()
    if cur - last_click < 1:
        annoyed_done = cur + 5
    last_click = cur

def toggle_pause():
    global playing
    if playing == True:
        playing = False
    else:
        playing = True

# Set up UI
calm_img = PhotoImage(file='calm.png')
display_lbl = Label(root, image=calm_img, bg="sky blue")
display_lbl.pack(pady=10)

name_lbl = Label(root, text="Name", fg="green", font=("Helvetica", 20), bg="sky blue")
name_lbl.pack()

play_btn = Button(root, text="Play", width=10, command=play)
play_btn.pack(pady=10)

play_btn = Button(root, text="Feed", width=10, command=feed)
play_btn.pack(pady=10)

play_btn = Button(root, text="Pet", width=10, command=pet)
play_btn.pack(pady=10)

Play_lbl = Label(root, image=play_img, bg="sky blue")
Play_lbl.pack()

Play_bar = Progressbar(root, length=250)
Play_bar.pack()

Feed_lbl = Label(root, image=feed_img, bg="sky blue")
Feed_lbl.pack()

Feed_bar = Progressbar(root, length=250)
Feed_bar.pack()

Pet_lbl = Label(root, image=pet_img, bg="sky blue")
Pet_lbl.pack()

Pet_bar = Progressbar(root, length=250)
Pet_bar.pack()

paused_btn = Button(root, image=pauseicon, command=toggle_pause)
paused_btn.pack(pady=10)

root.configure(bg="sky blue")

# Start Game
name = askstring("Name", "What's your pet's name?")
name_lbl.configure(text=name)


schedule_update()
frame()
