from random import *

# Global variables
all_names = []
all_answers = []
answers = []

def quiz():
    global user_name
    user_name = input("Can you type your name again for me? ")
    all_names.append(user_name)
    quiz_intro = ["Thanks " + user_name + ". I love to talk!",
                  "Okay " + user_name + ", Let's chat about coding",
                  "What do you think of coding " + user_name + "?"]
    print(quiz_intro[randrange(len(quiz_intro))])

    
    # ask the questions
    # First
    print("Here's the first question. How much do you like coding?")
    choice = input("Type a number from 1 to 5. 1 being meh, I could do without to 5, being obsessed with it: ")

    need_input = True
    if (len(choice) == 1 and choice >= "1" and choice <= "5"):
        choice = int(choice)
        need_input = False
    else:
        print("Sorry, I don't understand that")
        print("Please enter a number a number between 1 to 5")
        choice = input()
    answers.append(choice)

    replies = ["I really love coding " + user_name + "!",
               "My favorite laguage of coding is Python!",
               "Did you know " + user_name +
               "? There are up to 250 to 2500 types of coding languages in the world!"]
    print(replies[randrange(len(replies))])
    print("\n")

    # Second
    print("Here's the second question. How long have you done coding?")
    choice = input("Type a number from 1 to 5. 1 being not that long to 5, been doing it for a long time: ")

    if (len(choice) == 1 and choice >= "1" and choice <= "5"):
        choice = int(choice)
        need_input = False
    else:
        print("Sorry, I don't understand that")
        print("Please enter a number a number between 1 to 5")
        choice = input()
    answers.append(choice)

    replies = ["I have been doing coding for a long time " + user_name + "!",
               "Somebody even coded me!",
               "Did you know " + user_name +
               "? The first computer program was generally dated to 1843!"]
    print(replies[randrange(len(replies))])
    print("\n")

    # Third
    print("Here's the third question. Is Python your favorite coding laguage?")
    choice = input("Type a number from 1 to 5. 1 being no, It isn't my favorite to 5, being It is my favorite!: ")

    if (len(choice) == 1 and choice >= "1" and choice <= "5"):
        choice = int(choice)
        need_input = False
    else:
        print("Sorry, I don't understand that")
        print("Please enter a number a number between 1 to 5")
        choice = input()
    answers.append(choice)

    replies = ["Thank you for sharing your opinion, " + user_name + "!",
               "That's a great opinion!",
               "I agree with you, " + user_name]
    print(replies[randrange(len(replies))])
    print("\n")
    all_answers.append(answers)


def report():
    qsum = 0
    report_intro = ["Okay, " + user_name + ", Lets see what other people think.",
                    "Who else has answered the questions so far?",
                    "What does everyone think about coding?"]
    print(report_intro[randrange(len(report_intro))])
    if len(all_names) == 0:
        print("Oops, I don't have anything to report to you yet!")
    else:
        for i in range(len(all_names)):
            name = all_names[i]
            answers = all_answers[i]
            print(name + ":" + str(answers))
            qsum += answers[1]
        print("The average rating for question 2 was " + str(qsum/len(all_names)) + ".")

# Display greeting
print("Hi! I'm Chaty the ChatBot!")
print("What's your name?")
user_name = input()
print("Nice to meet you, " + user_name + "!")
intro_list = ["How old are you?", "Where do you live?",
              "What grade are you in?"]
input(intro_list[randrange(len(intro_list))])
print("That's cool! :) Thanks for sharing!")

print("I talk to people about coding!")
print("Sometimes I sound like a robot, but I try my best.")
input("Are you good at sounding like a human?")
human_list = ["SILLY me! You ARE a human!",
              "You sure sound like a human to me!",
              "I wish I was good at sounding human as you."]
print(human_list[randrange(len(human_list))])

# choice 1 is for quiz
# choice 2 is for report
# choice 3 is for exit

while True:
    print("What would you like to do today?")
    print("1) Put your knowlege of coding to the test.")
    print("2) Veiw the report.")
    print("3) Say goodbye!")
    Choice = input("Choice: ")

    if Choice == "1":
        quiz()
        # print("quiz")
    elif Choice == "2":
        report()
        #print("report")
    elif Choice == "3":
        goodbye_responses = ["Have a great day " + user_name + "!",
                             "Thanks for chatting with me " + user_name + "!",
                             "Goodbye! " + user_name + "!"]
        print(goodbye_responses[randrange(len(goodbye_responses))])
        break
    else:
        print("I am sorry. I don't understand. Please type 1, 2, or 3.")
