myList = [3,5,6,7,13,14,15,]
guesses = ()

num = int(input("guess a number from 1-20: ") )

if num in myList:
    print("Good Job!")
    guesses.append (num)



elif num not in myList:
            print("Try again!")
            guesses.append  (num)


            
            print("you guessed: " + str(guesses))
            print("your numbers were   "+str(myList))


    
