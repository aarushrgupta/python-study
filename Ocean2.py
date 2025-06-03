from turtle import *
#bubble

setup(500, 500)

background = "Ocean3.gif"
bgpic(background)
penup()
goto(200, 10)
color("white")
pendown()
circle(50, 360)
penup()
left(105)
fd(60)
pendown()
circle(15, 360)
penup()
rt(40)
fd(10)
pendown()
circle(5, 360)
hideturtle()
from turtle import *
#starfish
setup(500, 500)
showturtle()
penup()
goto(10, 10)
setheading(0)
pendown()
color("brown")

begin_fill()

for i in range(5):
    fd(50)
    rt(144)
    fd(50)
    lt(72)

end_fill()    
#3 goldfish
x = 50
y = -100

for i in range(3):
    penup()
    goto(x, y)
    pendown()
    width(10)
    color("gold")
    setheading(45)
    fd(20)
    circle(-70, 90)
    rt(90)
    circle(-70, 90)
    fd(20)
    lt(135)
    fd(20)
    x = x + 50  
    y = y + -100
    

#bluefish
showturtle()
penup()
goto(-150, -150)
pendown()
color("blue")
setheading(135)
fd(60)
rt(90)
circle(-60, 135)
circle(30, -90)
lt(90)
fd(60)
rt(90)
circle(-30, 90)
circle(60, -135)
rt(90)
bk(60)

from turtle import *
#ocean_facts

ocean_facts = ["Over 70% of the Earth's surface is covered in water.",
               "The majority of creatures on Earth live in oceans.",
               "The largest animal to ever exist, the blue whale, lives in the ocean.",
               "Blue whales can live 80 - 90 years",
               "The deepest part of the ocean is the challenger deep."]

for fact in ocean_facts:
    print(fact)
#message
message = "My name is Aarush. \nMy picture is from pixy.org."
fact = ocean_facts[0]

color("yellow")
penup()
goto(-200, 200)
write(message, font = ("Arial", 18))
goto(-200, 175)
write(fact, font = ("Arial", 18))
hideturtle()

#jellyfish
showturtle()
penup()
goto(-200, 10)
pendown()
width(10)
setheading(90)
color("purple")
circle(60, 180)
lt(90)
for legs in range(6):
    fd(10)
    rt(110)
    fd(100)
    bk(100)
    lt(110)
    fd(10)
