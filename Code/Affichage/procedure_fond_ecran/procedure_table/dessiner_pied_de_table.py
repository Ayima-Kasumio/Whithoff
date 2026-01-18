def dessiner_pied_de_table(position, taille, t):
    t.up()
    t.goto(position)
    t.down()
    t.color("black", "#B5651D")
    t.begin_fill()

    for i in range(2):
        t.forward(taille//10)
        t.left(90)
        t.forward(3*taille//5)
        t.left(90)

    t.end_fill()