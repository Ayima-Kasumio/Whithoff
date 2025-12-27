from turtle import *

def dessiner_base_feuille(position, taille, t):
    t.up()
    t.goto(position[0], position[1] + 2*taille)
    t.down()
    t.speed(0)
    t.color("brown")
    t.pensize(taille//12)
    t.left(70)
    t.circle(taille, 50)
    t.pensize(1)