from turtle import *

def dessiner_pasteque_mangee(position, taille, t):
    taille *=2
    t.up()
    t.goto(position[0]-taille, position[1]+taille)
    t.down()
    t.right(90)
    t.color("black", "green")
    t.begin_fill()

    t.circle(taille, 180)
    t.left(90)
    t.forward(1.5*taille//8)
    t.right(90)
    t.circle(6.5*taille//8, -180)
    t.right(90)
    t.forward(1.5*taille//8)
    t.left(90)

    t.end_fill()



    t.goto(position[0]-6.5*taille//8, position[1]+taille)
    t.color("black", "red")

    t.begin_fill()
    t.circle(6.5*taille//8, 180)
    t.left(90)
    t.forward(3*taille//18)
    t.right(90)
    for i in range(3):
        t.circle(taille//4.5, -180)
        t.left(180)
    t.left(90)

    t.forward(3*taille//18)


    t.end_fill()

    t.right(180)
    t.color("black")
    
    for i in range(7):
        t.right(180//8)
        t.up()
        t.goto(position[0], position[1]+taille)
        t.forward(2*taille//3)
        t.down()
        t.forward(taille//10)
    
    t.setheading(0)