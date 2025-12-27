from turtle import *

def dessiner_axe(t):
    t.write("(0,0)")
    for i in range(4):
        t.up()
        t.goto(0,0)
        t.down()
        t.forward(500)
        t.left(90)
    
    t.color("black")
    t.up()
    t.goto(-514,232)
    t.down()
    t.write("(-514,232)")

    t.up()
    t.goto(-514,88)
    t.down()
    t.write("(-514,88)")