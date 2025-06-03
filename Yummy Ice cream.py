def make_icecream(flavor,amount):
    print(amount)
    if flavor == "Vanilla":
          print("Vanilla is yummy")
    elif flavor == "Chocolate":
          print("Chocolate is great!")
    else:
          print(flavor + " is great too!")
          print("1cecreams are tasty " + (str(amount)))

make_icecream("Chocolate", 100)
