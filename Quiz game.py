#Quiz Game


print('''
1. What orange veggetable do rabbits like?
a - Orange
b - Carrot
c - broccoli\n
''')

answer1 = input()


if answer1 == "b":
    print("correct!")
else:
    print(" sorry, wrong answer.")




print('''
1. What animal has a really long neck?
a - Giraffe
b - parrot
c - Gorilla\n
''')

answer2 = input()


if answer2 == "a":
    print("correct!")
else:
    print(" sorry, wrong answer.")

if answer1 == "b" and answer2 =="a":
    print(" YOU WIN! ")
else:
    print(" YOU LOST! ")


