def dessiner_feuillage(position, taille, t):
    t.up()
    t.goto(position)
    t.down()

    t.color("Forest Green")
    t.begin_fill()

    t.circle(2*taille)
    t.end_fill()