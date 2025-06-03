# Fortune Teller
from random import *
fortunes = ["Luck will find you!",
            "You have a hard road ahead of you.",
            "Happy days are here again!",
            "Just go back to bed. This isn't your day.",
            "You're going to become a rock star some day!"]


no_fortune = ["The future is a mystery!",
              "I guess you'd rather be surprised...",
              "Have a nice day."]

check = True

while check == True:
    ask = input("Do you want to read your fortune? Answer y or n: ")
    if ask == "y":
        print(fortunes[randrange(len(fortunes))])
    elif ask == "n":
        print(no_fortune[randrange(len(no_fortune))])
        check = False
    else: print("Please type y or n.")
