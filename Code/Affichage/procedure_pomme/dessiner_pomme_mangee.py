from turtle import *
from Code.Affichage.dessiner_feuille import *
from Code.Affichage.dessiner_tige import *


def dessiner_pomme_mangee(position, taille,t):
    t.clear()
    
    t.color("black", "red")
    t.begin_fill()

    t.up()
    t.goto(position[0]-taille/2, position[1]+taille/10)
    t.down()
    t.left(60)
    for i in range(2):
        t.right(90)
        t.circle(9*taille/10, 60)

        t.right(90)
        t.circle(9*taille/5, -60)

    t.end_fill()

    t.setheading(0)

    dessiner_tige((position[0], position[1] + 2*taille), taille, t)
    dessiner_feuille((position[0], position[1] + 2.5*taille), taille, "#09a809",t)