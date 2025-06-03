color = ["black", "gold", "blue", "green"]

color.append("yellow")

for paint in color:
    print(paint)

    if paint == "green":
        print("I like green!")
    else:
        print("Other colors are also cool!")

print(len(color))

