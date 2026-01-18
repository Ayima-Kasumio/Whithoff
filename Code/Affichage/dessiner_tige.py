from turtle import *

def dessiner_tige(position, taille, t):
    t.up()
    t.goto(position)
    t.down()
    t.color("brown")
    t.pensize(taille//12)
    t.left(70)
    t.circle(taille, 50)
    t.pensize(1)