
# donut animation
from turtle import *
from random import *
from time import *

replies = ["yum", "I love donuts!", "it's all gone", "that was great"]
print("Feed your computer a donut!")
choice = input("Type 1 to feed your computer a donut, 2 to quit: ")

if choice == "1":
    setup(700, 700)
    speed("fastest")
    bgcolor("lightblue")
    color("brown")
    dot(400)
    color("lightblue")
    dot(200)
    
    sleep(0.5)
    goto(150, 0)
    dot(200)
    
    sleep(0.5)
    goto(100, 100)
    dot(200)
    
    sleep(0.5)
    goto(100, -75)
    dot(200)
    
    sleep(0.5)
    goto(25, -125)
    dot(200)
    
    sleep(0.5)
    goto(0, 125)
    dot(200)
    
    sleep(0.5)
    goto(-75, 100)
    dot(200)
    
    sleep(0.5)
    goto(-150, 0)
    dot(200)
    
    sleep(0.5)
    goto(-75, -100)
    dot(200)
    
    ind = randrange(len(replies))
    
    print(replies[ind])
    
elif choice == "2":
    print("I wish I had gotten that donut :(")
    
else:
    
    print("Please type a 1 or 2!")
