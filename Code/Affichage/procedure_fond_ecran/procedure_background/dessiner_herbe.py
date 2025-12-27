def dessiner_herbe(t, hauteur):
    t.up()
    t.goto(-960, hauteur)
    t.down()
    t.color("seagreen")
    t.begin_fill()
    for i in range(2):
        t.forward(1920)
        t.right(90)
        t.forward(540+hauteur)
        t.right(90)
    t.end_fill()