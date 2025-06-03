def make_chocolate():
    ingredients = ["sugar","milk","butter","bean extract"]
    print("Gather cocoa beans. Roast them and get extract.")
    mix = "mix ingredients: "
    print(" Value of mix : " + mix)
    for i in ingredients:
        print("ingredient = " + i)
        mix = mix + i + ", "
        print(mix)
        print("then bake for an hour")
        print("#####################")


make_chocolate()        

