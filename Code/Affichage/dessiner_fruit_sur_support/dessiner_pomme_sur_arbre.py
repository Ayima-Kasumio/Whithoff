"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from math import*
from random import *
from Code.Affichage.procedure_pomme.dessiner_pomme import*

def dessiner_pomme_sur_arbre(nb, position, taille_pomme, taille_arbre):
    liste_pomme = []
    center_x = position[0]
    center_y = position[1] + 6* taille_arbre
    R = 1.8* taille_arbre

    for _ in range(nb):
        t = Turtle()
        t.up()
        t.hideturtle()
        t.speed()

        fruit_positionne = False
        while not fruit_positionne:

            fruit_positionne = True

            theta = uniform(0, 2*pi)
            r = R * sqrt(random())
            x = int(center_x + r*cos(theta))
            y = int(center_y + r*sin(theta))

            for i in liste_pomme:
                if ((x-i[0][0])**2+(y-i[0][1])**2)**(0.5) < 4*taille_pomme:
                    fruit_positionne = False
        

        dessiner_pomme((x, y-taille_pomme), taille_pomme, t)
        liste_pomme.append([(x, y),t, "Pas mangé", taille_pomme])
        

    return liste_pomme