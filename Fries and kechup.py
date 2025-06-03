restraunt_ketchup_inventory = 10
print("Are you hungry? Here are some fries!")
customer_ketchup_order = int(input("How many ketchup packets do you want with your fries?: "))

if customer_ketchup_order <= restraunt_ketchup_inventory:
    print("Great! Here are your packets of ketchup.")
elif customer_ketchup_order > restraunt_ketchup_inventory:
    print("Sorry, We don't have tyhat much of ketchup.")
else:
    print("you must pick a number!")
