from turtle import *
from random import *
from math import *
from Code.Affichage.fonction_affichage import *
from Code.game.fonction_game import*


""" 
position debut feuillage = (position[0]+taille_arbre/2, position[1]+4*taille_arbre)
equation du cercle du feuillage : (x-x0)² +(y-y0)² < 2*taille_arbre

(x-x0)² +(y-y0)² < 2*taille
(x-x0)² < 2*taille - (y-y0)²
x-x0 =
x0 - sqrt(2*taille - (y-y0)²) < x < x0 + sqrt(2*taille - (y-y0)²)
"""

def fxn(x, y):
    global liste_tortue_raisin
    global liste_tortue_pasteque

    for i in liste_tortue_raisin:
        if ((x-i[0][0])**2 + (y-i[0][1])**2)**0.5 < taille_raisin:
            i[1].clear()
            dessiner_raisin_mangee((i[0][0], i[0][1]-taille_raisin), taille_raisin, i[1])
            break

    for i in liste_tortue_pasteque:
        if ( ((x-i[0][0])**2 + (y-i[0][1])**2)**0.5 < taille_pasteque and y<i[0][1]):
            i[1].clear()
            dessiner_pasteque_mangee((i[0][0], i[0][1]-taille_pasteque), taille_pasteque, i[1])
            break




t_background = Turtle()
t_background.speed()
t_background.hideturtle()
screen = Screen()



nb_raisin = 0#randint(15,30)
nb_pasteque = randint(15,25)

nb_arbre = 4
nb_table = 3

taille_arbre = 72
taille_table = 750//nb_table # largeur de la table = 2*taille_table

taille_raisin = 12 #taille_arbre//6 72/6 = 12
taille_pasteque = taille_table//14

liste_tortue_raisin, liste_tortue_pasteque = initialisation(t_background, screen, nb_raisin, nb_pasteque, nb_arbre, nb_table, taille_arbre, taille_table, taille_raisin, taille_pasteque)

screen.onclick(fxn)


done()


