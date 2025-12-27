from Code.Affichage.fonction_affichage import*

def initialisation(t_background, screen, nb_raisin, nb_pasteque, nb_arbre, nb_table, taille_arbre, taille_table, taille_raisin, taille_pasteque):
    dessiner_fond(t_background, screen, nb_arbre, nb_table, taille_arbre, taille_table)

    nb_raisin_restant_a_dessiner = nb_raisin
    nb_raisin_par_arbre = nb_raisin//nb_arbre +1

    nb_pasteque_restant_a_dessiner = nb_pasteque
    nb_pasteque_par_table = nb_pasteque//nb_table +1

    liste_tortue_raisin = []
    liste_tortue_pasteque = []

    for i in range(nb_arbre):
        if nb_raisin_restant_a_dessiner//nb_raisin_par_arbre >= 1:
            liste_tortue_raisin += dessiner_raisin_sur_arbre(nb_raisin_par_arbre, (-550+i*1100//(nb_arbre-1),-100), taille_raisin, taille_arbre)
            nb_raisin_restant_a_dessiner -= nb_raisin_par_arbre
        else:
            liste_tortue_raisin += dessiner_raisin_sur_arbre(nb_raisin_restant_a_dessiner, (-550+i*1100//(nb_arbre-1),-100), taille_raisin, taille_arbre)

    
    for i in range(nb_table):
        if nb_pasteque_restant_a_dessiner//nb_pasteque_par_table >= 1:
            liste_tortue_pasteque += dessiner_pasteque_sur_table(nb_pasteque_par_table, (-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_pasteque, taille_table)
            nb_pasteque_restant_a_dessiner -= nb_pasteque_par_table
        else:
            liste_tortue_pasteque += dessiner_pasteque_sur_table(nb_pasteque_restant_a_dessiner, (-550+i*1100//(nb_table-1),-475+(i%2)*30*nb_table), taille_pasteque, taille_table)
            nb_pasteque_restant_a_dessiner =0

    return liste_tortue_raisin, liste_tortue_pasteque