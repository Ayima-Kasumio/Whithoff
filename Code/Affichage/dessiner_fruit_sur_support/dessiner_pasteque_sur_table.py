from random import*
from turtle import*
from Code.Affichage.procedure_pasteque.dessiner_pasteque import*

def dessiner_pasteque_sur_table(nb, position, taille_pasteque, taille_table):
    liste_pasteque = []
    center_x = position[0]
    center_y = position[1] + 19*taille_table//20

    """
    3*taille/5 -taille/10 = 5*taille/10 = taille/2                  # hauteur plateau sans rebord
    6*taille/5-taille/4 = 24*taille/20 -5*taille/20 =19*taille/20
    """

    for _ in range(nb):
        t = Turtle()
        t.up()
        t.hideturtle()
        t.speed()
        x = y = 0

        fruit_positionne = False
        while not fruit_positionne:
            fruit_positionne = True

            
            x = center_x + randint(-4*taille_table//5,4*taille_table//5) *0.9
            y = center_y + randint(-taille_table//4, taille_table//4) *0.9

            for i in liste_pasteque:
                if ((x-i[0][0])**2+(y-i[0][1])**2)**(0.5) < 4*taille_pasteque:
                    fruit_positionne = False

        dessiner_pasteque((x, y-taille_pasteque), taille_pasteque, t)
        liste_pasteque.append([(x, y),t, "Pas mangé"])

    return liste_pasteque