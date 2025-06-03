shopping = ['milk' , 'eggs' , 'butter' , 'waffles' , 'syrup' ]
shopping[3] = "flour"
shopping.pop(0)
print(shopping)


while len(shopping) < 7: 
    item_to_add = input("what else do you need?")
    shopping.append(item_to_add)
    print(shopping)
print("time to go shopping!")

   
