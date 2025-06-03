parts = ["butter","apple","mayo","pickles","jelly","bananas","lettuce"]


my_sandwich = []

for item in parts:
    ask = input("Do you want " + item + "? ")
    if ask == "yes":
        my_sandwich.append(item)
        else:print("please chose yes or no")
        
print("Your sandwich will have:")    
print(my_sandwich)
