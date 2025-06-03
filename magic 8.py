from random import *
fortune = ["yes", "definitely", "it seems so",
           "no", "nope", "not likely",
           "maybe", "could be", "answer hazy"]
while True:
    ask = input("Ask a question with a yes or no answer: ")
    if ask == "quit": break
    answer = randrange(len(fortune))
    print(fortune[answer])






































    
