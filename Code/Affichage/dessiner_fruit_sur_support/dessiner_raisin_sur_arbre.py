from math import*
from random import *
from turtle import*
from Code.Affichage.procedure_raisin.dessiner_raisin import*

def dessiner_raisin_sur_arbre(nb, position, taille_raisin, taille_arbre):
    liste_fruit = []
    center_x = position[0]
    center_y = position[1] + 6* taille_arbre
    R = 1.8* taille_arbre

    for _ in range(nb):
        t = Turtle()
        t.up()
        t.hideturtle()
        t.speed()
        x = y = 0

        fruit_positionne = False
        while not fruit_positionne:

            fruit_positionne = True

            theta = uniform(0, 2*pi)
            r = R * sqrt(random())
            x = int(center_x + r*cos(theta))
            y = int(center_y + r*sin(theta))

            for i in liste_fruit:
                if ((x-i[0][0])**2+(y-i[0][1])**2)**(0.5) < 4*taille_raisin:
                    fruit_positionne = False

        dessiner_raisin((x, y-taille_raisin), taille_raisin, t)
        liste_fruit.append([(x, y),t, "Pas mangé"])

    return liste_fruit