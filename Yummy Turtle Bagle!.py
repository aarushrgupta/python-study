# Bagle animation
from turtle import *
from random import *
from time import *

Replies = ["Yummy!", "I love bagles!", "I ate the bagle too fast!", "That tasted so amazing!"]

print("Feed your computer a bagle! It is now 50% off!")
choice = input("Type 1 to feed your computer a bagel, or 2 to quit: ")    

    
if choice == "1":
    setup(700, 700)
    speed("fastest")
    bgcolor("Orange")
    color("Tan")
    dot(400)
    setup(500, 700)
    begin_fill()
    color("white")
    circle(10)
    end_fill()
    color("Orange")
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

    ind = randrange(len(Replies))

    print(Replies[ind])
    
elif choice == "2":
    print("I wish I had gotten a Bagle :(")
    
else:
    print("Please type a 1 or 2 when you want to get a bagle! :)")
    
    
