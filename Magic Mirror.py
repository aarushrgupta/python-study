from random import *
Answers = ["Yours, of course!", "I don't know.", "Whose do you think?", "Maybe someone else.", "Not you!"]
print("Whose lucky day is it today?")
while True:
    Phrase = input("Call upon the magic mirror! ")
    if Phrase == "mirror mirror":
        reply = randrange(len(Answers))
        print(Answers[reply])
        print("Why don't you ask again?")
    else: print("Try saying mirror mirror...")
