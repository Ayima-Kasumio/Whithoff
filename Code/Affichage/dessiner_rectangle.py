def dessiner_rectangle(position,longueur,largeur,color,t):
    t.up()
    t.goto(position)
    t.down()
    t.color("black", color)
    t.begin_fill()

    for i in range (2):
        t.forward(longueur)
        t.right(90)
        t.forward(largeur)
        t.right(90)
    
    t.end_fill()