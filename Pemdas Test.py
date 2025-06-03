Points = 0
print("Here are the rules:")
print(" Solve the problem.")
print(" Remember the order of operations: PEMDAS.")
print(" Each problem is the same, exept for the parentheses.")
print(" Answer bank: 11, 3, -180")

Q1 = int(input("4 + 7 * 3 - (11 * 2) = "))
if Q1 == 3:
    print("Correct!")
    Points += 1
else:
    print("Sorry, it's incorrect")
    
Q2 = int(input("4 + 7 * (3 - 11) * 2 = "))
if Q2 == -108:
    print("Correct!")
    Points += 1
else:
    print("Sorry, it's incorrect")


Q3 = int(input("(4 + 7) * 3 - 11 * 2 = "))
if Q3 == 11:
    print("Correct!")
    Points += 1
else:
    print("Sorry, it's incorrect")


print("You got " + str(Points) + " points.")
