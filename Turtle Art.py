
# turtle art

from turtle import *
from time import *
from random import *

colors = ["red", "blue", "green", "purple", "turquoise", "yellow"]

print("Welcome to my art program.")
choice = input("Type 1 to make art, 2 to quit: ")

if choice == "1":
    setup(700, 700)
    bgcolor("lightblue")
    speed("fastest")
    pensize(15)
    while True:

        try:
            action = randint(1, 20)
            
            if action >= 1 and action <= 3:
                ind = randrange(len(colors))
                color(colors[ind], "black")
            elif action >= 4 and action <= 8:
                pu()    
            elif action == 9:
                ind = randrange(len(colors))
                bgcolor(colors[ind])
            elif action == 10:
                clear()
            else:
                
                x = randint(-300, 300)
                y = randint(-300, 300)
                goto(x, y)
                
                dot(randint(10, 100))
                
                pd()
                sleep(0.1)
                
        except Terminator:
            print("Bye!")
            break
            
elif choice == "2":
    print("OK, goodbye!")
else:
    print("I only understand 1 and 2!!")
