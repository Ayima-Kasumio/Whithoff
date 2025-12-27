from Code.Affichage.procedure_fond_ecran.procedure_arbre.dessiner_arbre import *
from Code.Affichage.procedure_fond_ecran.procedure_table.dessiner_table import *

from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_herbe import*
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_nuage import*
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_soleil import*

def dessiner_fond(t, screen,nb_arbre, nb_table, taille_arbre, taille_table):
    screen.bgcolor("Sky Blue")
    t.speed(0)
    
    dessiner_herbe(t, -100)
    dessiner_soleil((750, 400), 50, t)
    dessiner_nuage((-600, 200), 30, t)
    dessiner_nuage((-100, 300), 25, t)
    dessiner_nuage((300, 200), 35, t)
    

    for i in range(nb_arbre):
        dessiner_arbre((-550+i*1100//(nb_arbre-1), -100), taille_arbre, t)

    for i in range(nb_table):
        dessiner_table((-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_table,t)
