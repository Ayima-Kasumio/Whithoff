def dessiner_triangle_isocele(position, longeur, hauteur, color, t):
    t.up()
    t.goto(position[0]-longeur//2,position[1])
    t.down()

    t.color("black", color)

    t.begin_fill()

    t.goto(position[0]+longeur//2,position[1])
    t.goto(position[0],position[1]+hauteur)
    t.goto(position[0]-longeur//2,position[1])

    t.end_fill()    