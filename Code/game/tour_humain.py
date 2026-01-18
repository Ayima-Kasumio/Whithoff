from turtle import *
from Code.Affichage.affichage_fruit_mange_tour import*
from Code.Affichage.fonction_affichage import *
from Code.game.coup_valide import *
from time import sleep


def tour_humain(t, liste_objet, screen, regle):                         # Un tour pour un joueur humain

    #liste_objet = [[[],[],[],[]] , [nb_pomme, nb_pasteque, nb_cerise, nb_raisin] , ["pomme(s)", "pastèque(s)","cerise(s)", "raisin(s)"] , [[dessiner_pomme, dessiner_pomme_mangee], [dessiner_pasteque, dessiner_pasteque_mangee], [dessiner_cerise, dessiner_cerise_mangee], [dessiner_raisin, dessiner_raisin_mangee]]]

    coup_temporaire = [0,0,0,0]
    action = False

    def fonction_onclick(x, y):
        nonlocal action
        # bouton 'Fin de tour' dessiné à (-860, -200) taille 100
        if (abs(x + 860) < 50) and (abs(y + 200) < 25):
            action = True
            return
        
        for i_fruit in range(len(liste_objet[0])):
            for i in liste_objet[0][i_fruit]:
                if ( ((x - i[0][0])**2 + (y - i[0][1])**2)**0.5 < i[3] ) or (((x - i[0][0])**2 + (y - i[0][1])**2)**0.5 < 2 * i[3]) and (y - i[0][1] < i[3]) :
                    if i[2] == "Pas mangé":
                        liste_objet[3][i_fruit][1]((i[0][0], i[0][1] - i[3]), i[3], i[1])
                        i[2] = "Mangé"
                        liste_objet[1][i_fruit] -= 1
                        coup_temporaire[i_fruit] += 1
                        break

        affichage_fruit_mange_tour(t, liste_objet, coup_temporaire)
        screen.update()


    affichage_fruit_mange_tour(t, liste_objet , coup_temporaire)

    screen.onclick(fonction_onclick)

    # attendre que l'utilisateur clique sur le bouton "Fin de tour"
    while not action:
        screen.update()
        sleep(0.01)

    # nettoyer et retourner
    screen.onclick(None)

    if coup_valide(liste_objet, coup_temporaire, regle):
        last_play = "Le Joueur a mangé :\n"
        for i in range(len(coup_temporaire)):
            last_play += str(coup_temporaire[i])+" "+liste_objet[2][i]+"\n"
    else:
        last_play = "le joueur n'a pas\nrespécté les règles"

    return liste_objet, last_play