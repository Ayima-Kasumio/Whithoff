def dessiner_cercle(position, taille , color, t):
        t.up()
        t.goto(position)
        t.color(color)
        t.down()
        t.begin_fill()
        t.circle(taille)
        t.end_fill()