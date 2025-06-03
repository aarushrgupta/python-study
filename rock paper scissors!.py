from random import *
from time import *

player_list = ["rock", "paper", "scissors"]

print("let's play rock, paper, scissors!")
start = input("type rock, paper,rock or scissors: ")

answer = randrange(len(player_list))

if start == "rock":
    print("rock")
    sleep(0.5)
    print(player_list[answer])
elif start == "paper":
    print("paper")
    sleep(0.5)
    print(player_list[answer])
elif start == "scissors":
    print("scissors")
    sleep(0.5)
    print(player_list[answer])
else:
    print("I don't understand what your saying!")




