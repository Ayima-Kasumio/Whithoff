from turtle import*
from numpy import *

def dessiner_feuille(position, taille):
    up()
    goto(position[0]-taille/10, position[1] + 2*taille)
    down()
    color("green")
    begin_fill()
    left(135)
    circle(2.5*taille, 40)
    left(140)
    circle(2.5*taille, 40)
    end_fill()

def dessiner_base_feuille(position, taille):
    up()
    goto(position[0], position[1] + 3*taille/2)
    down()
    color("brown")
    begin_fill()
    left(90)
    forward(taille)
    left(90)
    forward(taille/10)
    left(90)
    forward(taille)
    left(90)
    forward(taille/10)
    end_fill()


def dessiner_pomme(position, taille):
    up()
    goto(position)
    down()
    color("red")
    begin_fill()
    circle(taille)
    end_fill()

    dessiner_base_feuille(position, taille)
    dessiner_feuille(position, taille)

    setheading(0)
    
def dessiner_pomme_mangee(position, taille):
    color("red")
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


speed(0)
hideturtle()

taille = 100

dessiner_pomme((-300,0), taille)

dessiner_pomme_mangee((0,0), taille)

done()

"""




    goto(position[0]-taille/2, position[1]+taille/10)

    setheading(180)
    
    goto(position[0]+taille/2, position[1]+18*taille/10)
    right(30)
    circle(taille, 60)
    
    goto(position[0]+taille/2, position[1]+18*taille/10 )
    circle(2*taille, 120 )"""