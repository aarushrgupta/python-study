from random import *
print("The worm convention is beginning")
print("Are there enough apples for each worm to have one?")
worms = randint(0, 100)

apples = int(input("How many apples are there?: "))
print("There are " + str(worms) + " worms.")

if not apples > worms:
    print("Oh no! There are not enough apples for the worms. You need to get some more.")

else: print("It looks like you have enough apples!")
