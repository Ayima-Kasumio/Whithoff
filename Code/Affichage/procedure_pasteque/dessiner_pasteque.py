from turtle import *

def dessiner_pasteque(position, taille,t):
    taille *=2
    t.up()
    t.goto(position[0]-taille, position[1]+taille)
    t.down()
    t.right(90)
    t.color("black", "green")
    t.begin_fill()
    t.circle(taille, 180)

    t.goto(position[0]-taille, position[1]+taille)
    t.end_fill()

    t.goto(position[0]-6.5*taille//8, position[1]+taille)
    t.left(180)
    t.color("black", "red")

    t.begin_fill()
    t.circle(6.5*taille//8, 180)
    t.goto(position[0]-6.5*taille//8, position[1]+taille)
    t.end_fill()

    t.right(90)
    t.color("black")
    
    for i in range(7):
        t.right(180//8)
        t.up()
        t.goto(position[0], position[1]+taille)
        t.forward(taille//2)
        t.down()
        t.forward(taille//5)
    
    t.setheading(0)