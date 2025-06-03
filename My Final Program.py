# Icecream makeret
from random import *

Size = ["Small- ", "Mediem- ", "Large- "]
Flavor = ["Chocolate flavored- ", "Vanilla flavored- ", "Strawberry flavored- ", "Mint flavored- "]
Sprinkles = ["Rainbow sprinkled- ", "Chocolate sprinkled- ", "Vanilla sprinkled- "]
Surup = ["Chocolate Suruped- ", "Strawberry suruped- ", "Maple Suruped- "]

Check = True
while Check == True:
    ask = input("Hello! Do you want to have some Ice cream? ")
    if ask == "yes":
        print("Awsome sauce!! You will have a "
              + Size[(randrange(len(Size)))]
              + Flavor[(randrange(len(Flavor)))]             
              + Sprinkles[(randrange(len(Sprinkles)))]
              + Surup[(randrange(len(Surup)))]
              + " Ice Cream!")
    elif ask == "no":
        print("If you want ice cream, you can just come here again!")
        Check = False
    else:
        print("Enter right response please:  ")
        Check = True

