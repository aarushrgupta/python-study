Salad = ["spinach", "tomatoes", "carrots", "olives", "ranch"]
Size = input("Hi! Please type a size of salad you want!:  ")


if Size == "small":
        print("Your salad has " + Salad[0] + ", " + Salad[1] + " and " + Salad[4] + "!")
elif Size == "medium":
        print("Your salad has " + Salad[0] + ", " + Salad[1] + ", " + Salad[2] + " and " + Salad[4] + "!")
elif Size == "large":
        print("Your salad has " + Salad[0] + ", " + Salad[1] + ", " + Salad[2] + ", " + Salad[3] + " and " + Salad[4] + "!")
else:
    print("You must pick a size of salad!")
