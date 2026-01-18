from turtle import *

def dessiner_feuille(position, taille, color,t):
    t.up()
    t.goto(position)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(5*taille//3, 40)
    t.left(140)
    t.circle(5*taille//3, 40)
    t.end_fill()

    t.setheading(0)