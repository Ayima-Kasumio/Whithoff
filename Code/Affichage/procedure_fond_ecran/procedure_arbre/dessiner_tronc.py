"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

def dessiner_tronc(position, taille, t):
    t.up()
    t.goto(position[0]-taille//2, position[1])
    t.down()

    t.color("#8B5A2B")
    t.begin_fill()
    for i in range(2):
        t.forward(taille)
        t.left(90)
        t.forward(4*taille)
        t.left(90)
    t.end_fill()