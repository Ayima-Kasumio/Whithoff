from Code.Affichage.procedure_fond_ecran.procedure_table.dessiner_pied_de_table import*
from Code.Affichage.procedure_fond_ecran.procedure_table.dessiner_plateau import*


def dessiner_table(position, taille, t):
    dessiner_pied_de_table((position[0]-4*taille//5,position[1]), taille, t)
    dessiner_pied_de_table((position[0]+7*taille//10,position[1]), taille, t)

    dessiner_pied_de_table((position[0]-3*taille//5,position[1]+3*taille//10), taille, t)
    dessiner_pied_de_table((position[0]+taille//2,position[1]+3*taille//10), taille, t)          # + 5taille/10 -> taille/2

    dessiner_plateau((position[0], position[1]+3*taille//5) ,taille, t)
    
