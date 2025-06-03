from random import *
Colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
Animals = ["ostrich", "raccoon", "lionfish", "slug", "bison", "rhino"]

for i in range(6):
    num = randrange(len(Colors))
    num2 = randrange(len(Animals))
    print(Colors[num] + " " + Animals[num2])
    Colors.pop(num)
    Animals.pop(num2)
print(Colors)
print(Animals)
