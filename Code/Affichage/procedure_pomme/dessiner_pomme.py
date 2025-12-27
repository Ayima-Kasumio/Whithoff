from turtle import *
from Code.Affichage.dessiner_feuille import *
from Code.Affichage.dessiner_base_feuille import *


def dessiner_pomme(position, taille, t):
    t.up()
    t.goto(position)
    t.down()
    t.color("black", "red")
    
    t.begin_fill()
    t.circle(taille)
    t.end_fill()

    dessiner_base_feuille(position, taille, t)
    dessiner_feuille(position, taille, t)

    t.setheading(0)