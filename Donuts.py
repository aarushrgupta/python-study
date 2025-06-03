print("Here is the menu we have for our donuts!")
Donuts = {"Glazed": 2.45, "Long John": 4.00, "Jelly": 5.00}
Price = Donuts["Glazed"]
Donuts["Long John"] = 7.00
print(Donuts)

for Donut in Donuts:
    print("****************************")
    print("Donut: " + Donut)
    Donut_price = Donuts[Donut]
    print("Price: " + str(Donut_price))
    print("****************************")
