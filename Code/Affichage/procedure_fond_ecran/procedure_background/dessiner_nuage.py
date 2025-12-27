def dessiner_nuage(position, taille, t):
    t.color("white")
    for i in range(4):
        t.up()
        t.goto(position[0] + i * taille * 0.8, position[1])
        t.down()
        t.begin_fill()
        t.circle(taille)
        t.end_fill()