from Code.Affichage.dessiner_triangle_isocele import *

def dessiner_montagne(position, largeur, hauteur, t):
    dessiner_triangle_isocele(position, largeur, hauteur, "brown", t)
    dessiner_triangle_isocele((position[0], position[1]+4*hauteur//5), largeur//5, hauteur//5, "white", t)