myList = [1, 5, 8, 11, 20]
guesses = []

from random import *
while len(guesses) < 5:
    num = int(input("pick a number from 1-20: ") )
    print(num)
    if num in myList:
        print("Good!")
        guesses.append (num)


    elif num not in myList:
            print("Try again!")
            guesses.append  (num)


            print("you guessed: " + str(guesses))
            print("your numbers were   "+str(myList))
        
    
