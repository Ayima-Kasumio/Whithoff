from Code.Affichage.fonction_affichage import*
from random import*

def initialisation(t_background, t_ecriture,  screen, last_play):
    nb_pomme = randint(10,15)
    nb_pasteque = randint(10,15)
    nb_cerise = randint(10,15)
    nb_raisin = randint(10,15)

    # initialisation des variables de quantité d'élément initiale et en fonction de la partie

    nb_arbre = 4
    nb_table = 7

    taille_arbre = 72
    taille_table = 900//nb_table # largeur de la table = 2*taille_table

    taille_pomme = taille_table//13
    taille_pasteque = taille_table//16
    taille_cerise = taille_arbre//7
    taille_raisin = taille_arbre//7

    liste_objet_initiale = [[[],[],[],[]],[nb_pomme, nb_pasteque, nb_cerise, nb_raisin], ["pomme(s)", "pastèque(s)","cerise(s)", "raisin(s)"], [[dessiner_pomme, dessiner_pomme_mangee], [dessiner_pasteque, dessiner_pasteque_mangee], [dessiner_cerise, dessiner_cerise_mangee], [dessiner_raisin, dessiner_raisin_mangee]]]


    dessiner_fond(t_background, screen, nb_arbre, nb_table, taille_arbre, taille_table)

    affichage_information_game(t_ecriture, liste_objet_initiale, "Joueur n°1", last_play)

    nb_pomme_restant_a_dessiner = nb_pomme
    nb_pomme_par_arbre = nb_pomme//(nb_arbre//2) +1

    nb_pasteque_restant_a_dessiner = nb_pasteque
    nb_pasteque_par_table = nb_pasteque//(nb_table//2) +1

    nb_cerise_restant_a_dessiner = nb_cerise
    nb_cerise_par_arbre = nb_cerise//(nb_arbre - nb_arbre//2) +1        # pas factorisable car partie entiere de la division par 2

    nb_raisin_restant_a_dessiner = nb_raisin
    nb_raisin_par_arbre = nb_raisin//(nb_table - nb_table//2) +1

    

    for i in range(nb_arbre//2):
        if nb_pomme_restant_a_dessiner >= nb_pomme_par_arbre:
            liste_objet_initiale[0][0] += dessiner_pomme_sur_arbre(nb_pomme_par_arbre, (-550+i*1100//(nb_arbre-1),-100) , taille_pomme, taille_arbre)
            nb_pomme_restant_a_dessiner -= nb_pomme_par_arbre
        else:
            liste_objet_initiale[0][0] += dessiner_pomme_sur_arbre(nb_pomme_restant_a_dessiner, (-550+i*1100//(nb_arbre-1),-100) , taille_pomme, taille_arbre)
            nb_pomme_restant_a_dessiner = 0
    
    
    for i in range(nb_table//2):
        if nb_pasteque_restant_a_dessiner//nb_pasteque_par_table >= 1:
            liste_objet_initiale[0][1] += dessiner_pasteque_sur_table(nb_pasteque_par_table, (-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_pasteque, taille_table)
            nb_pasteque_restant_a_dessiner -= nb_pasteque_par_table
        else:
            liste_objet_initiale[0][1] += dessiner_pasteque_sur_table(nb_pasteque_restant_a_dessiner, (-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_pasteque, taille_table)
            nb_pasteque_restant_a_dessiner =0



    for i in range(nb_arbre - nb_arbre//2):
        if nb_cerise_restant_a_dessiner//nb_cerise_par_arbre >= 1:
            liste_objet_initiale[0][2] += dessiner_cerise_sur_arbre(nb_cerise_par_arbre, (-550+(nb_arbre//2+i)*1100//(nb_arbre-1),-100), taille_cerise, taille_arbre)
            nb_cerise_restant_a_dessiner -= nb_cerise_par_arbre
        else:
            liste_objet_initiale[0][2] += dessiner_cerise_sur_arbre(nb_cerise_restant_a_dessiner, (-550+(nb_arbre//2+i)*1100//(nb_arbre-1),-100), taille_cerise, taille_arbre)
            nb_cerise_restant_a_dessiner = 0

    for i in range(nb_table - nb_table//2):
        if nb_raisin_restant_a_dessiner//nb_raisin_par_arbre >= 1:
            liste_objet_initiale[0][3] += dessiner_raisin_sur_table(nb_raisin_par_arbre, (-550+(nb_table//2+i)*1100//(nb_table-1),-475+((i+1)%2)*30*nb_table), taille_raisin, taille_table)
            nb_raisin_restant_a_dessiner -= nb_raisin_par_arbre
        else:
            liste_objet_initiale[0][3] += dessiner_raisin_sur_table(nb_raisin_restant_a_dessiner, (-550+(nb_table//2+i)*1100//(nb_table-1),-475+((i+1)%2)*30*nb_table), taille_raisin, taille_table)
            nb_raisin_restant_a_dessiner = 0

        
    
    screen.update()

    return liste_objet_initiale