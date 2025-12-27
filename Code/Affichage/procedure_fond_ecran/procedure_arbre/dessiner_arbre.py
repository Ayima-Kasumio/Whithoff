from Code.Affichage.procedure_fond_ecran.procedure_arbre.dessiner_feuillage import*
from Code.Affichage.procedure_fond_ecran.procedure_arbre.dessiner_tronc import*


def dessiner_arbre(position, taille, t):
    x = position[0]
    y = position[1]
    
    dessiner_tronc((x,y), taille, t)
    dessiner_feuillage((x, y+4*taille), taille, t)