from random import *
def Superhero_name():

    Adjective = ["Intrepid", "Lightning", "Astonishing", "Ultra",
                 "Daring", "Bold", "Atomic", "Time", "Formless", "Rocket"]


    Hero = ["Storm", "Wasp", "Bunny", "Ranger", "Talon", "Beast",
            "Puppy", "Flame", "Wolf", "Python"]



    index1 = randrange(len(Adjective))
    index2 = randrange(len(Hero))

    adj = Adjective[index1]
    noun = Hero[index2]

    print("You are the " + adj + " " + noun + "!")


Superhero_name()
