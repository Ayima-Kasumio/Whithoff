from turtle import *
tc = Screen()
tg = Turtle()

def dessiner_grain_raisin(t, position, taille):
    t.up()
    t.goto(position)
    t.down()

    
    t.color("black", "purple")

    t.begin_fill()
    t.circle(taille)
    t.end_fill()

    t.up()
    t.goto(position[0]-taille//3, position[1] + 5*taille//4)
    t.down()
    t.color("white")
    t.begin_fill()
    t.circle(taille//6)
    t.end_fill()

    t.setheading(0)

def dessiner_axe():
    write("(0,0)")
    for i in range(4):
        up()
        goto(0,0)
        down()
        forward(500)
        left(90)
    
    up()
    goto(0,200)
    down()
    write("(0,200)")

def fxn(x, y):
    if ((x**2+(100-y)**2)**(0.5)< 100):
        dessiner_grain_raisin(tg, (300,300), 40)


speed()
#dessiner_axe()
#dessiner_grain_raisin(tg, (0,0), 100)
tc.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

tc.onclick(fxn)
done()