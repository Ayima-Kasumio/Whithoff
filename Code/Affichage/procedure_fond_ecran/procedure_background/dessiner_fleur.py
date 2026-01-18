"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from Code.Affichage.dessiner_tige import*
from math import *

def dessiner_fleur(position, taille, color, t):
    colormode(255)
    dessiner_tige(position, taille, t)
    t.setheading(0)

    position_centre_petale = (position[0], position[1]+2*taille*sin(25*pi/180)) # reliation trouvé sur internet, la hauteur d'un arc de cercle est égale à 2*R*sin(teta/2) avec teta l'angle entre les deux points et l'origine, ici 50° car la tige est un arc de cercle de 50°

    t.color(color)

    for angle in range(0,360,60):
        t.up()
        t.goto(position_centre_petale[0]+2*taille*cos(angle*pi/180)//9, position_centre_petale[1]+2*taille*sin(angle*pi/180)//9 )
        t.down()
        t.begin_fill()
        t.circle(2*taille//9)
        t.end_fill()


    colormode(1)
    t.up()
    t.goto(position_centre_petale)
    t.color("#FFD700")
    t.down()
    t.begin_fill()
    t.circle(5*taille//24)
    t.end_fill()