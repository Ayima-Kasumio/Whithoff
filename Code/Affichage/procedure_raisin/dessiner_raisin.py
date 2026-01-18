from turtle import *
from Code.Affichage.dessiner_feuille import *
from Code.Affichage.dessiner_tige import *
from Code.Affichage.dessiner_grain_fruit import *

def dessiner_raisin(position, taille, t):
    taille_raisin = taille//2.5
    
    dessiner_grain_fruit(position, taille_raisin, t, "purple")
    dessiner_grain_fruit((position[0]-taille_raisin,position[1]+3*taille//5), taille_raisin, t, "purple")
    dessiner_grain_fruit((position[0]+taille_raisin,position[1]+3*taille//5), taille_raisin, t, "purple")
    dessiner_grain_fruit((position[0]-2*taille_raisin,position[1]+6*taille//5), taille_raisin, t, "purple")
    dessiner_grain_fruit((position[0],position[1]+6*taille//5), taille_raisin, t, "purple")
    dessiner_grain_fruit((position[0]+2*taille_raisin,position[1]+6*taille//5), taille_raisin, t, "purple")

    dessiner_tige((position[0], position[1] + 2*taille), taille, t)
    dessiner_feuille((position[0], position[1] + 2.5*taille), taille, "#09a809", t)