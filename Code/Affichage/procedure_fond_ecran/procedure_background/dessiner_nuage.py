from Code.Affichage.dessiner_cercle import *

def dessiner_nuage(position, taille, t):
    for i in range(3):
        dessiner_cercle((position[0] + i * taille * 0.8, position[1]), taille,"white" ,t)
        dessiner_cercle((position[0] +taille*0.8 + i * taille * 0.8, position[1]+taille*0.8), taille, "white", t)

    dessiner_cercle((position[0] + taille*2.4, position[1]), taille,"white" ,t)
    dessiner_cercle((position[0] + taille*3.2, position[1]), taille,"white" ,t)