from math import*

def dessiner_plateau(position, taille, t):
    t.up()
    t.goto(position[0]-taille, position[1])
    t.down()
    t.color("black", "#8b4513")
    t.begin_fill()
    for i in range(2):
        t.forward(2*taille)
        t.left(90)
        t.forward(taille//10)
        t.left(90)
    t.end_fill()

    
    teta = 20 #degre
    cote_adjacent = taille//10
    hypotenus = cote_adjacent/cos(teta)
    cote_oppose = sin(teta)*hypotenus

    
    t.begin_fill()

    t.up()
    t.goto(position[0]-taille, position[1]+taille//10)
    t.down()


    """
    t.left(90-teta)
    t.forward(hypotenus)
    t.right(90-teta)
    t.forward(2*(taille-cote_oppose))
    t.right(90-teta)
    t.forward(hypotenus)
    t.right(90+teta)
    t.forward(2*taille)
    t.left(180)
    """

    t.goto(position[0]-taille+cote_oppose, position[1]+3*taille//5)
    t.goto(position[0]+taille-cote_oppose, position[1]+3*taille//5)
    t.goto(position[0]+taille, position[1]+taille//10)
    t.goto(position[0]-taille, position[1]+taille//10)
    

    t.end_fill()