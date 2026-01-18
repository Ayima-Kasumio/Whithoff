"""
Binome :
Megemont Aymeric
Sarfati Enzo
"""

from Code.Affichage.procedure_fond_ecran.procedure_arbre.dessiner_arbre import *
from Code.Affichage.procedure_fond_ecran.procedure_table.dessiner_table import *

from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_herbe import*
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_nuage import*
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_soleil import*
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_scoreboard import*

from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_montagne import *
from Code.Affichage.procedure_fond_ecran.procedure_background.dessiner_fleur import *

from random import*

def dessiner_fond(t, screen,nb_arbre, nb_table, taille_arbre, taille_table):
    screen.bgcolor("Sky Blue")
    
    dessiner_herbe(t, -100)
    dessiner_soleil((750, 400), 50, t)

    for i in range(11):
        dessiner_montagne((-866+i*192, -100), 192, randint(250,350), t)
        dessiner_montagne((-960+i*192,-100), 192, randint(350,550), t)

        dessiner_nuage((randint(-960, 960), randint(100, 450)), 30, t)



    

    for i in range(nb_arbre):
        dessiner_arbre((-550+i*1100//(nb_arbre-1), -100), taille_arbre, t)

    for i in range(20):
        dessiner_fleur((randint(-960, 960), randint(-500, -100)), 30,(randint(0,255), randint(0,255), randint(0,255)),  t)


    dessiner_scoreboard(t)

    for i in range(nb_table):
        dessiner_table((-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_table,t)