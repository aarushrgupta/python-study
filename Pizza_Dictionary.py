Pizza = {
    'Crust': 'Thick',
    'Sauce': 'Tomato',
    'Toppings': ['Cheese,', 'Mushrooms,', 'and', 'Onions'],
    }
print(f"You have ordered a {Pizza['Crust']}-crust pizza, with {Pizza['Sauce']} sauce "
      "and with the following toppings include:")

for Topping in Pizza['Toppings']:
    print(f"\t{Topping}")
