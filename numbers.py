from random import *
secret = randint(1, 10)
print("Can you guess the number I picked?")
ans = int(input("Pick a number from 1-10: "))
if ans == secret:
    print("you got it!")
else:
    print("Nope. It was " + str(secret))
    
    
