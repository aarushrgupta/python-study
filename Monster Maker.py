# Monster Maker
from random import *

number = ["one-", "two-", "three-", "four-"]
face = ["eyed-", "nosed-", "toothed-", "eared-"]
body = ["armed-", "legged-", "tailed-", "headed-"]
action = ["flying-", "fire-breathing-", "gurgling-", "sneezing-"]
color = ["purple-", "green-", "orange-", "blue-"]
creature = ["dragon", "centaur", "griffin", "cyclops"]

choice = True
while choice == True:
    ask = input("Do you want to know what I just saw??? ")
    if ask == "yes":
        print("It was a "
              + number[(randrange(len(number)))]
              + face[(randrange(len(number)))]             
              + number[(randrange(len(number)))]
              + body[(randrange(len(number)))]
              + action[(randrange(len(number)))]
              + color[(randrange(len(number)))]              
              + creature[(randrange(len(number)))]
              + "!")
    else:
        choice = False

