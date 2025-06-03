from random import *
# greeting
print("Hi! What's your name?")
name = input("> ")
print("Nice to meet you " + name + "!")

running = True
# main loop
while running:
    # menu
    choice = input("What math quiz do you want to do?"
                   +"\n1) Take the Multiplication quiz"
                   +"\n2) Take the Division quiz"
                   +"\n3) Take the Fractions quiz"
                   +"\n4) Leave"
                   +"\n> ")
    score = 0
 # Questions   
    if choice == "1":
        Question_num1 = [42,56,32,324,1224]
        Question_num2 = [10,24,2,7,9]
        for i in range(5):
            num1 = Question_num1[i]
            num2 = Question_num2[i]
            ans = num1 * num2
            question = int(input("What is " + str(num1) + "*" + str(num2) + "? \n> "))
            print(str(question))
            if (question == ans):
                print("Correct!")
                score += 1
            else:
                print("Sorry! That's wrong")

                
    elif choice == "2":
        Question_num1 = [42,90,32,552,1224]
        Question_num2 = [2,3,2,6,6]
        for i in range(5):
            num1 = Question_num1[i]
            num2 = Question_num2[i]
            ans = num1 / num2
            question = int(input("What is " + str(num1) + "/" + str(num2) + "? \n> "))
            print(str(question))
            if (question == ans):
                print("Correct!")
                score += 1
            else:
                print("Sorry! That's wrong")

                
    elif choice == "3":
        Question_num1 = [223,337.5,88.8,555, 1228]
        Question_num2 = [2, 3, 2, 6, 6]
        for i in range(5):
            num1 = Question_num1[i]
            num2 = Question_num2[i]
            ans = num1 / num2
            question = float(input("Simplify " + str(num1) + " to " + str(num2) + "\n>"))
            if question == ans:
                print("Correct!")
                score += 1
            else:
                print("Sorry! That's wrong")

    elif choice == "4":
        running = False


    else:
        print("I don't understand your choice. Please try again!")
    
    print("Your score was " + str(score) + "!")
