from turtle import *
from time import *
setup(700, 700)

bgcolor("gray")
tracer(0)
ht()

ypos = 0
spin = 0

for frame in range(180):
    clear()
    
    # Tree
    # Draw a line
    color("dark goldenrod")
    pensize(20)
    pu()
    goto(-100, -200)
    pd()
    seth(90)
    fd(150)
    lt(45)
    # branches and twigs
    for branch in range(4):
        pensize(15)
        fd(75)
        lt(45)
        pensize(10)
        for twig in range(4):
            fd(50)
            bk(50)
            rt(30)
        lt(75)
        bk(75)
        rt(30)

    # Snowy ground
    pu()
    goto(-350, -350)
    pd()
    color("white")
    pensize(300)
    seth(0)
    fd(700)

    # Snow
    def flake(x, y):
        pensize(1)
        pu()
        pensize(1)
        pu()
        goto(x, y)
        pd()
        for snowflake in range(4):
            fd(30)
            bk(30)
            rt(90)
        lt(45)
        for snowflake in range(4):
            fd(30)
            bk(30)
            rt(90)

    seth(spin)       
    flake(250, 50 + ypos)
    flake(-20, 100 + ypos)
    flake(-200, 200 + ypos)
    flake(-250, 250 + ypos)
    flake(200, 150 + ypos)
    flake(100, 300 + ypos)

    ypos -= 3
    spin += 7

    update()
    sleep(0.05)

    
# Color change
cur_sky_red = 0.5
cur_sky_green = 0.5
cur_sky_blue = 0.5
sky_red_change = (0.529 - 0.5) / 100
sky_green_change = (0.808 - 0.5) / 100
sky_blue_change = (0.922 - 0.5) / 100

cur_ground_red = 1
cur_ground_green = 1
cur_ground_blue = 1

ground_red_change = -1 / 100
ground_green_change = (0.392 - 1) / 100
ground_blue_change = -1 / 100


for frame in range(100):
    clear()
    
    #Tree
    # Draw a line
    color("dark goldenrod")
    pensize(20)
    pu()
    goto(-100, -200)
    pd()
    seth(90)
    fd(150)
    lt(45)
    for branch in range(4):
        pensize(15)
        fd(75)
        lt(45)
        pensize(10)
        for twig in range(4):
            fd(50)
            bk(50)
            rt(30)
        lt(75)
        bk(75)
        rt(30)

    # snowy ground
    pu()
    goto(-350, -350)
    pd()
    color(cur_ground_red, cur_ground_green, cur_ground_blue)
    pensize(300)
    seth(0)
    fd(700)

    update()
    bgcolor(cur_sky_red, cur_sky_green, cur_sky_blue)
    sleep(0.05)

    cur_sky_red += sky_red_change
    cur_sky_green += sky_green_change
    cur_sky_blue += sky_blue_change

    cur_ground_red += ground_red_change
    cur_ground_green += ground_green_change
    cur_ground_blue += ground_blue_change

# Green Tree

green_size = 1

 
for frame in range(100):
    clear()
    
    #Tree
    color("dark goldenrod")
    pensize(20)
    pu()
    goto(-100, -200)
    pd()
    seth(90)
    fd(150)
    lt(45)
    for branch in range(4):
        pensize(15)
        fd(75)
        lt(45)
        pensize(10)
        for twig in range(4):
            fd(50)
            
            lt(90)
            color("dark green")
            begin_fill()
            circle(green_size)
            end_fill
            rt(90)
            
            bk(50)
            rt(30)
        lt(75)
        bk(75)
        rt(30)



     # snowy ground
    pu()
    goto(-350, -350)
    pd()
    color(cur_ground_red, cur_ground_green, cur_ground_blue)
    pensize(300)
    seth(0)
    fd(700)


    update()
    sleep(0.05)
    green_size += 0.75

# Flower

stem = 1
blossom = 1
for frame in range(40):
    clear()
    
    #Tree
    color("dark goldenrod")
    pensize(20)
    pu()
    goto(-100, -200)
    pd()
    seth(90)
    fd(150)
    lt(45)
    for branch in range(4):
        pensize(15)
        fd(75)
        lt(45)
        pensize(10)
        for twig in range(4):
            fd(50)
            
            lt(90)
            color("dark green")
            begin_fill()
            circle(green_size)
            end_fill
            rt(90)
            
            bk(50)
            rt(30)
        lt(75)
        bk(75)
        rt(30)



     # snowy ground
    pu()
    goto(-350, -350)
    pd()
    color(cur_ground_red, cur_ground_green, cur_ground_blue)
    pensize(300)
    seth(0)
    fd(700)

    update()
    sleep(0.05)

    # Growing
    update()
    sleep(0.05)
    pu()
    goto(125, -300)
    pd()
    seth(90)
    pensize(12)
    color("green")
    
    if stem < 30:
        circle(-150, stem)
        stem += 1
    else:
        circle(-150, stem)
        pensize(2)
        color("orange", "purple")
        rt(blossom * 2)
        for petal in range(5):
            begin_fill()
            circle(blossom)
            end_fill()
            rt(72)
        bk(blossom / 3)
        rt(90)
        color("orange")
        begin_fill()
        circle(blossom / 3)
        end_fill()
        blossom += 2

        # sunshine
        xpos = -400

        for frame in range(100):
        clear()
        
        # sun
        color("yellow")
        pensize(1)
        pu()
        goto(xpos, 100)
        pd()
        seth(90)
        fd(150)
        lt(45)
        for branch in range(4):
            pensize(15)
            fd(75)
            lt(45)
            pensize(10)
            for twig in range(4):
                fd(50)
                
                lt(90)
                color("dark green")
                begin_fill()
                circle(green_size)
                end_fill
                rt(90)
                
                bk(50)
                rt(30)
            lt(75)
            bk(75)
            rt(30)



         # snowy ground
        pu()
        goto(-350, -350)
        pd()
        color(cur_ground_red, cur_ground_green, cur_ground_blue)
        pensize(300)
        seth(0)
        fd(700)

        update()
        sleep(0.05)

        
    
   










