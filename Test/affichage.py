from turtle import*
from numpy import *

def dessiner_feuille(position, taille):
    up()
    goto(position[0], position[1] + 2.5*taille)
    down()
    color("green")
    begin_fill()
    circle(5*taille//3, 40)
    left(140)
    circle(5*taille//3, 40)
    end_fill()

def dessiner_base_feuille(position, taille):
    up()
    goto(position[0], position[1] + 2*taille)
    down()
    color("brown")
    
    left(70)
    circle(taille, 50)

def dessiner_pomme(position, taille):
    up()
    goto(position)
    down()
    color("black", "red")
    
    begin_fill()
    circle(taille)
    end_fill()

    dessiner_base_feuille(position, taille)
    dessiner_feuille(position, taille)

    setheading(0)
    
def dessiner_pomme_mangee(position, taille):
    color("red", "black")
    begin_fill()

    up()
    goto(position[0]-taille/2, position[1]+taille/10)
    down()
    left(60)
    for i in range(2):
        right(90)
        circle(9*taille/10, 60)

        right(90)
        circle(9*taille/5, -60)

    end_fill()

    setheading(0)

    dessiner_base_feuille(position, taille)
    dessiner_feuille(position, taille)

    setheading(0)

def dessiner_grain_raisin(position, taille):
    up()
    goto(position)
    down()

    
    color("black", "purple")

    begin_fill()
    circle(taille)
    end_fill()

    up()
    goto(position[0]-taille//3, position[1] + 5*taille//4)
    down()
    color("white")
    begin_fill()
    circle(taille//6)
    end_fill()

def dessiner_raisin(position, taille):
    taille_raisin = taille//2.5
    up()
    goto(position)
    down()
    
    dessiner_grain_raisin(position, taille_raisin)
    dessiner_grain_raisin((position[0]-taille_raisin,position[1]+3*taille//5), taille_raisin)
    dessiner_grain_raisin((position[0]+taille_raisin,position[1]+3*taille//5), taille_raisin)
    dessiner_grain_raisin((position[0]-2*taille_raisin,position[1]+6*taille//5), taille_raisin)
    dessiner_grain_raisin((position[0],position[1]+6*taille//5), taille_raisin)
    dessiner_grain_raisin((position[0]+2*taille_raisin,position[1]+6*taille//5), taille_raisin)

    dessiner_base_feuille(position, taille)
    dessiner_feuille(position, taille)

    setheading(0)

def dessiner_raisin_mangee(position, taille):
    taille_raisin = taille//2.5
    up()
    goto(position)
    down()
    
    dessiner_grain_raisin(position, taille_raisin)
    dessiner_grain_raisin((position[0]+taille_raisin,position[1]+3*taille//5), taille_raisin)
    dessiner_grain_raisin((position[0],position[1]+6*taille//5), taille_raisin)

    dessiner_base_feuille(position, taille)
    dessiner_feuille(position, taille)

    setheading(0)

def dessiner_pasteque(position, taille):
    taille *=2
    up()
    goto(position[0]-taille, position[1]+taille)
    down()
    right(90)
    color("black", "green")
    begin_fill()
    circle(taille, 180)

    goto(position[0]-taille, position[1]+taille)
    end_fill()

    goto(position[0]-6.5*taille//8, position[1]+taille)
    left(180)
    color("black", "red")

    begin_fill()
    circle(6.5*taille//8, 180)
    goto(position[0]-6.5*taille//8, position[1]+taille)
    end_fill()

    right(90)
    color("black")
    
    for i in range(7):
        right(180//8)
        up()
        goto(position[0], position[1]+taille)
        forward(taille//2)
        down()
        forward(taille//5)
    
    setheading(0)
    
def dessiner_pasteque_mangee(position, taille):
    taille *=2
    up()
    goto(position[0]-taille, position[1]+taille)
    down()
    right(90)
    color("black", "green")
    begin_fill()

    circle(taille, 180)
    left(90)
    forward(1.5*taille//8)
    right(90)
    circle(6.5*taille//8, -180)
    right(90)
    forward(1.5*taille//8)
    left(90)

    end_fill()



    goto(position[0]-6.5*taille//8, position[1]+taille)
    color("black", "red")

    begin_fill()
    circle(6.5*taille//8, 180)
    left(90)
    forward(3*taille//18)
    right(90)
    for i in range(3):
        circle(taille//4.5, -180)
        left(180)
    left(90)

    forward(3*taille//18)


    end_fill()

    right(180)
    color("black")
    
    for i in range(7):
        right(180//8)
        up()
        goto(position[0], position[1]+taille)
        forward(2*taille//3)
        down()
        forward(taille//10)
    
    setheading(0)
