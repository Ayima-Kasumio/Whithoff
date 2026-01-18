"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from math import*
from random import *
from Code.Affichage.dessiner_feuille import*

def dessiner_feuillage(position, taille, t):
    t.up()
    t.goto(position)
    t.down()

    t.color("Forest Green")
    t.begin_fill()
    t.circle(2*taille)
    t.end_fill()

    liste_feuille = []
    taille_feuille = 15
    R = 1.8* taille

    for _ in range(4):
        x = y = 0

        fruit_positionne = False
        while not fruit_positionne:
            fruit_positionne = True

            theta = uniform(0, 2*pi)
            r = R * sqrt(random())
            x = int(position[0] + r*cos(theta))
            y = int(position[1] + 2*taille + r*sin(theta))

            for i in liste_feuille:
                if ((x-i[0])**2+(y-i[1])**2)**(0.5) < 4*taille_feuille:
                    fruit_positionne = False

        dessiner_feuille((x, y-taille_feuille), taille_feuille,"#047A0A",  t)
        liste_feuille.append((x, y))

    