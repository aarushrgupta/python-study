def greeting(name,age):
    print("Hello " + name)

    if age > 18:
        print("You are an adult")
    elif age == 18:
        print("You are a teenager")
    elif age < 18:
        print("You are a kid")


greeting("Aarush",18)
