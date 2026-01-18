#from turtle import*

def dessiner_grain_fruit(position, taille, t, color):
    t.up()
    t.goto(position)
    t.down()

    t.color("black", color)

    t.begin_fill()
    t.circle(taille)
    t.end_fill()

    t.up()
    t.goto(position[0]-taille//3, position[1] + 5*taille//4)
    t.down()
    t.color("white")
    t.begin_fill()
    t.circle(taille//6)
    t.end_fill()