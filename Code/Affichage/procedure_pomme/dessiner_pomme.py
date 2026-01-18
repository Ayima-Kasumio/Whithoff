from turtle import *
from Code.Affichage.dessiner_feuille import *
from Code.Affichage.dessiner_tige import *
from Code.Affichage.dessiner_grain_fruit import *


def dessiner_pomme(position, taille, t):
    
    dessiner_grain_fruit(position, taille, t, "red")
    dessiner_tige((position[0], position[1] + 2*taille), taille, t)
    dessiner_feuille((position[0], position[1] + 2.5*taille), taille, "#09a809", t)