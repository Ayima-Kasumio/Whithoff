from turtle import *

def dessiner_feuille(position, taille,t):
    t.up()
    t.goto(position[0], position[1] + 2.5*taille)
    t.down()
    t.speed(0)
    t.color("green")
    t.begin_fill()
    t.circle(5*taille//3, 40)
    t.left(140)
    t.circle(5*taille//3, 40)
    t.end_fill()