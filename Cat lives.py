Cat_lives = 9
print("Everyone knows that cats have " + str(Cat_lives) + " lives.")
Cats = int(input("How many cats are there?"))

Lives = Cats * 9
print("Ther are " + str(Lives) + " lives total")

Cats = Lives / 9
print("There are " + str(Cats) + " cats here")

Vacation = int(input("How many cats went on vacation?"))
Left = Cats - Vacation
print("There are " + str(Left) + " cats left home")
