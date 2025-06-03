animals  = {
    "cow": "moo!",
    "pig": "oink!",
    "horse": "neigh!",
    "chicken": "cluck!"}

choice = input ("Choose an animal: ")
if choice in animals:
    print(animals[choice] + " " + animals[choice])
else:
    print("E-I-E-I-O!")
