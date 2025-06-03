rid = ["What belongs to you, but other people use?",
       "What do you break before using it?",
       "What's brown and sticky"]


ans = ["your name", "an egg", "a stick"]

def riddle(choice):
    question = rid[choice]
    print(question)
    answer = input()

    correct = ans[choice]

    while answer != correct:
        answer = input("Try again: ")

    print("Good job!")  
