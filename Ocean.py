from turtle import *
bgcolor("blue")
penup()
goto(80, 80)
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
setup(500, 500)

background = "Ocean.gif"
bgpic(background)
showturtle()
penup()
goto(0, 0)
setheading(0)
pendown()
color("tan")

begin_fill()

for i in range(5):
    fd(50)
    rt(144)
    fd(50)
    lt(72)

end_fill()    
