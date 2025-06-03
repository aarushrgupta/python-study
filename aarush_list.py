toys = ["bear" ,"duck" ,"hippo"]
print(toys)
print(toys[2])
toys[2] = "lion"
print(toys)
toys.pop(2)
print(toys)
toys.append("rabbit")
print(toys)
toys[0] = "orange juice"
print(toys)
newtoy = input("enter your favorite toy")
print(newtoy)
toys.append(newtoy)
print(toys)
if len (toys) > 4:
    print("the list is not empty")
else:
    print("the list is empty")
