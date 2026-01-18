def dessiner_soleil(position, taille, t):
    t.up()
    t.goto(position[0], position[1] - taille)  
    t.down()
    t.color("gold")
    t.begin_fill()
    t.circle(taille)
    t.end_fill()

    for i in range(12):
        t.up()
        t.goto(position[0], position[1]) 
        t.left(30)  
        t.forward(taille)  
        t.down()
        t.forward(taille * 0.6)