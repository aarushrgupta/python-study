# Taco animation
from turtle import *
from random import *
from time import *

replies = ["Yummy!", "I love bagles!", "I ate the bagle too fast!", "That tasted so amazing!"]
bad_replies = ["That's disgusting!", "I hate it!", "I don't like it at all!", ]

print("Feed your computer a taco!")
choice = input("Type 1 to feed your computer a taco, or 2 to quit: ")

if choice == "1":
    setup(700, 700)
    speed("fastest")
    bgcolor("sky blue")
    
elif choice == "2":
    print(2)
else:
    print(3)

    
