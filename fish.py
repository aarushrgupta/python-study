from turtle import *
bgcolor("blue")
x = 10
y = 20

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
    y = y + 70 
    



