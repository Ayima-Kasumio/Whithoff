"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from random import*
from turtle import*
from Code.Affichage.procedure_raisin.dessiner_raisin import*

def dessiner_raisin_sur_table(nb, position, taille_raisin, taille_table):
    liste_raisin = []
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

            for i in liste_raisin:
                if ((x-i[0][0])**2+(y-i[0][1])**2)**(0.5) < 4*taille_raisin:
                    fruit_positionne = False

        dessiner_raisin((x, y-taille_raisin), taille_raisin, t)
        liste_raisin.append([(x, y),t, "Pas mangé", taille_raisin])

    return liste_raisin