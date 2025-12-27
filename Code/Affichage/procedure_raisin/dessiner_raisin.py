from turtle import *
from Code.Affichage.dessiner_feuille import *
from Code.Affichage.dessiner_base_feuille import *
from Code.Affichage.procedure_raisin.dessiner_grain_raisin import *

def dessiner_raisin(position, taille, t):
    taille_raisin = taille//2.5
    
    dessiner_grain_raisin(position, taille_raisin, t)
    dessiner_grain_raisin((position[0]-taille_raisin,position[1]+3*taille//5), taille_raisin, t)
    dessiner_grain_raisin((position[0]+taille_raisin,position[1]+3*taille//5), taille_raisin, t)
    dessiner_grain_raisin((position[0]-2*taille_raisin,position[1]+6*taille//5), taille_raisin, t)
    dessiner_grain_raisin((position[0],position[1]+6*taille//5), taille_raisin, t)
    dessiner_grain_raisin((position[0]+2*taille_raisin,position[1]+6*taille//5), taille_raisin, t)

    dessiner_base_feuille(position, taille, t)
    dessiner_feuille(position, taille, t)

    t.setheading(0)