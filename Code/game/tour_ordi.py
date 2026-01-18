from random import*
from time import*

from Code.game.choix_legit import*

from Code.Affichage.fonction_affichage import *


def tour_ordi(regle, liste_objet, screen):                           # Un tour pour un joueur bot
    action = False                      # definition d'une variable action pour la boucle while

    while not action:                       # action permet de verifier si le joueur a joué ou pas encore
        monde_choisi = randint(0,1)
        nb_A = liste_objet[1][2*monde_choisi]
        nb_B = liste_objet[1][2*monde_choisi+1]
        
        choix = randint(1,3)                                                    # choisi aléatoirement un choix possible
        nb_element_voulu = regle[randint(0,2)]                                  # choisi aléatoirement un nb d'élément à enlever
        cA, cB, action = choix_legit(nb_A, nb_B, choix, nb_element_voulu)       # choix_legit() il verifie que cette combinaison est possible où si il mannque des éléments de A ou de B, et il assigne les bonnes valeurs de cA et cB en fonction du choix; il modifie action à True

    for i in range(cA):
        mange = False
        while not mange:
            index = randint(0, len(liste_objet[0][2*monde_choisi])-1)
            if liste_objet[0][2*monde_choisi][index][2] == "Pas mangé":
                liste_objet[0][2*monde_choisi][index][2] = "mangé"
                mange = True
                liste_objet[3][2*monde_choisi][1]((liste_objet[0][2*monde_choisi][index][0][0], liste_objet[0][2*monde_choisi][index][0][1]-liste_objet[0][2*monde_choisi][index][3]),liste_objet[0][2*monde_choisi][index][3],liste_objet[0][2*monde_choisi][index][1])
        screen.update()
        sleep(0.5)


    for i in range(cB):
        mange = False
        while not mange:
            index = randint(0, len(liste_objet[0][2*monde_choisi+1])-1)
            if liste_objet[0][2*monde_choisi+1][index][2] == "Pas mangé":
                liste_objet[0][2*monde_choisi+1][index][2] = "mangé"
                mange = True
                liste_objet[3][2*monde_choisi+1][1]((liste_objet[0][2*monde_choisi+1][index][0][0], liste_objet[0][2*monde_choisi+1][index][0][1]-liste_objet[0][2*monde_choisi+1][index][3]),liste_objet[0][2*monde_choisi+1][index][3],liste_objet[0][2*monde_choisi+1][index][1])
        screen.update()
        sleep(0.5)


    if monde_choisi ==0:
        coup = [cA, cB,0,0]
    elif monde_choisi ==1:
        coup = [0,0, cA, cB]

    last_play = "Le bot a mangé :\n"
    for i in range(len(coup)):
        last_play += str(coup[i])+" " +liste_objet[2][i] + "\n"
        liste_objet[1][i] -= coup[i]
    
    return liste_objet, last_play